---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-animated-download-button/"
title: "Tailwind Animated Download Button with Progress Fill"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "Click and the arrow bounces, a progress bar sweeps the button's bottom edge, and the label resolves to \"Downloaded!\". Three states, one data-state attribute,…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Download Button with Progress Fill
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-animated-download-button/

Click and the arrow bounces, a progress bar sweeps the button's bottom edge, and the label resolves to "Downloaded!". Three states, one data-state attribute, and a progress bar that is a single after: layer scaling on the compositor.
## HTML
```html
<section class="tab-13 w-full min-h-svh grid place-items-center bg-tab13-bg font-tab13-sans px-6 py-10">
  <div class="flex flex-col items-center gap-5">
    <p class="text-[0.78rem] tracking-[0.1em] uppercase text-tab13-mut m-0">Click the button to download</p>
    <button type="button" id="tab13-btn" data-state="idle" class="relative overflow-hidden inline-flex items-center gap-2.5 min-h-11 px-9 text-base font-bold text-white bg-tab13-blue rounded-xl cursor-pointer shadow-[0_4px_16px_oklch(0.55_0.22_264/0.4)] transition-[background-color,box-shadow,translate] duration-300 hover:brightness-108 hover:-translate-y-0.5 active:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab13-blue data-[state=downloading]:bg-tab13-deep data-[state=downloading]:cursor-not-allowed data-[state=downloading]:hover:translate-y-0 data-[state=done]:bg-tab13-done data-[state=done]:shadow-[0_4px_16px_oklch(0.58_0.14_163/0.4)] after:content-[''] after:absolute after:left-0 after:bottom-0 after:w-full after:h-[3px] after:bg-white/55 after:origin-left after:scale-x-0 after:pointer-events-none after:transition-transform after:duration-[2200ms] after:ease-linear data-[state=downloading]:after:scale-x-100 data-[state=downloading]:[&_svg]:animate-tab13-bounce motion-reduce:transition-none motion-reduce:after:transition-none motion-reduce:data-[state=downloading]:[&_svg]:animate-none">
      <svg id="tab13-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="size-5 shrink-0">
        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
        <polyline points="7 10 12 15 17 10"/>
        <line x1="12" y1="15" x2="12" y2="3"/>
      </svg>
      <span id="tab13-text" role="status" aria-live="polite">Download v2.4.1</span>
    </button>
    <p class="text-[0.78rem] tracking-[0.1em] uppercase text-tab13-mut m-0">macOS &middot; 48.2 MB</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab13-bg: #f0f4ff;
  --color-tab13-bg: oklch(0.97 0.015 265);
  --color-tab13-mut: #64748b;
  --color-tab13-mut: oklch(0.55 0.03 255);
  --color-tab13-blue: #2563eb;
  --color-tab13-blue: oklch(0.55 0.22 264);
  --color-tab13-deep: #1d4ed8;
  --color-tab13-deep: oklch(0.5 0.22 264);
  --color-tab13-done: #059669;
  --color-tab13-done: oklch(0.58 0.14 163);
  --font-tab13-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tab13-bounce: tab13-bounce 0.6s ease-in-out infinite;
}

@keyframes tab13-bounce {
  0%,
    100% {
    translate: 0 0;
  }

  50% {
    translate: 0 4px;
  }
}

.tab-13 {
  width: 100%;
  min-height: 100svh;
}

.tab-13 ::selection {
  background: var(--color-tab13-blue);
  color: #fff;
}
```

## JavaScript
```js
(function () {
  var btn = document.getElementById('tab13-btn');
  var txt = document.getElementById('tab13-text');
  var icon = document.getElementById('tab13-icon');
  if (!btn || !txt || !icon) return;
  var DONE_ICON = '<polyline points="20 6 9 17 4 12"/>';
  var IDLE_ICON = icon.innerHTML;
  btn.addEventListener('click', function () {
    if (btn.dataset.state !== 'idle') return;
    btn.dataset.state = 'downloading';
    btn.setAttribute('aria-busy', 'true');
    txt.textContent = 'Downloading\u2026';
    setTimeout(function () {
      btn.dataset.state = 'done';
      btn.setAttribute('aria-busy', 'false');
      icon.innerHTML = DONE_ICON;
      txt.textContent = 'Downloaded!';
      setTimeout(function () {
        btn.dataset.state = 'idle';
        icon.innerHTML = IDLE_ICON;
        txt.textContent = 'Download v2.4.1';
      }, 2000);
    }, 2200);
  });
})();
```
