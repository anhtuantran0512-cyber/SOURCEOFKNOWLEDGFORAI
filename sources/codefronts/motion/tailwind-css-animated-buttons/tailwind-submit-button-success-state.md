---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-submit-button-success-state/"
title: "Tailwind Submit Button Success State with Checkmark Draw"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "A submit button that collapses into a circle and draws a checkmark."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Submit Button Success State with Checkmark Draw
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-submit-button-success-state/

A submit button that collapses into a circle and draws a checkmark. The port replaces a class toggle with data-state, so the markup reads data-[state=success]:w-12 and the impossible state ("success and idle at once") stops existing.
## HTML
```html
<section class="tab-12 w-full min-h-svh grid place-items-center bg-tab12-bg font-tab12-sans px-6 py-10">
  <div class="w-[min(380px,100%)] p-8 bg-white rounded-2xl shadow-[0_4px_24px_oklch(0_0_0/0.08)]">
    <h2 class="text-[1.4rem] font-bold text-tab12-ink m-0">Contact Us</h2>
    <p class="mt-1.5 mb-6 text-[0.88rem] leading-relaxed text-tab12-mut">We'll get back to you within 24 hours.</p>
    <label class="block mb-3.5">
      <span class="sr-only">Your name</span>
      <input type="text" placeholder="Your name" class="w-full min-h-11 px-4 text-[0.9rem] text-tab12-ink bg-tab12-bg border-[1.5px] border-tab12-edge rounded-lg transition-colors duration-200 focus:border-tab12-primary focus:outline-2 focus:outline-offset-2 focus:outline-tab12-primary/40">
    </label>
    <label class="block mb-4">
      <span class="sr-only">Email address</span>
      <input type="email" placeholder="Email address" class="w-full min-h-11 px-4 text-[0.9rem] text-tab12-ink bg-tab12-bg border-[1.5px] border-tab12-edge rounded-lg transition-colors duration-200 focus:border-tab12-primary focus:outline-2 focus:outline-offset-2 focus:outline-tab12-primary/40">
    </label>
    <div class="flex justify-center">
      <button type="button" id="tab12-btn" data-state="idle" class="relative flex items-center justify-center w-full h-12 px-6 text-base font-bold text-white bg-tab12-primary rounded-full cursor-pointer overflow-hidden shadow-[0_4px_16px_oklch(0.51_0.24_277/0.3)] transition-[width,background-color,box-shadow] duration-[400ms] ease-[cubic-bezier(0.4,0,0.2,1)] hover:brightness-108 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab12-primary data-[state=success]:w-12 data-[state=success]:bg-tab12-success data-[state=success]:shadow-[0_4px_16px_oklch(0.7_0.15_163/0.35)] data-[state=success]:cursor-default motion-reduce:transition-none">
        <span class="whitespace-nowrap transition-[opacity,scale] duration-200">Send Message</span>
        <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="absolute size-6 opacity-0 scale-50 transition-[opacity,scale] duration-300 delay-[350ms]">
          <polyline points="20 6 9 17 4 12" pathLength="30" stroke-dasharray="30" stroke-dashoffset="30"></polyline>
        </svg>
      </button>
    </div>
    <p id="tab12-status" role="status" aria-live="polite" class="mt-3 text-center text-[0.8rem] text-tab12-mut min-h-5"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab12-bg: #f8fafc;
  --color-tab12-bg: oklch(0.98 0.004 250);
  --color-tab12-ink: #1e293b;
  --color-tab12-ink: oklch(0.28 0.03 258);
  --color-tab12-mut: #64748b;
  --color-tab12-mut: oklch(0.55 0.03 255);
  --color-tab12-edge: #e2e8f0;
  --color-tab12-edge: oklch(0.92 0.01 250);
  --color-tab12-primary: #4f46e5;
  --color-tab12-primary: oklch(0.51 0.24 277);
  --color-tab12-success: #10b981;
  --color-tab12-success: oklch(0.7 0.15 163);
  --font-tab12-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tab12-draw: tab12-draw 0.4s ease 0.4s forwards;
}

@keyframes tab12-draw {
  from {
    stroke-dashoffset: 30;
  }

  to {
    stroke-dashoffset: 0;
  }
}
/* The two state-driven child rules that have no variant form worth writing:
   the label fade and the checkmark reveal both key off the parent's data-state. */

.tab-12 [data-state="success"] > span {
  opacity: 0;
  scale: 0.6;
  position: absolute;
}

.tab-12 [data-state="success"] > svg {
  opacity: 1;
  scale: 1;
}

.tab-12 [data-state="success"] polyline {
  animation: var(--animate-tab12-draw);
}

.tab-12 {
  width: 100%;
  min-height: 100svh;
}

.tab-12 ::selection {
  background: var(--color-tab12-success);
  color: #04231a;
}

@media (prefers-reduced-motion: reduce) {
  .tab-12 [data-state="success"] polyline {
    animation: none;
    stroke-dashoffset: 0;
  }
}
```

## JavaScript
```js
(function () {
  var btn = document.getElementById('tab12-btn');
  var status = document.getElementById('tab12-status');
  if (!btn) return;
  var timer = null;
  btn.addEventListener('click', function () {
    if (btn.dataset.state === 'success') return;
    btn.dataset.state = 'success';
    btn.disabled = true;
    btn.setAttribute('aria-busy', 'false');
    if (status) status.textContent = 'Message sent.';
    clearTimeout(timer);
    timer = setTimeout(function () {
      btn.dataset.state = 'idle';
      btn.disabled = false;
      if (status) status.textContent = '';
    }, 2500);
  });
})();
```
