---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-slide-to-confirm-toggle-rail/"
title: "Tailwind Slide-to-Confirm Toggle Rail (Drag or Arrow Keys)"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The hold-to-confirm guard rebuilt as a gesture: drag the handle the full width of the rail to arm, let go early and it springs back."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Slide-to-Confirm Toggle Rail (Drag or Arrow Keys)
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-slide-to-confirm-toggle-rail/

The hold-to-confirm guard rebuilt as a gesture: drag the handle the full width of the rail to arm, let go early and it springs back. A shimmer sweeps the hint text while it waits, and the whole thing is operable with arrow keys.
## HTML
```html
<section class="ttg-31 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg31-bg font-ttg31-sans" aria-label="Slide to confirm toggle">
  <div class="w-[min(380px,100%)] flex flex-col gap-5 px-7 py-6 rounded-[22px] bg-ttg31-card border border-ttg31-edge">
    <span class="flex flex-col gap-0.5">
      <b class="text-[16px] font-bold text-ttg31-ink">Wipe staging database</b>
      <span class="text-[12.5px] text-ttg31-mute">Irreversible &middot; slide the handle to confirm</span>
    </span>
    <div id="ttg-31-rail" class="relative h-14 rounded-2xl overflow-hidden bg-ttg31-rail border border-ttg31-edge data-armed:bg-ttg31-okbg data-armed:border-ttg31-ok data-dragging:[&_.ttg31-hint]:animate-none">
      <span aria-hidden="true" class="ttg31-hint absolute inset-0 grid place-items-center text-[13px] font-semibold tracking-[0.14em] uppercase text-ttg31-hint animate-ttg31-shimmer motion-reduce:animate-none">Slide to confirm</span>
      <span aria-hidden="true" class="ttg31-done absolute inset-0 grid place-items-center text-[13px] font-bold tracking-[0.14em] uppercase text-ttg31-ok opacity-0 transition-opacity duration-200">Confirmed</span>
      <button type="button" id="ttg-31-handle" role="switch" aria-checked="false" aria-label="Slide to confirm wiping the staging database" class="absolute top-1 left-1 h-12 w-12 grid place-items-center rounded-xl border-0 cursor-grab select-none [touch-action:none] bg-ttg31-handle text-ttg31-handleink shadow-[0_4px_12px_-2px_oklch(0_0_0/0.55)] translate-x-[calc(var(--p,0)*1%)] active:cursor-grabbing focus-visible:outline-3 focus-visible:outline-ttg31-focus focus-visible:outline-offset-3">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"/></svg>
      </button>
    </div>
    <p id="ttg-31-live" aria-live="polite" class="font-ttg31-mono text-[12px] text-ttg31-mute">Locked</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg31-bg: #111319;
  --color-ttg31-bg: oklch(0.19 0.008 265);
  --color-ttg31-card: #1a1d25;
  --color-ttg31-card: oklch(0.24 0.01 265);
  --color-ttg31-edge: #2a2f3b;
  --color-ttg31-edge: oklch(0.31 0.012 265);
  --color-ttg31-rail: #202530;
  --color-ttg31-rail: oklch(0.27 0.012 265);
  --color-ttg31-handle: #e9edf5;
  --color-ttg31-handle: oklch(0.94 0.006 265);
  --color-ttg31-handleink: #1d2230;
  --color-ttg31-handleink: oklch(0.25 0.015 265);
  --color-ttg31-hint: #8d95a6;
  --color-ttg31-hint: oklch(0.66 0.015 265);
  --color-ttg31-ok: #4fd398;
  --color-ttg31-ok: oklch(0.79 0.15 160);
  --color-ttg31-okbg: #17352c;
  --color-ttg31-okbg: oklch(0.3 0.06 165);
  --color-ttg31-ink: #e8ebf3;
  --color-ttg31-ink: oklch(0.93 0.008 265);
  --color-ttg31-mute: #939bad;
  --color-ttg31-mute: oklch(0.68 0.015 265);
  --color-ttg31-focus: #6cb6f0;
  --color-ttg31-focus: oklch(0.74 0.14 235);
  --font-ttg31-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttg31-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-ttg31-shimmer: ttg31-shimmer 2.4s ease-in-out infinite;
}

@keyframes ttg31-shimmer {
  0%,
    100% {
    opacity: 0.55;
  }

  50% {
    opacity: 1;
  }
}

.ttg-31 {
  width: 100%;
  min-height: 100svh;
}
/* The handle's travel is a live pointer value, so the percentage lives on the rail as a
   custom property; only the release animates. */

#ttg-31-handle {
  transition: transform 0s;
}

#ttg-31-rail:not([data-dragging]) #ttg-31-handle {
  transition: transform 250ms cubic-bezier(0.3, 1, 0.35, 1.05);
}

#ttg-31-rail[data-armed] .ttg31-hint {
  animation: none;
  opacity: 0;
  transition: opacity 150ms linear;
}

#ttg-31-rail[data-armed] .ttg31-done {
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  #ttg-31-rail:not([data-dragging]) #ttg-31-handle {
    transition: transform 80ms linear;
  }
}
```

## JavaScript
```js
(() => {
  const COMMIT = 0.92;
  const rail = document.querySelector('#ttg-31-rail');
  const handle = document.querySelector('#ttg-31-handle');
  const live = document.querySelector('#ttg-31-live');
  if (!rail || !handle || !live) return;

  const maxPct = () => ((rail.clientWidth - handle.offsetWidth - 8) / handle.offsetWidth) * 100;
  const set = (pct) => handle.style.setProperty('--p', String(pct));

  const commit = (on) => {
    handle.setAttribute('aria-checked', String(on));
    rail.toggleAttribute('data-armed', on);
    set(on ? maxPct() : 0);
    live.textContent = on ? 'Confirmed \u2014 release to run' : 'Locked';
  };

  let dragging = false, startX = 0;
  handle.addEventListener('pointerdown', (e) => {
    if (handle.getAttribute('aria-checked') === 'true') { commit(false); return; }
    dragging = true; startX = e.clientX;
    handle.setPointerCapture(e.pointerId);
    rail.setAttribute('data-dragging', '');
  });
  handle.addEventListener('pointermove', (e) => {
    if (!dragging) return;
    const travel = rail.clientWidth - handle.offsetWidth - 8;
    const px = Math.min(Math.max(0, e.clientX - startX), travel);
    set((px / handle.offsetWidth) * 100);
  });
  const end = () => {
    if (!dragging) return;
    dragging = false;
    rail.removeAttribute('data-dragging');
    const travel = rail.clientWidth - handle.offsetWidth - 8;
    const px = (parseFloat(handle.style.getPropertyValue('--p')) || 0) / 100 * handle.offsetWidth;
    commit(px >= travel * COMMIT);
  };
  ['pointerup', 'pointercancel'].forEach((t) => handle.addEventListener(t, end));

  handle.addEventListener('keydown', (e) => {
    if (['ArrowRight', 'ArrowUp', 'End'].includes(e.key)) { e.preventDefault(); commit(true); }
    if (['ArrowLeft', 'ArrowDown', 'Home'].includes(e.key)) { e.preventDefault(); commit(false); }
    if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); commit(handle.getAttribute('aria-checked') !== 'true'); }
  });
  window.addEventListener('resize', () => { if (handle.getAttribute('aria-checked') === 'true') set(maxPct()); });
})();
```
