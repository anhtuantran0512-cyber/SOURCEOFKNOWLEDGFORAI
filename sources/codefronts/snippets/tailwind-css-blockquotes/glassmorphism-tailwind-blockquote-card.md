---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/glassmorphism-tailwind-blockquote-card/"
title: "Glassmorphism Tailwind Blockquote Card"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "Frosted-glass quote over drifting colour orbs."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Tailwind Blockquote Card
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/glassmorphism-tailwind-blockquote-card/

Frosted-glass quote over drifting colour orbs. The port turns the original's @supports block into supports-[backdrop-filter:blur(1px)]: variants — so the opaque fallback and the frosted version are both visible in one class list — and adds a specular top-edge highlight that sells the glass.
## HTML
```html
<section class="tbq-09 relative w-full min-h-svh grid place-items-center overflow-hidden bg-linear-135 from-tbq09-g1 via-tbq09-g2 via-55% to-tbq09-g3 px-5 py-14 font-tbq09-sans text-tbq09-ink" aria-label="Glassmorphism blockquote card demo">
  <div aria-hidden="true" class="absolute top-[14%] left-[12%] size-70 animate-tbq09-drift rounded-full bg-[radial-gradient(circle_at_32%_30%,var(--color-tbq09-o1a),var(--color-tbq09-o1b))] blur-[2px] motion-reduce:animate-none"></div>
  <div aria-hidden="true" class="absolute top-[22%] right-[14%] size-48 animate-tbq09-drift rounded-full bg-[radial-gradient(circle_at_35%_30%,var(--color-tbq09-o2a),var(--color-tbq09-o2b))] blur-[2px] [animation-direction:alternate-reverse] [animation-duration:13s] motion-reduce:animate-none"></div>
  <div aria-hidden="true" class="absolute bottom-[8%] left-[38%] size-58 animate-tbq09-drift rounded-full bg-[radial-gradient(circle_at_30%_30%,var(--color-tbq09-o3a),var(--color-tbq09-o3b))] blur-[2px] [animation-duration:19s] motion-reduce:animate-none"></div>
  <div class="relative grid w-full justify-items-center gap-8">
    <figure class="relative w-full max-w-[520px] rounded-[22px] border border-white/28 bg-tbq09-fallback p-[clamp(26px,4vw,38px)] shadow-[inset_0_1px_0_oklch(1_0_0/0.32),0_24px_50px_oklch(0_0_0/0.35)] before:pointer-events-none before:absolute before:inset-x-8 before:top-0 before:h-px before:bg-linear-to-r before:from-transparent before:via-white/80 before:to-transparent supports-[backdrop-filter:blur(1px)]:bg-white/10 supports-[backdrop-filter:blur(1px)]:backdrop-blur-[18px] supports-[backdrop-filter:blur(1px)]:backdrop-saturate-160">
      <blockquote>
        <p class="text-[clamp(18px,2.4vw,23px)] leading-[1.55] font-semibold tracking-[-0.012em] text-balance [text-shadow:0_1px_2px_oklch(0_0_0/0.2)]">“Good abstractions are like frosted glass — they hide the machinery without pretending it isn't there.”</p>
      </blockquote>
      <figcaption class="mt-6 flex items-center gap-3.5 text-[13.5px] leading-[1.45] text-tbq09-mut">
        <span aria-hidden="true" class="grid size-11 flex-none place-items-center rounded-full border border-white/35 bg-white/20 text-[13px] font-extrabold text-tbq09-ink">LN</span>
        <span><strong class="block text-sm font-bold text-tbq09-ink">Lena Novak</strong>Staff Engineer, Praxis Cloud</span>
      </figcaption>
    </figure>
    <p aria-hidden="true" class="rounded-full border border-white/25 bg-white/14 px-3.5 py-2 font-tbq09-mono text-[11.5px] text-tbq09-ink">supports-[backdrop-filter]: · backdrop-blur-[18px] · backdrop-saturate-160</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq09-g1: #583da6;
  --color-tbq09-g1: oklch(0.45 0.16 290);
  --color-tbq09-g2: #b43694;
  --color-tbq09-g2: oklch(0.55 0.19 340);
  --color-tbq09-g3: #eb883b;
  --color-tbq09-g3: oklch(0.72 0.15 55);
  --color-tbq09-fallback: #3f3355;
  --color-tbq09-fallback: oklch(0.35 0.06 300);
  --color-tbq09-ink: #fafcff;
  --color-tbq09-ink: oklch(0.99 0.004 260);
  --color-tbq09-mut: #eef3fb;
  --color-tbq09-mut: oklch(0.96 0.015 260);
  --color-tbq09-o1a: #58e5ed;
  --color-tbq09-o1a: oklch(0.85 0.12 200);
  --color-tbq09-o1b: #0082e6;
  --color-tbq09-o1b: oklch(0.6 0.18 250);
  --color-tbq09-o2a: #f9dd73;
  --color-tbq09-o2a: oklch(0.9 0.13 95);
  --color-tbq09-o2b: #fe6652;
  --color-tbq09-o2b: oklch(0.7 0.19 30);
  --color-tbq09-o3a: #fec0f7;
  --color-tbq09-o3a: oklch(0.88 0.1 330);
  --color-tbq09-o3b: #9543c6;
  --color-tbq09-o3b: oklch(0.55 0.2 310);
  --font-tbq09-sans: 'Geist', system-ui, sans-serif;
  --font-tbq09-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tbq09-drift: tbq09-drift 16s ease-in-out infinite alternate;

  @keyframes tbq09-drift {
    from {
      translate: 0 0;
    }

    to {
      translate: 60px -40px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-09 {
  width: 100%;
  min-height: 100svh;
}
```
