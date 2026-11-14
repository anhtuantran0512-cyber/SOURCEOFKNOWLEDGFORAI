---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-camera-aperture-menu-animation-iris-reveal/"
title: "Tailwind CSS Camera Aperture Menu Animation (Iris Reveal)"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A photography portfolio menu behind a working iris: eight blades pivot on the barrel rim and swing open together &mdash;…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Camera Aperture Menu Animation (Iris Reveal)
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-camera-aperture-menu-animation-iris-reveal/

A photography portfolio menu behind a working iris: eight blades pivot on the barrel rim and swing open together &mdash; group-data-open/lens:rotate-[calc(var(--i)*45deg+108deg)] &mdash; while the portfolio is exposed by a synchronised [clip-path:circle(9%)] &rarr; circle(50%). A knurled focus ring, a gold bezel and an f-stop that ticks from f/1.8 to f/8 finish the instrument.
## HTML
```html
<section class="tcm-23 w-full min-h-svh grid place-items-center bg-tcm23-bg bg-[radial-gradient(50%_45%_at_50%_45%,var(--color-tcm23-glow),transparent_72%)] px-4 py-14 font-tcm23-sans text-tcm23-ink antialiased" aria-label="Camera aperture menu demo">
  <div class="grid w-full justify-items-center gap-6">
    <header class="grid justify-items-center gap-1 text-center">
      <p class="font-tcm23-mono text-[11px] tracking-[0.22em] text-tcm23-gold-ink uppercase">Elena Varga · Photography</p>
      <h2 class="text-[clamp(1.6rem,4.5vw,2.3rem)] font-semibold tracking-[-0.03em]">Open the lens</h2>
    </header>
    <div id="tcm-23-lens" class="group/lens relative grid size-[min(22rem,92vw)] place-items-center [--t:700ms] [--r:min(7rem,29vw)]">
      <div class="absolute inset-0 overflow-hidden rounded-full bg-[radial-gradient(circle_at_40%_32%,var(--color-tcm23-barrel-hi),var(--color-tcm23-barrel)_70%)] shadow-tcm23-barrel">
        <span aria-hidden="true" class="absolute inset-[3%] rounded-full bg-[repeating-conic-gradient(var(--color-tcm23-knurl)_0_2deg,transparent_2deg_4deg)] [mask-image:radial-gradient(circle,transparent_90%,black_91%)]"></span>
        <nav id="tcm-23-menu" aria-label="Portfolio" class="absolute inset-[7%] z-20 rounded-full bg-[radial-gradient(circle_at_45%_38%,var(--color-tcm23-deep-hi),var(--color-tcm23-deep)_75%)] [clip-path:circle(9%)] transition-[clip-path] duration-(--t) ease-[cubic-bezier(.4,0,.25,1)] group-data-open/lens:[clip-path:circle(50%)] motion-reduce:transition-none">
          <ul class="absolute inset-0">
          <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:0] [--a:calc(60deg*var(--i)-60deg)]">
            <a href="#tcm-23-portraits" data-item class="tcm23-polar pointer-events-auto min-w-[5rem] rounded-full bg-white/8 px-3.5 py-2.5 text-center text-[12.5px] font-semibold tracking-[0.04em] text-tcm23-gold-hi ring-1 ring-tcm23-gold/40 invisible scale-60 opacity-0 transition-[opacity,scale,visibility,background-color,color] duration-400 ease-[cubic-bezier(.34,1.45,.5,1)] group-data-open/lens:visible group-data-open/lens:scale-100 group-data-open/lens:opacity-100 group-data-open/lens:delay-[calc(var(--t)*0.55+var(--i)*40ms)] hover:bg-tcm23-gold hover:text-tcm23-on focus-visible:bg-tcm23-gold focus-visible:text-tcm23-on focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm23-gold motion-reduce:transition-none">Portraits</a>
          </li>
          <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:1] [--a:calc(60deg*var(--i)-60deg)]">
            <a href="#tcm-23-street" data-item class="tcm23-polar pointer-events-auto min-w-[5rem] rounded-full bg-white/8 px-3.5 py-2.5 text-center text-[12.5px] font-semibold tracking-[0.04em] text-tcm23-gold-hi ring-1 ring-tcm23-gold/40 invisible scale-60 opacity-0 transition-[opacity,scale,visibility,background-color,color] duration-400 ease-[cubic-bezier(.34,1.45,.5,1)] group-data-open/lens:visible group-data-open/lens:scale-100 group-data-open/lens:opacity-100 group-data-open/lens:delay-[calc(var(--t)*0.55+var(--i)*40ms)] hover:bg-tcm23-gold hover:text-tcm23-on focus-visible:bg-tcm23-gold focus-visible:text-tcm23-on focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm23-gold motion-reduce:transition-none">Street</a>
          </li>
          <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:2] [--a:calc(60deg*var(--i)-60deg)]">
            <a href="#tcm-23-nature" data-item class="tcm23-polar pointer-events-auto min-w-[5rem] rounded-full bg-white/8 px-3.5 py-2.5 text-center text-[12.5px] font-semibold tracking-[0.04em] text-tcm23-gold-hi ring-1 ring-tcm23-gold/40 invisible scale-60 opacity-0 transition-[opacity,scale,visibility,background-color,color] duration-400 ease-[cubic-bezier(.34,1.45,.5,1)] group-data-open/lens:visible group-data-open/lens:scale-100 group-data-open/lens:opacity-100 group-data-open/lens:delay-[calc(var(--t)*0.55+var(--i)*40ms)] hover:bg-tcm23-gold hover:text-tcm23-on focus-visible:bg-tcm23-gold focus-visible:text-tcm23-on focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm23-gold motion-reduce:transition-none">Nature</a>
          </li>
          <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:3] [--a:calc(60deg*var(--i)-60deg)]">
            <a href="#tcm-23-studio" data-item class="tcm23-polar pointer-events-auto min-w-[5rem] rounded-full bg-white/8 px-3.5 py-2.5 text-center text-[12.5px] font-semibold tracking-[0.04em] text-tcm23-gold-hi ring-1 ring-tcm23-gold/40 invisible scale-60 opacity-0 transition-[opacity,scale,visibility,background-color,color] duration-400 ease-[cubic-bezier(.34,1.45,.5,1)] group-data-open/lens:visible group-data-open/lens:scale-100 group-data-open/lens:opacity-100 group-data-open/lens:delay-[calc(var(--t)*0.55+var(--i)*40ms)] hover:bg-tcm23-gold hover:text-tcm23-on focus-visible:bg-tcm23-gold focus-visible:text-tcm23-on focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm23-gold motion-reduce:transition-none">Studio</a>
          </li>
          <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:4] [--a:calc(60deg*var(--i)-60deg)]">
            <a href="#tcm-23-film" data-item class="tcm23-polar pointer-events-auto min-w-[5rem] rounded-full bg-white/8 px-3.5 py-2.5 text-center text-[12.5px] font-semibold tracking-[0.04em] text-tcm23-gold-hi ring-1 ring-tcm23-gold/40 invisible scale-60 opacity-0 transition-[opacity,scale,visibility,background-color,color] duration-400 ease-[cubic-bezier(.34,1.45,.5,1)] group-data-open/lens:visible group-data-open/lens:scale-100 group-data-open/lens:opacity-100 group-data-open/lens:delay-[calc(var(--t)*0.55+var(--i)*40ms)] hover:bg-tcm23-gold hover:text-tcm23-on focus-visible:bg-tcm23-gold focus-visible:text-tcm23-on focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm23-gold motion-reduce:transition-none">Film</a>
          </li>
          <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:5] [--a:calc(60deg*var(--i)-60deg)]">
            <a href="#tcm-23-prints" data-item class="tcm23-polar pointer-events-auto min-w-[5rem] rounded-full bg-white/8 px-3.5 py-2.5 text-center text-[12.5px] font-semibold tracking-[0.04em] text-tcm23-gold-hi ring-1 ring-tcm23-gold/40 invisible scale-60 opacity-0 transition-[opacity,scale,visibility,background-color,color] duration-400 ease-[cubic-bezier(.34,1.45,.5,1)] group-data-open/lens:visible group-data-open/lens:scale-100 group-data-open/lens:opacity-100 group-data-open/lens:delay-[calc(var(--t)*0.55+var(--i)*40ms)] hover:bg-tcm23-gold hover:text-tcm23-on focus-visible:bg-tcm23-gold focus-visible:text-tcm23-on focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm23-gold motion-reduce:transition-none">Prints</a>
          </li>
          </ul>
          <span data-fstop aria-hidden="true" class="absolute top-1/2 left-1/2 -translate-1/2 font-tcm23-mono text-[13px] tracking-[0.14em] text-tcm23-gold">f/1.8</span>
        </nav>
        <div aria-hidden="true" class="absolute inset-[7%] z-10 overflow-hidden rounded-full">
        <span class="absolute inset-0 rotate-[calc(var(--i)*45deg)] [--i:0] transition-[rotate] duration-(--t) ease-[cubic-bezier(.4,0,.25,1)] group-data-open/lens:rotate-[calc(var(--i)*45deg+108deg)] motion-reduce:transition-none"><i class="absolute top-[-14%] left-1/2 h-[58%] w-[58%] origin-top-left rotate-24 rounded-[0_62%_42%_46%] bg-linear-to-br from-tcm23-blade-hi via-tcm23-blade to-tcm23-blade-lo shadow-tcm23-blade"></i></span>
        <span class="absolute inset-0 rotate-[calc(var(--i)*45deg)] [--i:1] transition-[rotate] duration-(--t) ease-[cubic-bezier(.4,0,.25,1)] group-data-open/lens:rotate-[calc(var(--i)*45deg+108deg)] motion-reduce:transition-none"><i class="absolute top-[-14%] left-1/2 h-[58%] w-[58%] origin-top-left rotate-24 rounded-[0_62%_42%_46%] bg-linear-to-br from-tcm23-blade-hi via-tcm23-blade to-tcm23-blade-lo shadow-tcm23-blade"></i></span>
        <span class="absolute inset-0 rotate-[calc(var(--i)*45deg)] [--i:2] transition-[rotate] duration-(--t) ease-[cubic-bezier(.4,0,.25,1)] group-data-open/lens:rotate-[calc(var(--i)*45deg+108deg)] motion-reduce:transition-none"><i class="absolute top-[-14%] left-1/2 h-[58%] w-[58%] origin-top-left rotate-24 rounded-[0_62%_42%_46%] bg-linear-to-br from-tcm23-blade-hi via-tcm23-blade to-tcm23-blade-lo shadow-tcm23-blade"></i></span>
        <span class="absolute inset-0 rotate-[calc(var(--i)*45deg)] [--i:3] transition-[rotate] duration-(--t) ease-[cubic-bezier(.4,0,.25,1)] group-data-open/lens:rotate-[calc(var(--i)*45deg+108deg)] motion-reduce:transition-none"><i class="absolute top-[-14%] left-1/2 h-[58%] w-[58%] origin-top-left rotate-24 rounded-[0_62%_42%_46%] bg-linear-to-br from-tcm23-blade-hi via-tcm23-blade to-tcm23-blade-lo shadow-tcm23-blade"></i></span>
        <span class="absolute inset-0 rotate-[calc(var(--i)*45deg)] [--i:4] transition-[rotate] duration-(--t) ease-[cubic-bezier(.4,0,.25,1)] group-data-open/lens:rotate-[calc(var(--i)*45deg+108deg)] motion-reduce:transition-none"><i class="absolute top-[-14%] left-1/2 h-[58%] w-[58%] origin-top-left rotate-24 rounded-[0_62%_42%_46%] bg-linear-to-br from-tcm23-blade-hi via-tcm23-blade to-tcm23-blade-lo shadow-tcm23-blade"></i></span>
        <span class="absolute inset-0 rotate-[calc(var(--i)*45deg)] [--i:5] transition-[rotate] duration-(--t) ease-[cubic-bezier(.4,0,.25,1)] group-data-open/lens:rotate-[calc(var(--i)*45deg+108deg)] motion-reduce:transition-none"><i class="absolute top-[-14%] left-1/2 h-[58%] w-[58%] origin-top-left rotate-24 rounded-[0_62%_42%_46%] bg-linear-to-br from-tcm23-blade-hi via-tcm23-blade to-tcm23-blade-lo shadow-tcm23-blade"></i></span>
        <span class="absolute inset-0 rotate-[calc(var(--i)*45deg)] [--i:6] transition-[rotate] duration-(--t) ease-[cubic-bezier(.4,0,.25,1)] group-data-open/lens:rotate-[calc(var(--i)*45deg+108deg)] motion-reduce:transition-none"><i class="absolute top-[-14%] left-1/2 h-[58%] w-[58%] origin-top-left rotate-24 rounded-[0_62%_42%_46%] bg-linear-to-br from-tcm23-blade-hi via-tcm23-blade to-tcm23-blade-lo shadow-tcm23-blade"></i></span>
        <span class="absolute inset-0 rotate-[calc(var(--i)*45deg)] [--i:7] transition-[rotate] duration-(--t) ease-[cubic-bezier(.4,0,.25,1)] group-data-open/lens:rotate-[calc(var(--i)*45deg+108deg)] motion-reduce:transition-none"><i class="absolute top-[-14%] left-1/2 h-[58%] w-[58%] origin-top-left rotate-24 rounded-[0_62%_42%_46%] bg-linear-to-br from-tcm23-blade-hi via-tcm23-blade to-tcm23-blade-lo shadow-tcm23-blade"></i></span>
        </div>
      </div>
      <button type="button" data-toggle aria-expanded="false" aria-controls="tcm-23-menu" class="absolute -bottom-6 left-1/2 z-30 grid size-20 -translate-x-1/2 cursor-pointer place-content-center rounded-full bg-[radial-gradient(circle_at_38%_30%,var(--color-tcm23-btn-hi),var(--color-tcm23-btn))] text-[11.5px] leading-tight font-bold tracking-[0.12em] text-tcm23-gold-hi uppercase shadow-tcm23-btn ring-2 ring-tcm23-gold/50 transition-[box-shadow] duration-300 hover:ring-tcm23-gold focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tcm23-gold"><span class="group-data-open/lens:hidden">Open<br>lens</span><span class="hidden group-data-open/lens:inline">Close<br>lens</span></button>
    </div>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm23-card px-3.5 py-2 text-center font-tcm23-mono text-[11.5px] text-tcm23-mut ring-1 ring-tcm23-line mt-6">[clip-path:circle(9%)] → group-data-open/lens:[clip-path:circle(50%)] · 8 blades +108°</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm23-bg: #eeece8;
  --color-tcm23-bg: oklch(0.944 0.006 84.6);
  --color-tcm23-glow: #fde68a73;
  --color-tcm23-glow: oklch(0.924 0.115 95.7 / 0.45);
  --color-tcm23-barrel: #1d1e22;
  --color-tcm23-barrel: oklch(0.236 0.008 274.6);
  --color-tcm23-barrel-hi: #3a3b41;
  --color-tcm23-barrel-hi: oklch(0.354 0.01 278.3);
  --color-tcm23-knurl: #00000066;
  --color-tcm23-knurl: oklch(0 0 0 / 0.4);
  --color-tcm23-deep: #141218;
  --color-tcm23-deep: oklch(0.187 0.012 300.4);
  --color-tcm23-deep-hi: #2b2633;
  --color-tcm23-deep-hi: oklch(0.28 0.025 302.4);
  --color-tcm23-blade: #26272c;
  --color-tcm23-blade: oklch(0.274 0.009 276.8);
  --color-tcm23-blade-hi: #43444b;
  --color-tcm23-blade-hi: oklch(0.388 0.012 279.4);
  --color-tcm23-blade-lo: #18191c;
  --color-tcm23-blade-lo: oklch(0.214 0.006 271.1);
  --color-tcm23-btn: #1d1e22;
  --color-tcm23-btn: oklch(0.236 0.008 274.6);
  --color-tcm23-btn-hi: #45464d;
  --color-tcm23-btn-hi: oklch(0.396 0.012 279.4);
  --color-tcm23-gold: #d4a24c;
  --color-tcm23-gold: oklch(0.743 0.119 78.7);
  --color-tcm23-gold-hi: #f3d9a4;
  --color-tcm23-gold-hi: oklch(0.894 0.074 84.8);
  --color-tcm23-gold-ink: #8a6216;
  --color-tcm23-gold-ink: oklch(0.525 0.101 78.1);
  --color-tcm23-on: #1d1405;
  --color-tcm23-on: oklch(0.198 0.031 79.8);
  --color-tcm23-ink: #1c1b1a;
  --color-tcm23-ink: oklch(0.223 0.002 67.7);
  --color-tcm23-mut: #5f5b55;
  --color-tcm23-mut: oklch(0.473 0.011 78.2);
  --color-tcm23-card: #faf9f6;
  --color-tcm23-card: oklch(0.982 0.004 91.4);
  --color-tcm23-line: #dcd8d0;
  --color-tcm23-line: oklch(0.883 0.012 84.6);
  --font-tcm23-sans: 'Manrope', system-ui, sans-serif;
  --font-tcm23-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm23-barrel: 0 0 0 8px oklch(0.28 0.005 260), 0 0 0 10px oklch(0.6 0.09 80 / 0.55), 0 40px 80px -36px oklch(0 0 0 / 0.8), inset 0 0 40px oklch(0 0 0 / 0.6);
  --shadow-tcm23-blade: inset 1px -1px 0 oklch(0.6 0.03 80 / 0.35), 0 4px 10px oklch(0 0 0 / 0.5);
  --shadow-tcm23-btn: 0 14px 30px -10px oklch(0 0 0 / 0.8), inset 0 1px 0 oklch(1 0 0 / 0.15);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-23 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm23-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: darkroom: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-23:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm23-bg: #0b0b0d;
    --color-tcm23-bg: oklch(0.151 0.004 285.9);
    --color-tcm23-glow: #78350f40;
    --color-tcm23-glow: oklch(0.414 0.105 45.9 / 0.25);
    --color-tcm23-barrel: #18191c;
    --color-tcm23-barrel: oklch(0.214 0.006 271.1);
    --color-tcm23-barrel-hi: #34353b;
    --color-tcm23-barrel-hi: oklch(0.33 0.011 278.3);
    --color-tcm23-knurl: #00000080;
    --color-tcm23-knurl: oklch(0 0 0 / 0.5);
    --color-tcm23-deep: #100e14;
    --color-tcm23-deep: oklch(0.169 0.013 300.3);
    --color-tcm23-deep-hi: #2a2433;
    --color-tcm23-deep-hi: oklch(0.274 0.028 302.8);
    --color-tcm23-blade: #232428;
    --color-tcm23-blade: oklch(0.261 0.008 274.7);
    --color-tcm23-blade-hi: #3d3e45;
    --color-tcm23-blade-hi: oklch(0.366 0.012 279.3);
    --color-tcm23-blade-lo: #141518;
    --color-tcm23-blade-lo: oklch(0.196 0.006 271.1);
    --color-tcm23-btn: #18191c;
    --color-tcm23-btn: oklch(0.214 0.006 271.1);
    --color-tcm23-btn-hi: #3e3f46;
    --color-tcm23-btn-hi: oklch(0.369 0.012 279.3);
    --color-tcm23-gold: #e2b45e;
    --color-tcm23-gold: oklch(0.794 0.117 81.4);
    --color-tcm23-gold-hi: #f6e0b0;
    --color-tcm23-gold-hi: oklch(0.913 0.067 86.2);
    --color-tcm23-gold-ink: #e9c27a;
    --color-tcm23-gold-ink: oklch(0.833 0.101 81.9);
    --color-tcm23-on: #1d1405;
    --color-tcm23-on: oklch(0.198 0.031 79.8);
    --color-tcm23-ink: #f2efe9;
    --color-tcm23-ink: oklch(0.953 0.009 84.6);
    --color-tcm23-mut: #a8a29a;
    --color-tcm23-mut: oklch(0.715 0.013 75.3);
    --color-tcm23-card: #161618;
    --color-tcm23-card: oklch(0.201 0.004 286);
    --color-tcm23-line: #2c2b2e;
    --color-tcm23-line: oklch(0.291 0.006 301.2);
  }
}

.tcm-23[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm23-bg: #0b0b0d;
  --color-tcm23-bg: oklch(0.151 0.004 285.9);
  --color-tcm23-glow: #78350f40;
  --color-tcm23-glow: oklch(0.414 0.105 45.9 / 0.25);
  --color-tcm23-barrel: #18191c;
  --color-tcm23-barrel: oklch(0.214 0.006 271.1);
  --color-tcm23-barrel-hi: #34353b;
  --color-tcm23-barrel-hi: oklch(0.33 0.011 278.3);
  --color-tcm23-knurl: #00000080;
  --color-tcm23-knurl: oklch(0 0 0 / 0.5);
  --color-tcm23-deep: #100e14;
  --color-tcm23-deep: oklch(0.169 0.013 300.3);
  --color-tcm23-deep-hi: #2a2433;
  --color-tcm23-deep-hi: oklch(0.274 0.028 302.8);
  --color-tcm23-blade: #232428;
  --color-tcm23-blade: oklch(0.261 0.008 274.7);
  --color-tcm23-blade-hi: #3d3e45;
  --color-tcm23-blade-hi: oklch(0.366 0.012 279.3);
  --color-tcm23-blade-lo: #141518;
  --color-tcm23-blade-lo: oklch(0.196 0.006 271.1);
  --color-tcm23-btn: #18191c;
  --color-tcm23-btn: oklch(0.214 0.006 271.1);
  --color-tcm23-btn-hi: #3e3f46;
  --color-tcm23-btn-hi: oklch(0.369 0.012 279.3);
  --color-tcm23-gold: #e2b45e;
  --color-tcm23-gold: oklch(0.794 0.117 81.4);
  --color-tcm23-gold-hi: #f6e0b0;
  --color-tcm23-gold-hi: oklch(0.913 0.067 86.2);
  --color-tcm23-gold-ink: #e9c27a;
  --color-tcm23-gold-ink: oklch(0.833 0.101 81.9);
  --color-tcm23-on: #1d1405;
  --color-tcm23-on: oklch(0.198 0.031 79.8);
  --color-tcm23-ink: #f2efe9;
  --color-tcm23-ink: oklch(0.953 0.009 84.6);
  --color-tcm23-mut: #a8a29a;
  --color-tcm23-mut: oklch(0.715 0.013 75.3);
  --color-tcm23-card: #161618;
  --color-tcm23-card: oklch(0.201 0.004 286);
  --color-tcm23-line: #2c2b2e;
  --color-tcm23-line: oklch(0.291 0.006 301.2);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-23-lens');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const btn = root.querySelector('[data-toggle]');
  const items = [...root.querySelectorAll('[data-item]')];
  const set = (open, focus) => {
    root.toggleAttribute('data-open', open);
    btn.setAttribute('aria-expanded', String(open));
    const f = root.querySelector('[data-fstop]'), stops = ['f/1.8', 'f/2.8', 'f/4', 'f/5.6', 'f/8'];
    clearInterval(root._t); let k = open ? 0 : stops.length - 1;
    root._t = setInterval(() => { f.textContent = stops[k]; k += open ? 1 : -1; if (k < 0 || k >= stops.length) clearInterval(root._t); }, 120);
    if (open && focus && items[0]) setTimeout(() => items[0].focus(), 220);
  };
  btn.addEventListener('click', (e) => set(!root.hasAttribute('data-open'), e.detail === 0));
  root.querySelectorAll('[data-close]').forEach((el) => el.addEventListener('click', () => set(false)));
  root.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && root.hasAttribute('data-open')) { set(false); btn.focus(); return; }
    const k = items.indexOf(document.activeElement);
    const d = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
    if (k < 0 || !d) return;
    e.preventDefault();
    items[(k + d + items.length) % items.length].focus();
  });
  document.addEventListener('pointerdown', (e) => { if (!root.contains(e.target)) set(false); });
})();
```
