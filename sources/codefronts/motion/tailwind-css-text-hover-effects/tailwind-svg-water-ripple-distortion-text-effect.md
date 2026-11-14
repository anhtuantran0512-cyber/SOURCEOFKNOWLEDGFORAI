---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-svg-water-ripple-distortion-text-effect/"
title: "Tailwind SVG Water Ripple Distortion Text Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A surf-report wordmark that slips underwater on hover: a hidden SVG filter (feTurbulence + feDisplacementMap, with an animated baseFrequency) distorts an…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind SVG Water Ripple Distortion Text Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-svg-water-ripple-distortion-text-effect/

A surf-report wordmark that slips underwater on hover: a hidden SVG filter (feTurbulence + feDisplacementMap, with an animated baseFrequency) distorts an aqua clone, applied with [filter:url(#tth29-ripple)]. Because filter:url() can't transition, the crisp word and the rippled clone crossfade instead.
## HTML
```html
<section class="tth-29 w-full min-h-svh grid place-items-center bg-tth29-bg bg-[radial-gradient(100%_85%_at_50%_100%,var(--color-tth29-deep),var(--color-tth29-bg)_70%)] px-5 py-14 font-tth29-sans text-tth29-ink" aria-label="Ripple distortion text demo">
  <svg width="0" height="0" class="absolute" aria-hidden="true" focusable="false"><filter id="tth29-ripple" x="-25%" y="-25%" width="150%" height="150%"><feTurbulence type="turbulence" baseFrequency="0.012 0.05" numOctaves="2" seed="4" result="n"><animate attributeName="baseFrequency" dur="7s" values="0.012 0.05; 0.017 0.09; 0.012 0.05" repeatCount="indefinite"/></feTurbulence><feDisplacementMap in="SourceGraphic" in2="n" scale="16" xChannelSelector="R" yChannelSelector="G"/></filter></svg>
  <div class="flex flex-col items-center gap-[clamp(16px,3vw,26px)] text-center">
    <p class="text-xs font-bold uppercase tracking-[0.26em] text-tth29-mut">Undertow &mdash; surf &amp; swell reports, delivered at dawn</p>
    <a id="tth29-top" href="#tth29-top" class="group/word relative inline-block rounded-md px-[0.12em] py-[0.15em] font-tth29-display text-[clamp(64px,14vw,150px)] font-black uppercase leading-none tracking-[0.01em] no-underline focus-visible:outline-2 focus-visible:outline-offset-8 focus-visible:outline-tth29-acc">
      <span class="block opacity-100 transition-[opacity,color] duration-600 group-hover/word:opacity-6 group-focus-visible/word:opacity-6 motion-reduce:transition-none motion-reduce:group-hover/word:opacity-100 motion-reduce:group-hover/word:text-tth29-acc">UNDERTOW</span>
      <span aria-hidden="true" class="absolute inset-x-[0.12em] inset-y-[0.15em] block text-tth29-acc opacity-0 [filter:url(#tth29-ripple)] transition-opacity duration-600 group-hover/word:opacity-100 group-focus-visible/word:opacity-100 motion-reduce:hidden">UNDERTOW</span>
    </a>
    <svg viewBox="0 0 220 14" aria-hidden="true" class="w-[min(220px,60%)] text-tth29-acc/55"><path fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" d="M2 7 Q 15 1, 28 7 T 54 7 T 80 7 T 106 7 T 132 7 T 158 7 T 184 7 T 210 7"><animate attributeName="d" dur="2.6s" repeatCount="indefinite" values="M2 7 Q 15 1, 28 7 T 54 7 T 80 7 T 106 7 T 132 7 T 158 7 T 184 7 T 210 7; M2 7 Q 15 13, 28 7 T 54 7 T 80 7 T 106 7 T 132 7 T 158 7 T 184 7 T 210 7; M2 7 Q 15 1, 28 7 T 54 7 T 80 7 T 106 7 T 132 7 T 158 7 T 184 7 T 210 7"/></path></svg>
    <form class="flex w-full max-w-md flex-wrap justify-center gap-2" onsubmit="return false" aria-label="Subscribe to dawn reports">
      <label for="tth29-email" class="sr-only">Email address</label>
      <input id="tth29-email" type="email" placeholder="[email protected]" class="min-h-12 min-w-0 flex-1 rounded-full border border-tth29-ink/20 bg-white/5 px-5 text-[15px] text-tth29-ink placeholder:text-tth29-mut focus:border-tth29-acc focus:outline-none focus-visible:ring-2 focus-visible:ring-tth29-acc/40">
      <button type="submit" class="min-h-12 cursor-pointer rounded-full bg-tth29-acc px-6 text-[15px] font-bold text-tth29-bg transition-[translate,box-shadow] duration-300 hover:-translate-y-0.5 hover:shadow-[0_10px_30px_-8px_var(--color-tth29-acc)] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth29-acc">Get the dawn report</button>
    </form>
    <p class="max-w-[58ch] text-[12.5px] leading-[1.7] text-tth29-mut">Hover the wordmark &mdash; it slips underwater. <code class="rounded bg-tth29-chip px-1.5 py-px font-tth29-mono text-[0.9em] text-tth29-acc">feTurbulence</code> + <code class="rounded bg-tth29-chip px-1.5 py-px font-tth29-mono text-[0.9em] text-tth29-acc">feDisplacementMap</code> do the physics; a crossfaded clone hides that <code class="rounded bg-tth29-chip px-1.5 py-px font-tth29-mono text-[0.9em] text-tth29-acc">filter:url()</code> can't transition.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth29-bg: #0a1a22;
  --color-tth29-bg: oklch(0.17 0.025 230);
  --color-tth29-deep: #0f2e3d;
  --color-tth29-deep: oklch(0.24 0.05 220);
  --color-tth29-chip: #13252f;
  --color-tth29-chip: oklch(0.24 0.03 225);
  --color-tth29-ink: #e3f2f6;
  --color-tth29-ink: oklch(0.94 0.02 210);
  --color-tth29-mut: #8fa9b5;
  --color-tth29-mut: oklch(0.71 0.04 220);
  --color-tth29-acc: #5fd6e0;
  --color-tth29-acc: oklch(0.8 0.12 195);
  --font-tth29-display: 'Big Shoulders Display', Impact, sans-serif;
  --font-tth29-sans: 'Outfit', system-ui, sans-serif;
  --font-tth29-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-29 {
  width: 100%;
  min-height: 100svh;
}
```
