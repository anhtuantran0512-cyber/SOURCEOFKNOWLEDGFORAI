---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-nested-radial-submenu-solar-system-navigation/"
title: "Tailwind CSS Nested Radial Submenu (Solar System Navigation)"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A two-level radial menu for developer docs: three planets orbit a glowing sun, and opening one spawns its own ring of moons around it &mdash; the same…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Nested Radial Submenu (Solar System Navigation)
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-nested-radial-submenu-solar-system-navigation/

A two-level radial menu for developer docs: three planets orbit a glowing sun, and opening one spawns its own ring of moons around it &mdash; the same tcm18-polar utility, nested. The open planet grows while its siblings dim and shrink (group-data-open/planet: and group-data-muted/planet:), focus moves into the moons, and Escape returns it to the planet.
## HTML
```html
<section class="tcm-18 w-full min-h-svh grid place-items-center overflow-hidden bg-tcm18-bg bg-[radial-gradient(50%_45%_at_50%_50%,var(--color-tcm18-glow),transparent_72%)] px-4 py-14 font-tcm18-sans text-tcm18-ink antialiased" aria-label="Nested radial submenu demo">
  <div class="grid w-full justify-items-center gap-6">
    <header class="grid justify-items-center gap-1.5 text-center">
      <p class="font-tcm18-mono text-[11px] tracking-[0.16em] text-tcm18-acc-ink uppercase">Developer docs</p>
      <h2 class="text-[clamp(1.5rem,4vw,2rem)] font-semibold tracking-[-0.03em]">Pick a planet, then a moon</h2>
    </header>
    <nav id="tcm-18-space" class="relative my-12 grid size-[min(25rem,96vw)] place-items-center [--pr:min(8.6rem,34vw)]" aria-label="Documentation">
      <span aria-hidden="true" class="absolute inset-[calc(50%-var(--pr))] rounded-full border border-dashed border-tcm18-line"></span>
      <span aria-hidden="true" class="absolute inset-[calc(50%-var(--pr)-2.5rem)] rounded-full border border-tcm18-line/50"></span>
      <div aria-hidden="true" class="grid size-24 place-items-center rounded-full bg-[radial-gradient(circle_at_35%_30%,#fff1c1,#fbbf24_55%,#ea580c)] text-[17px] font-extrabold text-amber-950 shadow-tcm18-sun">Docs</div>
      <ul class="absolute inset-0">
        <li data-planet class="group/planet absolute inset-0 grid place-items-center pointer-events-none [--i:0] [--a:calc(360deg/3*var(--i)-90deg)] [--r:var(--pr)]">
          <div class="tcm18-polar relative grid place-items-center">
            <button type="button" aria-expanded="false" aria-controls="tcm-18-moons-0" class="pointer-events-auto relative z-10 grid size-18 cursor-pointer place-items-center rounded-full bg-linear-to-br from-sky-400 to-blue-600 text-[13.5px] font-bold text-white shadow-tcm18-planet ring-1 ring-white/30 transition-[scale,opacity] duration-400 ease-[cubic-bezier(.34,1.45,.5,1)] hover:scale-110 group-data-open/planet:scale-125 group-data-muted/planet:scale-85 group-data-muted/planet:opacity-40 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tcm18-ring motion-reduce:transition-none">Guides</button>
            <ul id="tcm-18-moons-0" class="absolute inset-0">
              <li class="tcm18-polar absolute top-1/2 left-1/2 [--j:0] [--a:calc(360deg/3*var(--j)-90deg)] [--r:0rem] transition-[translate] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:[--r:5.6rem] group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] motion-reduce:transition-none">
                <a href="#tcm-18-quickstart" data-moon class="absolute top-0 left-0 grid h-10 -translate-1/2 place-items-center rounded-full bg-tcm18-moon px-3.5 text-[12px] font-semibold whitespace-nowrap text-tcm18-moon-ink shadow-tcm18-moon ring-1 ring-tcm18-line pointer-events-auto invisible scale-30 opacity-0 transition-[scale,opacity,visibility,background-color] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:visible group-data-open/planet:scale-100 group-data-open/planet:opacity-100 group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] hover:bg-tcm18-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm18-ring motion-reduce:transition-none">Quickstart</a>
              </li>
              <li class="tcm18-polar absolute top-1/2 left-1/2 [--j:1] [--a:calc(360deg/3*var(--j)-90deg)] [--r:0rem] transition-[translate] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:[--r:5.6rem] group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] motion-reduce:transition-none">
                <a href="#tcm-18-tutorials" data-moon class="absolute top-0 left-0 grid h-10 -translate-1/2 place-items-center rounded-full bg-tcm18-moon px-3.5 text-[12px] font-semibold whitespace-nowrap text-tcm18-moon-ink shadow-tcm18-moon ring-1 ring-tcm18-line pointer-events-auto invisible scale-30 opacity-0 transition-[scale,opacity,visibility,background-color] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:visible group-data-open/planet:scale-100 group-data-open/planet:opacity-100 group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] hover:bg-tcm18-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm18-ring motion-reduce:transition-none">Tutorials</a>
              </li>
              <li class="tcm18-polar absolute top-1/2 left-1/2 [--j:2] [--a:calc(360deg/3*var(--j)-90deg)] [--r:0rem] transition-[translate] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:[--r:5.6rem] group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] motion-reduce:transition-none">
                <a href="#tcm-18-recipes" data-moon class="absolute top-0 left-0 grid h-10 -translate-1/2 place-items-center rounded-full bg-tcm18-moon px-3.5 text-[12px] font-semibold whitespace-nowrap text-tcm18-moon-ink shadow-tcm18-moon ring-1 ring-tcm18-line pointer-events-auto invisible scale-30 opacity-0 transition-[scale,opacity,visibility,background-color] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:visible group-data-open/planet:scale-100 group-data-open/planet:opacity-100 group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] hover:bg-tcm18-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm18-ring motion-reduce:transition-none">Recipes</a>
              </li>
            </ul>
          </div>
        </li>
        <li data-planet class="group/planet absolute inset-0 grid place-items-center pointer-events-none [--i:1] [--a:calc(360deg/3*var(--i)-90deg)] [--r:var(--pr)]">
          <div class="tcm18-polar relative grid place-items-center">
            <button type="button" aria-expanded="false" aria-controls="tcm-18-moons-1" class="pointer-events-auto relative z-10 grid size-18 cursor-pointer place-items-center rounded-full bg-linear-to-br from-fuchsia-400 to-purple-600 text-[13.5px] font-bold text-white shadow-tcm18-planet ring-1 ring-white/30 transition-[scale,opacity] duration-400 ease-[cubic-bezier(.34,1.45,.5,1)] hover:scale-110 group-data-open/planet:scale-125 group-data-muted/planet:scale-85 group-data-muted/planet:opacity-40 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tcm18-ring motion-reduce:transition-none">API</button>
            <ul id="tcm-18-moons-1" class="absolute inset-0">
              <li class="tcm18-polar absolute top-1/2 left-1/2 [--j:0] [--a:calc(360deg/3*var(--j)-90deg)] [--r:0rem] transition-[translate] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:[--r:5.6rem] group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] motion-reduce:transition-none">
                <a href="#tcm-18-rest" data-moon class="absolute top-0 left-0 grid h-10 -translate-1/2 place-items-center rounded-full bg-tcm18-moon px-3.5 text-[12px] font-semibold whitespace-nowrap text-tcm18-moon-ink shadow-tcm18-moon ring-1 ring-tcm18-line pointer-events-auto invisible scale-30 opacity-0 transition-[scale,opacity,visibility,background-color] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:visible group-data-open/planet:scale-100 group-data-open/planet:opacity-100 group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] hover:bg-tcm18-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm18-ring motion-reduce:transition-none">REST</a>
              </li>
              <li class="tcm18-polar absolute top-1/2 left-1/2 [--j:1] [--a:calc(360deg/3*var(--j)-90deg)] [--r:0rem] transition-[translate] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:[--r:5.6rem] group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] motion-reduce:transition-none">
                <a href="#tcm-18-graphql" data-moon class="absolute top-0 left-0 grid h-10 -translate-1/2 place-items-center rounded-full bg-tcm18-moon px-3.5 text-[12px] font-semibold whitespace-nowrap text-tcm18-moon-ink shadow-tcm18-moon ring-1 ring-tcm18-line pointer-events-auto invisible scale-30 opacity-0 transition-[scale,opacity,visibility,background-color] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:visible group-data-open/planet:scale-100 group-data-open/planet:opacity-100 group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] hover:bg-tcm18-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm18-ring motion-reduce:transition-none">GraphQL</a>
              </li>
              <li class="tcm18-polar absolute top-1/2 left-1/2 [--j:2] [--a:calc(360deg/3*var(--j)-90deg)] [--r:0rem] transition-[translate] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:[--r:5.6rem] group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] motion-reduce:transition-none">
                <a href="#tcm-18-webhooks" data-moon class="absolute top-0 left-0 grid h-10 -translate-1/2 place-items-center rounded-full bg-tcm18-moon px-3.5 text-[12px] font-semibold whitespace-nowrap text-tcm18-moon-ink shadow-tcm18-moon ring-1 ring-tcm18-line pointer-events-auto invisible scale-30 opacity-0 transition-[scale,opacity,visibility,background-color] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:visible group-data-open/planet:scale-100 group-data-open/planet:opacity-100 group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] hover:bg-tcm18-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm18-ring motion-reduce:transition-none">Webhooks</a>
              </li>
            </ul>
          </div>
        </li>
        <li data-planet class="group/planet absolute inset-0 grid place-items-center pointer-events-none [--i:2] [--a:calc(360deg/3*var(--i)-90deg)] [--r:var(--pr)]">
          <div class="tcm18-polar relative grid place-items-center">
            <button type="button" aria-expanded="false" aria-controls="tcm-18-moons-2" class="pointer-events-auto relative z-10 grid size-18 cursor-pointer place-items-center rounded-full bg-linear-to-br from-emerald-400 to-teal-600 text-[13.5px] font-bold text-white shadow-tcm18-planet ring-1 ring-white/30 transition-[scale,opacity] duration-400 ease-[cubic-bezier(.34,1.45,.5,1)] hover:scale-110 group-data-open/planet:scale-125 group-data-muted/planet:scale-85 group-data-muted/planet:opacity-40 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tcm18-ring motion-reduce:transition-none">SDKs</button>
            <ul id="tcm-18-moons-2" class="absolute inset-0">
              <li class="tcm18-polar absolute top-1/2 left-1/2 [--j:0] [--a:calc(360deg/3*var(--j)-90deg)] [--r:0rem] transition-[translate] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:[--r:5.6rem] group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] motion-reduce:transition-none">
                <a href="#tcm-18-javascript" data-moon class="absolute top-0 left-0 grid h-10 -translate-1/2 place-items-center rounded-full bg-tcm18-moon px-3.5 text-[12px] font-semibold whitespace-nowrap text-tcm18-moon-ink shadow-tcm18-moon ring-1 ring-tcm18-line pointer-events-auto invisible scale-30 opacity-0 transition-[scale,opacity,visibility,background-color] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:visible group-data-open/planet:scale-100 group-data-open/planet:opacity-100 group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] hover:bg-tcm18-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm18-ring motion-reduce:transition-none">JavaScript</a>
              </li>
              <li class="tcm18-polar absolute top-1/2 left-1/2 [--j:1] [--a:calc(360deg/3*var(--j)-90deg)] [--r:0rem] transition-[translate] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:[--r:5.6rem] group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] motion-reduce:transition-none">
                <a href="#tcm-18-python" data-moon class="absolute top-0 left-0 grid h-10 -translate-1/2 place-items-center rounded-full bg-tcm18-moon px-3.5 text-[12px] font-semibold whitespace-nowrap text-tcm18-moon-ink shadow-tcm18-moon ring-1 ring-tcm18-line pointer-events-auto invisible scale-30 opacity-0 transition-[scale,opacity,visibility,background-color] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:visible group-data-open/planet:scale-100 group-data-open/planet:opacity-100 group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] hover:bg-tcm18-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm18-ring motion-reduce:transition-none">Python</a>
              </li>
              <li class="tcm18-polar absolute top-1/2 left-1/2 [--j:2] [--a:calc(360deg/3*var(--j)-90deg)] [--r:0rem] transition-[translate] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:[--r:5.6rem] group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] motion-reduce:transition-none">
                <a href="#tcm-18-go" data-moon class="absolute top-0 left-0 grid h-10 -translate-1/2 place-items-center rounded-full bg-tcm18-moon px-3.5 text-[12px] font-semibold whitespace-nowrap text-tcm18-moon-ink shadow-tcm18-moon ring-1 ring-tcm18-line pointer-events-auto invisible scale-30 opacity-0 transition-[scale,opacity,visibility,background-color] duration-450 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--j)*55ms)] group-data-open/planet:visible group-data-open/planet:scale-100 group-data-open/planet:opacity-100 group-data-open/planet:delay-[calc(100ms+var(--j)*55ms)] hover:bg-tcm18-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm18-ring motion-reduce:transition-none">Go</a>
              </li>
            </ul>
          </div>
        </li>
      </ul>
    </nav>
    <p class="text-[13px] text-tcm18-mut">Escape closes the open planet</p>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm18-card px-3.5 py-2 text-center font-tcm18-mono text-[11.5px] text-tcm18-mut ring-1 ring-tcm18-line ">nested tcm18-polar · group-data-open/planet: · group-data-muted/planet:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm18-bg: #f1f3fb;
  --color-tcm18-bg: oklch(0.965 0.011 274.9);
  --color-tcm18-glow: #fde68a80;
  --color-tcm18-glow: oklch(0.924 0.115 95.7 / 0.5);
  --color-tcm18-moon: #ffffff;
  --color-tcm18-moon: oklch(1 0 0);
  --color-tcm18-moon-ink: #1e2445;
  --color-tcm18-moon-ink: oklch(0.273 0.062 273.9);
  --color-tcm18-ink: #141933;
  --color-tcm18-ink: oklch(0.224 0.051 273.4);
  --color-tcm18-mut: #565d7c;
  --color-tcm18-mut: oklch(0.485 0.051 274.5);
  --color-tcm18-line: #c9cfe6;
  --color-tcm18-line: oklch(0.857 0.033 274.1);
  --color-tcm18-acc: #4f46e5;
  --color-tcm18-acc: oklch(0.511 0.23 277);
  --color-tcm18-acc-ink: #4338ca;
  --color-tcm18-acc-ink: oklch(0.457 0.215 277);
  --color-tcm18-ring: #4338ca;
  --color-tcm18-ring: oklch(0.457 0.215 277);
  --color-tcm18-card: #ffffff;
  --color-tcm18-card: oklch(1 0 0);
  --font-tcm18-sans: 'Sora', system-ui, sans-serif;
  --font-tcm18-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm18-planet: 0 14px 30px -12px oklch(0.25 0.1 270 / 0.6), inset 0 2px 0 oklch(1 0 0 / 0.35), inset 0 -8px 14px oklch(0 0 0 / 0.15);
  --shadow-tcm18-moon: 0 8px 18px -10px oklch(0.25 0.1 270 / 0.6);
  --shadow-tcm18-sun: 0 0 70px -6px oklch(0.8 0.17 75 / 0.75);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-18 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm18-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: deep space: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-18:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm18-bg: #080b1a;
    --color-tcm18-bg: oklch(0.156 0.032 273.2);
    --color-tcm18-glow: #b4530959;
    --color-tcm18-glow: oklch(0.555 0.146 49 / 0.35);
    --color-tcm18-moon: #e9ecfb;
    --color-tcm18-moon: oklch(0.945 0.02 277);
    --color-tcm18-moon-ink: #141933;
    --color-tcm18-moon-ink: oklch(0.224 0.051 273.4);
    --color-tcm18-ink: #eef0fb;
    --color-tcm18-ink: oklch(0.957 0.015 277.9);
    --color-tcm18-mut: #a1a8c8;
    --color-tcm18-mut: oklch(0.737 0.047 275.5);
    --color-tcm18-line: #2d3458;
    --color-tcm18-line: oklch(0.337 0.064 274.1);
    --color-tcm18-acc: #6366f1;
    --color-tcm18-acc: oklch(0.585 0.204 277.1);
    --color-tcm18-acc-ink: #a5b4fc;
    --color-tcm18-acc-ink: oklch(0.785 0.104 274.7);
    --color-tcm18-ring: #a5b4fc;
    --color-tcm18-ring: oklch(0.785 0.104 274.7);
    --color-tcm18-card: #121735;
    --color-tcm18-card: oklch(0.219 0.059 273.5);
  }
}

.tcm-18[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm18-bg: #080b1a;
  --color-tcm18-bg: oklch(0.156 0.032 273.2);
  --color-tcm18-glow: #b4530959;
  --color-tcm18-glow: oklch(0.555 0.146 49 / 0.35);
  --color-tcm18-moon: #e9ecfb;
  --color-tcm18-moon: oklch(0.945 0.02 277);
  --color-tcm18-moon-ink: #141933;
  --color-tcm18-moon-ink: oklch(0.224 0.051 273.4);
  --color-tcm18-ink: #eef0fb;
  --color-tcm18-ink: oklch(0.957 0.015 277.9);
  --color-tcm18-mut: #a1a8c8;
  --color-tcm18-mut: oklch(0.737 0.047 275.5);
  --color-tcm18-line: #2d3458;
  --color-tcm18-line: oklch(0.337 0.064 274.1);
  --color-tcm18-acc: #6366f1;
  --color-tcm18-acc: oklch(0.585 0.204 277.1);
  --color-tcm18-acc-ink: #a5b4fc;
  --color-tcm18-acc-ink: oklch(0.785 0.104 274.7);
  --color-tcm18-ring: #a5b4fc;
  --color-tcm18-ring: oklch(0.785 0.104 274.7);
  --color-tcm18-card: #121735;
  --color-tcm18-card: oklch(0.219 0.059 273.5);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-18-space');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const planets = [...root.querySelectorAll('[data-planet]')];
  const set = (open) => planets.forEach((p) => {
    const on = p === open;
    p.toggleAttribute('data-open', on);
    p.toggleAttribute('data-muted', !!open && !on);
    p.querySelector('button').setAttribute('aria-expanded', String(on));
  });
  planets.forEach((p) => {
    const btn = p.querySelector('button');
    btn.addEventListener('click', (e) => {
      const opening = !p.hasAttribute('data-open');
      set(opening ? p : null);
      if (opening && e.detail === 0) setTimeout(() => p.querySelector('[data-moon]').focus(), 420);
    });
  });
  root.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape') return;
    const open = planets.find((p) => p.hasAttribute('data-open'));
    if (open) { set(null); open.querySelector('button').focus(); }
  });
  document.addEventListener('pointerdown', (e) => { if (!root.contains(e.target)) set(null); });
})();
```
