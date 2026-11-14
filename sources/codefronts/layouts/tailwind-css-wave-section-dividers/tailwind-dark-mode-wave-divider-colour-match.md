---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-dark-mode-wave-divider-colour-match/"
title: "Tailwind Dark Mode Wave Divider Colour Match"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "Three ways to make a wave follow the theme automatically: a working toggle keyed off data-theme, a zero-JS prefers-color-scheme version, and the modern…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Wave Divider Colour Match
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-dark-mode-wave-divider-colour-match/

Three ways to make a wave follow the theme automatically: a working toggle keyed off data-theme, a zero-JS prefers-color-scheme version, and the modern light-dark() one-liner. The rule that fixes every dark-mode wave bug is the same in all three &mdash; never put a colour on the path.
## HTML
```html
<section class="twd-11 w-full min-h-svh flex flex-col font-twd11-sans">

  <!-- Working theme toggle, currentColor wave -->
  <div id="twd11-root" data-theme="dark" class="group/theme flex flex-col">
    <div class="relative bg-twd11-hero text-twd11-text px-6 pt-14 pb-28 text-center transition-colors duration-200 motion-reduce:transition-none group-data-[theme=dark]/theme:bg-twd11-nighthero group-data-[theme=dark]/theme:text-twd11-nighttext">
      <button id="twd11-toggle" type="button" aria-pressed="true" class="inline-flex items-center gap-2.5 min-h-11 px-4 mb-5 rounded-full text-[13px] font-bold border cursor-pointer transition-colors duration-200 bg-twd11-chip border-twd11-chipedge text-twd11-text group-data-[theme=dark]/theme:bg-twd11-nightchip group-data-[theme=dark]/theme:border-twd11-nightchipedge group-data-[theme=dark]/theme:text-twd11-nighttext hover:bg-twd11-chiphover group-data-[theme=dark]/theme:hover:bg-twd11-nightchiphover focus-visible:outline-3 focus-visible:outline-twd11-ring focus-visible:outline-offset-3 motion-reduce:transition-none">
        <span aria-hidden="true" class="w-2.5 h-2.5 rounded-full bg-current"></span><span id="twd11-toggle-label">Dark mode</span>
      </button>
      <h2 class="text-[clamp(24px,3.8vw,38px)] font-semibold mb-2">The wave follows the theme</h2>
      <p class="font-twd11-mono text-[14px]">fill-current &mdash; nothing to recolour by hand.</p>
      <svg class="absolute inset-x-0 -bottom-px block w-full h-[clamp(54px,8vw,110px)] text-twd11-next group-data-[theme=dark]/theme:text-twd11-nightnext [&_path]:fill-current pointer-events-none transition-colors duration-200 motion-reduce:transition-none" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
        <path d="M0,56 C260,116 540,4 820,50 C1060,88 1250,104 1440,72 L1440,120 L0,120 Z"></path>
      </svg>
    </div>
    <div class="bg-twd11-next text-twd11-text group-data-[theme=dark]/theme:bg-twd11-nightnext group-data-[theme=dark]/theme:text-twd11-nighttext px-6 pt-6 pb-14 text-center transition-colors duration-200 motion-reduce:transition-none">
      <p class="text-[15px]">Both surfaces and the seam recolour from one token pair.</p>
    </div>
  </div>

  <!-- prefers-color-scheme, zero JS -->
  <div class="relative bg-twd11-lhero dark:bg-twd11-dhero text-twd11-ltext dark:text-twd11-dtext px-6 pt-15 pb-26 text-center">
    <h2 class="text-[clamp(24px,3.8vw,36px)] font-semibold mb-2">Matches your OS right now</h2>
    <p class="text-[15px]">Switch your system theme &mdash; this recolours with no script.</p>
    <svg class="absolute inset-x-0 -bottom-px block w-full h-[clamp(50px,8vw,104px)] text-twd11-lnext dark:text-twd11-dnext [&_path]:fill-current pointer-events-none" viewBox="0 0 1440 110" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,50 C300,104 620,2 940,48 C1160,80 1300,92 1440,64 L1440,110 L0,110 Z"></path>
    </svg>
  </div>
  <div class="bg-twd11-lnext dark:bg-twd11-dnext text-twd11-ltext dark:text-twd11-dtext px-6 pt-6 pb-13 text-center">
    <p class="text-[15px]">One variant, both surfaces, one seam.</p>
  </div>

  <!-- light-dark() one-liner -->
  <div class="relative [color-scheme:light_dark] bg-twd11-lhero bg-[light-dark(#f6f8fb,#11161d)] text-twd11-ltext text-[light-dark(#22303c,#eaf1f8)] px-6 pt-15 pb-25 text-center">
    <h2 class="text-[clamp(23px,3.6vw,34px)] font-semibold mb-2">light-dark(), one declaration</h2>
    <p class="font-twd11-mono text-[14px]">bg-[light-dark(#dbe4ee,#1b2430)]</p>
    <svg class="absolute inset-x-0 -bottom-px block w-full h-[clamp(46px,7vw,96px)] text-twd11-lnext text-[light-dark(#dbe4ee,#1b2430)] [&_path]:fill-current pointer-events-none" viewBox="0 0 1440 100" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,44 C240,96 520,0 800,42 C1040,78 1250,90 1440,58 L1440,100 L0,100 Z"></path>
    </svg>
  </div>
  <div class="[color-scheme:light_dark] bg-twd11-lnext bg-[light-dark(#dbe4ee,#1b2430)] text-twd11-ltext text-[light-dark(#22303c,#eaf1f8)] px-6 pt-6 pb-13 text-center">
    <p class="text-[15px]">Keep a plain token declaration above it for older browsers.</p>
  </div>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd11-hero: #f3f5f8;
  --color-twd11-hero: oklch(0.96 0.01 250);
  --color-twd11-next: #d5dce6;
  --color-twd11-next: oklch(0.88 0.03 250);
  --color-twd11-text: #1f242e;
  --color-twd11-text: oklch(0.24 0.02 250);
  --color-twd11-chip: #e2e7ee;
  --color-twd11-chip: oklch(0.92 0.01 250);
  --color-twd11-chiphover: #d3dae4;
  --color-twd11-chiphover: oklch(0.87 0.02 250);
  --color-twd11-chipedge: #b7c0cd;
  --color-twd11-chipedge: oklch(0.79 0.02 250);
  --color-twd11-nighthero: #141820;
  --color-twd11-nighthero: oklch(0.17 0.02 260);
  --color-twd11-nightnext: #262d38;
  --color-twd11-nightnext: oklch(0.26 0.03 260);
  --color-twd11-nighttext: #eef1f6;
  --color-twd11-nighttext: oklch(0.95 0.01 260);
  --color-twd11-nightchip: #2e3644;
  --color-twd11-nightchip: oklch(0.3 0.03 260);
  --color-twd11-nightchiphover: #3a4351;
  --color-twd11-nightchiphover: oklch(0.36 0.03 260);
  --color-twd11-nightchipedge: #4b5564;
  --color-twd11-nightchipedge: oklch(0.44 0.03 260);
  --color-twd11-ring: #6aa6f2;
  --color-twd11-ring: oklch(0.7 0.14 250);
  --color-twd11-lhero: #f5f7fa;
  --color-twd11-lhero: oklch(0.97 0.01 210);
  --color-twd11-lnext: #d3dee8;
  --color-twd11-lnext: oklch(0.87 0.03 210);
  --color-twd11-ltext: #1f2a33;
  --color-twd11-ltext: oklch(0.24 0.03 210);
  --color-twd11-dhero: #101519;
  --color-twd11-dhero: oklch(0.16 0.02 215);
  --color-twd11-dnext: #1f2b33;
  --color-twd11-dnext: oklch(0.25 0.03 215);
  --color-twd11-dtext: #eaf1f6;
  --color-twd11-dtext: oklch(0.95 0.01 215);
  --font-twd11-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twd11-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.twd-11 {
  width: 100%;
  min-height: 100svh;
}
/* color-scheme follows the toggle so native scrollbars and controls match the surface.
   There is no utility for writing this from a data attribute. */

#twd11-root {
  color-scheme: light;
}

#twd11-root[data-theme="dark"] {
  color-scheme: dark;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#twd11-root');
  const btn = document.querySelector('#twd11-toggle');
  const label = document.querySelector('#twd11-toggle-label');
  if (!root || !btn || !label) return;
  // Respect the OS preference on first paint, then let the user override it.
  const set = (dark) => {
    root.dataset.theme = dark ? 'dark' : 'light';
    btn.setAttribute('aria-pressed', String(dark));
    label.textContent = dark ? 'Dark mode' : 'Light mode';
  };
  set(matchMedia('(prefers-color-scheme: dark)').matches);
  btn.addEventListener('click', () => set(root.dataset.theme !== 'dark'));
})();
```
