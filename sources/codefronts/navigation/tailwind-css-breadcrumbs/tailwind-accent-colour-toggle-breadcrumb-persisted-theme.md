---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-accent-colour-toggle-breadcrumb-persisted-theme/"
title: "Tailwind Accent-Colour Toggle Breadcrumb with Persisted Theme"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "A trail whose accent is one custom property the user switches live from a swatch row &mdash; hover tint, current-page fill and every focus ring recolour from…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accent-Colour Toggle Breadcrumb with Persisted Theme
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-accent-colour-toggle-breadcrumb-persisted-theme/

A trail whose accent is one custom property the user switches live from a swatch row &mdash; hover tint, current-page fill and every focus ring recolour from that single variable. Nine lines of JS persist the choice; the port adds aria-pressed so the selected swatch is announced, not just visible.
## HTML
```html
<section class="tbc-12 w-full min-h-svh grid place-items-center gap-5 bg-tbc12-bg font-tbc12-sans px-6 py-8 [--tbc12-accent:oklch(0.6_0.18_265)]">
  <div role="group" aria-label="Accent colour" class="flex items-center gap-2">
    <button type="button" data-accent="oklch(0.6 0.18 265)" aria-pressed="true" aria-label="Indigo accent" style="background:oklch(0.6 0.18 265)" class="w-6.5 h-6.5 rounded-full border-2 border-white cursor-pointer ring-1 ring-tbc12-edge transition-[scale,box-shadow] duration-150 hover:scale-112 focus-visible:outline-2 focus-visible:outline-[var(--tbc12-accent)] focus-visible:outline-offset-3 aria-pressed:ring-2 aria-pressed:ring-tbc12-ink aria-pressed:ring-offset-2 motion-reduce:transition-none"></button>
    <button type="button" data-accent="oklch(0.65 0.17 25)" aria-pressed="false" aria-label="Coral accent" style="background:oklch(0.65 0.17 25)" class="w-6.5 h-6.5 rounded-full border-2 border-white cursor-pointer ring-1 ring-tbc12-edge transition-[scale,box-shadow] duration-150 hover:scale-112 focus-visible:outline-2 focus-visible:outline-[var(--tbc12-accent)] focus-visible:outline-offset-3 aria-pressed:ring-2 aria-pressed:ring-tbc12-ink aria-pressed:ring-offset-2 motion-reduce:transition-none"></button>
    <button type="button" data-accent="oklch(0.7 0.16 160)" aria-pressed="false" aria-label="Emerald accent" style="background:oklch(0.7 0.16 160)" class="w-6.5 h-6.5 rounded-full border-2 border-white cursor-pointer ring-1 ring-tbc12-edge transition-[scale,box-shadow] duration-150 hover:scale-112 focus-visible:outline-2 focus-visible:outline-[var(--tbc12-accent)] focus-visible:outline-offset-3 aria-pressed:ring-2 aria-pressed:ring-tbc12-ink aria-pressed:ring-offset-2 motion-reduce:transition-none"></button>
    <button type="button" data-accent="oklch(0.72 0.15 60)" aria-pressed="false" aria-label="Amber accent" style="background:oklch(0.72 0.15 60)" class="w-6.5 h-6.5 rounded-full border-2 border-white cursor-pointer ring-1 ring-tbc12-edge transition-[scale,box-shadow] duration-150 hover:scale-112 focus-visible:outline-2 focus-visible:outline-[var(--tbc12-accent)] focus-visible:outline-offset-3 aria-pressed:ring-2 aria-pressed:ring-tbc12-ink aria-pressed:ring-offset-2 motion-reduce:transition-none"></button>
  </div>
  <nav aria-label="Breadcrumb">
    <ol class="flex flex-wrap items-center list-none m-0 p-0">
      <li class="flex items-center"><a href="#" class="flex items-center min-h-9 px-2.75 rounded-lg text-[13.5px] font-semibold text-tbc12-link no-underline transition-colors duration-200 hover:text-[var(--tbc12-accent)] hover:bg-[color-mix(in_oklab,var(--tbc12-accent)_12%,transparent)] focus-visible:outline-2 focus-visible:outline-[var(--tbc12-accent)] focus-visible:outline-offset-2 motion-reduce:transition-none">Home</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc12-sep"><a href="#" class="flex items-center min-h-9 px-2.75 rounded-lg text-[13.5px] font-semibold text-tbc12-link no-underline transition-colors duration-200 hover:text-[var(--tbc12-accent)] hover:bg-[color-mix(in_oklab,var(--tbc12-accent)_12%,transparent)] focus-visible:outline-2 focus-visible:outline-[var(--tbc12-accent)] focus-visible:outline-offset-2 motion-reduce:transition-none">Settings</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc12-sep"><a href="#" class="flex items-center min-h-9 px-2.75 rounded-lg text-[13.5px] font-semibold text-tbc12-link no-underline transition-colors duration-200 hover:text-[var(--tbc12-accent)] hover:bg-[color-mix(in_oklab,var(--tbc12-accent)_12%,transparent)] focus-visible:outline-2 focus-visible:outline-[var(--tbc12-accent)] focus-visible:outline-offset-2 motion-reduce:transition-none">Appearance</a></li>
      <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-tbc12-sep"><a href="#" aria-current="page" class="flex items-center min-h-9 px-2.75 rounded-lg text-[13.5px] font-bold text-white no-underline bg-[var(--tbc12-accent)] focus-visible:outline-2 focus-visible:outline-tbc12-ink focus-visible:outline-offset-2">Accent Colour</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc12-bg: #fbfbfd;
  --color-tbc12-bg: oklch(0.98 0.004 265);
  --color-tbc12-edge: #d9dae2;
  --color-tbc12-edge: oklch(0.86 0.01 265);
  --color-tbc12-link: #63666f;
  --color-tbc12-link: oklch(0.45 0.03 265);
  --color-tbc12-sep: #adb0ba;
  --color-tbc12-sep: oklch(0.72 0.02 265);
  --color-tbc12-ink: #2f323a;
  --color-tbc12-ink: oklch(0.26 0.02 265);
  --font-tbc12-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-12 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tbc-12').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var KEY = 'tbc12-accent', swatches = root.querySelectorAll('button[data-accent]');
    function apply(c) {
      root.style.setProperty('--tbc12-accent', c);
      swatches.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.accent === c)); });
    }
    try { var saved = localStorage.getItem(KEY); if (saved) apply(saved); } catch (e) {}
    swatches.forEach(function (btn) {
      btn.addEventListener('click', function () {
        apply(btn.dataset.accent);
        try { localStorage.setItem(KEY, btn.dataset.accent); } catch (e) {}
      });
    });
  });
})();
```
