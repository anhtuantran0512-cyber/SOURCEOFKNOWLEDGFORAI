---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-click-to-flip-card-persisted-state-keyboard/"
title: "Tailwind Click-to-Flip Card with Persisted State & Keyboard Control"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "The explicitly scripted variant: no hover trigger at all, a real <button> that owns aria-expanded, and the flipped state persisted to localStorage so a…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Click-to-Flip Card with Persisted State & Keyboard Control
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-click-to-flip-card-persisted-state-keyboard/

The explicitly scripted variant: no hover trigger at all, a real <button> that owns aria-expanded, and the flipped state persisted to localStorage so a reload does not throw the reader back to the front. State lives in a data-flipped attribute, which Tailwind reads with data-flipped: &mdash; no .is-flipped class, no string matching in the stylesheet.
## HTML
```html
<section class="tfc-16 w-full min-h-svh grid place-items-center content-center gap-5 bg-tfc16-bg font-tfc16-sans px-5 py-10 text-tfc16-ink">
  <div class="text-center">
    <h2 class="text-base font-bold text-white">Click-to-flip &middot; scripted toggle</h2>
    <p class="mt-1 text-[11px] text-tfc16-muted">No hover trigger &mdash; the state is a data attribute, and it survives a reload</p>
    <p class="mt-2 inline-flex items-center gap-1.5 rounded-full border border-tfc16-orange/25 bg-tfc16-orange/12 px-3.5 py-1.5 text-[11px] text-tfc16-orange">
      <span class="size-1.5 rounded-full bg-tfc16-orange animate-tfc16-pulse motion-reduce:animate-none"></span>Use the button, or press Enter
    </p>
  </div>

  <div class="relative mx-auto h-[430px] w-[340px] max-w-full [perspective:1200px]">
    <div id="tfc-16-card" data-flipped="false" class="relative h-full w-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] data-[flipped=true]:[transform:rotateY(180deg)] motion-reduce:transition-none">

      <div class="absolute inset-0 flex flex-col items-center justify-center gap-4 rounded-2xl overflow-hidden px-7 py-9 bg-linear-145 from-tfc16-panel to-tfc16-panel2 border border-tfc16-orange/25 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.55_0.18_45/0.4)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden] before:absolute before:inset-0 before:bg-[radial-gradient(circle_at_50%_40%,oklch(0.7_0.19_45/0.08),transparent_60%)]">
        <span class="relative z-1 grid size-20 place-items-center rounded-3xl border border-tfc16-orange/25 bg-linear-135 from-tfc16-orange/15 to-tfc16-yellow/8 shadow-[0_0_30px_oklch(0.7_0.19_45/0.12)]">
          <svg viewBox="0 0 24 24" class="size-9 fill-none stroke-tfc16-orange stroke-[1.8]" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
        </span>
        <p class="relative z-1 text-[10px] font-bold uppercase tracking-[0.15em] text-tfc16-orange">Click trigger &middot; scripted</p>
        <h3 class="relative z-1 text-center text-2xl font-black tracking-[-0.02em] text-white">Click to flip</h3>
        <p class="relative z-1 text-center text-[13px] leading-[1.6] text-tfc16-muted text-pretty">This card flips on click, never on hover &mdash; which is the only version that behaves the same on a phone as on a desktop.</p>
        <button id="tfc-16-toggle" type="button" aria-expanded="false" aria-controls="tfc-16-back" class="relative z-30 mt-2 inline-flex min-h-11 items-center gap-2 rounded-xl bg-linear-135 from-tfc16-orange to-tfc16-yellow px-6 text-[13px] font-extrabold tracking-[0.04em] text-black shadow-[0_4px_20px_oklch(0.7_0.19_45/0.3)] transition-[filter,box-shadow] duration-150 hover:brightness-110 active:brightness-95 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg>
          Click to reveal
        </button>
      </div>

      <div id="tfc-16-back" class="absolute inset-0 flex flex-col items-center justify-center gap-4 rounded-2xl overflow-hidden px-7 py-9 bg-linear-145 from-tfc16-back to-tfc16-back2 border border-tfc16-green/25 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.6_0.17_150/0.35)] [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <span class="grid size-20 place-items-center rounded-3xl border border-tfc16-green/20 bg-tfc16-green/10">
          <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" class="text-tfc16-green" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        </span>
        <h3 class="text-center text-[22px] font-black tracking-[-0.02em] text-white">Flip complete</h3>
        <p class="text-center text-[13px] leading-[1.6] text-tfc16-muted text-pretty">The script sets <code class="rounded bg-black/30 px-1.5 py-0.5 font-tfc16-mono text-tfc16-green">data-flipped</code> and Tailwind's <code class="rounded bg-black/30 px-1.5 py-0.5 font-tfc16-mono text-tfc16-green">data-[flipped=true]:</code> variant styles it.</p>
        <pre class="w-full rounded-xl border border-white/8 bg-black/40 px-4 py-3 text-left font-tfc16-mono text-[11px] leading-[1.7] text-tfc16-ink/60"><span class="text-tfc16-ink/30">// one attribute, one source of truth</span>
card.dataset.<span class="text-tfc16-green">flipped</span> = <span class="text-tfc16-orangeL">'true'</span>;</pre>
        <button id="tfc-16-back-btn" type="button" class="relative z-30 min-h-11 rounded-xl border border-tfc16-green/30 bg-tfc16-green/10 px-6 text-[13px] font-bold text-tfc16-green transition-colors duration-200 hover:bg-tfc16-green/20 focus-visible:outline-2 focus-visible:outline-tfc16-green focus-visible:outline-offset-2">&larr; Flip back</button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc16-bg: #0c0800;
  --color-tfc16-bg: oklch(0.14 0.02 70);
  --color-tfc16-panel: #1a0e00;
  --color-tfc16-panel: oklch(0.19 0.045 60);
  --color-tfc16-panel2: #0f0900;
  --color-tfc16-panel2: oklch(0.15 0.03 65);
  --color-tfc16-back: #0e1a0a;
  --color-tfc16-back: oklch(0.2 0.045 145);
  --color-tfc16-back2: #081008;
  --color-tfc16-back2: oklch(0.14 0.025 150);
  --color-tfc16-orange: #f97316;
  --color-tfc16-orange: oklch(0.7 0.19 45);
  --color-tfc16-orangeL: #fb923c;
  --color-tfc16-orangeL: oklch(0.76 0.16 55);
  --color-tfc16-yellow: #fbbf24;
  --color-tfc16-yellow: oklch(0.83 0.16 82);
  --color-tfc16-green: #4ade80;
  --color-tfc16-green: oklch(0.8 0.17 152);
  --color-tfc16-ink: #fffbf0;
  --color-tfc16-ink: oklch(0.99 0.015 90);
  --color-tfc16-muted: #bdb09c;
  --color-tfc16-muted: oklch(0.77 0.03 85);
  --font-tfc16-sans: 'Sora', system-ui, sans-serif;
  --font-tfc16-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tfc16-pulse: tfc16-pulse 1.5s ease-in-out infinite;
}

@keyframes tfc16-pulse {
  0%,
    100% {
    opacity: 0.4;
    transform: scale(0.8);
  }

  50% {
    opacity: 1;
    transform: scale(1);
  }
}

.tfc-16 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-16 * {
    animation: none !important;
    transition-duration: 1ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.getElementById('tfc-16-card');
  const toggle = document.getElementById('tfc-16-toggle');
  const backBtn = document.getElementById('tfc-16-back-btn');
  const KEY = 'tfc-16-flipped';
  if (!card) return;

  const set = (flipped) => {
    card.dataset.flipped = String(flipped);
    toggle.setAttribute('aria-expanded', String(flipped));
    try { localStorage.setItem(KEY, String(flipped)); } catch {}
  };

  // Restore without animating the restore frame.
  try {
    if (localStorage.getItem(KEY) === 'true') {
      card.classList.add('transition-none');
      set(true);
      requestAnimationFrame(() => card.classList.remove('transition-none'));
    }
  } catch {}

  toggle.addEventListener('click', () => set(card.dataset.flipped !== 'true'));
  backBtn.addEventListener('click', (e) => { e.stopPropagation(); set(false); });
})();
```
