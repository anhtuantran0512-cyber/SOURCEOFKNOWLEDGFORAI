---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/tailwind-video-player-overlay-close-button/"
title: "Tailwind Video Player Overlay Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "Player chrome that gets out of the way: a gradient top bar with a blurred glass × that fades after 2.4s of stillness via group-data-idle/player:opacity-0.…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Video Player Overlay Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/tailwind-video-player-overlay-close-button/

Player chrome that gets out of the way: a gradient top bar with a blurred glass × that fades after 2.4s of stillness via group-data-idle/player:opacity-0. The port closes the original's keyboard gap — any key press or focus inside the player now wakes the chrome, and it never idles while focus is inside — and adds a matching bottom scrubber that hides with it.
## HTML
```html
<section class="tcb-09 w-full min-h-svh grid place-items-center bg-tcb09-bg px-6 py-12 font-tcb09-sans" aria-label="Video player overlay close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <div id="tcb-09-player" class="group/player relative aspect-video w-full max-w-[28rem] overflow-hidden rounded-2xl shadow-[0_26px_60px_-28px_rgb(0_0_0/0.9)] ring-1 ring-white/10">
      <div aria-hidden="true" class="absolute inset-0 grid place-items-center bg-[radial-gradient(80%_70%_at_30%_25%,var(--color-tcb09-v1),transparent_55%),linear-gradient(200deg,var(--color-tcb09-v2),var(--color-tcb09-v3)_55%,var(--color-tcb09-v4))]">
        <span class="grid size-15 place-items-center rounded-full bg-black/45 backdrop-blur-sm"><span class="ms-1 size-5 bg-white [clip-path:polygon(0_0,100%_50%,0_100%)]"></span></span>
      </div>
      <div class="absolute inset-x-0 top-0 flex items-center justify-between gap-3 bg-linear-to-b from-black/62 to-transparent pt-3 pe-3 pb-7 ps-4 transition-opacity duration-300 group-data-idle/player:pointer-events-none group-data-idle/player:opacity-0 motion-reduce:transition-none">
        <span class="truncate text-[13px] font-medium text-white [text-shadow:0_1px_4px_rgb(0_0_0/0.5)]">Trail running the Dolomites</span>
        <button type="button" aria-label="Close player" class="group grid size-11 flex-none cursor-pointer place-items-center rounded-full border border-white/16 bg-[rgb(15_15_18/0.55)] backdrop-blur-sm transition duration-150 hover:bg-[rgb(15_15_18/0.8)] focus-visible:outline-[2.5px] focus-visible:outline-offset-2 focus-visible:outline-white active:scale-90 motion-reduce:transition-none">
          <span aria-hidden="true" class="relative size-3.5 before:absolute before:top-1/2 before:left-1/2 before:h-[1.8px] before:w-3.5 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-white after:absolute after:top-1/2 after:left-1/2 after:h-[1.8px] after:w-3.5 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-white"></span>
        </button>
      </div>
      <div aria-hidden="true" class="absolute inset-x-0 bottom-0 flex items-center gap-3 bg-linear-to-t from-black/60 to-transparent px-4 pt-6 pb-3 font-tcb09-mono text-[11px] text-white transition-opacity duration-300 group-data-idle/player:opacity-0 motion-reduce:transition-none">
        <span>1:12</span>
        <span class="relative h-1 flex-1 overflow-hidden rounded-full bg-white/25"><span class="absolute inset-y-0 start-0 w-[38%] rounded-full bg-white"></span></span>
        <span>3:08</span>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tcb09-mono text-[11.5px] text-tcb09-mut ring-1 ring-white/12">group-data-idle/player:opacity-0 · wakes on move, key &amp; focus</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb09-bg: #0c0e12;
  --color-tcb09-bg: oklch(0.14 0.01 260);
  --color-tcb09-mut: #a6aab5;
  --color-tcb09-mut: oklch(0.74 0.015 260);
  --color-tcb09-v1: #b9d6e6;
  --color-tcb09-v1: oklch(0.8 0.06 220);
  --color-tcb09-v2: #6ea3cf;
  --color-tcb09-v2: oklch(0.72 0.1 230);
  --color-tcb09-v3: #3e5790;
  --color-tcb09-v3: oklch(0.45 0.09 260);
  --color-tcb09-v4: #1f1d3a;
  --color-tcb09-v4: oklch(0.25 0.05 280);
  --font-tcb09-sans: 'Geist', system-ui, sans-serif;
  --font-tcb09-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-09 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const player = document.getElementById('tcb-09-player');
  if (!player || player.dataset.wired) return;
  player.dataset.wired = '1';
  const IDLE = 2400;
  let timer = 0;
  const sleep = () => { if (!player.matches(':focus-within')) player.setAttribute('data-idle', ''); };
  const wake = () => {
    player.removeAttribute('data-idle');
    clearTimeout(timer);
    timer = setTimeout(sleep, IDLE);
  };
  ['pointermove', 'pointerdown', 'keydown', 'focusin'].forEach((ev) => player.addEventListener(ev, wake));
  player.addEventListener('focusout', wake);
  wake();
})();
```
