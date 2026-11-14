---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-fullscreen-radial-menu-overlay-with-dialog-and-backdrop-blur/"
title: "Tailwind CSS Fullscreen Radial Menu Overlay with dialog and Backdrop Blur"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "The full-takeover finale: a festival site&rsquo;s CTA blooms into a modal <dialog> where six destinations circle a glowing monogram while soft bokeh drifts…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Fullscreen Radial Menu Overlay with dialog and Backdrop Blur
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-fullscreen-radial-menu-overlay-with-dialog-and-backdrop-blur/

The full-takeover finale: a festival site&rsquo;s CTA blooms into a modal <dialog> where six destinations circle a glowing monogram while soft bokeh drifts through a frosted ::backdrop. showModal() gives focus trapping, Escape and an inert page for free; open:, starting:open: and transition-discrete animate it both ways, and backdrop:backdrop-blur-xl frosts the page behind.
## HTML
```html
<section class="tcm-26 relative w-full min-h-svh grid place-items-center overflow-hidden bg-linear-160 from-tcm26-bg1 via-tcm26-bg2 to-tcm26-bg3 px-5 py-14 font-tcm26-sans text-white antialiased" aria-label="Fullscreen radial menu overlay demo">
  <div id="tcm-26-site" class="relative grid justify-items-center gap-4 text-center">
    <p class="font-tcm26-mono text-[12px] tracking-[0.24em] text-white/75 uppercase">June 18–20 · Reykjavík</p>
    <h2 class="font-tcm26-display text-[clamp(2.6rem,9vw,5rem)] leading-[0.92] font-extrabold tracking-[-0.03em]">Aurora<br><span class="bg-linear-to-r from-tcm26-a via-tcm26-c to-tcm26-b bg-clip-text text-transparent">Festival &rsquo;27</span></h2>
    <p class="max-w-[24rem] text-[15px] text-white/80">Three nights of light, sound and code under the midnight sun.</p>
    <button type="button" data-open class="mt-3 min-h-12 cursor-pointer rounded-full bg-white/10 px-7 text-[15px] font-bold tracking-[0.02em] text-white ring-1 ring-white/35 shadow-tcm26-glow backdrop-blur-md transition-[background-color,scale] duration-300 hover:scale-[1.03] hover:bg-white/18 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tcm26-a">Explore the festival</button>
    <dialog data-dialog aria-label="Festival navigation" class="fixed inset-0 m-0 grid h-full max-h-none w-full max-w-none place-items-center overflow-hidden border-0 bg-transparent p-0 text-white not-open:hidden opacity-0 scale-95 transition-[opacity,scale,display,overlay] transition-discrete duration-500 ease-[cubic-bezier(.16,1,.3,1)] open:opacity-100 open:scale-100 starting:open:opacity-0 starting:open:scale-90 backdrop:bg-[radial-gradient(circle_at_50%_50%,var(--color-tcm26-veil),var(--color-tcm26-veil2))] backdrop:backdrop-blur-xl motion-reduce:transition-none">
      <div aria-hidden="true" class="pointer-events-none absolute inset-0 motion-reduce:hidden">
      <span class="absolute rounded-full bg-tcm26-a/50 animate-tcm26-drift" style="width:30px;height:30px;left:21.7%;top:93.3%;filter:blur(4.3px);animation-duration:10.5s;animation-delay:-7.9s"></span>
      <span class="absolute rounded-full bg-tcm26-b/50 animate-tcm26-drift" style="width:25px;height:25px;left:96.2%;top:43.0%;filter:blur(3.6px);animation-duration:10.4s;animation-delay:-5.8s"></span>
      <span class="absolute rounded-full bg-tcm26-c/50 animate-tcm26-drift" style="width:67px;height:67px;left:72.0%;top:36.2%;filter:blur(9.6px);animation-duration:12.7s;animation-delay:-8.4s"></span>
      <span class="absolute rounded-full bg-tcm26-d/50 animate-tcm26-drift" style="width:11px;height:11px;left:89.9%;top:73.2%;filter:blur(1.6px);animation-duration:14.8s;animation-delay:-1.9s"></span>
      <span class="absolute rounded-full bg-tcm26-a/50 animate-tcm26-drift" style="width:24px;height:24px;left:32.0%;top:83.9%;filter:blur(3.4px);animation-duration:12.6s;animation-delay:-9.6s"></span>
      <span class="absolute rounded-full bg-tcm26-b/50 animate-tcm26-drift" style="width:31px;height:31px;left:31.7%;top:72.4%;filter:blur(4.4px);animation-duration:7.9s;animation-delay:-8.8s"></span>
      <span class="absolute rounded-full bg-tcm26-c/50 animate-tcm26-drift" style="width:40px;height:40px;left:52.4%;top:27.8%;filter:blur(5.8px);animation-duration:12.1s;animation-delay:-0.3s"></span>
      <span class="absolute rounded-full bg-tcm26-d/50 animate-tcm26-drift" style="width:33px;height:33px;left:31.3%;top:2.4%;filter:blur(4.7px);animation-duration:11.1s;animation-delay:-2.1s"></span>
      <span class="absolute rounded-full bg-tcm26-a/50 animate-tcm26-drift" style="width:66px;height:66px;left:91.2%;top:55.6%;filter:blur(9.5px);animation-duration:8.6s;animation-delay:-2.1s"></span>
      <span class="absolute rounded-full bg-tcm26-b/50 animate-tcm26-drift" style="width:63px;height:63px;left:17.3%;top:65.6%;filter:blur(9.0px);animation-duration:12.1s;animation-delay:-4.0s"></span>
      <span class="absolute rounded-full bg-tcm26-c/50 animate-tcm26-drift" style="width:56px;height:56px;left:2.7%;top:6.7%;filter:blur(8.1px);animation-duration:15.5s;animation-delay:-8.2s"></span>
      <span class="absolute rounded-full bg-tcm26-d/50 animate-tcm26-drift" style="width:58px;height:58px;left:58.8%;top:94.1%;filter:blur(8.3px);animation-duration:15.6s;animation-delay:-1.4s"></span>
      <span class="absolute rounded-full bg-tcm26-a/50 animate-tcm26-drift" style="width:24px;height:24px;left:93.2%;top:94.8%;filter:blur(3.4px);animation-duration:15.6s;animation-delay:-1.9s"></span>
      <span class="absolute rounded-full bg-tcm26-b/50 animate-tcm26-drift" style="width:40px;height:40px;left:54.4%;top:5.2%;filter:blur(5.7px);animation-duration:8.7s;animation-delay:-4.9s"></span>
      <span class="absolute rounded-full bg-tcm26-c/50 animate-tcm26-drift" style="width:12px;height:12px;left:42.8%;top:96.3%;filter:blur(1.7px);animation-duration:11.5s;animation-delay:-7.7s"></span>
      <span class="absolute rounded-full bg-tcm26-d/50 animate-tcm26-drift" style="width:48px;height:48px;left:88.3%;top:23.7%;filter:blur(6.8px);animation-duration:14.3s;animation-delay:-7.2s"></span>
      </div>
      <nav class="relative grid size-[min(24rem,94vw)] place-items-center [--r:min(9.5rem,37vw)]" aria-label="Festival">
        <span aria-hidden="true" class="absolute inset-[calc(50%-var(--r))] rounded-full border border-dashed border-white/20"></span>
        <ul class="absolute inset-0">
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:0] [--a:calc(360deg/6*var(--i)-90deg)]">
          <a href="#tcm-26-lineup" data-item class="tcm26-polar pointer-events-auto min-w-[5.5rem] rounded-full bg-white/10 px-5 py-3.5 text-center text-[15px] font-bold tracking-[0.04em] text-white ring-1 ring-white/25 backdrop-blur-md transition-[background-color,translate,box-shadow] duration-300 hover:bg-white/20 hover:shadow-tcm26-glow focus-visible:bg-white/20 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm26-a">Lineup</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:1] [--a:calc(360deg/6*var(--i)-90deg)]">
          <a href="#tcm-26-tickets" data-item class="tcm26-polar pointer-events-auto min-w-[5.5rem] rounded-full bg-white/10 px-5 py-3.5 text-center text-[15px] font-bold tracking-[0.04em] text-white ring-1 ring-white/25 backdrop-blur-md transition-[background-color,translate,box-shadow] duration-300 hover:bg-white/20 hover:shadow-tcm26-glow focus-visible:bg-white/20 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm26-a">Tickets</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:2] [--a:calc(360deg/6*var(--i)-90deg)]">
          <a href="#tcm-26-map" data-item class="tcm26-polar pointer-events-auto min-w-[5.5rem] rounded-full bg-white/10 px-5 py-3.5 text-center text-[15px] font-bold tracking-[0.04em] text-white ring-1 ring-white/25 backdrop-blur-md transition-[background-color,translate,box-shadow] duration-300 hover:bg-white/20 hover:shadow-tcm26-glow focus-visible:bg-white/20 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm26-a">Map</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:3] [--a:calc(360deg/6*var(--i)-90deg)]">
          <a href="#tcm-26-food" data-item class="tcm26-polar pointer-events-auto min-w-[5.5rem] rounded-full bg-white/10 px-5 py-3.5 text-center text-[15px] font-bold tracking-[0.04em] text-white ring-1 ring-white/25 backdrop-blur-md transition-[background-color,translate,box-shadow] duration-300 hover:bg-white/20 hover:shadow-tcm26-glow focus-visible:bg-white/20 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm26-a">Food</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:4] [--a:calc(360deg/6*var(--i)-90deg)]">
          <a href="#tcm-26-art" data-item class="tcm26-polar pointer-events-auto min-w-[5.5rem] rounded-full bg-white/10 px-5 py-3.5 text-center text-[15px] font-bold tracking-[0.04em] text-white ring-1 ring-white/25 backdrop-blur-md transition-[background-color,translate,box-shadow] duration-300 hover:bg-white/20 hover:shadow-tcm26-glow focus-visible:bg-white/20 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm26-a">Art</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:5] [--a:calc(360deg/6*var(--i)-90deg)]">
          <a href="#tcm-26-faq" data-item class="tcm26-polar pointer-events-auto min-w-[5.5rem] rounded-full bg-white/10 px-5 py-3.5 text-center text-[15px] font-bold tracking-[0.04em] text-white ring-1 ring-white/25 backdrop-blur-md transition-[background-color,translate,box-shadow] duration-300 hover:bg-white/20 hover:shadow-tcm26-glow focus-visible:bg-white/20 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm26-a">FAQ</a>
        </li>
        </ul>
        <div aria-hidden="true" class="grid size-32 place-content-center justify-items-center rounded-full bg-[radial-gradient(circle_at_38%_32%,var(--color-tcm26-core-hi),var(--color-tcm26-core)_72%)] ring-1 ring-white/25 shadow-tcm26-core">
          <b class="bg-linear-to-r from-tcm26-a to-tcm26-b bg-clip-text font-tcm26-display text-[2rem] text-transparent">AF</b><span class="text-[11px] tracking-[0.3em] text-white/75">&rsquo;27</span>
        </div>
      </nav>
      <button type="button" data-close-dialog aria-label="Close menu" class="absolute top-5 right-5 grid size-12 cursor-pointer place-items-center rounded-full bg-white/10 text-white ring-1 ring-white/30 transition-[background-color,rotate] duration-300 hover:rotate-90 hover:bg-white/20 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm26-a"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg></button>
    </dialog>
  </div>
  <div class="absolute bottom-6">
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm26-card px-3.5 py-2 text-center font-tcm26-mono text-[11.5px] text-tcm26-mut ring-1 ring-tcm26-line ">dialog.showModal() · open: · starting:open: · backdrop:backdrop-blur-xl</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm26-bg1: #4c1d95;
  --color-tcm26-bg1: oklch(0.38 0.178 293.7);
  --color-tcm26-bg2: #1e3a8a;
  --color-tcm26-bg2: oklch(0.379 0.138 265.5);
  --color-tcm26-bg3: #0f766e;
  --color-tcm26-bg3: oklch(0.511 0.086 186.4);
  --color-tcm26-a: #5eead4;
  --color-tcm26-a: oklch(0.855 0.125 181.1);
  --color-tcm26-b: #f0abfc;
  --color-tcm26-b: oklch(0.833 0.132 321.4);
  --color-tcm26-c: #a5b4fc;
  --color-tcm26-c: oklch(0.785 0.104 274.7);
  --color-tcm26-d: #fde68a;
  --color-tcm26-d: oklch(0.924 0.115 95.7);
  --color-tcm26-veil: #312e81bf;
  --color-tcm26-veil: oklch(0.359 0.135 278.7 / 0.75);
  --color-tcm26-veil2: #0b0a2aeb;
  --color-tcm26-veil2: oklch(0.171 0.063 278.8 / 0.92);
  --color-tcm26-core: #1e1b4b;
  --color-tcm26-core: oklch(0.257 0.086 281.3);
  --color-tcm26-core-hi: #3730a3;
  --color-tcm26-core-hi: oklch(0.398 0.177 277.4);
  --color-tcm26-card: #ffffff1f;
  --color-tcm26-card: oklch(1 0 0 / 0.12);
  --color-tcm26-mut: #ffffffd9;
  --color-tcm26-mut: oklch(1 0 0 / 0.85);
  --color-tcm26-line: #ffffff40;
  --color-tcm26-line: oklch(1 0 0 / 0.25);
  --font-tcm26-sans: 'Inter', system-ui, sans-serif;
  --font-tcm26-display: 'Syne', system-ui, sans-serif;
  --font-tcm26-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm26-glow: 0 0 40px -8px oklch(0.85 0.12 180 / 0.55);
  --shadow-tcm26-core: 0 0 90px -10px oklch(0.85 0.12 180 / 0.5), 0 0 140px -20px oklch(0.8 0.15 320 / 0.45), inset 0 1px 0 oklch(1 0 0 / 0.2);
  --animate-tcm26-drift: tcm26-drift 10s ease-in-out infinite alternate;

  @keyframes tcm26-drift {
    from {
      translate: -10px 24px;
    }

    to {
      translate: 12px -24px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-26 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm26-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: polar night: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-26:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm26-bg1: #2e1065;
    --color-tcm26-bg1: oklch(0.283 0.135 291.1);
    --color-tcm26-bg2: #0c1530;
    --color-tcm26-bg2: oklch(0.205 0.055 267.5);
    --color-tcm26-bg3: #042f2e;
    --color-tcm26-bg3: oklch(0.277 0.045 192.5);
    --color-tcm26-a: #5eead4;
    --color-tcm26-a: oklch(0.855 0.125 181.1);
    --color-tcm26-b: #f0abfc;
    --color-tcm26-b: oklch(0.833 0.132 321.4);
    --color-tcm26-c: #a5b4fc;
    --color-tcm26-c: oklch(0.785 0.104 274.7);
    --color-tcm26-d: #fde68a;
    --color-tcm26-d: oklch(0.924 0.115 95.7);
    --color-tcm26-veil: #1e1b4bcc;
    --color-tcm26-veil: oklch(0.257 0.086 281.3 / 0.8);
    --color-tcm26-veil2: #05040ff2;
    --color-tcm26-veil2: oklch(0.118 0.028 287 / 0.95);
    --color-tcm26-core: #141236;
    --color-tcm26-core: oklch(0.209 0.068 281.2);
    --color-tcm26-core-hi: #2e2a7a;
    --color-tcm26-core-hi: oklch(0.343 0.131 279.1);
    --color-tcm26-card: #ffffff17;
    --color-tcm26-card: oklch(1 0 0 / 0.09);
    --color-tcm26-mut: #ffffffd9;
    --color-tcm26-mut: oklch(1 0 0 / 0.85);
    --color-tcm26-line: #ffffff33;
    --color-tcm26-line: oklch(1 0 0 / 0.2);
  }
}

.tcm-26[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm26-bg1: #2e1065;
  --color-tcm26-bg1: oklch(0.283 0.135 291.1);
  --color-tcm26-bg2: #0c1530;
  --color-tcm26-bg2: oklch(0.205 0.055 267.5);
  --color-tcm26-bg3: #042f2e;
  --color-tcm26-bg3: oklch(0.277 0.045 192.5);
  --color-tcm26-a: #5eead4;
  --color-tcm26-a: oklch(0.855 0.125 181.1);
  --color-tcm26-b: #f0abfc;
  --color-tcm26-b: oklch(0.833 0.132 321.4);
  --color-tcm26-c: #a5b4fc;
  --color-tcm26-c: oklch(0.785 0.104 274.7);
  --color-tcm26-d: #fde68a;
  --color-tcm26-d: oklch(0.924 0.115 95.7);
  --color-tcm26-veil: #1e1b4bcc;
  --color-tcm26-veil: oklch(0.257 0.086 281.3 / 0.8);
  --color-tcm26-veil2: #05040ff2;
  --color-tcm26-veil2: oklch(0.118 0.028 287 / 0.95);
  --color-tcm26-core: #141236;
  --color-tcm26-core: oklch(0.209 0.068 281.2);
  --color-tcm26-core-hi: #2e2a7a;
  --color-tcm26-core-hi: oklch(0.343 0.131 279.1);
  --color-tcm26-card: #ffffff17;
  --color-tcm26-card: oklch(1 0 0 / 0.09);
  --color-tcm26-mut: #ffffffd9;
  --color-tcm26-mut: oklch(1 0 0 / 0.85);
  --color-tcm26-line: #ffffff33;
  --color-tcm26-line: oklch(1 0 0 / 0.2);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-26-site');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const dlg = root.querySelector('[data-dialog]');
  root.querySelector('[data-open]').addEventListener('click', () => dlg.showModal());
  dlg.querySelector('[data-close-dialog]').addEventListener('click', () => dlg.close());
  dlg.querySelectorAll('[data-item]').forEach((a) => a.addEventListener('click', () => dlg.close()));
  dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); });
})();
```
