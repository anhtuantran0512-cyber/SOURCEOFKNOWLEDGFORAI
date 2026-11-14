---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-paper-stock-letterpress-press-effect/"
title: "Tailwind Paper Stock and Letterpress Press Effect"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Letterpress in three parts: anisotropic fibre noise for the stock, a two-value text-shadow for the impression, and a deckle edge chewed by feDisplacementMap."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Paper Stock and Letterpress Press Effect
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-paper-stock-letterpress-press-effect/

Letterpress in three parts: anisotropic fibre noise for the stock, a two-value text-shadow for the impression, and a deckle edge chewed by feDisplacementMap. One light source, declared once, shared by the type, the card edges and the paper itself — which is the only reason the effect is convincing.
## HTML
```html
<section class="gtw-16 relative block w-full min-h-svh bg-gtw16-stock text-gtw16-ink" aria-labelledby="gtw-16-title">
  <svg class="absolute w-0 h-0 overflow-hidden" width="0" height="0" aria-hidden="true" focusable="false">
    <filter id="gtw-16-fibre" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.04 0.7" numOctaves="4" seed="14" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
    <filter id="gtw-16-deckle" x="-15%" y="-15%" width="130%" height="130%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.02 0.4" numOctaves="3" seed="7" result="gtw16n"/>
      <feDisplacementMap in="SourceGraphic" in2="gtw16n" scale="9" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </svg>

  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-16-theme" class="gtw-16-theme peer sr-only">
    <label for="gtw-16-theme" class="grid place-items-center w-11 h-11 rounded-full border border-gtw16-line bg-gtw16-stock2 text-gtw16-ink cursor-pointer shadow-[inset_0_1px_0_var(--gtw16-down)] peer-focus-visible:outline-2 peer-focus-visible:outline-gtw16-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="relative z-[1] w-[min(72rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(3rem,8vw,5rem)] pb-[clamp(2.5rem,6vw,4rem)] grid gap-[clamp(2rem,5vw,3rem)]">
    <header class="max-w-[44rem] grid gap-2">
      <p class="m-0 font-gtw16-mono text-[0.72rem] leading-none tracking-[0.18em] uppercase text-gtw16-mut">Stock No. 4 · 600gsm cotton rag</p>
      <h1 id="gtw-16-title" class="m-0 font-gtw16-display text-[clamp(2.4rem,7vw,4.4rem)] font-normal leading-[0.98] tracking-[-0.02em] [text-shadow:0_calc(var(--gtw16-press)*-1)_0_var(--gtw16-up),0_var(--gtw16-press)_0_var(--gtw16-down),0_0_1px_color-mix(in_oklab,var(--color-gtw16-ink)_18%,transparent)]">Pressed, not printed</h1>
      <p class="m-0 max-w-[38rem] text-gtw16-mut text-[clamp(0.95rem,1.9vw,1.06rem)] text-pretty">Directional fibre for the stock, a two-value <code class="font-gtw16-mono text-[0.9em]">text-shadow</code> for the press, and one light source shared by every layer.</p>
    </header>

    <article class="relative p-[clamp(0.5rem,2vw,1rem)]">
      <div class="relative grid justify-items-center gap-[0.7rem] text-center px-[clamp(1.4rem,5vw,3.5rem)] py-[clamp(2.2rem,6vw,4rem)] bg-gtw16-stock2 shadow-[inset_0_1px_0_var(--gtw16-down),0_22px_50px_-30px_oklch(0.3_0.03_70/0.45)] [filter:url(#gtw-16-deckle)]">
        <p aria-hidden="true" class="m-0 text-[1.1rem] text-gtw16-acc">✦</p>
        <p class="m-0 font-gtw16-display text-[clamp(1.6rem,5vw,2.8rem)] font-normal leading-[1.1] tracking-[0.01em] [text-shadow:0_calc(var(--gtw16-press)*-1)_0_var(--gtw16-up),0_var(--gtw16-press)_0_var(--gtw16-down)]">Aleksandra &amp; Tomás</p>
        <h2 class="m-0 max-w-[26rem] text-[clamp(0.95rem,2.2vw,1.15rem)] font-normal leading-[1.5] tracking-[0.06em] lowercase text-gtw16-mut">request the pleasure of your company</h2>
        <p class="mt-[0.3rem] mb-0 font-gtw16-display text-[clamp(1.05rem,2.6vw,1.35rem)] font-normal leading-[1.5] [text-shadow:0_calc(var(--gtw16-press)*-1)_0_var(--gtw16-up),0_var(--gtw16-press)_0_var(--gtw16-down)]">Saturday, the fourteenth of June<br>Two thousand and twenty-seven</p>
        <div aria-hidden="true" class="w-12 h-px bg-gtw16-acc"></div>
        <p class="m-0 font-gtw16-mono text-[0.78rem] leading-[1.6] tracking-[0.14em] uppercase text-gtw16-mut">Bracken Hall · Northumberland · 4 o'clock</p>
      </div>
    </article>

    <div class="grid gap-[clamp(1.2rem,3vw,2rem)] grid-cols-[repeat(auto-fit,minmax(min(100%,18rem),1fr))] items-start">
      <article class="grid content-center gap-[0.4rem] aspect-[85/55] p-[clamp(1.1rem,3vw,1.6rem)] rounded-sm bg-gtw16-stock2 shadow-[inset_0_1px_0_var(--gtw16-down),0_12px_30px_-20px_oklch(0.3_0.03_70/0.4)] transition-[translate,rotate,box-shadow] duration-[380ms] ease-[cubic-bezier(0.22,1,0.36,1)] hover:-translate-y-[3px] hover:-rotate-[0.4deg] motion-reduce:transition-none motion-reduce:hover:translate-y-0 motion-reduce:hover:rotate-0">
        <p class="m-0 font-gtw16-display text-[clamp(1.3rem,3.4vw,1.8rem)] font-normal leading-[1.1] [text-shadow:0_calc(var(--gtw16-press)*-1)_0_var(--gtw16-up),0_var(--gtw16-press)_0_var(--gtw16-down)]">Rowan Ellis</p>
        <p class="m-0 font-gtw16-mono text-[0.72rem] leading-[1.4] tracking-[0.14em] uppercase text-gtw16-acc">Compositor &amp; Press Operator</p>
        <dl class="grid gap-[0.1rem] mt-2 mb-0 pt-[0.6rem] border-t border-gtw16-line">
          <div class="flex gap-2"><dt class="m-0 min-w-[3.4rem] font-gtw16-mono text-[0.7rem] leading-[1.6] tracking-[0.1em] uppercase text-gtw16-mut">Studio</dt><dd class="m-0 text-[0.85rem]">Unit 7, Sackville Yard</dd></div>
          <div class="flex gap-2"><dt class="m-0 min-w-[3.4rem] font-gtw16-mono text-[0.7rem] leading-[1.6] tracking-[0.1em] uppercase text-gtw16-mut">Post</dt><dd class="m-0 text-[0.85rem]">[email protected]</dd></div>
        </dl>
      </article>

      <section class="grid gap-[0.7rem] p-[clamp(1.1rem,3vw,1.7rem)] rounded-sm border border-gtw16-line bg-[color-mix(in_oklab,var(--color-gtw16-stock2)_60%,transparent)]" aria-labelledby="gtw-16-h-spec">
        <h2 id="gtw-16-h-spec" class="m-0 font-gtw16-display text-[clamp(1.2rem,3vw,1.6rem)] font-normal leading-[1.15] [text-shadow:0_calc(var(--gtw16-press)*-1)_0_var(--gtw16-up),0_var(--gtw16-press)_0_var(--gtw16-down)]">Press specification</h2>
        <dl class="grid gap-0 m-0">
          <div class="grid grid-cols-[minmax(6rem,8rem)_minmax(0,1fr)] gap-[0.6rem] py-2 border-t border-gtw16-line"><dt class="m-0 font-gtw16-mono text-[0.7rem] leading-[1.7] tracking-[0.1em] uppercase text-gtw16-mut">Stock</dt><dd class="m-0 text-[0.88rem]">600gsm cotton rag, deckle edge</dd></div>
          <div class="grid grid-cols-[minmax(6rem,8rem)_minmax(0,1fr)] gap-[0.6rem] py-2 border-t border-gtw16-line"><dt class="m-0 font-gtw16-mono text-[0.7rem] leading-[1.7] tracking-[0.1em] uppercase text-gtw16-mut">Fibre</dt><dd class="m-0 text-[0.88rem]">anisotropic turbulence · 0.04 0.7</dd></div>
          <div class="grid grid-cols-[minmax(6rem,8rem)_minmax(0,1fr)] gap-[0.6rem] py-2 border-t border-gtw16-line"><dt class="m-0 font-gtw16-mono text-[0.7rem] leading-[1.7] tracking-[0.1em] uppercase text-gtw16-mut">Impression</dt><dd class="m-0 text-[0.88rem]">text-shadow · 1px above, 1px below</dd></div>
          <div class="grid grid-cols-[minmax(6rem,8rem)_minmax(0,1fr)] gap-[0.6rem] py-2 border-t border-gtw16-line"><dt class="m-0 font-gtw16-mono text-[0.7rem] leading-[1.7] tracking-[0.1em] uppercase text-gtw16-mut">Ink bleed</dt><dd class="m-0 text-[0.88rem]">0 0 1px at 18% ink</dd></div>
          <div class="grid grid-cols-[minmax(6rem,8rem)_minmax(0,1fr)] gap-[0.6rem] py-2 border-t border-gtw16-line"><dt class="m-0 font-gtw16-mono text-[0.7rem] leading-[1.7] tracking-[0.1em] uppercase text-gtw16-mut">Light</dt><dd class="m-0 text-[0.88rem]">above, consistent across all layers</dd></div>
        </dl>
        <p class="m-0 text-gtw16-mut text-[0.83rem] text-pretty">Deboss below 13px hurts legibility. Cap the impression at your body size and drop it entirely for captions.</p>
      </section>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw16-stock: #efe9dc;
  --color-gtw16-stock: oklch(0.92 0.02 84);
  --color-gtw16-stock2: #f8f4ea;
  --color-gtw16-stock2: oklch(0.96 0.015 85);
  --color-gtw16-ink: #221f1a;
  --color-gtw16-ink: oklch(0.24 0.01 70);
  --color-gtw16-mut: #6b6355;
  --color-gtw16-mut: oklch(0.47 0.015 80);
  --color-gtw16-line: #d8cfbc;
  --color-gtw16-line: oklch(0.86 0.02 84);
  --color-gtw16-acc: #8c2f39;
  --color-gtw16-acc: oklch(0.42 0.13 20);
  --font-gtw16-display: 'Instrument Serif', 'Cormorant Garamond', 'Playfair Display', Georgia, serif;
  --font-gtw16-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-16 {
  width: 100%;
  min-height: 100svh;
  --gtw16-press: 1px;
  --gtw16-fibre: 0.06;
  --gtw16-up: rgba(34, 31, 26, 0.24);
  --gtw16-down: rgba(255, 255, 255, 0.92);
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.6;
}
/* The paper itself: a fixed, viewport-covering fibre layer. It is a ::before on the root
   rather than a utility because it must sit behind every child at z-index 0 and never scroll. */

.gtw-16::before {
  content: "";
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  filter: url(#gtw-16-fibre);
  opacity: var(--gtw16-fibre);
  mix-blend-mode: multiply;
}

.gtw-16:has(.gtw-16-theme:checked) {
  --color-gtw16-stock: #171512;
  --color-gtw16-stock: oklch(0.19 0.01 70);
  --color-gtw16-stock2: #201d19;
  --color-gtw16-stock2: oklch(0.24 0.012 70);
  --color-gtw16-ink: #f0e9da;
  --color-gtw16-ink: oklch(0.93 0.02 82);
  --color-gtw16-mut: #a49a86;
  --color-gtw16-mut: oklch(0.7 0.02 82);
  --color-gtw16-line: #322c24;
  --color-gtw16-line: oklch(0.31 0.015 78);
  --color-gtw16-acc: #d9a04a;
  --color-gtw16-acc: oklch(0.75 0.12 74);
  --gtw16-up: rgba(0, 0, 0, 0.6);
  --gtw16-down: rgba(255, 255, 255, 0.14);
  --gtw16-fibre: 0.09;
}

@media (prefers-color-scheme: dark) {
  .gtw-16 {
    --color-gtw16-stock: #171512;
    --color-gtw16-stock: oklch(0.19 0.01 70);
    --color-gtw16-stock2: #201d19;
    --color-gtw16-stock2: oklch(0.24 0.012 70);
    --color-gtw16-ink: #f0e9da;
    --color-gtw16-ink: oklch(0.93 0.02 82);
    --color-gtw16-mut: #a49a86;
    --color-gtw16-mut: oklch(0.7 0.02 82);
    --color-gtw16-line: #322c24;
    --color-gtw16-line: oklch(0.31 0.015 78);
    --color-gtw16-acc: #d9a04a;
    --color-gtw16-acc: oklch(0.75 0.12 74);
    --gtw16-up: rgba(0, 0, 0, 0.6);
    --gtw16-down: rgba(255, 255, 255, 0.14);
    --gtw16-fibre: 0.09;
  }

  .gtw-16:has(.gtw-16-theme:checked) {
    --color-gtw16-stock: #efe9dc;
    --color-gtw16-stock: oklch(0.92 0.02 84);
    --color-gtw16-stock2: #f8f4ea;
    --color-gtw16-stock2: oklch(0.96 0.015 85);
    --color-gtw16-ink: #221f1a;
    --color-gtw16-ink: oklch(0.24 0.01 70);
    --color-gtw16-mut: #6b6355;
    --color-gtw16-mut: oklch(0.47 0.015 80);
    --color-gtw16-line: #d8cfbc;
    --color-gtw16-line: oklch(0.86 0.02 84);
    --color-gtw16-acc: #8c2f39;
    --color-gtw16-acc: oklch(0.42 0.13 20);
    --gtw16-up: rgba(34, 31, 26, 0.24);
    --gtw16-down: rgba(255, 255, 255, 0.92);
    --gtw16-fibre: 0.06;
  }
}

@media (prefers-color-scheme: light) {
  .gtw-16:has(.gtw-16-theme:checked) {
    --color-gtw16-stock: #171512;
    --color-gtw16-stock: oklch(0.19 0.01 70);
    --color-gtw16-stock2: #201d19;
    --color-gtw16-stock2: oklch(0.24 0.012 70);
    --color-gtw16-ink: #f0e9da;
    --color-gtw16-ink: oklch(0.93 0.02 82);
    --color-gtw16-mut: #a49a86;
    --color-gtw16-mut: oklch(0.7 0.02 82);
    --color-gtw16-line: #322c24;
    --color-gtw16-line: oklch(0.31 0.015 78);
    --color-gtw16-acc: #d9a04a;
    --color-gtw16-acc: oklch(0.75 0.12 74);
    --gtw16-up: rgba(0, 0, 0, 0.6);
    --gtw16-down: rgba(255, 255, 255, 0.14);
    --gtw16-fibre: 0.09;
  }
}
```
