const { chromium, devices } = require('playwright');
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext(devices['iPhone 13']); const p = await ctx.newPage();
  const errs=[]; p.on('pageerror', e => errs.push(e.message));
  await p.goto('https://fadilal.com/products/fadilal-warm-oil-candle?preview_theme_id=190902337916', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await p.waitForTimeout(3000);
  await p.evaluate(() => document.querySelectorAll('#shopify-pc__banner, #preview-bar-iframe').forEach(e => e.remove()));
  const r = {};
  // variant switch
  const prov = p.locator('label:has-text("Provence"), button:has-text("Provence")').first();
  await prov.click({ timeout: 8000 }).catch(e => r.variantClickErr = e.message.slice(0,80));
  await p.waitForTimeout(800);
  r.urlAfterVariant = p.url().split('?')[1];
  // gallery video
  r.galleryVideoEls = await p.evaluate(() => document.querySelectorAll('video, [data-media-type="video"], deferred-media, .product__media--video, [data-type="video"]').length);
  r.videoSrcs = await p.evaluate(() => [...document.querySelectorAll('video source, video')].map(v => (v.src||v.currentSrc||'').slice(0,90)).filter(Boolean).slice(0,3));
  // add to cart
  const before = await p.evaluate(async () => (await (await fetch('/cart.js')).json()).item_count);
  await p.locator('form[action*="/cart/add"] button[type="submit"], button[name="add"]').first().click({ timeout: 8000 }).catch(e => r.atcErr = e.message.slice(0,80));
  await p.waitForTimeout(2500);
  const cart = await p.evaluate(async () => (await (await fetch('/cart.js')).json()));
  r.cartBefore = before; r.cartAfter = cart.item_count; r.cartVariant = cart.items.map(i => i.variant_title);
  r.pageErrors = errs.slice(0,3);
  console.log(JSON.stringify(r, null, 1)); await b.close();
})();
