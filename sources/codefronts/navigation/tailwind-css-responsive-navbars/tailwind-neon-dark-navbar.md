---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-neon-dark-navbar/"
title: "Tailwind Neon Dark Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "Cyber-terminal chrome: gradient-clipped logotype, a status chip whose dot pulses on a theme-registered keyframe, and links whose neon underline grows inward…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Dark Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-neon-dark-navbar/

Cyber-terminal chrome: gradient-clipped logotype, a status chip whose dot pulses on a theme-registered keyframe, and links whose neon underline grows inward from both edges. The glows are arbitrary shadow-[…] and drop-shadow-[…] values in oklch, which is where colour precision actually matters.
## HTML
```html
<div class="tnb-07 group w-full min-h-svh bg-tnb07-page font-tnb07-body text-tnb07-ink" aria-label="Neon dark navbar demo">
  <input type="checkbox" id="tnb07-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <header class="sticky top-0 z-100 border-b border-tnb07-cyan/20 bg-tnb07-page shadow-[0_1px_0_oklch(0.85_0.15_200/0.15),0_0_40px_oklch(0.85_0.15_200/0.05)]">
    <nav class="mx-auto flex h-16 max-w-6xl items-center gap-6 px-5 font-tnb07-display md:px-8" aria-label="Primary">
      <a href="#system" class="shrink-0 bg-linear-[90deg,var(--color-tnb07-cyan),var(--color-tnb07-magenta)] bg-clip-text text-base font-black tracking-[0.1em] text-transparent uppercase no-underline drop-shadow-[0_0_8px_oklch(0.85_0.15_200/0.5)] transition-[filter] duration-300 hover:drop-shadow-[0_0_16px_oklch(0.85_0.15_200/0.9)] motion-reduce:transition-none">Nexus</a>
      <ul class="hidden flex-1 list-none items-center gap-0 md:flex">
        <li><a href="#system" aria-current="page" class="relative block px-4 py-2 text-[11px] font-semibold tracking-[0.12em] text-tnb07-cyan uppercase no-underline before:absolute before:inset-x-4 before:bottom-1.5 before:h-px before:bg-tnb07-cyan before:shadow-[0_0_6px_var(--color-tnb07-cyan),0_0_12px_var(--color-tnb07-cyan)] before:content-['']">System</a></li>
        <li><a href="#networks" class="relative block px-4 py-2 text-[11px] font-semibold tracking-[0.12em] text-tnb07-mut uppercase no-underline transition-colors duration-250 before:absolute before:right-1/2 before:bottom-1.5 before:left-1/2 before:h-px before:bg-tnb07-cyan before:shadow-[0_0_6px_var(--color-tnb07-cyan),0_0_12px_var(--color-tnb07-cyan)] before:transition-[inset] before:duration-250 before:content-[''] hover:text-tnb07-cyan hover:before:inset-x-4 focus-visible:text-tnb07-cyan focus-visible:before:inset-x-4 motion-reduce:before:transition-none">Networks</a></li>
        <li><a href="#data" class="relative block px-4 py-2 text-[11px] font-semibold tracking-[0.12em] text-tnb07-mut uppercase no-underline transition-colors duration-250 before:absolute before:right-1/2 before:bottom-1.5 before:left-1/2 before:h-px before:bg-tnb07-cyan before:shadow-[0_0_6px_var(--color-tnb07-cyan),0_0_12px_var(--color-tnb07-cyan)] before:transition-[inset] before:duration-250 before:content-[''] hover:text-tnb07-cyan hover:before:inset-x-4 focus-visible:text-tnb07-cyan focus-visible:before:inset-x-4 motion-reduce:before:transition-none">Data</a></li>
        <li><a href="#security" class="relative block px-4 py-2 text-[11px] font-semibold tracking-[0.12em] text-tnb07-mut uppercase no-underline transition-colors duration-250 before:absolute before:right-1/2 before:bottom-1.5 before:left-1/2 before:h-px before:bg-tnb07-cyan before:shadow-[0_0_6px_var(--color-tnb07-cyan),0_0_12px_var(--color-tnb07-cyan)] before:transition-[inset] before:duration-250 before:content-[''] hover:text-tnb07-cyan hover:before:inset-x-4 focus-visible:text-tnb07-cyan focus-visible:before:inset-x-4 motion-reduce:before:transition-none">Security</a></li>
        <li><a href="#console" class="relative block px-4 py-2 text-[11px] font-semibold tracking-[0.12em] text-tnb07-mut uppercase no-underline transition-colors duration-250 before:absolute before:right-1/2 before:bottom-1.5 before:left-1/2 before:h-px before:bg-tnb07-cyan before:shadow-[0_0_6px_var(--color-tnb07-cyan),0_0_12px_var(--color-tnb07-cyan)] before:transition-[inset] before:duration-250 before:content-[''] hover:text-tnb07-cyan hover:before:inset-x-4 focus-visible:text-tnb07-cyan focus-visible:before:inset-x-4 motion-reduce:before:transition-none">Console</a></li>
      </ul>
      <p role="status" class="hidden shrink-0 items-center gap-2 rounded border border-tnb07-green/30 bg-tnb07-green/5 px-3 py-1.5 text-[10px] tracking-[0.1em] text-tnb07-green lg:flex">
        <span class="size-1.5 animate-tnb07-pulse rounded-full bg-tnb07-green shadow-[0_0_6px_var(--color-tnb07-green),0_0_12px_var(--color-tnb07-green)] motion-reduce:animate-none" aria-hidden="true"></span>ONLINE
      </p>
      <a href="#connect" class="hidden shrink-0 rounded border border-tnb07-cyan px-5 py-2 text-[10px] font-bold tracking-[0.12em] text-tnb07-cyan uppercase no-underline shadow-[0_0_8px_oklch(0.85_0.15_200/0.2),inset_0_0_8px_oklch(0.85_0.15_200/0.05)] transition-[background,box-shadow,color] duration-250 hover:bg-tnb07-cyan/10 hover:text-white hover:shadow-[0_0_20px_oklch(0.85_0.15_200/0.5),inset_0_0_20px_oklch(0.85_0.15_200/0.1)] md:block motion-reduce:transition-none">Connect</a>
      <label for="tnb07-menu" class="ml-auto flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 md:hidden" aria-hidden="true">
        <span class="block h-px w-5.5 rounded-sm bg-tnb07-cyan shadow-[0_0_4px_var(--color-tnb07-cyan)] transition-transform duration-300 group-has-checked:translate-y-1.5 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
        <span class="block h-px w-5.5 rounded-sm bg-tnb07-cyan shadow-[0_0_4px_var(--color-tnb07-cyan)] transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-px w-5.5 rounded-sm bg-tnb07-cyan shadow-[0_0_4px_var(--color-tnb07-cyan)] transition-transform duration-300 group-has-checked:-translate-y-1.5 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
      </label>
    </nav>
    <div class="hidden border-b border-tnb07-cyan/15 bg-tnb07-page px-5 py-2 font-tnb07-display max-md:group-has-checked:grid">
      <a href="#system" class="flex min-h-11 items-center border-b border-tnb07-cyan/10 text-[11px] font-semibold tracking-[0.12em] text-tnb07-cyan uppercase no-underline">System</a>
      <a href="#networks" class="flex min-h-11 items-center border-b border-tnb07-cyan/10 text-[11px] font-semibold tracking-[0.12em] text-tnb07-mut uppercase no-underline transition-colors hover:text-tnb07-cyan">Networks</a>
      <a href="#data" class="flex min-h-11 items-center border-b border-tnb07-cyan/10 text-[11px] font-semibold tracking-[0.12em] text-tnb07-mut uppercase no-underline transition-colors hover:text-tnb07-cyan">Data</a>
      <a href="#security" class="flex min-h-11 items-center border-b border-tnb07-cyan/10 text-[11px] font-semibold tracking-[0.12em] text-tnb07-mut uppercase no-underline transition-colors hover:text-tnb07-cyan">Security</a>
      <a href="#console" class="flex min-h-11 items-center text-[11px] font-semibold tracking-[0.12em] text-tnb07-mut uppercase no-underline transition-colors hover:text-tnb07-cyan">Console</a>
    </div>
  </header>
  <main class="mx-auto max-w-3xl px-5 py-16 md:px-8">
    <h1 class="mb-4 bg-linear-[90deg,var(--color-tnb07-cyan),var(--color-tnb07-magenta)] bg-clip-text font-tnb07-display text-4xl font-black tracking-[0.05em] text-transparent">Neon Dark Navbar</h1>
    <p class="text-base leading-relaxed text-tnb07-ink/55">Hover a link: the underline grows outward from the centre because only its <code class="rounded bg-white/5 px-1.5 py-0.5 text-[0.9em] text-tnb07-cyan">inset</code> animates. Every glow is an arbitrary <code class="rounded bg-white/5 px-1.5 py-0.5 text-[0.9em] text-tnb07-cyan">shadow-[…]</code> in oklch.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb07-page: #0a0a1a;
  --color-tnb07-page: oklch(0.16 0.03 275);
  --color-tnb07-ink: #e0e8ff;
  --color-tnb07-ink: oklch(0.92 0.03 270);
  --color-tnb07-mut: #7e89ad;
  --color-tnb07-mut: oklch(0.62 0.04 270);
  --color-tnb07-cyan: #00f5ff;
  --color-tnb07-cyan: oklch(0.85 0.15 200);
  --color-tnb07-magenta: #ff00cc;
  --color-tnb07-magenta: oklch(0.63 0.31 340);
  --color-tnb07-green: #00ff88;
  --color-tnb07-green: oklch(0.87 0.23 155);
  --font-tnb07-display: 'Orbitron', ui-monospace, monospace;
  --font-tnb07-body: 'DM Sans', system-ui, sans-serif;
  --animate-tnb07-pulse: tnb07-pulse 2s ease-in-out infinite;
}

@keyframes tnb07-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.3;
  }
}

.tnb-07 {
  width: 100%;
  min-height: 100svh;
}

.tnb-07 ::selection {
  background: var(--color-tnb07-cyan);
  color: #0a0a1a;
}
```
