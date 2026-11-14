---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/tailwind-css-vertical-tabs/"
title: "Tailwind CSS Vertical Tabs"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "Utility-first vertical tabs with no component library, no Alpine and no Headless UI — just Tailwind classes plus 18 lines of vanilla JS."
has_js: "true"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Vertical Tabs
Source: https://codefronts.com/navigation/css-vertical-tabs/tailwind-css-vertical-tabs/

Utility-first vertical tabs with no component library, no Alpine and no Headless UI — just Tailwind classes plus 18 lines of vanilla JS. The trick that makes it clean is the aria-selected: variant: state lives in one ARIA attribute, styling reacts to it declaratively, and the script never touches a class list.
## HTML
```html
<section class="vt-07" aria-label="Tailwind CSS vertical tabs demo">
  <div class="vt-07__stage">
    <div class="vt-07__head">
      <p class="vt-07__eyebrow">utility-first · aria-selected: variant</p>
      <h2 class="vt-07__title">State in ARIA, style in variants</h2>
    </div>
    <div class="vt-07__card">
      <div class="flex gap-6">
        <div class="flex flex-col w-56" id="vt-07-tablist" role="tablist" aria-orientation="vertical" aria-label="Deployment docs">
          <button type="button" role="tab" id="vt-07-tab1" aria-controls="vt-07-panel1" aria-selected="true" class="flex w-full items-center gap-3 border-l-2 border-transparent px-4 py-3 text-sm font-medium text-slate-500 transition hover:bg-slate-50 hover:text-slate-900 aria-selected:border-indigo-600 aria-selected:bg-indigo-50 aria-selected:text-indigo-700">Install</button>
          <button type="button" role="tab" id="vt-07-tab2" aria-controls="vt-07-panel2" aria-selected="false" tabindex="-1" class="flex w-full items-center gap-3 border-l-2 border-transparent px-4 py-3 text-sm font-medium text-slate-500 transition hover:bg-slate-50 hover:text-slate-900 aria-selected:border-indigo-600 aria-selected:bg-indigo-50 aria-selected:text-indigo-700">Configure</button>
          <button type="button" role="tab" id="vt-07-tab3" aria-controls="vt-07-panel3" aria-selected="false" tabindex="-1" class="flex w-full items-center gap-3 border-l-2 border-transparent px-4 py-3 text-sm font-medium text-slate-500 transition hover:bg-slate-50 hover:text-slate-900 aria-selected:border-indigo-600 aria-selected:bg-indigo-50 aria-selected:text-indigo-700">Deploy</button>
          <button type="button" role="tab" id="vt-07-tab4" aria-controls="vt-07-panel4" aria-selected="false" tabindex="-1" class="flex w-full items-center gap-3 border-l-2 border-transparent px-4 py-3 text-sm font-medium text-slate-500 transition hover:bg-slate-50 hover:text-slate-900 aria-selected:border-indigo-600 aria-selected:bg-indigo-50 aria-selected:text-indigo-700">Monitor</button>
        </div>
        <div class="vt-07__panels">
          <div role="tabpanel" id="vt-07-panel1" aria-labelledby="vt-07-tab1" tabindex="0" class="vt-07__pane"><h3>One attribute, one truth</h3><p>The <code>aria-selected:</code> variant compiles to <code>&amp;[aria-selected="true"]</code>, so the visual state and the announced state can never disagree.</p><pre>aria-selected:border-indigo-600</pre></div>
          <div role="tabpanel" id="vt-07-panel2" aria-labelledby="vt-07-tab2" tabindex="0" hidden class="vt-07__pane"><h3>Reserve the border</h3><p><code>border-transparent</code> on every tab means activating one recolours 2px instead of inserting them — no sideways jolt.</p><pre>border-l-2 border-transparent</pre></div>
          <div role="tabpanel" id="vt-07-panel3" aria-labelledby="vt-07-tab3" tabindex="0" hidden class="vt-07__pane"><h3>No library needed</h3><p>Eighteen lines of vanilla JS replace Headless UI here: flip one attribute, toggle the <code>hidden</code> property, move the roving tabindex.</p><pre>el.setAttribute('aria-selected', on)</pre></div>
          <div role="tabpanel" id="vt-07-panel4" aria-labelledby="vt-07-tab4" tabindex="0" hidden class="vt-07__pane"><h3>Watch the scanner</h3><p>Tailwind reads your source as text. Template-literal class names are never generated — write them whole or safelist them.</p><pre>&#96;text-&#36;{c}-600&#96; → not compiled</pre></div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-07-bg);
  --vt-07-bg: oklch(0.972 0.004 265);
  --vt-07-slate50: oklch(0.984 0.003 265);
  --vt-07-slate500: oklch(0.554 0.024 265);
  --vt-07-slate900: oklch(0.21 0.03 265);
  --vt-07-indigo50: oklch(0.962 0.021 285);
  --vt-07-indigo600: oklch(0.511 0.21 285);
  --vt-07-indigo700: oklch(0.457 0.19 285);
  --vt-07-line: oklch(0.21 0.03 265/.1);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-07-slate900);
}

.vt-07 *,
.vt-07 *::before,
.vt-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-07__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(16px,2.6vw,28px);
  padding: clamp(20px,5vw,64px);
  background: radial-gradient(80% 55% at 50% 0%,oklch(0.95 0.03 285/.8),transparent);
}

.vt-07__head {
  display: grid;
  justify-items: center;
  gap: 9px;
  text-align: center;
}

.vt-07__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--vt-07-indigo600);
}

.vt-07__title {
  font-size: clamp(24px,3.6vw,38px);
  line-height: 1.08;
  letter-spacing: -.028em;
  font-weight: 700;
  text-wrap: balance;
}

.vt-07__card {
  width: min(94vw,860px);
  padding: clamp(16px,2.6vw,26px);
  background: oklch(1 0 0);
  border: 1px solid var(--vt-07-line);
  border-radius: 16px;
  box-shadow: 0 22px 60px -32px oklch(0.21 0.03 265/.4);
}

.vt-07 .flex {
  display: flex;
}

.vt-07 .flex-col {
  flex-direction: column;
}

.vt-07 .w-full {
  width: 100%;
}

.vt-07 .w-56 {
  inline-size: 14rem;
  flex: none;
}

.vt-07 .gap-3 {
  gap: .75rem;
}

.vt-07 .gap-6 {
  gap: 1.5rem;
}

.vt-07 .items-center {
  align-items: center;
}

.vt-07 .px-4 {
  padding-inline: 1rem;
}

.vt-07 .py-3 {
  padding-block: .75rem;
}

.vt-07 .text-sm {
  font-size: .875rem;
  line-height: 1.25rem;
}

.vt-07 .font-medium {
  font-weight: 600;
}

.vt-07 .border-l-2 {
  border-left-width: 2px;
  border-left-style: solid;
}

.vt-07 .border-transparent {
  border-left-color: transparent;
}

.vt-07 .text-slate-500 {
  color: var(--vt-07-slate500);
}

.vt-07 .transition {
  transition: color .18s ease,background-color .18s ease,border-color .18s ease;
}

.vt-07 [role="tab"] {
  min-height: 46px;
  background: transparent;
  border-block: 0;
  border-right: 0;
  font-family: inherit;
  text-align: left;
  cursor: pointer;
}

.vt-07 .hover\:bg-slate-50:hover {
  background-color: var(--vt-07-slate50);
}

.vt-07 .hover\:text-slate-900:hover {
  color: var(--vt-07-slate900);
}

.vt-07 .aria-selected\:border-indigo-600[aria-selected="true"] {
  border-left-color: var(--vt-07-indigo600);
}

.vt-07 .aria-selected\:bg-indigo-50[aria-selected="true"] {
  background-color: var(--vt-07-indigo50);
}

.vt-07 .aria-selected\:text-indigo-700[aria-selected="true"] {
  color: var(--vt-07-indigo700);
}

.vt-07 [role="tab"]:focus-visible {
  outline: 2px solid var(--vt-07-indigo600);
  outline-offset: -2px;
}

.vt-07__panels {
  flex: 1 1 auto;
  min-inline-size: 0;
  display: grid;
  min-height: clamp(220px,28vw,256px);
}

.vt-07__pane {
  grid-area: 1/1;
  align-content: center;
  display: grid;
  gap: 12px;
  justify-items: start;
}

.vt-07__pane[hidden] {
  display: none;
}

.vt-07__pane:not([hidden]) {
  animation: vt-07-in .32s cubic-bezier(.32,.72,.3,1) both;
}

@keyframes vt-07-in {
  from {
    opacity: 0;
    translate: 0 8px;
  }

  to {
    opacity: 1;
    translate: 0;
  }
}

.vt-07__pane:focus-visible {
  outline: 2px solid var(--vt-07-indigo600);
  outline-offset: 6px;
  border-radius: 10px;
}

.vt-07__pane h3 {
  font-size: clamp(18px,2.3vw,23px);
  line-height: 1.22;
  letter-spacing: -.02em;
  font-weight: 680;
  text-wrap: balance;
}

.vt-07__pane p {
  max-width: 46ch;
  font-size: 14.6px;
  line-height: 1.62;
  color: var(--vt-07-slate500);
  text-wrap: pretty;
}

.vt-07__pane pre,
.vt-07__pane code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
}

.vt-07__pane code {
  font-size: .85em;
  background: var(--vt-07-indigo50);
  color: var(--vt-07-indigo700);
  padding: 2px 6px;
  border-radius: 5px;
}

.vt-07__pane pre {
  font-size: 11.5px;
  color: var(--vt-07-indigo700);
  background: var(--vt-07-indigo50);
  padding: 9px 13px;
  border-radius: 9px;
  overflow-wrap: anywhere;
  white-space: pre-wrap;
}

@media (max-width: 640px) {
  .vt-07 .flex.gap-6 {
    flex-direction: column;
  }

  .vt-07 .w-56 {
    inline-size: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-07 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const list = document.getElementById('vt-07-tablist');
  if (!list || list.dataset.vtWired) return;
  list.dataset.vtWired = '1';
  const tabs = [...list.querySelectorAll('[role="tab"]')];
  const select = (tab) => {
    tabs.forEach((t) => {
      const on = t === tab;
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
      const panel = document.getElementById(t.getAttribute('aria-controls'));
      if (panel) panel.hidden = !on;
    });
  };
  list.addEventListener('click', (e) => {
    const tab = e.target.closest('[role="tab"]');
    if (tab) select(tab);
  });
  list.addEventListener('keydown', (e) => {
    const map = { ArrowDown: 1, ArrowUp: -1, Home: 'first', End: 'last' };
    if (!(e.key in map)) return;
    e.preventDefault();
    const i = tabs.indexOf(document.activeElement);
    const to = map[e.key] === 'first' ? 0 : map[e.key] === 'last' ? tabs.length - 1
      : (i + map[e.key] + tabs.length) % tabs.length;
    tabs[to].focus(); select(tabs[to]);
  });
})();
```
