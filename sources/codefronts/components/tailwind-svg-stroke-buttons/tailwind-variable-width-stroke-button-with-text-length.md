---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-variable-width-stroke-button-with-text-length/"
title: "Tailwind Variable Width Stroke Button with Text Length"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "Six labels from three characters to thirty-five, each deriving its stroke weight, dash rhythm and draw duration from one inline number."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Variable Width Stroke Button with Text Length
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-variable-width-stroke-button-with-text-length/

Six labels from three characters to thirty-five, each deriving its stroke weight, dash rhythm and draw duration from one inline number. Hover transitions the dash pattern rather than the offset &mdash; hover:[--svgb-20-duty:1] closes every gap until the measure becomes a solid border, a state change no dash-offset draw can express. Both @property blocks stay in CSS, and they are the load-bearing part.
## HTML
```html
<section class="svgb-20 relative block w-full min-h-svh bg-svgb20-bg text-svgb20-fg font-svgb20-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-20-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded-sm border border-current/22 bg-current/7 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/14 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-20-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="min-h-svh grid place-items-center p-[clamp(22px,5vw,68px)]">
    <div class="w-full max-w-225 flex flex-col gap-[clamp(20px,3vw,32px)]">
      <div class="flex flex-wrap items-end justify-between gap-3.5 pb-4 border-b border-svgb20-rest">
        <h1 class="m-0 text-[clamp(38px,7vw,82px)] font-bold [font-stretch:118%] leading-[0.88] tracking-[-0.045em] uppercase">Weight<br>Ladder</h1>
        <p class="m-0 font-svgb20-mono text-[11px] tracking-[0.02em] text-svgb20-muted">stroke-width: clamp(1.5px, 1.1px + chars &times; 0.055px, 3px)</p>
      </div>

      <ol class="list-none m-0 p-0 flex flex-col gap-[clamp(12px,2vw,18px)]">
        <li class="grid grid-cols-[34px_1fr_54px] gap-[clamp(12px,2.5vw,22px)] items-center">
          <span class="font-svgb20-mono text-[11px] tabular-nums text-svgb20-muted">03</span>
          <button class="group relative inline-grid place-items-center justify-self-start min-w-24 min-h-[62px] px-[clamp(20px,2.6vw,32px)] border-0 rounded bg-transparent font-normal tracking-[-0.01em] text-[clamp(15px,calc(14px+var(--svgb-20-chars)*0.04px),18px)] cursor-pointer [transition:--svgb-20-duty_calc(340ms+var(--svgb-20-chars)*14ms)_cubic-bezier(0.22,1,0.36,1)] hover:[--svgb-20-duty:1] focus-visible:[--svgb-20-duty:1] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-svgb20-stroke focus-visible:outline-offset-[3px]" type="button" data-chars="3" style="--svgb-20-chars: 3">
            <svg class="absolute inset-0 w-full h-full overflow-visible" aria-hidden="true"><rect class="svgb-20__ink fill-none [x:1.5px] [y:1.5px] [width:calc(100%-3px)] [height:calc(100%-3px)] [rx:4px] stroke-svgb20-rest [stroke-linecap:butt] [stroke-dasharray:calc(var(--svgb-20-duty)/var(--svgb-20-chars))_calc((1-var(--svgb-20-duty))/var(--svgb-20-chars))] transition-[stroke] duration-[240ms] group-hover:stroke-svgb20-stroke group-focus-visible:stroke-svgb20-stroke motion-reduce:[stroke-dasharray:none] [stroke-width:clamp(1.5px,calc(1.1px+var(--svgb-20-chars)*0.055px),3px)]" data-chars="3" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="relative z-[1] whitespace-nowrap transition-colors duration-[260ms] motion-reduce:transition-none group-hover:text-svgb20-stroke group-focus-visible:text-svgb20-stroke">Buy</span>
          </button>
          <span class="font-svgb20-mono text-[11px] tabular-nums text-svgb20-muted text-end">1.5px</span>
        </li>
        <li class="grid grid-cols-[34px_1fr_54px] gap-[clamp(12px,2.5vw,22px)] items-center">
          <span class="font-svgb20-mono text-[11px] tabular-nums text-svgb20-muted">08</span>
          <button class="group relative inline-grid place-items-center justify-self-start min-w-24 min-h-[62px] px-[clamp(20px,2.6vw,32px)] border-0 rounded bg-transparent font-normal tracking-[-0.01em] text-[clamp(15px,calc(14px+var(--svgb-20-chars)*0.04px),18px)] cursor-pointer [transition:--svgb-20-duty_calc(340ms+var(--svgb-20-chars)*14ms)_cubic-bezier(0.22,1,0.36,1)] hover:[--svgb-20-duty:1] focus-visible:[--svgb-20-duty:1] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-svgb20-stroke focus-visible:outline-offset-[3px]" type="button" data-chars="8" style="--svgb-20-chars: 8">
            <svg class="absolute inset-0 w-full h-full overflow-visible" aria-hidden="true"><rect class="svgb-20__ink fill-none [x:1.5px] [y:1.5px] [width:calc(100%-3px)] [height:calc(100%-3px)] [rx:4px] stroke-svgb20-rest [stroke-linecap:butt] [stroke-dasharray:calc(var(--svgb-20-duty)/var(--svgb-20-chars))_calc((1-var(--svgb-20-duty))/var(--svgb-20-chars))] transition-[stroke] duration-[240ms] group-hover:stroke-svgb20-stroke group-focus-visible:stroke-svgb20-stroke motion-reduce:[stroke-dasharray:none] [stroke-width:clamp(1.5px,calc(1.1px+var(--svgb-20-chars)*0.055px),3px)]" data-chars="8" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="relative z-[1] whitespace-nowrap transition-colors duration-[260ms] motion-reduce:transition-none group-hover:text-svgb20-stroke group-focus-visible:text-svgb20-stroke">Add note</span>
          </button>
          <span class="font-svgb20-mono text-[11px] tabular-nums text-svgb20-muted text-end">1.5px</span>
        </li>
        <li class="grid grid-cols-[34px_1fr_54px] gap-[clamp(12px,2.5vw,22px)] items-center">
          <span class="font-svgb20-mono text-[11px] tabular-nums text-svgb20-muted">13</span>
          <button class="group relative inline-grid place-items-center justify-self-start min-w-24 min-h-[62px] px-[clamp(20px,2.6vw,32px)] border-0 rounded bg-transparent font-normal tracking-[-0.01em] text-[clamp(15px,calc(14px+var(--svgb-20-chars)*0.04px),18px)] cursor-pointer [transition:--svgb-20-duty_calc(340ms+var(--svgb-20-chars)*14ms)_cubic-bezier(0.22,1,0.36,1)] hover:[--svgb-20-duty:1] focus-visible:[--svgb-20-duty:1] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-svgb20-stroke focus-visible:outline-offset-[3px]" type="button" data-chars="13" style="--svgb-20-chars: 13">
            <svg class="absolute inset-0 w-full h-full overflow-visible" aria-hidden="true"><rect class="svgb-20__ink fill-none [x:1.5px] [y:1.5px] [width:calc(100%-3px)] [height:calc(100%-3px)] [rx:4px] stroke-svgb20-rest [stroke-linecap:butt] [stroke-dasharray:calc(var(--svgb-20-duty)/var(--svgb-20-chars))_calc((1-var(--svgb-20-duty))/var(--svgb-20-chars))] transition-[stroke] duration-[240ms] group-hover:stroke-svgb20-stroke group-focus-visible:stroke-svgb20-stroke motion-reduce:[stroke-dasharray:none] [stroke-width:clamp(1.5px,calc(1.1px+var(--svgb-20-chars)*0.055px),3px)]" data-chars="13" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="relative z-[1] whitespace-nowrap transition-colors duration-[260ms] motion-reduce:transition-none group-hover:text-svgb20-stroke group-focus-visible:text-svgb20-stroke">Export as CSV</span>
          </button>
          <span class="font-svgb20-mono text-[11px] tabular-nums text-svgb20-muted text-end">1.8px</span>
        </li>
        <li class="grid grid-cols-[34px_1fr_54px] gap-[clamp(12px,2.5vw,22px)] items-center">
          <span class="font-svgb20-mono text-[11px] tabular-nums text-svgb20-muted">22</span>
          <button class="group relative inline-grid place-items-center justify-self-start min-w-24 min-h-[62px] px-[clamp(20px,2.6vw,32px)] border-0 rounded bg-transparent font-normal tracking-[-0.01em] text-[clamp(15px,calc(14px+var(--svgb-20-chars)*0.04px),18px)] cursor-pointer [transition:--svgb-20-duty_calc(340ms+var(--svgb-20-chars)*14ms)_cubic-bezier(0.22,1,0.36,1)] hover:[--svgb-20-duty:1] focus-visible:[--svgb-20-duty:1] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-svgb20-stroke focus-visible:outline-offset-[3px]" type="button" data-chars="22" style="--svgb-20-chars: 22">
            <svg class="absolute inset-0 w-full h-full overflow-visible" aria-hidden="true"><rect class="svgb-20__ink fill-none [x:1.5px] [y:1.5px] [width:calc(100%-3px)] [height:calc(100%-3px)] [rx:4px] stroke-svgb20-rest [stroke-linecap:butt] [stroke-dasharray:calc(var(--svgb-20-duty)/var(--svgb-20-chars))_calc((1-var(--svgb-20-duty))/var(--svgb-20-chars))] transition-[stroke] duration-[240ms] group-hover:stroke-svgb20-stroke group-focus-visible:stroke-svgb20-stroke motion-reduce:[stroke-dasharray:none] [stroke-width:clamp(1.5px,calc(1.1px+var(--svgb-20-chars)*0.055px),3px)]" data-chars="22" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="relative z-[1] whitespace-nowrap transition-colors duration-[260ms] motion-reduce:transition-none group-hover:text-svgb20-stroke group-focus-visible:text-svgb20-stroke">Schedule for next week</span>
          </button>
          <span class="font-svgb20-mono text-[11px] tabular-nums text-svgb20-muted text-end">2.3px</span>
        </li>
        <li class="grid grid-cols-[34px_1fr_54px] gap-[clamp(12px,2.5vw,22px)] items-center">
          <span class="font-svgb20-mono text-[11px] tabular-nums text-svgb20-muted">35</span>
          <button class="group relative inline-grid place-items-center justify-self-start min-w-24 min-h-[62px] px-[clamp(20px,2.6vw,32px)] border-0 rounded bg-transparent font-normal tracking-[-0.01em] text-[clamp(15px,calc(14px+var(--svgb-20-chars)*0.04px),18px)] cursor-pointer [transition:--svgb-20-duty_calc(340ms+var(--svgb-20-chars)*14ms)_cubic-bezier(0.22,1,0.36,1)] hover:[--svgb-20-duty:1] focus-visible:[--svgb-20-duty:1] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-svgb20-stroke focus-visible:outline-offset-[3px]" type="button" data-chars="35" style="--svgb-20-chars: 35">
            <svg class="absolute inset-0 w-full h-full overflow-visible" aria-hidden="true"><rect class="svgb-20__ink fill-none [x:1.5px] [y:1.5px] [width:calc(100%-3px)] [height:calc(100%-3px)] [rx:4px] stroke-svgb20-rest [stroke-linecap:butt] [stroke-dasharray:calc(var(--svgb-20-duty)/var(--svgb-20-chars))_calc((1-var(--svgb-20-duty))/var(--svgb-20-chars))] transition-[stroke] duration-[240ms] group-hover:stroke-svgb20-stroke group-focus-visible:stroke-svgb20-stroke motion-reduce:[stroke-dasharray:none] [stroke-width:clamp(1.5px,calc(1.1px+var(--svgb-20-chars)*0.055px),3px)]" data-chars="35" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="relative z-[1] whitespace-nowrap transition-colors duration-[260ms] motion-reduce:transition-none group-hover:text-svgb20-stroke group-focus-visible:text-svgb20-stroke">Duplicate workspace and invite team</span>
          </button>
          <span class="font-svgb20-mono text-[11px] tabular-nums text-svgb20-muted text-end">3.0px</span>
        </li>
      </ol>

      <div class="flex flex-col gap-3 pt-[18px] border-t border-svgb20-rest">
        <span class="font-svgb20-mono text-[10.5px] tracking-[0.16em] uppercase text-svgb20-muted">control &middot; fixed 2px</span>
        <div class="flex flex-wrap items-center gap-3.5">
          <button class="group relative inline-grid place-items-center justify-self-start min-w-24 min-h-[62px] px-[clamp(20px,2.6vw,32px)] border-0 rounded bg-transparent font-normal tracking-[-0.01em] text-[clamp(15px,calc(14px+var(--svgb-20-chars)*0.04px),18px)] cursor-pointer [transition:--svgb-20-duty_calc(340ms+var(--svgb-20-chars)*14ms)_cubic-bezier(0.22,1,0.36,1)] hover:[--svgb-20-duty:1] focus-visible:[--svgb-20-duty:1] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-svgb20-stroke focus-visible:outline-offset-[3px] text-svgb20-muted" type="button" data-chars="3" style="--svgb-20-chars: 3">
            <svg class="absolute inset-0 w-full h-full overflow-visible" aria-hidden="true"><rect class="svgb-20__ink fill-none [x:1.5px] [y:1.5px] [width:calc(100%-3px)] [height:calc(100%-3px)] [rx:4px] stroke-svgb20-rest [stroke-linecap:butt] [stroke-dasharray:calc(var(--svgb-20-duty)/var(--svgb-20-chars))_calc((1-var(--svgb-20-duty))/var(--svgb-20-chars))] transition-[stroke] duration-[240ms] group-hover:stroke-svgb20-stroke group-focus-visible:stroke-svgb20-stroke motion-reduce:[stroke-dasharray:none] [stroke-width:2px] [transition-duration:560ms]" data-chars="3" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="relative z-[1] whitespace-nowrap transition-colors duration-[260ms] motion-reduce:transition-none group-hover:text-svgb20-stroke group-focus-visible:text-svgb20-stroke">Buy</span>
          </button>
          <button class="group relative inline-grid place-items-center justify-self-start min-w-24 min-h-[62px] px-[clamp(20px,2.6vw,32px)] border-0 rounded bg-transparent font-normal tracking-[-0.01em] text-[clamp(15px,calc(14px+var(--svgb-20-chars)*0.04px),18px)] cursor-pointer [transition:--svgb-20-duty_calc(340ms+var(--svgb-20-chars)*14ms)_cubic-bezier(0.22,1,0.36,1)] hover:[--svgb-20-duty:1] focus-visible:[--svgb-20-duty:1] motion-reduce:transition-none focus-visible:outline-2 focus-visible:outline-svgb20-stroke focus-visible:outline-offset-[3px] text-svgb20-muted" type="button" data-chars="35" style="--svgb-20-chars: 35">
            <svg class="absolute inset-0 w-full h-full overflow-visible" aria-hidden="true"><rect class="svgb-20__ink fill-none [x:1.5px] [y:1.5px] [width:calc(100%-3px)] [height:calc(100%-3px)] [rx:4px] stroke-svgb20-rest [stroke-linecap:butt] [stroke-dasharray:calc(var(--svgb-20-duty)/var(--svgb-20-chars))_calc((1-var(--svgb-20-duty))/var(--svgb-20-chars))] transition-[stroke] duration-[240ms] group-hover:stroke-svgb20-stroke group-focus-visible:stroke-svgb20-stroke motion-reduce:[stroke-dasharray:none] [stroke-width:2px] [transition-duration:560ms]" data-chars="35" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="relative z-[1] whitespace-nowrap transition-colors duration-[260ms] motion-reduce:transition-none group-hover:text-svgb20-stroke group-focus-visible:text-svgb20-stroke">Duplicate workspace and invite team</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Both properties must be registered, and neither can be a utility. An
   unregistered custom property is an untyped token, so calc() with a unit can
   fail to resolve — and an unregistered number cannot be interpolated, which
   is what the hover transition depends on. */

@property --svgb-20-chars {
  syntax: '<integer>';
  inherits: true;
  initial-value: 12;
}
/* the duty cycle of the measure: 0.65 = ticks with gaps, 1 = a closed border */

@property --svgb-20-duty {
  syntax: '<number>';
  inherits: true;
  initial-value: 0.65;
}

@theme {
  --color-svgb20-bg: #101010;
  --color-svgb20-bg: oklch(0.18 0 0);
  --color-svgb20-fg: #f4f4f0;
  --color-svgb20-fg: oklch(0.96 0.005 100);
  --color-svgb20-muted: #8d8d86;
  --color-svgb20-muted: oklch(0.67 0.008 100);
  --color-svgb20-rest: rgba(244, 244, 240, 0.16);
  --color-svgb20-rest: oklch(0.96 0.005 100 / 0.16);
  --color-svgb20-stroke: #d8ff2b;
  --color-svgb20-stroke: oklch(0.93 0.22 116);
  --font-svgb20-sans: 'Archivo', system-ui, sans-serif;
  --font-svgb20-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Progressive enhancement: attr() with a type reads the count straight off the
   rect and drops the inline custom property entirely. A feature query is not a
   variant, so this cannot move into the markup. */

@supports (stroke-width: attr(data-chars type(<number>))) {
  .svgb-20__ink {
    stroke-width: clamp(1.5px, calc(1.1px + attr(data-chars type(<number>), 12) * 0.055px), 3px);
  }
}

.svgb-20:has(#svgb-20-theme:checked) {
  --color-svgb20-bg: #f4f4f0;
  --color-svgb20-bg: oklch(0.96 0.005 100);
  --color-svgb20-fg: #111111;
  --color-svgb20-fg: oklch(0.185 0 0);
  --color-svgb20-muted: #5e5e58;
  --color-svgb20-muted: oklch(0.50 0.008 100);
  --color-svgb20-rest: rgba(17, 17, 17, 0.18);
  --color-svgb20-rest: oklch(0.185 0 0 / 0.18);
  --color-svgb20-stroke: #4a5c00;
  --color-svgb20-stroke: oklch(0.44 0.14 116);
}
```

## JavaScript
```js
/* Optional convenience: the count can equally be printed into the markup by your template. */
(function () {
  var root = document.querySelector('.svgb-20');
  if (!root) return;
  root.querySelectorAll('.svgb-20__btn').forEach(function (btn) {
    var n = btn.querySelector('.svgb-20__label').textContent.trim().length;
    btn.dataset.chars = String(n);
    btn.style.setProperty('--svgb-20-chars', String(n));
    /* attr() resolves against the element the declaration sits on, so the rect
       needs its own copy — the button's attribute is not in scope for it. */
    var ink = btn.querySelector('.svgb-20__ink');
    if (ink) ink.dataset.chars = String(n);
  });
})();
```
