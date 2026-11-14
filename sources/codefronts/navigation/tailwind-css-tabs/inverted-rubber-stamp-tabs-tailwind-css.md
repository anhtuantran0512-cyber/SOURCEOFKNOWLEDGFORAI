---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/inverted-rubber-stamp-tabs-tailwind-css/"
title: "Inverted Rubber Stamp Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "A crimson ink bar with cream legends; the chosen tab inverts to crimson-on-cream in a single frame while an inset shadow thumps in and lifts — a rubber stamp…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inverted Rubber Stamp Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/inverted-rubber-stamp-tabs-tailwind-css/

A crimson ink bar with cream legends; the chosen tab inverts to crimson-on-cream in a single frame while an inset shadow thumps in and lifts — a rubber stamp bedding into paper. The port runs the impact from has-checked:animate-ttb23-impact and adds a stamped "filed" mark that lands on the panel.
## HTML
```html
<section class="ttb-23 group/tabs grid min-h-svh w-full place-items-center bg-ttb23-desk px-5 py-14 font-ttb23-mono text-ttb23-ink" aria-label="Inverted rubber stamp tabs demo">
  <div class="grid w-full max-w-xl justify-items-center gap-7">
    <div class="w-full overflow-hidden rounded-lg shadow-[0_18px_40px_-20px_rgb(0_0_0/0.45)]">
      <div role="radiogroup" aria-label="Page" class="flex bg-ttb23-crimson">
        <label class="flex min-h-14 flex-1 cursor-pointer items-center justify-center border-r border-ttb23-cream/25 text-[13px] font-bold tracking-[0.22em] text-ttb23-cream uppercase transition-[background-color,color] duration-50 ease-[steps(1,end)] last:border-r-0 hover:bg-ttb23-cream/10 has-checked:animate-ttb23-impact has-checked:bg-ttb23-cream has-checked:text-ttb23-crimson has-focus-visible:outline-2 has-focus-visible:-outline-offset-6 has-focus-visible:outline-dashed has-focus-visible:outline-current motion-reduce:has-checked:animate-none"><input class="sr-only" type="radio" name="ttb23" id="ttb23-r1" checked>Recto</label>
        <label class="flex min-h-14 flex-1 cursor-pointer items-center justify-center border-r border-ttb23-cream/25 text-[13px] font-bold tracking-[0.22em] text-ttb23-cream uppercase transition-[background-color,color] duration-50 ease-[steps(1,end)] last:border-r-0 hover:bg-ttb23-cream/10 has-checked:animate-ttb23-impact has-checked:bg-ttb23-cream has-checked:text-ttb23-crimson has-focus-visible:outline-2 has-focus-visible:-outline-offset-6 has-focus-visible:outline-dashed has-focus-visible:outline-current motion-reduce:has-checked:animate-none"><input class="sr-only" type="radio" name="ttb23" id="ttb23-r2">Verso</label>
        <label class="flex min-h-14 flex-1 cursor-pointer items-center justify-center text-[13px] font-bold tracking-[0.22em] text-ttb23-cream uppercase transition-[background-color,color] duration-50 ease-[steps(1,end)] hover:bg-ttb23-cream/10 has-checked:animate-ttb23-impact has-checked:bg-ttb23-cream has-checked:text-ttb23-crimson has-focus-visible:outline-2 has-focus-visible:-outline-offset-6 has-focus-visible:outline-dashed has-focus-visible:outline-current motion-reduce:has-checked:animate-none"><input class="sr-only" type="radio" name="ttb23" id="ttb23-r3">Folio</label>
      </div>
      <div class="relative min-h-32 bg-ttb23-cream px-6 py-5 font-ttb23-serif text-[17px] leading-relaxed italic">
        <p class="hidden max-w-[30ch] group-has-[#ttb23-r1:checked]/tabs:block">The right-hand page, traditionally odd-numbered.</p>
        <p class="hidden max-w-[30ch] group-has-[#ttb23-r2:checked]/tabs:block">The left-hand page, traditionally even-numbered.</p>
        <p class="hidden max-w-[30ch] group-has-[#ttb23-r3:checked]/tabs:block">The full leaf — both sides counted as one.</p>
        <span aria-hidden="true" class="absolute right-5 bottom-4 hidden -rotate-8 animate-ttb23-stamp rounded-sm border-2 border-ttb23-crimson/80 px-2 py-0.5 font-ttb23-mono text-[11px] font-bold tracking-[0.2em] text-ttb23-crimson/80 not-italic uppercase group-has-[#ttb23-r1:checked]/tabs:block motion-reduce:animate-none">Filed · R</span>
        <span aria-hidden="true" class="absolute right-5 bottom-4 hidden -rotate-8 animate-ttb23-stamp rounded-sm border-2 border-ttb23-crimson/80 px-2 py-0.5 font-ttb23-mono text-[11px] font-bold tracking-[0.2em] text-ttb23-crimson/80 not-italic uppercase group-has-[#ttb23-r2:checked]/tabs:block motion-reduce:animate-none">Filed · V</span>
        <span aria-hidden="true" class="absolute right-5 bottom-4 hidden -rotate-8 animate-ttb23-stamp rounded-sm border-2 border-ttb23-crimson/80 px-2 py-0.5 font-ttb23-mono text-[11px] font-bold tracking-[0.2em] text-ttb23-crimson/80 not-italic uppercase group-has-[#ttb23-r3:checked]/tabs:block motion-reduce:animate-none">Filed · F</span>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb23-ink/12 bg-ttb23-cream/70 px-3.5 py-2 text-[11.5px] text-ttb23-ash">ease-[steps(1,end)] swap · has-checked:animate-impact · stamp mark</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb23-desk: #e4ddd0;
  --color-ttb23-desk: oklch(0.900 0.019 83.1);
  --color-ttb23-crimson: #c41a33;
  --color-ttb23-crimson: oklch(0.528 0.199 21.4);
  --color-ttb23-cream: #f5ead0;
  --color-ttb23-cream: oklch(0.939 0.036 87.8);
  --color-ttb23-ink: #2a2324;
  --color-ttb23-ink: oklch(0.264 0.011 8.1);
  --color-ttb23-ash: #4a4448;
  --color-ttb23-ash: oklch(0.394 0.010 337.8);
  --font-ttb23-mono: 'Space Mono', ui-monospace, monospace;
  --font-ttb23-serif: 'Newsreader', Georgia, serif;
  --animate-ttb23-impact: ttb23-impact 0.35s cubic-bezier(0.65, 0, 0.35, 1);
  --animate-ttb23-stamp: ttb23-stamp 0.4s cubic-bezier(0.2, 0.9, 0.3, 1.3) both;

  @keyframes ttb23-impact {
    0% {
      box-shadow: inset 0 0 0 0 rgb(0 0 0 / 0.4);
    }

    20% {
      box-shadow: inset 0 4px 14px rgb(0 0 0 / 0.45);
    }

    100% {
      box-shadow: inset 0 0 0 0 rgb(0 0 0 / 0);
    }
  }

  @keyframes ttb23-stamp {
    from {
      scale: 1.6;
      opacity: 0;
    }

    to {
      scale: 1;
      opacity: 1;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-23 {
  width: 100%;
  min-height: 100svh;
}
```
