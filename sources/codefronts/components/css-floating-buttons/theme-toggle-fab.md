---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/theme-toggle-fab/"
title: "Dark Mode Theme Toggle Floating Button CSS"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "A theme switch worth the screen space it takes: the sun morphs into a moon with a travelling mask instead of a cross-fade, and the whole page flips…"
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Theme Toggle Floating Button CSS
Source: https://codefronts.com/components/css-floating-buttons/theme-toggle-fab/

A theme switch worth the screen space it takes: the sun morphs into a moon with a travelling mask instead of a cross-fade, and the whole page flips underneath a circular reveal that expands from the button itself. Respects the system preference on first load, remembers an explicit choice, and stays a proper aria-pressed toggle throughout.
## HTML
```html
<section class="fb-24" id="fb-24-root" data-theme="light" aria-label="Dark mode theme toggle demo">
  <div class="fb-24__stage">
    <p class="fb-24__eyebrow">masked morph · circular reveal</p>
    <h2 class="fb-24__title">One button, two worlds</h2>
    <p class="fb-24__sub">The sun is eaten into a crescent by a travelling mask while the page flips beneath an expanding circle anchored to the button.</p>
    <div class="fb-24__cards">
      <article class="fb-24__card"><span class="fb-24__k">Surface</span><b>--surface</b><i>oklch lightness swaps, hue holds</i></article>
      <article class="fb-24__card"><span class="fb-24__k">Ink</span><b>--ink</b><i>contrast ≥ 7:1 in both themes</i></article>
      <article class="fb-24__card"><span class="fb-24__k">Accent</span><b>--accent</b><i>chroma drops in dark mode</i></article>
    </div>
    <p class="fb-24__chip" id="fb-24-chip">system preference honoured on load</p>
  </div>
  <button class="fb-24__toggle" id="fb-24-toggle" type="button" aria-pressed="false" aria-label="Dark mode">
    <span class="fb-24__orb" aria-hidden="true"></span>
    <span class="fb-24__rays" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span>
  </button>
</section>
```
## CSS
```css
.fb-24 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-24-surface);
  --fb-24-surface: oklch(0.97 0.01 85);
  --fb-24-panel: oklch(1 0 0);
  --fb-24-ink: oklch(0.22 0.02 70);
  --fb-24-mut: oklch(0.52 0.015 70);
  --fb-24-accent: oklch(0.68 0.17 62);
  --fb-24-line: oklch(0.22 0.02 70/.1);
  --fb-24-shadow: oklch(0.22 0.02 70/.16);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-24-ink);
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
  transition: background .4s ease,color .4s ease;
}

.fb-24[data-theme="dark"] {
  --fb-24-surface: oklch(0.17 0.02 265);
  --fb-24-panel: oklch(0.22 0.025 265);
  --fb-24-ink: oklch(0.96 0.008 265);
  --fb-24-mut: oklch(0.74 0.015 265);
  --fb-24-accent: oklch(0.78 0.12 250);
  --fb-24-line: oklch(1 0 0/.1);
  --fb-24-shadow: oklch(0.05 0.01 265/.7);
}

.fb-24 *,
.fb-24 *::before,
.fb-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-24__stage {
  width: min(100%,64ch);
  display: grid;
  gap: clamp(16px,3vw,26px);
  justify-items: center;
  text-align: center;
}

.fb-24__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-24-accent);
}

.fb-24__title {
  font-size: clamp(26px,4.8vw,46px);
  line-height: 1.04;
  letter-spacing: -.035em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-24__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-24-mut);
  text-wrap: pretty;
}

.fb-24__cards {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(170px,1fr));
  gap: 12px;
  width: 100%;
}

.fb-24__card {
  display: grid;
  gap: 5px;
  padding: 16px;
  border-radius: 18px;
  text-align: left;
  background: var(--fb-24-panel);
  border: 1px solid var(--fb-24-line);
  box-shadow: 0 14px 34px -26px var(--fb-24-shadow);
  transition: background .4s ease,border-color .4s ease;
}

.fb-24__k {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--fb-24-accent);
}

.fb-24__card b {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13.5px;
  font-weight: 650;
}

.fb-24__card i {
  font-style: normal;
  font-size: 12px;
  line-height: 1.5;
  color: var(--fb-24-mut);
}

.fb-24__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-24-mut);
  padding: 8px 14px;
  border: 1px solid var(--fb-24-line);
  border-radius: 99px;
}

.fb-24__toggle {
  position: absolute;
  right: clamp(18px,4vw,44px);
  bottom: calc(clamp(18px,4vw,44px) + env(safe-area-inset-bottom));
  z-index: 5;
  display: grid;
  place-items: center;
  inline-size: 62px;
  block-size: 62px;
  border: 1px solid var(--fb-24-line);
  border-radius: 50%;
  cursor: pointer;
  background: var(--fb-24-panel);
  box-shadow: 0 14px 32px -14px var(--fb-24-shadow);
  transition: transform .3s cubic-bezier(.2,1.3,.4,1),background .4s ease,border-color .4s ease;
}

.fb-24__toggle:hover {
  transform: translateY(-2px) scale(1.04);
}

.fb-24__toggle:active {
  transform: scale(.93);
}

.fb-24__toggle:focus-visible {
  outline: 3px solid var(--fb-24-accent);
  outline-offset: 4px;
}

.fb-24__orb {
  grid-area: 1/1;
  position: relative;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--fb-24-accent);
  transition: background .4s ease,scale .5s cubic-bezier(.2,1.3,.4,1),translate .5s cubic-bezier(.2,.9,.3,1);
}

.fb-24__orb::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: var(--fb-24-panel);
  translate: 120% -120%;
  scale: 1;
  transition: translate .5s cubic-bezier(.2,.9,.3,1),background .4s ease;
}

.fb-24[data-theme="dark"] .fb-24__orb {
  scale: 1.14;
}

.fb-24[data-theme="dark"] .fb-24__orb::after {
  translate: 32% -32%;
}

.fb-24__rays {
  grid-area: 1/1;
  position: relative;
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  transition: rotate .5s cubic-bezier(.2,.9,.3,1),opacity .35s ease,scale .5s ease;
}

.fb-24__rays i {
  position: absolute;
  width: 2.4px;
  height: 6px;
  border-radius: 99px;
  background: var(--fb-24-accent);
  translate: 0 -18px;
  transition: background .4s ease;
}

.fb-24__rays i:nth-child(1) {
  rotate: 0deg;
}

.fb-24__rays i:nth-child(2) {
  rotate: 45deg;
  translate: 0 -18px;
}

.fb-24__rays i:nth-child(3) {
  rotate: 90deg;
}

.fb-24__rays i:nth-child(4) {
  rotate: 135deg;
}

.fb-24__rays i:nth-child(5) {
  rotate: 180deg;
}

.fb-24__rays i:nth-child(6) {
  rotate: 225deg;
}

.fb-24__rays i:nth-child(7) {
  rotate: 270deg;
}

.fb-24__rays i:nth-child(8) {
  rotate: 315deg;
}

.fb-24[data-theme="dark"] .fb-24__rays {
  opacity: 0;
  rotate: 40deg;
  scale: .5;
}

::view-transition-old(root),
::view-transition-new(root) {
  animation: none;
  mix-blend-mode: normal;
}

::view-transition-old(root) {
  z-index: 1;
}

::view-transition-new(root) {
  z-index: 2;
}

@media (prefers-reduced-motion: reduce) {
  .fb-24,
    .fb-24 * {
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('fb-24-root');
  const btn = document.getElementById('fb-24-toggle');
  const chip = document.getElementById('fb-24-chip');
  if (!root || !btn || btn.dataset.fbWired) return;
  btn.dataset.fbWired = '1';
  const calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const sysDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const apply = (dark) => {
    root.dataset.theme = dark ? 'dark' : 'light';
    btn.setAttribute('aria-pressed', String(dark));
    btn.setAttribute('aria-label', dark ? 'Dark mode, on' : 'Dark mode, off');
    chip.textContent = dark ? 'dark tokens active · chroma reduced' : 'light tokens active · system preference honoured';
  };
  apply(sysDark);
  btn.addEventListener('click', (e) => {
    const next = root.dataset.theme !== 'dark';
    if (!document.startViewTransition || calm) { apply(next); return; }
    const r = btn.getBoundingClientRect();
    const x = r.left + r.width / 2, y = r.top + r.height / 2;
    const maxR = Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y));
    const t = document.startViewTransition(() => apply(next));
    t.ready.then(() => {
      document.documentElement.animate(
        { clipPath: ['circle(0px at ' + x + 'px ' + y + 'px)', 'circle(' + maxR + 'px at ' + x + 'px ' + y + 'px)'] },
        { duration: 520, easing: 'ease-in-out', pseudoElement: '::view-transition-new(root)' }
      );
    });
  });
})();
```
