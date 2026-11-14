---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/dark-mode-vertical-tabs-with-theme-toggle/"
title: "Dark Mode Vertical Tabs with Theme Toggle"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "Dark mode done the way it survives a redesign: semantic tokens, a system default, a manual override that wins, and no flash of the wrong theme."
has_js: "true"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Vertical Tabs with Theme Toggle
Source: https://codefronts.com/navigation/css-vertical-tabs/dark-mode-vertical-tabs-with-theme-toggle/

Dark mode done the way it survives a redesign: semantic tokens, a system default, a manual override that wins, and no flash of the wrong theme. The toggle flips one data-theme attribute — every colour in the component is derived from that, so adding a third theme is a single CSS block, not a refactor.
## HTML
```html
<section class="vt-16" data-theme="dark" id="vt-16-root" aria-label="Dark mode vertical tabs demo">
  <div class="vt-16__stage">
    <div class="vt-16__card" role="radiogroup" aria-label="Theme documentation">
      <div class="vt-16__rail">
        <div class="vt-16__col">
          <div class="vt-16__top">
            <p class="vt-16__brand"><span class="vt-16__logo" aria-hidden="true"></span>Tokens</p>
            <button class="vt-16__toggle" type="button" id="vt-16-toggle" aria-pressed="true">
              <span class="vt-16__pill" aria-hidden="true"></span>
              <span class="vt-16__opt vt-16__opt--light" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="4.2" stroke-width="1.8"/><path d="M12 2.6v2.2M12 19.2v2.2M2.6 12h2.2M19.2 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M18.7 5.3l-1.6 1.6M6.9 17.1l-1.6 1.6" stroke-width="1.8" stroke-linecap="round"/></svg>
              </span>
              <span class="vt-16__opt vt-16__opt--dark" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4z" stroke-width="1.8" stroke-linejoin="round"/></svg>
              </span>
              <span class="vt-16__sr">Toggle theme</span>
            </button>
          </div>
          <input class="vt-16__radio" type="radio" name="vt-16" id="vt-16-t1" checked>
          <label class="vt-16__tab" for="vt-16-t1"><span class="vt-16__dot" aria-hidden="true"></span>Two token layers<em class="vt-16__key" aria-hidden="true">01</em></label>
          <input class="vt-16__radio" type="radio" name="vt-16" id="vt-16-t2">
          <label class="vt-16__tab" for="vt-16-t2"><span class="vt-16__dot" aria-hidden="true"></span>System vs override<em class="vt-16__key" aria-hidden="true">02</em></label>
          <input class="vt-16__radio" type="radio" name="vt-16" id="vt-16-t3">
          <label class="vt-16__tab" for="vt-16-t3"><span class="vt-16__dot" aria-hidden="true"></span>No flash on load<em class="vt-16__key" aria-hidden="true">03</em></label>
          <input class="vt-16__radio" type="radio" name="vt-16" id="vt-16-t4">
          <label class="vt-16__tab" for="vt-16-t4"><span class="vt-16__dot" aria-hidden="true"></span>Contrast, carefully<em class="vt-16__key" aria-hidden="true">04</em></label>
        </div>
        <div class="vt-16__panels">
          <article class="vt-16__panel" id="vt-16-p1"><h3 class="vt-16__h">Primitives, then semantics</h3><p class="vt-16__p">Components reference <code>--surface</code> and <code>--text</code>, never a raw grey. A new theme is one extra block — no component CSS is touched.</p><div class="vt-16__swatches"><i style="background:var(--vt-16-surface)"></i><i style="background:var(--vt-16-raised)"></i><i style="background:var(--vt-16-acc)"></i><i style="background:var(--vt-16-text)"></i></div></article>
          <article class="vt-16__panel" id="vt-16-p2"><h3 class="vt-16__h">The override always wins</h3><p class="vt-16__p">Defaults come from <code>prefers-color-scheme</code>; an explicit <code>data-theme</code> on the root outranks them because it is a more specific selector on the same element.</p><p class="vt-16__chip">[data-theme="dark"] &gt; @media (prefers-color-scheme)</p></article>
          <article class="vt-16__panel" id="vt-16-p3"><h3 class="vt-16__h">Set color-scheme too</h3><p class="vt-16__p">It themes scrollbars, form controls and the canvas behind your page. Skipping it is why some dark sites still flash a white scrollbar.</p><p class="vt-16__chip">color-scheme: light dark</p></article>
          <article class="vt-16__panel" id="vt-16-p4"><h3 class="vt-16__h">Not pure black</h3><p class="vt-16__p">Maximum contrast causes halation for readers with astigmatism. This theme bottoms out near <code>oklch(0.16)</code> — around 15:1, not 21:1.</p><p class="vt-16__chip">aria-pressed on a real &lt;button&gt;</p></article>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --vt-16-g950: oklch(0.16 0.014 265);
  --vt-16-g900: oklch(0.21 0.016 265);
  --vt-16-g800: oklch(0.26 0.017 265);
  --vt-16-g400: oklch(0.66 0.015 265);
  --vt-16-g200: oklch(0.9 0.006 265);
  --vt-16-g50: oklch(0.98 0.003 265);
  --vt-16-white: oklch(1 0 0);
  color-scheme: light dark;
  background: var(--vt-16-bg);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-16-text);
  transition: background .4s ease,color .4s ease;
}

.vt-16[data-theme="dark"] {
  --vt-16-bg: var(--vt-16-g950);
  --vt-16-surface: var(--vt-16-g900);
  --vt-16-raised: var(--vt-16-g800);
  --vt-16-text: var(--vt-16-g50);
  --vt-16-mut: var(--vt-16-g400);
  --vt-16-acc: oklch(0.78 0.15 205);
  --vt-16-line: oklch(1 0 0/.11);
  color-scheme: dark;
}

.vt-16[data-theme="light"] {
  --vt-16-bg: var(--vt-16-g50);
  --vt-16-surface: var(--vt-16-white);
  --vt-16-raised: oklch(0.975 0.004 265);
  --vt-16-text: var(--vt-16-g950);
  --vt-16-mut: oklch(0.52 0.018 265);
  --vt-16-acc: oklch(0.5 0.16 235);
  --vt-16-line: oklch(0.16 0.014 265/.12);
  color-scheme: light;
}

.vt-16 *,
.vt-16 *::before,
.vt-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-16__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  padding: clamp(18px,4vw,60px);
}

.vt-16__card {
  width: min(96vw,880px);
  background: var(--vt-16-surface);
  border: 1px solid var(--vt-16-line);
  border-radius: 20px;
  box-shadow: 0 26px 70px -36px oklch(0 0 0/.55);
  overflow: hidden;
  transition: background .4s ease,border-color .4s ease;
}

.vt-16__rail {
  display: grid;
  grid-template-columns: minmax(190px,254px) minmax(0,1fr);
  align-items: stretch;
}

.vt-16__col {
  display: flex;
  flex-direction: column;
  gap: 2px;
  background: var(--vt-16-raised);
  padding: 12px;
  border-right: 1px solid var(--vt-16-line);
  transition: background .4s ease;
}

.vt-16__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 4px 4px 12px;
  margin-block-end: 8px;
  border-bottom: 1px solid var(--vt-16-line);
}

.vt-16__brand {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.vt-16__logo {
  position: relative;
  inline-size: 16px;
  block-size: 16px;
  border-radius: 4px;
  background: linear-gradient(135deg,var(--vt-16-acc) 0% 50%,color-mix(in oklch,var(--vt-16-text) 88%,transparent) 50% 100%);
}

.vt-16__toggle {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  place-items: center;
  inline-size: 66px;
  block-size: 32px;
  padding: 2px;
  border: 1px solid var(--vt-16-line);
  border-radius: 99px;
  background: color-mix(in oklch,var(--vt-16-text) 6%,transparent);
  color: var(--vt-16-mut);
  cursor: pointer;
  transition: background .3s ease,border-color .3s ease;
}

.vt-16__toggle:focus-visible {
  outline: 2px solid var(--vt-16-acc);
  outline-offset: 2px;
}

.vt-16__pill {
  position: absolute;
  inset-block: 2px;
  inset-inline-start: 2px;
  inline-size: 28px;
  border-radius: 99px;
  background: var(--vt-16-surface);
  border: 1px solid var(--vt-16-line);
  box-shadow: 0 2px 6px -2px oklch(0 0 0/.35);
  transition: translate .3s cubic-bezier(.34,1.2,.5,1),background .3s ease;
}

.vt-16[data-theme="dark"] .vt-16__pill {
  translate: 32px 0;
}

.vt-16__opt {
  position: relative;
  z-index: 1;
  display: grid;
  place-items: center;
  inline-size: 100%;
  block-size: 100%;
  transition: color .3s ease;
}

.vt-16__opt svg {
  inline-size: 14px;
  block-size: 14px;
  stroke: currentColor;
}

.vt-16[data-theme="light"] .vt-16__opt--light {
  color: var(--vt-16-acc);
}

.vt-16[data-theme="dark"] .vt-16__opt--dark {
  color: var(--vt-16-acc);
}

.vt-16__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.vt-16__tab {
  position: relative;
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 40px;
  padding: 0 12px;
  border-radius: 8px;
  font-size: 13.6px;
  font-weight: 600;
  color: var(--vt-16-mut);
  cursor: pointer;
  transition: color .18s ease,background .18s ease,box-shadow .18s ease;
}

.vt-16__dot {
  flex: none;
  inline-size: 6px;
  block-size: 6px;
  border-radius: 50%;
  background: color-mix(in oklch,var(--vt-16-text) 26%,transparent);
  transition: background .18s ease,scale .18s ease;
}

.vt-16__key {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  font-style: normal;
  font-weight: 600;
  color: var(--vt-16-mut);
  opacity: .5;
  letter-spacing: .06em;
}

.vt-16__tab:hover {
  color: var(--vt-16-text);
  background: color-mix(in oklch,var(--vt-16-text) 4%,transparent);
}

.vt-16__tab:hover .vt-16__dot {
  background: color-mix(in oklch,var(--vt-16-text) 50%,transparent);
}

.vt-16__radio:checked+.vt-16__tab {
  color: var(--vt-16-text);
  background: var(--vt-16-surface);
  box-shadow: 0 1px 2px oklch(0 0 0/.06),0 4px 12px -6px oklch(0 0 0/.24),inset 0 0 0 1px var(--vt-16-line);
}

.vt-16__radio:checked+.vt-16__tab .vt-16__dot {
  background: var(--vt-16-acc);
  scale: 1.35;
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--vt-16-acc) 22%,transparent);
}

.vt-16__radio:checked+.vt-16__tab .vt-16__key {
  color: var(--vt-16-acc);
  opacity: 1;
}

.vt-16__radio:focus-visible+.vt-16__tab {
  outline: 2px solid var(--vt-16-acc);
  outline-offset: 1px;
}

.vt-16__panels {
  display: grid;
  min-height: clamp(250px,32vw,300px);
  padding: clamp(22px,3.4vw,40px);
}

.vt-16__panel {
  grid-area: 1/1;
  align-content: center;
  display: grid;
  gap: 13px;
  justify-items: start;
  opacity: 0;
  visibility: hidden;
  transform: translateY(8px);
  transition: opacity .28s ease,transform .34s cubic-bezier(.32,.72,.3,1),visibility 0s .34s;
}

.vt-16__card:has(#vt-16-t1:checked) #vt-16-p1,
.vt-16__card:has(#vt-16-t2:checked) #vt-16-p2,
.vt-16__card:has(#vt-16-t3:checked) #vt-16-p3,
.vt-16__card:has(#vt-16-t4:checked) #vt-16-p4 {
  opacity: 1;
  visibility: visible;
  transform: none;
  transition-delay: 0s;
}

.vt-16__h {
  font-size: clamp(19px,2.4vw,26px);
  line-height: 1.18;
  letter-spacing: -.024em;
  font-weight: 690;
  text-wrap: balance;
}

.vt-16__p {
  max-width: 48ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--vt-16-mut);
  text-wrap: pretty;
}

.vt-16__p code,
.vt-16__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
}

.vt-16__p code {
  font-size: .85em;
  background: color-mix(in oklch,var(--vt-16-text) 9%,transparent);
  padding: 2px 6px;
  border-radius: 5px;
}

.vt-16__chip {
  font-size: 11px;
  padding: 7px 13px;
  border-radius: 99px;
  color: var(--vt-16-acc);
  background: color-mix(in oklch,var(--vt-16-acc) 11%,transparent);
  border: 1px solid color-mix(in oklch,var(--vt-16-acc) 26%,transparent);
  overflow-wrap: anywhere;
}

.vt-16__swatches {
  display: flex;
  gap: 8px;
}

.vt-16__swatches i {
  inline-size: 34px;
  block-size: 34px;
  border-radius: 9px;
  border: 1px solid var(--vt-16-line);
  transition: background .4s ease;
}

.vt-16__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (max-width: 680px) {
  .vt-16__rail {
    grid-template-columns: 1fr;
  }

  .vt-16__col {
    border-right: 0;
    border-bottom: 1px solid var(--vt-16-line);
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-16 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('vt-16-root');
  const btn = document.getElementById('vt-16-toggle');
  if (!root || !btn || root.dataset.vtWired) return;
  root.dataset.vtWired = '1';
  const system = matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  const apply = (theme) => {
    root.dataset.theme = theme;
    btn.setAttribute('aria-pressed', String(theme === 'dark'));
    btn.querySelector('.vt-16__sr').textContent = theme === 'dark' ? 'Dark mode' : 'Light mode';
  };
  apply(system);
  btn.addEventListener('click', () => apply(root.dataset.theme === 'dark' ? 'light' : 'dark'));
})();
```
