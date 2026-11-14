---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-developer-hero-section-terminal-window/"
title: "Tailwind CSS Developer Hero Section with Terminal Window"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A vintage-CRT terminal hero for a modern dev tool — phosphor-green output and amber prompts in a framed window, with scanlines, a blinking cursor and log…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Developer Hero Section with Terminal Window
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-developer-hero-section-terminal-window/

A vintage-CRT terminal hero for a modern dev tool — phosphor-green output and amber prompts in a framed window, with scanlines, a blinking cursor and log lines that print in sequence on load. Ruled beige paper behind, monospace headline in front.
## HTML
```html
<section class="ths-05 grid w-full min-h-svh items-center gap-12 bg-ths05-bg bg-[repeating-linear-gradient(0deg,transparent_0_31px,rgb(50_30_10/0.05)_31px_32px)] px-5 py-16 font-ths05-sans text-ths05-ink sm:px-12 lg:grid-cols-[1fr_1.05fr] lg:gap-16" aria-label="Developer hero with terminal">
  <div class="max-w-xl">
    <span class="inline-flex items-center gap-2 rounded-full border border-ths05-ink/15 bg-ths05-paper px-3 py-1 font-ths05-mono text-[11px] font-medium text-ths05-body"><span aria-hidden="true" class="size-1.5 rounded-full bg-ths05-green shadow-[0_0_8px_var(--color-ths05-green)]"></span>v2.4 · now with remote cache</span>
    <h1 class="mt-5 font-ths05-mono text-[clamp(34px,5vw,56px)] leading-[1.04] font-extrabold tracking-[-0.03em] text-balance">Ship from <em class="text-ths05-amber not-italic before:opacity-60 before:content-['>_']">your terminal.</em></h1>
    <p class="mt-5 max-w-md text-base/relaxed text-ths05-body">One command. No dashboard. No yak shave. Your CI agrees with your local because they share an OS.</p>
    <div class="mt-8 flex flex-wrap items-center gap-3">
      <a href="#install" class="inline-flex min-h-12 items-center bg-ths05-ink px-6 font-ths05-mono text-sm font-bold text-ths05-bg transition hover:bg-ths05-amber focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths05-ink motion-reduce:transition-none">Read the docs →</a>
      <code class="inline-flex min-h-12 items-center gap-2 border border-dashed border-ths05-ink/35 px-4 font-ths05-mono text-[13px] text-ths05-ink"><span class="text-ths05-amber select-none">$</span>brew install swift-ship</code>
    </div>
  </div>
  <div aria-hidden="true" class="overflow-hidden rounded-xl border-2 border-ths05-ink bg-ths05-screen shadow-[0_0_0_8px_rgb(13_25_8/0.1),0_30px_60px_-24px_rgb(42_29_10/0.6)]">
    <div class="flex items-center gap-1.5 border-b border-white/10 bg-ths05-chrome px-4 py-2.5">
      <span class="size-2.5 rounded-full bg-ths05-amber"></span><span class="size-2.5 rounded-full bg-ths05-green/70"></span><span class="size-2.5 rounded-full bg-white/20"></span>
      <span class="ml-auto font-ths05-mono text-[10.5px] text-white/50">~/app — zsh</span>
    </div>
    <div class="relative p-6 font-ths05-mono text-sm leading-[1.9] text-ths05-green [text-shadow:0_0_8px_rgb(95_255_140/0.5)] after:pointer-events-none after:absolute after:inset-0 after:bg-[repeating-linear-gradient(0deg,rgb(0_0_0/0.18)_0_1px,transparent_1px_3px)] after:content-[''] sm:text-[15px]">
      <p><span class="mr-2 text-ths05-amber [text-shadow:0_0_8px_rgb(255_179_72/0.5)]">$</span>swift install</p>
      <p class="pl-4 text-ths05-out transition-opacity delay-300 duration-200 starting:opacity-0 motion-reduce:transition-none">→ resolving dependencies</p>
      <p class="pl-4 text-ths05-out transition-opacity delay-700 duration-200 starting:opacity-0 motion-reduce:transition-none">→ compiling 47 modules</p>
      <p class="pl-4 text-ths05-out transition-opacity delay-[1100ms] duration-200 starting:opacity-0 motion-reduce:transition-none">→ linking binary</p>
      <p class="pl-4 font-bold transition-opacity delay-[1500ms] duration-200 starting:opacity-0 motion-reduce:transition-none">✓ shipped in 2.3s</p>
      <p class="transition-opacity delay-[1700ms] duration-200 starting:opacity-0 motion-reduce:transition-none"><span class="mr-2 text-ths05-amber">$</span><span class="inline-block h-4 w-2 animate-ths05-blink bg-ths05-green align-[-2px] motion-reduce:animate-none"></span></p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths05-bg: #f0e4cf;
  --color-ths05-bg: oklch(0.923 0.031 81.8);
  --color-ths05-paper: #f7eedd;
  --color-ths05-paper: oklch(0.952 0.025 83.4);
  --color-ths05-ink: #2a1d0a;
  --color-ths05-ink: oklch(0.242 0.037 74.8);
  --color-ths05-body: #5a4220;
  --color-ths05-body: oklch(0.397 0.059 74.2);
  --color-ths05-amber: #b8580c;
  --color-ths05-amber: oklch(0.569 0.145 50.4);
  --color-ths05-screen: #0d1908;
  --color-ths05-screen: oklch(0.196 0.037 137);
  --color-ths05-chrome: #1a2414;
  --color-ths05-chrome: oklch(0.245 0.032 134.3);
  --color-ths05-green: #5fff8c;
  --color-ths05-green: oklch(0.89 0.206 149.4);
  --color-ths05-out: #9cbca4;
  --color-ths05-out: oklch(0.765 0.049 152.7);
  --font-ths05-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-ths05-sans: 'Geist', system-ui, sans-serif;
  --animate-ths05-blink: ths05-blink 1s steps(2) infinite;

  @keyframes ths05-blink {
    to {
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-05 {
  width: 100%;
  min-height: 100svh;
}
```
