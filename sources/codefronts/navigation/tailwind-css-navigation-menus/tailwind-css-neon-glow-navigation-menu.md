---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-neon-glow-navigation-menu/"
title: "Tailwind CSS Neon Glow Navigation Menu"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "A cyberpunk command bar on a faint cyan grid: a flickering neon logo, a scanning gradient rule under the bar, and links that each ignite in their own hue…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Neon Glow Navigation Menu
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-neon-glow-navigation-menu/

A cyberpunk command bar on a faint cyan grid: a flickering neon logo, a scanning gradient rule under the bar, and links that each ignite in their own hue with a glowing underline that grows from the centre. The Access button fills with a slide-in reveal. Built on v4.1's text-shadow-* utilities and three @theme keyframes. Zero JavaScript.
## HTML
```html
<div class="tnv-14 relative isolate flex min-h-svh w-full flex-col bg-tnv14-bg bg-[linear-gradient(rgb(0_229_255/0.04)_1px,transparent_1px),linear-gradient(90deg,rgb(0_229_255/0.04)_1px,transparent_1px)] bg-[length:40px_40px] font-tnv14-sans text-tnv14-ink antialiased selection:bg-tnv14-green selection:text-black">
  <header class="relative z-10 border-b border-tnv14-cyan/15 bg-tnv14-bg/80 backdrop-blur-sm after:absolute after:inset-x-0 after:-bottom-px after:h-px after:animate-tnv14-scan after:bg-[linear-gradient(90deg,transparent,var(--color-tnv14-cyan),var(--color-tnv14-magenta),transparent)] after:bg-[length:200%_100%] after:content-[''] motion-reduce:after:animate-none">
    <nav aria-label="Main" class="mx-auto flex h-[68px] max-w-6xl items-center justify-between gap-6 px-6 sm:px-12">
      <a href="#" class="animate-tnv14-flicker font-tnv14-display text-[1.45rem] font-black tracking-[0.1em] text-tnv14-cyan text-shadow-[0_0_10px_var(--color-tnv14-cyan),0_0_28px_rgb(0_229_255/0.45)] motion-reduce:animate-none">NEO<span class="text-tnv14-magenta text-shadow-[0_0_10px_var(--color-tnv14-magenta),0_0_28px_rgb(255_0_255/0.45)]">N</span></a>
      <ul class="hidden items-center gap-1 text-[15px] font-semibold tracking-[0.1em] text-tnv14-mut uppercase md:flex [&_a]:relative [&_a]:flex [&_a]:h-11 [&_a]:items-center [&_a]:gap-2 [&_a]:px-3.5 [&_a]:transition-[color,text-shadow] [&_a]:duration-200 [&_a]:after:absolute [&_a]:after:right-1/2 [&_a]:after:bottom-1 [&_a]:after:left-1/2 [&_a]:after:h-[1.5px] [&_a]:after:bg-current [&_a]:after:transition-[left,right,box-shadow] [&_a]:after:duration-300 [&_a]:after:content-[''] [&_a:hover]:text-shadow-[0_0_10px_currentColor] [&_a:hover]:after:right-3 [&_a:hover]:after:left-3 [&_a:hover]:after:shadow-[0_0_10px_currentColor] [&_a:focus-visible]:outline-1 [&_a:focus-visible]:outline-current [&_a[aria-current]]:text-tnv14-cyan [&_a[aria-current]]:text-shadow-[0_0_10px_rgb(0_229_255/0.6)] [&_a[aria-current]]:after:right-3 [&_a[aria-current]]:after:left-3 [&_a[aria-current]]:after:shadow-[0_0_10px_var(--color-tnv14-cyan)] [&_svg]:size-3.5 [&_svg]:opacity-75">
        <li><a href="#" aria-current="page"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/></svg>Home</a></li>
        <li><a href="#" class="hover:text-tnv14-magenta"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/></svg>Systems</a></li>
        <li><a href="#" class="hover:text-tnv14-green"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>Network</a></li>
        <li><a href="#" class="hover:text-tnv14-amber"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>Security</a></li>
        <li><a href="#" class="hover:text-tnv14-pink"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 1v3M12 20v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M1 12h3M20 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/></svg>Config</a></li>
      </ul>
      <a href="#" class="relative isolate inline-flex h-10 items-center overflow-hidden rounded border border-tnv14-cyan px-5 text-sm font-bold tracking-[0.14em] text-tnv14-cyan uppercase transition-[color,box-shadow] duration-200 before:absolute before:inset-0 before:-z-10 before:-translate-x-[101%] before:bg-tnv14-cyan before:transition-transform before:duration-200 before:content-[''] hover:text-black hover:shadow-[0_0_24px_rgb(0_229_255/0.45)] hover:before:translate-x-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnv14-cyan">Access</a>
    </nav>
  </header>
  <main class="relative z-0 flex flex-1 flex-col items-center justify-center px-6 py-20 text-center [&_code]:rounded-sm [&_code]:bg-tnv14-cyan/10 [&_code]:px-1.5 [&_code]:text-tnv14-cyan">
    <p class="mb-7 animate-tnv14-blink text-xs font-semibold tracking-[0.25em] text-tnv14-cyan uppercase motion-reduce:animate-none">▶ System online · hover the nav</p>
    <h1 class="font-tnv14-display text-[clamp(2.75rem,9vw,6.5rem)] leading-[0.98] font-black tracking-[0.04em] uppercase">
      <span class="block text-tnv14-ink">Navigate the</span>
      <span class="block text-tnv14-cyan text-shadow-[0_0_20px_var(--color-tnv14-cyan),0_0_50px_rgb(0_229_255/0.3)]">Cyber</span>
      <span class="block text-tnv14-magenta text-shadow-[0_0_20px_var(--color-tnv14-magenta),0_0_50px_rgb(255_0_255/0.3)]">Grid</span>
    </h1>
    <p class="mt-8 max-w-lg text-lg/[1.6] font-medium text-tnv14-mut text-pretty">Each link ignites in its own hue with a <code>text-shadow-*</code> halo and an underline that grows from the centre. The rule under the bar scans; the logo flickers on a <code>steps()</code> curve.</p>
    <ul class="mt-12 flex flex-wrap justify-center gap-3.5 text-left [&>li]:flex [&>li]:items-center [&>li]:gap-3 [&>li]:rounded-lg [&>li]:border [&>li]:bg-white/[0.025] [&>li]:px-5 [&>li]:py-4 [&>li]:transition-[border-color,box-shadow] [&_b]:block [&_b]:text-sm [&_b]:font-bold [&_b]:tracking-wider [&_b]:uppercase [&_small]:block [&_small]:text-[13px] [&_small]:text-tnv14-mut [&_svg]:size-5">
      <li class="border-tnv14-cyan/25 hover:border-tnv14-cyan hover:shadow-[0_0_24px_rgb(0_229_255/0.15)]"><svg class="text-tnv14-cyan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg><span><b>Underline glow</b><small>box-shadow on after:</small></span></li>
      <li class="border-tnv14-magenta/25 hover:border-tnv14-magenta hover:shadow-[0_0_24px_rgb(255_0_255/0.12)]"><svg class="text-tnv14-magenta" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg><span><b>Scan gradient</b><small>@theme keyframes</small></span></li>
      <li class="border-tnv14-green/25 hover:border-tnv14-green hover:shadow-[0_0_24px_rgb(0_255_157/0.12)]"><svg class="text-tnv14-green" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg><span><b>Fill button</b><small>isolate + translate reveal</small></span></li>
    </ul>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv14-bg: #030307;
  --color-tnv14-bg: oklch(0.1 0.01 285);
  --color-tnv14-ink: #e8e8f0;
  --color-tnv14-ink: oklch(0.93 0.01 285);
  --color-tnv14-mut: #9d9dc0;
  --color-tnv14-mut: oklch(0.72 0.05 285);
  --color-tnv14-cyan: #00e5ff;
  --color-tnv14-cyan: oklch(0.86 0.15 205);
  --color-tnv14-magenta: #ff00ff;
  --color-tnv14-magenta: oklch(0.702 0.322 328);
  --color-tnv14-green: #00ff9d;
  --color-tnv14-green: oklch(0.88 0.21 158);
  --color-tnv14-amber: #ffaa00;
  --color-tnv14-amber: oklch(0.8 0.17 72);
  --color-tnv14-pink: #ff2d7f;
  --color-tnv14-pink: oklch(0.66 0.25 6);
  --font-tnv14-sans: 'Rajdhani', system-ui, sans-serif;
  --font-tnv14-display: 'Orbitron', 'Rajdhani', sans-serif;
  --animate-tnv14-scan: tnv14-scan 4s linear infinite;
  --animate-tnv14-flicker: tnv14-flicker 6s steps(1, end) infinite;
  --animate-tnv14-blink: tnv14-blink 2.5s step-end infinite;

  @keyframes tnv14-scan {
    0% {
      background-position: 100% 0;
    }

    100% {
      background-position: -100% 0;
    }
  }

  @keyframes tnv14-flicker {
    0%,
        18%,
        22%,
        25%,
        53%,
        57%,
        100% {
      opacity: 1;
    }

    20%,
        24%,
        55% {
      opacity: 0.35;
    }
  }

  @keyframes tnv14-blink {
    0%,
        100% {
      opacity: 1;
    }

    50% {
      opacity: 0.25;
    }
  }
}

.tnv-14 {
  width: 100%;
  min-height: 100svh;
}
```
