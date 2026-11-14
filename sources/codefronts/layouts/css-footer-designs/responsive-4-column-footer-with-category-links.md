---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/responsive-4-column-footer-with-category-links/"
title: "Responsive 4-Column Footer with Category Links"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "The workhorse site footer: four labelled link categories that reflow from 4 → 2 → 1 columns without a single media query, using one repeat(auto-fit,…"
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive 4-Column Footer with Category Links
Source: https://codefronts.com/layouts/css-footer-designs/responsive-4-column-footer-with-category-links/

The workhorse site footer: four labelled link categories that reflow from 4 → 2 → 1 columns without a single media query, using one repeat(auto-fit, minmax()) track definition. The markup is the accessible version most templates get wrong — each category is its own <nav> named by its own visible heading, so screen-reader users can jump straight to Support instead of wading through forty links.
## HTML
```html
<section class="ft-02" aria-label="Responsive four column footer demo">
  <main class="ft-02__main">
    <p class="ft-02__eyebrow">repeat(auto-fit, minmax(11rem, 1fr))</p>
    <h1 class="ft-02__title">Four columns that fold themselves</h1>
    <p class="ft-02__sub">Drag the frame narrower. The category grid steps 4 → 3 → 2 → 1 with no media query in the stylesheet — the breakpoints are wherever the words stop fitting.</p>
  </main>
  <footer class="ft-02__foot">
    <div class="ft-02__inner">
      <div class="ft-02__cols">
        <div class="ft-02__brandcol">
          <div class="ft-02__brand"><span class="ft-02__mark" aria-hidden="true"></span>Northwind</div>
          <p class="ft-02__blurb">Field-tested tooling for teams who ship on Fridays. Built in Dublin, used in 78 countries.</p>
          <p class="ft-02__badge">Trusted by 12,400 teams</p>
        </div>
        <nav class="ft-02__col" aria-labelledby="ft-02-h1">
          <h2 class="ft-02__h" id="ft-02-h1">Product</h2>
          <ul class="ft-02__list">
            <li><a class="ft-02__link" href="#ft-02-a">Overview</a></li>
            <li><a class="ft-02__link" href="#ft-02-a">Integrations</a></li>
            <li><a class="ft-02__link" href="#ft-02-a">Automations</a></li>
            <li><a class="ft-02__link" href="#ft-02-a">Pricing</a></li>
            <li><a class="ft-02__link" href="#ft-02-a">Changelog <span class="ft-02__pill">New</span></a></li>
          </ul>
        </nav>
        <nav class="ft-02__col" aria-labelledby="ft-02-h2">
          <h2 class="ft-02__h" id="ft-02-h2">Solutions</h2>
          <ul class="ft-02__list">
            <li><a class="ft-02__link" href="#ft-02-a">For engineering</a></li>
            <li><a class="ft-02__link" href="#ft-02-a">For marketing</a></li>
            <li><a class="ft-02__link" href="#ft-02-a">For agencies</a></li>
            <li><a class="ft-02__link" href="#ft-02-a">Enterprise</a></li>
          </ul>
        </nav>
        <nav class="ft-02__col" aria-labelledby="ft-02-h3">
          <h2 class="ft-02__h" id="ft-02-h3">Resources</h2>
          <ul class="ft-02__list">
            <li><a class="ft-02__link" href="#ft-02-a">Documentation</a></li>
            <li><a class="ft-02__link" href="#ft-02-a">API reference</a></li>
            <li><a class="ft-02__link" href="#ft-02-a">Guides</a></li>
            <li><a class="ft-02__link" href="#ft-02-a">Community</a></li>
          </ul>
        </nav>
        <nav class="ft-02__col" aria-labelledby="ft-02-h4">
          <h2 class="ft-02__h" id="ft-02-h4">Company</h2>
          <ul class="ft-02__list">
            <li><a class="ft-02__link" href="#ft-02-a">About</a></li>
            <li><a class="ft-02__link" href="#ft-02-a">Careers <span class="ft-02__pill">7</span></a></li>
            <li><a class="ft-02__link" href="#ft-02-a">Press kit</a></li>
            <li><a class="ft-02__link" href="#ft-02-a">Contact</a></li>
          </ul>
        </nav>
      </div>
      <div class="ft-02__bar">
        <p class="ft-02__copy">© <time datetime="2026">2026</time> Northwind Systems Ltd.</p>
        <ul class="ft-02__legal">
          <li><a class="ft-02__slink" href="#ft-02-a">Privacy</a></li>
          <li><a class="ft-02__slink" href="#ft-02-a">Terms</a></li>
          <li><a class="ft-02__slink" href="#ft-02-a">Cookies</a></li>
          <li><a class="ft-02__slink" href="#ft-02-a">Accessibility</a></li>
        </ul>
      </div>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-02-bg);
  --ft-02-bg: oklch(0.975 0.005 250);
  --ft-02-ink: oklch(0.21 0.03 265);
  --ft-02-mut: oklch(0.54 0.02 265);
  --ft-02-acc: oklch(0.52 0.15 195);
  --ft-02-line: oklch(0.21 0.03 265/.1);
  --ft-02-foot: oklch(0.99 0.003 250);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-02-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-02 *,
.ft-02 *::before,
.ft-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-02 ul {
  list-style: none;
}

.ft-02__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(44px,9vh,96px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1240px)/2));
}

.ft-02__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ft-02-acc);
}

.ft-02__title {
  font-size: clamp(30px,5.5vw,58px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 15ch;
  text-wrap: balance;
}

.ft-02__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-02-mut);
  max-width: 58ch;
  text-wrap: pretty;
}

.ft-02__foot {
  background: var(--ft-02-foot);
  border-top: 1px solid var(--ft-02-line);
  container-type: inline-size;
  container-name: ft-02-foot;
}

.ft-02__inner {
  padding-block: clamp(38px,6vw,64px) 0;
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1240px)/2));
}

.ft-02__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
  gap: clamp(28px,4vw,44px) clamp(20px,3vw,36px);
}

.ft-02__brandcol {
  display: grid;
  align-content: start;
  gap: 12px;
  min-width: 0;
  grid-column: span 2;
}

@container ft-02-foot (max-width: 720px) {
  .ft-02__brandcol {
    grid-column: auto;
  }
}

.ft-02__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -.025em;
}

.ft-02__mark {
  width: 24px;
  height: 24px;
  border-radius: 8px;
  background: conic-gradient(from 210deg,var(--ft-02-acc),oklch(0.62 0.17 260),var(--ft-02-acc));
  box-shadow: 0 5px 16px -6px var(--ft-02-acc);
}

.ft-02__blurb {
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--ft-02-mut);
  max-width: 34ch;
  text-wrap: pretty;
}

.ft-02__badge {
  justify-self: start;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .02em;
  color: var(--ft-02-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--ft-02-acc) 10%,transparent);
  border: 1px solid color-mix(in oklch,var(--ft-02-acc) 24%,transparent);
}

.ft-02__col {
  display: grid;
  align-content: start;
  gap: 4px;
  min-width: 0;
}

.ft-02__h {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--ft-02-ink);
  margin-block-end: 8px;
}

.ft-02__list {
  display: grid;
  gap: 2px;
}

.ft-02__link {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 36px;
  font-size: 14.5px;
  color: var(--ft-02-mut);
  text-decoration: none;
  position: relative;
  width: fit-content;
  transition: color .18s ease,transform .18s ease;
}

.ft-02__link::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: 6px;
  height: 1px;
  width: 100%;
  background: currentColor;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .28s cubic-bezier(.2,.8,.2,1);
}

.ft-02__link:hover {
  color: var(--ft-02-acc);
}

.ft-02__link:hover::after {
  transform: scaleX(1);
}

.ft-02__link:focus-visible,
.ft-02__slink:focus-visible {
  outline: 2px solid var(--ft-02-acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.ft-02__pill {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .04em;
  padding: 2px 7px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--ft-02-acc) 16%,transparent);
  color: var(--ft-02-acc);
}

.ft-02__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px 24px;
  margin-block-start: clamp(30px,4vw,48px);
  padding-block: 20px;
  padding-bottom: calc(20px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-02-line);
}

.ft-02__copy {
  font-size: 13.5px;
  color: var(--ft-02-mut);
}

.ft-02__legal {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 6px;
  margin-inline-start: auto;
}

.ft-02__slink {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 10px;
  border-radius: 8px;
  font-size: 13.5px;
  color: var(--ft-02-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.ft-02__slink:hover {
  color: var(--ft-02-ink);
  background: oklch(0.21 0.03 265/.05);
}

@media (max-width: 520px) {
  .ft-02__legal {
    margin-inline-start: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-02 * {
    transition-duration: .01ms !important;
  }
}
```
