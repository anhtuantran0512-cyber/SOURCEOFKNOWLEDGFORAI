---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/saas-product-mega-footer-with-resource-grid/"
title: "SaaS Product Mega Footer with Resource Grid"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "The big-surface SaaS footer: a promoted resource rail of three real content cards sitting above six link columns, so the last screen of the page does…"
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Product Mega Footer with Resource Grid
Source: https://codefronts.com/layouts/css-footer-designs/saas-product-mega-footer-with-resource-grid/

The big-surface SaaS footer: a promoted resource rail of three real content cards sitting above six link columns, so the last screen of the page does conversion work instead of just listing URLs. Named grid areas keep the whole arrangement readable, and the mobile order is declared, not accidental.
## HTML
```html
<section class="ft-03" aria-label="SaaS mega footer with resource grid demo">
  <main class="ft-03__main">
    <p class="ft-03__eyebrow">grid-template-areas · mega footer</p>
    <h1 class="ft-03__title">The last screen should still sell</h1>
    <p class="ft-03__sub">A promoted resource rail above the link columns turns dead footer space into the second-best converting block on a SaaS page.</p>
  </main>
  <footer class="ft-03__foot">
    <div class="ft-03__mega">
      <section class="ft-03__promo" aria-labelledby="ft-03-ph">
        <div class="ft-03__promohead">
          <h2 class="ft-03__h2" id="ft-03-ph">From the library</h2>
          <a class="ft-03__all" href="#ft-03-a">Browse all 214 resources<span aria-hidden="true"> →</span></a>
        </div>
        <ul class="ft-03__cards">
          <li class="ft-03__card">
            <div class="ft-03__thumb" style="--ft-03-img:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=640&amp;q=70&amp;auto=format&amp;fit=crop')"></div>
            <p class="ft-03__cat">Benchmark report</p>
            <h3 class="ft-03__ch"><a class="ft-03__clink" href="#ft-03-a">The 2026 State of Deployment Frequency</a></h3>
            <p class="ft-03__cmeta">18 min read · updated March</p>
          </li>
          <li class="ft-03__card">
            <div class="ft-03__thumb" style="--ft-03-img:url('https://images.unsplash.com/photo-1552664730-d307ca884978?w=640&amp;q=70&amp;auto=format&amp;fit=crop')"></div>
            <p class="ft-03__cat">Playbook</p>
            <h3 class="ft-03__ch"><a class="ft-03__clink" href="#ft-03-a">Migrating 40 services without a freeze window</a></h3>
            <p class="ft-03__cmeta">Guide · 6 chapters</p>
          </li>
          <li class="ft-03__card">
            <div class="ft-03__thumb" style="--ft-03-img:url('https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=640&amp;q=70&amp;auto=format&amp;fit=crop')"></div>
            <p class="ft-03__cat">Webinar</p>
            <h3 class="ft-03__ch"><a class="ft-03__clink" href="#ft-03-a">Cutting build minutes by 62%: a live teardown</a></h3>
            <p class="ft-03__cmeta">On demand · 42 min</p>
          </li>
        </ul>
      </section>
      <div class="ft-03__links">
        <nav class="ft-03__col" aria-labelledby="ft-03-c1"><h2 class="ft-03__ch3" id="ft-03-c1">Platform</h2><ul class="ft-03__list"><li><a class="ft-03__link" href="#ft-03-a">Pipelines</a></li><li><a class="ft-03__link" href="#ft-03-a">Environments</a></li><li><a class="ft-03__link" href="#ft-03-a">Secrets</a></li><li><a class="ft-03__link" href="#ft-03-a">Observability</a></li><li><a class="ft-03__link" href="#ft-03-a">Rollbacks</a></li></ul></nav>
        <nav class="ft-03__col" aria-labelledby="ft-03-c2"><h2 class="ft-03__ch3" id="ft-03-c2">Developers</h2><ul class="ft-03__list"><li><a class="ft-03__link" href="#ft-03-a">Docs</a></li><li><a class="ft-03__link" href="#ft-03-a">CLI</a></li><li><a class="ft-03__link" href="#ft-03-a">API reference</a></li><li><a class="ft-03__link" href="#ft-03-a">SDKs</a></li><li><a class="ft-03__link" href="#ft-03-a">Status</a></li></ul></nav>
        <nav class="ft-03__col" aria-labelledby="ft-03-c3"><h2 class="ft-03__ch3" id="ft-03-c3">Solutions</h2><ul class="ft-03__list"><li><a class="ft-03__link" href="#ft-03-a">Startups</a></li><li><a class="ft-03__link" href="#ft-03-a">Enterprise</a></li><li><a class="ft-03__link" href="#ft-03-a">Regulated industries</a></li><li><a class="ft-03__link" href="#ft-03-a">Migrations</a></li></ul></nav>
        <nav class="ft-03__col" aria-labelledby="ft-03-c4"><h2 class="ft-03__ch3" id="ft-03-c4">Company</h2><ul class="ft-03__list"><li><a class="ft-03__link" href="#ft-03-a">About</a></li><li><a class="ft-03__link" href="#ft-03-a">Customers</a></li><li><a class="ft-03__link" href="#ft-03-a">Careers</a></li><li><a class="ft-03__link" href="#ft-03-a">Newsroom</a></li></ul></nav>
        <nav class="ft-03__col" aria-labelledby="ft-03-c5"><h2 class="ft-03__ch3" id="ft-03-c5">Compare</h2><ul class="ft-03__list"><li><a class="ft-03__link" href="#ft-03-a">vs. self-hosted</a></li><li><a class="ft-03__link" href="#ft-03-a">vs. in-house CI</a></li><li><a class="ft-03__link" href="#ft-03-a">Migration cost</a></li></ul></nav>
        <nav class="ft-03__col" aria-labelledby="ft-03-c6"><h2 class="ft-03__ch3" id="ft-03-c6">Support</h2><ul class="ft-03__list"><li><a class="ft-03__link" href="#ft-03-a">Help centre</a></li><li><a class="ft-03__link" href="#ft-03-a">Community</a></li><li><a class="ft-03__link" href="#ft-03-a">Professional services</a></li><li><a class="ft-03__link" href="#ft-03-a">Contact sales</a></li></ul></nav>
      </div>
      <div class="ft-03__legal">
        <div class="ft-03__brand"><span class="ft-03__mark" aria-hidden="true"></span>Ferrite</div>
        <p class="ft-03__copy">© <time datetime="2026">2026</time> Ferrite, Inc. · SOC 2 Type II · Data resident in eu-west-1</p>
        <ul class="ft-03__legallinks"><li><a class="ft-03__slink" href="#ft-03-a">Privacy</a></li><li><a class="ft-03__slink" href="#ft-03-a">Terms</a></li><li><a class="ft-03__slink" href="#ft-03-a">DPA</a></li><li><a class="ft-03__slink" href="#ft-03-a">Sub-processors</a></li></ul>
      </div>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-03-bg);
  --ft-03-bg: oklch(0.18 0.022 265);
  --ft-03-foot: oklch(0.15 0.02 265);
  --ft-03-surface: oklch(0.22 0.024 265);
  --ft-03-ink: oklch(0.97 0.005 265);
  --ft-03-mut: oklch(0.72 0.017 265);
  --ft-03-dim: oklch(0.6 0.017 265);
  --ft-03-acc: oklch(0.78 0.17 155);
  --ft-03-line: oklch(0.97 0.005 265/.12);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-03-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-03 *,
.ft-03 *::before,
.ft-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-03 ul {
  list-style: none;
}

.ft-03__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(44px,9vh,96px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1280px)/2));
  background: radial-gradient(80% 60% at 80% 0%,oklch(0.28 0.06 165/.5),transparent);
}

.ft-03__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ft-03-acc);
}

.ft-03__title {
  font-size: clamp(30px,5.5vw,60px);
  line-height: 1.02;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 14ch;
  text-wrap: balance;
}

.ft-03__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-03-mut);
  max-width: 54ch;
  text-wrap: pretty;
}

.ft-03__foot {
  background: var(--ft-03-foot);
  border-top: 1px solid var(--ft-03-line);
}

.ft-03__mega {
  display: grid;
  grid-template-areas: 'promo' 'links' 'legal';
  gap: clamp(32px,4.5vw,56px);
  padding-block: clamp(38px,6vw,68px) 0;
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1280px)/2));
}

.ft-03__promo {
  grid-area: promo;
  display: grid;
  gap: 18px;
}

.ft-03__promohead {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 10px 20px;
}

.ft-03__h2 {
  font-size: clamp(18px,2vw,22px);
  font-weight: 680;
  letter-spacing: -.02em;
}

.ft-03__all {
  margin-inline-start: auto;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--ft-03-acc);
  text-decoration: none;
  padding: 8px 2px;
  transition: opacity .18s ease;
}

.ft-03__all:hover {
  opacity: .75;
}

.ft-03__cards {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(15rem,100%),1fr));
  gap: clamp(14px,1.6vw,20px);
}

.ft-03__card {
  position: relative;
  display: grid;
  align-content: start;
  gap: 8px;
  padding: 14px;
  border-radius: 16px;
  background: var(--ft-03-surface);
  border: 1px solid var(--ft-03-line);
  transition: transform .3s cubic-bezier(.2,.8,.2,1),background .3s ease;
}

.ft-03__card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(140deg,var(--ft-03-acc),transparent 62%);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask-composite: exclude;
  opacity: 0;
  transition: opacity .3s ease;
  pointer-events: none;
}

.ft-03__card:hover {
  transform: translateY(-3px);
}

.ft-03__card:hover::before,
.ft-03__card:focus-within::before {
  opacity: 1;
}

.ft-03__cards:has(.ft-03__card:hover) .ft-03__card:not(:hover) {
  opacity: .62;
}

.ft-03__thumb {
  aspect-ratio: 16/9;
  border-radius: 10px;
  background-image: var(--ft-03-img),linear-gradient(140deg,oklch(0.42 0.09 165),oklch(0.3 0.05 265));
  background-size: cover;
  background-position: center;
  filter: saturate(.85) contrast(1.03);
}

.ft-03__cat {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ft-03-acc);
  margin-block-start: 4px;
}

.ft-03__ch {
  font-size: 15.5px;
  line-height: 1.32;
  font-weight: 640;
  letter-spacing: -.015em;
  text-wrap: balance;
}

.ft-03__clink {
  color: inherit;
  text-decoration: none;
}

.ft-03__clink::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
}

.ft-03__clink:focus-visible::after {
  outline: 2px solid var(--ft-03-acc);
  outline-offset: 3px;
}

.ft-03__cmeta {
  font-size: 12.5px;
  color: var(--ft-03-dim);
}

.ft-03__links {
  grid-area: links;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(9.5rem,1fr));
  gap: clamp(24px,3vw,36px) clamp(16px,2vw,28px);
  padding-block-start: clamp(24px,3vw,36px);
  border-top: 1px solid var(--ft-03-line);
}

.ft-03__col {
  display: grid;
  align-content: start;
  gap: 4px;
  min-width: 0;
}

.ft-03__ch3 {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ft-03-ink);
  margin-block-end: 8px;
}

.ft-03__list {
  display: grid;
  gap: 1px;
}

.ft-03__link {
  display: inline-flex;
  align-items: center;
  min-height: 34px;
  font-size: 14px;
  color: var(--ft-03-mut);
  text-decoration: none;
  width: fit-content;
  transition: color .18s ease,translate .18s ease;
}

.ft-03__link:hover {
  color: var(--ft-03-acc);
  translate: 3px 0;
}

.ft-03__link:focus-visible,
.ft-03__slink:focus-visible,
.ft-03__all:focus-visible {
  outline: 2px solid var(--ft-03-acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.ft-03__legal {
  grid-area: legal;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px 22px;
  padding-block: 20px;
  padding-bottom: calc(20px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-03-line);
}

.ft-03__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.ft-03__mark {
  width: 20px;
  height: 20px;
  border-radius: 6px;
  background: linear-gradient(140deg,var(--ft-03-acc),oklch(0.68 0.15 200));
  box-shadow: 0 0 18px -4px var(--ft-03-acc);
}

.ft-03__copy {
  font-size: 12.5px;
  color: var(--ft-03-dim);
}

.ft-03__legallinks {
  display: flex;
  flex-wrap: wrap;
  gap: 2px 4px;
  margin-inline-start: auto;
}

.ft-03__slink {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 10px;
  border-radius: 8px;
  font-size: 13px;
  color: var(--ft-03-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.ft-03__slink:hover {
  color: var(--ft-03-ink);
  background: oklch(0.97 0.005 265/.07);
}

@media (min-width: 62rem) {
  .ft-03__mega {
    grid-template-areas: 'promo' 'links' 'legal';
  }
}

@media (max-width: 520px) {
  .ft-03__legallinks {
    margin-inline-start: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-03 * {
    transition-duration: .01ms !important;
  }
}
```
