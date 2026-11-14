---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-scroll-triggered-button-stroke-with-animation-timeline/"
title: "Tailwind Scroll Triggered Button Stroke with animation-timeline"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "Scroll-driven strokes with no observer and no listener &mdash; the timeline and range are arbitrary properties, [animation-timeline:view()] and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scroll Triggered Button Stroke with animation-timeline
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-scroll-triggered-button-stroke-with-animation-timeline/

Scroll-driven strokes with no observer and no listener &mdash; the timeline and range are arbitrary properties, [animation-timeline:view()] and [animation-range:entry_100%_contain_55%], which turns out to be the readable form: the two CTAs differ by exactly one class, so you can compare their ranges without opening a stylesheet. The @supports not block stays in CSS and is what makes this safe to ship.
## HTML
```html
<section class="svgb-17 relative block w-full min-h-svh bg-svgb17-bg text-svgb17-fg font-svgb17-serif">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-17-theme">
  <label class="absolute z-[6] top-4 right-[22px] grid place-items-center size-11 rounded-full border border-current/20 bg-current/8 backdrop-blur-lg cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/15 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-17-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="h-svh overflow-y-auto overflow-x-hidden [scrollbar-width:thin] [scrollbar-color:var(--color-svgb17-rest)_transparent]">
    <div class="sticky z-[4] top-[calc(100svh-76px)] left-[clamp(16px,4vw,40px)] size-14 -mb-14 [&>svg]:w-full [&>svg]:h-full [&>svg]:overflow-visible [&>svg]:-rotate-90 [&_circle]:fill-none" aria-hidden="true">
      <svg viewBox="0 0 56 56">
        <circle class="stroke-svgb17-rest [stroke-width:2]" cx="28" cy="28" r="25" pathLength="1"/>
        <circle class="svgb-17__mfill stroke-svgb17-stroke [stroke-width:2.6] [stroke-linecap:round] [stroke-dasharray:1] [stroke-dashoffset:1] animate-svgb17-read [animation-timeline:scroll(nearest_block)]" cx="28" cy="28" r="25" pathLength="1"/>
      </svg>
    </div>
    <article class="max-w-[62ch] mx-auto px-[clamp(22px,6vw,40px)] pt-[clamp(48px,12vh,120px)] pb-[clamp(160px,34vh,340px)] flex flex-col gap-5">
      <p class="m-0 font-svgb17-sans text-[11px] tracking-[0.24em] uppercase text-svgb17-stroke">Craft &middot; Issue 04</p>
      <h1 class="m-0 text-[clamp(38px,7vw,68px)] font-normal leading-[1.02] tracking-[-0.03em] text-balance">The line that draws itself</h1>
      <p class="m-0 text-[clamp(19px,2.4vw,24px)] leading-[1.5] text-svgb17-fg/82">Scroll-driven animation moved a whole category of interaction out of JavaScript and into the style sheet. What it changed is not the effect &mdash; it is who owns the clock.</p>

      <p class="m-0 text-lg leading-[1.66] text-pretty [&_code]:font-mono [&_code]:text-[0.86em] [&_code]:px-[5px] [&_code]:py-px [&_code]:rounded [&_code]:bg-svgb17-fg/7">For a decade the recipe was fixed: observe the element, add a class, let a transition run. It worked, and it always carried the same three costs &mdash; a listener, a layout read, and a state that the browser could not reason about.</p>
      <p class="m-0 text-lg leading-[1.66] text-pretty [&_code]:font-mono [&_code]:text-[0.86em] [&_code]:px-[5px] [&_code]:py-px [&_code]:rounded [&_code]:bg-svgb17-fg/7">A view timeline replaces all three with a declaration. The element's progress through the scrollport <em>is</em> the animation's time, so scrolling backwards runs it backwards, and nothing has to be told when to start.</p>

      <div class="flex flex-wrap items-center gap-4 py-2.5">
        <button class="relative w-[min(300px,100%)] h-[62px] grid place-items-center border-0 p-0 rounded-md bg-svgb17-stroke/7 text-inherit font-svgb17-sans text-[15px] font-medium cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb17-stroke focus-visible:outline-offset-4" type="button">
          <svg class="absolute inset-0 w-full h-full overflow-visible [&_rect]:fill-none [&_rect]:[stroke-linecap:round]" viewBox="0 0 300 62" aria-hidden="true">
            <rect class="stroke-svgb17-rest [stroke-width:1.4]" x="2" y="2" width="296" height="58" rx="6" pathLength="1"/>
            <rect class="svgb-17__ink stroke-svgb17-stroke [stroke-width:2.2] [stroke-dasharray:1] [stroke-dashoffset:1] animate-svgb17-draw [animation-timeline:view()] [animation-range:entry_100%_contain_55%]" x="2" y="2" width="296" height="58" rx="6" pathLength="1"/>
          </svg>
          <span class="relative z-[1]">Read the spec notes</span>
        </button>
        <span class="font-svgb17-sans text-[11px] tracking-[0.06em] text-svgb17-muted">entry 100% &rarr; contain 55%</span>
      </div>

      <p class="m-0 text-lg leading-[1.66] text-pretty [&_code]:font-mono [&_code]:text-[0.86em] [&_code]:px-[5px] [&_code]:py-px [&_code]:rounded [&_code]:bg-svgb17-fg/7">The range is the design decision. Begin at <code>entry 100%</code> &mdash; the instant the button is wholly inside the scrollport, never a pixel earlier &mdash; and finish at <code>contain 55%</code>, while it still sits well inside the viewport. The whole draw happens where the reader is actually looking.</p>
      <blockquote class="my-2.5 ps-[22px] border-s-2 border-svgb17-stroke text-[clamp(20px,2.6vw,26px)] italic leading-[1.4]">A reveal that finishes late reads as a bug, because the reader is already looking at the thing you are still animating.</blockquote>
      <p class="m-0 text-lg leading-[1.66] text-pretty [&_code]:font-mono [&_code]:text-[0.86em] [&_code]:px-[5px] [&_code]:py-px [&_code]:rounded [&_code]:bg-svgb17-fg/7">Fill mode is the part that catches everyone. Without <code>both</code>, the animation applies only inside its range and the border reverts the moment you scroll past it.</p>

      <div class="flex flex-wrap items-center gap-4 py-2.5">
        <button class="relative w-[min(300px,100%)] h-[62px] grid place-items-center border-0 p-0 rounded-md bg-svgb17-stroke/7 text-inherit font-svgb17-sans text-[15px] font-medium cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb17-stroke focus-visible:outline-offset-4" type="button">
          <svg class="absolute inset-0 w-full h-full overflow-visible [&_rect]:fill-none [&_rect]:[stroke-linecap:round]" viewBox="0 0 300 62" aria-hidden="true">
            <rect class="stroke-svgb17-rest [stroke-width:1.4]" x="2" y="2" width="296" height="58" rx="6" pathLength="1"/>
            <rect class="svgb-17__ink stroke-svgb17-stroke [stroke-width:2.2] [stroke-dasharray:1] [stroke-dashoffset:1] animate-svgb17-draw [animation-timeline:view()] [animation-range:contain_10%_contain_50%]" x="2" y="2" width="296" height="58" rx="6" pathLength="1"/>
          </svg>
          <span class="relative z-[1]">Subscribe to Craft</span>
        </button>
        <span class="font-svgb17-sans text-[11px] tracking-[0.06em] text-svgb17-muted">contain 10% &rarr; contain 50%</span>
      </div>

      <p class="m-0 text-lg leading-[1.66] text-pretty [&_code]:font-mono [&_code]:text-[0.86em] [&_code]:px-[5px] [&_code]:py-px [&_code]:rounded [&_code]:bg-svgb17-fg/7">Everything here degrades to a plain, fully drawn border where scroll-driven animation is unavailable &mdash; and to the same finished state for anyone who has asked for reduced motion.</p>
      <p class="mt-[18px] mb-0 text-svgb17-muted">&#9633;</p>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb17-bg: #f6f4ef;
  --color-svgb17-bg: oklch(0.968 0.008 85);
  --color-svgb17-fg: #17161c;
  --color-svgb17-fg: oklch(0.20 0.008 285);
  --color-svgb17-muted: #6b6875;
  --color-svgb17-muted: oklch(0.555 0.014 285);
  --color-svgb17-rest: rgba(23, 22, 28, 0.16);
  --color-svgb17-rest: oklch(0.20 0.008 285 / 0.16);
  --color-svgb17-stroke: #a8320f;
  --color-svgb17-stroke: oklch(0.48 0.17 38);
  --font-svgb17-serif: 'Newsreader', ui-serif, Georgia, serif;
  --font-svgb17-sans: 'Archivo', system-ui, sans-serif;
  /* No duration and no iteration count: a scroll-driven animation takes its
       time from the timeline, and 'both' is what holds the end state. */
  --animate-svgb17-draw: svgb17-draw linear both;
  --animate-svgb17-read: svgb17-read linear both;
}

@keyframes svgb17-draw {
  to {
    stroke-dashoffset: 0;
  }
}

@keyframes svgb17-read {
  to {
    stroke-dashoffset: 0;
  }
}
/* The fallback is the reason this demo is shippable. Engines without
   scroll-driven animation get the finished border immediately rather than an
   invisible one, and anyone asking for reduced motion gets the same. */

@supports not (animation-timeline: view()) {
  .svgb-17__ink {
    animation: none;
    stroke-dashoffset: 0;
  }

  .svgb-17__mfill {
    animation: none;
    stroke-dashoffset: 0.65;
    opacity: 0.4;
  }
}

@media (prefers-reduced-motion: reduce) {
  .svgb-17__ink {
    animation: none;
    stroke-dashoffset: 0;
  }

  .svgb-17__mfill {
    animation: none;
    stroke-dashoffset: 0.65;
    opacity: 0.4;
  }
}

.svgb-17:has(#svgb-17-theme:checked) {
  --color-svgb17-bg: #100f13;
  --color-svgb17-bg: oklch(0.18 0.008 285);
  --color-svgb17-fg: #f0eef4;
  --color-svgb17-fg: oklch(0.96 0.006 285);
  --color-svgb17-muted: #918e9b;
  --color-svgb17-muted: oklch(0.68 0.014 285);
  --color-svgb17-rest: rgba(240, 238, 244, 0.18);
  --color-svgb17-rest: oklch(0.96 0.006 285 / 0.18);
  --color-svgb17-stroke: #ff9070;
  --color-svgb17-stroke: oklch(0.79 0.15 40);
}
```
