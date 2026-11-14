---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-album-card-clip-path-iris-aperture-reveal/"
title: "Tailwind Album Card with clip-path Iris Aperture Reveal (No 3D)"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A reveal with no rotation at all: the cover shrinks through clip-path: circle(0%) while the tracklist opens from the centre, like a camera aperture."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Album Card with clip-path Iris Aperture Reveal (No 3D)
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-album-card-clip-path-iris-aperture-reveal/

A reveal with no rotation at all: the cover shrinks through clip-path: circle(0%) while the tracklist opens from the centre, like a camera aperture. One animated property per face, GPU-composited, and cheaper than a 3D turn &mdash; and the port closes the original's own noted gap by putting aria-hidden on the clipped face.
## HTML
```html
<section class="tfc-21 w-full min-h-svh grid place-items-center bg-tfc21-bg font-tfc21-sans px-5 py-10 text-tfc21-ink">
  <div class="group relative h-[510px] w-[360px] max-w-full overflow-hidden rounded-lg shadow-[0_0_0_1px_oklch(0.65_0.22_350/0.2),0_24px_60px_oklch(0_0_0/0.6)] has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc21-neon has-[:focus-visible]:outline-offset-4">
    <input id="tfc-21-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-21-flip" class="absolute inset-0 z-20 cursor-pointer peer-checked:pointer-events-none"><span class="sr-only">Open the tracklist for After Midnight Drives</span></label>

    <div class="absolute inset-0 z-1 flex flex-col items-center bg-linear-160 from-tfc21-p1 to-tfc21-bg px-7 py-7.5 [clip-path:circle(150%_at_50%_50%)] [-webkit-clip-path:circle(150%_at_50%_50%)] transition-[clip-path] duration-[650ms] ease-[cubic-bezier(.7,0,.3,1)] group-hover:[clip-path:circle(0%_at_50%_50%)] group-has-checked:[clip-path:circle(0%_at_50%_50%)] group-has-[:focus-visible]:[clip-path:circle(0%_at_50%_50%)] motion-reduce:transition-none">
      <div class="mt-1.5 overflow-hidden rounded-sm shadow-[0_14px_30px_oklch(0_0_0/0.5)]">
        <svg width="220" height="220" viewBox="0 0 220 220" fill="none" role="img" aria-label="Album cover: a vinyl record on a magenta and indigo gradient">
          <defs>
            <radialGradient id="tfc-21-cover" cx="0.4" cy="0.35" r="0.7"><stop offset="0%" stop-color="#ec4899"/><stop offset="40%" stop-color="#a21caf"/><stop offset="100%" stop-color="#1e1b4b"/></radialGradient>
            <linearGradient id="tfc-21-vinyl" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1c1c1c"/><stop offset="100%" stop-color="#0a0a0a"/></linearGradient>
          </defs>
          <rect width="220" height="220" fill="url(#tfc-21-cover)"/>
          <circle cx="110" cy="110" r="78" fill="url(#tfc-21-vinyl)"/>
          <circle cx="110" cy="110" r="78" fill="none" stroke="#3a3a3a" stroke-width="0.5"/>
          <circle cx="110" cy="110" r="68" fill="none" stroke="#2a2a2a" stroke-width="0.5"/>
          <circle cx="110" cy="110" r="58" fill="none" stroke="#2a2a2a" stroke-width="0.5"/>
          <circle cx="110" cy="110" r="48" fill="none" stroke="#2a2a2a" stroke-width="0.5"/>
          <circle cx="110" cy="110" r="38" fill="none" stroke="#2a2a2a" stroke-width="0.5"/>
          <circle cx="110" cy="110" r="28" fill="#ec4899"/>
          <circle cx="110" cy="110" r="4" fill="#0a0a0a"/>
          <g opacity="0.4"><circle cx="170" cy="50" r="2" fill="#fef3c7"/><circle cx="180" cy="180" r="1.5" fill="#fef3c7"/><circle cx="40" cy="170" r="2" fill="#fef3c7"/><circle cx="30" cy="40" r="1.5" fill="#fef3c7"/></g>
        </svg>
      </div>
      <div class="mt-5.5 w-full text-center">
        <p class="text-[11px] font-bold tracking-[0.45em] text-tfc21-neon">VANTABLACK</p>
        <h2 class="mt-1.5 font-tfc21-display text-[23px] font-bold italic tracking-[-0.02em] text-tfc21-ink">After Midnight Drives</h2>
        <ul class="mt-3 flex justify-center gap-1.5">
          <li class="rounded-full border border-tfc21-neon/40 px-2.5 py-1 text-[9px] font-semibold uppercase tracking-[0.2em] text-tfc21-ink/75">Synthwave</li>
          <li class="rounded-full border border-tfc21-neon/40 px-2.5 py-1 text-[9px] font-semibold uppercase tracking-[0.2em] text-tfc21-ink/75">2026 &middot; LP</li>
        </ul>
      </div>
      <p class="mt-auto text-[10px] uppercase tracking-[0.2em] text-tfc21-ink/45">Hover, tap or press Space for the tracklist</p>
    </div>

    <div aria-hidden="true" class="absolute inset-0 z-2 flex flex-col items-center bg-linear-160 from-tfc21-bg to-tfc21-p1 px-7 py-7.5 [clip-path:circle(0%_at_50%_50%)] [-webkit-clip-path:circle(0%_at_50%_50%)] transition-[clip-path] duration-[650ms] ease-[cubic-bezier(.7,0,.3,1)] group-hover:[clip-path:circle(150%_at_50%_50%)] group-has-checked:[clip-path:circle(150%_at_50%_50%)] group-has-[:focus-visible]:[clip-path:circle(150%_at_50%_50%)] motion-reduce:transition-none">
      <div class="mb-3.5 flex w-full justify-between border-b border-tfc21-neon/25 pb-3.5 text-[10px] font-bold uppercase tracking-[0.3em] text-tfc21-neon">
        <span>Side A</span>
        <span class="font-tfc21-mono tracking-[0.1em] text-tfc21-ink/60">38 : 12</span>
      </div>
      <ol class="flex w-full flex-1 flex-col">
        <li class="grid grid-cols-[28px_1fr_auto] items-center gap-3 rounded-md px-2 py-2.5 transition-colors duration-150 hover:bg-tfc21-neon/8"><span class="font-tfc21-mono text-[10px] tracking-[0.1em] text-tfc21-ink/45">01</span><span class="text-[13px] font-medium text-tfc21-ink">Neon Highway</span><span class="font-tfc21-mono text-[11px] text-tfc21-ink/45">4:18</span></li>
        <li class="grid grid-cols-[28px_1fr_auto] items-center gap-3 rounded-md px-2 py-2.5 transition-colors duration-150 hover:bg-tfc21-neon/8"><span class="font-tfc21-mono text-[10px] tracking-[0.1em] text-tfc21-ink/45">02</span><span class="text-[13px] font-medium text-tfc21-ink">Cassette Memory</span><span class="font-tfc21-mono text-[11px] text-tfc21-ink/45">5:42</span></li>
        <li class="grid grid-cols-[28px_1fr_auto] items-center gap-3 rounded-md px-2 py-2.5 transition-colors duration-150 hover:bg-tfc21-neon/8"><span class="font-tfc21-mono text-[10px] tracking-[0.1em] text-tfc21-ink/45">03</span><span class="text-[13px] font-medium text-tfc21-ink">Static Bloom</span><span class="font-tfc21-mono text-[11px] text-tfc21-ink/45">3:55</span></li>
        <li class="grid grid-cols-[28px_1fr_auto] items-center gap-3 rounded-md px-2 py-2.5 transition-colors duration-150 hover:bg-tfc21-neon/8"><span class="font-tfc21-mono text-[10px] tracking-[0.1em] text-tfc21-ink/45">04</span><span class="text-[13px] font-medium text-tfc21-ink">2 AM in Tokyo</span><span class="font-tfc21-mono text-[11px] text-tfc21-ink/45">6:08</span></li>
        <li class="grid grid-cols-[28px_1fr_auto] items-center gap-3 rounded-md px-2 py-2.5 transition-colors duration-150 hover:bg-tfc21-neon/8"><span class="font-tfc21-mono text-[10px] tracking-[0.1em] text-tfc21-ink/45">05</span><span class="text-[13px] font-medium text-tfc21-ink">Lavender Static</span><span class="font-tfc21-mono text-[11px] text-tfc21-ink/45">4:33</span></li>
        <li class="grid grid-cols-[28px_1fr_auto] items-center gap-3 rounded-md px-2 py-2.5 transition-colors duration-150 hover:bg-tfc21-neon/8"><span class="font-tfc21-mono text-[10px] tracking-[0.1em] text-tfc21-ink/45">06</span><span class="text-[13px] font-medium text-tfc21-ink">After Midnight</span><span class="font-tfc21-mono text-[11px] text-tfc21-ink/45">13:36</span></li>
      </ol>
      <button type="button" class="relative z-30 mt-3.5 flex min-h-11 w-full items-center justify-center gap-2 rounded-lg border border-tfc21-neon/50 bg-linear-135 from-tfc21-neon/18 to-tfc21-violet/12 text-xs font-bold uppercase tracking-[0.25em] text-tfc21-neon transition-[background,box-shadow] duration-200 hover:from-tfc21-neon/30 hover:to-tfc21-violet/20 hover:shadow-[0_8px_24px_oklch(0.65_0.22_350/0.25)] focus-visible:outline-2 focus-visible:outline-tfc21-neon focus-visible:outline-offset-2">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="5 3 19 12 5 21 5 3"/></svg>
        Play full album
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc21-bg: #0a0612;
  --color-tfc21-bg: oklch(0.13 0.03 300);
  --color-tfc21-p1: #1e0b3b;
  --color-tfc21-p1: oklch(0.21 0.09 295);
  --color-tfc21-neon: #ec4899;
  --color-tfc21-neon: oklch(0.65 0.22 350);
  --color-tfc21-violet: #a21caf;
  --color-tfc21-violet: oklch(0.5 0.22 320);
  --color-tfc21-ink: #f5e8ff;
  --color-tfc21-ink: oklch(0.95 0.03 310);
  --font-tfc21-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tfc21-display: 'Playfair Display', Georgia, serif;
  --font-tfc21-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfc-21 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-21 * {
    transition-duration: 1ms !important;
  }
}
```
