---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-animated-border-button-hover-effect/"
title: "Tailwind Animated Border Button Hover Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "Two ways to encase a CTA: a frame drawn by two corner pseudo-elements (width first, then height, so the corners chase and meet), and a conic “comet” that…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Border Button Hover Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-animated-border-button-hover-effect/

Two ways to encase a CTA: a frame drawn by two corner pseudo-elements (width first, then height, so the corners chase and meet), and a conic “comet” that orbits the label on a typed @property angle. Both are complete class lists — the only CSS is the angle registration and its keyframe.
## HTML
```html
<section class="tth-18 w-full min-h-svh grid place-items-center bg-tth18-bg bg-[radial-gradient(90%_70%_at_50%_25%,var(--color-tth18-glow),var(--color-tth18-bg)_72%)] px-5 py-14 font-tth18-sans text-tth18-ink" aria-label="Animated border encased text demo">
  <div class="flex flex-col items-center gap-[clamp(14px,2.6vw,20px)] text-center">
    <p class="text-xs font-bold uppercase tracking-[0.26em] text-tth18-acc">Helio deploy &mdash; private beta</p>
    <h2 class="text-[clamp(34px,6.6vw,62px)] font-extrabold leading-[1.06] tracking-[-0.03em] text-balance">Ship the edge build</h2>
    <p class="max-w-[46ch] text-[15px] leading-[1.65] text-tth18-mut">Zero-config previews on every push. Two seats left in the winter cohort.</p>
    <div class="mt-2.5 flex flex-wrap justify-center gap-[clamp(14px,3vw,24px)]">
      <a id="tth18-top" href="#tth18-top" class="group/trace relative grid min-h-14 place-items-center bg-tth18-panel px-[30px] text-[15.5px] font-bold tracking-[0.02em] no-underline before:pointer-events-none before:absolute before:left-0 before:top-0 before:h-0 before:w-0 before:border-t-[1.5px] before:border-r-[1.5px] before:border-tth18-acc before:[transition:width_.2s_ease-out,height_.2s_ease-out_.2s] before:content-[''] after:pointer-events-none after:absolute after:bottom-0 after:right-0 after:h-0 after:w-0 after:border-b-[1.5px] after:border-l-[1.5px] after:border-tth18-acc after:[transition:width_.2s_ease-out,height_.2s_ease-out_.2s] after:content-[''] hover:before:size-full hover:after:size-full focus-visible:before:size-full focus-visible:after:size-full focus-visible:outline-[1.5px] focus-visible:outline-offset-[5px] focus-visible:outline-tth18-acc pointer-coarse:before:size-full pointer-coarse:after:size-full motion-reduce:before:transition-none motion-reduce:after:transition-none"><span class="transition-colors delay-250 duration-300 group-hover/trace:text-tth18-acc group-focus-visible/trace:text-tth18-acc">Read the runbook</span></a>
      <a href="#tth18-top" class="group/orbit relative grid min-h-14 place-items-center rounded-[14px] px-0.5 no-underline [--tth18-a:40deg] bg-[conic-gradient(from_var(--tth18-a),transparent_0_78%,var(--color-tth18-acc)_92%,transparent_100%)] transition-shadow duration-300 hover:animate-tth18-spin hover:shadow-[0_0_40px_-8px_color-mix(in_oklch,var(--color-tth18-acc)_55%,transparent)] focus-visible:animate-tth18-spin focus-visible:outline-[1.5px] focus-visible:outline-offset-4 focus-visible:outline-tth18-acc motion-reduce:animate-none!"><span class="m-[1.5px] grid min-h-[calc(56px-3px)] place-items-center rounded-[12.5px] bg-tth18-panel2 px-[30px] text-[15.5px] font-bold tracking-[0.02em] text-tth18-ink transition-colors duration-300 group-hover/orbit:bg-tth18-panel group-hover/orbit:text-tth18-acc group-focus-visible/orbit:text-tth18-acc">Request access</span></a>
    </div>
    <p class="mt-2 max-w-[60ch] text-[12.5px] leading-[1.7] text-tth18-mut">Left: two corner pseudo-elements trace the frame (width, then height &mdash; watch the corners meet). Right: a typed <code class="rounded bg-tth18-chip px-1.5 py-px font-tth18-mono text-[0.9em] text-tth18-acc">@property</code> angle spins a conic comet around the text.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tth18-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-tth18-bg: #0e1119;
  --color-tth18-bg: oklch(0.17 0.012 260);
  --color-tth18-glow: #161a25;
  --color-tth18-glow: oklch(0.21 0.018 262);
  --color-tth18-panel: #131722;
  --color-tth18-panel: oklch(0.2 0.014 260);
  --color-tth18-panel2: #181c28;
  --color-tth18-panel2: oklch(0.22 0.016 260);
  --color-tth18-chip: #1c2130;
  --color-tth18-chip: oklch(0.25 0.016 260);
  --color-tth18-ink: #eff1f6;
  --color-tth18-ink: oklch(0.95 0.008 250);
  --color-tth18-mut: #a0a6b4;
  --color-tth18-mut: oklch(0.72 0.02 255);
  --color-tth18-acc: #b7ea4f;
  --color-tth18-acc: oklch(0.87 0.17 130);
  --font-tth18-sans: 'Sora', system-ui, sans-serif;
  --font-tth18-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tth18-spin: tth18-spin 1.6s linear infinite;

  @keyframes tth18-spin {
    to {
      --tth18-a: 400deg;
    }
  }
}

.tth-18 {
  width: 100%;
  min-height: 100svh;
}
```
