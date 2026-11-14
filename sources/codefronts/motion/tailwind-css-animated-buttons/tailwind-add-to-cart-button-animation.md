---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-add-to-cart-button-animation/"
title: "Tailwind Add to Cart Button with Flying Product Dot"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "A dot leaps from the cursor into the cart badge, the count ticks, and the button flashes confirmation."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Add to Cart Button with Flying Product Dot
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-add-to-cart-button-animation/

A dot leaps from the cursor into the cart badge, the count ticks, and the button flashes confirmation. JS measures the flight vector once per click and hands it to CSS as two custom properties &mdash; the arc itself is a keyframe.
## HTML
```html
<section class="tab-15 w-full min-h-svh grid place-items-center bg-tab15-bg font-tab15-sans px-6 py-10">
  <div class="w-[min(360px,100%)] p-6 bg-white rounded-2xl shadow-[0_4px_24px_oklch(0_0_0/0.08)]">
    <div class="flex items-center gap-4 mb-5">
      <div class="size-18 shrink-0 rounded-[10px] bg-[linear-gradient(135deg,#fde68a,#f59e0b)]"></div>
      <div>
        <p class="text-[0.95rem] font-bold text-tab15-ink m-0">Mechanical Keyboard Pro</p>
        <p class="mt-1.5 text-[1.15rem] font-bold text-tab15-amber m-0">$149.00</p>
      </div>
    </div>
    <div class="relative">
      <button type="button" id="tab15-btn" data-state="idle" class="relative flex items-center gap-2.5 w-full min-h-11 px-6 text-[0.95rem] font-bold text-white bg-tab15-ink rounded-[10px] cursor-pointer transition-[background-color,translate] duration-300 hover:bg-tab15-ink-soft hover:-translate-y-px active:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab15-ink data-[state=added]:bg-tab15-done motion-reduce:transition-none">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="size-5 shrink-0">
          <circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/>
          <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
        </svg>
        <span>Add to Cart</span>
        <span id="tab15-badge" class="absolute -top-2 -right-2 grid place-items-center min-w-5 h-5 px-1.5 text-[0.72rem] font-bold text-white bg-tab15-amber border-2 border-white rounded-full data-pop:animate-tab15-pop motion-reduce:data-pop:animate-none">0</span>
      </button>
      <p id="tab15-status" role="status" aria-live="polite" class="sr-only"></p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab15-bg: #fff7ed;
  --color-tab15-bg: oklch(0.97 0.02 75);
  --color-tab15-ink: #1e293b;
  --color-tab15-ink: oklch(0.28 0.03 258);
  --color-tab15-ink-soft: #334155;
  --color-tab15-ink-soft: oklch(0.37 0.03 258);
  --color-tab15-amber: #b45309;
  --color-tab15-amber: oklch(0.53 0.15 62);
  --color-tab15-done: #059669;
  --color-tab15-done: oklch(0.58 0.14 163);
  --font-tab15-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tab15-fly: tab15-fly 0.65s cubic-bezier(0.4, 0, 0.2, 1) forwards;
  --animate-tab15-pop: tab15-pop 0.3s ease both;
}

@keyframes tab15-fly {
  0% {
    translate: 0 0;
    scale: 1;
    opacity: 1;
  }

  50% {
    translate: calc(var(--tx) * 0.5) calc(var(--ty) * 0.5 - 40px);
    scale: 0.8;
    opacity: 0.9;
  }

  100% {
    translate: var(--tx) var(--ty);
    scale: 0;
    opacity: 0;
  }
}

@keyframes tab15-pop {
  0% {
    scale: 1;
  }

  50% {
    scale: 1.5;
  }

  100% {
    scale: 1;
  }
}

.tab-15 {
  width: 100%;
  min-height: 100svh;
}

.tab-15 ::selection {
  background: var(--color-tab15-amber);
  color: #fff;
}
```

## JavaScript
```js
(function () {
  var btn = document.getElementById('tab15-btn');
  var badge = document.getElementById('tab15-badge');
  var status = document.getElementById('tab15-status');
  if (!btn || !badge) return;
  var count = 0;
  var calm = window.matchMedia('(prefers-reduced-motion: reduce)');
  function bump() {
    count++;
    badge.textContent = String(count);
    badge.removeAttribute('data-pop');
    void badge.offsetWidth;
    badge.setAttribute('data-pop', '');
    if (status) status.textContent = count + (count === 1 ? ' item in cart' : ' items in cart');
  }
  btn.addEventListener('click', function (e) {
    btn.dataset.state = 'added';
    setTimeout(function () { btn.dataset.state = 'idle'; }, 800);
    if (calm.matches) { bump(); return; }
    var target = badge.getBoundingClientRect();
    var startX = e.clientX - 5;
    var startY = e.clientY - 5;
    var dot = document.createElement('div');
    dot.className = 'fixed size-2.5 rounded-full bg-tab15-amber pointer-events-none z-[9999] animate-tab15-fly will-change-transform';
    dot.style.left = startX + 'px';
    dot.style.top = startY + 'px';
    dot.style.setProperty('--tx', (target.left + target.width / 2 - 5 - startX) + 'px');
    dot.style.setProperty('--ty', (target.top + target.height / 2 - 5 - startY) + 'px');
    document.body.appendChild(dot);
    dot.addEventListener('animationend', function () { dot.remove(); bump(); });
  });
})();
```
