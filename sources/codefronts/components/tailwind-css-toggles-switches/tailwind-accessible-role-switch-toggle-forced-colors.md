---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-accessible-role-switch-toggle-forced-colors/"
title: "Tailwind Accessible role=switch Toggle with forced-colors Support"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The reference implementation to ship in a design system: button[role=switch] with correct aria-checked handling, visible state text, a spec-grade focus ring…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accessible role=switch Toggle with forced-colors Support
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-accessible-role-switch-toggle-forced-colors/

The reference implementation to ship in a design system: button[role=switch] with correct aria-checked handling, visible state text, a spec-grade focus ring &mdash; and it stays fully visible in Windows High Contrast, where most CSS toggles silently vanish.
## HTML
```html
<section class="ttg-27 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg27-bg font-ttg27-sans" aria-label="Accessible ARIA switch">
  <div class="w-[min(350px,100%)] flex flex-col items-center gap-4 px-9 py-7 rounded-[18px] bg-white border border-ttg27-edge">
    <div class="flex flex-col items-center gap-1 text-center">
      <b class="text-[17px] font-bold text-ttg27-ink">Live captions</b>
      <span class="text-[12.5px] text-ttg27-mute">Immediate effect &middot; not a form value</span>
    </div>
    <button type="button" id="ttg-27-btn" role="switch" aria-checked="false" class="group flex items-center gap-3.5 min-h-11 px-2.5 py-1.5 rounded-xl border-0 bg-transparent cursor-pointer font-inherit focus-visible:outline-3 focus-visible:outline-ttg27-on focus-visible:outline-offset-2 forced-colors:focus-visible:outline-[Highlight] aria-checked:[&_.ttg27-track]:bg-ttg27-on aria-checked:[&_.ttg27-track]:forced-colors:bg-[Highlight] aria-checked:[&_.ttg27-track]:forced-colors:border-[Highlight] aria-checked:[&_.ttg27-thumb]:translate-x-[26px] aria-checked:[&_.ttg27-thumb]:forced-colors:bg-[Canvas] aria-checked:[&_.ttg27-thumb]:forced-colors:border-[Canvas] aria-checked:[&_.ttg27-off]:opacity-0 aria-checked:[&_.ttg27-on]:opacity-100">
      <span aria-hidden="true" class="ttg27-track relative block w-15 h-8.5 rounded-[18px] bg-ttg27-track transition-colors duration-250 forced-colors:bg-[Canvas] forced-colors:border-2 forced-colors:border-[ButtonText] motion-reduce:transition-none">
        <span class="ttg27-thumb absolute top-[3px] left-[3px] w-7 h-7 rounded-full bg-white shadow-[0_2px_6px_oklch(0.25_0.03_265/0.35)] transition-transform duration-250 ease-[cubic-bezier(0.3,1,0.35,1.05)] forced-colors:bg-[ButtonText] forced-colors:border-2 forced-colors:border-[ButtonText] forced-colors:shadow-none motion-reduce:transition-none"></span>
      </span>
      <span aria-hidden="true" class="relative block w-8 h-[1.3em] text-left text-[15px] font-bold text-ttg27-ink">
        <i class="ttg27-off absolute inset-0 not-italic transition-opacity duration-200 motion-reduce:transition-none">Off</i>
        <i class="ttg27-on absolute inset-0 not-italic opacity-0 text-ttg27-on transition-opacity duration-200 forced-colors:text-[ButtonText] motion-reduce:transition-none">On</i>
      </span>
    </button>
    <p id="ttg-27-live" aria-live="polite" class="min-h-[1.2em] text-[12.5px] text-ttg27-mute">Captions are off</p>
    <p class="text-center text-[11.5px] text-ttg27-faint">Space or Enter toggles &middot; survives Windows High Contrast</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg27-bg: #f4f5f9;
  --color-ttg27-bg: oklch(0.96 0.005 265);
  --color-ttg27-edge: #e5e7ee;
  --color-ttg27-edge: oklch(0.92 0.006 265);
  --color-ttg27-track: #cfd3dd;
  --color-ttg27-track: oklch(0.86 0.01 265);
  --color-ttg27-on: #3f63e0;
  --color-ttg27-on: oklch(0.52 0.19 265);
  --color-ttg27-ink: #212636;
  --color-ttg27-ink: oklch(0.27 0.018 265);
  --color-ttg27-mute: #767d90;
  --color-ttg27-mute: oklch(0.58 0.018 265);
  --color-ttg27-faint: #8d93a4;
  --color-ttg27-faint: oklch(0.65 0.016 265);
  --font-ttg27-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-27 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('#ttg-27-btn');
  const live = document.querySelector('#ttg-27-live');
  if (!btn || !live) return;
  // The attribute IS the state. Never mirror it into a class — the CSS reads it directly.
  btn.addEventListener('click', () => {
    const next = btn.getAttribute('aria-checked') !== 'true';
    btn.setAttribute('aria-checked', String(next));
    live.textContent = next ? 'Live captions on' : 'Live captions off';
  });
})();
```
