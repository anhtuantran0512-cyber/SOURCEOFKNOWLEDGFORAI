---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-responsive-flip-card-grid-per-card-perspective/"
title: "Tailwind Responsive Flip Card Grid with Per-Card 3D Perspective"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "Six portfolio cards in a grid that reflows 3&rarr;2&rarr;1 with one auto-fit track, each holding its own perspective so no card at the edge of a wide row skews."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Responsive Flip Card Grid with Per-Card 3D Perspective
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-responsive-flip-card-grid-per-card-perspective/

Six portfolio cards in a grid that reflows 3&rarr;2&rarr;1 with one auto-fit track, each holding its own perspective so no card at the edge of a wide row skews. Every card flips independently, which turns the grid from a hover toy into something you can actually read: open three, compare them, tab through the rest.
## HTML
```html
<section class="tfc-18 w-full min-h-svh bg-tfc18-bg font-tfc18-sans px-5 pt-10 pb-15 text-tfc18-ink">
  <header class="mb-9 text-center">
    <h2 class="text-xl font-extrabold tracking-[-0.015em] text-white">Responsive flip card matrix</h2>
    <p class="mt-1.5 text-xs text-tfc18-muted">Three columns, two, then one &mdash; one <code>auto-fit</code> track, per-card perspective, every card independently flippable</p>
  </header>

  <ul class="mx-auto grid max-w-[960px] grid-cols-[repeat(auto-fit,minmax(260px,1fr))] gap-5">

    <li class="group relative h-[270px] [perspective:1000px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc18-indigo has-[:focus-visible]:outline-offset-4">
      <input id="tfc-18-1" type="checkbox" class="peer sr-only"><label for="tfc-18-1" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show details for Token Architecture</span></label>
      <div class="relative h-full w-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">
        <div class="absolute inset-0 flex flex-col rounded-2xl overflow-hidden border border-white/8 bg-linear-145 from-tfc18-i1 to-tfc18-bg p-6 [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <span aria-hidden="true" class="absolute top-4 right-4.5 text-[32px] font-black italic leading-none text-white/7">01</span>
          <p class="mb-2.5 text-[9px] font-bold uppercase tracking-[0.15em] text-tfc18-indigoL">Design systems</p>
          <span class="mb-2.5 grid size-9 place-items-center rounded-lg border border-tfc18-indigo/25 bg-tfc18-indigo/12"><svg viewBox="0 0 24 24" class="size-4.5 fill-none stroke-tfc18-indigoL stroke-[1.8]" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 3v18M3 12h18"/></svg></span>
          <h3 class="text-[17px] font-extrabold leading-tight text-white">Token Architecture</h3>
          <p class="mt-1.5 text-xs leading-[1.5] text-tfc18-indigoP">Scalable design token system</p>
          <p class="mt-auto text-[9px] tracking-[0.08em] text-tfc18-dim">Hover, tap or press Space</p>
        </div>
        <div class="absolute inset-0 flex flex-col gap-2.5 rounded-2xl overflow-hidden border border-white/10 bg-linear-145 from-tfc18-i1 to-tfc18-i2 p-5 [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <p class="text-[9px] font-bold uppercase tracking-[0.14em] text-tfc18-indigoL">Design systems</p>
          <h3 class="text-[15px] font-extrabold leading-tight text-white">Token Architecture</h3>
          <ul class="flex flex-1 flex-col gap-1.5 text-[11px] text-tfc18-ink/70">
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-indigo">Semantic colour layers</li>
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-indigo">Typography scale (clamp)</li>
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-indigo">Multi-brand theming</li>
          </ul>
          <a href="#" class="relative z-30 flex min-h-11 items-center justify-center rounded-xl bg-linear-135 from-tfc18-indigo to-tfc18-indigoD text-xs font-bold tracking-[0.04em] text-white no-underline transition-opacity duration-200 hover:opacity-85 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">View project</a>
        </div>
      </div>
    </li>

    <li class="group relative h-[270px] [perspective:1000px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc18-green has-[:focus-visible]:outline-offset-4">
      <input id="tfc-18-2" type="checkbox" class="peer sr-only"><label for="tfc-18-2" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show details for Core Web Vitals</span></label>
      <div class="relative h-full w-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">
        <div class="absolute inset-0 flex flex-col rounded-2xl overflow-hidden border border-white/8 bg-linear-145 from-tfc18-g1 to-tfc18-g2 p-6 [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <span aria-hidden="true" class="absolute top-4 right-4.5 text-[32px] font-black italic leading-none text-white/7">02</span>
          <p class="mb-2.5 text-[9px] font-bold uppercase tracking-[0.15em] text-tfc18-greenL">Web performance</p>
          <span class="mb-2.5 grid size-9 place-items-center rounded-lg border border-tfc18-green/25 bg-tfc18-green/12"><svg viewBox="0 0 24 24" class="size-4.5 fill-none stroke-tfc18-greenL stroke-[1.8]" aria-hidden="true"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg></span>
          <h3 class="text-[17px] font-extrabold leading-tight text-white">Core Web Vitals</h3>
          <p class="mt-1.5 text-xs leading-[1.5] text-tfc18-greenP">LCP under 1.2s in production</p>
          <p class="mt-auto text-[9px] tracking-[0.08em] text-tfc18-dim">Hover, tap or press Space</p>
        </div>
        <div class="absolute inset-0 flex flex-col gap-2.5 rounded-2xl overflow-hidden border border-white/10 bg-linear-145 from-tfc18-g1 to-tfc18-g3 p-5 [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <p class="text-[9px] font-bold uppercase tracking-[0.14em] text-tfc18-greenL">Web performance</p>
          <h3 class="text-[15px] font-extrabold leading-tight text-white">Core Web Vitals</h3>
          <ul class="flex flex-1 flex-col gap-1.5 text-[11px] text-tfc18-ink/70">
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-green">LCP 1.1s at p75</li>
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-green">INP under 60ms</li>
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-green">CLS 0.01</li>
          </ul>
          <a href="#" class="relative z-30 flex min-h-11 items-center justify-center rounded-xl bg-linear-135 from-tfc18-green to-tfc18-greenD text-xs font-bold tracking-[0.04em] text-black no-underline transition-opacity duration-200 hover:opacity-85 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Case study</a>
        </div>
      </div>
    </li>

    <li class="group relative h-[270px] [perspective:1000px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc18-rose has-[:focus-visible]:outline-offset-4">
      <input id="tfc-18-3" type="checkbox" class="peer sr-only"><label for="tfc-18-3" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show details for the WCAG 2.2 AA audit</span></label>
      <div class="relative h-full w-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">
        <div class="absolute inset-0 flex flex-col rounded-2xl overflow-hidden border border-white/8 bg-linear-145 from-tfc18-r1 to-tfc18-r2 p-6 [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <span aria-hidden="true" class="absolute top-4 right-4.5 text-[32px] font-black italic leading-none text-white/7">03</span>
          <p class="mb-2.5 text-[9px] font-bold uppercase tracking-[0.15em] text-tfc18-roseL">Accessibility</p>
          <span class="mb-2.5 grid size-9 place-items-center rounded-lg border border-tfc18-rose/25 bg-tfc18-rose/12"><svg viewBox="0 0 24 24" class="size-4.5 fill-none stroke-tfc18-roseL stroke-[1.8]" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8v8M8 12h8"/></svg></span>
          <h3 class="text-[17px] font-extrabold leading-tight text-white">WCAG 2.2 AA audit</h3>
          <p class="mt-1.5 text-xs leading-[1.5] text-tfc18-roseP">Full accessibility review</p>
          <p class="mt-auto text-[9px] tracking-[0.08em] text-tfc18-dim">Hover, tap or press Space</p>
        </div>
        <div class="absolute inset-0 flex flex-col gap-2.5 rounded-2xl overflow-hidden border border-white/10 bg-linear-145 from-tfc18-r1 to-tfc18-r3 p-5 [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <p class="text-[9px] font-bold uppercase tracking-[0.14em] text-tfc18-roseL">Accessibility</p>
          <h3 class="text-[15px] font-extrabold leading-tight text-white">WCAG 2.2 AA audit</h3>
          <ul class="flex flex-1 flex-col gap-1.5 text-[11px] text-tfc18-ink/70">
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-rose">Colour contrast 4.5:1+</li>
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-rose">Full keyboard flow</li>
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-rose">ARIA landmark audit</li>
          </ul>
          <a href="#" class="relative z-30 flex min-h-11 items-center justify-center rounded-xl bg-linear-135 from-tfc18-rose to-tfc18-roseD text-xs font-bold tracking-[0.04em] text-white no-underline transition-opacity duration-200 hover:opacity-85 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Read report</a>
        </div>
      </div>
    </li>

    <li class="group relative h-[270px] [perspective:1000px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc18-amber has-[:focus-visible]:outline-offset-4">
      <input id="tfc-18-4" type="checkbox" class="peer sr-only"><label for="tfc-18-4" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show details for the Motion Library</span></label>
      <div class="relative h-full w-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">
        <div class="absolute inset-0 flex flex-col rounded-2xl overflow-hidden border border-white/8 bg-linear-145 from-tfc18-a1 to-tfc18-a2 p-6 [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <span aria-hidden="true" class="absolute top-4 right-4.5 text-[32px] font-black italic leading-none text-white/7">04</span>
          <p class="mb-2.5 text-[9px] font-bold uppercase tracking-[0.15em] text-tfc18-amberL">Animation</p>
          <span class="mb-2.5 grid size-9 place-items-center rounded-lg border border-tfc18-amber/25 bg-tfc18-amber/12"><svg viewBox="0 0 24 24" class="size-4.5 fill-none stroke-tfc18-amberL stroke-[1.8]" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m10 9 5 3-5 3z"/></svg></span>
          <h3 class="text-[17px] font-extrabold leading-tight text-white">Motion Library</h3>
          <p class="mt-1.5 text-xs leading-[1.5] text-tfc18-amberP">60fps CSS keyframe suite</p>
          <p class="mt-auto text-[9px] tracking-[0.08em] text-tfc18-dim">Hover, tap or press Space</p>
        </div>
        <div class="absolute inset-0 flex flex-col gap-2.5 rounded-2xl overflow-hidden border border-white/10 bg-linear-145 from-tfc18-a1 to-tfc18-a3 p-5 [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <p class="text-[9px] font-bold uppercase tracking-[0.14em] text-tfc18-amberL">Animation</p>
          <h3 class="text-[15px] font-extrabold leading-tight text-white">Motion Library</h3>
          <ul class="flex flex-1 flex-col gap-1.5 text-[11px] text-tfc18-ink/70">
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-amber">48 keyframe demos</li>
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-amber">Reduced-motion safe</li>
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-amber">Zero JS dependencies</li>
          </ul>
          <a href="#" class="relative z-30 flex min-h-11 items-center justify-center rounded-xl bg-linear-135 from-tfc18-amber to-tfc18-amberD text-xs font-bold tracking-[0.04em] text-black no-underline transition-opacity duration-200 hover:opacity-85 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Browse library</a>
        </div>
      </div>
    </li>

    <li class="group relative h-[270px] [perspective:1000px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc18-cyan has-[:focus-visible]:outline-offset-4">
      <input id="tfc-18-5" type="checkbox" class="peer sr-only"><label for="tfc-18-5" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show details for the micro-frontend architecture</span></label>
      <div class="relative h-full w-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">
        <div class="absolute inset-0 flex flex-col rounded-2xl overflow-hidden border border-white/8 bg-linear-145 from-tfc18-c1 to-tfc18-c2 p-6 [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <span aria-hidden="true" class="absolute top-4 right-4.5 text-[32px] font-black italic leading-none text-white/7">05</span>
          <p class="mb-2.5 text-[9px] font-bold uppercase tracking-[0.15em] text-tfc18-cyanL">Architecture</p>
          <span class="mb-2.5 grid size-9 place-items-center rounded-lg border border-tfc18-cyan/25 bg-tfc18-cyan/12"><svg viewBox="0 0 24 24" class="size-4.5 fill-none stroke-tfc18-cyanL stroke-[1.8]" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg></span>
          <h3 class="text-[17px] font-extrabold leading-tight text-white">Micro-frontend</h3>
          <p class="mt-1.5 text-xs leading-[1.5] text-tfc18-cyanP">Module federation at scale</p>
          <p class="mt-auto text-[9px] tracking-[0.08em] text-tfc18-dim">Hover, tap or press Space</p>
        </div>
        <div class="absolute inset-0 flex flex-col gap-2.5 rounded-2xl overflow-hidden border border-white/10 bg-linear-145 from-tfc18-c1 to-tfc18-c3 p-5 [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <p class="text-[9px] font-bold uppercase tracking-[0.14em] text-tfc18-cyanL">Architecture</p>
          <h3 class="text-[15px] font-extrabold leading-tight text-white">Micro-frontend</h3>
          <ul class="flex flex-1 flex-col gap-1.5 text-[11px] text-tfc18-ink/70">
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-cyan">Module federation</li>
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-cyan">Shared runtime deps</li>
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-cyan">12 independent teams</li>
          </ul>
          <a href="#" class="relative z-30 flex min-h-11 items-center justify-center rounded-xl bg-linear-135 from-tfc18-cyan to-tfc18-cyanD text-xs font-bold tracking-[0.04em] text-white no-underline transition-opacity duration-200 hover:opacity-85 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Architecture docs</a>
        </div>
      </div>
    </li>

    <li class="group relative h-[270px] [perspective:1000px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc18-violet has-[:focus-visible]:outline-offset-4">
      <input id="tfc-18-6" type="checkbox" class="peer sr-only"><label for="tfc-18-6" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show details for the E2E test suite</span></label>
      <div class="relative h-full w-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">
        <div class="absolute inset-0 flex flex-col rounded-2xl overflow-hidden border border-white/8 bg-linear-145 from-tfc18-v1 to-tfc18-v2 p-6 [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <span aria-hidden="true" class="absolute top-4 right-4.5 text-[32px] font-black italic leading-none text-white/7">06</span>
          <p class="mb-2.5 text-[9px] font-bold uppercase tracking-[0.15em] text-tfc18-violetL">Testing</p>
          <span class="mb-2.5 grid size-9 place-items-center rounded-lg border border-tfc18-violet/25 bg-tfc18-violet/12"><svg viewBox="0 0 24 24" class="size-4.5 fill-none stroke-tfc18-violetL stroke-[1.8]" aria-hidden="true"><path d="M9 3v7L4 20h16L15 10V3"/><path d="M8 3h8"/></svg></span>
          <h3 class="text-[17px] font-extrabold leading-tight text-white">E2E test suite</h3>
          <p class="mt-1.5 text-xs leading-[1.5] text-tfc18-violetP">Playwright plus CI pipeline</p>
          <p class="mt-auto text-[9px] tracking-[0.08em] text-tfc18-dim">Hover, tap or press Space</p>
        </div>
        <div class="absolute inset-0 flex flex-col gap-2.5 rounded-2xl overflow-hidden border border-white/10 bg-linear-145 from-tfc18-v1 to-tfc18-v3 p-5 [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
          <p class="text-[9px] font-bold uppercase tracking-[0.14em] text-tfc18-violetL">Testing</p>
          <h3 class="text-[15px] font-extrabold leading-tight text-white">E2E test suite</h3>
          <ul class="flex flex-1 flex-col gap-1.5 text-[11px] text-tfc18-ink/70">
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-violet">98% critical path coverage</li>
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-violet">Cross-browser parallel runs</li>
            <li class="flex items-center gap-2 before:size-1 before:shrink-0 before:rounded-full before:bg-tfc18-violet">Visual regression gates</li>
          </ul>
          <a href="#" class="relative z-30 flex min-h-11 items-center justify-center rounded-xl bg-linear-135 from-tfc18-violet to-tfc18-violetD text-xs font-bold tracking-[0.04em] text-white no-underline transition-opacity duration-200 hover:opacity-85 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">View suite</a>
        </div>
      </div>
    </li>

  </ul>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc18-bg: #07080f;
  --color-tfc18-bg: oklch(0.13 0.015 275);
  --color-tfc18-i1: #0e0f28;
  --color-tfc18-i1: oklch(0.18 0.05 275);
  --color-tfc18-i2: #090a1a;
  --color-tfc18-i2: oklch(0.15 0.035 275);
  --color-tfc18-g1: #071a0e;
  --color-tfc18-g1: oklch(0.19 0.05 150);
  --color-tfc18-g2: #04100a;
  --color-tfc18-g2: oklch(0.14 0.03 150);
  --color-tfc18-g3: #030c07;
  --color-tfc18-g3: oklch(0.12 0.025 150);
  --color-tfc18-r1: #1a0710;
  --color-tfc18-r1: oklch(0.18 0.06 355);
  --color-tfc18-r2: #0e0408;
  --color-tfc18-r2: oklch(0.13 0.035 355);
  --color-tfc18-r3: #0a0306;
  --color-tfc18-r3: oklch(0.11 0.03 355);
  --color-tfc18-a1: #1a1000;
  --color-tfc18-a1: oklch(0.19 0.05 75);
  --color-tfc18-a2: #0e0900;
  --color-tfc18-a2: oklch(0.14 0.03 75);
  --color-tfc18-a3: #0a0700;
  --color-tfc18-a3: oklch(0.12 0.025 75);
  --color-tfc18-c1: #041618;
  --color-tfc18-c1: oklch(0.18 0.04 205);
  --color-tfc18-c2: #020e10;
  --color-tfc18-c2: oklch(0.13 0.025 205);
  --color-tfc18-c3: #020c0e;
  --color-tfc18-c3: oklch(0.12 0.02 205);
  --color-tfc18-v1: #120820;
  --color-tfc18-v1: oklch(0.18 0.06 300);
  --color-tfc18-v2: #0a0414;
  --color-tfc18-v2: oklch(0.13 0.04 300);
  --color-tfc18-v3: #08031a;
  --color-tfc18-v3: oklch(0.12 0.045 295);
  --color-tfc18-indigo: #6366f1;
  --color-tfc18-indigo: oklch(0.58 0.2 280);
  --color-tfc18-indigoD: #4f46e5;
  --color-tfc18-indigoD: oklch(0.51 0.22 275);
  --color-tfc18-indigoL: #818cf8;
  --color-tfc18-indigoL: oklch(0.68 0.16 280);
  --color-tfc18-indigoP: #c7d2fe;
  --color-tfc18-indigoP: oklch(0.86 0.07 280);
  --color-tfc18-green: #22c55e;
  --color-tfc18-green: oklch(0.73 0.18 150);
  --color-tfc18-greenD: #16a34a;
  --color-tfc18-greenD: oklch(0.63 0.16 150);
  --color-tfc18-greenL: #4ade80;
  --color-tfc18-greenL: oklch(0.8 0.17 152);
  --color-tfc18-greenP: #bbf7d0;
  --color-tfc18-greenP: oklch(0.92 0.08 155);
  --color-tfc18-rose: #f43f5e;
  --color-tfc18-rose: oklch(0.65 0.22 15);
  --color-tfc18-roseD: #e11d48;
  --color-tfc18-roseD: oklch(0.58 0.22 15);
  --color-tfc18-roseL: #fb7185;
  --color-tfc18-roseL: oklch(0.72 0.17 15);
  --color-tfc18-roseP: #fecdd3;
  --color-tfc18-roseP: oklch(0.9 0.05 10);
  --color-tfc18-amber: #f59e0b;
  --color-tfc18-amber: oklch(0.77 0.16 70);
  --color-tfc18-amberD: #d97706;
  --color-tfc18-amberD: oklch(0.68 0.16 60);
  --color-tfc18-amberL: #fbbf24;
  --color-tfc18-amberL: oklch(0.83 0.16 82);
  --color-tfc18-amberP: #fde68a;
  --color-tfc18-amberP: oklch(0.92 0.09 90);
  --color-tfc18-cyan: #06b6d4;
  --color-tfc18-cyan: oklch(0.7 0.14 205);
  --color-tfc18-cyanD: #0284c7;
  --color-tfc18-cyanD: oklch(0.57 0.15 235);
  --color-tfc18-cyanL: #22d3ee;
  --color-tfc18-cyanL: oklch(0.78 0.13 200);
  --color-tfc18-cyanP: #a5f3fc;
  --color-tfc18-cyanP: oklch(0.9 0.07 200);
  --color-tfc18-violet: #a855f7;
  --color-tfc18-violet: oklch(0.65 0.22 300);
  --color-tfc18-violetD: #7c3aed;
  --color-tfc18-violetD: oklch(0.55 0.24 295);
  --color-tfc18-violetL: #c084fc;
  --color-tfc18-violetL: oklch(0.75 0.17 300);
  --color-tfc18-violetP: #e9d5ff;
  --color-tfc18-violetP: oklch(0.91 0.06 300);
  --color-tfc18-ink: #eef2ff;
  --color-tfc18-ink: oklch(0.96 0.015 280);
  --color-tfc18-muted: #a5aac4;
  --color-tfc18-muted: oklch(0.74 0.03 280);
  --color-tfc18-dim: #82869c;
  --color-tfc18-dim: oklch(0.62 0.025 280);
  --font-tfc18-sans: 'Sora', system-ui, sans-serif;
}

.tfc-18 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-18 * {
    transition-duration: 1ms !important;
  }
}
```
