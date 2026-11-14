---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-loading-spinner-button-state-transition/"
title: "CSS Loading Spinner Button (State Transition)"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Idle → pending → success in one button that never changes width, because all three labels are stacked in the same grid cell."
has_js: "true"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Loading Spinner Button (State Transition)
Source: https://codefronts.com/components/css-buttons/css-loading-spinner-button-state-transition/

Idle → pending → success in one button that never changes width, because all three labels are stacked in the same grid cell. The spinner is a conic gradient masked into a ring, the success tick draws itself with stroke-dashoffset, and the state lives in a single data-state attribute mirrored to aria-busy and a live region.
## HTML
```html
<div class="cb-06">
  <div class="cb-06__stage">
    <button class="cb-06__btn" type="button" data-state="idle" aria-describedby="cb-06-live">
      <span class="cb-06__slot cb-06__slot--idle">
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5 10 17.5 19 6.5"/></svg>
        <span>Save changes</span>
      </span>
      <span class="cb-06__slot cb-06__slot--busy">
        <span class="cb-06__spin" aria-hidden="true"></span>
        <span>Saving</span>
      </span>
      <span class="cb-06__slot cb-06__slot--done">
        <svg class="cb-06__tick" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5 10 17.5 19 6.5"/></svg>
        <span>Saved</span>
      </span>
    </button>
    <span class="cb-06__live" id="cb-06-live" role="status" aria-live="polite"></span>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap');

.cb-06 {
  --bg: #eef1f5;
  --accent: #1d4ed8;
  --ink: #ffffff;
  --ok: #059669;
  --radius: .8rem;
  --sans: "Outfit",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-06 {
    --bg: oklch(95.5% .008 250);
    --accent: oklch(48% .22 265);
    --ok: oklch(56% .13 162);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-06:not([data-theme="light"]) {
    --bg: #0a0d12;
    --accent: #3b74f2;
    --ok: #10b981;
  }
}

.cb-06[data-theme="dark"] {
  --bg: #0a0d12;
  --accent: #3b74f2;
  --ok: #10b981;
}

.cb-06,
.cb-06 *,
.cb-06 *::before,
.cb-06 *::after {
  box-sizing: border-box;
}

.cb-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-06__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cb-06__btn {
  position: relative;
  cursor: pointer;
  display: grid;
  align-items: center;
  min-height: 3.25rem;
  padding: 0 1.75rem;
  border: 0;
  border-radius: var(--radius);
  font: inherit;
  font-size: 1rem;
  font-weight: 600;
  color: var(--ink);
  background: var(--accent);
  box-shadow: 0 10px 24px -12px color-mix(in oklab,var(--accent) 90%,transparent);
  transition: background-color .3s ease, translate .2s cubic-bezier(.16,1,.3,1), box-shadow .3s ease;
}

.cb-06__slot {
  grid-area: 1/1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .55rem;
  opacity: 0;
  scale: .92;
  transition: opacity .22s ease, scale .28s cubic-bezier(.16,1,.3,1);
}

.cb-06__slot svg {
  width: 1.1rem;
  height: 1.1rem;
}

.cb-06__btn[data-state="idle"] .cb-06__slot--idle,
.cb-06__btn[data-state="busy"] .cb-06__slot--busy,
.cb-06__btn[data-state="done"] .cb-06__slot--done {
  opacity: 1;
  scale: 1;
}

.cb-06__btn[data-state="done"] {
  background: var(--ok);
  box-shadow: 0 10px 24px -12px color-mix(in oklab,var(--ok) 90%,transparent);
}

.cb-06__btn[data-state="busy"] {
  cursor: progress;
}

.cb-06__spin {
  width: 1.1rem;
  height: 1.1rem;
  border-radius: 50%;
  flex: none;
  background: conic-gradient(from 0deg,transparent 0 22%,currentColor);
  -webkit-mask: radial-gradient(farthest-side,transparent calc(100% - 2.5px),#000 calc(100% - 2.5px));
  mask: radial-gradient(farthest-side,transparent calc(100% - 2.5px),#000 calc(100% - 2.5px));
  animation: cb-06-spin .7s linear infinite;
}

@keyframes cb-06-spin {
  to {
    rotate: 1turn;
  }
}

.cb-06__tick path {
  stroke-dasharray: 26;
  stroke-dashoffset: 26;
}

.cb-06__btn[data-state="done"] .cb-06__tick path {
  animation: cb-06-draw .45s cubic-bezier(.16,1,.3,1) forwards;
}

@keyframes cb-06-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.cb-06__btn:hover[data-state="idle"] {
  translate: 0 -2px;
  background: color-mix(in oklab,var(--accent) 88%,black);
}

.cb-06__btn:active[data-state="idle"] {
  translate: 0 1px;
}

.cb-06__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cb-06__btn:disabled {
  opacity: .9;
}

@media (prefers-reduced-motion: reduce) {
  .cb-06__btn,
    .cb-06__slot {
    transition: none;
  }

  .cb-06__spin {
    animation: cb-06-pulse 1s ease-in-out infinite;
    background: currentColor;
    mask: none;
    -webkit-mask: none;
  }

  @keyframes cb-06-pulse {
    50% {
      opacity: .25;
    }
  }

  .cb-06__tick path {
    stroke-dashoffset: 0;
    animation: none;
  }
}

@media (forced-colors: active) {
  .cb-06__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.cb-06__btn');
  const live = document.getElementById('cb-06-live');
  if (!btn) return;
  const set = (state, msg) => {
    btn.dataset.state = state;
    btn.disabled = state === 'busy';
    btn.setAttribute('aria-busy', String(state === 'busy'));
    if (msg) live.textContent = msg;
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
