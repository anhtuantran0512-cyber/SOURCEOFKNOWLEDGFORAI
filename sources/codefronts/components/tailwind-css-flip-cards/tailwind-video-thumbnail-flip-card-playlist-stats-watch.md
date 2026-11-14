---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-video-thumbnail-flip-card-playlist-stats-watch/"
title: "Tailwind Video Thumbnail Flip Card with Playlist, Stats & Watch CTA"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A video entry: poster, runtime badge and channel row on the front; description, three stats and a three-lesson playlist on the back."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Video Thumbnail Flip Card with Playlist, Stats & Watch CTA
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-video-thumbnail-flip-card-playlist-stats-watch/

A video entry: poster, runtime badge and channel row on the front; description, three stats and a three-lesson playlist on the back. The port swaps the fixed 210px poster for aspect-video, which is the utility layer doing something the hand-written CSS quietly never did &mdash; guaranteeing the thumbnail's ratio at any card width.
## HTML
```html
<section class="tfc-10 w-full min-h-svh grid place-items-center bg-tfc10-bg font-tfc10-sans px-5 py-10 text-tfc10-ink">
  <div class="group relative w-[360px] max-w-full h-[430px] [perspective:1200px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc10-red has-[:focus-visible]:outline-offset-4">
    <input id="tfc-10-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-10-flip" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show description and playlist for this video</span></label>

    <div class="relative w-full h-full transition-transform duration-[750ms] ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">

      <div class="absolute inset-0 flex flex-col rounded-2xl overflow-hidden bg-tfc10-panel border border-tfc10-red/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.5_0.2_25/0.35)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <div class="relative w-full shrink-0 aspect-video overflow-hidden bg-linear-160 from-tfc10-stage to-tfc10-stage2">
          <svg class="absolute inset-0 size-full" viewBox="0 0 360 210" preserveAspectRatio="xMidYMid slice" fill="none" aria-hidden="true">
            <defs><linearGradient id="tfc-10-code" x1="0" y1="0" x2="0" y2="210" gradientUnits="userSpaceOnUse"><stop stop-color="#0d1117"/><stop offset="1" stop-color="#161b22"/></linearGradient></defs>
            <rect width="360" height="210" fill="url(#tfc-10-code)"/>
            <rect x="20" y="20" width="320" height="8" rx="4" fill="oklch(0.63 0.22 25 / 0.5)"/>
            <rect x="20" y="36" width="240" height="6" rx="3" fill="oklch(0.7 0.19 45 / 0.4)"/>
            <rect x="40" y="52" width="200" height="6" rx="3" fill="oklch(0.63 0.2 295 / 0.4)"/>
            <rect x="40" y="68" width="280" height="6" rx="3" fill="oklch(0.73 0.18 150 / 0.3)"/>
            <rect x="60" y="84" width="160" height="6" rx="3" fill="oklch(0.7 0.15 230 / 0.4)"/>
            <rect x="60" y="100" width="220" height="6" rx="3" fill="oklch(0.83 0.16 82 / 0.3)"/>
            <rect x="40" y="116" width="180" height="6" rx="3" fill="oklch(0.63 0.2 295 / 0.3)"/>
            <rect x="20" y="132" width="260" height="6" rx="3" fill="oklch(0.7 0.19 45 / 0.4)"/>
            <rect x="20" y="148" width="120" height="6" rx="3" fill="oklch(0.63 0.22 25 / 0.5)"/>
            <rect width="360" height="210" fill="oklch(0 0 0 / 0.35)"/>
          </svg>
          <div class="absolute inset-0 grid place-items-center bg-black/30">
            <span class="grid size-15 place-items-center rounded-full bg-tfc10-red/90 shadow-[0_0_30px_oklch(0.63_0.22_25/0.5)] transition-transform duration-300 group-hover:scale-105 motion-reduce:group-hover:scale-100">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="white" aria-hidden="true"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            </span>
          </div>
          <p class="absolute bottom-2.5 right-2.5 rounded bg-black/80 px-1.5 py-0.5 text-[11px] font-bold text-tfc10-ink">18:42</p>
        </div>
        <div class="flex items-center gap-2.5 px-4 pt-4 pb-2">
          <span class="grid size-8 shrink-0 place-items-center rounded-full bg-linear-135 from-tfc10-red to-tfc10-orange text-[13px] font-extrabold text-white">CF</span>
          <div>
            <p class="text-xs font-bold text-tfc10-ink/75">CodeFronts</p>
            <p class="text-[10px] text-tfc10-dim">248K subscribers</p>
          </div>
        </div>
        <h3 class="px-4 text-base font-extrabold leading-[1.4] tracking-[-0.01em] text-white text-pretty">Build a Full-Stack Auth System in 18 Minutes</h3>
        <p class="flex items-center gap-3 px-4 py-2.5 text-[11px] text-tfc10-dim"><span>1.4M views</span><span class="size-[3px] rounded-full bg-tfc10-dim"></span><span>3 months ago</span></p>
        <p class="mt-auto border-t border-white/5 px-4 py-3.5 text-[10px] tracking-[0.08em] text-tfc10-dim">Hover, tap or press Space for the description &rarr;</p>
      </div>

      <div class="absolute inset-0 flex flex-col gap-3.5 rounded-2xl overflow-hidden p-6 bg-linear-160 from-tfc10-back to-tfc10-back2 border border-tfc10-orange/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.55_0.18_45/0.35)] [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <h3 class="text-[10px] font-bold uppercase tracking-[0.15em] text-tfc10-orange">About this video</h3>
        <p class="text-[13px] leading-[1.7] text-tfc10-ink/65 text-pretty">In 18 minutes you'll build a production-ready JWT auth system with refresh tokens, protected routes, and Postgres storage &mdash; fully from scratch, zero magic libraries.</p>
        <dl class="flex gap-3">
          <div class="flex-1 rounded-xl border border-white/7 bg-white/4 p-3 text-center"><dd class="bg-linear-135 from-tfc10-red to-tfc10-orange bg-clip-text text-xl font-extrabold text-transparent">1.4M</dd><dt class="mt-0.5 text-[9px] uppercase tracking-[0.1em] text-tfc10-dim">Views</dt></div>
          <div class="flex-1 rounded-xl border border-white/7 bg-white/4 p-3 text-center"><dd class="bg-linear-135 from-tfc10-red to-tfc10-orange bg-clip-text text-xl font-extrabold text-transparent">98K</dd><dt class="mt-0.5 text-[9px] uppercase tracking-[0.1em] text-tfc10-dim">Likes</dt></div>
          <div class="flex-1 rounded-xl border border-white/7 bg-white/4 p-3 text-center"><dd class="bg-linear-135 from-tfc10-red to-tfc10-orange bg-clip-text text-xl font-extrabold text-transparent">18:42</dd><dt class="mt-0.5 text-[9px] uppercase tracking-[0.1em] text-tfc10-dim">Runtime</dt></div>
        </dl>
        <ol class="flex flex-col gap-2">
          <li class="flex items-center gap-2.5 rounded-lg border border-white/5 bg-white/3 px-2.5 py-2"><span class="grid size-5 shrink-0 place-items-center rounded-full bg-tfc10-red/15 text-[10px] font-bold text-tfc10-red">1</span><span class="flex-1 text-[11px] text-tfc10-ink/70">Project setup &amp; JWT basics</span><span class="text-[10px] text-tfc10-dim">4:12</span></li>
          <li class="flex items-center gap-2.5 rounded-lg border border-white/5 bg-white/3 px-2.5 py-2"><span class="grid size-5 shrink-0 place-items-center rounded-full bg-tfc10-red/15 text-[10px] font-bold text-tfc10-red">2</span><span class="flex-1 text-[11px] text-tfc10-ink/70">Refresh token strategy</span><span class="text-[10px] text-tfc10-dim">6:30</span></li>
          <li class="flex items-center gap-2.5 rounded-lg border border-white/5 bg-white/3 px-2.5 py-2"><span class="grid size-5 shrink-0 place-items-center rounded-full bg-tfc10-red/15 text-[10px] font-bold text-tfc10-red">3</span><span class="flex-1 text-[11px] text-tfc10-ink/70">Protected routes &amp; middleware</span><span class="text-[10px] text-tfc10-dim">8:00</span></li>
        </ol>
        <button type="button" class="relative z-30 mt-auto flex min-h-11 w-full items-center justify-center gap-2 rounded-xl bg-linear-135 from-tfc10-red to-tfc10-orange text-[13px] font-extrabold tracking-[0.04em] text-white transition-opacity duration-150 hover:opacity-90 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="white" aria-hidden="true"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          Watch now
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
  --color-tfc10-bg: #0c0800;
  --color-tfc10-bg: oklch(0.14 0.015 70);
  --color-tfc10-panel: #111111;
  --color-tfc10-panel: oklch(0.17 0.004 60);
  --color-tfc10-stage: #1a0800;
  --color-tfc10-stage: oklch(0.18 0.05 45);
  --color-tfc10-stage2: #0d1a2e;
  --color-tfc10-stage2: oklch(0.21 0.05 260);
  --color-tfc10-back: #1a0400;
  --color-tfc10-back: oklch(0.18 0.05 30);
  --color-tfc10-back2: #0e0e0e;
  --color-tfc10-back2: oklch(0.16 0.003 60);
  --color-tfc10-red: #ef4444;
  --color-tfc10-red: oklch(0.63 0.22 25);
  --color-tfc10-orange: #f97316;
  --color-tfc10-orange: oklch(0.7 0.19 45);
  --color-tfc10-ink: #fff7ed;
  --color-tfc10-ink: oklch(0.98 0.015 70);
  --color-tfc10-dim: #96897c;
  --color-tfc10-dim: oklch(0.65 0.02 70);
  --font-tfc10-sans: 'Sora', system-ui, sans-serif;
}

.tfc-10 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-10 * {
    transition-duration: 1ms !important;
  }
}
```
