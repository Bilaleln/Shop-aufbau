const { chromium, devices } = require('playwright');
(async () => {
  const out = process.argv[2];
  const b = await chromium.launch();
  const T = 'preview_theme_id=190902337916';
  const pages = [['pdp', `https://fadilal.com/products/fadilal-warm-oil-candle?${T}`], ['home', `https://fadilal.com/?${T}`]];
  const report = [];
  for (const [vp, opts] of [['desktop', { viewport: { width: 1440, height: 900 } }], ['mobile', devices['iPhone 13']]]) {
    const ctx = await b.newContext(opts);
    for (const [name, url] of pages) {
      const p = await ctx.newPage(); const errs = []; const bad = [];
      p.on('pageerror', e => errs.push(e.message));
      p.on('response', r => { if (r.status() >= 400 && /cdn\.shopify|fadilal/.test(r.url())) bad.push(r.status() + ' ' + r.url().slice(0, 120)); });
      await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
      await p.waitForTimeout(4000);
      const title = await p.title();
      // scroll to trigger lazy images
      const h = await p.evaluate(() => document.body.scrollHeight);
      for (let y = 0; y < h; y += 700) { await p.evaluate(y => window.scrollTo(0, y), y); await p.waitForTimeout(250); }
      await p.evaluate(() => window.scrollTo(0, 0)); await p.waitForTimeout(800);
      const info = await p.evaluate(() => {
        const imgs = [...document.images];
        return { total: imgs.length, newAssets: imgs.filter(i => /fadilal-(wildrose|how-to|evening|campaign)/.test(i.currentSrc || i.src)).length,
          broken: imgs.filter(i => i.complete && i.naturalWidth === 0 && (i.currentSrc||i.src)).map(i => (i.currentSrc||i.src).slice(0,100)).slice(0,5),
          placeholders: document.querySelectorAll('svg.placeholder-svg, .placeholder-svg').length,
          hscroll: document.documentElement.scrollWidth > window.innerWidth + 1, videos: document.querySelectorAll('video').length };
      });
      await p.screenshot({ path: `${out}/${name}-${vp}.png`, fullPage: true });
      report.push({ name, vp, title, ...info, pageErrors: errs.slice(0, 5), http4xx: bad.slice(0, 5) });
      await p.close();
    }
    await ctx.close();
  }
  console.log(JSON.stringify(report, null, 1)); await b.close();
})();
