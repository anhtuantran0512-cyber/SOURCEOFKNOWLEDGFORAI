---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-data-uri-svg-noise-without-image-request/"
title: "Tailwind Data URI SVG Noise Texture Without an Image Request"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "The shippable form of browser-generated grain: the whole <feTurbulence> document folded into a URL-encoded data URI, parked in one custom property, and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Data URI SVG Noise Texture Without an Image Request
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-data-uri-svg-noise-without-image-request/

The shippable form of browser-generated grain: the whole <feTurbulence> document folded into a URL-encoded data URI, parked in one custom property, and reused across a hero, three cards, two buttons and a footer. 382 bytes, zero network requests, and in v4 every surface reads it as bg-[image:var(--gtw03-noise),…] with the blend stack stated right beside it.
## HTML
```html
<section class="gtw-03 relative block w-full min-h-svh bg-gtw03-bg text-gtw03-ink" aria-labelledby="gtw-03-title">
  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-03-theme" class="gtw-03-theme peer sr-only">
    <label for="gtw-03-theme" class="grid place-items-center w-11 h-11 rounded-full border border-gtw03-line bg-gtw03-surf text-gtw03-ink cursor-pointer transition-colors duration-200 hover:border-gtw03-acc peer-focus-visible:outline-2 peer-focus-visible:outline-gtw03-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="relative overflow-hidden bg-[image:var(--gtw03-noise),radial-gradient(120%_140%_at_12%_0%,color-mix(in_oklab,var(--color-gtw03-acc)_26%,var(--color-gtw03-bg))_0%,var(--color-gtw03-bg)_62%)] [background-repeat:repeat,no-repeat] [background-blend-mode:overlay,normal]">
    <div class="w-[min(70rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(4rem,11vw,7.5rem)] pb-[clamp(3rem,8vw,5rem)] grid gap-4 max-w-[58rem]">
      <p class="inline-flex items-center gap-2 justify-self-start m-0 px-[0.8rem] py-[0.35rem] rounded-full border border-gtw03-line bg-[color-mix(in_oklab,var(--color-gtw03-surf)_70%,transparent)] font-gtw03-mono text-[0.74rem] font-medium leading-[1.4] tracking-[0.06em] text-gtw03-mut">
        <span class="w-[7px] h-[7px] rounded-full bg-gtw03-acc" aria-hidden="true"></span>382 bytes · 0 requests
      </p>
      <h1 id="gtw-03-title" class="m-0 max-w-[34rem] font-gtw03-display text-[clamp(2.1rem,6vw,4rem)] font-semibold leading-[1.02] tracking-[-0.035em] text-balance">One texture token. Six surfaces. Nothing fetched.</h1>
      <p class="m-0 max-w-[38rem] text-gtw03-mut text-[clamp(0.97rem,2vw,1.12rem)] text-pretty">Every grained surface on this page reads the same <code class="font-gtw03-mono text-[0.9em]">--gtw03-noise</code> custom property. The texture ships inside the stylesheet as a URL-encoded SVG, so the fifth and sixth uses cost nothing at all.</p>
      <div class="flex flex-wrap gap-[0.7rem] mt-[0.6rem]">
        <a href="#gtw-03-title" class="inline-flex items-center min-h-12 px-[1.35rem] rounded-[10px] no-underline font-gtw03-display text-[0.92rem] font-semibold leading-none text-gtw03-onacc bg-[image:var(--gtw03-noise),linear-gradient(var(--color-gtw03-acc),var(--color-gtw03-acc))] [background-blend-mode:soft-light,normal] transition-[filter] duration-200 hover:brightness-[1.06] focus-visible:outline-2 focus-visible:outline-gtw03-acc focus-visible:outline-offset-[3px]">Copy the token</a>
        <a href="#gtw-03-title" class="inline-flex items-center min-h-12 px-[1.35rem] rounded-[10px] no-underline font-gtw03-display text-[0.92rem] font-semibold leading-none text-gtw03-ink bg-transparent border border-gtw03-line transition-colors duration-200 hover:border-gtw03-acc focus-visible:outline-2 focus-visible:outline-gtw03-acc focus-visible:outline-offset-[3px]">Read the encoding rules</a>
      </div>
    </div>
  </header>

  <main class="w-[min(70rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto py-[clamp(2.5rem,7vw,4.5rem)] grid gap-[clamp(2rem,5vw,3.2rem)]">
    <section class="grid gap-[clamp(1rem,2.4vw,1.5rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,16rem),1fr))] items-start" aria-labelledby="gtw-03-h-cards">
      <h2 id="gtw-03-h-cards" class="sr-only">Surfaces using the token</h2>

      <article class="relative grid gap-3 content-start min-w-0 p-[clamp(1.2rem,3vw,1.8rem)] rounded-2xl border border-gtw03-line bg-[image:var(--gtw03-noise),linear-gradient(var(--color-gtw03-surf),var(--color-gtw03-surf))] [background-blend-mode:overlay,normal] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <h3 class="m-0 font-gtw03-display text-[1.1rem] font-semibold leading-tight">Starter</h3>
        <p class="m-0 font-gtw03-display text-[clamp(1.7rem,4vw,2.3rem)] font-semibold leading-none tracking-[-0.03em]">Free<span class="block mt-1 font-gtw03-mono text-[0.78rem] font-normal leading-none tracking-[0.04em] text-gtw03-mut">forever</span></p>
        <ul class="list-none m-0 p-0 pt-[0.8rem] grid gap-[0.4rem] border-t border-gtw03-line text-[0.9rem] text-gtw03-mut">
          <li class="flex gap-2 before:content-['+'] before:font-gtw03-mono before:text-gtw03-acc">One texture token</li>
          <li class="flex gap-2 before:content-['+'] before:font-gtw03-mono before:text-gtw03-acc">Fine, medium, coarse presets</li>
          <li class="flex gap-2 before:content-['+'] before:font-gtw03-mono before:text-gtw03-acc">Unlimited surfaces</li>
        </ul>
        <a href="#gtw-03-title" class="inline-flex items-center justify-center min-h-11 mt-[0.3rem] rounded-[10px] no-underline font-gtw03-display text-[0.86rem] font-semibold leading-none text-gtw03-onacc bg-[image:var(--gtw03-noise),linear-gradient(var(--color-gtw03-acc),var(--color-gtw03-acc))] [background-blend-mode:soft-light,normal] transition-[filter] duration-200 hover:brightness-[1.07] focus-visible:outline-2 focus-visible:outline-gtw03-acc focus-visible:outline-offset-[3px]">Start here</a>
      </article>

      <article class="relative grid gap-3 content-start min-w-0 p-[clamp(1.2rem,3vw,1.8rem)] rounded-2xl border border-gtw03-acc shadow-[0_0_0_1px_color-mix(in_oklab,var(--color-gtw03-acc)_40%,transparent),0_20px_50px_-30px_color-mix(in_oklab,var(--color-gtw03-acc)_60%,transparent)] bg-[image:var(--gtw03-noise),linear-gradient(var(--color-gtw03-surf),var(--color-gtw03-surf))] [background-blend-mode:overlay,normal] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <p class="m-0 justify-self-start px-[0.6rem] py-[0.2rem] rounded-full bg-gtw03-acc text-gtw03-onacc font-gtw03-mono text-[0.68rem] font-semibold leading-[1.5] tracking-[0.1em] uppercase">Recommended</p>
        <h3 class="m-0 font-gtw03-display text-[1.1rem] font-semibold leading-tight">Studio</h3>
        <p class="m-0 font-gtw03-display text-[clamp(1.7rem,4vw,2.3rem)] font-semibold leading-none tracking-[-0.03em]">$0<span class="block mt-1 font-gtw03-mono text-[0.78rem] font-normal leading-none tracking-[0.04em] text-gtw03-mut">it is CSS</span></p>
        <ul class="list-none m-0 p-0 pt-[0.8rem] grid gap-[0.4rem] border-t border-gtw03-line text-[0.9rem] text-gtw03-mut">
          <li class="flex gap-2 before:content-['+'] before:font-gtw03-mono before:text-gtw03-acc">Everything in Starter</li>
          <li class="flex gap-2 before:content-['+'] before:font-gtw03-mono before:text-gtw03-acc">Per-surface blend modes</li>
          <li class="flex gap-2 before:content-['+'] before:font-gtw03-mono before:text-gtw03-acc">Dark-mode grain balance</li>
        </ul>
        <a href="#gtw-03-title" class="inline-flex items-center justify-center min-h-11 mt-[0.3rem] rounded-[10px] no-underline font-gtw03-display text-[0.86rem] font-semibold leading-none text-gtw03-onacc bg-[image:var(--gtw03-noise),linear-gradient(var(--color-gtw03-acc),var(--color-gtw03-acc))] [background-blend-mode:soft-light,normal] transition-[filter] duration-200 hover:brightness-[1.07] focus-visible:outline-2 focus-visible:outline-gtw03-acc focus-visible:outline-offset-[3px]">Use in production</a>
      </article>

      <article class="relative grid gap-3 content-start min-w-0 p-[clamp(1.2rem,3vw,1.8rem)] rounded-2xl border border-gtw03-line bg-[image:var(--gtw03-noise),linear-gradient(var(--color-gtw03-surf),var(--color-gtw03-surf))] [background-blend-mode:overlay,normal] transition-[translate] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <h3 class="m-0 font-gtw03-display text-[1.1rem] font-semibold leading-tight">Legacy PNG</h3>
        <p class="m-0 font-gtw03-display text-[clamp(1.7rem,4vw,2.3rem)] font-semibold leading-none tracking-[-0.03em]">148KB<span class="block mt-1 font-gtw03-mono text-[0.78rem] font-normal leading-none tracking-[0.04em] text-gtw03-mut">per tile</span></p>
        <ul class="list-none m-0 p-0 pt-[0.8rem] grid gap-[0.4rem] border-t border-gtw03-line text-[0.9rem] text-gtw03-mut">
          <li class="flex gap-2 line-through decoration-1 before:content-['-'] before:font-gtw03-mono before:text-gtw03-mut before:no-underline">Extra network request</li>
          <li class="flex gap-2 line-through decoration-1 before:content-['-'] before:font-gtw03-mono before:text-gtw03-mut before:no-underline">Visible tiling seams</li>
          <li class="flex gap-2 line-through decoration-1 before:content-['-'] before:font-gtw03-mono before:text-gtw03-mut before:no-underline">Cannot be themed</li>
        </ul>
        <a href="#gtw-03-title" class="inline-flex items-center justify-center min-h-11 mt-[0.3rem] rounded-[10px] no-underline font-gtw03-display text-[0.86rem] font-semibold leading-none text-gtw03-mut bg-transparent border border-gtw03-line transition-colors duration-200 hover:border-gtw03-acc hover:text-gtw03-ink focus-visible:outline-2 focus-visible:outline-gtw03-acc focus-visible:outline-offset-[3px]">Not this one</a>
      </article>
    </section>

    <section class="grid gap-[0.9rem] p-[clamp(1.2rem,3vw,1.9rem)] rounded-2xl border border-gtw03-line bg-gtw03-surf" aria-labelledby="gtw-03-h-strip">
      <h2 id="gtw-03-h-strip" class="m-0 font-gtw03-display text-[clamp(1.1rem,2.6vw,1.35rem)] font-semibold leading-tight">The four characters that break it</h2>
      <dl class="m-0 grid gap-[0.6rem] grid-cols-[repeat(auto-fit,minmax(min(100%,7rem),1fr))]">
        <div class="grid gap-[0.15rem] px-[0.85rem] py-[0.7rem] rounded-[10px] border border-gtw03-line bg-[color-mix(in_oklab,var(--color-gtw03-acc)_6%,transparent)]"><dt class="m-0 font-gtw03-mono text-[1.15rem] font-semibold leading-none">&lt;</dt><dd class="m-0 font-gtw03-mono text-[0.85rem] leading-none text-gtw03-acc">%3C</dd></div>
        <div class="grid gap-[0.15rem] px-[0.85rem] py-[0.7rem] rounded-[10px] border border-gtw03-line bg-[color-mix(in_oklab,var(--color-gtw03-acc)_6%,transparent)]"><dt class="m-0 font-gtw03-mono text-[1.15rem] font-semibold leading-none">&gt;</dt><dd class="m-0 font-gtw03-mono text-[0.85rem] leading-none text-gtw03-acc">%3E</dd></div>
        <div class="grid gap-[0.15rem] px-[0.85rem] py-[0.7rem] rounded-[10px] border border-gtw03-line bg-[color-mix(in_oklab,var(--color-gtw03-acc)_6%,transparent)]"><dt class="m-0 font-gtw03-mono text-[1.15rem] font-semibold leading-none">#</dt><dd class="m-0 font-gtw03-mono text-[0.85rem] leading-none text-gtw03-acc">%23</dd></div>
        <div class="grid gap-[0.15rem] px-[0.85rem] py-[0.7rem] rounded-[10px] border border-gtw03-line bg-[color-mix(in_oklab,var(--color-gtw03-acc)_6%,transparent)]"><dt class="m-0 font-gtw03-mono text-[1.15rem] font-semibold leading-none">%</dt><dd class="m-0 font-gtw03-mono text-[0.85rem] leading-none text-gtw03-acc">%25</dd></div>
      </dl>
      <p class="m-0 text-gtw03-mut text-[0.9rem] text-pretty">An unescaped <code class="font-gtw03-mono text-[0.9em]">#</code> truncates the URI at the first filter reference. No background, no error, one lost hour.</p>
    </section>
  </main>

  <footer class="border-t border-gtw03-line bg-[image:var(--gtw03-noise),linear-gradient(var(--color-gtw03-surf),var(--color-gtw03-surf))] [background-blend-mode:overlay,normal]">
    <p class="w-[min(70rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto my-0 py-[clamp(1.5rem,4vw,2.4rem)] text-gtw03-mut text-[0.88rem]">Grained footer, grained hero, grained cards, grained buttons — one declaration, and the reader downloaded it exactly zero times.</p>
  </footer>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw03-bg: #101211;
  --color-gtw03-bg: oklch(0.19 0.006 150);
  --color-gtw03-surf: #191d1b;
  --color-gtw03-surf: oklch(0.24 0.008 155);
  --color-gtw03-line: #2c332f;
  --color-gtw03-line: oklch(0.32 0.01 155);
  --color-gtw03-ink: #eef3ef;
  --color-gtw03-ink: oklch(0.96 0.008 150);
  --color-gtw03-mut: #93a29a;
  --color-gtw03-mut: oklch(0.7 0.02 155);
  --color-gtw03-acc: #a3e635;
  --color-gtw03-acc: oklch(0.85 0.2 125);
  --color-gtw03-onacc: #14210a;
  --color-gtw03-onacc: oklch(0.2 0.06 130);
  --font-gtw03-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw03-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}
/* The 382-byte texture token. It stays a custom property, not an @theme entry: it is a payload
   rather than a design-scale value, and utilities read it back with bg-[image:var(--gtw03-noise),…].
   Note the quoting — single quotes inside, double outside — and the four escaped characters. */

.gtw-03 {
  width: 100%;
  min-height: 100svh;
  --gtw03-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='gtw03n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='140' height='140' filter='url(%23gtw03n)' opacity='0.6'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}

.gtw-03:has(.gtw-03-theme:checked) {
  --color-gtw03-bg: #f2f5f0;
  --color-gtw03-bg: oklch(0.96 0.008 145);
  --color-gtw03-surf: #ffffff;
  --color-gtw03-surf: oklch(1 0 0);
  --color-gtw03-line: #d8e0d6;
  --color-gtw03-line: oklch(0.89 0.012 150);
  --color-gtw03-ink: #101211;
  --color-gtw03-ink: oklch(0.19 0.006 150);
  --color-gtw03-mut: #5d6a62;
  --color-gtw03-mut: oklch(0.49 0.015 155);
  --color-gtw03-acc: #4d7c0f;
  --color-gtw03-acc: oklch(0.52 0.14 128);
  --color-gtw03-onacc: #f7fee7;
  --color-gtw03-onacc: oklch(0.98 0.03 120);
}

@media (prefers-color-scheme: light) {
  .gtw-03 {
    --color-gtw03-bg: #f2f5f0;
    --color-gtw03-bg: oklch(0.96 0.008 145);
    --color-gtw03-surf: #ffffff;
    --color-gtw03-surf: oklch(1 0 0);
    --color-gtw03-line: #d8e0d6;
    --color-gtw03-line: oklch(0.89 0.012 150);
    --color-gtw03-ink: #101211;
    --color-gtw03-ink: oklch(0.19 0.006 150);
    --color-gtw03-mut: #5d6a62;
    --color-gtw03-mut: oklch(0.49 0.015 155);
    --color-gtw03-acc: #4d7c0f;
    --color-gtw03-acc: oklch(0.52 0.14 128);
    --color-gtw03-onacc: #f7fee7;
    --color-gtw03-onacc: oklch(0.98 0.03 120);
  }

  .gtw-03:has(.gtw-03-theme:checked) {
    --color-gtw03-bg: #101211;
    --color-gtw03-bg: oklch(0.19 0.006 150);
    --color-gtw03-surf: #191d1b;
    --color-gtw03-surf: oklch(0.24 0.008 155);
    --color-gtw03-line: #2c332f;
    --color-gtw03-line: oklch(0.32 0.01 155);
    --color-gtw03-ink: #eef3ef;
    --color-gtw03-ink: oklch(0.96 0.008 150);
    --color-gtw03-mut: #93a29a;
    --color-gtw03-mut: oklch(0.7 0.02 155);
    --color-gtw03-acc: #a3e635;
    --color-gtw03-acc: oklch(0.85 0.2 125);
    --color-gtw03-onacc: #14210a;
    --color-gtw03-onacc: oklch(0.2 0.06 130);
  }
}

@media (prefers-color-scheme: dark) {
  .gtw-03:has(.gtw-03-theme:checked) {
    --color-gtw03-bg: #f2f5f0;
    --color-gtw03-bg: oklch(0.96 0.008 145);
    --color-gtw03-surf: #ffffff;
    --color-gtw03-surf: oklch(1 0 0);
    --color-gtw03-line: #d8e0d6;
    --color-gtw03-line: oklch(0.89 0.012 150);
    --color-gtw03-ink: #101211;
    --color-gtw03-ink: oklch(0.19 0.006 150);
    --color-gtw03-mut: #5d6a62;
    --color-gtw03-mut: oklch(0.49 0.015 155);
    --color-gtw03-acc: #4d7c0f;
    --color-gtw03-acc: oklch(0.52 0.14 128);
    --color-gtw03-onacc: #f7fee7;
    --color-gtw03-onacc: oklch(0.98 0.03 120);
  }
}
```
