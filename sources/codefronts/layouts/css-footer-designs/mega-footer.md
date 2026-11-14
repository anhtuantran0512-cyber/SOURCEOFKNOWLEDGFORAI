---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/mega-footer/"
title: "Multi-Column Mega Footer HTML CSS Grid"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "The six-column sitemap footer big sites need, using subgrid so every column's heading, list and secondary link sit on the same baselines even when the lists…"
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Column Mega Footer HTML CSS Grid
Source: https://codefronts.com/layouts/css-footer-designs/mega-footer/

The six-column sitemap footer big sites need, using subgrid so every column's heading, list and secondary link sit on the same baselines even when the lists are different lengths. This is the one layout problem plain auto-fit grids cannot solve — and subgrid solves it in two lines.
## HTML
```html
<section class="ft-19" aria-label="Multi column mega footer with CSS grid demo">
  <main class="ft-19__main">
    <p class="ft-19__eyebrow">grid-template-rows: subgrid</p>
    <h1 class="ft-19__title">Six columns, one baseline grid</h1>
    <p class="ft-19__sub">Each list is a different length, yet every heading, every list start and every “see all” link lands on the same line. Two declarations, no fixed heights.</p>
  </main>
  <footer class="ft-19__foot">
    <div class="ft-19__cols">
      <div class="ft-19__brandcell">
        <div class="ft-19__brand"><span class="ft-19__mark" aria-hidden="true"></span>Tidewater</div>
        <p class="ft-19__blurb">Logistics software for ports, freight forwarders and the people who keep 41,000 containers moving each day.</p>
        <ul class="ft-19__stats"><li><strong>62</strong> ports live</li><li><strong>99.98%</strong> uptime</li><li><strong>24/7</strong> support</li></ul>
      </div>
      <nav class="ft-19__col" aria-labelledby="ft-19-c1">
        <h2 class="ft-19__ch" id="ft-19-c1">Products</h2>
        <ul class="ft-19__list"><li><a class="ft-19__link" href="#ft-19-a">Terminal OS</a></li><li><a class="ft-19__link" href="#ft-19-a">Yard planner</a></li><li><a class="ft-19__link" href="#ft-19-a">Berth scheduling</a></li><li><a class="ft-19__link" href="#ft-19-a">Customs filing</a></li><li><a class="ft-19__link" href="#ft-19-a">Driver app</a></li><li><a class="ft-19__link" href="#ft-19-a">Telemetry</a></li></ul>
        <a class="ft-19__more" href="#ft-19-a">All products</a>
      </nav>
      <nav class="ft-19__col" aria-labelledby="ft-19-c2">
        <h2 class="ft-19__ch" id="ft-19-c2">Industries</h2>
        <ul class="ft-19__list"><li><a class="ft-19__link" href="#ft-19-a">Container ports</a></li><li><a class="ft-19__link" href="#ft-19-a">Bulk terminals</a></li><li><a class="ft-19__link" href="#ft-19-a">Ro-Ro</a></li></ul>
        <a class="ft-19__more" href="#ft-19-a">All industries</a>
      </nav>
      <nav class="ft-19__col" aria-labelledby="ft-19-c3">
        <h2 class="ft-19__ch" id="ft-19-c3">Developers</h2>
        <ul class="ft-19__list"><li><a class="ft-19__link" href="#ft-19-a">API reference</a></li><li><a class="ft-19__link" href="#ft-19-a">EDI &amp; EDIFACT</a></li><li><a class="ft-19__link" href="#ft-19-a">Webhooks</a></li><li><a class="ft-19__link" href="#ft-19-a">Sandbox</a></li><li><a class="ft-19__link" href="#ft-19-a">Status</a></li></ul>
        <a class="ft-19__more" href="#ft-19-a">Developer hub</a>
      </nav>
      <nav class="ft-19__col" aria-labelledby="ft-19-c4">
        <h2 class="ft-19__ch" id="ft-19-c4">Resources</h2>
        <ul class="ft-19__list"><li><a class="ft-19__link" href="#ft-19-a">Case studies</a></li><li><a class="ft-19__link" href="#ft-19-a">Whitepapers</a></li><li><a class="ft-19__link" href="#ft-19-a">Webinars</a></li><li><a class="ft-19__link" href="#ft-19-a">Glossary</a></li></ul>
        <a class="ft-19__more" href="#ft-19-a">Resource centre</a>
      </nav>
      <nav class="ft-19__col" aria-labelledby="ft-19-c5">
        <h2 class="ft-19__ch" id="ft-19-c5">Company</h2>
        <ul class="ft-19__list"><li><a class="ft-19__link" href="#ft-19-a">About</a></li><li><a class="ft-19__link" href="#ft-19-a">Careers</a></li><li><a class="ft-19__link" href="#ft-19-a">Newsroom</a></li><li><a class="ft-19__link" href="#ft-19-a">Partners</a></li><li><a class="ft-19__link" href="#ft-19-a">Contact</a></li></ul>
        <a class="ft-19__more" href="#ft-19-a">Company hub</a>
      </nav>
    </div>
    <div class="ft-19__bar">
      <p class="ft-19__copy">© <time datetime="2026">2026</time> Tidewater Systems N.V. · Rotterdam · Singapore · Houston</p>
      <ul class="ft-19__legal"><li><a class="ft-19__slink" href="#ft-19-a">Privacy</a></li><li><a class="ft-19__slink" href="#ft-19-a">Terms</a></li><li><a class="ft-19__slink" href="#ft-19-a">Security</a></li><li><a class="ft-19__slink" href="#ft-19-a">Sitemap</a></li></ul>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-19-bg);
  --ft-19-bg: oklch(0.97 0.008 220);
  --ft-19-foot: oklch(0.21 0.03 235);
  --ft-19-ink: oklch(0.21 0.03 235);
  --ft-19-mut: oklch(0.53 0.02 235);
  --ft-19-fink: oklch(0.97 0.006 235);
  --ft-19-fmut: oklch(0.74 0.016 235);
  --ft-19-acc: oklch(0.75 0.14 200);
  --ft-19-line: oklch(0.97 0.006 235/.14);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-19-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-19 *,
.ft-19 *::before,
.ft-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-19 ul {
  list-style: none;
}

.ft-19__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(38px,7.5vh,86px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1320px)/2));
}

.ft-19__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: oklch(0.5 0.13 210);
}

.ft-19__title {
  font-size: clamp(29px,5.2vw,56px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 15ch;
  text-wrap: balance;
}

.ft-19__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-19-mut);
  max-width: 58ch;
  text-wrap: pretty;
}

.ft-19__foot {
  background: var(--ft-19-foot);
  color: var(--ft-19-fink);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1320px)/2));
  container-type: inline-size;
  container-name: ft-19-foot;
}

.ft-19__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(10rem,1fr));
  gap: clamp(24px,3vw,38px) clamp(16px,2vw,30px);
  padding-block: clamp(32px,4.6vw,56px);
}

.ft-19__brandcell {
  display: grid;
  align-content: start;
  gap: 12px;
  min-width: 0;
}

.ft-19__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 18px;
  font-weight: 700;
  letter-spacing: -.025em;
}

.ft-19__mark {
  width: 25px;
  height: 25px;
  border-radius: 8px;
  background: linear-gradient(150deg,var(--ft-19-acc),oklch(0.55 0.16 255));
  box-shadow: 0 6px 18px -8px var(--ft-19-acc);
}

.ft-19__blurb {
  font-size: 14px;
  line-height: 1.6;
  color: var(--ft-19-fmut);
  max-width: 34ch;
  text-wrap: pretty;
}

.ft-19__stats {
  display: grid;
  gap: 5px;
  font-size: 12.8px;
  color: var(--ft-19-fmut);
}

.ft-19__stats strong {
  color: var(--ft-19-fink);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.ft-19__col {
  display: grid;
  align-content: start;
  gap: 8px;
  min-width: 0;
}

.ft-19__ch {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ft-19-fink);
}

.ft-19__list {
  display: grid;
  gap: 1px;
  align-content: start;
}

.ft-19__link {
  display: inline-flex;
  align-items: center;
  min-height: 34px;
  font-size: 14px;
  color: var(--ft-19-fmut);
  text-decoration: none;
  width: fit-content;
  transition: color .18s ease,translate .18s ease;
}

.ft-19__link:hover {
  color: var(--ft-19-acc);
  translate: 3px 0;
}

.ft-19__more {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  align-self: end;
  min-height: 34px;
  font-size: 12.6px;
  font-weight: 650;
  color: var(--ft-19-acc);
  text-decoration: none;
  width: fit-content;
}

.ft-19__more::after {
  content: '→';
  transition: translate .2s ease;
}

.ft-19__more:hover::after {
  translate: 3px 0;
}

.ft-19__link:focus-visible,
.ft-19__more:focus-visible,
.ft-19__slink:focus-visible {
  outline: 2px solid var(--ft-19-acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.ft-19__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px 22px;
  padding-block: 20px;
  padding-bottom: calc(20px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-19-line);
}

.ft-19__copy {
  font-size: 12.8px;
  color: var(--ft-19-fmut);
}

.ft-19__legal {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 16px;
  margin-inline-start: auto;
}

.ft-19__slink {
  display: flex;
  align-items: center;
  min-height: 36px;
  font-size: 12.8px;
  color: var(--ft-19-fmut);
  text-decoration: none;
}

.ft-19__slink:hover {
  color: var(--ft-19-fink);
  text-decoration: underline;
  text-underline-offset: .25em;
}

@container ft-19-foot (min-width: 60rem) {
  .ft-19__cols {
    grid-template-columns: repeat(7,1fr);
    grid-template-rows: auto 1fr auto;
  }

  .ft-19__brandcell {
    grid-column: span 2;
    grid-row: span 3;
  }

  .ft-19__col {
    grid-row: span 3;
    grid-template-rows: subgrid;
  }
}

@media (max-width: 560px) {
  .ft-19__legal {
    margin-inline-start: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-19 * {
    transition-duration: .01ms !important;
  }
}
```
