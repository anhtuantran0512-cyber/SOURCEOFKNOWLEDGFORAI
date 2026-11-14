---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/glassmorphism-tailwind-css-accordion/"
title: "Glassmorphism Tailwind CSS Accordion"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "Frosted panes floating over vivid, slowly drifting colour blobs: each item is backdrop-blur-xl backdrop-saturate-150 glass with a hairline ring-white/15 rim…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Tailwind CSS Accordion
Source: https://codefronts.com/navigation/tailwind-css-accordions/glassmorphism-tailwind-css-accordion/

Frosted panes floating over vivid, slowly drifting colour blobs: each item is backdrop-blur-xl backdrop-saturate-150 glass with a hairline ring-white/15 rim and an inset top highlight, brightening to bg-white/14 on open. The panes default to a solid tinted fill and only turn translucent inside supports-[backdrop-filter:blur(1px)]:, so text is never stranded on raw gradient. An ambient-sound app FAQ.
## HTML
```html
<section class="tac-12 relative isolate w-full min-h-svh grid place-items-center overflow-hidden bg-tac12-bg px-5 py-14 font-tac12-sans text-white [interpolate-size:allow-keywords]" aria-label="Glassmorphism accordion demo">
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10">
    <div class="absolute -top-[6%] left-[14%] size-[min(520px,90vw)] rounded-full bg-[radial-gradient(circle,var(--color-tac12-blob1),transparent_68%)] blur-3xl animate-tac12-drift motion-reduce:animate-none"></div>
    <div class="absolute right-[6%] -bottom-[8%] size-[min(600px,100vw)] rounded-full bg-[radial-gradient(circle,var(--color-tac12-blob2),transparent_68%)] blur-3xl animate-tac12-drift [animation-delay:-9s] [animation-direction:reverse] motion-reduce:animate-none"></div>
    <div class="absolute top-[30%] left-[40%] size-[min(440px,80vw)] rounded-full bg-[radial-gradient(circle,var(--color-tac12-blob3),transparent_70%)] blur-3xl animate-tac12-drift [animation-delay:-4s] motion-reduce:animate-none"></div>
  </div>

  <div class="grid w-full justify-items-center gap-8">
    <div class="w-full max-w-[580px]">
      <header class="mb-7 flex items-center gap-4">
        <span aria-hidden="true" class="grid size-13 flex-none place-items-center rounded-2xl bg-linear-to-br from-tac12-blob1 to-tac12-blob2 shadow-[inset_0_1px_0_oklch(1_0_0/0.4),0_10px_30px_-8px_oklch(0.4_0.2_300/0.6)] ring-1 ring-white/25">
          <svg viewBox="0 0 24 24" width="26" height="26"><path d="M3 14c2.2 0 2.2-4 4.5-4S9.7 17 12 17s2.2-10 4.5-10S18.8 14 21 14" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
        <div>
          <p class="font-tac12-mono text-[11.5px] tracking-[0.14em] uppercase text-white/80">Aurora 3.2 · Help</p>
          <h2 class="mt-0.5 text-[clamp(22px,4vw,28px)] leading-tight font-semibold tracking-[-0.02em] [text-shadow:0_2px_20px_oklch(0_0_0/0.3)]">Ambient sound engine</h2>
        </div>
      </header>

      <div class="flex flex-col gap-3.5">
        <details class="group rounded-2xl bg-tac12-pane shadow-[inset_0_1px_0_oklch(1_0_0/0.25),0_16px_40px_-20px_oklch(0.1_0.05_290/0.7)] ring-1 ring-white/15 transition-[background-color,box-shadow] duration-300 hover:ring-white/25 open:bg-tac12-pane-hi open:ring-white/30 supports-[backdrop-filter:blur(1px)]:bg-white/8 supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl supports-[backdrop-filter:blur(1px)]:backdrop-saturate-150 supports-[backdrop-filter:blur(1px)]:open:bg-white/14 motion-reduce:transition-none details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-400 details-content:ease-[cubic-bezier(.2,.7,.2,1)] open:details-content:h-auto motion-reduce:details-content:transition-none" open>
          <summary class="flex min-h-15 cursor-pointer list-none items-center gap-4 rounded-2xl py-3 pr-4 pl-5 text-[15.5px] font-medium select-none focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white [&::-webkit-details-marker]:hidden">
            <span class="flex-1">What does Aurora listen to?</span>
            <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-white/10 ring-1 ring-white/20 transition-[rotate,background-color] duration-300 ease-[cubic-bezier(.3,1.3,.5,1)] group-open:rotate-180 group-open:bg-white/25 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.25 8 10l4-3.75" fill="none" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="px-5 pb-5">
            <p class="text-[14.5px] leading-[1.65] text-white/90 text-pretty">Nothing. All processing happens on-device: the engine reacts to time of day, local weather and how packed your calendar is &mdash; no microphone access, ever.</p>
            <ul class="mt-3.5 flex flex-wrap gap-2 font-tac12-mono text-[11.5px]">
              <li class="rounded-full bg-white/10 px-2.5 py-1 ring-1 ring-white/15">On-device</li>
              <li class="rounded-full bg-white/10 px-2.5 py-1 ring-1 ring-white/15">No mic</li>
              <li class="rounded-full bg-white/10 px-2.5 py-1 ring-1 ring-white/15">Zero analytics</li>
            </ul>
          </div>
        </details>

        <details class="group rounded-2xl bg-tac12-pane shadow-[inset_0_1px_0_oklch(1_0_0/0.25),0_16px_40px_-20px_oklch(0.1_0.05_290/0.7)] ring-1 ring-white/15 transition-[background-color,box-shadow] duration-300 hover:ring-white/25 open:bg-tac12-pane-hi open:ring-white/30 supports-[backdrop-filter:blur(1px)]:bg-white/8 supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl supports-[backdrop-filter:blur(1px)]:backdrop-saturate-150 supports-[backdrop-filter:blur(1px)]:open:bg-white/14 motion-reduce:transition-none details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-400 details-content:ease-[cubic-bezier(.2,.7,.2,1)] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-15 cursor-pointer list-none items-center gap-4 rounded-2xl py-3 pr-4 pl-5 text-[15.5px] font-medium select-none focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white [&::-webkit-details-marker]:hidden">
            <span class="flex-1">Which platforms are supported?</span>
            <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-white/10 ring-1 ring-white/20 transition-[rotate,background-color] duration-300 ease-[cubic-bezier(.3,1.3,.5,1)] group-open:rotate-180 group-open:bg-white/25 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.25 8 10l4-3.75" fill="none" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="px-5 pb-5">
            <p class="text-[14.5px] leading-[1.65] text-white/90 text-pretty">macOS, iOS and iPadOS today, with seamless handoff between them. Windows is in private beta &mdash; request an invite from the Settings pane.</p>
          </div>
        </details>

        <details class="group rounded-2xl bg-tac12-pane shadow-[inset_0_1px_0_oklch(1_0_0/0.25),0_16px_40px_-20px_oklch(0.1_0.05_290/0.7)] ring-1 ring-white/15 transition-[background-color,box-shadow] duration-300 hover:ring-white/25 open:bg-tac12-pane-hi open:ring-white/30 supports-[backdrop-filter:blur(1px)]:bg-white/8 supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl supports-[backdrop-filter:blur(1px)]:backdrop-saturate-150 supports-[backdrop-filter:blur(1px)]:open:bg-white/14 motion-reduce:transition-none details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:transition-discrete details-content:duration-400 details-content:ease-[cubic-bezier(.2,.7,.2,1)] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="flex min-h-15 cursor-pointer list-none items-center gap-4 rounded-2xl py-3 pr-4 pl-5 text-[15.5px] font-medium select-none focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white [&::-webkit-details-marker]:hidden">
            <span class="flex-1">Can I import my own soundscapes?</span>
            <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-white/10 ring-1 ring-white/20 transition-[rotate,background-color] duration-300 ease-[cubic-bezier(.3,1.3,.5,1)] group-open:rotate-180 group-open:bg-white/25 motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M4 6.25 8 10l4-3.75" fill="none" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="px-5 pb-5">
            <p class="text-[14.5px] leading-[1.65] text-white/90 text-pretty">Drop in any lossless file and Aurora will loop-point, EQ-match and weather-blend it automatically. Creators can publish packs to the community gallery.</p>
          </div>
        </details>
      </div>

      <div class="mt-7 flex flex-wrap items-center justify-between gap-4 rounded-2xl bg-tac12-pane px-5 py-4 ring-1 ring-white/15 supports-[backdrop-filter:blur(1px)]:bg-white/6 supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl">
        <p class="text-sm text-white/90">Free for 14 days · then $4 / month</p>
        <a href="#tac12-download" id="tac12-download" class="inline-flex min-h-11 items-center gap-2 rounded-full bg-white px-5 text-sm font-semibold text-tac12-bg shadow-[0_8px_24px_-8px_oklch(1_0_0/0.5)] transition-[translate,box-shadow] hover:-translate-y-px hover:shadow-[0_12px_30px_-8px_oklch(1_0_0/0.6)] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none motion-reduce:hover:translate-y-0">Download for Mac</a>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/8 px-3.5 py-2 text-center font-tac12-mono text-[11.5px] text-white/85 ring-1 ring-white/15">backdrop-blur-xl · backdrop-saturate-150 · supports-[backdrop-filter:blur(1px)]:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac12-bg: #150f2e;
  --color-tac12-bg: oklch(0.2 0.07 290);
  --color-tac12-pane: #2a2350eb;
  --color-tac12-pane: oklch(0.29 0.07 290 / 0.92);
  --color-tac12-pane-hi: #352c61f0;
  --color-tac12-pane-hi: oklch(0.33 0.08 290 / 0.94);
  --color-tac12-blob1: #c13fd9;
  --color-tac12-blob1: oklch(0.6 0.24 315);
  --color-tac12-blob2: #1f8fe0;
  --color-tac12-blob2: oklch(0.62 0.16 245);
  --color-tac12-blob3: #f06a4a;
  --color-tac12-blob3: oklch(0.68 0.17 35);
  --font-tac12-sans: 'Sora', system-ui, sans-serif;
  --font-tac12-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tac12-drift: tac12-drift 22s ease-in-out infinite alternate;

  @keyframes tac12-drift {
    0% {
      transform: translate3d(0, 0, 0) scale(1);
    }

    50% {
      transform: translate3d(6%, 8%, 0) scale(1.08);
    }

    100% {
      transform: translate3d(-5%, 3%, 0) scale(0.96);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-12 {
  width: 100%;
  min-height: 100svh;
}
```
