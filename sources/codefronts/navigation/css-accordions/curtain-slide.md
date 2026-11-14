---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/curtain-slide/"
title: "Curtain Slide Horizontal Accordion — clip-path Reveal Panels"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Every panel is always full width, stacked in the same grid cell — the active one is revealed by an animated clip-path wipe that sweeps across like a stage…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Curtain Slide Horizontal Accordion — clip-path Reveal Panels
Source: https://codefronts.com/navigation/css-accordions/curtain-slide/

Every panel is always full width, stacked in the same grid cell — the active one is revealed by an animated clip-path wipe that sweeps across like a stage curtain, driven by a slim tab rail on the left. Unlike flex-grow accordions, content NEVER reflows: it's uncovered, not resized.
## HTML
```html
<section class="acc-19" aria-label="Curtain slide clip-path accordion demo">
  <div class="acc-19__shell" role="group" aria-label="Quarterly report sections">
    <div class="acc-19__rail">
      <input type="radio" name="acc-19" id="acc-19-a" checked><label class="acc-19__tab" for="acc-19-a">Revenue</label>
      <input type="radio" name="acc-19" id="acc-19-b"><label class="acc-19__tab" for="acc-19-b">Customers</label>
      <input type="radio" name="acc-19" id="acc-19-c"><label class="acc-19__tab" for="acc-19-c">Product</label>
      <input type="radio" name="acc-19" id="acc-19-d"><label class="acc-19__tab" for="acc-19-d">Team</label>
    </div>
    <div class="acc-19__stage">
      <div class="acc-19__panel" data-p="a"><b>$4.2M ARR</b><p>Up 38% year over year. Net revenue retention held at 121% while CAC payback improved to 11 months.</p><span class="acc-19__stat"><i>+38%</i>YoY growth</span></div>
      <div class="acc-19__panel" data-p="b"><b>1,940 teams</b><p>Enterprise logos doubled this quarter. The self-serve funnel now converts 4.1% of signups within 14 days.</p><span class="acc-19__stat"><i>2×</i>enterprise logos</span></div>
      <div class="acc-19__panel" data-p="c"><b>31 releases</b><p>Headline: the plugin API shipped to GA. Median time-to-resolution for P1 bugs dropped to 6 hours.</p><span class="acc-19__stat"><i>GA</i>plugin API</span></div>
      <div class="acc-19__panel" data-p="d"><b>58 people</b><p>Nine hires, zero regretted attrition. Engineering is now 40% of the company across four time zones.</p><span class="acc-19__stat"><i>9</i>new hires</span></div>
    </div>
  </div>
</section>
```
## CSS
```css
.acc-19,
.acc-19 *,
.acc-19 *::before,
.acc-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-19 {
  --accent: oklch(0.6 0.19 20);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f7f3f2;
  padding: 44px 24px;
}

.acc-19__shell {
  display: flex;
  width: min(760px,100%);
  min-height: 340px;
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 24px 60px -34px rgba(80,30,25,.35);
  overflow: hidden;
}

.acc-19__rail {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 18px 14px;
  border-right: 1.5px solid #f0e6e4;
  background: #fbf8f7;
}

.acc-19__rail input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.acc-19__tab {
  position: relative;
  display: flex;
  align-items: center;
  min-height: 48px;
  padding: 0 18px 0 22px;
  font-size: 14.5px;
  font-weight: 650;
  color: #7d6a66;
  cursor: pointer;
  border-radius: 10px;
  transition: color .2s,background .2s;
}

.acc-19__tab::before {
  content: "";
  position: absolute;
  left: 6px;
  top: 50%;
  translate: 0 -50%;
  width: 3.5px;
  height: 0;
  border-radius: 3px;
  background: var(--accent);
  transition: height .25s;
}

.acc-19__tab:hover {
  background: #f4ecea;
}

.acc-19__rail input:checked + .acc-19__tab {
  color: var(--accent);
  background: #f7edeb;
}

.acc-19__rail input:checked + .acc-19__tab::before {
  height: 22px;
}

.acc-19__rail input:focus-visible + .acc-19__tab {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.acc-19__stage {
  flex: 1;
  display: grid;
  position: relative;
}

.acc-19__panel {
  grid-area: 1/1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 14px;
  padding: 36px 40px;
  clip-path: inset(0 0 0 100%);
  visibility: hidden;
  transition: clip-path .5s cubic-bezier(.65,0,.2,1),visibility 0s .5s;
}

.acc-19__shell:has(#acc-19-a:checked) .acc-19__panel[data-p=a],
.acc-19__shell:has(#acc-19-b:checked) .acc-19__panel[data-p=b],
.acc-19__shell:has(#acc-19-c:checked) .acc-19__panel[data-p=c],
.acc-19__shell:has(#acc-19-d:checked) .acc-19__panel[data-p=d] {
  clip-path: inset(0);
  visibility: visible;
  transition: clip-path .5s cubic-bezier(.65,0,.2,1),visibility 0s;
  z-index: 1;
}

.acc-19__panel b {
  font-size: 34px;
  font-weight: 850;
  color: #2b1d1a;
  letter-spacing: -.02em;
}

.acc-19__panel p {
  font-size: 15px;
  line-height: 1.65;
  color: #5d4b47;
  max-width: 52ch;
}

.acc-19__stat {
  display: flex;
  align-items: baseline;
  gap: 10px;
  font-size: 13px;
  font-weight: 600;
  color: #7d6a66;
}

.acc-19__stat i {
  font-style: normal;
  font-size: 22px;
  font-weight: 800;
  color: var(--accent);
}

@media (max-width: 600px) {
  .acc-19__shell {
    flex-direction: column;
  }

  .acc-19__rail {
    flex-direction: row;
    overflow-x: auto;
    border-right: none;
    border-bottom: 1.5px solid #f0e6e4;
  }

  .acc-19__panel {
    padding: 26px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .acc-19__panel {
    transition: visibility 0s;
  }

  .acc-19__tab,
    .acc-19__tab::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — all panels stack in one grid cell at full size; :has(radio:checked) transitions the active panel's clip-path from inset(0 0 0 100%) to inset(0), wiping it in like a curtain with zero content reflow. Inactive panels get visibility:hidden so keyboard/AT users never land in covered content. */
```
