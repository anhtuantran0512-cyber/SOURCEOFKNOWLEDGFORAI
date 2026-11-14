---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/hold-to-confirm/"
title: "Hold to Confirm Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "Destructive-action friction: a conic progress ring fills while you press and hold, completing after 900ms; release early and it drains back."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hold to Confirm Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/hold-to-confirm/

Destructive-action friction: a conic progress ring fills while you press and hold, completing after 900ms; release early and it drains back. The fill is a typed @property percentage transitioned via data-holding:[--tcb24-p:100%]. The port fixes a silent bug in the original — the property was registered inherits:false, so the ring pseudo-element never saw the value — and announces completion to screen readers.
## HTML
```html
<section class="tcb-24 w-full min-h-svh grid place-items-center bg-[linear-gradient(180deg,var(--color-tcb24-bg),var(--color-tcb24-bg2))] px-6 py-12 font-tcb24-sans" aria-label="Hold to confirm close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="flex flex-col items-center gap-5">
      <button id="tcb-24-btn" type="button" aria-label="Hold to close" aria-describedby="tcb-24-hint" class="relative grid size-19 cursor-pointer touch-none place-items-center rounded-full bg-tcb24-btn shadow-[0_18px_40px_-20px_rgb(0_0_0/0.9)] transition-[--tcb24-p,scale,background-color] duration-300 ease-out select-none [--tcb24-p:0%] before:absolute before:-inset-1.5 before:rounded-full before:bg-[conic-gradient(var(--color-tcb24-acc)_var(--tcb24-p),var(--color-tcb24-track)_0)] before:[mask:radial-gradient(circle,transparent_66%,#000_67%)] focus-visible:outline-3 focus-visible:outline-offset-5 focus-visible:outline-tcb24-acc data-holding:scale-96 data-holding:duration-900 data-holding:ease-linear data-holding:[--tcb24-p:100%] data-done:bg-tcb24-acc data-done:[--tcb24-p:100%] motion-reduce:transition-none">
        <span aria-hidden="true" class="relative size-6 before:absolute before:top-1/2 before:left-1/2 before:h-[3px] before:w-6 before:-translate-1/2 before:rotate-45 before:rounded-[2px] before:bg-tcb24-x after:absolute after:top-1/2 after:left-1/2 after:h-[3px] after:w-6 after:-translate-1/2 after:-rotate-45 after:rounded-[2px] after:bg-tcb24-x"></span>
      </button>
      <span id="tcb-24-hint" role="status" class="text-[13px] font-medium tracking-[0.03em] text-tcb24-mut">Press &amp; hold to close</span>
    </div>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tcb24-mono text-[11.5px] text-tcb24-mut ring-1 ring-white/12">@property --tcb24-p · data-holding:[--tcb24-p:100%] · conic ring</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* The one rule utilities cannot express: a typed, inheritable custom property the ring's ::before can read and the browser can interpolate. */

@property --tcb24-p {
  syntax: "<percentage>";
  inherits: true;
  initial-value: 0%;
}

@theme {
  --color-tcb24-bg: #2a1c1b;
  --color-tcb24-bg: oklch(0.2 0.02 25);
  --color-tcb24-bg2: #1a1211;
  --color-tcb24-bg2: oklch(0.14 0.015 20);
  --color-tcb24-btn: #3a2826;
  --color-tcb24-btn: oklch(0.25 0.03 25);
  --color-tcb24-acc: #ef4f43;
  --color-tcb24-acc: oklch(0.64 0.2 27);
  --color-tcb24-track: #54403e80;
  --color-tcb24-track: oklch(0.35 0.03 25 / 0.5);
  --color-tcb24-x: #fbeeec;
  --color-tcb24-x: oklch(0.95 0.02 25);
  --color-tcb24-mut: #c6aaa6;
  --color-tcb24-mut: oklch(0.77 0.04 25);
  --font-tcb24-sans: 'Geist', system-ui, sans-serif;
  --font-tcb24-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-24 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const btn = document.getElementById('tcb-24-btn');
  if (!btn || btn.dataset.wired) return;
  btn.dataset.wired = '1';
  const hint = document.getElementById('tcb-24-hint');
  const HOLD = 900;
  let timer = 0;
  const done = () => btn.hasAttribute('data-done');
  const start = () => {
    if (done()) return;
    btn.setAttribute('data-holding', '');
    hint.textContent = 'Keep holding\u2026';
    timer = setTimeout(complete, HOLD);
  };
  const cancel = () => {
    if (!btn.hasAttribute('data-holding')) return;
    clearTimeout(timer);
    btn.removeAttribute('data-holding');
    hint.textContent = 'Press & hold to close';
  };
  const complete = () => {
    btn.removeAttribute('data-holding');
    btn.setAttribute('data-done', '');
    btn.setAttribute('aria-label', 'Closed. Press to reset');
    hint.textContent = 'Closed \u2014 click to reset';
    navigator.vibrate?.(10);
  };
  btn.addEventListener('pointerdown', start);
  ['pointerup', 'pointerleave', 'pointercancel'].forEach((ev) => btn.addEventListener(ev, cancel));
  btn.addEventListener('keydown', (e) => { if ((e.key === 'Enter' || e.key === ' ') && !e.repeat) { e.preventDefault(); start(); } });
  btn.addEventListener('keyup', (e) => { if (e.key === 'Enter' || e.key === ' ') cancel(); });
  btn.addEventListener('click', () => {
    if (!done()) return;
    btn.removeAttribute('data-done');
    btn.setAttribute('aria-label', 'Hold to close');
    hint.textContent = 'Press & hold to close';
  });
})();
```
