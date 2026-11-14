---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-animated-cta-hero-button/"
title: "Tailwind Animated CTA Hero Button with Beacon Rings & Particle Burst"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "A landing-page CTA with two radar rings pinging outward and a particle burst on click."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated CTA Hero Button with Beacon Rings & Particle Burst
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-animated-cta-hero-button/

A landing-page CTA with two radar rings pinging outward and a particle burst on click. The rings are pure utilities on one wrapper's two pseudo-elements; the JS does nothing but stamp a vector onto each particle and let the animation system handle every frame.
## HTML
```html
<section class="tab-11 w-full min-h-svh grid place-items-center bg-tab11-bg font-tab11-sans px-6 py-10">
  <div class="w-[min(520px,100%)] text-center">
    <p class="text-[0.8rem] tracking-[0.16em] uppercase text-tab11-beacon m-0">&#10022; Now in public beta</p>
    <h1 class="mt-4 mb-4 text-[clamp(2rem,5vw,3rem)] font-bold leading-[1.1] text-white">The dev platform<br>built for speed.</h1>
    <p class="mb-8 text-base leading-relaxed text-tab11-mut">Deploy anywhere. Scale effortlessly. Ship today.</p>
    <span id="tab11-wrap" class="relative inline-block mb-4 before:content-[''] before:absolute before:-inset-1.5 before:rounded-2xl before:border-2 before:border-tab11-beacon before:opacity-0 before:animate-tab11-beacon before:pointer-events-none after:content-[''] after:absolute after:-inset-1.5 after:rounded-2xl after:border-2 after:border-tab11-beacon after:opacity-0 after:animate-tab11-beacon after:[animation-delay:0.7s] after:pointer-events-none motion-reduce:before:animate-none motion-reduce:after:animate-none">
      <button type="button" id="tab11-btn" class="relative z-10 min-h-11 px-10 py-3.5 text-[1.05rem] font-bold tracking-[0.03em] text-white rounded-xl cursor-pointer bg-[linear-gradient(135deg,#7c3aed,#2563eb)] shadow-[0_4px_24px_oklch(0.53_0.25_295/0.45)] transition-[translate,filter] duration-150 hover:brightness-110 hover:-translate-y-0.5 active:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white motion-reduce:transition-none">Start Building Free</button>
    </span>
    <p class="text-[0.75rem] text-tab11-dim">No credit card &middot; 50k free API calls included</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab11-bg: #050510;
  --color-tab11-bg: oklch(0.07 0.02 280);
  --color-tab11-beacon: #a78bfa;
  --color-tab11-beacon: oklch(0.74 0.15 292);
  --color-tab11-mut: #94a3b8;
  --color-tab11-mut: oklch(0.72 0.03 255);
  --color-tab11-dim: #64748b;
  --color-tab11-dim: oklch(0.55 0.03 255);
  --font-tab11-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tab11-beacon: tab11-beacon 2s ease-out infinite;
  --animate-tab11-burst: tab11-burst 0.7s ease-out forwards;
}

@keyframes tab11-beacon {
  0% {
    scale: 1;
    opacity: 0.7;
  }

  100% {
    scale: 1.5;
    opacity: 0;
  }
}

@keyframes tab11-burst {
  0% {
    translate: -50% -50%;
    scale: 1;
    opacity: 1;
  }

  100% {
    translate: calc(-50% + var(--dx)) calc(-50% + var(--dy));
    scale: 0;
    opacity: 0;
  }
}

.tab-11 {
  width: 100%;
  min-height: 100svh;
}

.tab-11 ::selection {
  background: var(--color-tab11-beacon);
  color: #14091f;
}
```

## JavaScript
```js
(function () {
  var wrap = document.getElementById('tab11-wrap');
  var btn = document.getElementById('tab11-btn');
  if (!btn || !wrap) return;
  var COLOURS = ['#a78bfa', '#60a5fa', '#34d399', '#f472b6', '#fbbf24', '#ffffff'];
  var COUNT = 12;
  var calm = window.matchMedia('(prefers-reduced-motion: reduce)');
  btn.addEventListener('click', function (e) {
    if (calm.matches) return;
    for (var i = 0; i < COUNT; i++) {
      var p = document.createElement('span');
      p.className = 'absolute top-0 left-0 size-2 rounded-full pointer-events-none animate-tab11-burst will-change-transform';
      var angle = Math.random() * Math.PI * 2;
      var dist = 40 + Math.random() * 40;
      p.style.setProperty('--dx', Math.cos(angle) * dist + 'px');
      p.style.setProperty('--dy', Math.sin(angle) * dist + 'px');
      p.style.background = COLOURS[Math.floor(Math.random() * COLOURS.length)];
      p.style.left = e.offsetX + 'px';
      p.style.top = e.offsetY + 'px';
      wrap.appendChild(p);
      p.addEventListener('animationend', function () { this.remove(); });
    }
  });
})();
```
