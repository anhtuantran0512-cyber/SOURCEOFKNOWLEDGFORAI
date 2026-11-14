---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-spiral-vortex-menu-animation-with-particles/"
title: "Tailwind CSS Spiral Vortex Menu Animation with Particles"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A game launcher where menu items arrive on a spiral: each arm rotates in from &minus;220&deg; while its rider slides out along the arm, and two independently…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Spiral Vortex Menu Animation with Particles
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-spiral-vortex-menu-animation-with-particles/

A game launcher where menu items arrive on a spiral: each arm rotates in from &minus;220&deg; while its rider slides out along the arm, and two independently eased motions compose into a decaying orbit. A swirl of 22 particles drifts behind a glowing core. Exits are fast (350ms) so closing never feels laggy, and the whole field disappears for reduced-motion users.
## HTML
```html
<section class="tcm-24 relative w-full min-h-svh grid place-items-center overflow-hidden bg-tcm24-bg bg-[radial-gradient(50%_45%_at_50%_50%,var(--color-tcm24-glow),transparent_72%)] px-4 py-14 font-tcm24-sans text-tcm24-ink antialiased" aria-label="Spiral vortex menu demo">
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 motion-reduce:hidden">
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-a opacity-60 animate-tcm24-orbit" style="--s:4.0px;--r:167px;--a0:42deg;animation-duration:14.4s;animation-delay:-8.9s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-b opacity-60 animate-tcm24-orbit" style="--s:4.0px;--r:75px;--a0:316deg;animation-duration:22.0s;animation-delay:-8.2s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-c opacity-60 animate-tcm24-orbit" style="--s:3.1px;--r:208px;--a0:237deg;animation-duration:10.7s;animation-delay:-10.0s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-d opacity-60 animate-tcm24-orbit" style="--s:2.9px;--r:188px;--a0:57deg;animation-duration:21.3s;animation-delay:-9.7s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-a opacity-60 animate-tcm24-orbit" style="--s:2.7px;--r:70px;--a0:338deg;animation-duration:30.3s;animation-delay:-2.4s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-b opacity-60 animate-tcm24-orbit" style="--s:3.8px;--r:242px;--a0:68deg;animation-duration:18.2s;animation-delay:-11.0s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-c opacity-60 animate-tcm24-orbit" style="--s:4.7px;--r:113px;--a0:61deg;animation-duration:30.7s;animation-delay:-8.9s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-d opacity-60 animate-tcm24-orbit" style="--s:2.9px;--r:164px;--a0:119deg;animation-duration:12.4s;animation-delay:-15.5s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-a opacity-60 animate-tcm24-orbit" style="--s:3.4px;--r:127px;--a0:29deg;animation-duration:29.4s;animation-delay:-4.8s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-b opacity-60 animate-tcm24-orbit" style="--s:5.5px;--r:149px;--a0:85deg;animation-duration:22.3s;animation-delay:-8.0s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-c opacity-60 animate-tcm24-orbit" style="--s:5.0px;--r:184px;--a0:49deg;animation-duration:13.9s;animation-delay:-9.0s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-d opacity-60 animate-tcm24-orbit" style="--s:2.4px;--r:69px;--a0:148deg;animation-duration:24.0s;animation-delay:-12.9s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-a opacity-60 animate-tcm24-orbit" style="--s:5.8px;--r:122px;--a0:158deg;animation-duration:19.9s;animation-delay:-8.8s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-b opacity-60 animate-tcm24-orbit" style="--s:5.4px;--r:146px;--a0:158deg;animation-duration:14.8s;animation-delay:-4.7s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-c opacity-60 animate-tcm24-orbit" style="--s:5.0px;--r:85px;--a0:97deg;animation-duration:25.9s;animation-delay:-17.2s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-d opacity-60 animate-tcm24-orbit" style="--s:5.9px;--r:236px;--a0:310deg;animation-duration:25.4s;animation-delay:-12.8s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-a opacity-60 animate-tcm24-orbit" style="--s:4.2px;--r:65px;--a0:117deg;animation-duration:16.9s;animation-delay:-4.3s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-b opacity-60 animate-tcm24-orbit" style="--s:3.6px;--r:190px;--a0:265deg;animation-duration:14.9s;animation-delay:-19.1s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-c opacity-60 animate-tcm24-orbit" style="--s:2.0px;--r:128px;--a0:211deg;animation-duration:18.7s;animation-delay:-1.8s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-d opacity-60 animate-tcm24-orbit" style="--s:6.0px;--r:147px;--a0:314deg;animation-duration:21.9s;animation-delay:-9.4s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-a opacity-60 animate-tcm24-orbit" style="--s:2.5px;--r:211px;--a0:323deg;animation-duration:14.8s;animation-delay:-0.5s;width:var(--s);height:var(--s)"></span>
      <span class="absolute top-1/2 left-1/2 rounded-full bg-tcm24-b opacity-60 animate-tcm24-orbit" style="--s:2.6px;--r:194px;--a0:251deg;animation-duration:23.5s;animation-delay:-17.4s;width:var(--s);height:var(--s)"></span>
  </div>
  <div class="relative grid w-full justify-items-center gap-8">
    <header class="grid justify-items-center gap-2 text-center">
      <p class="font-tcm24-mono text-[11px] tracking-[0.24em] text-tcm24-mut uppercase">Driftborne · Season 3</p>
      <h2 class="font-tcm24-display text-[clamp(1.8rem,6vw,2.8rem)] leading-none font-bold tracking-[-0.03em] uppercase">Into the <span class="bg-linear-to-r from-tcm24-a via-tcm24-b to-tcm24-c bg-clip-text text-transparent">vortex</span></h2>
    </header>
    <nav id="tcm-24-vx" class="group/vx relative grid size-[min(22rem,92vw)] place-items-center [--r:min(9.8rem,40vw)]" aria-label="Game menu">
      <span aria-hidden="true" class="absolute inset-[18%] rounded-full bg-[conic-gradient(from_0deg,var(--color-tcm24-a),transparent_30%,var(--color-tcm24-b)_50%,transparent_80%,var(--color-tcm24-a))] opacity-30 blur-xl animate-tcm24-spin motion-reduce:animate-none"></span>
      <ul id="tcm-24-menu" class="absolute inset-0">
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:0] [--slot:calc(360deg/5*var(--i)-90deg)] rotate-[calc(var(--slot)-220deg)] transition-[rotate] duration-350 delay-0 group-data-open/vx:rotate-(--slot) group-data-open/vx:duration-900 group-data-open/vx:delay-[calc(var(--i)*55ms)] group-data-open/vx:ease-[cubic-bezier(.3,1.15,.35,1)] motion-reduce:transition-none">
          <a href="#tcm-24-worlds" data-item class="pointer-events-auto absolute min-w-[5rem] rounded-full bg-white/8 px-4 py-3 text-center text-[13px] font-bold tracking-[0.06em] text-white ring-1 ring-tcm24-a/50 backdrop-blur-sm translate-x-0 rotate-[calc(220deg-var(--slot))] opacity-0 invisible transition-[translate,rotate,opacity,visibility,background-color] duration-350 group-data-open/vx:translate-x-(--r) group-data-open/vx:rotate-[calc(0deg-var(--slot))] group-data-open/vx:opacity-100 group-data-open/vx:visible group-data-open/vx:duration-900 group-data-open/vx:delay-[calc(var(--i)*55ms)] group-data-open/vx:ease-[cubic-bezier(.25,.9,.3,1)] hover:bg-linear-to-br hover:from-tcm24-a hover:to-tcm24-b focus-visible:bg-linear-to-br focus-visible:from-tcm24-a focus-visible:to-tcm24-b focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none">Worlds</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:1] [--slot:calc(360deg/5*var(--i)-90deg)] rotate-[calc(var(--slot)-220deg)] transition-[rotate] duration-350 delay-0 group-data-open/vx:rotate-(--slot) group-data-open/vx:duration-900 group-data-open/vx:delay-[calc(var(--i)*55ms)] group-data-open/vx:ease-[cubic-bezier(.3,1.15,.35,1)] motion-reduce:transition-none">
          <a href="#tcm-24-fleet" data-item class="pointer-events-auto absolute min-w-[5rem] rounded-full bg-white/8 px-4 py-3 text-center text-[13px] font-bold tracking-[0.06em] text-white ring-1 ring-tcm24-a/50 backdrop-blur-sm translate-x-0 rotate-[calc(220deg-var(--slot))] opacity-0 invisible transition-[translate,rotate,opacity,visibility,background-color] duration-350 group-data-open/vx:translate-x-(--r) group-data-open/vx:rotate-[calc(0deg-var(--slot))] group-data-open/vx:opacity-100 group-data-open/vx:visible group-data-open/vx:duration-900 group-data-open/vx:delay-[calc(var(--i)*55ms)] group-data-open/vx:ease-[cubic-bezier(.25,.9,.3,1)] hover:bg-linear-to-br hover:from-tcm24-a hover:to-tcm24-b focus-visible:bg-linear-to-br focus-visible:from-tcm24-a focus-visible:to-tcm24-b focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none">Fleet</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:2] [--slot:calc(360deg/5*var(--i)-90deg)] rotate-[calc(var(--slot)-220deg)] transition-[rotate] duration-350 delay-0 group-data-open/vx:rotate-(--slot) group-data-open/vx:duration-900 group-data-open/vx:delay-[calc(var(--i)*55ms)] group-data-open/vx:ease-[cubic-bezier(.3,1.15,.35,1)] motion-reduce:transition-none">
          <a href="#tcm-24-crew" data-item class="pointer-events-auto absolute min-w-[5rem] rounded-full bg-white/8 px-4 py-3 text-center text-[13px] font-bold tracking-[0.06em] text-white ring-1 ring-tcm24-a/50 backdrop-blur-sm translate-x-0 rotate-[calc(220deg-var(--slot))] opacity-0 invisible transition-[translate,rotate,opacity,visibility,background-color] duration-350 group-data-open/vx:translate-x-(--r) group-data-open/vx:rotate-[calc(0deg-var(--slot))] group-data-open/vx:opacity-100 group-data-open/vx:visible group-data-open/vx:duration-900 group-data-open/vx:delay-[calc(var(--i)*55ms)] group-data-open/vx:ease-[cubic-bezier(.25,.9,.3,1)] hover:bg-linear-to-br hover:from-tcm24-a hover:to-tcm24-b focus-visible:bg-linear-to-br focus-visible:from-tcm24-a focus-visible:to-tcm24-b focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none">Crew</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:3] [--slot:calc(360deg/5*var(--i)-90deg)] rotate-[calc(var(--slot)-220deg)] transition-[rotate] duration-350 delay-0 group-data-open/vx:rotate-(--slot) group-data-open/vx:duration-900 group-data-open/vx:delay-[calc(var(--i)*55ms)] group-data-open/vx:ease-[cubic-bezier(.3,1.15,.35,1)] motion-reduce:transition-none">
          <a href="#tcm-24-codex" data-item class="pointer-events-auto absolute min-w-[5rem] rounded-full bg-white/8 px-4 py-3 text-center text-[13px] font-bold tracking-[0.06em] text-white ring-1 ring-tcm24-a/50 backdrop-blur-sm translate-x-0 rotate-[calc(220deg-var(--slot))] opacity-0 invisible transition-[translate,rotate,opacity,visibility,background-color] duration-350 group-data-open/vx:translate-x-(--r) group-data-open/vx:rotate-[calc(0deg-var(--slot))] group-data-open/vx:opacity-100 group-data-open/vx:visible group-data-open/vx:duration-900 group-data-open/vx:delay-[calc(var(--i)*55ms)] group-data-open/vx:ease-[cubic-bezier(.25,.9,.3,1)] hover:bg-linear-to-br hover:from-tcm24-a hover:to-tcm24-b focus-visible:bg-linear-to-br focus-visible:from-tcm24-a focus-visible:to-tcm24-b focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none">Codex</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:4] [--slot:calc(360deg/5*var(--i)-90deg)] rotate-[calc(var(--slot)-220deg)] transition-[rotate] duration-350 delay-0 group-data-open/vx:rotate-(--slot) group-data-open/vx:duration-900 group-data-open/vx:delay-[calc(var(--i)*55ms)] group-data-open/vx:ease-[cubic-bezier(.3,1.15,.35,1)] motion-reduce:transition-none">
          <a href="#tcm-24-signal" data-item class="pointer-events-auto absolute min-w-[5rem] rounded-full bg-white/8 px-4 py-3 text-center text-[13px] font-bold tracking-[0.06em] text-white ring-1 ring-tcm24-a/50 backdrop-blur-sm translate-x-0 rotate-[calc(220deg-var(--slot))] opacity-0 invisible transition-[translate,rotate,opacity,visibility,background-color] duration-350 group-data-open/vx:translate-x-(--r) group-data-open/vx:rotate-[calc(0deg-var(--slot))] group-data-open/vx:opacity-100 group-data-open/vx:visible group-data-open/vx:duration-900 group-data-open/vx:delay-[calc(var(--i)*55ms)] group-data-open/vx:ease-[cubic-bezier(.25,.9,.3,1)] hover:bg-linear-to-br hover:from-tcm24-a hover:to-tcm24-b focus-visible:bg-linear-to-br focus-visible:from-tcm24-a focus-visible:to-tcm24-b focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none">Signal</a>
        </li>
      </ul>
      <button type="button" data-toggle aria-expanded="false" aria-controls="tcm-24-menu" class="relative z-10 grid size-28 cursor-pointer place-items-center rounded-full bg-[radial-gradient(circle_at_40%_32%,var(--color-tcm24-core-hi),var(--color-tcm24-core)_70%)] text-white shadow-tcm24-core transition-[scale] duration-300 hover:scale-105 focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-tcm24-a">
        <span aria-hidden="true" class="absolute -inset-2.5 rounded-full border border-dashed border-tcm24-a/60 animate-tcm24-spin [animation-duration:14s] motion-reduce:animate-none"></span>
        <b class="font-tcm24-display text-[14px] tracking-[0.18em] uppercase"><span class="group-data-open/vx:hidden">Enter</span><span class="hidden group-data-open/vx:inline">Close</span></b>
      </button>
    </nav>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm24-card px-3.5 py-2 text-center font-tcm24-mono text-[11.5px] text-tcm24-mut ring-1 ring-tcm24-line ">arm rotate-(--slot) × rider translate-x-(--r) = spiral · particles on @keyframes</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm24-bg: #2a1650;
  --color-tcm24-bg: oklch(0.265 0.101 294.4);
  --color-tcm24-glow: #a855f773;
  --color-tcm24-glow: oklch(0.627 0.233 303.9 / 0.45);
  --color-tcm24-a: #c084fc;
  --color-tcm24-a: oklch(0.722 0.177 305.5);
  --color-tcm24-b: #f472b6;
  --color-tcm24-b: oklch(0.725 0.175 349.8);
  --color-tcm24-c: #67e8f9;
  --color-tcm24-c: oklch(0.865 0.115 207.1);
  --color-tcm24-d: #fbbf24;
  --color-tcm24-d: oklch(0.837 0.164 84.4);
  --color-tcm24-core: #5b21b6;
  --color-tcm24-core: oklch(0.432 0.211 292.8);
  --color-tcm24-core-hi: #a855f7;
  --color-tcm24-core-hi: oklch(0.627 0.233 303.9);
  --color-tcm24-ink: #ffffff;
  --color-tcm24-ink: oklch(1 0 0);
  --color-tcm24-mut: #e9d5ffcc;
  --color-tcm24-mut: oklch(0.902 0.06 306.7 / 0.8);
  --color-tcm24-card: #ffffff14;
  --color-tcm24-card: oklch(1 0 0 / 0.08);
  --color-tcm24-line: #ffffff33;
  --color-tcm24-line: oklch(1 0 0 / 0.2);
  --font-tcm24-sans: 'Inter', system-ui, sans-serif;
  --font-tcm24-display: 'Unbounded', system-ui, sans-serif;
  --font-tcm24-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm24-core: 0 0 70px -6px oklch(0.65 0.25 305 / 0.75), inset 0 1px 0 oklch(1 0 0 / 0.3);
  --animate-tcm24-spin: tcm24-spin 6s linear infinite;
  --animate-tcm24-orbit: tcm24-orbit 20s linear infinite;

  @keyframes tcm24-spin {
    to {
      rotate: 360deg;
    }
  }

  @keyframes tcm24-orbit {
    from {
      transform: rotate(var(--a0)) translateX(var(--r));
    }

    to {
      transform: rotate(calc(var(--a0) + 360deg)) translateX(var(--r));
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-24 {
  width: 100%;
  min-height: 100svh;
}
/* Dark theme: deep nebula (light mode is a lighter violet dusk): the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-24:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm24-bg: #0c0718;
    --color-tcm24-bg: oklch(0.147 0.037 295.7);
    --color-tcm24-glow: #6d28d966;
    --color-tcm24-glow: oklch(0.491 0.241 292.6 / 0.4);
    --color-tcm24-a: #c084fc;
    --color-tcm24-a: oklch(0.722 0.177 305.5);
    --color-tcm24-b: #f472b6;
    --color-tcm24-b: oklch(0.725 0.175 349.8);
    --color-tcm24-c: #67e8f9;
    --color-tcm24-c: oklch(0.865 0.115 207.1);
    --color-tcm24-d: #fbbf24;
    --color-tcm24-d: oklch(0.837 0.164 84.4);
    --color-tcm24-core: #3b0f7a;
    --color-tcm24-core: oklch(0.319 0.16 293.3);
    --color-tcm24-core-hi: #7e22ce;
    --color-tcm24-core-hi: oklch(0.496 0.237 301.9);
    --color-tcm24-ink: #ffffff;
    --color-tcm24-ink: oklch(1 0 0);
    --color-tcm24-mut: #d8c7f2cc;
    --color-tcm24-mut: oklch(0.857 0.061 303.1 / 0.8);
    --color-tcm24-card: #ffffff12;
    --color-tcm24-card: oklch(1 0 0 / 0.07);
    --color-tcm24-line: #ffffff2e;
    --color-tcm24-line: oklch(1 0 0 / 0.18);
  }
}

.tcm-24[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm24-bg: #0c0718;
  --color-tcm24-bg: oklch(0.147 0.037 295.7);
  --color-tcm24-glow: #6d28d966;
  --color-tcm24-glow: oklch(0.491 0.241 292.6 / 0.4);
  --color-tcm24-a: #c084fc;
  --color-tcm24-a: oklch(0.722 0.177 305.5);
  --color-tcm24-b: #f472b6;
  --color-tcm24-b: oklch(0.725 0.175 349.8);
  --color-tcm24-c: #67e8f9;
  --color-tcm24-c: oklch(0.865 0.115 207.1);
  --color-tcm24-d: #fbbf24;
  --color-tcm24-d: oklch(0.837 0.164 84.4);
  --color-tcm24-core: #3b0f7a;
  --color-tcm24-core: oklch(0.319 0.16 293.3);
  --color-tcm24-core-hi: #7e22ce;
  --color-tcm24-core-hi: oklch(0.496 0.237 301.9);
  --color-tcm24-ink: #ffffff;
  --color-tcm24-ink: oklch(1 0 0);
  --color-tcm24-mut: #d8c7f2cc;
  --color-tcm24-mut: oklch(0.857 0.061 303.1 / 0.8);
  --color-tcm24-card: #ffffff12;
  --color-tcm24-card: oklch(1 0 0 / 0.07);
  --color-tcm24-line: #ffffff2e;
  --color-tcm24-line: oklch(1 0 0 / 0.18);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-24-vx');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const btn = root.querySelector('[data-toggle]');
  const items = [...root.querySelectorAll('[data-item]')];
  const set = (open, focus) => {
    root.toggleAttribute('data-open', open);
    btn.setAttribute('aria-expanded', String(open));
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
