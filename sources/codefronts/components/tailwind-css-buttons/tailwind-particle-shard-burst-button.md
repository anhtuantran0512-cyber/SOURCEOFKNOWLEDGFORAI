---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-particle-shard-burst-button/"
title: "Tailwind Particle Shard Burst Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Every press shatters a ring of glass shards outward, each with its own angle, distance, spin and lifetime — spawned as real elements, animated by one…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Particle Shard Burst Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-particle-shard-burst-button/

Every press shatters a ring of glass shards outward, each with its own angle, distance, spin and lifetime — spawned as real elements, animated by one keyframe, and removed on animationend so the DOM never grows. The shard's look is a class list the JS applies; its trajectory is inline data.
## HTML
```html
<div class="tb-20 w-full min-h-svh grid place-items-center font-tb20-sans p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-20__btn relative cursor-pointer grid place-items-center min-h-14 px-8 border border-tb20-line rounded-[0.85rem] text-[0.9375rem] font-semibold tracking-[0.02em] text-tb20-ink bg-[linear-gradient(180deg,var(--color-tb20-btn-lift),var(--color-tb20-btn))] shadow-[0_16px_34px_-20px_#000000e6] transition-[scale,border-color] duration-250 ease-tb20-out [-webkit-tap-highlight-color:transparent] hover:border-tb20-line-hot active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tb20-s1 motion-reduce:transition-none">
    <span aria-hidden="true" class="tb-20__shards absolute inset-0 z-10 pointer-events-none"></span>
    <span class="relative z-20">Shatter</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb20-bg: #0a0a10;
  --color-tb20-bg: oklch(0.12 0.015 285);
  --color-tb20-btn: #15151f;
  --color-tb20-btn: oklch(0.22 0.02 285);
  --color-tb20-btn-lift: #1d1d29;
  --color-tb20-btn-lift: oklch(0.26 0.02 285);
  --color-tb20-line: #2b2b3a;
  --color-tb20-line: oklch(0.33 0.02 285);
  --color-tb20-line-hot: #4d7d94;
  --color-tb20-line-hot: oklch(0.58 0.07 226);
  --color-tb20-ink: #f4f4fa;
  --color-tb20-ink: oklch(0.97 0.004 285);
  --color-tb20-s1: #7dd3fc;
  --color-tb20-s1: oklch(0.84 0.11 226);
  --color-tb20-s2: #c4b5fd;
  --color-tb20-s2: oklch(0.82 0.1 293);
  --color-tb20-s3: #fda4af;
  --color-tb20-s3: oklch(0.82 0.1 15);
  --font-tb20-sans: "Space Grotesk", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb20-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb20-fly: tb-20-fly var(--t, 700ms) cubic-bezier(0.14, 0.8, 0.3, 1) forwards;
}

@keyframes tb-20-fly {
  0% {
    translate: 0 0;
    scale: 0.35;
    opacity: 1;
  }

  100% {
    translate: 0 calc(var(--d, 60px) * -1);
    scale: 0.95;
    opacity: 0;
  }
}

.tb-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(40rem 24rem at 50% 50%, color-mix(in oklab, var(--color-tb20-s2) 10%, transparent), transparent 72%), var(--color-tb20-bg);
}
/* Each shard's own angle: set inline by the controller, applied here because a
   rotate utility cannot read a per-element variable. */

.tb-20__shards > span {
  rotate: var(--a, 0deg);
}

@media (prefers-color-scheme: light) {
  .tb-20:not([data-theme="dark"]) {
    --color-tb20-bg: oklch(0.95 0.008 285);
  }
}

.tb-20[data-theme="light"] {
  --color-tb20-bg: oklch(0.95 0.008 285);
}

@media (forced-colors: active) {
  .tb-20__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .tb-20__shards {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.tb-20__btn');
  const layer = btn && btn.querySelector('.tb-20__shards');
  if (!layer) return;
  const calm = matchMedia('(prefers-reduced-motion: reduce)');
  // The particle's SKIN lives here as Tailwind classes; its TRAJECTORY is inline data.
  const BASE = 'absolute top-1/2 left-1/2 opacity-0 animate-tb20-fly ';
  const SLIVER = BASE + 'w-3 h-[0.28rem] -mt-[0.14rem] -ml-1.5 [clip-path:polygon(0_50%,55%_0,100%_42%,62%_100%)] ';
  const CHIP = BASE + 'size-2 -mt-1 -ml-1 [clip-path:polygon(50%_0,100%_38%,80%_100%,18%_92%,0_34%)] ';
  btn.addEventListener('click', () => {
    if (calm.matches || layer.childElementCount > 40) return;
    for (let i = 0; i < 12; i++) {
      const s = document.createElement('span');
      s.className = i % 3 === 0 ? CHIP + 'bg-tb20-s2' : (i % 3 === 1 ? SLIVER + 'bg-tb20-s3' : SLIVER + 'bg-tb20-s1');
      s.style.setProperty('--a', ((i / 12) * 360 + (Math.random() * 22 - 11)).toFixed(1) + 'deg');
      s.style.setProperty('--d', (46 + Math.random() * 54).toFixed(0) + 'px');
      s.style.setProperty('--t', (520 + Math.random() * 380).toFixed(0) + 'ms');
      s.addEventListener('animationend', () => s.remove());
      layer.appendChild(s);
    }
  });
})();
```
