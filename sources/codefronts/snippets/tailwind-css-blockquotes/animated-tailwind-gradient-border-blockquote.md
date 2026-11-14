---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/animated-tailwind-gradient-border-blockquote/"
title: "Animated Tailwind Gradient Border Blockquote"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "A quote card whose border is a rotating conic gradient, drawn with the two-background padding-box / border-box trick and animated by registering the angle…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Tailwind Gradient Border Blockquote
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/animated-tailwind-gradient-border-blockquote/

A quote card whose border is a rotating conic gradient, drawn with the two-background padding-box / border-box trick and animated by registering the angle with @property. The Tailwind port keeps the keyframes as an --animate-* theme token and adds a blurred glow twin of the border behind the card that brightens on hover.
## HTML
```html
<section class="tbq-06 w-full min-h-svh grid place-items-center bg-tbq06-bg bg-[radial-gradient(70%_55%_at_50%_120%,var(--color-tbq06-glow),transparent)] px-5 py-14 font-tbq06-sans text-tbq06-ink" aria-label="Animated gradient border blockquote demo">
  <div class="isolate grid w-full justify-items-center gap-8">
    <figure class="relative w-full max-w-[520px] animate-tbq06-spin rounded-[20px] border-[1.5px] border-transparent p-[clamp(24px,4vw,36px)] shadow-[0_24px_60px_oklch(0_0_0/0.45)] [background:linear-gradient(var(--color-tbq06-card),var(--color-tbq06-card))_padding-box,conic-gradient(from_var(--tbq06-angle),var(--color-tbq06-c1),var(--color-tbq06-c2),var(--color-tbq06-c3),var(--color-tbq06-c1))_border-box] before:absolute before:-inset-[1.5px] before:-z-10 before:rounded-[inherit] before:opacity-45 before:blur-2xl before:transition-opacity before:duration-500 before:[background:conic-gradient(from_var(--tbq06-angle),var(--color-tbq06-c1),var(--color-tbq06-c2),var(--color-tbq06-c3),var(--color-tbq06-c1))] hover:before:opacity-80 motion-reduce:animate-none">
      <blockquote>
        <p class="text-[clamp(17px,2.2vw,21px)] leading-[1.6] font-medium tracking-[-0.01em] text-pretty">“We shipped the redesign in six weeks. The border animation in this quote card took two of them — and it was worth every hour.”</p>
      </blockquote>
      <figcaption class="mt-5 flex items-center gap-2.5 text-[13.5px] text-tbq06-mut">
        <span aria-hidden="true" class="size-2.5 flex-none rounded-full bg-[conic-gradient(var(--color-tbq06-c1),var(--color-tbq06-c2),var(--color-tbq06-c3),var(--color-tbq06-c1))]"></span>
        <span><strong class="font-semibold text-tbq06-ink">Marcus Webb</strong> · Design Engineer, Meridian</span>
      </figcaption>
    </figure>
    <p aria-hidden="true" class="rounded-full border border-white/12 px-3.5 py-2 font-tbq06-mono text-[11.5px] text-tbq06-mut">@property &lt;angle&gt; · padding-box / border-box · animate-tbq06-spin</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq06-bg: #090b10;
  --color-tbq06-bg: oklch(0.15 0.012 270);
  --color-tbq06-glow: #291c3c80;
  --color-tbq06-glow: oklch(0.26 0.06 300 / 0.5);
  --color-tbq06-card: #13161d;
  --color-tbq06-card: oklch(0.2 0.015 270);
  --color-tbq06-ink: #f0f2f7;
  --color-tbq06-ink: oklch(0.96 0.008 270);
  --color-tbq06-mut: #acb1be;
  --color-tbq06-mut: oklch(0.76 0.02 270);
  --color-tbq06-c1: #fd736d;
  --color-tbq06-c1: oklch(0.72 0.17 25);
  --color-tbq06-c2: #d78de8;
  --color-tbq06-c2: oklch(0.75 0.15 320);
  --color-tbq06-c3: #53a3f2;
  --color-tbq06-c3: oklch(0.7 0.14 250);
  --font-tbq06-sans: 'Geist', system-ui, sans-serif;
  --font-tbq06-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tbq06-spin: tbq06-spin 7s linear infinite;

  @keyframes tbq06-spin {
    to {
      --tbq06-angle: 400deg;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-06 {
  width: 100%;
  min-height: 100svh;
}
/* Registered so the angle interpolates; inherits:true lets the before: glow read the same value. */

@property --tbq06-angle {
  syntax: '<angle>';
  initial-value: 40deg;
  inherits: true;
}
```
