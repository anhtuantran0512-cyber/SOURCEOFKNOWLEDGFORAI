---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/css-wave-divider-full-width-responsive-mobile-fix/"
title: "CSS wave divider full width responsive mobile fix"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "The bug-fix demo: side-by-side broken and fixed dividers so you can see exactly what causes the white gap, the hairline seam and the horizontally smeared…"
has_js: "true"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS wave divider full width responsive mobile fix
Source: https://codefronts.com/layouts/css-wave-section-dividers/css-wave-divider-full-width-responsive-mobile-fix/

The bug-fix demo: side-by-side broken and fixed dividers so you can see exactly what causes the white gap, the hairline seam and the horizontally smeared curve on narrow screens — plus a live viewport squeeze slider that reproduces the failure without resizing your browser.
## HTML
```html
<div class="wsd-08-group">
<section class="wsd-08a">
  <div class="wsd-08a__ctl">
    <label class="wsd-08a__label" for="wsd-08a-range">Simulated viewport width: <output id="wsd-08a-out">100%</output></label>
    <input class="wsd-08a__range" id="wsd-08a-range" type="range" min="32" max="100" value="100" step="1" aria-describedby="wsd-08a-hint">
    <p class="wsd-08a__hint" id="wsd-08a-hint">Drag to squeeze both panes. The left pane shows the classic bugs; the right pane is the fixed recipe.</p>
  </div>
  <div class="wsd-08a__panes" id="wsd-08a-panes">
    <div class="wsd-08a__pane">
      <p class="wsd-08a__tag wsd-08a__tag--bad">Broken</p>
      <div class="wsd-08a__demo wsd-08a__demo--bad">
        <div class="wsd-08a__hero"><span>Hero</span>
          <svg class="wsd-08a__wave" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0,60 C300,120 620,0 940,54 C1160,90 1300,100 1440,70 L1440,120 L0,120 Z"></path></svg>
        </div>
        <div class="wsd-08a__body"><span>Next section</span></div>
      </div>
      <ul class="wsd-08a__notes"><li>inline SVG baseline gap</li><li>seam at fractional DPR</li><li>curve smears when narrow</li></ul>
    </div>
    <div class="wsd-08a__pane">
      <p class="wsd-08a__tag wsd-08a__tag--good">Fixed</p>
      <div class="wsd-08a__demo wsd-08a__demo--good">
        <div class="wsd-08a__hero"><span>Hero</span>
          <svg class="wsd-08a__wave" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0,60 C300,120 620,0 940,54 C1160,90 1300,100 1440,70 L1440,120 L0,120 Z"></path></svg>
        </div>
        <div class="wsd-08a__body"><span>Next section</span></div>
      </div>
      <ul class="wsd-08a__notes"><li>display:block</li><li>bottom:-1px overlap</li><li>min-width keeps the ratio</li></ul>
    </div>
  </div>
</section>
<section class="wsd-08b">
  <div class="wsd-08b__hero">
    <h2 class="wsd-08b__title">Different wave per breakpoint</h2>
    <p class="wsd-08b__copy">Below 640px a taller, shorter-wavelength mask takes over so the curve stays legible.</p>
  </div>
  <div class="wsd-08b__divider" role="presentation"></div>
  <div class="wsd-08b__body"><p class="wsd-08b__copy">Swapping the mask beats stretching one path across every viewport.</p></div>
</section>
</div>
```
## CSS
```css
.wsd-08-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-08-group > section {
  width: 100%;
}

.wsd-08a,
.wsd-08a *,
.wsd-08a *::before,
.wsd-08a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-08a {
  --ink: oklch(0.24 0.02 250);
  --paper: oklch(0.97 0.005 250);
  --bad: oklch(0.62 0.2 22);
  --good: oklch(0.68 0.16 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--paper);
  padding: 26px 20px 34px;
  color: var(--ink);
}

.wsd-08a__ctl {
  max-width: 720px;
  margin: 0 auto 22px;
}

.wsd-08a__label {
  display: block;
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 8px;
}

.wsd-08a__label output {
  font-family: ui-monospace,monospace;
  font-weight: 800;
}

.wsd-08a__range {
  width: 100%;
  accent-color: oklch(0.55 0.16 260);
}

.wsd-08a__range:focus-visible {
  outline: 3px solid oklch(0.55 0.16 260);
  outline-offset: 4px;
}

.wsd-08a__hint {
  font-size: 12.5px;
  opacity: .66;
  margin-top: 8px;
}

.wsd-08a__panes {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(260px,1fr));
  gap: 20px;
  max-width: 920px;
  margin: 0 auto;
}

.wsd-08a__pane {
  min-width: 0;
}

.wsd-08a__tag {
  display: inline-block;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: 4px 9px;
  border-radius: 999px;
  margin-bottom: 9px;
  color: #fff;
}

.wsd-08a__tag--bad {
  background: var(--bad);
}

.wsd-08a__tag--good {
  background: var(--good);
}

.wsd-08a__demo {
  border: 1px solid oklch(0.88 0.01 250);
  border-radius: 12px;
  overflow: hidden;
}

.wsd-08a__hero {
  position: relative;
  background: var(--ink);
  color: #fff;
  font-size: 12px;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: 30px 12px 54px;
  text-align: center;
}

.wsd-08a__body {
  background: oklch(0.86 0.03 250);
  color: var(--ink);
  font-size: 12px;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: 20px 12px;
  text-align: center;
}

.wsd-08a__demo--bad .wsd-08a__wave {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 46px;
  color: oklch(0.86 0.03 250);
}

.wsd-08a__demo--good .wsd-08a__wave {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: -1px;
  display: block;
  width: 100%;
  min-width: 520px;
  height: clamp(38px,6vw,52px);
  color: oklch(0.86 0.03 250);
  pointer-events: none;
}

.wsd-08a__wave path {
  fill: currentColor;
}

.wsd-08a__demo--good {
  overflow-x: clip;
}

.wsd-08a__notes {
  list-style: none;
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  gap: 5px;
  font-size: 12.5px;
  font-family: ui-monospace,monospace;
  opacity: .72;
}

.wsd-08a__notes li::before {
  content: "› ";
  opacity: .5;
}

.wsd-08b,
.wsd-08b *,
.wsd-08b *::before,
.wsd-08b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-08b {
  --hero: oklch(0.3 0.1 300);
  --next: oklch(0.96 0.02 300);
  --wave: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 110' preserveAspectRatio='none'%3E%3Cpath d='M0,54 C300,110 620,4 940,52 C1160,86 1300,96 1440,66 L1440,110 L0,110 Z' fill='%23000'/%3E%3C/svg%3E");
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-08b__hero {
  background: var(--hero);
  color: #fff;
  padding: 62px 24px 34px;
  text-align: center;
}

.wsd-08b__title {
  font-size: clamp(23px,3.6vw,34px);
  margin-bottom: 8px;
}

.wsd-08b__copy {
  font-size: 15px;
  opacity: .8;
  max-width: 50ch;
  margin: 0 auto;
}

.wsd-08b__divider {
  height: clamp(52px,8vw,100px);
  background: var(--next);
  -webkit-mask: var(--wave) no-repeat center/100% 100%;
  mask: var(--wave) no-repeat center/100% 100%;
  margin-top: -1px;
}

.wsd-08b__body {
  background: var(--next);
  color: oklch(0.32 0.07 300);
  padding: 10px 24px 58px;
  text-align: center;
}

.wsd-08b__body .wsd-08b__copy {
  opacity: .74;
}

@media (max-width: 640px) {
  .wsd-08b {
    --wave: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 480 110' preserveAspectRatio='none'%3E%3Cpath d='M0,48 C80,104 160,6 240,48 C320,90 400,104 480,60 L480,110 L0,110 Z' fill='%23000'/%3E%3C/svg%3E");
  }
}
```

## JavaScript
```js
(() => {
  const range = document.querySelector('#wsd-08a-range');
  const panes = document.querySelector('#wsd-08a-panes');
  const out = document.querySelector('#wsd-08a-out');
  if (!range || !panes || !out) return;
  const apply = () => { panes.style.width = range.value + '%'; panes.style.marginInline = 'auto'; out.textContent = range.value + '%'; };
  range.addEventListener('input', apply); apply();
})();

/* No JavaScript — the wave lives in a --wave custom property, so a media query can swap the entire shape without touching markup. */
```
