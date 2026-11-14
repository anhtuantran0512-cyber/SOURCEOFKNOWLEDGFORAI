---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-loading-spinner-inside-button/"
title: "Tailwind Loading Spinner Inside Button with State Machine"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "Idle &rarr; loading &rarr; success &rarr; idle, with a spinner built from a single after: ring."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Loading Spinner Inside Button with State Machine
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-loading-spinner-inside-button/

Idle &rarr; loading &rarr; success &rarr; idle, with a spinner built from a single after: ring. The port replaces measured inline widths with min-w-40, so the button no longer needs JavaScript to know how wide it is.
## HTML
```html
<section class="tab-18 w-full min-h-svh grid place-items-center bg-tab18-bg font-tab18-sans px-6 py-10">
  <div class="flex flex-col items-center gap-8">
    <p class="text-[0.78rem] tracking-[0.14em] uppercase text-tab18-mut m-0">Click to simulate a request</p>
    <div class="flex flex-wrap justify-center gap-4">
      <button type="button" data-state="idle" class="tab18-btn relative inline-flex items-center justify-center overflow-hidden min-w-40 min-h-11 px-8 text-[0.95rem] font-bold text-white bg-tab18-primary border-2 border-tab18-primary rounded-[10px] cursor-pointer transition-[background-color,border-color,translate] duration-300 hover:not-disabled:brightness-108 hover:not-disabled:-translate-y-px active:not-disabled:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab18-primary disabled:cursor-not-allowed disabled:opacity-85 data-[state=success]:bg-tab18-done data-[state=success]:border-tab18-done after:content-[''] after:absolute after:size-[18px] after:rounded-full after:border-2 after:border-white/30 after:border-t-white after:opacity-0 after:scale-0 after:pointer-events-none after:transition-[opacity,scale] after:duration-200 data-[state=loading]:after:opacity-100 data-[state=loading]:after:scale-100 data-[state=loading]:after:animate-tab18-spin motion-reduce:transition-none motion-reduce:data-[state=loading]:after:animate-none">
        <span class="transition-opacity duration-[250ms]">Save Changes</span>
        <svg viewBox="0 0 20 20" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="absolute size-5 opacity-0 scale-50 transition-[opacity,scale] duration-300 delay-200">
          <polyline points="16 5 8 14 4 10" pathLength="24" stroke-dasharray="24" stroke-dashoffset="24"/>
        </svg>
      </button>
      <button type="button" data-state="idle" class="tab18-btn relative inline-flex items-center justify-center overflow-hidden min-w-40 min-h-11 px-8 text-[0.95rem] font-bold text-tab18-primary bg-transparent border-2 border-tab18-primary rounded-[10px] cursor-pointer transition-[background-color,border-color,color,translate] duration-300 hover:not-disabled:bg-tab18-primary/8 hover:not-disabled:-translate-y-px active:not-disabled:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab18-primary disabled:cursor-not-allowed disabled:opacity-85 data-[state=success]:bg-tab18-done data-[state=success]:border-tab18-done data-[state=success]:text-white after:content-[''] after:absolute after:size-[18px] after:rounded-full after:border-2 after:border-tab18-primary/30 after:border-t-tab18-primary after:opacity-0 after:scale-0 after:pointer-events-none after:transition-[opacity,scale] after:duration-200 data-[state=loading]:after:opacity-100 data-[state=loading]:after:scale-100 data-[state=loading]:after:animate-tab18-spin motion-reduce:transition-none motion-reduce:data-[state=loading]:after:animate-none">
        <span class="transition-opacity duration-[250ms]">Subscribe</span>
        <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="absolute size-5 opacity-0 scale-50 transition-[opacity,scale] duration-300 delay-200">
          <polyline points="16 5 8 14 4 10" pathLength="24" stroke-dasharray="24" stroke-dashoffset="24"/>
        </svg>
      </button>
    </div>
    <p id="tab18-status" role="status" aria-live="polite" class="text-[0.8rem] text-tab18-mut min-h-5"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab18-bg: #f1f5f9;
  --color-tab18-bg: oklch(0.97 0.006 250);
  --color-tab18-mut: #64748b;
  --color-tab18-mut: oklch(0.55 0.03 255);
  --color-tab18-primary: #4f46e5;
  --color-tab18-primary: oklch(0.51 0.24 277);
  --color-tab18-done: #059669;
  --color-tab18-done: oklch(0.58 0.14 163);
  --font-tab18-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tab18-spin: tab18-spin 0.8s linear infinite;
  --animate-tab18-draw: tab18-draw 0.4s ease 0.1s forwards;
}

@keyframes tab18-spin {
  to {
    rotate: 360deg;
  }
}

@keyframes tab18-draw {
  from {
    stroke-dashoffset: 24;
  }

  to {
    stroke-dashoffset: 0;
  }
}
/* State-driven child rules: the label fade and the checkmark reveal both read the
   button's data-state, which is more legible here than three nested variants. */

.tab-18 [data-state="loading"] > span,
.tab-18 [data-state="success"] > span {
  opacity: 0;
}

.tab-18 [data-state="success"] > svg {
  opacity: 1;
  scale: 1;
}

.tab-18 [data-state="success"] polyline {
  animation: var(--animate-tab18-draw);
}

.tab-18 {
  width: 100%;
  min-height: 100svh;
}

.tab-18 ::selection {
  background: var(--color-tab18-primary);
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .tab-18 [data-state="success"] polyline {
    animation: none;
    stroke-dashoffset: 0;
  }
}
```

## JavaScript
```js
(function () {
  var status = document.getElementById('tab18-status');
  document.querySelectorAll('.tab-18 .tab18-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      if (btn.dataset.state !== 'idle') return;
      btn.dataset.state = 'loading';
      btn.disabled = true;
      btn.setAttribute('aria-busy', 'true');
      if (status) status.textContent = 'Saving\u2026';
      setTimeout(function () {
        btn.dataset.state = 'success';
        btn.setAttribute('aria-busy', 'false');
        if (status) status.textContent = 'Saved.';
        setTimeout(function () {
          btn.dataset.state = 'idle';
          btn.disabled = false;
          if (status) status.textContent = '';
        }, 1800);
      }, 2000);
    });
  });
})();
```
