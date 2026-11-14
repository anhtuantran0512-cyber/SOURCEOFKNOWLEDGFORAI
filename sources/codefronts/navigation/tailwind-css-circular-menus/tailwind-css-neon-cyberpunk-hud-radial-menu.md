---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-neon-cyberpunk-hud-radial-menu/"
title: "Tailwind CSS Neon Cyberpunk HUD Radial Menu"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A starship bridge HUD: a radar sweep turns behind six hexagonal system nodes, two dashed rails counter-rotate for parallax, scanlines and a fading grid sit…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Neon Cyberpunk HUD Radial Menu
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-neon-cyberpunk-hud-radial-menu/

A starship bridge HUD: a radar sweep turns behind six hexagonal system nodes, two dashed rails counter-rotate for parallax, scanlines and a fading grid sit under everything, and the core flickers with live status. The sweep is one masked conic-gradient, the nodes are clip-path hexagons styled by aria-pressed:, and every animation is a @theme token &mdash; deep-space dark by default, with a daylight lab variant.
## HTML
```html
<section class="tcm-16 relative w-full min-h-svh grid place-items-center overflow-hidden bg-tcm16-bg bg-[radial-gradient(50%_45%_at_50%_48%,var(--color-tcm16-glow),transparent_72%)] px-4 py-14 font-tcm16-sans text-tcm16-ink antialiased" aria-label="Neon cyberpunk HUD radial menu demo">
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 bg-[repeating-linear-gradient(0deg,transparent_0_3px,var(--color-tcm16-scan)_3px_4px)]"></div>
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 bg-[linear-gradient(var(--color-tcm16-grid)_1px,transparent_1px),linear-gradient(90deg,var(--color-tcm16-grid)_1px,transparent_1px)] bg-size-[40px_40px] [mask-image:radial-gradient(circle_at_50%_50%,black,transparent_70%)]"></div>
  <div class="relative grid w-full justify-items-center gap-6">
    <header class="flex w-full max-w-[24rem] items-center justify-between font-tcm16-mono text-[11px] tracking-[0.18em] text-tcm16-neon uppercase">
      <span>ISV Kestrel</span><span class="inline-flex items-center gap-1.5"><span aria-hidden="true" class="size-1.5 animate-pulse rounded-full bg-tcm16-neon shadow-tcm16-dot motion-reduce:animate-none"></span>Bridge link</span>
    </header>
    <nav id="tcm-16-hud" class="relative grid size-[min(23rem,92vw)] place-items-center [--n:6] [--r:min(9.6rem,38vw)]" aria-label="Ship systems">
      <span aria-hidden="true" class="absolute inset-[4%] rounded-full bg-[conic-gradient(from_0deg,transparent_78%,var(--color-tcm16-neon-dim)_96%,var(--color-tcm16-neon))] [mask-image:radial-gradient(circle,transparent_33%,black_34%)] animate-tcm16-rot motion-reduce:animate-none"></span>
      <span aria-hidden="true" class="absolute inset-0 rounded-full border border-dashed border-tcm16-neon/40 animate-tcm16-rot [animation-duration:60s] motion-reduce:animate-none"></span>
      <span aria-hidden="true" class="absolute inset-[11%] rounded-full border border-dashed border-tcm16-neon/25 animate-tcm16-rot [animation-direction:reverse] [animation-duration:45s] motion-reduce:animate-none"></span>
      <span aria-hidden="true" class="absolute inset-[calc(50%-var(--r))] rounded-full border border-tcm16-neon/20"></span>
      <ul class="absolute inset-0">
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:0] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-node data-sys="Navigation" data-stat="Plotting course · 4.2 AU" aria-pressed="true" aria-label="Navigation" class="tcm16-polar pointer-events-auto grid size-14 cursor-pointer place-items-center bg-tcm16-panel font-tcm16-mono text-[12px] font-bold tracking-[0.1em] text-tcm16-neon [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] shadow-tcm16-node transition-[background-color,color,scale] duration-200 hover:scale-110 hover:bg-tcm16-neon/20 aria-pressed:bg-tcm16-neon aria-pressed:text-tcm16-on focus-visible:scale-110 focus-visible:bg-tcm16-neon/30 focus-visible:outline-none motion-reduce:transition-none">NAV</button>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:1] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-node data-sys="Shields" data-stat="94% integrity" aria-pressed="false" aria-label="Shields" class="tcm16-polar pointer-events-auto grid size-14 cursor-pointer place-items-center bg-tcm16-panel font-tcm16-mono text-[12px] font-bold tracking-[0.1em] text-tcm16-neon [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] shadow-tcm16-node transition-[background-color,color,scale] duration-200 hover:scale-110 hover:bg-tcm16-neon/20 aria-pressed:bg-tcm16-neon aria-pressed:text-tcm16-on focus-visible:scale-110 focus-visible:bg-tcm16-neon/30 focus-visible:outline-none motion-reduce:transition-none">SHD</button>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:2] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-node data-sys="Weapons" data-stat="Safeties engaged" aria-pressed="false" aria-label="Weapons" class="tcm16-polar pointer-events-auto grid size-14 cursor-pointer place-items-center bg-tcm16-panel font-tcm16-mono text-[12px] font-bold tracking-[0.1em] text-tcm16-neon [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] shadow-tcm16-node transition-[background-color,color,scale] duration-200 hover:scale-110 hover:bg-tcm16-neon/20 aria-pressed:bg-tcm16-neon aria-pressed:text-tcm16-on focus-visible:scale-110 focus-visible:bg-tcm16-neon/30 focus-visible:outline-none motion-reduce:transition-none">WPN</button>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:3] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-node data-sys="Comms" data-stat="Channel 7 open" aria-pressed="false" aria-label="Comms" class="tcm16-polar pointer-events-auto grid size-14 cursor-pointer place-items-center bg-tcm16-panel font-tcm16-mono text-[12px] font-bold tracking-[0.1em] text-tcm16-neon [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] shadow-tcm16-node transition-[background-color,color,scale] duration-200 hover:scale-110 hover:bg-tcm16-neon/20 aria-pressed:bg-tcm16-neon aria-pressed:text-tcm16-on focus-visible:scale-110 focus-visible:bg-tcm16-neon/30 focus-visible:outline-none motion-reduce:transition-none">COM</button>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:4] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-node data-sys="Engines" data-stat="62% thrust" aria-pressed="false" aria-label="Engines" class="tcm16-polar pointer-events-auto grid size-14 cursor-pointer place-items-center bg-tcm16-panel font-tcm16-mono text-[12px] font-bold tracking-[0.1em] text-tcm16-neon [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] shadow-tcm16-node transition-[background-color,color,scale] duration-200 hover:scale-110 hover:bg-tcm16-neon/20 aria-pressed:bg-tcm16-neon aria-pressed:text-tcm16-on focus-visible:scale-110 focus-visible:bg-tcm16-neon/30 focus-visible:outline-none motion-reduce:transition-none">ENG</button>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:5] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-node data-sys="Sensors" data-stat="Sweep active" aria-pressed="false" aria-label="Sensors" class="tcm16-polar pointer-events-auto grid size-14 cursor-pointer place-items-center bg-tcm16-panel font-tcm16-mono text-[12px] font-bold tracking-[0.1em] text-tcm16-neon [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] shadow-tcm16-node transition-[background-color,color,scale] duration-200 hover:scale-110 hover:bg-tcm16-neon/20 aria-pressed:bg-tcm16-neon aria-pressed:text-tcm16-on focus-visible:scale-110 focus-visible:bg-tcm16-neon/30 focus-visible:outline-none motion-reduce:transition-none">SNS</button>
        </li>
      </ul>
      <div class="relative grid size-[min(12.5rem,50vw)] place-content-center justify-items-center gap-2 rounded-full bg-tcm16-core text-center shadow-tcm16-core ring-1 ring-tcm16-neon/50">
        <span class="font-tcm16-mono text-[10px] tracking-[0.4em] text-tcm16-mut uppercase">System</span>
        <output data-sys aria-live="polite" class="font-tcm16-sans text-[clamp(1.1rem,4.5vw,1.45rem)] leading-none font-bold tracking-[0.06em] text-tcm16-neon uppercase [text-shadow:0_0_12px_var(--color-tcm16-neon-dim)]">Navigation</output>
        <span data-stat class="max-w-[9rem] font-tcm16-mono text-[12px] leading-snug text-tcm16-ink/85 animate-tcm16-flicker motion-reduce:animate-none">Plotting course · 4.2 AU</span>
        <span aria-hidden="true" class="mt-1 h-1 w-20 overflow-hidden rounded-full bg-tcm16-neon/15"><span class="block h-full w-1/2 rounded-full bg-tcm16-neon shadow-tcm16-dot animate-tcm16-load motion-reduce:animate-none"></span></span>
      </div>
    </nav>
    <p class="font-tcm16-mono text-[12px] tracking-[0.06em] text-tcm16-mut">Select a system · ← → to cycle</p>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm16-card px-3.5 py-2 text-center font-tcm16-mono text-[11.5px] text-tcm16-mut ring-1 ring-tcm16-line ">conic sweep + mask · hex clip-path nodes · aria-pressed:bg-tcm16-neon</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm16-bg: #eaf6f8;
  --color-tcm16-bg: oklch(0.965 0.013 208.8);
  --color-tcm16-glow: #a5f3fc80;
  --color-tcm16-glow: oklch(0.917 0.077 205 / 0.5);
  --color-tcm16-scan: #0e749012;
  --color-tcm16-scan: oklch(0.52 0.094 223.1 / 0.07);
  --color-tcm16-grid: #0e74901a;
  --color-tcm16-grid: oklch(0.52 0.094 223.1 / 0.1);
  --color-tcm16-panel: #ffffffd9;
  --color-tcm16-panel: oklch(1 0 0 / 0.85);
  --color-tcm16-core: #f6fdfe;
  --color-tcm16-core: oklch(0.989 0.008 207.1);
  --color-tcm16-ink: #082f37;
  --color-tcm16-ink: oklch(0.283 0.044 214.6);
  --color-tcm16-mut: #3f6670;
  --color-tcm16-mut: oklch(0.485 0.047 215.8);
  --color-tcm16-neon: #0e7490;
  --color-tcm16-neon: oklch(0.52 0.094 223.1);
  --color-tcm16-neon-dim: #0891b240;
  --color-tcm16-neon-dim: oklch(0.609 0.111 221.7 / 0.25);
  --color-tcm16-on: #ffffff;
  --color-tcm16-on: oklch(1 0 0);
  --color-tcm16-card: #ffffffcc;
  --color-tcm16-card: oklch(1 0 0 / 0.8);
  --color-tcm16-line: #0e749033;
  --color-tcm16-line: oklch(0.52 0.094 223.1 / 0.2);
  --font-tcm16-sans: 'Chakra Petch', system-ui, sans-serif;
  --font-tcm16-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm16-node: 0 0 18px -4px var(--color-tcm16-neon-dim);
  --shadow-tcm16-core: 0 0 60px -10px var(--color-tcm16-neon-dim), inset 0 0 30px var(--color-tcm16-neon-dim);
  --shadow-tcm16-dot: 0 0 8px var(--color-tcm16-neon);
  --animate-tcm16-rot: tcm16-rot 6s linear infinite;
  --animate-tcm16-flicker: tcm16-flicker 4s linear infinite;
  --animate-tcm16-load: tcm16-load 1.8s ease-in-out infinite;

  @keyframes tcm16-rot {
    to {
      rotate: 360deg;
    }
  }

  @keyframes tcm16-flicker {
    0%,
        91%,
        94%,
        98%,
        100% {
      opacity: 1;
    }

    92%,
        96% {
      opacity: 0.5;
    }
  }

  @keyframes tcm16-load {
    from {
      translate: -100% 0;
    }

    to {
      translate: 200% 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-16 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm16-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: deep space (the hero mode): the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-16:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm16-bg: #05090f;
    --color-tcm16-bg: oklch(0.138 0.016 253.5);
    --color-tcm16-glow: #0e749040;
    --color-tcm16-glow: oklch(0.52 0.094 223.1 / 0.25);
    --color-tcm16-scan: #00000033;
    --color-tcm16-scan: oklch(0 0 0 / 0.2);
    --color-tcm16-grid: #22d3ee14;
    --color-tcm16-grid: oklch(0.797 0.134 211.5 / 0.08);
    --color-tcm16-panel: #0b1a24e6;
    --color-tcm16-panel: oklch(0.21 0.029 239.3 / 0.9);
    --color-tcm16-core: #07131bf2;
    --color-tcm16-core: oklch(0.18 0.024 238.6 / 0.95);
    --color-tcm16-ink: #d9f7fb;
    --color-tcm16-ink: oklch(0.956 0.032 206.4);
    --color-tcm16-mut: #7fa9b2;
    --color-tcm16-mut: oklch(0.707 0.047 212.3);
    --color-tcm16-neon: #5ff5ff;
    --color-tcm16-neon: oklch(0.894 0.126 201.4);
    --color-tcm16-neon-dim: #22d3ee4d;
    --color-tcm16-neon-dim: oklch(0.797 0.134 211.5 / 0.3);
    --color-tcm16-on: #04141a;
    --color-tcm16-on: oklch(0.18 0.026 223.6);
    --color-tcm16-card: #0b1a24;
    --color-tcm16-card: oklch(0.21 0.029 239.3);
    --color-tcm16-line: #22d3ee33;
    --color-tcm16-line: oklch(0.797 0.134 211.5 / 0.2);
  }
}

.tcm-16[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm16-bg: #05090f;
  --color-tcm16-bg: oklch(0.138 0.016 253.5);
  --color-tcm16-glow: #0e749040;
  --color-tcm16-glow: oklch(0.52 0.094 223.1 / 0.25);
  --color-tcm16-scan: #00000033;
  --color-tcm16-scan: oklch(0 0 0 / 0.2);
  --color-tcm16-grid: #22d3ee14;
  --color-tcm16-grid: oklch(0.797 0.134 211.5 / 0.08);
  --color-tcm16-panel: #0b1a24e6;
  --color-tcm16-panel: oklch(0.21 0.029 239.3 / 0.9);
  --color-tcm16-core: #07131bf2;
  --color-tcm16-core: oklch(0.18 0.024 238.6 / 0.95);
  --color-tcm16-ink: #d9f7fb;
  --color-tcm16-ink: oklch(0.956 0.032 206.4);
  --color-tcm16-mut: #7fa9b2;
  --color-tcm16-mut: oklch(0.707 0.047 212.3);
  --color-tcm16-neon: #5ff5ff;
  --color-tcm16-neon: oklch(0.894 0.126 201.4);
  --color-tcm16-neon-dim: #22d3ee4d;
  --color-tcm16-neon-dim: oklch(0.797 0.134 211.5 / 0.3);
  --color-tcm16-on: #04141a;
  --color-tcm16-on: oklch(0.18 0.026 223.6);
  --color-tcm16-card: #0b1a24;
  --color-tcm16-card: oklch(0.21 0.029 239.3);
  --color-tcm16-line: #22d3ee33;
  --color-tcm16-line: oklch(0.797 0.134 211.5 / 0.2);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-16-hud');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const nodes = [...root.querySelectorAll('[data-node]')];
  const sys = root.querySelector('[data-sys]'), stat = root.querySelector('[data-stat]');
  const pick = (k, focus) => {
    nodes.forEach((n, j) => n.setAttribute('aria-pressed', String(j === k)));
    sys.textContent = nodes[k].dataset.sys;
    stat.textContent = nodes[k].dataset.stat;
    if (focus) nodes[k].focus();
  };
  nodes.forEach((n, k) => n.addEventListener('click', () => pick(k)));
  root.addEventListener('keydown', (e) => {
    const d = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
    const k = nodes.indexOf(document.activeElement);
    if (!d || k < 0) return;
    e.preventDefault();
    pick((k + d + nodes.length) % nodes.length, true);
  });
})();
```
