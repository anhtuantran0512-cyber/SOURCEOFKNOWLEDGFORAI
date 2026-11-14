---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/speech-bubble-tailwind-blockquote/"
title: "Speech Bubble Tailwind Blockquote"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "Two speech-bubble tails side by side: the classic zero-size border triangle (after:border-[11px] after:border-r-tbq12-bubble) and a clip-path polygon that…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Speech Bubble Tailwind Blockquote
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/speech-bubble-tailwind-blockquote/

Two speech-bubble tails side by side: the classic zero-size border triangle (after:border-[11px] after:border-r-tbq12-bubble) and a clip-path polygon that can carry the bubble's gradient. The port adds what every chat UI needs next — messages that slide in with the starting: variant (@starting-style) and a typing indicator.
## HTML
```html
<section class="tbq-12 w-full min-h-svh grid place-items-center bg-linear-to-b from-tbq12-top to-tbq12-bg px-5 py-14 font-tbq12-sans text-tbq12-ink" aria-label="Speech bubble blockquote demo">
  <div class="grid w-full justify-items-center gap-8">
    <div class="flex w-full max-w-[560px] flex-col gap-5.5">
      <figure class="flex items-end gap-3 drop-shadow-[0_6px_14px_oklch(0.3_0.03_260/0.16)] transition-[opacity,translate] duration-500 starting:translate-y-2 starting:opacity-0 motion-reduce:transition-none">
        <img class="size-10 flex-none rounded-full bg-linear-135 from-tbq12-av1 to-tbq12-av2 object-cover" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=120&auto=format&fit=crop" alt="" width="40" height="40" loading="lazy">
        <div class="max-w-[76%]">
          <blockquote class="relative rounded-[18px_18px_18px_6px] bg-tbq12-bubble px-4.5 py-3.5 text-[14.5px] leading-[1.58] after:absolute after:bottom-2.5 after:-left-2.5 after:border-[11px] after:border-l-0 after:border-transparent after:border-r-tbq12-bubble">
            <p class="text-pretty">The tail on this bubble is the old border trick — a zero-size box where only one border edge is painted. Works in literally every browser.</p>
          </blockquote>
          <figcaption class="mt-1.5 font-tbq12-mono text-[11.5px] text-tbq12-mut">Devon · border-r-color tail</figcaption>
        </div>
      </figure>
      <figure class="flex items-end justify-end gap-3 drop-shadow-[0_6px_14px_oklch(0.3_0.03_260/0.16)] transition-[opacity,translate] delay-200 duration-500 starting:translate-y-2 starting:opacity-0 motion-reduce:transition-none">
        <div class="max-w-[76%]">
          <blockquote class="relative rounded-[18px_18px_6px_18px] bg-linear-135 from-tbq12-b2a to-tbq12-b2b px-4.5 py-3.5 text-[14.5px] leading-[1.58] text-white after:absolute after:-right-[11px] after:bottom-2 after:h-4.5 after:w-3.5 after:bg-tbq12-b2b after:[clip-path:polygon(0_0,100%_78%,0_100%)]">
            <p class="text-pretty">And this one is clip-path — the tail carries the bubble's gradient, which borders can't do. Any polygon you can imagine.</p>
          </blockquote>
          <figcaption class="mt-1.5 text-right font-tbq12-mono text-[11.5px] text-tbq12-mut">Ana · clip-path polygon tail</figcaption>
        </div>
        <img class="size-10 flex-none rounded-full bg-linear-135 from-tbq12-av2 to-tbq12-av1 object-cover" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=120&auto=format&fit=crop" alt="" width="40" height="40" loading="lazy">
      </figure>
      <div role="status" aria-label="Devon is typing" class="flex items-end gap-3 drop-shadow-[0_6px_14px_oklch(0.3_0.03_260/0.12)] transition-opacity delay-700 duration-500 starting:opacity-0 motion-reduce:transition-none">
        <span aria-hidden="true" class="size-10 flex-none"></span>
        <span aria-hidden="true" class="flex items-center gap-1 rounded-[18px_18px_18px_6px] bg-tbq12-bubble px-4 py-3.5">
          <i class="size-1.5 animate-tbq12-typing rounded-full bg-tbq12-mut motion-reduce:animate-none"></i>
          <i class="size-1.5 animate-tbq12-typing rounded-full bg-tbq12-mut [animation-delay:0.15s] motion-reduce:animate-none"></i>
          <i class="size-1.5 animate-tbq12-typing rounded-full bg-tbq12-mut [animation-delay:0.3s] motion-reduce:animate-none"></i>
        </span>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-black/10 bg-white px-3.5 py-2 font-tbq12-mono text-[11.5px] text-tbq12-mut">border-triangle vs clip-path tails · drop-shadow · starting:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq12-bg: #eef2f7;
  --color-tbq12-bg: oklch(0.96 0.008 250);
  --color-tbq12-top: #f0f8fc;
  --color-tbq12-top: oklch(0.975 0.01 230);
  --color-tbq12-ink: #1b1f27;
  --color-tbq12-ink: oklch(0.24 0.015 260);
  --color-tbq12-mut: #5e646c;
  --color-tbq12-mut: oklch(0.5 0.015 260);
  --color-tbq12-bubble: #ffffff;
  --color-tbq12-bubble: oklch(1 0 0);
  --color-tbq12-b2a: #2773ee;
  --color-tbq12-b2a: oklch(0.58 0.2 260);
  --color-tbq12-b2b: #6d44d6;
  --color-tbq12-b2b: oklch(0.52 0.21 290);
  --color-tbq12-av1: #6da3da;
  --color-tbq12-av1: oklch(0.7 0.1 250);
  --color-tbq12-av2: #7b63a3;
  --color-tbq12-av2: oklch(0.55 0.1 300);
  --font-tbq12-sans: 'Geist', system-ui, sans-serif;
  --font-tbq12-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tbq12-typing: tbq12-typing 1.2s ease-in-out infinite;

  @keyframes tbq12-typing {
    0%,
        60%,
        100% {
      opacity: 0.35;
      translate: 0 0;
    }

    30% {
      opacity: 1;
      translate: 0 -3px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-12 {
  width: 100%;
  min-height: 100svh;
}
```
