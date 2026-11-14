---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-sticky-stacking-cards-on-scroll/"
title: "Tailwind Sticky Stacking Cards on Scroll"
section: "layouts"
category: "tailwind-css-full-page-sections"
category_name: "Tailwind CSS Full Page Sections"
description: "Five full-height sheets that pin at the top and stack over one another like a deck &mdash; each parking one labelled tab lower than the last, so the whole…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Stacking Cards on Scroll
Source: https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-sticky-stacking-cards-on-scroll/

Five full-height sheets that pin at the top and stack over one another like a deck &mdash; each parking one labelled tab lower than the last, so the whole deck reads as an index as you scroll. Built from sticky, one [--i:n] index class per panel and calc() arbitrary values for offset, height and z-order. No JavaScript, no scroll listeners.
## HTML
```html
<div class="tfps-04 relative isolate w-full min-h-svh bg-tfps04-bg font-tfps04-sans text-tfps04-ink antialiased [&_code]:font-tfps04-mono [&_code]:text-[.92em] [--step:2.25rem]">
  <input class="peer sr-only" type="checkbox" id="tfps-04-theme">
  <label for="tfps-04-theme" class="fixed top-[1.15rem] right-[1.15rem] z-80 grid size-11 cursor-pointer place-items-center rounded-full border border-tfps04-ink/10 bg-white/60 text-tfps04-ink hover:bg-white/85 tfps04-dark:bg-white/[.07] tfps04-dark:hover:bg-white/15 shadow-[0_8px_24px_-12px_var(--color-tfps04-shade)] backdrop-blur-[10px] backdrop-saturate-150 transition-[background-color,scale] duration-200 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tfps04-acc forced-colors:border-[CanvasText]">
    <svg class="size-[1.05rem] tfps04-dark:hidden" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/></svg>
    <svg class="hidden size-[1.05rem] tfps04-dark:block" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="sr-only">Switch light or dark theme</span>
  </label>

  <div class="h-dvh overflow-x-hidden overflow-y-auto snap-y snap-proximity scroll-smooth overscroll-y-contain [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps04-acc [@media(max-height:40rem)]:snap-proximity motion-reduce:snap-none motion-reduce:scroll-auto" tabindex="0" role="group" aria-label="Stacking panel sequence, five panels">
    <div class="relative">

      <section class="[--i:0] [--h:255] sticky top-[calc(var(--i)*var(--step))] z-[calc(var(--i)+1)] flex min-h-[calc(100dvh-var(--i)*var(--step))] snap-start items-center justify-center rounded-t-[1.9rem] border-t border-tfps04-ink/10 bg-[oklch(97%_.022_calc(var(--h)*1deg))] px-[clamp(1.25rem,5vw,4.5rem)] pt-[calc(var(--step)+clamp(1.5rem,4vh,3rem))] pb-[clamp(2.5rem,6vh,4rem)] shadow-[0_-22px_50px_-26px_var(--color-tfps04-shade)] tfps04-dark:bg-[oklch(19%_.03_calc(var(--h)*1deg))] forced-colors:border-[CanvasText]" id="tfps-04-s1" aria-labelledby="tfps-04-h1">
        <p aria-hidden="true" class="absolute inset-x-0 top-0 flex h-(--step) items-center gap-3 border-b border-tfps04-ink/[.06] px-[clamp(1.25rem,5vw,4.5rem)] font-tfps04-mono text-[.68rem] tracking-[.1em] uppercase text-[oklch(46%_.12_calc(var(--h)*1deg))] tfps04-dark:text-[oklch(84%_.1_calc(var(--h)*1deg))]"><span>01</span><span class="tracking-[.04em] normal-case text-tfps04-ink/60">Pin, then stack</span></p>
        <div class="grid w-full max-w-[60rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] transition-[opacity,translate] duration-700 ease-out starting:translate-y-4 starting:opacity-0 motion-reduce:transition-none">
          <p class="flex flex-wrap items-center gap-3"><span class="font-tfps04-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-[oklch(46%_.12_calc(var(--h)*1deg))] tfps04-dark:text-[oklch(84%_.1_calc(var(--h)*1deg))]">01 / 05</span><span class="rounded-[.45rem] border border-tfps04-ink/12 px-2 py-[.22rem] font-tfps04-mono text-[.7rem] text-tfps04-ink/75">sticky top-[calc(var(--i)*var(--step))]</span></p>
          <h2 class="max-w-[20ch] text-[clamp(2rem,5.6vw,4rem)] leading-[1.02] font-semibold tracking-[-.042em] text-balance" id="tfps-04-h1">Panels that pin, then stack</h2>
          <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps04-ink/75 [&_code]:text-tfps04-ink">Scroll once. This panel stays where it is while the next sheet rides over it, parking one tab lower so its label stays on screen. Five sheets, one <code>sticky</code> utility, no scroll listeners.</p>
          <a href="#tfps-04-s2" class="inline-flex min-h-11 items-center gap-2.5 rounded-full pe-3 font-tfps04-mono text-[.82rem] text-tfps04-ink/75 no-underline transition-colors hover:text-tfps04-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfps04-acc"><svg class="size-[1.1rem] animate-tfps04-bob motion-reduce:animate-none" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Scroll to build the deck</a>
        </div>
      </section>

      <section class="[--i:1] [--h:200] sticky top-[calc(var(--i)*var(--step))] z-[calc(var(--i)+1)] flex min-h-[calc(100dvh-var(--i)*var(--step))] snap-start items-center justify-center rounded-t-[1.9rem] border-t border-tfps04-ink/10 bg-[oklch(97%_.022_calc(var(--h)*1deg))] px-[clamp(1.25rem,5vw,4.5rem)] pt-[calc(var(--step)+clamp(1.5rem,4vh,3rem))] pb-[clamp(2.5rem,6vh,4rem)] shadow-[0_-22px_50px_-26px_var(--color-tfps04-shade)] tfps04-dark:bg-[oklch(19%_.03_calc(var(--h)*1deg))] forced-colors:border-[CanvasText]" id="tfps-04-s2" aria-labelledby="tfps-04-h2">
        <p aria-hidden="true" class="absolute inset-x-0 top-0 flex h-(--step) items-center gap-3 border-b border-tfps04-ink/[.06] px-[clamp(1.25rem,5vw,4.5rem)] font-tfps04-mono text-[.68rem] tracking-[.1em] uppercase text-[oklch(46%_.12_calc(var(--h)*1deg))] tfps04-dark:text-[oklch(84%_.1_calc(var(--h)*1deg))]"><span>02</span><span class="tracking-[.04em] normal-case text-tfps04-ink/60">The containing block</span></p>
        <div class="grid w-full max-w-[60rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
          <p class="flex flex-wrap items-center gap-3"><span class="font-tfps04-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-[oklch(46%_.12_calc(var(--h)*1deg))] tfps04-dark:text-[oklch(84%_.1_calc(var(--h)*1deg))]">02 / 05</span><span class="rounded-[.45rem] border border-tfps04-ink/12 px-2 py-[.22rem] font-tfps04-mono text-[.7rem] text-tfps04-ink/75">the containing block</span></p>
          <h2 class="max-w-[28ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-04-h2">Siblings in one wrapper stack. Nested ones do not.</h2>
          <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps04-ink/75 [&_code]:text-tfps04-ink">A sticky element stays pinned only while its own parent is on screen. Put all five panels in one wrapper and each stays pinned for the whole sequence &mdash; wrap each panel in its own box and every sheet unpins the moment its box scrolls away.</p>
          <ul class="grid w-full gap-1.5">
            <li class="grid gap-0.5 border-t border-tfps04-ink/10 py-3.5"><strong class="font-tfps04-mono text-[.82rem] font-medium">One wrapper</strong><span class="text-[.95rem] text-tfps04-ink/75">All five pins persist. This is the stack.</span></li>
            <li class="grid gap-0.5 border-t border-tfps04-ink/10 py-3.5"><strong class="font-tfps04-mono text-[.82rem] font-medium">One wrapper per panel</strong><span class="text-[.95rem] text-tfps04-ink/75">Each pin dies with its box. This is a plain scroller.</span></li>
          </ul>
        </div>
      </section>

      <section class="[--i:2] [--h:160] sticky top-[calc(var(--i)*var(--step))] z-[calc(var(--i)+1)] flex min-h-[calc(100dvh-var(--i)*var(--step))] snap-start items-center justify-center rounded-t-[1.9rem] border-t border-tfps04-ink/10 bg-[oklch(97%_.022_calc(var(--h)*1deg))] px-[clamp(1.25rem,5vw,4.5rem)] pt-[calc(var(--step)+clamp(1.5rem,4vh,3rem))] pb-[clamp(2.5rem,6vh,4rem)] shadow-[0_-22px_50px_-26px_var(--color-tfps04-shade)] tfps04-dark:bg-[oklch(19%_.03_calc(var(--h)*1deg))] forced-colors:border-[CanvasText]" id="tfps-04-s3" aria-labelledby="tfps-04-h3">
        <p aria-hidden="true" class="absolute inset-x-0 top-0 flex h-(--step) items-center gap-3 border-b border-tfps04-ink/[.06] px-[clamp(1.25rem,5vw,4.5rem)] font-tfps04-mono text-[.68rem] tracking-[.1em] uppercase text-[oklch(46%_.12_calc(var(--h)*1deg))] tfps04-dark:text-[oklch(84%_.1_calc(var(--h)*1deg))]"><span>03</span><span class="tracking-[.04em] normal-case text-tfps04-ink/60">Why proximity</span></p>
        <div class="grid w-full max-w-[60rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
          <p class="flex flex-wrap items-center gap-3"><span class="font-tfps04-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-[oklch(46%_.12_calc(var(--h)*1deg))] tfps04-dark:text-[oklch(84%_.1_calc(var(--h)*1deg))]">03 / 05</span><span class="rounded-[.45rem] border border-tfps04-ink/12 px-2 py-[.22rem] font-tfps04-mono text-[.7rem] text-tfps04-ink/75">why proximity</span></p>
          <h2 class="max-w-[28ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-04-h3">Mandatory snapping fights a pinned panel</h2>
          <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps04-ink/75 [&_code]:text-tfps04-ink">A pinned panel's snap edge sits at the top of the scrollport permanently, so <code>snap-mandatory</code> keeps pulling the scroll back to it. <code>snap-proximity</code> snaps only when the reader comes to rest near an edge &mdash; exactly what a stack wants.</p>
          <pre class="w-full overflow-x-auto overflow-y-hidden rounded-2xl border border-tfps04-ink/10 bg-tfps04-ink/[.04] px-[1.1rem] py-4 bg-white/60 tfps04-dark:bg-white/[.04]"><code class="text-[clamp(.78rem,1vw,.88rem)] leading-[1.75] whitespace-pre text-tfps04-ink/75 [&_mark]:rounded-[.25rem] [&_mark]:bg-tfps04-acc/15 [&_mark]:px-[.2rem] [&_mark]:text-tfps04-acc">&lt;div class="snap-y <mark>snap-proximity</mark>"&gt;
  &lt;section class="sticky top-[calc(var(--i)*var(--step))] snap-start"&gt;</code></pre>
        </div>
      </section>

      <section class="[--i:3] [--h:95] sticky top-[calc(var(--i)*var(--step))] z-[calc(var(--i)+1)] flex min-h-[calc(100dvh-var(--i)*var(--step))] snap-start items-center justify-center rounded-t-[1.9rem] border-t border-tfps04-ink/10 bg-[oklch(97%_.022_calc(var(--h)*1deg))] px-[clamp(1.25rem,5vw,4.5rem)] pt-[calc(var(--step)+clamp(1.5rem,4vh,3rem))] pb-[clamp(2.5rem,6vh,4rem)] shadow-[0_-22px_50px_-26px_var(--color-tfps04-shade)] tfps04-dark:bg-[oklch(19%_.03_calc(var(--h)*1deg))] forced-colors:border-[CanvasText]" id="tfps-04-s4" aria-labelledby="tfps-04-h4">
        <p aria-hidden="true" class="absolute inset-x-0 top-0 flex h-(--step) items-center gap-3 border-b border-tfps04-ink/[.06] px-[clamp(1.25rem,5vw,4.5rem)] font-tfps04-mono text-[.68rem] tracking-[.1em] uppercase text-[oklch(46%_.12_calc(var(--h)*1deg))] tfps04-dark:text-[oklch(84%_.1_calc(var(--h)*1deg))]"><span>04</span><span class="tracking-[.04em] normal-case text-tfps04-ink/60">The silent killers</span></p>
        <div class="grid w-full max-w-[60rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
          <p class="flex flex-wrap items-center gap-3"><span class="font-tfps04-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-[oklch(46%_.12_calc(var(--h)*1deg))] tfps04-dark:text-[oklch(84%_.1_calc(var(--h)*1deg))]">04 / 05</span><span class="rounded-[.45rem] border border-tfps04-ink/12 px-2 py-[.22rem] font-tfps04-mono text-[.7rem] text-tfps04-ink/75">the silent killers</span></p>
          <h2 class="max-w-[28ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-04-h4">Six things that quietly stop a panel pinning</h2>
          <ul class="grid w-full grid-cols-[repeat(auto-fit,minmax(11rem,1fr))] gap-2">
            <li class="rounded-[.8rem] border border-tfps04-ink/10 bg-white/60 px-3.5 py-3 font-tfps04-mono text-[.84rem] tfps04-dark:bg-white/[.04]">overflow-hidden</li>
            <li class="rounded-[.8rem] border border-tfps04-ink/10 bg-white/60 px-3.5 py-3 font-tfps04-mono text-[.84rem] tfps04-dark:bg-white/[.04]">overflow-auto</li>
            <li class="rounded-[.8rem] border border-tfps04-ink/10 bg-white/60 px-3.5 py-3 font-tfps04-mono text-[.84rem] tfps04-dark:bg-white/[.04]">overflow-scroll</li>
            <li class="rounded-[.8rem] border border-tfps04-ink/10 bg-white/60 px-3.5 py-3 font-tfps04-mono text-[.84rem] tfps04-dark:bg-white/[.04]">no top-*</li>
            <li class="rounded-[.8rem] border border-tfps04-ink/10 bg-white/60 px-3.5 py-3 font-tfps04-mono text-[.84rem] tfps04-dark:bg-white/[.04]">a wrapper per panel</li>
            <li class="rounded-[.8rem] border border-tfps04-ink/10 bg-white/60 px-3.5 py-3 font-tfps04-mono text-[.84rem] tfps04-dark:bg-white/[.04]">h-* on the stack</li>
          </ul>
          <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps04-ink/75 [&_code]:text-tfps04-ink">An <code>overflow-hidden</code> or <code>-auto</code> ancestor becomes the scroll container, so the panel sticks to <em>it</em> and never moves. Need clipping? Use <code>overflow-clip</code> &mdash; it clips without creating a scrollport, and sticky keeps working.</p>
        </div>
      </section>

      <section class="[--i:4] [--h:30] sticky top-[calc(var(--i)*var(--step))] z-[calc(var(--i)+1)] flex min-h-[calc(100dvh-var(--i)*var(--step))] snap-start items-center justify-center rounded-t-[1.9rem] border-t border-tfps04-ink/10 bg-[oklch(97%_.022_calc(var(--h)*1deg))] px-[clamp(1.25rem,5vw,4.5rem)] pt-[calc(var(--step)+clamp(1.5rem,4vh,3rem))] pb-[clamp(2.5rem,6vh,4rem)] shadow-[0_-22px_50px_-26px_var(--color-tfps04-shade)] tfps04-dark:bg-[oklch(19%_.03_calc(var(--h)*1deg))] forced-colors:border-[CanvasText]" id="tfps-04-s5" aria-labelledby="tfps-04-h5">
        <p aria-hidden="true" class="absolute inset-x-0 top-0 flex h-(--step) items-center gap-3 border-b border-tfps04-ink/[.06] px-[clamp(1.25rem,5vw,4.5rem)] font-tfps04-mono text-[.68rem] tracking-[.1em] uppercase text-[oklch(46%_.12_calc(var(--h)*1deg))] tfps04-dark:text-[oklch(84%_.1_calc(var(--h)*1deg))]"><span>05</span><span class="tracking-[.04em] normal-case text-tfps04-ink/60">The deck, complete</span></p>
        <div class="grid w-full max-w-[60rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
          <p class="flex flex-wrap items-center gap-3"><span class="font-tfps04-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-[oklch(46%_.12_calc(var(--h)*1deg))] tfps04-dark:text-[oklch(84%_.1_calc(var(--h)*1deg))]">05 / 05</span><span class="rounded-[.45rem] border border-tfps04-ink/12 px-2 py-[.22rem] font-tfps04-mono text-[.7rem] text-tfps04-ink/75">the deck, complete</span></p>
          <h2 class="max-w-[28ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-04-h5">Five sheets, one index variable</h2>
          <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps04-ink/75 [&_code]:text-tfps04-ink">Pin offset, panel height and stacking order all read from the same <code>[--i:n]</code> class on each section. Add a sixth panel with <code>[--i:5]</code> and the whole effect extends itself.</p>
          <figure class="grid max-w-[46ch] gap-2.5 border-s-2 border-tfps04-acc ps-[1.1rem]">
          <blockquote class="text-[clamp(1.05rem,1.9vw,1.35rem)] leading-[1.45] tracking-[-.02em] text-pretty"><p>&ldquo;The stack replaced three scroll listeners and a resize observer on our case-study template.&rdquo;</p></blockquote>
          <figcaption class="font-tfps04-mono text-[.68rem] tracking-[.1em] uppercase text-tfps04-ink/70">Jordan Lee &middot; design engineer</figcaption>
        </figure>
        </div>
      </section>

    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfps04-bg: #f4f6f8;
  --color-tfps04-bg: oklch(96.5% .006 220);
  --color-tfps04-ink: #0b1014;
  --color-tfps04-ink: oklch(14% .015 220);
  --color-tfps04-acc: #0d9488;
  --color-tfps04-acc: oklch(56% .12 185);
  --color-tfps04-shade: rgb(11 16 20 / .28);
  --font-tfps04-sans: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tfps04-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace;
  --animate-tfps04-bob: tfps04-bob 2.4s ease-in-out infinite;

  @keyframes tfps04-bob {
    0%,
        100% {
      translate: 0 -2px;
    }

    50% {
      translate: 0 3px;
    }
  }
}
/* Theme state. Dark = OS preference XOR the toggle, so the switch always flips what you see —
   the CSS original's checkbox did nothing for visitors whose OS was already dark. */

@custom-variant tfps04-dark {
  @media (prefers-color-scheme: light) {
    &:where(.tfps-04:has(#tfps-04-theme:checked), .tfps-04:has(#tfps-04-theme:checked) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: dark) {
    &:where(.tfps-04:not(:has(#tfps-04-theme:checked)), .tfps-04:not(:has(#tfps-04-theme:checked)) *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, stated before the browser build compiles. */

.tfps-04 {
  width: 100%;
  min-height: 100svh;

  @variant tfps04-dark {
    --color-tfps04-bg: #05080a;
    --color-tfps04-bg: oklch(0.131 0.008 232.1);
    --color-tfps04-ink: #eef4f6;
    --color-tfps04-ink: oklch(0.963 0.007 219.6);
    --color-tfps04-acc: #5eead4;
    --color-tfps04-acc: oklch(0.855 0.125 181.1);
    --color-tfps04-shade: rgb(0 0 0 / .85);
  }
}
```
