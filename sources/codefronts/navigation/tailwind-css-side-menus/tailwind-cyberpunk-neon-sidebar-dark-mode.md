---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-cyberpunk-neon-sidebar-dark-mode/"
title: "Tailwind Cyberpunk Neon Sidebar (Dark Mode)"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "A terminal-grade threat console: Orbitron headings with pink and cyan neon bloom, CRT scanlines drawn by a before: repeating gradient, a faulty-tube flicker…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Cyberpunk Neon Sidebar (Dark Mode)
Source: https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-cyberpunk-neon-sidebar-dark-mode/

A terminal-grade threat console: Orbitron headings with pink and cyan neon bloom, CRT scanlines drawn by a before: repeating gradient, a faulty-tube flicker on the logo and chamfered stat panels cut with clip-path. The port keeps the neon for accents only and lifts every body label to readable contrast — the original's grey-on-black nav was 2.4:1.
## HTML
```html
<section class="tsm-11 flex w-full min-h-svh bg-tsm11-bg font-tsm11-body text-tsm11-ink" aria-label="Cyberpunk neon sidebar demo">
  <nav aria-label="Main" class="relative flex w-56 shrink-0 flex-col overflow-hidden border-r border-tsm11-pink bg-tsm11-nav shadow-[2px_0_24px_oklch(0.65_0.25_5/0.15)] before:pointer-events-none before:absolute before:inset-0 before:bg-[repeating-linear-gradient(0deg,transparent_0_2px,oklch(0.85_0.15_200/0.03)_2px_4px)] after:absolute after:top-0 after:right-0 after:h-16 after:w-px after:bg-linear-to-b after:from-tsm11-cyan after:to-transparent after:shadow-[0_0_8px_var(--color-tsm11-cyan)]">
    <div class="relative border-b border-tsm11-pink/30 px-4 py-5">
      <p class="mb-1 font-tsm11-head text-[10px] tracking-[0.2em] text-tsm11-cyan [text-shadow:0_0_8px_var(--color-tsm11-cyan)]">// SYSTEM ACTIVE</p>
      <p class="font-tsm11-head text-lg font-black tracking-[0.05em] text-white animate-tsm11-flicker [text-shadow:0_0_12px_var(--color-tsm11-pink),0_0_30px_oklch(0.65_0.25_5/0.4)] motion-reduce:animate-none">CYBERX</p>
    </div>
    <ul class="relative flex-1 py-3">
      <li><a href="#" class="flex min-h-11 items-center gap-2.5 border-l-2 border-transparent px-4 font-tsm11-body text-[15px] font-bold tracking-[0.08em] text-tsm11-mut uppercase transition-[color,border-color,background-color,text-shadow] duration-200 hover:border-tsm11-cyan hover:bg-tsm11-cyan/5 hover:text-tsm11-cyan hover:[text-shadow:0_0_8px_var(--color-tsm11-cyan)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm11-cyan aria-[current=page]:border-tsm11-pink aria-[current=page]:bg-tsm11-pink/8 aria-[current=page]:text-tsm11-pink aria-[current=page]:[text-shadow:0_0_10px_var(--color-tsm11-pink)]" aria-current="page"><span aria-hidden="true" class="size-1.5 shrink-0 rounded-full bg-current shadow-[0_0_8px_currentColor]"></span>Matrix</a></li>
      <li><a href="#" class="flex min-h-11 items-center gap-2.5 border-l-2 border-transparent px-4 font-tsm11-body text-[15px] font-bold tracking-[0.08em] text-tsm11-mut uppercase transition-[color,border-color,background-color,text-shadow] duration-200 hover:border-tsm11-cyan hover:bg-tsm11-cyan/5 hover:text-tsm11-cyan hover:[text-shadow:0_0_8px_var(--color-tsm11-cyan)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm11-cyan aria-[current=page]:border-tsm11-pink aria-[current=page]:bg-tsm11-pink/8 aria-[current=page]:text-tsm11-pink aria-[current=page]:[text-shadow:0_0_10px_var(--color-tsm11-pink)]"><span aria-hidden="true" class="size-1.5 shrink-0 rounded-full bg-current shadow-[0_0_8px_currentColor]"></span>Network</a></li>
      <li><a href="#" class="flex min-h-11 items-center gap-2.5 border-l-2 border-transparent px-4 font-tsm11-body text-[15px] font-bold tracking-[0.08em] text-tsm11-mut uppercase transition-[color,border-color,background-color,text-shadow] duration-200 hover:border-tsm11-cyan hover:bg-tsm11-cyan/5 hover:text-tsm11-cyan hover:[text-shadow:0_0_8px_var(--color-tsm11-cyan)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm11-cyan aria-[current=page]:border-tsm11-pink aria-[current=page]:bg-tsm11-pink/8 aria-[current=page]:text-tsm11-pink aria-[current=page]:[text-shadow:0_0_10px_var(--color-tsm11-pink)]"><span aria-hidden="true" class="size-1.5 shrink-0 rounded-full bg-current shadow-[0_0_8px_currentColor]"></span>Console</a></li>
      <li><a href="#" class="flex min-h-11 items-center gap-2.5 border-l-2 border-transparent px-4 font-tsm11-body text-[15px] font-bold tracking-[0.08em] text-tsm11-mut uppercase transition-[color,border-color,background-color,text-shadow] duration-200 hover:border-tsm11-cyan hover:bg-tsm11-cyan/5 hover:text-tsm11-cyan hover:[text-shadow:0_0_8px_var(--color-tsm11-cyan)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm11-cyan aria-[current=page]:border-tsm11-pink aria-[current=page]:bg-tsm11-pink/8 aria-[current=page]:text-tsm11-pink aria-[current=page]:[text-shadow:0_0_10px_var(--color-tsm11-pink)]"><span aria-hidden="true" class="size-1.5 shrink-0 rounded-full bg-current shadow-[0_0_8px_currentColor]"></span>Threats</a></li>
      <li><a href="#" class="flex min-h-11 items-center gap-2.5 border-l-2 border-transparent px-4 font-tsm11-body text-[15px] font-bold tracking-[0.08em] text-tsm11-mut uppercase transition-[color,border-color,background-color,text-shadow] duration-200 hover:border-tsm11-cyan hover:bg-tsm11-cyan/5 hover:text-tsm11-cyan hover:[text-shadow:0_0_8px_var(--color-tsm11-cyan)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm11-cyan aria-[current=page]:border-tsm11-pink aria-[current=page]:bg-tsm11-pink/8 aria-[current=page]:text-tsm11-pink aria-[current=page]:[text-shadow:0_0_10px_var(--color-tsm11-pink)]"><span aria-hidden="true" class="size-1.5 shrink-0 rounded-full bg-current shadow-[0_0_8px_currentColor]"></span>Logs</a></li>
      <li><a href="#" class="flex min-h-11 items-center gap-2.5 border-l-2 border-transparent px-4 font-tsm11-body text-[15px] font-bold tracking-[0.08em] text-tsm11-mut uppercase transition-[color,border-color,background-color,text-shadow] duration-200 hover:border-tsm11-cyan hover:bg-tsm11-cyan/5 hover:text-tsm11-cyan hover:[text-shadow:0_0_8px_var(--color-tsm11-cyan)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm11-cyan aria-[current=page]:border-tsm11-pink aria-[current=page]:bg-tsm11-pink/8 aria-[current=page]:text-tsm11-pink aria-[current=page]:[text-shadow:0_0_10px_var(--color-tsm11-pink)]"><span aria-hidden="true" class="size-1.5 shrink-0 rounded-full bg-current shadow-[0_0_8px_currentColor]"></span>Config</a></li>
    </ul>
    <div class="relative border-t border-tsm11-pink/20 px-4 py-3 font-tsm11-head text-[10px] tracking-[0.1em]">
      <div class="mb-1 flex justify-between text-tsm11-mut"><span>CPU</span><span class="text-tsm11-cyan">73%</span></div>
      <div class="mb-1 flex justify-between text-tsm11-mut"><span>MEM</span><span class="text-tsm11-cyan">4.1 GB</span></div>
      <div role="meter" aria-label="CPU load" aria-valuemin="0" aria-valuemax="100" aria-valuenow="73" class="mt-1.5 h-0.5 overflow-hidden rounded-full bg-tsm11-cyan/15"><div class="h-full w-[73%] bg-tsm11-cyan shadow-[0_0_6px_var(--color-tsm11-cyan)]"></div></div>
    </div>
  </nav>
  <div class="relative min-w-0 flex-1 overflow-hidden p-6 before:pointer-events-none before:absolute before:inset-0 before:bg-[repeating-linear-gradient(0deg,transparent_0_3px,oklch(0.85_0.15_200/0.015)_3px_6px)]">
    <div class="relative mx-auto max-w-3xl">
      <h1 class="font-tsm11-head text-base font-black tracking-[0.1em] text-tsm11-pink [text-shadow:0_0_12px_var(--color-tsm11-pink)]">// THREAT MATRIX</h1>
      <p class="mt-1.5 mb-6 max-w-prose text-[15px] leading-relaxed font-semibold text-tsm11-mut text-pretty">Neon text-shadow glows, CRT scanlines and a stepped flicker — no images, no external assets, no JavaScript.</p>
      <div class="grid grid-cols-2 gap-2.5 md:grid-cols-4">
        <div class="relative bg-tsm11-surface p-4 ring-1 ring-tsm11-cyan/20 [clip-path:polygon(0_0,calc(100%-14px)_0,100%_14px,100%_100%,0_100%)] before:absolute before:top-0 before:left-0 before:h-px before:w-10 before:bg-tsm11-cyan before:shadow-[0_0_8px_var(--color-tsm11-cyan)] after:absolute after:top-0 after:left-0 after:h-8 after:w-px after:bg-tsm11-cyan after:shadow-[0_0_8px_var(--color-tsm11-cyan)]"><p class="font-tsm11-head text-xl font-bold text-tsm11-cyan [text-shadow:0_0_10px_var(--color-tsm11-cyan)]">0</p><p class="mt-1 text-[11px] font-bold tracking-[0.1em] text-tsm11-mut uppercase">Critical</p></div>
        <div class="relative bg-tsm11-surface p-4 ring-1 ring-tsm11-cyan/20 [clip-path:polygon(0_0,calc(100%-14px)_0,100%_14px,100%_100%,0_100%)] before:absolute before:top-0 before:left-0 before:h-px before:w-10 before:bg-tsm11-cyan before:shadow-[0_0_8px_var(--color-tsm11-cyan)] after:absolute after:top-0 after:left-0 after:h-8 after:w-px after:bg-tsm11-cyan after:shadow-[0_0_8px_var(--color-tsm11-cyan)]"><p class="font-tsm11-head text-xl font-bold text-tsm11-cyan [text-shadow:0_0_10px_var(--color-tsm11-cyan)]">3</p><p class="mt-1 text-[11px] font-bold tracking-[0.1em] text-tsm11-mut uppercase">Warnings</p></div>
        <div class="relative bg-tsm11-surface p-4 ring-1 ring-tsm11-cyan/20 [clip-path:polygon(0_0,calc(100%-14px)_0,100%_14px,100%_100%,0_100%)] before:absolute before:top-0 before:left-0 before:h-px before:w-10 before:bg-tsm11-cyan before:shadow-[0_0_8px_var(--color-tsm11-cyan)] after:absolute after:top-0 after:left-0 after:h-8 after:w-px after:bg-tsm11-cyan after:shadow-[0_0_8px_var(--color-tsm11-cyan)]"><p class="font-tsm11-head text-xl font-bold text-tsm11-cyan [text-shadow:0_0_10px_var(--color-tsm11-cyan)]">99.9%</p><p class="mt-1 text-[11px] font-bold tracking-[0.1em] text-tsm11-mut uppercase">Uptime</p></div>
        <div class="relative bg-tsm11-surface p-4 ring-1 ring-tsm11-cyan/20 [clip-path:polygon(0_0,calc(100%-14px)_0,100%_14px,100%_100%,0_100%)] before:absolute before:top-0 before:left-0 before:h-px before:w-10 before:bg-tsm11-cyan before:shadow-[0_0_8px_var(--color-tsm11-cyan)] after:absolute after:top-0 after:left-0 after:h-8 after:w-px after:bg-tsm11-cyan after:shadow-[0_0_8px_var(--color-tsm11-cyan)]"><p class="font-tsm11-head text-xl font-bold text-tsm11-cyan [text-shadow:0_0_10px_var(--color-tsm11-cyan)]">14ms</p><p class="mt-1 text-[11px] font-bold tracking-[0.1em] text-tsm11-mut uppercase">Latency</p></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm11-bg: #020409;
  --color-tsm11-bg: oklch(0.106 0.017 259.5);
  --color-tsm11-surface: #07080f;
  --color-tsm11-surface: oklch(0.137 0.016 276.8);
  --color-tsm11-nav: #040610;
  --color-tsm11-nav: oklch(0.126 0.025 270.5);
  --color-tsm11-pink: #ff2d78;
  --color-tsm11-pink: oklch(0.657 0.241 6.9);
  --color-tsm11-cyan: #00e5ff;
  --color-tsm11-cyan: oklch(0.844 0.146 209.3);
  --color-tsm11-ink: #e2e8f0;
  --color-tsm11-ink: oklch(0.929 0.013 255.5);
  --color-tsm11-mut: #9aa3b8;
  --color-tsm11-mut: oklch(0.715 0.032 267.1);
  --font-tsm11-head: 'Orbitron', monospace;
  --font-tsm11-body: 'Rajdhani', system-ui, sans-serif;
  --animate-tsm11-flicker: tsm11-flicker 6s step-end infinite;

  @keyframes tsm11-flicker {
    0%,
        95%,
        100% {
      opacity: 1;
    }

    96% {
      opacity: 0.7;
    }

    98% {
      opacity: 0.9;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-11 {
  width: 100%;
  min-height: 100svh;
}
```
