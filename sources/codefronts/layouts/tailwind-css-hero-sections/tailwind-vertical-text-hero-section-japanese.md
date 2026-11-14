---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-vertical-text-hero-section-japanese/"
title: "Vertical Text Hero Section in Tailwind CSS (Japanese Writing Mode)"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "Traditional Japanese vertical typography — the headline reads top-to-bottom with writing-mode: vertical-rl, set in Noto Serif JP beside English copy, with a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Text Hero Section in Tailwind CSS (Japanese Writing Mode)
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-vertical-text-hero-section-japanese/

Traditional Japanese vertical typography — the headline reads top-to-bottom with writing-mode: vertical-rl, set in Noto Serif JP beside English copy, with a double-ringed vermilion hanko seal. Indigo on washi white.
## HTML
```html
<section class="ths-17 relative isolate grid w-full min-h-svh grid-cols-[auto_1fr] items-center gap-[clamp(24px,6vw,80px)] overflow-hidden bg-ths17-bg bg-[radial-gradient(80%_60%_at_50%_0%,rgb(20_40_80/0.07),transparent_70%)] px-[clamp(20px,5vw,72px)] py-16 font-ths17-serif text-ths17-ink" aria-label="Vertical Japanese typography hero">
  <div aria-hidden="true" class="pointer-events-none absolute inset-y-0 -right-16 -z-10 w-72 bg-[repeating-linear-gradient(0deg,transparent_0_23px,rgb(26_40_88/0.06)_23px_24px)]"></div>
  <div aria-hidden="true" class="absolute top-6 right-6 grid size-[clamp(60px,8vw,80px)] place-items-center bg-ths17-red font-ths17-jp text-[clamp(17px,2.2vw,22px)] leading-tight font-bold text-ths17-bg shadow-[inset_0_0_0_4px_var(--color-ths17-bg),inset_0_0_0_6px_var(--color-ths17-red)]" lang="ja"><span class="text-center">無<br>名</span></div>
  <h1 lang="ja" class="min-h-[min(420px,70svh)] font-ths17-jp text-[clamp(38px,5.2vw,64px)] leading-[1.25] font-bold tracking-[0.08em] whitespace-nowrap [text-orientation:upright] [writing-mode:vertical-rl]">静かな<em class="font-black text-ths17-red not-italic">道具</em>。</h1>
  <div class="flex max-w-[30rem] flex-col gap-5">
    <p lang="ja-Latn" class="font-ths17-serif text-xl tracking-[0.06em] text-ths17-red italic">Shizuka na dōgu — quiet tools.</p>
    <p class="font-ths17-sans text-base/relaxed text-ths17-body">Hand-forged carpentry implements. Made by one family in Niigata since 1873.</p>
    <ul class="flex flex-wrap gap-x-5 gap-y-1 border-y border-ths17-ink/15 py-3 font-ths17-mono text-[11px] tracking-[0.12em] text-ths17-body uppercase">
      <li>Since 1873</li><li>Sanjo, Niigata</li><li>Ships worldwide</li>
    </ul>
    <a href="#shop" class="inline-flex min-h-12 items-center self-start bg-ths17-ink px-6 font-ths17-mono text-xs font-bold tracking-[0.12em] text-ths17-bg transition hover:bg-ths17-red focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths17-ink motion-reduce:transition-none">View the catalogue →</a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths17-bg: #f5ede0;
  --color-ths17-bg: oklch(0.949 0.019 80.1);
  --color-ths17-ink: #1a2858;
  --color-ths17-ink: oklch(0.294 0.088 268.3);
  --color-ths17-body: #3f4a70;
  --color-ths17-body: oklch(0.417 0.065 271);
  --color-ths17-red: #b8321f;
  --color-ths17-red: oklch(0.521 0.174 31.3);
  --font-ths17-jp: 'Noto Serif JP', 'Hiragino Mincho ProN', serif;
  --font-ths17-serif: 'Cormorant Garamond', Georgia, serif;
  --font-ths17-sans: 'Geist', system-ui, sans-serif;
  --font-ths17-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-17 {
  width: 100%;
  min-height: 100svh;
}
```
