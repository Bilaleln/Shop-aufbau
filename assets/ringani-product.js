/* ============================================================================
   RINGANI — Product page behaviour (vanilla, dependency-free)
   Custom elements auto-upgrade on Theme-Editor section reloads, so nothing
   here breaks when a section is added / removed / reordered / re-rendered.

   Elements:
     <ringani-product>    main purchase controller (variant / price / cart)
     <ringani-accordion>  generic accessible accordion (panel / specs / faq)

   Global:
     Reveal-on-scroll observer (respects prefers-reduced-motion), re-scanned
     on shopify:section:load.
   ========================================================================== */
(function () {
  'use strict';

  var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Reveal on scroll -------------------------------------------------- */
  var revealObserver = null;
  function ensureRevealObserver() {
    if (revealObserver || REDUCED || !('IntersectionObserver' in window)) return;
    revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          revealObserver.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  }
  function scanReveals(root) {
    (root || document).querySelectorAll('.ringani-reveal:not(.is-visible)').forEach(function (el) {
      if (REDUCED) { el.classList.add('is-visible'); return; }
      ensureRevealObserver();
      if (revealObserver) revealObserver.observe(el);
      else el.classList.add('is-visible');
    });
  }

  /* ---- Accordion --------------------------------------------------------- */
  var Accordion = (function () {
    function C() { return Reflect.construct(HTMLElement, [], C); }
    C.prototype = Object.create(HTMLElement.prototype);
    C.prototype.constructor = C;
    C.prototype.connectedCallback = function () {
      if (this._wired) return;
      this._wired = true;
      this._single = this.getAttribute('data-single') !== 'false';
      var self = this;
      this.addEventListener('click', function (e) {
        var head = e.target.closest('.ringani-acc__head');
        if (!head || !self.contains(head)) return;
        self.toggle(head);
      });
    };
    C.prototype.toggle = function (head) {
      var expanded = head.getAttribute('aria-expanded') === 'true';
      if (this._single && !expanded) {
        var self = this;
        this.querySelectorAll('.ringani-acc__head[aria-expanded="true"]').forEach(function (h) {
          if (h !== head) self._set(h, false);
        });
      }
      this._set(head, !expanded);
    };
    C.prototype._set = function (head, open) {
      head.setAttribute('aria-expanded', open ? 'true' : 'false');
      var panel = document.getElementById(head.getAttribute('aria-controls')) ||
        head.nextElementSibling;
      if (!panel) return;
      panel.hidden = false;
      if (open) {
        panel.style.maxHeight = panel.scrollHeight + 'px';
        panel.addEventListener('transitionend', function te() {
          if (head.getAttribute('aria-expanded') === 'true') panel.style.maxHeight = 'none';
          panel.removeEventListener('transitionend', te);
        });
      } else {
        panel.style.maxHeight = panel.scrollHeight + 'px';
        // force reflow so the transition from a fixed height runs
        void panel.offsetHeight;
        panel.style.maxHeight = '0px';
      }
    };
    if ('customElements' in window && !customElements.get('ringani-accordion')) {
      customElements.define('ringani-accordion', C);
    }
    return C;
  })();

  /* ---- Product controller ------------------------------------------------ */
  var Product = (function () {
    function C() { return Reflect.construct(HTMLElement, [], C); }
    C.prototype = Object.create(HTMLElement.prototype);
    C.prototype.constructor = C;

    C.prototype.connectedCallback = function () {
      if (this._wired) return;
      this._wired = true;
      this.sectionId = this.getAttribute('data-section-id');

      var data = this.querySelector('[data-ringani-variants]');
      try { this.variants = data ? JSON.parse(data.textContent) : []; }
      catch (e) { this.variants = []; }

      this.colorPos = parseInt(this.getAttribute('data-color-position') || '0', 10); // 1-based, 0 = none
      this.sizePos = parseInt(this.getAttribute('data-size-position') || '0', 10);
      this.optionCount = parseInt(this.getAttribute('data-option-count') || '0', 10);
      this.cartAddUrl = this.getAttribute('data-cart-add-url') || '/cart/add.js';
      this.cartUrl = this.getAttribute('data-cart-url') || '/cart';
      this.productUrl = this.getAttribute('data-product-url') || '';
      this.onAdd = this.getAttribute('data-on-add') || 'drawer';
      this.labelAdd = this.getAttribute('data-label-add') || 'In den Warenkorb';
      this.labelSoldOut = this.getAttribute('data-label-soldout') || 'Ausverkauft';
      this.labelChoose = this.getAttribute('data-label-choose') || 'Größe wählen';

      // Selected option values (index 0..optionCount-1)
      var current = this.currentVariant();
      this.selected = current ? current.options.slice() : new Array(this.optionCount).fill(null);
      // If there is a size option, start with none chosen (design requires an
      // explicit size pick before add-to-cart).
      if (this.sizePos) this.selected[this.sizePos - 1] = null;

      this.qty = 1;
      this._wireEvents();
      this.refresh();
      scanReveals(this);
    };

    C.prototype._wireEvents = function () {
      var self = this;
      this.addEventListener('click', function (e) {
        var swatch = e.target.closest('[data-ringani-swatch]');
        if (swatch) { self.pick(self.colorPos, swatch.getAttribute('data-value')); return; }
        var size = e.target.closest('[data-ringani-size]');
        if (size) {
          if (size.hasAttribute('disabled') || size.getAttribute('aria-disabled') === 'true') return;
          self.pick(self.sizePos, size.getAttribute('data-value')); return;
        }
        var thumb = e.target.closest('[data-ringani-thumb]');
        if (thumb) { self.showMedia(thumb.getAttribute('data-media-id')); return; }
        if (e.target.closest('[data-ringani-inc]')) { self.setQty(self.qty + 1); return; }
        if (e.target.closest('[data-ringani-dec]')) { self.setQty(self.qty - 1); return; }
        if (e.target.closest('[data-ringani-sizeguide-open]')) { self.sizeGuide(true); return; }
        if (e.target.closest('[data-ringani-sizeguide-close]') ||
            e.target.hasAttribute('data-ringani-overlay')) { self.sizeGuide(false); return; }
      });
      // Non-color/size options fall back to native selects.
      this.querySelectorAll('[data-ringani-option-select]').forEach(function (sel) {
        sel.addEventListener('change', function () {
          self.pick(parseInt(sel.getAttribute('data-position'), 10), sel.value);
        });
      });
      // Add-to-cart forms (main + sticky share one variant state).
      this.querySelectorAll('form[data-ringani-form]').forEach(function (form) {
        form.addEventListener('submit', function (e) { self.submit(e, form); });
      });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') self.sizeGuide(false);
      });
    };

    C.prototype.currentVariant = function () {
      var self = this;
      return this.variants.find(function (v) {
        return v.options.every(function (o, i) {
          return self.selected == null || self.selected[i] == null || self.selected[i] === o;
        });
      }) || null;
    };

    C.prototype.matchedVariant = function () {
      // Fully-specified match (all options chosen).
      var self = this;
      if (this.selected.some(function (o) { return o == null; })) return null;
      return this.variants.find(function (v) {
        return v.options.every(function (o, i) { return o === self.selected[i]; });
      }) || null;
    };

    C.prototype.pick = function (position, value) {
      if (!position) return;
      this.selected[position - 1] = value;
      this.refresh();
    };

    C.prototype.setQty = function (n) {
      this.qty = Math.max(1, Math.min(99, n | 0));
      this.querySelectorAll('[data-ringani-qty]').forEach(function (el) { el.textContent = this.qty; }, this);
      this.querySelectorAll('input[name="quantity"]').forEach(function (el) { el.value = this.qty; }, this);
    };

    C.prototype.variantAvailableFor = function (position, value) {
      // Is there an available variant with this option value, honouring the
      // other currently-selected options (ignoring this position)?
      var self = this;
      return this.variants.some(function (v) {
        if (!v.available) return false;
        if (v.options[position - 1] !== value) return false;
        return v.options.every(function (o, i) {
          if (i === position - 1) return true;
          var sel = self.selected[i];
          return sel == null || sel === o;
        });
      });
    };

    C.prototype.refresh = function () {
      var self = this;
      // Colour swatches selected state
      this.querySelectorAll('[data-ringani-swatch]').forEach(function (el) {
        var on = self.colorPos && el.getAttribute('data-value') === self.selected[self.colorPos - 1];
        el.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
      var colorLabel = this.querySelector('[data-ringani-color-name]');
      if (colorLabel && self.colorPos) colorLabel.textContent = self.selected[self.colorPos - 1] || '';

      // Size buttons: availability depends on the chosen colour.
      this.querySelectorAll('[data-ringani-size]').forEach(function (el) {
        var value = el.getAttribute('data-value');
        var ok = self.variantAvailableFor(self.sizePos, value);
        el.toggleAttribute('disabled', !ok);
        el.setAttribute('aria-disabled', ok ? 'false' : 'true');
        var chosen = self.selected[self.sizePos - 1] === value;
        el.setAttribute('aria-pressed', chosen ? 'true' : 'false');
      });

      // Fallback selects
      this.querySelectorAll('[data-ringani-option-select]').forEach(function (sel) {
        var pos = parseInt(sel.getAttribute('data-position'), 10);
        if (self.selected[pos - 1] != null) sel.value = self.selected[pos - 1];
      });

      var matched = this.matchedVariant();
      var display = matched || this.currentVariant();

      // Price
      if (display) {
        this.setText('[data-ringani-price]', display.price);
        var compareEl = this.querySelectorAll('[data-ringani-compare]');
        var saveEl = this.querySelectorAll('[data-ringani-save]');
        if (display.compare_at_price_raw > display.price_raw) {
          compareEl.forEach(function (el) { el.textContent = display.compare_at_price; el.hidden = false; });
          saveEl.forEach(function (el) { el.textContent = self.savingsText(display); el.hidden = false; });
        } else {
          compareEl.forEach(function (el) { el.hidden = true; });
          saveEl.forEach(function (el) { el.hidden = true; });
        }
      }

      // Size hint
      var hint = this.querySelector('[data-ringani-size-hint]');
      if (hint) {
        var chosenSize = self.sizePos ? self.selected[self.sizePos - 1] : null;
        hint.textContent = chosenSize
          ? (hint.getAttribute('data-chosen-prefix') || 'Größe') + ' ' + chosenSize
          : (hint.getAttribute('data-default') || '');
      }
      var badge = this.querySelector('[data-ringani-size-badge]');
      if (badge) badge.setAttribute('data-active', (self.sizePos && self.selected[self.sizePos - 1]) ? 'true' : 'false');

      // Sticky summary
      var summary = this.querySelector('[data-ringani-sticky-summary]');
      if (summary) {
        var parts = [];
        if (self.sizePos) parts.push(self.selected[self.sizePos - 1] ? 'Größe ' + self.selected[self.sizePos - 1] : self.labelChoose);
        if (self.colorPos && self.selected[self.colorPos - 1]) parts.push(self.selected[self.colorPos - 1]);
        if (display) parts.push(display.price);
        summary.textContent = parts.join(' · ');
      }

      // CTA state
      var needSize = self.sizePos && !self.selected[self.sizePos - 1];
      var soldOut = matched ? !matched.available : (!needSize);
      var label, disabled = false;
      if (needSize) { label = self.labelChoose; }
      else if (!matched || !matched.available) { label = self.labelSoldOut; disabled = true; }
      else { label = self.labelAdd; }
      this.querySelectorAll('[data-ringani-cta-label]').forEach(function (el) { el.textContent = label; });
      this.querySelectorAll('[data-ringani-submit]').forEach(function (btn) {
        // Not disabled when a size still needs choosing: clicking scrolls +
        // opens the size guide (mirrors the design behaviour).
        btn.disabled = disabled;
      });
      this.querySelectorAll('input[name="id"]').forEach(function (el) { if (matched) el.value = matched.id; });

      // Variant image + URL
      if (matched) {
        if (matched.featured_media_id) this.showMedia(String(matched.featured_media_id), true);
        this.updateUrl(matched.id);
      }
      this._matched = matched;
      this._needSize = needSize;
    };

    C.prototype.savingsText = function (v) {
      var tmpl = this.getAttribute('data-save-template') || 'Du sparst {amount}';
      return tmpl.replace('{amount}', v.savings);
    };

    C.prototype.setText = function (sel, text) {
      this.querySelectorAll(sel).forEach(function (el) { el.textContent = text; });
    };

    C.prototype.showMedia = function (mediaId, quiet) {
      var stage = this.querySelector('[data-ringani-gallery]');
      if (!stage || !mediaId) return;
      var found = false;
      stage.querySelectorAll('[data-media-id]').forEach(function (m) {
        var on = m.getAttribute('data-media-id') === mediaId;
        if (on) found = true;
        m.style.opacity = on ? '1' : '0';
        m.style.pointerEvents = on ? 'auto' : 'none';
      });
      if (found) {
        this.querySelectorAll('[data-ringani-thumb]').forEach(function (t) {
          t.setAttribute('aria-current', t.getAttribute('data-media-id') === mediaId ? 'true' : 'false');
        });
      }
    };

    C.prototype.updateUrl = function (variantId) {
      if (!this.productUrl || !window.history || !window.history.replaceState) return;
      try {
        var url = new URL(window.location.href);
        url.searchParams.set('variant', variantId);
        window.history.replaceState({}, '', url.toString());
      } catch (e) {}
    };

    C.prototype.sizeGuide = function (open) {
      var modal = document.getElementById('ringani-sizeguide-' + this.sectionId);
      var overlay = document.getElementById('ringani-overlay-' + this.sectionId);
      if (!modal) return;
      modal.setAttribute('data-open', open ? 'true' : 'false');
      if (overlay) overlay.setAttribute('data-open', open ? 'true' : 'false');
      document.documentElement.style.overflow = open ? 'hidden' : '';
      if (open) { var c = modal.querySelector('[data-ringani-sizeguide-close]'); if (c) c.focus(); }
    };

    C.prototype.submit = function (e, form) {
      // No size chosen yet → guide the customer instead of a dead click.
      if (this._needSize) {
        e.preventDefault();
        this.sizeGuide(true);
        var anchor = document.getElementById(this.getAttribute('data-scroll-anchor') || '');
        if (anchor) anchor.scrollIntoView({ behavior: REDUCED ? 'auto' : 'smooth', block: 'start' });
        return;
      }
      if (!this._matched || !this._matched.available) { e.preventDefault(); return; }
      e.preventDefault();

      var self = this;
      var body = new FormData(form);
      body.set('quantity', String(this.qty));
      var sections = this.themeSections();
      if (sections) { body.set('sections', sections.join(',')); body.set('sections_url', window.location.pathname); }

      this.querySelectorAll('[data-ringani-submit]').forEach(function (b) { b.setAttribute('data-loading', 'true'); });

      fetch(this.cartAddUrl, {
        method: 'POST',
        headers: { 'Accept': 'application/javascript', 'X-Requested-With': 'XMLHttpRequest' },
        body: body
      })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, data: j }; }); })
        .then(function (res) {
          self.querySelectorAll('[data-ringani-submit]').forEach(function (b) { b.removeAttribute('data-loading'); });
          if (!res.ok) { self.cartError(res.data && res.data.description); return; }
          self.afterAdd(res.data);
        })
        .catch(function () {
          self.querySelectorAll('[data-ringani-submit]').forEach(function (b) { b.removeAttribute('data-loading'); });
          // Network fallback: let the browser do a real form POST.
          form.submit();
        });
    };

    // Section ids the theme's cart UI needs re-rendered (Dawn conventions).
    C.prototype.themeSections = function () {
      var ids = [];
      if (document.querySelector('cart-drawer')) ids.push('cart-drawer');
      else if (document.querySelector('cart-notification')) ids.push('cart-notification');
      if (document.getElementById('cart-icon-bubble') ||
          document.querySelector('.shopify-section [id^="cart-icon-bubble"]')) ids.push('cart-icon-bubble');
      return ids.length ? ids : null;
    };

    C.prototype.afterAdd = function (data) {
      // 1) Broad, theme-agnostic notifications.
      document.dispatchEvent(new CustomEvent('cart:refresh', { bubbles: true }));
      document.dispatchEvent(new CustomEvent('cart:build', { bubbles: true }));
      if (window.Shopify && window.Shopify.designMode) { /* editor: no redirect */ }

      // 2) Dawn-compatible cart drawer / notification integration.
      var drawer = document.querySelector('cart-drawer');
      var notification = document.querySelector('cart-notification');
      var rendered = data && data.sections;
      var self = this;
      if (rendered) {
        this.replaceSection('cart-icon-bubble', rendered['cart-icon-bubble']);
        if (drawer && rendered['cart-drawer']) {
          this.replaceSection('cart-drawer', rendered['cart-drawer']);
          if (typeof drawer.open === 'function') { drawer.open(); return; }
          drawer.classList.remove('is-empty');
          drawer.classList.add('active', 'animate');
          drawer.removeAttribute('inert'); drawer.setAttribute('aria-hidden', 'false');
          return;
        }
        if (notification && rendered['cart-notification']) {
          this.replaceSection('cart-notification', rendered['cart-notification']);
          if (typeof notification.renderContents === 'function') { notification.renderContents(data); return; }
        }
      }

      // 3) Configurable fallback when no theme drawer is detected.
      this.refreshBubble();
      if (this.onAdd === 'cart') window.location.href = this.cartUrl;
      else this.toast(this.getAttribute('data-added-msg') || 'Zum Warenkorb hinzugefügt');
    };

    C.prototype.replaceSection = function (id, html) {
      if (!html) return;
      var target = document.getElementById('shopify-section-' + id) ||
        document.getElementById(id) ||
        document.querySelector('#shopify-section-' + id);
      if (!target) return;
      // Extract matching inner content when possible, else replace whole node.
      var tmp = document.createElement('div');
      tmp.innerHTML = html;
      var src = tmp.querySelector('#shopify-section-' + id) || tmp.firstElementChild || tmp;
      target.innerHTML = (src.id ? src.innerHTML : tmp.innerHTML);
    };

    C.prototype.refreshBubble = function () {
      fetch(this.cartUrl + '.js', { headers: { 'Accept': 'application/json' } })
        .then(function (r) { return r.json(); })
        .then(function (cart) {
          document.querySelectorAll('[data-ringani-cart-count]').forEach(function (el) {
            el.textContent = cart.item_count;
          });
        }).catch(function () {});
    };

    C.prototype.cartError = function (msg) {
      this.toast(msg || 'Hinzufügen nicht möglich.');
    };

    C.prototype.toast = function (msg) {
      var t = document.createElement('div');
      t.className = 'ringani-toast';
      t.setAttribute('role', 'status');
      t.textContent = msg;
      document.body.appendChild(t);
      requestAnimationFrame(function () { t.setAttribute('data-show', 'true'); });
      setTimeout(function () { t.removeAttribute('data-show'); setTimeout(function () { t.remove(); }, 300); }, 2600);
    };

    if ('customElements' in window && !customElements.get('ringani-product')) {
      customElements.define('ringani-product', C);
    }
    return C;
  })();

  /* ---- Sticky bar visibility -------------------------------------------- */
  function initSticky(root) {
    (root || document).querySelectorAll('[data-ringani-sticky]').forEach(function (bar) {
      if (bar._wired) return; bar._wired = true;
      var anchorSel = bar.getAttribute('data-anchor');
      var anchor = anchorSel ? document.querySelector(anchorSel) : null;
      var footer = document.querySelector('footer, [data-ringani-final]');
      function update() {
        var pastHero = anchor ? anchor.getBoundingClientRect().bottom < 40 : window.scrollY > 700;
        var nearEnd = footer ? footer.getBoundingClientRect().top < window.innerHeight : false;
        bar.setAttribute('data-visible', (pastHero && !nearEnd) ? 'true' : 'false');
      }
      window.addEventListener('scroll', function () {
        if (bar._raf) return;
        bar._raf = requestAnimationFrame(function () { bar._raf = null; update(); });
      }, { passive: true });
      update();
    });
  }

  /* ---- Boot + Theme Editor lifecycle ------------------------------------ */
  function boot(root) { scanReveals(root); initSticky(root); }
  if (document.readyState !== 'loading') boot(document);
  else document.addEventListener('DOMContentLoaded', function () { boot(document); });

  document.addEventListener('shopify:section:load', function (e) { boot(e.target); });
  document.addEventListener('shopify:section:select', function (e) {
    var bar = e.target.querySelector('[data-ringani-sticky]');
    if (bar) bar.setAttribute('data-visible', 'true');
  });
})();
