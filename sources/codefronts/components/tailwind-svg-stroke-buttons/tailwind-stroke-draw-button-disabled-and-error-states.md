---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-stroke-draw-button-disabled-and-error-states/"
title: "Tailwind Stroke Draw Button Disabled and Error States"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "Three states that must be distinguishable both visually and semantically: a genuinely disabled stepper at the floor, an aria-disabled sign-off a keyboard…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stroke Draw Button Disabled and Error States
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-stroke-draw-button-disabled-and-error-states/

Three states that must be distinguishable both visually and semantically: a genuinely disabled stepper at the floor, an aria-disabled sign-off a keyboard user can still reach and learn from, and an error frame that appears instantly at full weight. The root carries group/state and each button its own named group, so one class list can react to both: group-data-[state=error]/state: for the screen, group-hover/btn: for the control.
## HTML
```html
<section class="svgb-16 group/state relative block w-full min-h-svh bg-svgb16-bg text-svgb16-fg font-svgb16-sans" data-state="idle">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-16-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded border border-current/22 bg-current/6 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/13 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-16-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="min-h-svh grid place-items-center p-[clamp(20px,5vw,64px)]">
    <div class="w-full max-w-125 flex flex-col gap-3 p-[clamp(22px,4vw,36px)] rounded bg-svgb16-card border border-svgb16-rest border-t-4 border-t-svgb16-stroke">
      <div class="grid grid-cols-[auto_1fr_auto_1fr] gap-x-3 gap-y-1 pb-3.5 border-b border-svgb16-rest font-svgb16-mono text-[10.5px] tracking-[0.08em] uppercase">
        <span class="text-svgb16-muted">Patient</span>
        <span>R. Okonjo &middot; 42y</span>
        <span class="text-svgb16-muted">Ward</span>
        <span>C4 &middot; bed 11</span>
      </div>

      <h1 class="mt-1.5 mb-1 text-[clamp(24px,4vw,34px)] font-semibold tracking-[-0.02em] [&_span]:text-svgb16-muted [&_span]:font-normal">Amoxicillin <span>500 mg</span></h1>

      <div class="flex flex-col gap-2.5 py-2">
        <span class="text-[13px] font-medium">Doses per day</span>
        <div class="flex items-center gap-3.5">
          <button class="group/step relative size-13 grid place-items-center border-0 p-0 rounded-[10px] bg-svgb16-stroke/8 cursor-pointer disabled:cursor-not-allowed disabled:bg-svgb16-fg/4 disabled:text-svgb16-muted focus-visible:outline-2 focus-visible:outline-svgb16-stroke focus-visible:outline-offset-[3px]" type="button" disabled aria-label="Decrease doses">
            <svg class="absolute inset-0 w-full h-full overflow-visible [&_rect]:fill-none [&_rect]:[stroke-linecap:round]" viewBox="0 0 52 52" aria-hidden="true">
              <rect class="stroke-svgb16-rest [stroke-width:1.5] [stroke-dasharray:0.02_0.02]" x="1.5" y="1.5" width="49" height="49" rx="10" pathLength="1"/>
            </svg>
            <span class="relative z-[1] text-[22px] leading-none">&minus;</span>
          </button>
          <span class="min-w-[2ch] text-center text-[22px] font-semibold tabular-nums">1</span>
          <button class="group/step relative size-13 grid place-items-center border-0 p-0 rounded-[10px] bg-svgb16-stroke/8 cursor-pointer disabled:cursor-not-allowed disabled:bg-svgb16-fg/4 disabled:text-svgb16-muted focus-visible:outline-2 focus-visible:outline-svgb16-stroke focus-visible:outline-offset-[3px]" type="button" aria-label="Increase doses">
            <svg class="absolute inset-0 w-full h-full overflow-visible [&_rect]:fill-none [&_rect]:[stroke-linecap:round]" viewBox="0 0 52 52" aria-hidden="true">
              <rect class="stroke-svgb16-rest [stroke-width:1.5]" x="1.5" y="1.5" width="49" height="49" rx="10" pathLength="1"/>
              <rect class="stroke-svgb16-stroke [stroke-width:2.2] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[480ms] ease-[cubic-bezier(0.22,1,0.36,1)] motion-reduce:transition-none group-hover/step:[stroke-dashoffset:0] group-focus-visible/step:[stroke-dashoffset:0]" x="1.5" y="1.5" width="49" height="49" rx="10" pathLength="1"/>
            </svg>
            <span class="relative z-[1] text-[22px] leading-none">+</span>
          </button>
        </div>
        <span class="font-svgb16-mono text-[11px] text-svgb16-muted [&_code]:text-[11px]">minimum reached &rarr; truly <code>disabled</code></span>
      </div>

      <label class="mt-1.5 text-[13px] font-medium" for="svgb-16-field">Prescriber ID</label>
      <input class="svgb-16__field h-13 px-3.5 rounded border-[1.5px] border-svgb16-rest bg-svgb16-fg/2 font-svgb16-mono text-[15px] text-inherit transition-[border-color,box-shadow] duration-200 motion-reduce:transition-none focus-visible:outline-none focus-visible:border-svgb16-stroke focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-svgb16-stroke)_22%,transparent)] aria-invalid:border-svgb16-err" id="svgb-16-field" type="text" placeholder="GMC 7 digits" autocomplete="off" inputmode="numeric" aria-describedby="svgb-16-msg">
      <p class="mt-0 mb-1.5 flex gap-2 items-start text-[13px] leading-[1.45] text-svgb16-muted" id="svgb-16-msg">
        <span class="hidden flex-none text-svgb16-err group-data-[state=error]/state:block [&_svg]:size-4 [&_svg]:block" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 8v5"/><circle cx="12" cy="16.4" r="0.9" fill="currentColor" stroke="none"/><path d="M12 3.5 21 19H3Z"/></svg>
        </span>
        <span class="svgb-16__mtext group-data-[state=error]/state:text-svgb16-err group-data-[state=error]/state:font-medium">Sign-off is blocked until a prescriber ID is entered.</span>
      </p>

      <button class="svgb-16__sign group/sign relative w-full h-[62px] grid place-items-center border-0 p-0 rounded-lg bg-svgb16-stroke/10 text-[15.5px] font-semibold cursor-pointer aria-disabled:cursor-not-allowed aria-disabled:bg-svgb16-stroke/4 focus-visible:outline-2 focus-visible:outline-svgb16-stroke focus-visible:outline-offset-[3px] group-data-[state=error]/state:bg-svgb16-err/8 group-data-[state=error]/state:animate-svgb16-nudge motion-reduce:group-data-[state=error]/state:animate-none group-data-[state=sent]/state:bg-svgb16-stroke/16" type="button" aria-disabled="true">
        <svg class="absolute inset-0 w-full h-full overflow-visible [&_rect]:fill-none [&_rect]:[stroke-linecap:round]" viewBox="0 0 380 62" aria-hidden="true">
          <rect class="stroke-svgb16-rest [stroke-width:1.5]" x="2" y="2" width="376" height="58" rx="8" pathLength="1"/>
          <rect class="stroke-svgb16-stroke [stroke-width:2.2] [stroke-dasharray:1] [stroke-dashoffset:1] [transition:stroke-dashoffset_560ms_cubic-bezier(0.22,1,0.36,1),stroke_200ms_ease] motion-reduce:transition-none group-hover/sign:[stroke-dashoffset:0] group-focus-visible/sign:[stroke-dashoffset:0] group-aria-disabled/sign:[stroke-dasharray:0.02_0.014] group-aria-disabled/sign:[stroke-dashoffset:0] group-aria-disabled/sign:stroke-svgb16-stroke/50 group-data-[state=error]/state:!stroke-svgb16-err group-data-[state=error]/state:![stroke-width:2.6] group-data-[state=error]/state:![stroke-dasharray:none] group-data-[state=error]/state:![stroke-dashoffset:0] group-data-[state=error]/state:!transition-none" x="2" y="2" width="376" height="58" rx="8" pathLength="1"/>
        </svg>
        <span class="relative z-[1]">Sign and send to pharmacy</span>
      </button>

      <p class="mt-0.5 mb-0 flex flex-wrap items-center gap-x-3 gap-y-2 text-xs text-svgb16-muted">
        <span class="font-svgb16-mono text-[10.5px] px-[7px] py-[3px] rounded-[3px] bg-svgb16-stroke/12 text-[color-mix(in_oklab,var(--color-svgb16-stroke)_80%,var(--color-svgb16-fg))]">aria-disabled</span> reachable, explains itself
        <span class="font-svgb16-mono text-[10.5px] px-[7px] py-[3px] rounded-[3px] bg-svgb16-fg/8 text-svgb16-muted">disabled</span> inert by design
      </p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb16-bg: #eef0f1;
  --color-svgb16-bg: oklch(0.945 0.004 220);
  --color-svgb16-fg: #101316;
  --color-svgb16-fg: oklch(0.185 0.006 230);
  --color-svgb16-muted: #5a6169;
  --color-svgb16-muted: oklch(0.50 0.011 230);
  --color-svgb16-card: #ffffff;
  --color-svgb16-card: oklch(1 0 0);
  --color-svgb16-rest: rgba(16, 19, 22, 0.16);
  --color-svgb16-rest: oklch(0.185 0.006 230 / 0.16);
  --color-svgb16-stroke: #0c6b8f;
  --color-svgb16-stroke: oklch(0.48 0.11 225);
  --color-svgb16-err: #b81f1f;
  --color-svgb16-err: oklch(0.50 0.20 27);
  --font-svgb16-sans: 'IBM Plex Sans', system-ui, sans-serif;
  --font-svgb16-mono: 'IBM Plex Mono', ui-monospace, monospace;
  /* a translate-only nudge: no layout, one cycle, decoration and nothing more */
  --animate-svgb16-nudge: svgb16-nudge 420ms cubic-bezier(0.36, 0.07, 0.19, 0.97) 1;
}

@keyframes svgb16-nudge {
  0%,
    100% {
    translate: 0 0;
  }

  20% {
    translate: -4px 0;
  }

  45% {
    translate: 4px 0;
  }

  70% {
    translate: -2px 0;
  }
}

.svgb-16:has(#svgb-16-theme:checked) {
  --color-svgb16-bg: #0d1013;
  --color-svgb16-bg: oklch(0.175 0.006 230);
  --color-svgb16-fg: #eceff1;
  --color-svgb16-fg: oklch(0.95 0.004 230);
  --color-svgb16-muted: #8b929a;
  --color-svgb16-muted: oklch(0.67 0.011 230);
  --color-svgb16-card: #14181c;
  --color-svgb16-card: oklch(0.215 0.008 230);
  --color-svgb16-rest: rgba(236, 239, 241, 0.18);
  --color-svgb16-rest: oklch(0.95 0.004 230 / 0.18);
  --color-svgb16-stroke: #6fc6e8;
  --color-svgb16-stroke: oklch(0.80 0.10 225);
  --color-svgb16-err: #ff8f80;
  --color-svgb16-err: oklch(0.78 0.15 30);
}
/* Forced-colors mode: the drawn strokes cannot be remapped, so they are
   surrendered and real borders take over. System keywords, not tokens. */

@media (forced-colors: active) {
  .svgb-16 svg rect {
    stroke: transparent;
  }

  .svgb-16 button {
    border: 1px solid ButtonBorder;
  }

  .svgb-16[data-state='error'] .svgb-16__mtext {
    color: LinkText;
  }
}
```

## JavaScript
```js
/* aria-disabled keeps the sign-off reachable; the handler declines and explains. */
(function () {
  var root = document.querySelector('.svgb-16');
  if (!root) return;
  var btn = root.querySelector('.svgb-16__sign');
  var field = root.querySelector('.svgb-16__field');
  var text = root.querySelector('.svgb-16__mtext');

  function sync() {
    var ok = field.value.trim().length >= 4;
    btn.setAttribute('aria-disabled', ok ? 'false' : 'true');
    if (ok && root.dataset.state === 'error') {
      root.dataset.state = 'idle';
      field.setAttribute('aria-invalid', 'false');
      text.textContent = 'Prescriber ID accepted. Ready to sign.';
    }
  }

  btn.addEventListener('click', function () {
    if (btn.getAttribute('aria-disabled') === 'true') {
      root.dataset.state = 'error';
      field.setAttribute('aria-invalid', 'true');
      text.textContent = 'Enter your prescriber ID before signing.';
      field.focus();
      return;
    }
    root.dataset.state = 'sent';
    text.textContent = 'Sent to pharmacy queue.';
  });

  field.addEventListener('input', sync);
  sync();
  root.__svgb16Cleanup = function () { field.removeEventListener('input', sync); };
})();
```
