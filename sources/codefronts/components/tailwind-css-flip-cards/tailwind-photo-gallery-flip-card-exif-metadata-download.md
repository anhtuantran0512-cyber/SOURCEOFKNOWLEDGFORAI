---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-photo-gallery-flip-card-exif-metadata-download/"
title: "Tailwind Photo Gallery Flip Card with EXIF Metadata & Download CTA"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A photograph that folds down from its top edge like peeling back a Polaroid, revealing location, EXIF, tags and a download action."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Photo Gallery Flip Card with EXIF Metadata & Download CTA
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-photo-gallery-flip-card-exif-metadata-download/

A photograph that folds down from its top edge like peeling back a Polaroid, revealing location, EXIF, tags and a download action. The scrim &mdash; the gradient that keeps overlay text readable over any sky &mdash; survives the port as a single bg-linear-to-t utility, and the whole thing is now a <figure> with a real caption.
## HTML
```html
<section class="tfc-09 w-full min-h-svh grid place-items-center bg-tfc09-bg font-tfc09-sans px-5 py-10 text-tfc09-ink">
  <div class="group relative w-[340px] max-w-full h-[450px] [perspective:1200px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc09-sky has-[:focus-visible]:outline-offset-4">
    <input id="tfc-09-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-09-flip" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show capture details for Aurora at Jökulsárlón</span></label>

    <div class="relative w-full h-full origin-top transition-transform duration-[850ms] ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:translateY(100%)_rotateX(-180deg)] group-has-checked:[transform:translateY(100%)_rotateX(-180deg)] group-has-[:focus-visible]:[transform:translateY(100%)_rotateX(-180deg)] motion-reduce:transition-none">

      <figure class="absolute inset-0 m-0 flex flex-col rounded-2xl overflow-hidden border border-tfc09-sky/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.4_0.1_230/0.6)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <div class="relative flex-1 overflow-hidden bg-linear-160 from-tfc09-p1 via-tfc09-p2 to-tfc09-p3">
          <svg class="absolute inset-0 size-full" viewBox="0 0 340 380" preserveAspectRatio="xMidYMid slice" fill="none" role="img" aria-label="Aurora borealis over a glacial lagoon with mountains and a crescent moon">
            <defs>
              <linearGradient id="tfc-09-sky" x1="0" y1="0" x2="0" y2="380" gradientUnits="userSpaceOnUse"><stop stop-color="#041830"/><stop offset=".5" stop-color="#0a2a4a"/><stop offset="1" stop-color="#0d3a5c"/></linearGradient>
              <linearGradient id="tfc-09-water" x1="0" y1="280" x2="0" y2="380" gradientUnits="userSpaceOnUse"><stop stop-color="#062035"/><stop offset="1" stop-color="#020d18"/></linearGradient>
            </defs>
            <rect width="340" height="380" fill="url(#tfc-09-sky)"/>
            <circle cx="30" cy="30" r="1.5" fill="white" opacity=".8"/><circle cx="80" cy="15" r="1" fill="white" opacity=".6"/><circle cx="150" cy="25" r="1.5" fill="white" opacity=".9"/><circle cx="220" cy="10" r="1" fill="white" opacity=".7"/><circle cx="290" cy="35" r="1.5" fill="white" opacity=".8"/><circle cx="310" cy="15" r="1" fill="white" opacity=".5"/><circle cx="60" cy="60" r="1" fill="white" opacity=".6"/><circle cx="260" cy="60" r="1.5" fill="white" opacity=".7"/>
            <ellipse cx="170" cy="80" rx="200" ry="40" fill="oklch(0.7 0.12 190 / 0.15)"/>
            <ellipse cx="170" cy="90" rx="160" ry="25" fill="oklch(0.68 0.14 230 / 0.1)"/>
            <path d="M0 220 L60 140 L120 200 L180 130 L240 190 L300 140 L340 180 L340 280 L0 280Z" fill="oklch(0.25 0.05 250 / 0.7)"/>
            <path d="M0 260 L80 180 L140 230 L200 170 L260 220 L340 175 L340 280 L0 280Z" fill="oklch(0.18 0.04 255 / 0.9)"/>
            <rect x="0" y="280" width="340" height="100" fill="url(#tfc-09-water)"/>
            <line x1="50" y1="300" x2="290" y2="300" stroke="oklch(0.68 0.14 230 / 0.08)" stroke-width="8"/>
            <line x1="30" y1="320" x2="310" y2="320" stroke="oklch(0.68 0.14 230 / 0.05)" stroke-width="12"/>
            <ellipse cx="170" cy="330" rx="180" ry="20" fill="oklch(0.7 0.12 190 / 0.08)"/>
            <circle cx="260" cy="55" r="20" fill="oklch(0.97 0.01 230 / 0.9)"/>
            <circle cx="268" cy="48" r="16" fill="oklch(0.19 0.03 250 / 0.95)"/>
          </svg>
          <figcaption class="absolute inset-x-0 bottom-0 bg-linear-to-t from-tfc09-bg/90 to-transparent p-5">
            <p class="flex items-center gap-1.5 text-[10px] uppercase tracking-[0.1em] text-tfc09-ink/60">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
              f/2.8 &middot; 25s &middot; ISO 3200
            </p>
            <h3 class="mt-1 text-xl font-extrabold tracking-[-0.02em] text-white">Aurora at Jökulsárlón</h3>
          </figcaption>
        </div>
        <p class="bg-black/40 p-3.5 text-center text-[10px] tracking-[0.08em] text-tfc09-dim">Hover, tap or press Space for details &amp; download &rarr;</p>
      </figure>

      <div class="absolute inset-0 flex flex-col gap-4 rounded-2xl overflow-hidden p-7 bg-linear-160 from-tfc09-b1 to-tfc09-b2 border border-tfc09-teal/25 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.45_0.1_190/0.5)] [transform:rotateX(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <div class="relative h-30 shrink-0 overflow-hidden rounded-xl bg-linear-160 from-tfc09-p1 to-tfc09-p3">
          <svg class="absolute inset-0 size-full" viewBox="0 0 340 120" preserveAspectRatio="xMidYMid slice" fill="none" aria-hidden="true">
            <rect width="340" height="120" fill="#041830"/>
            <path d="M0 80 L80 50 L140 70 L200 40 L260 65 L340 45 L340 120 L0 120Z" fill="oklch(0.25 0.05 250 / 0.9)"/>
            <ellipse cx="170" cy="30" rx="160" ry="18" fill="oklch(0.7 0.12 190 / 0.2)"/>
            <rect x="0" y="90" width="340" height="30" fill="oklch(0.17 0.02 250 / 0.9)"/>
          </svg>
        </div>
        <dl class="grid grid-cols-2 gap-2.5">
          <div class="rounded-xl border border-white/7 bg-white/4 px-3 py-2.5"><dt class="mb-1 text-[9px] uppercase tracking-[0.12em] text-tfc09-dim">Location</dt><dd class="text-[13px] font-semibold text-white">Iceland</dd></div>
          <div class="rounded-xl border border-white/7 bg-white/4 px-3 py-2.5"><dt class="mb-1 text-[9px] uppercase tracking-[0.12em] text-tfc09-dim">Date captured</dt><dd class="text-[13px] font-semibold text-white">Nov 12, 2024</dd></div>
          <div class="rounded-xl border border-white/7 bg-white/4 px-3 py-2.5"><dt class="mb-1 text-[9px] uppercase tracking-[0.12em] text-tfc09-dim">Camera</dt><dd class="text-[13px] font-semibold text-white">Sony A7R V</dd></div>
          <div class="rounded-xl border border-white/7 bg-white/4 px-3 py-2.5"><dt class="mb-1 text-[9px] uppercase tracking-[0.12em] text-tfc09-dim">Resolution</dt><dd class="text-[13px] font-semibold text-white">61 MP RAW</dd></div>
        </dl>
        <ul class="flex flex-wrap gap-1.5">
          <li class="rounded-full border border-tfc09-sky/20 bg-tfc09-sky/10 px-2.5 py-0.5 text-[10px] text-tfc09-sky">Aurora</li>
          <li class="rounded-full border border-tfc09-sky/20 bg-tfc09-sky/10 px-2.5 py-0.5 text-[10px] text-tfc09-sky">Landscape</li>
          <li class="rounded-full border border-tfc09-sky/20 bg-tfc09-sky/10 px-2.5 py-0.5 text-[10px] text-tfc09-sky">Night Sky</li>
        </ul>
        <button type="button" aria-disabled="true" title="Demo only — wire to a signed download URL" class="relative z-30 mt-auto flex min-h-11 items-center justify-center gap-2 rounded-xl bg-linear-135 from-tfc09-sky to-tfc09-teal text-[13px] font-extrabold tracking-[0.04em] text-black transition-opacity duration-150 hover:opacity-90 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Download full resolution
        </button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc09-bg: #080c10;
  --color-tfc09-bg: oklch(0.14 0.01 240);
  --color-tfc09-p1: #0c2340;
  --color-tfc09-p1: oklch(0.24 0.06 250);
  --color-tfc09-p2: #041520;
  --color-tfc09-p2: oklch(0.16 0.03 240);
  --color-tfc09-p3: #0d2a2a;
  --color-tfc09-p3: oklch(0.24 0.04 190);
  --color-tfc09-b1: #0a1520;
  --color-tfc09-b1: oklch(0.18 0.025 245);
  --color-tfc09-b2: #060e18;
  --color-tfc09-b2: oklch(0.14 0.02 245);
  --color-tfc09-sky: #0ea5e9;
  --color-tfc09-sky: oklch(0.7 0.15 230);
  --color-tfc09-teal: #14b8a6;
  --color-tfc09-teal: oklch(0.72 0.12 185);
  --color-tfc09-ink: #f0f9ff;
  --color-tfc09-ink: oklch(0.97 0.015 230);
  --color-tfc09-dim: #7e8c99;
  --color-tfc09-dim: oklch(0.64 0.02 235);
  --font-tfc09-sans: 'Sora', system-ui, sans-serif;
}

.tfc-09 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-09 * {
    transition-duration: 1ms !important;
  }
}
```
