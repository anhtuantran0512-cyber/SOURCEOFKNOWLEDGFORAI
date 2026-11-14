---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-css-animated-underline-hover-effect/"
title: "Tailwind CSS Animated Underline Hover Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "Four navbar underlines in one class list each: grow left→right, bloom from center, slide-through (enters left, exits right) and the native underline that…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Animated Underline Hover Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-css-animated-underline-hover-effect/

Four navbar underlines in one class list each: grow left→right, bloom from center, slide-through (enters left, exits right) and the native underline that docks onto the text with underline-offset. The first three are a single gradient sized with bg-[length:0%_0.09em] → hover:bg-[length:100%_0.09em], so links that wrap underline every line.
## HTML
```html
<section class="tth-01 @container w-full min-h-svh grid place-items-center bg-tth01-bg bg-[radial-gradient(110%_80%_at_50%_0%,var(--color-tth01-glow),transparent_70%)] px-5 py-14 font-tth01-sans text-tth01-ink" aria-label="Animated underline on hover demo">
  <div class="flex w-full max-w-[49rem] flex-col gap-7">
    <header class="flex items-center justify-between gap-4 border-b-[1.5px] border-tth01-ink pb-4">
      <a id="tth01-top" href="#tth01-top" class="rounded-sm text-[15px] font-extrabold uppercase tracking-[0.05em] no-underline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tth01-acc">Ledger<span class="text-tth01-acc">&amp;</span>Loom</a>
      <span class="whitespace-nowrap rounded-full border border-tth01-acc/45 px-3 py-1.5 font-tth01-mono text-[11px] font-semibold text-tth01-acc @max-[35rem]:hidden">bg-[length:0%] &rarr; 100%</span>
    </header>
    <nav aria-label="Underline animation styles">
      <div class="grid grid-cols-[10.5rem_1fr] items-baseline gap-x-6 gap-y-1.5 border-b border-tth01-line py-4 @max-[35rem]:grid-cols-1">
        <span class="font-tth01-mono text-[10.5px] uppercase tracking-[0.1em] text-tth01-mut">01 &middot; left &rarr; right</span>
        <a href="#tth01-top" class="justify-self-start rounded-[2px] pb-[0.12em] text-[clamp(24px,4.6cqi,38px)] font-bold leading-tight tracking-[-0.02em] no-underline bg-[linear-gradient(var(--color-tth01-acc),var(--color-tth01-acc))] bg-no-repeat bg-[length:0%_0.09em] bg-[position:0%_100%] transition-[background-size] duration-450 ease-[cubic-bezier(.22,1,.36,1)] hover:bg-[length:100%_0.09em] focus-visible:bg-[length:100%_0.09em] focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tth01-acc pointer-coarse:bg-[length:100%_0.09em] motion-reduce:transition-none">Selected work</a>
      </div>
      <div class="grid grid-cols-[10.5rem_1fr] items-baseline gap-x-6 gap-y-1.5 border-b border-tth01-line py-4 @max-[35rem]:grid-cols-1">
        <span class="font-tth01-mono text-[10.5px] uppercase tracking-[0.1em] text-tth01-mut">02 &middot; center out</span>
        <a href="#tth01-top" class="justify-self-start rounded-[2px] pb-[0.12em] text-[clamp(24px,4.6cqi,38px)] font-bold leading-tight tracking-[-0.02em] no-underline bg-[linear-gradient(var(--color-tth01-acc),var(--color-tth01-acc))] bg-no-repeat bg-[length:0%_0.09em] bg-[position:50%_100%] transition-[background-size] duration-450 ease-[cubic-bezier(.22,1,.36,1)] hover:bg-[length:100%_0.09em] focus-visible:bg-[length:100%_0.09em] focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tth01-acc pointer-coarse:bg-[length:100%_0.09em] motion-reduce:transition-none">Studio journal</a>
      </div>
      <div class="grid grid-cols-[10.5rem_1fr] items-baseline gap-x-6 gap-y-1.5 border-b border-tth01-line py-4 @max-[35rem]:grid-cols-1">
        <span class="font-tth01-mono text-[10.5px] uppercase tracking-[0.1em] text-tth01-mut">03 &middot; slide through</span>
        <a href="#tth01-top" class="justify-self-start rounded-[2px] pb-[0.12em] text-[clamp(24px,4.6cqi,38px)] font-bold leading-tight tracking-[-0.02em] no-underline bg-[linear-gradient(var(--color-tth01-acc),var(--color-tth01-acc))] bg-no-repeat bg-[length:0%_0.09em] bg-[position:100%_100%] transition-[background-size] duration-450 ease-[cubic-bezier(.22,1,.36,1)] hover:bg-[position:0%_100%] hover:bg-[length:100%_0.09em] focus-visible:bg-[position:0%_100%] focus-visible:bg-[length:100%_0.09em] focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tth01-acc pointer-coarse:bg-[length:100%_0.09em] motion-reduce:transition-none">About the practice</a>
      </div>
      <div class="grid grid-cols-[10.5rem_1fr] items-baseline gap-x-6 gap-y-1.5 border-b border-tth01-line py-4 @max-[35rem]:grid-cols-1">
        <span class="font-tth01-mono text-[10.5px] uppercase tracking-[0.1em] text-tth01-mut">04 &middot; text-decoration</span>
        <a href="#tth01-top" class="justify-self-start rounded-[2px] pb-[0.12em] text-[clamp(24px,4.6cqi,38px)] font-bold leading-tight tracking-[-0.02em] underline decoration-transparent decoration-[0.06em] underline-offset-[0.32em] [text-decoration-skip-ink:auto] transition-[text-decoration-color,text-underline-offset,text-decoration-thickness] duration-350 ease-[cubic-bezier(.22,1,.36,1)] hover:decoration-tth01-acc hover:decoration-[0.1em] hover:underline-offset-[0.14em] focus-visible:decoration-tth01-acc focus-visible:underline-offset-[0.14em] focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tth01-acc pointer-coarse:decoration-tth01-acc motion-reduce:transition-none">Get in touch</a>
      </div>
    </nav>
    <p class="max-w-[58ch] text-[15px] leading-[1.75] text-tth01-mut">Underlines also live inside prose: the <a href="#tth01-top" class="font-semibold text-tth01-ink no-underline bg-[linear-gradient(var(--color-tth01-acc),var(--color-tth01-acc))] bg-no-repeat bg-[position:0_88%] bg-[length:100%_0.14em] transition-[background-size] duration-300 hover:bg-[length:100%_0.6em] focus-visible:bg-[length:100%_0.6em] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth01-acc [--color-tth01-acc:var(--color-tth01-mark)]">type specimens</a> and the <a href="#tth01-top" class="font-semibold text-tth01-ink no-underline bg-[linear-gradient(var(--color-tth01-acc),var(--color-tth01-acc))] bg-no-repeat bg-[position:0_88%] bg-[length:100%_0.14em] transition-[background-size] duration-300 hover:bg-[length:100%_0.6em] focus-visible:bg-[length:100%_0.6em] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth01-acc [--color-tth01-acc:var(--color-tth01-mark)]">2026 grid audit</a> use the same gradient at marker weight &mdash; and because they're real inline links, they keep underlining when they wrap.</p>
    <p class="text-[12.5px] text-tth01-mut">Hover the links &mdash; or press <kbd class="rounded-[5px] border border-b-2 border-tth01-line bg-white px-1.5 py-0.5 font-tth01-mono text-[11px]">Tab</kbd>. Every variant also fires on <code class="rounded bg-tth01-ink/6 px-1.5 py-px font-tth01-mono text-[0.92em]">focus-visible:</code>.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth01-bg: #f8f6ef;
  --color-tth01-bg: oklch(0.975 0.007 95);
  --color-tth01-glow: #fffefa;
  --color-tth01-glow: oklch(0.995 0.004 95);
  --color-tth01-ink: #2a2017;
  --color-tth01-ink: oklch(0.25 0.02 55);
  --color-tth01-mut: #645a51;
  --color-tth01-mut: oklch(0.47 0.02 60);
  --color-tth01-acc: #d2462a;
  --color-tth01-acc: oklch(0.6 0.19 33);
  --color-tth01-mark: #f2c6b8;
  --color-tth01-mark: oklch(0.85 0.07 33);
  --color-tth01-line: #e2ddd2;
  --color-tth01-line: oklch(0.89 0.012 85);
  --font-tth01-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tth01-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well, so the stage is sized before the browser build compiles. */

.tth-01 {
  width: 100%;
  min-height: 100svh;
}
```
