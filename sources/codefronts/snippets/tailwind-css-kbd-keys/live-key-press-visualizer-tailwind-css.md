---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/live-key-press-visualizer-tailwind-css/"
title: "Live Key Press Visualizer with Tailwind CSS"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "A keystroke visualizer for screencasts and docs: focus the pad, press anything, and each press appears as a cap group — modifiers included, so Ctrl + Shift +…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Live Key Press Visualizer with Tailwind CSS
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/live-key-press-visualizer-tailwind-css/

A keystroke visualizer for screencasts and docs: focus the pad, press anything, and each press appears as a cap group — modifiers included, so Ctrl + Shift + K shows as one chord. Caps animate in with zero JS via starting: (@starting-style), leave via a data-out: variant, and a readout shows event.key beside event.code so the difference is visible.
## HTML
```html
<section id="kbd-15-root" class="kbd-15 relative w-full min-h-svh scheme-light kbd15-dark:scheme-dark bg-kbd15-bg bg-[radial-gradient(70%_55%_at_50%_45%,var(--color-kbd15-glow),transparent_70%)] text-kbd15-ink font-kbd15-sans" aria-label="Live key press feedback demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
    <div class="grid w-full min-w-0 max-w-[40rem] justify-items-center gap-6 text-center">
      <button type="button" data-pad class="group grid min-h-56 w-full place-content-center gap-5 rounded-3xl border border-dashed border-kbd15-rim bg-kbd15-pad p-6 transition-[border-color,box-shadow] focus:border-solid focus:border-kbd15-acc focus:shadow-[0_0_0_4px_var(--color-kbd15-ring)] focus:outline-none motion-reduce:transition-none">
        <span data-idle class="text-[15px] text-kbd15-mut"><span class="group-focus:hidden">Click here, then press any key</span><span class="hidden group-focus:inline">Listening — press any key or chord</span></span>
        <span data-list aria-live="polite" class="flex min-h-14 flex-wrap items-center justify-center gap-3"></span>
      </button>
      <p data-readout class="min-h-5 font-kbd15-mono text-[12.5px] text-kbd15-mut">key · code readout appears here</p>
      <p class="text-[12.5px] text-kbd15-mut">One group per physical press · repeats suppressed · Tab still moves focus</p>
      <kbd data-chip hidden class="inline-flex items-center gap-1.5 rounded-2xl bg-kbd15-tray p-1.5 ring-1 ring-kbd15-rule transition-[opacity,translate,scale] duration-300 ease-out starting:translate-y-3 starting:scale-90 starting:opacity-0 data-out:-translate-y-2 data-out:opacity-0 motion-reduce:transition-none"></kbd>
      <kbd data-cap hidden class="inline-flex h-14 min-w-14 items-center justify-center rounded-xl border border-kbd15-caprim bg-linear-to-b from-kbd15-captop to-kbd15-cap px-4 font-kbd15-mono text-lg font-semibold text-kbd15-capink shadow-[0_4px_0_var(--color-kbd15-edge)]"></kbd>
    </div>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-15-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-15-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd15-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd15-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd15-dark:bg-transparent kbd15-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd15-dark:hidden">Light</span><span class="hidden kbd15-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd15-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-15:not(:has(#kbd-15-theme:checked)), .kbd-15:not(:has(#kbd-15-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-15:has(#kbd-15-theme:checked), .kbd-15:has(#kbd-15-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd15-bg: light-dark(#eef0f4, #08090c);
  --color-kbd15-bg: light-dark(oklch(0.955 0.006 264.5), oklch(0.14 0.007 269.7));
  --color-kbd15-glow: light-dark(#dfe5ff, #141a33);
  --color-kbd15-glow: light-dark(oklch(0.925 0.036 275.4), oklch(0.226 0.049 271.8));
  --color-kbd15-pad: light-dark(#ffffff, #0f1116);
  --color-kbd15-pad: light-dark(oklch(1 0 0), oklch(0.178 0.011 268.1));
  --color-kbd15-ring: light-dark(#4f6bed33, #7c93ff40);
  --color-kbd15-ring: light-dark(oklch(0.579 0.198 270 / 0.2), oklch(0.694 0.16 272.5 / 0.25));
  --color-kbd15-ink: light-dark(#151821, #e9ebf2);
  --color-kbd15-ink: light-dark(oklch(0.21 0.018 270.4), oklch(0.941 0.01 273.4));
  --color-kbd15-mut: light-dark(#585f6e, #979eae);
  --color-kbd15-mut: light-dark(oklch(0.485 0.026 265.6), oklch(0.699 0.025 266.8));
  --color-kbd15-rim: light-dark(#c4cad6, #2f3442);
  --color-kbd15-rim: light-dark(oklch(0.838 0.018 264.5), oklch(0.326 0.026 269.6));
  --color-kbd15-rule: light-dark(#dde1ea, #23283a);
  --color-kbd15-rule: light-dark(oklch(0.909 0.013 266.7), oklch(0.28 0.034 272.1));
  --color-kbd15-tray: light-dark(#f1f3f8, #161a26);
  --color-kbd15-tray: light-dark(oklch(0.964 0.007 268.5), oklch(0.22 0.024 270.1));
  --color-kbd15-cap: light-dark(#f6f7fb, #222838);
  --color-kbd15-cap: light-dark(oklch(0.977 0.005 275), oklch(0.278 0.031 268.5));
  --color-kbd15-captop: light-dark(#ffffff, #2d3449);
  --color-kbd15-captop: light-dark(oklch(1 0 0), oklch(0.328 0.039 270));
  --color-kbd15-caprim: light-dark(#c9cfdb, #3d4560);
  --color-kbd15-caprim: light-dark(oklch(0.853 0.018 264.5), oklch(0.395 0.047 271.4));
  --color-kbd15-edge: light-dark(#a9b0c0, #040509);
  --color-kbd15-edge: light-dark(oklch(0.757 0.024 266.9), oklch(0.116 0.012 270.7));
  --color-kbd15-capink: light-dark(#1c2030, #eef0f8);
  --color-kbd15-capink: light-dark(oklch(0.247 0.031 273.1), oklch(0.956 0.011 274.9));
  --color-kbd15-acc: light-dark(#4f6bed, #7c93ff);
  --color-kbd15-acc: light-dark(oklch(0.579 0.198 270), oklch(0.694 0.16 272.5));
  --font-kbd15-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-kbd15-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-15 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('kbd-15-root');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const pad = root.querySelector('[data-pad]'), list = root.querySelector('[data-list]');
  const chip = root.querySelector('[data-chip]'), cap = root.querySelector('[data-cap]'), readout = root.querySelector('[data-readout]');
  const isMac = /mac/i.test(navigator.userAgentData?.platform || navigator.platform);
  const names = { ' ': 'Space', Escape: 'Esc', Control: 'Ctrl', Meta: isMac ? '\u2318' : 'Win', ArrowUp: '\u2191', ArrowDown: '\u2193', ArrowLeft: '\u2190', ArrowRight: '\u2192' };
  const label = (k) => names[k] ?? (k.length === 1 ? k.toUpperCase() : k);
  const clone = (el) => { const c = el.cloneNode(); c.removeAttribute('hidden'); return c; };
  pad.addEventListener('keydown', (e) => {
    if (e.repeat || e.key === 'Tab') return;
    e.preventDefault();
    const mods = [e.ctrlKey && 'Control', e.altKey && 'Alt', e.shiftKey && 'Shift', e.metaKey && 'Meta'].filter((m) => m && m !== e.key);
    const g = clone(chip);
    [...mods, e.key].forEach((k) => { const c = clone(cap); c.textContent = label(k); g.append(c); });
    list.append(g);
    readout.textContent = 'key: "' + e.key + '" \u00b7 code: "' + e.code + '"';
    while (list.childElementCount > 4) list.firstElementChild.remove();
    setTimeout(() => { g.setAttribute('data-out', ''); setTimeout(() => g.remove(), 300); }, 1600);
  });
})();
```
