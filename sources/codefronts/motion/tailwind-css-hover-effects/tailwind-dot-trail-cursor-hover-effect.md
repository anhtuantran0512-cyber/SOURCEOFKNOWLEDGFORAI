---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-dot-trail-cursor-hover-effect/"
title: "Tailwind Dot Trail Cursor Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four cursor trails inside bounded zones — classic fade, rainbow cycle, comet tail and sparkle burst."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dot Trail Cursor Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-dot-trail-cursor-hover-effect/

Four cursor trails inside bounded zones — classic fade, rainbow cycle, comet tail and sparkle burst. The controller is 30 lines; the interesting part of the port is the boundary: elements created at runtime cannot be scanned by a build, so their styling stays in CSS on purpose.
## HTML
```html
<section class="thv-29 w-full min-h-svh bg-thv29-bg font-thv29-sans px-8 py-10 select-none">
  <p class="text-center text-[0.72rem] tracking-[0.15em] uppercase text-thv29-dim mb-6">Dot Trail Cursor — 4 Styles</p>
  <div class="grid grid-cols-[repeat(auto-fit,minmax(240px,1fr))] gap-4 max-w-[740px] mx-auto">
    <div data-trail="classic" class="thv29-zone relative overflow-hidden grid place-items-center aspect-[4/3] rounded-xl border border-thv29-edge bg-thv29-panel cursor-none">
      <span class="text-[0.75rem] tracking-[0.1em] uppercase text-thv29-hint pointer-events-none">Classic Fade</span>
    </div>
    <div data-trail="rainbow" class="thv29-zone relative overflow-hidden grid place-items-center aspect-[4/3] rounded-xl border border-thv29-edge bg-thv29-panel cursor-none">
      <span class="text-[0.75rem] tracking-[0.1em] uppercase text-thv29-hint pointer-events-none">Rainbow</span>
    </div>
    <div data-trail="comet" class="thv29-zone relative overflow-hidden grid place-items-center aspect-[4/3] rounded-xl border border-thv29-edge bg-thv29-panel cursor-none">
      <span class="text-[0.75rem] tracking-[0.1em] uppercase text-thv29-hint pointer-events-none">Comet Tail</span>
    </div>
    <div data-trail="sparkle" class="thv29-zone relative overflow-hidden grid place-items-center aspect-[4/3] rounded-xl border border-thv29-edge bg-thv29-panel cursor-none">
      <span class="text-[0.75rem] tracking-[0.1em] uppercase text-thv29-hint pointer-events-none">Sparkle</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv29-bg: #080810;
  --color-thv29-bg: oklch(0.12 0.02 285);
  --color-thv29-panel: #0d0d18;
  --color-thv29-panel: oklch(0.15 0.02 285);
  --color-thv29-edge: #1a1a2a;
  --color-thv29-edge: oklch(0.22 0.02 285);
  --color-thv29-dim: #8a8a99;
  --color-thv29-dim: oklch(0.64 0.02 285);
  --color-thv29-hint: #5e5e78;
  --color-thv29-hint: oklch(0.48 0.03 285);
  --font-thv29-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-thv29-classic: thv29-classic .6s ease-out forwards;
  --animate-thv29-rainbow: thv29-rainbow .7s ease-out forwards;
  --animate-thv29-comet: thv29-comet .5s ease-out forwards;
  --animate-thv29-sparkle: thv29-sparkle .65s ease-out forwards;
}

.thv-29 {
  width: 100%;
  min-height: 100svh;
}

.thv-29 ::selection {
  background: #ffffff;
  color: #000;
}
/* Runtime-generated elements: the JS mints these nodes after the build has
   scanned the document, so their styling cannot live in utilities without a
   safelist. Four rules is the honest cost of the port. */

.thv29-dot {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  transform: translate(-50%, -50%);
  will-change: transform, opacity;
}

[data-trail="classic"] .thv29-dot {
  width: 8px;
  height: 8px;
  background: #fff;
  animation: var(--animate-thv29-classic);
}

[data-trail="rainbow"] .thv29-dot {
  width: 10px;
  height: 10px;
  animation: var(--animate-thv29-rainbow);
}

[data-trail="comet"] .thv29-dot {
  width: 12px;
  height: 4px;
  border-radius: 2px;
  background: linear-gradient(90deg, rgba(100,180,255,0), rgba(100,180,255,1));
  animation: var(--animate-thv29-comet);
}

[data-trail="sparkle"] .thv29-dot {
  width: 10px;
  height: 10px;
  background: #f7d060;
  clip-path: polygon(50% 0%,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%);
  animation: var(--animate-thv29-sparkle);
}

@keyframes thv29-classic {
  0% {
    opacity: .9;
    transform: translate(-50%,-50%) scale(1);
  }

  100% {
    opacity: 0;
    transform: translate(-50%,-50%) scale(0);
  }
}

@keyframes thv29-rainbow {
  0% {
    opacity: 1;
    transform: translate(-50%,-50%) scale(1.1);
  }

  100% {
    opacity: 0;
    transform: translate(-50%,-50%) scale(.1);
  }
}

@keyframes thv29-comet {
  0% {
    opacity: 1;
    transform: translate(-50%,-50%) scale(1,1);
  }

  100% {
    opacity: 0;
    transform: translate(-50%,-50%) scale(3,.3);
  }
}

@keyframes thv29-sparkle {
  0% {
    opacity: 1;
    transform: translate(-50%,-50%) scale(0) rotate(0deg);
  }

  60% {
    opacity: 1;
    transform: translate(-50%,-50%) scale(1.3) rotate(60deg);
  }

  100% {
    opacity: 0;
    transform: translate(-50%,-50%) scale(.4) rotate(90deg);
  }
}
```

## JavaScript
```js
(function () {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const zones = document.querySelectorAll('.thv29-zone');
  const RAINBOW = ['#ff6b6b','#ffa94d','#ffd43b','#69db7c','#4dabf7','#cc5de8','#f783ac'];
  let hueIndex = 0, rafId = null, pendingZone = null, pendingX = 0, pendingY = 0;

  function spawnDot(zone, x, y) {
    const dot = document.createElement('span');
    dot.className = 'thv29-dot';
    dot.style.left = x + 'px';
    dot.style.top = y + 'px';
    if (zone.dataset.trail === 'rainbow') {
      dot.style.background = RAINBOW[hueIndex++ % RAINBOW.length];
    }
    zone.appendChild(dot);
    dot.addEventListener('animationend', () => dot.remove(), { once: true });
  }

  function onMove(e) {
    const zone = e.currentTarget;
    const rect = zone.getBoundingClientRect();
    pendingX = e.clientX - rect.left;
    pendingY = e.clientY - rect.top;
    pendingZone = zone;
    if (!rafId) {
      rafId = requestAnimationFrame(() => {
        if (pendingZone) spawnDot(pendingZone, pendingX, pendingY);
        rafId = null;
      });
    }
  }

  zones.forEach((zone) => {
    zone.addEventListener('mousemove', onMove);
    zone.addEventListener('mouseleave', () => { pendingZone = null; });
  });
})();
```
