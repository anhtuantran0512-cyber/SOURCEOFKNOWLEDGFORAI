---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-interactive-pointer-trail-image-gallery/"
title: "Tailwind Interactive Pointer Trail Image Gallery"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "A canvas where photographs bloom behind the cursor, drift and fade."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Interactive Pointer Trail Image Gallery
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-interactive-pointer-trail-image-gallery/

A canvas where photographs bloom behind the cursor, drift and fade. CSS owns every frame of the motion; twelve lines of JavaScript decide only where and when to spawn. In Tailwind the spawned node's entire look is one class string the script assigns, which is the cleanest possible split between behaviour and style.
## HTML
```html
<section class="tgl-06 w-full min-h-svh grid place-items-center px-5 py-10 font-tgl06-sans bg-[radial-gradient(120%_120%_at_50%_30%,oklch(0.22_0.04_300),oklch(0.09_0.02_285))]" aria-label="Interactive pointer trail gallery">
  <div id="tgl-06-canvas" role="img" aria-label="Move your cursor to leave a trail of images" class="relative w-[min(860px,100%)] h-[min(520px,70vh)] rounded-[20px] overflow-hidden cursor-crosshair touch-none border border-white/10 bg-[linear-gradient(135deg,rgba(255,255,255,0.03),rgba(255,255,255,0.01))]">
    <p class="absolute inset-0 grid place-items-center m-0 text-white/40 font-tgl06-mono text-xs tracking-[0.2em] uppercase pointer-events-none">move your cursor across the canvas</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl06-acc: #d982e8;
  --color-tgl06-acc: oklch(0.74 0.17 320);
  --font-tgl06-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tgl06-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-tgl06-bloom: tgl06-bloom 1.1s cubic-bezier(0.2, 0.7, 0.2, 1) forwards;
}

@keyframes tgl06-bloom {
  0% {
    opacity: 0;
    transform: scale(0.4) rotate(-6deg);
  }

  18% {
    opacity: 1;
    transform: scale(1) rotate(0deg);
  }

  100% {
    opacity: 0;
    transform: scale(0.86) translateY(40px) rotate(4deg);
  }
}

.tgl-06 {
  width: 100%;
  min-height: 100svh;
}

.tgl-06 ::selection {
  background: var(--color-tgl06-acc);
  color: #fff;
}
```

## JavaScript
```js
(function () {
  var canvas = document.getElementById('tgl-06-canvas');
  if (!canvas) return;
  if (matchMedia('(hover:none)').matches || matchMedia('(prefers-reduced-motion:reduce)').matches) return;

  // The spawned node's entire appearance, as Tailwind utilities.
  var SPARK = 'absolute w-[120px] h-[150px] -mt-[75px] -ml-[60px] rounded-xl object-cover ' +
              'pointer-events-none will-change-[transform,opacity] ' +
              'shadow-[0_12px_30px_-12px_rgba(0,0,0,0.6)] animate-tgl06-bloom';

  var pool = [1801, 1803, 1002, 1601, 1101, 1301].map(function (n) {
    return 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=240&h=300&auto=format&fit=crop?lock=' + n;
  });

  var i = 0, last = 0;
  canvas.addEventListener('pointermove', function (e) {
    var now = Date.now();
    if (now - last < 90) return;          // throttle spawn rate
    last = now;
    var r = canvas.getBoundingClientRect();
    var img = document.createElement('img');
    img.className = SPARK;
    img.alt = '';
    img.setAttribute('aria-hidden', 'true');
    img.src = pool[i % pool.length]; i++;
    img.style.left = (e.clientX - r.left) + 'px';
    img.style.top = (e.clientY - r.top) + 'px';
    img.addEventListener('animationend', function () { img.remove(); }, { once: true });
    canvas.appendChild(img);
  });
})();
```
