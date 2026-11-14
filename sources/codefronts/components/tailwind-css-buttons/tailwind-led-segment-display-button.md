---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-led-segment-display-button/"
title: "Tailwind LED Segment Display Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A machined instrument panel with a real seven-segment readout: every digit is seven CSS bars lit from a lookup table, glowing with a layered bloom against a…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind LED Segment Display Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-led-segment-display-button/

A machined instrument panel with a real seven-segment readout: every digit is seven CSS bars lit from a lookup table, glowing with a layered bloom against a smoked lens. Press it and the counter ticks up with correct segment-by-segment switching.
## HTML
```html
<div class="tb-36 w-full min-h-svh grid place-items-center font-tb36-sans p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" aria-label="Increment the counter" class="tb-36__btn relative cursor-pointer grid place-items-center p-3.5 border border-tb36-edge rounded-[0.8rem] bg-[linear-gradient(180deg,var(--color-tb36-panel-hi),var(--color-tb36-panel))] shadow-[inset_0_1px_0_#ffffff24,inset_0_-2px_4px_#00000080,0_14px_26px_-12px_#000000cc] transition-[translate,box-shadow] duration-[160ms] [-webkit-tap-highlight-color:transparent] hover:-translate-y-px active:translate-y-0.5 active:shadow-[inset_0_2px_8px_#000000b3] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tb36-on motion-reduce:transition-none">
    <span aria-hidden="true" class="tb-36__lens flex gap-2 px-4 py-3 rounded-[0.45rem] shadow-[inset_0_2px_8px_#000000d9,inset_0_0_0_1px_#ffffff0d]">
      <span class="tb-36__digit relative block w-6.5 h-11.5"><i class="tb-36__seg tb-36__seg--a" data-s="a" data-on="false"></i><i class="tb-36__seg tb-36__seg--b" data-s="b" data-on="false"></i><i class="tb-36__seg tb-36__seg--c" data-s="c" data-on="false"></i><i class="tb-36__seg tb-36__seg--d" data-s="d" data-on="false"></i><i class="tb-36__seg tb-36__seg--e" data-s="e" data-on="false"></i><i class="tb-36__seg tb-36__seg--f" data-s="f" data-on="false"></i><i class="tb-36__seg tb-36__seg--g" data-s="g" data-on="false"></i></span>
      <span class="tb-36__digit relative block w-6.5 h-11.5"><i class="tb-36__seg tb-36__seg--a" data-s="a" data-on="false"></i><i class="tb-36__seg tb-36__seg--b" data-s="b" data-on="false"></i><i class="tb-36__seg tb-36__seg--c" data-s="c" data-on="false"></i><i class="tb-36__seg tb-36__seg--d" data-s="d" data-on="false"></i><i class="tb-36__seg tb-36__seg--e" data-s="e" data-on="false"></i><i class="tb-36__seg tb-36__seg--f" data-s="f" data-on="false"></i><i class="tb-36__seg tb-36__seg--g" data-s="g" data-on="false"></i></span>
      <span class="tb-36__digit relative block w-6.5 h-11.5"><i class="tb-36__seg tb-36__seg--a" data-s="a" data-on="false"></i><i class="tb-36__seg tb-36__seg--b" data-s="b" data-on="false"></i><i class="tb-36__seg tb-36__seg--c" data-s="c" data-on="false"></i><i class="tb-36__seg tb-36__seg--d" data-s="d" data-on="false"></i><i class="tb-36__seg tb-36__seg--e" data-s="e" data-on="false"></i><i class="tb-36__seg tb-36__seg--f" data-s="f" data-on="false"></i><i class="tb-36__seg tb-36__seg--g" data-s="g" data-on="false"></i></span>
    </span>
    <span role="status" aria-live="polite" class="tb-36__live sr-only">0</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb36-bg: #0b0d0c;
  --color-tb36-bg: oklch(0.13 0.008 150);
  --color-tb36-panel: #1c211f;
  --color-tb36-panel: oklch(0.24 0.012 150);
  --color-tb36-panel-hi: #2c3331;
  --color-tb36-panel-hi: oklch(0.3 0.012 150);
  --color-tb36-edge: #0a0d0c;
  --color-tb36-edge: oklch(0.12 0.008 150);
  --color-tb36-lens: #0a0f0d;
  --color-tb36-lens: oklch(0.12 0.012 155);
  --color-tb36-on: #5ef08a;
  --color-tb36-on: oklch(0.84 0.2 148);
  --color-tb36-on-60: #5ef08a99;
  --color-tb36-on-60: oklch(0.84 0.2 148 / 0.55);
  --color-tb36-on-30: #5ef08a47;
  --color-tb36-on-30: oklch(0.84 0.2 148 / 0.28);
  --color-tb36-off: #1f2b24;
  --color-tb36-off: oklch(0.28 0.03 150);
  --font-tb36-sans: "Chakra Petch", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
}

.tb-36 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(34rem 20rem at 50% 44%, #17201c, transparent 74%), var(--color-tb36-bg);
}

.tb-36__lens {
  background: radial-gradient(120% 140% at 50% 0%, rgba(255,255,255,.06), transparent 60%), var(--color-tb36-lens);
}
/* BAR GEOMETRY: 21 bars, two chamfer shapes, eight position rules. As utilities
   this would be 21 near-identical class lists differing by one edge. */

.tb-36__seg {
  position: absolute;
  display: block;
  border-radius: .06rem;
  background: var(--color-tb36-off);
  transition: background-color .09s linear, box-shadow .09s linear;
}

.tb-36__seg--a,
.tb-36__seg--d,
.tb-36__seg--g {
  left: 14%;
  width: 72%;
  height: .28rem;
  clip-path: polygon(.18rem 0, calc(100% - .18rem) 0, 100% 50%, calc(100% - .18rem) 100%, .18rem 100%, 0 50%);
}

.tb-36__seg--a {
  top: 0;
}

.tb-36__seg--g {
  top: calc(50% - .14rem);
}

.tb-36__seg--d {
  bottom: 0;
}

.tb-36__seg--b,
.tb-36__seg--c,
.tb-36__seg--e,
.tb-36__seg--f {
  width: .28rem;
  height: calc(50% - .34rem);
  clip-path: polygon(0 .18rem, 50% 0, 100% .18rem, 100% calc(100% - .18rem), 50% 100%, 0 calc(100% - .18rem));
}

.tb-36__seg--f {
  left: 0;
  top: .34rem;
}

.tb-36__seg--b {
  right: 0;
  top: .34rem;
}

.tb-36__seg--e {
  left: 0;
  bottom: .34rem;
}

.tb-36__seg--c {
  right: 0;
  bottom: .34rem;
}

.tb-36__seg[data-on="true"] {
  background: var(--color-tb36-on);
  box-shadow: 0 0 4px var(--color-tb36-on), 0 0 12px var(--color-tb36-on-60), 0 0 22px var(--color-tb36-on-30);
}

@media (prefers-reduced-motion: reduce) {
  .tb-36__seg {
    transition: none;
  }
}

@media (prefers-color-scheme: light) {
  .tb-36:not([data-theme="dark"]) {
    --color-tb36-bg: oklch(0.18 0.012 150);
  }
}

.tb-36[data-theme="light"] {
  --color-tb36-bg: oklch(0.18 0.012 150);
}

@media (forced-colors: active) {
  .tb-36__btn {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-36__lens {
    background: Canvas;
    box-shadow: none;
  }

  .tb-36__seg {
    background: GrayText;
    box-shadow: none;
  }

  .tb-36__seg[data-on="true"] {
    background: Highlight;
    box-shadow: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.tb-36__btn');
  if (!btn) return;
  const MAP = { 0:'abcdef', 1:'bc', 2:'abdeg', 3:'abcdg', 4:'bcfg', 5:'acdfg', 6:'acdefg', 7:'abc', 8:'abcdefg', 9:'abcdfg' };
  const digits = [...btn.querySelectorAll('.tb-36__digit')];
  const live = btn.querySelector('.tb-36__live');
  let value = 0;
  const render = () => {
    const text = String(value % 1000).padStart(digits.length, '0');
    digits.forEach((d, i) => {
      const lit = MAP[text[i]] || '';
      d.querySelectorAll('.tb-36__seg').forEach((s) => { s.dataset.on = String(lit.includes(s.dataset.s)); });
    });
    live.textContent = String(value % 1000);
  };
  btn.addEventListener('click', () => { value += 1; render(); });
  render();
})();
```
