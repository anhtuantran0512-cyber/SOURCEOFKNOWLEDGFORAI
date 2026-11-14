---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-staircase-offset-stacked-cards-cascade/"
title: "Tailwind Staircase Offset Stacked Cards Cascade"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A strict stair-step cascade where one uniform corner of every card stays visible."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Staircase Offset Stacked Cards Cascade
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-staircase-offset-stacked-cards-cascade/

A strict stair-step cascade where one uniform corner of every card stays visible. The whole staircase is a single expression &mdash; [transform:translate(calc(var(--i)*24px),calc(var(--i)*46px))] with [z-index:calc(var(--i)+1)] &mdash; and hovering adds a lateral offset to the same expression, so the step slides out along its own diagonal rather than jumping off it.
## HTML
```html
<section class="stk-13 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk13-sans bg-stk13-bg" aria-label="Staircase cascade of cards">
  <div class="relative w-65 h-70">
    <a class="absolute left-0 top-0 flex h-30 w-47.5 flex-col gap-1.5 rounded-2xl bg-stk13-c1 p-5 text-white no-underline shadow-[0_18px_34px_-20px_rgba(0,0,0,0.8)] [transform:translate(calc(var(--i)*24px),calc(var(--i)*46px))] [z-index:calc(var(--i)+1)] transition-[transform,box-shadow] duration-350 ease-stk13 hover:z-20 hover:shadow-[0_28px_48px_-20px_rgba(0,0,0,0.9)] hover:[transform:translate(calc(var(--i)*24px+40px),calc(var(--i)*46px-8px))] focus-visible:z-20 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_#fff,0_28px_48px_-20px_rgba(0,0,0,0.9)] focus-visible:[transform:translate(calc(var(--i)*24px+40px),calc(var(--i)*46px-8px))] motion-reduce:transition-[box-shadow]" href="#" style="--i:0">
      <b class="text-[19px] font-extrabold tracking-[-0.02em]">Plan</b>
      <span class="font-stk13-mono text-[13px] opacity-90">Scope &amp; milestones</span>
    </a>
    <a class="absolute left-0 top-0 flex h-30 w-47.5 flex-col gap-1.5 rounded-2xl bg-stk13-c2 p-5 text-white no-underline shadow-[0_18px_34px_-20px_rgba(0,0,0,0.8)] [transform:translate(calc(var(--i)*24px),calc(var(--i)*46px))] [z-index:calc(var(--i)+1)] transition-[transform,box-shadow] duration-350 ease-stk13 hover:z-20 hover:shadow-[0_28px_48px_-20px_rgba(0,0,0,0.9)] hover:[transform:translate(calc(var(--i)*24px+40px),calc(var(--i)*46px-8px))] focus-visible:z-20 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_#fff,0_28px_48px_-20px_rgba(0,0,0,0.9)] focus-visible:[transform:translate(calc(var(--i)*24px+40px),calc(var(--i)*46px-8px))] motion-reduce:transition-[box-shadow]" href="#" style="--i:1">
      <b class="text-[19px] font-extrabold tracking-[-0.02em]">Design</b>
      <span class="font-stk13-mono text-[13px] opacity-90">Flows &amp; system</span>
    </a>
    <a class="absolute left-0 top-0 flex h-30 w-47.5 flex-col gap-1.5 rounded-2xl bg-stk13-c3 p-5 text-white no-underline shadow-[0_18px_34px_-20px_rgba(0,0,0,0.8)] [transform:translate(calc(var(--i)*24px),calc(var(--i)*46px))] [z-index:calc(var(--i)+1)] transition-[transform,box-shadow] duration-350 ease-stk13 hover:z-20 hover:shadow-[0_28px_48px_-20px_rgba(0,0,0,0.9)] hover:[transform:translate(calc(var(--i)*24px+40px),calc(var(--i)*46px-8px))] focus-visible:z-20 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_#fff,0_28px_48px_-20px_rgba(0,0,0,0.9)] focus-visible:[transform:translate(calc(var(--i)*24px+40px),calc(var(--i)*46px-8px))] motion-reduce:transition-[box-shadow]" href="#" style="--i:2">
      <b class="text-[19px] font-extrabold tracking-[-0.02em]">Build</b>
      <span class="font-stk13-mono text-[13px] opacity-90">Ship in slices</span>
    </a>
    <a class="absolute left-0 top-0 flex h-30 w-47.5 flex-col gap-1.5 rounded-2xl bg-stk13-c4 p-5 text-stk13-dark no-underline shadow-[0_18px_34px_-20px_rgba(0,0,0,0.8)] [transform:translate(calc(var(--i)*24px),calc(var(--i)*46px))] [z-index:calc(var(--i)+1)] transition-[transform,box-shadow] duration-350 ease-stk13 hover:z-20 hover:shadow-[0_28px_48px_-20px_rgba(0,0,0,0.9)] hover:[transform:translate(calc(var(--i)*24px+40px),calc(var(--i)*46px-8px))] focus-visible:z-20 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_#fff,0_28px_48px_-20px_rgba(0,0,0,0.9)] focus-visible:[transform:translate(calc(var(--i)*24px+40px),calc(var(--i)*46px-8px))] motion-reduce:transition-[box-shadow]" href="#" style="--i:3">
      <b class="text-[19px] font-extrabold tracking-[-0.02em]">Launch</b>
      <span class="font-stk13-mono text-[13px] opacity-80">Measure &amp; iterate</span>
    </a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk13-bg: #12141c;
  --color-stk13-bg: oklch(0.21 0.014 275);
  --color-stk13-dark: #1a1508;
  --color-stk13-dark: oklch(0.24 0.030 85);
  --color-stk13-c1: #5f7ae0;
  --color-stk13-c1: oklch(0.60 0.16 265);
  --color-stk13-c2: #4a94cc;
  --color-stk13-c2: oklch(0.62 0.15 210);
  --color-stk13-c3: #3fae8c;
  --color-stk13-c3: oklch(0.64 0.15 160);
  --color-stk13-c4: #d0b23a;
  --color-stk13-c4: oklch(0.78 0.16 90);
  --font-stk13-sans: 'Archivo', system-ui, sans-serif;
  --font-stk13-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-stk13: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
