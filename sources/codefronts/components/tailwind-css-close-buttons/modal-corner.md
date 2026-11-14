---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/modal-corner/"
title: "Tailwind Lightbox Image Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "Legible over any photo: dark translucent fill, backdrop-blur-md and a white hairline — three layers that survive white skies and black shadows alike — with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Lightbox Image Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/modal-corner/

Legible over any photo: dark translucent fill, backdrop-blur-md and a white hairline — three layers that survive white skies and black shadows alike — with top-[max(14px,env(safe-area-inset-top))] keeping the × clear of the notch in full-screen viewers. The port adds the chrome real lightboxes need: a counter and a scrim-backed caption.
## HTML
```html
<section class="tcb-26 w-full min-h-svh grid place-items-center bg-tcb26-bg px-6 py-12 font-tcb26-sans" aria-label="Lightbox image close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <div role="dialog" aria-label="Photo viewer" class="relative aspect-16/10 w-full max-w-[28rem] overflow-hidden rounded-2xl shadow-[0_30px_70px_-30px_rgb(0_0_0/0.9)]">
      <div aria-hidden="true" class="absolute inset-0 bg-[radial-gradient(70%_60%_at_78%_18%,var(--color-tcb26-sun),var(--color-tcb26-gold)_30%,transparent_60%),linear-gradient(190deg,var(--color-tcb26-p1),var(--color-tcb26-p2)_38%,var(--color-tcb26-p3)_70%,var(--color-tcb26-p4))]"></div>
      <span class="absolute top-[max(14px,env(safe-area-inset-top))] start-3.5 rounded-full bg-[rgb(20_20_24/0.55)] px-2.5 py-1 font-tcb26-mono text-[11px] text-white ring-1 ring-white/18 backdrop-blur-md">3 / 12</span>
      <button type="button" aria-label="Close photo viewer" class="absolute top-[max(14px,env(safe-area-inset-top))] end-3.5 grid size-11 cursor-pointer place-items-center rounded-full border border-white/18 bg-[rgb(20_20_24/0.55)] backdrop-blur-md transition duration-180 hover:bg-[rgb(20_20_24/0.75)] focus-visible:outline-[2.5px] focus-visible:outline-offset-2 focus-visible:outline-white active:scale-92 motion-reduce:transition-none">
        <span aria-hidden="true" class="relative size-4 before:absolute before:top-1/2 before:left-1/2 before:h-[1.8px] before:w-4 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-white/95 after:absolute after:top-1/2 after:left-1/2 after:h-[1.8px] after:w-4 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-white/95"></span>
      </button>
      <div class="absolute inset-x-0 bottom-0 bg-linear-to-t from-black/60 to-transparent px-4 pt-8 pb-3.5">
        <span class="text-[13px] font-medium text-white">Golden hour, Big Sur</span>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tcb26-mono text-[11.5px] text-tcb26-mut ring-1 ring-white/12">backdrop-blur-md · border-white/18 · top-[max(14px,env(safe-area-inset-top))]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb26-bg: #0b0a10;
  --color-tcb26-bg: oklch(0.12 0.01 280);
  --color-tcb26-sun: #fff8e6;
  --color-tcb26-sun: oklch(0.98 0.03 90);
  --color-tcb26-gold: #f2bf63;
  --color-tcb26-gold: oklch(0.85 0.12 70);
  --color-tcb26-p1: #e39a4f;
  --color-tcb26-p1: oklch(0.75 0.13 60);
  --color-tcb26-p2: #b0502e;
  --color-tcb26-p2: oklch(0.55 0.14 40);
  --color-tcb26-p3: #3c2a57;
  --color-tcb26-p3: oklch(0.3 0.08 290);
  --color-tcb26-p4: #15121f;
  --color-tcb26-p4: oklch(0.16 0.03 280);
  --color-tcb26-mut: #a4a2b0;
  --color-tcb26-mut: oklch(0.74 0.02 280);
  --font-tcb26-sans: 'Geist', system-ui, sans-serif;
  --font-tcb26-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-26 {
  width: 100%;
  min-height: 100svh;
}
```
