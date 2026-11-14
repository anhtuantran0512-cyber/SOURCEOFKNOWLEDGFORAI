---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-loading-spinner-button-state-transition/"
title: "Tailwind Loading Spinner Button (State Transition)"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Idle → pending → success in a button that never changes width, because all three labels share one grid cell."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Loading Spinner Button (State Transition)
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-loading-spinner-button-state-transition/

Idle → pending → success in a button that never changes width, because all three labels share one grid cell. The port's headline is group-data-[state=busy]:: the CSS version needed three descendant selectors keyed off [data-state], and Tailwind states each slot's own visibility condition on the slot itself.
## HTML
```html
<div class="tb-06 w-full min-h-svh grid place-items-center bg-tb06-bg font-tb06-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" data-state="idle" aria-describedby="tb-06-live" class="group relative cursor-pointer grid items-center min-h-13 px-7 border-0 rounded-[0.8rem] text-base font-semibold text-white bg-tb06-accent shadow-[0_10px_24px_-12px_var(--color-tb06-accent-glow)] transition-[background-color,translate,box-shadow] duration-300 ease-tb06-out data-[state=done]:bg-tb06-ok data-[state=done]:shadow-[0_10px_24px_-12px_var(--color-tb06-ok-glow)] data-[state=busy]:cursor-progress hover:data-[state=idle]:-translate-y-0.5 hover:data-[state=idle]:bg-tb06-accent-deep active:data-[state=idle]:translate-y-px focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tb06-accent disabled:opacity-90 motion-reduce:transition-none">
    <span class="col-start-1 row-start-1 flex items-center justify-center gap-2 opacity-0 scale-90 transition-[opacity,scale] duration-[220ms] ease-tb06-out group-data-[state=idle]:opacity-100 group-data-[state=idle]:scale-100 motion-reduce:transition-none">
      <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" class="size-[1.1rem]"><path d="M5 12.5 10 17.5 19 6.5"/></svg>
      <span>Save changes</span>
    </span>
    <span class="col-start-1 row-start-1 flex items-center justify-center gap-2 opacity-0 scale-90 transition-[opacity,scale] duration-[220ms] ease-tb06-out group-data-[state=busy]:opacity-100 group-data-[state=busy]:scale-100 motion-reduce:transition-none">
      <span aria-hidden="true" class="size-[1.1rem] shrink-0 rounded-full bg-[conic-gradient(from_0deg,transparent_0_22%,currentColor)] [mask-image:radial-gradient(farthest-side,transparent_calc(100%-2.5px),#000_calc(100%-2.5px))] animate-tb06-spin motion-reduce:animate-tb06-pulse motion-reduce:bg-current motion-reduce:[mask-image:none]"></span>
      <span>Saving</span>
    </span>
    <span class="col-start-1 row-start-1 flex items-center justify-center gap-2 opacity-0 scale-90 transition-[opacity,scale] duration-[220ms] ease-tb06-out group-data-[state=done]:opacity-100 group-data-[state=done]:scale-100 motion-reduce:transition-none">
      <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" class="tb-06__tick size-[1.1rem]"><path d="M5 12.5 10 17.5 19 6.5"/></svg>
      <span>Saved</span>
    </span>
  </button>
  <span id="tb-06-live" role="status" aria-live="polite" class="sr-only"></span>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb06-bg: #eef1f5;
  --color-tb06-bg: oklch(0.955 0.008 250);
  --color-tb06-accent: #1d4ed8;
  --color-tb06-accent: oklch(0.48 0.22 265);
  --color-tb06-accent-deep: #1740b4;
  --color-tb06-accent-deep: oklch(0.42 0.2 265);
  --color-tb06-accent-glow: #1d4ed8e6;
  --color-tb06-accent-glow: oklch(0.48 0.22 265 / 0.9);
  --color-tb06-ok: #059669;
  --color-tb06-ok: oklch(0.56 0.13 162);
  --color-tb06-ok-glow: #059669e6;
  --color-tb06-ok-glow: oklch(0.56 0.13 162 / 0.9);
  --font-tb06-sans: "Outfit", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb06-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb06-spin: tb-06-spin 0.7s linear infinite;
  --animate-tb06-pulse: tb-06-pulse 1s ease-in-out infinite;
}

@keyframes tb-06-spin {
  to {
    rotate: 1turn;
  }
}

@keyframes tb-06-pulse {
  50% {
    opacity: 0.25;
  }
}

@keyframes tb-06-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.tb-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
/* Safari ≤15.3 mask shim — the utility emits the unprefixed property only. */

.tb-06 [class*="mask-image"] {
  -webkit-mask-image: radial-gradient(farthest-side, transparent calc(100% - 2.5px), #000 calc(100% - 2.5px));
}
/* SVG path geometry: dasharray/dashoffset have no utility form. */

.tb-06__tick path {
  stroke-dasharray: 26;
  stroke-dashoffset: 26;
}

.tb-06 button[data-state="done"] .tb-06__tick path {
  animation: tb-06-draw 0.45s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@media (prefers-reduced-motion: reduce) {
  .tb-06__tick path {
    stroke-dashoffset: 0;
    animation: none;
  }
}

@media (prefers-color-scheme: dark) {
  .tb-06:not([data-theme="light"]) {
    --color-tb06-bg: oklch(0.14 0.012 255);
    --color-tb06-accent: oklch(0.6 0.19 265);
    --color-tb06-ok: oklch(0.68 0.15 162);
  }
}

.tb-06[data-theme="dark"] {
  --color-tb06-bg: oklch(0.14 0.012 255);
  --color-tb06-accent: oklch(0.6 0.19 265);
  --color-tb06-ok: oklch(0.68 0.15 162);
}

@media (forced-colors: active) {
  .tb-06 button {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.tb-06 button');
  const live = document.getElementById('tb-06-live');
  if (!btn) return;
  const set = (state, msg) => {
    btn.dataset.state = state;
    btn.disabled = state === 'busy';
    btn.setAttribute('aria-busy', String(state === 'busy'));
    if (msg !== undefined) live.textContent = msg;
  };
  btn.addEventListener('click', () => {
    if (btn.dataset.state !== 'idle') return;
    set('busy', 'Saving changes');
    // Replace both timeouts with your real await fetch(...) resolution.
    setTimeout(() => set('done', 'Changes saved'), 1500);
    setTimeout(() => set('idle', ''), 3200);
  });
})();
```
