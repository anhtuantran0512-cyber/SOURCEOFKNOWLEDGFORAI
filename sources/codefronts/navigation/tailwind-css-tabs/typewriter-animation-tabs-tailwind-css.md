---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/typewriter-animation-tabs-tailwind-css/"
title: "Typewriter Animation Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Choosing a tab types the panel's line out character by character, then leaves a blinking amber caret."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Typewriter Animation Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/typewriter-animation-tabs-tailwind-css/

Choosing a tab types the panel's line out character by character, then leaves a blinking amber caret. The original's steps(20) was a magic number that only fit one string; the port gives each line its own [--n:16] and animates to calc(var(--n)*1ch) in exactly steps(var(--n)), so any string types one glyph per step.
## HTML
```html
<section class="ttb-11 group/tabs grid min-h-svh w-full place-items-center bg-ttb11-bg px-5 py-14 font-ttb11-mono text-ttb11-ink" aria-label="Typewriter animation tabs demo">
  <div class="grid w-full max-w-lg justify-items-center gap-7">
    <div class="w-full rounded-2xl bg-ttb11-card p-2 ring-1 ring-white/8">
      <div role="radiogroup" aria-label="Message" class="flex gap-1 rounded-xl bg-black/25 p-1">
        <label class="flex min-h-10 flex-1 cursor-pointer items-center justify-center rounded-lg text-[11px] font-semibold tracking-[0.12em] text-ttb11-mut uppercase transition-colors hover:text-ttb11-ink has-checked:bg-ttb11-amber/12 has-checked:text-ttb11-amber has-focus-visible:outline-1 has-focus-visible:-outline-offset-2 has-focus-visible:outline-dashed has-focus-visible:outline-ttb11-amber"><input class="sr-only" type="radio" name="ttb11" id="ttb11-r1" checked>Greet</label>
        <label class="flex min-h-10 flex-1 cursor-pointer items-center justify-center rounded-lg text-[11px] font-semibold tracking-[0.12em] text-ttb11-mut uppercase transition-colors hover:text-ttb11-ink has-checked:bg-ttb11-amber/12 has-checked:text-ttb11-amber has-focus-visible:outline-1 has-focus-visible:-outline-offset-2 has-focus-visible:outline-dashed has-focus-visible:outline-ttb11-amber"><input class="sr-only" type="radio" name="ttb11" id="ttb11-r2">Status</label>
        <label class="flex min-h-10 flex-1 cursor-pointer items-center justify-center rounded-lg text-[11px] font-semibold tracking-[0.12em] text-ttb11-mut uppercase transition-colors hover:text-ttb11-ink has-checked:bg-ttb11-amber/12 has-checked:text-ttb11-amber has-focus-visible:outline-1 has-focus-visible:-outline-offset-2 has-focus-visible:outline-dashed has-focus-visible:outline-ttb11-amber"><input class="sr-only" type="radio" name="ttb11" id="ttb11-r3">Goodbye</label>
      </div>
      <div class="flex min-h-24 items-center px-4 text-lg">
        <p class="hidden group-has-[#ttb11-r1:checked]/tabs:block"><span aria-hidden="true" class="mr-2 text-ttb11-dim">›</span><span class="inline-block w-[calc(var(--n)*1ch)] animate-ttb11-type overflow-hidden border-r-2 border-ttb11-amber align-bottom whitespace-nowrap text-ttb11-amber [--n:14] motion-reduce:animate-none">Hello, friend.</span></p>
        <p class="hidden group-has-[#ttb11-r2:checked]/tabs:block"><span aria-hidden="true" class="mr-2 text-ttb11-dim">›</span><span class="inline-block w-[calc(var(--n)*1ch)] animate-ttb11-type overflow-hidden border-r-2 border-ttb11-amber align-bottom whitespace-nowrap text-ttb11-amber [--n:16] motion-reduce:animate-none">Systems nominal.</span></p>
        <p class="hidden group-has-[#ttb11-r3:checked]/tabs:block"><span aria-hidden="true" class="mr-2 text-ttb11-dim">›</span><span class="inline-block w-[calc(var(--n)*1ch)] animate-ttb11-type overflow-hidden border-r-2 border-ttb11-amber align-bottom whitespace-nowrap text-ttb11-amber [--n:17] motion-reduce:animate-none">See you tomorrow.</span></p>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/10 px-3.5 py-2 text-[11.5px] text-ttb11-mut">[--n:16] · w-[calc(var(--n)*1ch)] · steps(var(--n))</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb11-bg: #17121f;
  --color-ttb11-bg: oklch(0.195 0.027 301.6);
  --color-ttb11-card: #211a2c;
  --color-ttb11-card: oklch(0.235 0.035 301.6);
  --color-ttb11-ink: #f3eff8;
  --color-ttb11-ink: oklch(0.958 0.013 306.0);
  --color-ttb11-mut: #a99fb8;
  --color-ttb11-mut: oklch(0.719 0.037 303.6);
  --color-ttb11-dim: #8b7f9c;
  --color-ttb11-dim: oklch(0.617 0.045 303.9);
  --color-ttb11-amber: #fbbf24;
  --color-ttb11-amber: oklch(0.837 0.164 84.4);
  --font-ttb11-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ttb11-type: ttb11-type 1.2s steps(var(--n)) both, ttb11-blink 0.8s step-end 1.2s infinite;

  @keyframes ttb11-type {
    from {
      width: 0;
    }
  }

  @keyframes ttb11-blink {
    50% {
      border-color: transparent;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-11 {
  width: 100%;
  min-height: 100svh;
}
```
