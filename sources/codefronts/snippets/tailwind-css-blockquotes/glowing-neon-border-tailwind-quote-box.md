---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/glowing-neon-border-tailwind-quote-box/"
title: "Glowing Neon Border Tailwind Quote Box"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "A neon sign: a 4-layer cyan box-shadow falloff (tight core → wide bloom → inner cast), matching text-shadow on the quote, a pink pill for the author, and an…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glowing Neon Border Tailwind Quote Box
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/glowing-neon-border-tailwind-quote-box/

A neon sign: a 4-layer cyan box-shadow falloff (tight core → wide bloom → inner cast), matching text-shadow on the quote, a pink pill for the author, and an occasional flicker. The port sets the quote in Tilt Neon — a typeface drawn as bent tubing — and lets hover "turn the power up" with a brighter shadow stack.
## HTML
```html
<section class="tbq-10 w-full min-h-svh grid place-items-center bg-tbq10-bg bg-[radial-gradient(80%_60%_at_50%_30%,var(--color-tbq10-wall),transparent_75%)] px-6 py-16 font-tbq10-sans text-tbq10-ink" aria-label="Neon border quote box demo">
  <div class="grid w-full justify-items-center gap-9">
    <figure class="group grid w-full max-w-[560px] justify-items-center gap-6">
      <div class="w-full animate-tbq10-flicker rounded-[18px] border-2 border-tbq10-cyan bg-tbq10-panel p-[clamp(26px,4.5vw,40px)] shadow-[0_0_6px_oklch(0.8_0.16_195/0.9),0_0_18px_oklch(0.75_0.17_195/0.5),0_0_46px_oklch(0.7_0.18_195/0.3),inset_0_0_14px_oklch(0.8_0.16_195/0.22)] transition-shadow duration-500 group-hover:shadow-[0_0_8px_oklch(0.88_0.15_195),0_0_26px_oklch(0.8_0.17_195/0.7),0_0_72px_oklch(0.72_0.18_195/0.45),inset_0_0_24px_oklch(0.8_0.16_195/0.32)] motion-reduce:animate-none">
        <p aria-hidden="true" class="mb-4 flex items-center gap-2.5 font-tbq10-mono text-[11px] font-bold tracking-[0.34em] text-tbq10-cyan [text-shadow:0_0_8px_oklch(0.8_0.16_195/0.8)]"><span class="size-1.5 rounded-full bg-tbq10-cyan shadow-[0_0_8px_var(--color-tbq10-cyan)]"></span>OPEN · EST 2026</p>
        <blockquote>
          <p class="font-tbq10-neon text-[clamp(26px,3.6vw,38px)] leading-[1.22] tracking-[-0.005em] text-balance [text-shadow:0_0_4px_oklch(0.9_0.1_195/0.9),0_0_14px_oklch(0.8_0.16_195/0.55),0_0_34px_oklch(0.75_0.17_195/0.3)]">The future is already here — it's just not evenly distributed.</p>
        </blockquote>
      </div>
      <figcaption class="rounded-full border-[1.5px] border-tbq10-pink px-4.5 py-2.5 font-tbq10-neon text-sm tracking-[0.3em] text-tbq10-pink shadow-[0_0_6px_oklch(0.75_0.17_350/0.7),0_0_20px_oklch(0.7_0.18_350/0.35),inset_0_0_10px_oklch(0.75_0.17_350/0.18)] [text-shadow:0_0_8px_oklch(0.75_0.17_350/0.8)]">WILLIAM GIBSON</figcaption>
    </figure>
    <p aria-hidden="true" class="rounded-full border border-white/12 px-3.5 py-2 font-tbq10-mono text-[11.5px] text-tbq10-mut">4-layer shadow falloff · [text-shadow:…] · hover powers up</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq10-bg: #06060f;
  --color-tbq10-bg: oklch(0.13 0.02 280);
  --color-tbq10-wall: #101125;
  --color-tbq10-wall: oklch(0.19 0.04 280);
  --color-tbq10-panel: #060b16a6;
  --color-tbq10-panel: oklch(0.15 0.025 265 / 0.65);
  --color-tbq10-ink: #eef7f7;
  --color-tbq10-ink: oklch(0.97 0.01 195);
  --color-tbq10-cyan: #00ebec;
  --color-tbq10-cyan: oklch(0.85 0.15 195);
  --color-tbq10-pink: #ff90cc;
  --color-tbq10-pink: oklch(0.8 0.16 350);
  --color-tbq10-mut: #94a8b6;
  --color-tbq10-mut: oklch(0.72 0.03 240);
  --font-tbq10-neon: 'Tilt Neon', system-ui, sans-serif;
  --font-tbq10-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tbq10-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tbq10-flicker: tbq10-flicker 8s linear infinite;

  @keyframes tbq10-flicker {
    0%,
        41%,
        43%,
        78%,
        80%,
        100% {
      opacity: 1;
    }

    42% {
      opacity: 0.62;
    }

    79% {
      opacity: 0.74;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-10 {
  width: 100%;
  min-height: 100svh;
}
```
