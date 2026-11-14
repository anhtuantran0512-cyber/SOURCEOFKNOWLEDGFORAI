---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-next-prev-arrow-button-hover/"
title: "Tailwind Next & Prev Arrow Buttons with Chasing Icons"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "Slider controls where the arrow slides out as a duplicate slides in behind it."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Next & Prev Arrow Buttons with Chasing Icons
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-next-prev-arrow-button-hover/

Slider controls where the arrow slides out as a duplicate slides in behind it. The port swaps a fake .is-disabled class for the real disabled attribute, so disabled: handles the styling and the browser handles the blocking.
## HTML
```html
<section class="tab-19 w-full min-h-svh grid place-items-center bg-tab19-bg font-tab19-sans px-6 py-10">
  <div class="flex flex-col items-center gap-8">
    <div class="w-[min(480px,100%)] min-h-[130px] p-8 bg-tab19-card border border-white/8 rounded-2xl" role="group" aria-live="polite">
      <p id="tab19-label" class="text-[0.72rem] tracking-[0.12em] uppercase text-tab19-dim m-0">Slide 1 of 5</p>
      <h3 id="tab19-title" class="mt-2.5 mb-2 text-[1.3rem] font-bold text-tab19-ink">Effortless Deployment</h3>
      <p id="tab19-body" class="text-[0.88rem] leading-relaxed text-tab19-mut m-0">Push your code and watch it go live in seconds. Zero config, zero downtime.</p>
    </div>
    <div class="flex items-center gap-5">
      <button type="button" id="tab19-prev" aria-label="Previous slide" disabled class="group relative grid place-items-center size-11 overflow-hidden text-tab19-ink bg-tab19-card border-[1.5px] border-white/10 rounded-[10px] cursor-pointer transition-[background-color,border-color,scale] duration-200 hover:not-disabled:bg-tab19-card-hi hover:not-disabled:border-tab19-acc/50 hover:not-disabled:scale-105 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab19-acc disabled:opacity-35 disabled:cursor-not-allowed motion-reduce:transition-none">
        <span class="relative grid place-items-center size-6 overflow-hidden">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="absolute size-[22px] transition-transform duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:not-disabled:-translate-x-[120%] motion-reduce:transition-none"><polyline points="15 18 9 12 15 6"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="absolute size-[22px] translate-x-[120%] pointer-events-none transition-transform duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:not-disabled:translate-x-0 motion-reduce:transition-none"><polyline points="15 18 9 12 15 6"/></svg>
        </span>
      </button>
      <span id="tab19-counter" class="min-w-15 text-center text-[0.85rem] font-bold tracking-[0.08em] text-tab19-mut data-tick:animate-tab19-tick motion-reduce:data-tick:animate-none">01 / 05</span>
      <button type="button" id="tab19-next" aria-label="Next slide" class="group relative grid place-items-center size-11 overflow-hidden text-tab19-ink bg-tab19-card border-[1.5px] border-white/10 rounded-[10px] cursor-pointer transition-[background-color,border-color,scale] duration-200 hover:not-disabled:bg-tab19-card-hi hover:not-disabled:border-tab19-acc/50 hover:not-disabled:scale-105 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab19-acc disabled:opacity-35 disabled:cursor-not-allowed motion-reduce:transition-none">
        <span class="relative grid place-items-center size-6 overflow-hidden">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="absolute size-[22px] transition-transform duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:not-disabled:translate-x-[120%] motion-reduce:transition-none"><polyline points="9 18 15 12 9 6"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="absolute size-[22px] -translate-x-[120%] pointer-events-none transition-transform duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:not-disabled:translate-x-0 motion-reduce:transition-none"><polyline points="9 18 15 12 9 6"/></svg>
        </span>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab19-bg: #0f172a;
  --color-tab19-bg: oklch(0.21 0.04 258);
  --color-tab19-card: #1e293b;
  --color-tab19-card: oklch(0.28 0.03 258);
  --color-tab19-card-hi: #334155;
  --color-tab19-card-hi: oklch(0.37 0.03 258);
  --color-tab19-ink: #e2e8f0;
  --color-tab19-ink: oklch(0.92 0.01 250);
  --color-tab19-mut: #94a3b8;
  --color-tab19-mut: oklch(0.72 0.03 255);
  --color-tab19-dim: #64748b;
  --color-tab19-dim: oklch(0.55 0.03 255);
  --color-tab19-acc: #818cf8;
  --color-tab19-acc: oklch(0.7 0.14 279);
  --font-tab19-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tab19-tick: tab19-tick 0.25s ease both;
}

@keyframes tab19-tick {
  0% {
    scale: 1.3;
  }

  100% {
    scale: 1;
  }
}

.tab-19 {
  width: 100%;
  min-height: 100svh;
}

.tab-19 ::selection {
  background: var(--color-tab19-acc);
  color: #0b1220;
}
```

## JavaScript
```js
(function () {
  var prev = document.getElementById('tab19-prev');
  var next = document.getElementById('tab19-next');
  var counter = document.getElementById('tab19-counter');
  var label = document.getElementById('tab19-label');
  var title = document.getElementById('tab19-title');
  var body = document.getElementById('tab19-body');
  if (!prev || !next || !counter || !label || !title || !body) return;
  var SLIDES = [
    ['Effortless Deployment', 'Push your code and watch it go live in seconds. Zero config, zero downtime.'],
    ['Instant Scaling', 'Handle millions of requests without touching infrastructure settings.'],
    ['Built-in Observability', 'Real-time logs, traces, and metrics out of the box.'],
    ['Zero Config Security', 'Automatic TLS, DDoS protection, and secrets management included.'],
    ['Global Edge Network', 'Your app served from 300+ PoPs worldwide, under 20ms latency.']
  ];
  var idx = 0;
  function pad(n) { return n < 10 ? '0' + n : String(n); }
  function render() {
    label.textContent = 'Slide ' + (idx + 1) + ' of ' + SLIDES.length;
    title.textContent = SLIDES[idx][0];
    body.textContent = SLIDES[idx][1];
    counter.textContent = pad(idx + 1) + ' / ' + pad(SLIDES.length);
    counter.removeAttribute('data-tick');
    void counter.offsetWidth;
    counter.setAttribute('data-tick', '');
    prev.disabled = idx === 0;
    next.disabled = idx === SLIDES.length - 1;
  }
  prev.addEventListener('click', function () { if (idx > 0) { idx--; render(); } });
  next.addEventListener('click', function () { if (idx < SLIDES.length - 1) { idx++; render(); } });
  render();
})();
```
