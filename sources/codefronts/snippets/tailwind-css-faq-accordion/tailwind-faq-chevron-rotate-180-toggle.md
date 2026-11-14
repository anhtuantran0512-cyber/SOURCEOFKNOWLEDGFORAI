---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-faq-chevron-rotate-180-toggle/"
title: "Tailwind FAQ Chevron Rotate 180 Degrees on Toggle"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The definitive treatment of the web's most-copied micro-interaction, ported: three chevron builds in one FAQ — inline SVG, a two-border CSS chevron, and a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind FAQ Chevron Rotate 180 Degrees on Toggle
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-faq-chevron-rotate-180-toggle/

The definitive treatment of the web's most-copied micro-interaction, ported: three chevron builds in one FAQ — inline SVG, a two-border CSS chevron, and a Unicode glyph — each rotating on group-open: with matched timing, plus the UX rules for which way a closed chevron should point and why the rotation duration must equal the panel's.
## HTML
```html
<section class="tfa-11 w-full min-h-svh grid place-items-center bg-tfa11-bg font-tfa11-sans text-tfa11-ink px-5 py-12">
  <div class="w-[min(680px,100%)]">
    <header>
      <h1 class="text-[clamp(28px,5vw,40px)] font-extrabold leading-[1.08] tracking-[-0.025em]">The 180° chevron, three ways</h1>
      <p class="mt-3 max-w-[56ch] text-[15px] leading-relaxed text-tfa11-mut">Same rotation, three icon builds — SVG, pure CSS borders, Unicode. Matched <code class="rounded bg-tfa11-tint px-1.5 py-0.5 font-tfa11-mono text-[0.87em] text-tfa11-acc">duration-400</code> keeps icon and panel in sync.</p>
    </header>

    <div data-panel class="mt-8 flex flex-col gap-2.5">
      <details class="group rounded-2xl border border-tfa11-edge bg-white shadow-[0_2px_8px_oklch(0.4_0.05_250/0.05)] transition-[border-color,box-shadow] duration-300 open:border-tfa11-accedge open:shadow-[0_14px_34px_-20px_oklch(0.45_0.14_250/0.4)]" open>
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-3 px-5 py-4 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa11-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa11-acc [&::-webkit-details-marker]:hidden">
          <span class="shrink-0 rounded-md bg-tfa11-tint px-2 py-1 font-tfa11-mono text-[10px] font-bold tracking-[0.05em] text-tfa11-acc">A · SVG</span>Which icon build should production use?
          <span aria-hidden="true" class="ml-auto grid shrink-0 place-items-center text-tfa11-mut transition-[rotate,color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:text-tfa11-acc group-open:rotate-180 group-open:text-tfa11-acc motion-reduce:transition-colors"><svg viewBox="0 0 16 16" width="16" height="16"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa11-mut">This one. <code class="rounded bg-tfa11-tint px-1.5 py-0.5 font-tfa11-mono text-[0.87em] text-tfa11-acc">stroke: currentColor</code> inherits your text colour automatically, the rounded caps stay crisp at every DPI, and rotating the whole SVG element avoids every alignment quirk the other two builds carry.</p>
      </details>
      <details class="group rounded-2xl border border-tfa11-edge bg-white shadow-[0_2px_8px_oklch(0.4_0.05_250/0.05)] transition-[border-color,box-shadow] duration-300 open:border-tfa11-accedge open:shadow-[0_14px_34px_-20px_oklch(0.45_0.14_250/0.4)]">
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-3 px-5 py-4 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa11-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa11-acc [&::-webkit-details-marker]:hidden">
          <span class="shrink-0 rounded-md bg-tfa11-tint px-2 py-1 font-tfa11-mono text-[10px] font-bold tracking-[0.05em] text-tfa11-acc">B · borders</span>How does the zero-asset chevron work?
          <span aria-hidden="true" class="ml-auto size-2.5 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa11-mut transition-[rotate,translate,border-color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:border-tfa11-acc group-open:translate-y-0.5 group-open:rotate-[225deg] group-open:border-tfa11-acc motion-reduce:transition-colors"></span>
        </summary>
        <p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa11-mut">A 9px square with only its right and bottom borders, pre-rotated 45° — so “rotate 180°” actually means <code class="rounded bg-tfa11-tint px-1.5 py-0.5 font-tfa11-mono text-[0.87em] text-tfa11-acc">rotate-[225deg]</code>, and a 2px translate nudge re-centres its optical middle. Zero assets, two gotchas.</p>
      </details>
      <details class="group rounded-2xl border border-tfa11-edge bg-white shadow-[0_2px_8px_oklch(0.4_0.05_250/0.05)] transition-[border-color,box-shadow] duration-300 open:border-tfa11-accedge open:shadow-[0_14px_34px_-20px_oklch(0.45_0.14_250/0.4)]">
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-3 px-5 py-4 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa11-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa11-acc [&::-webkit-details-marker]:hidden">
          <span class="shrink-0 rounded-md bg-tfa11-tint px-2 py-1 font-tfa11-mono text-[10px] font-bold tracking-[0.05em] text-tfa11-acc">C · Unicode</span>When is a text arrow good enough?
          <span aria-hidden="true" class="ml-auto shrink-0 -translate-y-0.5 text-[18px] font-bold leading-none text-tfa11-mut transition-[rotate,translate,color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:text-tfa11-acc group-open:translate-y-0.5 group-open:rotate-180 group-open:text-tfa11-acc motion-reduce:transition-colors">&#8964;</span>
        </summary>
        <p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa11-mut">Prototypes and plain-text contexts. It costs one character, but its baseline position depends on the font stack — explicit sizing and <code class="rounded bg-tfa11-tint px-1.5 py-0.5 font-tfa11-mono text-[0.87em] text-tfa11-acc">leading-none</code> tame it, mostly. Ship SVG when it matters.</p>
      </details>
      <details class="group rounded-2xl border border-tfa11-edge bg-white shadow-[0_2px_8px_oklch(0.4_0.05_250/0.05)] transition-[border-color,box-shadow] duration-300 open:border-tfa11-accedge open:shadow-[0_14px_34px_-20px_oklch(0.45_0.14_250/0.4)]">
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-3 px-5 py-4 text-[15px] font-semibold transition-colors duration-200 hover:text-tfa11-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa11-acc [&::-webkit-details-marker]:hidden">
          <span class="shrink-0 rounded-md bg-tfa11-tint px-2 py-1 font-tfa11-mono text-[10px] font-bold tracking-[0.05em] text-tfa11-acc">UX</span>Which way should a closed chevron point?
          <span aria-hidden="true" class="ml-auto grid shrink-0 place-items-center text-tfa11-mut transition-[rotate,color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:text-tfa11-acc group-open:rotate-180 group-open:text-tfa11-acc motion-reduce:transition-colors"><svg viewBox="0 0 16 16" width="16" height="16"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <p class="max-w-[60ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa11-mut">Down when closed (content continues below), up when open. Right-pointing chevrons signal navigation into another screen — using one on an accordion misleads screen-magnifier and low-vision users especially. And match the rotation duration to the panel, or mismatched timings read as jank.</p>
      </details>
    </div>

    <p class="mt-6 text-[12.5px] text-tfa11-mut">All three rotate under <code class="rounded bg-tfa11-tint px-1.5 py-0.5 font-tfa11-mono text-[0.87em] text-tfa11-acc">group-open:</code> — build B to 225°, because it starts at 45°.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa11-bg: #f6f7fb;
  --color-tfa11-bg: oklch(0.97 0.008 250);
  --color-tfa11-ink: #262b38;
  --color-tfa11-ink: oklch(0.23 0.03 255);
  --color-tfa11-mut: #5e6472;
  --color-tfa11-mut: oklch(0.47 0.022 252);
  --color-tfa11-edge: #e2e5ee;
  --color-tfa11-edge: oklch(0.91 0.012 250);
  --color-tfa11-accedge: #8fa6e4;
  --color-tfa11-accedge: oklch(0.72 0.1 255);
  --color-tfa11-tint: #e9eefb;
  --color-tfa11-tint: oklch(0.94 0.028 255);
  --color-tfa11-acc: #2f4ec4;
  --color-tfa11-acc: oklch(0.47 0.19 260);
  --font-tfa11-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa11-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-11 {
  width: 100%;
  min-height: 100svh;
}

.tfa-11 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-11 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .4s cubic-bezier(.4,0,.2,1), opacity .32s, content-visibility .4s allow-discrete;
  }

  .tfa-11 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-11 details::details-content {
    transition-duration: 1ms;
  }
}
```
