---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-parallax-scroll-sections-with-scroll-driven-animations/"
title: "Tailwind Parallax Scroll Sections with Scroll-Driven Animations"
section: "layouts"
category: "tailwind-css-full-page-sections"
category_name: "Tailwind CSS Full Page Sections"
description: "Four full-viewport photo panels where the photograph, a colour wash and the headline each travel at a different rate as the panel crosses the scrollport…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Parallax Scroll Sections with Scroll-Driven Animations
Source: https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-parallax-scroll-sections-with-scroll-driven-animations/

Four full-viewport photo panels where the photograph, a colour wash and the headline each travel at a different rate as the panel crosses the scrollport &mdash; real depth from animation-timeline, no scroll listener and no bg-fixed (which simply doesn't work on iOS). Three one-class @utility layers do the work; under prefers-reduced-motion every layer locks into place.
## HTML
```html
<div class="tfps-07 relative isolate w-full min-h-svh bg-tfps07-bg font-tfps07-sans text-tfps07-ink antialiased [&_code]:font-tfps07-mono [&_code]:text-[.92em] text-white">
  <input class="peer sr-only" type="checkbox" id="tfps-07-theme">
  <label for="tfps-07-theme" class="fixed top-[1.15rem] right-[1.15rem] z-80 grid size-11 cursor-pointer place-items-center rounded-full border border-white/25 bg-black/30 text-white hover:bg-black/45 shadow-[0_8px_24px_-12px_var(--color-tfps07-shade)] backdrop-blur-[10px] backdrop-saturate-150 transition-[background-color,scale] duration-200 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-white forced-colors:border-[CanvasText]">
    <svg class="size-[1.05rem] tfps07-dark:hidden" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/></svg>
    <svg class="hidden size-[1.05rem] tfps07-dark:block" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="sr-only">Dim the photographs</span>
  </label>

  <div class="h-dvh overflow-x-hidden overflow-y-auto snap-y snap-mandatory scroll-smooth overscroll-y-contain [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-white [@media(max-height:40rem)]:snap-proximity motion-reduce:snap-none motion-reduce:scroll-auto" tabindex="0" role="group" aria-label="Parallax photo sections, four panels">

    <section class="[--h:205] [view-timeline-name:--tfps07] [view-timeline-axis:block] relative isolate flex min-h-dvh snap-start items-end overflow-hidden bg-[oklch(20%_.03_calc(var(--h)*1deg))] px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2.5rem,7vh,4.5rem)+3.5rem)] not-first:-mt-14 not-first:rounded-t-[2rem] not-first:border-t not-first:border-white/25 forced-colors:border-[CanvasText]" id="tfps-07-s1" aria-labelledby="tfps-07-h1">
      <img class="tfps07-back absolute inset-0 -z-20 size-full scale-[1.16] rounded-[inherit] object-cover transition-opacity duration-300 tfps07-dark:opacity-60" src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=1600&amp;auto=format" alt="Still alpine lake below a treeline ridge at dusk" width="1600" height="1067" loading="eager" fetchpriority="high" decoding="async">
      <span aria-hidden="true" class="tfps07-mid pointer-events-none absolute inset-x-0 -inset-y-[6%] -z-10 rounded-[inherit] bg-linear-to-t from-black/85 via-black/40 via-45% to-black/30 before:absolute before:inset-0 before:bg-[radial-gradient(120%_70%_at_12%_88%,oklch(52%_.17_calc(var(--h)*1deg)/.5),transparent_70%)] before:content-['']"></span>
      <div class="grid w-full max-w-[56rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] tfps07-fore transition-[opacity,translate] duration-700 ease-out starting:translate-y-4 starting:opacity-0 motion-reduce:transition-none">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps07-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-white">01 / 04</span><span class="rounded-[.45rem] border border-white/25 bg-black/30 px-2 py-[.22rem] font-tfps07-mono text-[.7rem] text-white/85 backdrop-blur-[6px]">tfps07-back &middot; tfps07-mid &middot; tfps07-fore</span></p>
        <h2 class="max-w-[20ch] text-[clamp(2.1rem,6.4vw,4.6rem)] leading-none font-semibold tracking-[-.045em] text-balance [text-shadow:0_2px_30px_rgb(0_0_0/.5)]" id="tfps-07-h1">Three layers, three rates, one scroll</h2>
        <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.16rem)] leading-[1.62] text-pretty text-white/85 [text-shadow:0_1px_18px_rgb(0_0_0/.6)] [&_code]:text-white">The photograph travels 18% of the panel height, the colour wash 8%, the type barely at all. Nothing here is timed &mdash; every layer is a pure function of how far this panel has crossed the screen.</p>
        <a href="#tfps-07-s2" class="inline-flex min-h-11 items-center gap-2.5 rounded-full pe-3 font-tfps07-mono text-[.82rem] text-white/85 no-underline [text-shadow:0_1px_18px_rgb(0_0_0/.6)] transition-colors hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"><svg class="size-[1.1rem] animate-tfps07-bob motion-reduce:animate-none" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Scroll slowly to see the layers separate</a>
      </div>
    </section>

    <section class="[--h:150] [view-timeline-name:--tfps07] [view-timeline-axis:block] relative isolate flex min-h-dvh snap-start items-end overflow-hidden bg-[oklch(20%_.03_calc(var(--h)*1deg))] px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2.5rem,7vh,4.5rem)+3.5rem)] not-first:-mt-14 not-first:rounded-t-[2rem] not-first:border-t not-first:border-white/25 forced-colors:border-[CanvasText]" id="tfps-07-s2" aria-labelledby="tfps-07-h2">
      <img class="tfps07-back absolute inset-0 -z-20 size-full scale-[1.16] rounded-[inherit] object-cover transition-opacity duration-300 tfps07-dark:opacity-60" src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=1600&amp;auto=format" alt="Fog drifting between tall conifers on a hillside" width="1600" height="1067" loading="lazy" decoding="async">
      <span aria-hidden="true" class="tfps07-mid pointer-events-none absolute inset-x-0 -inset-y-[6%] -z-10 rounded-[inherit] bg-linear-to-t from-black/85 via-black/40 via-45% to-black/30 before:absolute before:inset-0 before:bg-[radial-gradient(120%_70%_at_12%_88%,oklch(52%_.17_calc(var(--h)*1deg)/.5),transparent_70%)] before:content-['']"></span>
      <div class="grid w-full max-w-[56rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] tfps07-fore">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps07-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-white">02 / 04</span><span class="rounded-[.45rem] border border-white/25 bg-black/30 px-2 py-[.22rem] font-tfps07-mono text-[.7rem] text-white/85 backdrop-blur-[6px]">why not bg-fixed</span></p>
        <h2 class="max-w-[26ch] text-[clamp(1.7rem,4vw,3rem)] leading-[1.04] font-semibold tracking-[-.035em] text-balance [text-shadow:0_2px_30px_rgb(0_0_0/.5)]" id="tfps-07-h2">The fixed-background trick has always been broken</h2>
        <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.16rem)] leading-[1.62] text-pretty text-white/85 [text-shadow:0_1px_18px_rgb(0_0_0/.6)] [&_code]:text-white">iOS Safari ignores <code>bg-fixed</code> (<code>background-attachment: fixed</code>) entirely &mdash; the image just scrolls with the section &mdash; and Android Chrome repaints the whole layer every frame to honour it. A translating child stays on the compositor and behaves the same everywhere.</p>
        <pre class="w-full max-w-[36rem] overflow-x-auto overflow-y-hidden rounded-2xl border border-white/25 bg-black/40 px-[1.1rem] py-4 backdrop-blur-[8px]"><code class="text-[clamp(.76rem,1vw,.86rem)] leading-[1.7] whitespace-pre text-white/80 [&_mark]:bg-transparent [&_mark]:font-medium [&_mark]:text-white">&lt;section class="bg-fixed"&gt;          <mark>&lt;!-- no --&gt;</mark>
&lt;img class="tfps07-back scale-[1.16]"&gt; <mark>&lt;!-- yes --&gt;</mark></code></pre>
      </div>
    </section>

    <section class="[--h:262] [view-timeline-name:--tfps07] [view-timeline-axis:block] relative isolate flex min-h-dvh snap-start items-end overflow-hidden bg-[oklch(20%_.03_calc(var(--h)*1deg))] px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2.5rem,7vh,4.5rem)+3.5rem)] not-first:-mt-14 not-first:rounded-t-[2rem] not-first:border-t not-first:border-white/25 forced-colors:border-[CanvasText]" id="tfps-07-s3" aria-labelledby="tfps-07-h3">
      <img class="tfps07-back absolute inset-0 -z-20 size-full scale-[1.16] rounded-[inherit] object-cover transition-opacity duration-300 tfps07-dark:opacity-60" src="https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1600&amp;auto=format" alt="Snow-covered peak under a dense field of stars" width="1600" height="1067" loading="lazy" decoding="async">
      <span aria-hidden="true" class="tfps07-mid pointer-events-none absolute inset-x-0 -inset-y-[6%] -z-10 rounded-[inherit] bg-linear-to-t from-black/85 via-black/40 via-45% to-black/30 before:absolute before:inset-0 before:bg-[radial-gradient(120%_70%_at_12%_88%,oklch(52%_.17_calc(var(--h)*1deg)/.5),transparent_70%)] before:content-['']"></span>
      <div class="grid w-full max-w-[56rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] tfps07-fore">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps07-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-white">03 / 04</span><span class="rounded-[.45rem] border border-white/25 bg-black/30 px-2 py-[.22rem] font-tfps07-mono text-[.7rem] text-white/85 backdrop-blur-[6px]">the slack rule</span></p>
        <h2 class="max-w-[26ch] text-[clamp(1.7rem,4vw,3rem)] leading-[1.04] font-semibold tracking-[-.035em] text-balance [text-shadow:0_2px_30px_rgb(0_0_0/.5)]" id="tfps-07-h3">A layer that moves 9% needs 9% to spare</h2>
        <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.16rem)] leading-[1.62] text-pretty text-white/85 [text-shadow:0_1px_18px_rgb(0_0_0/.6)] [&_code]:text-white">Translate a full-bleed image without pre-scaling it and the panel's own background shows at the extremes of the range. The rule of thumb: <code>scale</code> at least 1&nbsp;+&nbsp;(2&nbsp;&times;&nbsp;amplitude), so &plusmn;9% travel wants <code>scale-[1.14]</code> or more.</p>
        <ul class="grid w-full max-w-[34rem] gap-1">
          <li class="grid grid-cols-[5rem_1fr] items-baseline gap-4 border-t border-white/25 py-2.5"><strong class="font-tfps07-mono text-[.78rem] font-medium tracking-[.06em] uppercase">photo</strong><span class="font-tfps07-mono text-[.84rem] text-white/80">&plusmn;9% travel &middot; scale-[1.16]</span></li>
          <li class="grid grid-cols-[5rem_1fr] items-baseline gap-4 border-t border-white/25 py-2.5"><strong class="font-tfps07-mono text-[.78rem] font-medium tracking-[.06em] uppercase">wash</strong><span class="font-tfps07-mono text-[.84rem] text-white/80">&plusmn;4% travel &middot; -inset-y-[6%]</span></li>
          <li class="grid grid-cols-[5rem_1fr] items-baseline gap-4 border-t border-white/25 py-2.5"><strong class="font-tfps07-mono text-[.78rem] font-medium tracking-[.06em] uppercase">type</strong><span class="font-tfps07-mono text-[.84rem] text-white/80">+3% &rarr; 0 &middot; fades in</span></li>
        </ul>
      </div>
    </section>

    <section class="[--h:95] [view-timeline-name:--tfps07] [view-timeline-axis:block] relative isolate flex min-h-dvh snap-start items-end overflow-hidden bg-[oklch(20%_.03_calc(var(--h)*1deg))] px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2.5rem,7vh,4.5rem)+3.5rem)] not-first:-mt-14 not-first:rounded-t-[2rem] not-first:border-t not-first:border-white/25 forced-colors:border-[CanvasText]" id="tfps-07-s4" aria-labelledby="tfps-07-h4">
      <img class="tfps07-back absolute inset-0 -z-20 size-full scale-[1.16] rounded-[inherit] object-cover transition-opacity duration-300 tfps07-dark:opacity-60" src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1600&amp;auto=format" alt="Sunlight breaking through a stand of tall birch trees" width="1600" height="1067" loading="lazy" decoding="async">
      <span aria-hidden="true" class="tfps07-mid pointer-events-none absolute inset-x-0 -inset-y-[6%] -z-10 rounded-[inherit] bg-linear-to-t from-black/85 via-black/40 via-45% to-black/30 before:absolute before:inset-0 before:bg-[radial-gradient(120%_70%_at_12%_88%,oklch(52%_.17_calc(var(--h)*1deg)/.5),transparent_70%)] before:content-['']"></span>
      <div class="grid w-full max-w-[56rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] tfps07-fore">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps07-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-white">04 / 04</span><span class="rounded-[.45rem] border border-white/25 bg-black/30 px-2 py-[.22rem] font-tfps07-mono text-[.7rem] text-white/85 backdrop-blur-[6px]">motion-reduce</span></p>
        <h2 class="max-w-[26ch] text-[clamp(1.7rem,4vw,3rem)] leading-[1.04] font-semibold tracking-[-.035em] text-balance [text-shadow:0_2px_30px_rgb(0_0_0/.5)]" id="tfps-07-h4">Reduced motion means fully static</h2>
        <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.16rem)] leading-[1.62] text-pretty text-white/85 [text-shadow:0_1px_18px_rgb(0_0_0/.6)] [&_code]:text-white">Parallax is one of the most reliable ways to make a reader queasy. Every layer utility is wrapped in <code>prefers-reduced-motion: no-preference</code>, and the scroller carries <code>motion-reduce:snap-none</code> &mdash; what is left is four photographic panels and nothing that moves.</p>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfps07-bg: #0b0f14;
  --color-tfps07-bg: oklch(0.167 0.012 254.2);
  --color-tfps07-ink: #ffffff;
  --color-tfps07-ink: oklch(1 0 0);
  --color-tfps07-acc: #ffffff;
  --color-tfps07-acc: oklch(1 0 0);
  --color-tfps07-shade: rgb(0 0 0 / .5);
  --font-tfps07-sans: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tfps07-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace;
  --animate-tfps07-bob: tfps07-bob 2.4s ease-in-out infinite;

  @keyframes tfps07-bob {
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

@custom-variant tfps07-dark {
  @media (prefers-color-scheme: light) {
    &:where(.tfps-07:has(#tfps-07-theme:checked), .tfps-07:has(#tfps-07-theme:checked) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: dark) {
    &:where(.tfps-07:not(:has(#tfps-07-theme:checked)), .tfps-07:not(:has(#tfps-07-theme:checked)) *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, stated before the browser build compiles, photographic, so dark by nature: the toggle dims the photos. */

.tfps-07 {
  width: 100%;
  min-height: 100svh;
}
/* What stayed CSS: the three parallax layers. Each is one @utility so the animation shorthand,
   the named timeline and the range are declared in order, and gated on support + motion preference. */

@keyframes tfps07-back {
  from {
    translate: 0 -9%;
  }

  to {
    translate: 0 9%;
  }
}

@keyframes tfps07-mid {
  from {
    translate: 0 -4%;
  }

  to {
    translate: 0 4%;
  }
}

@keyframes tfps07-fore {
  from {
    translate: 0 3%;
    opacity: .4;
  }

  60%,
    to {
    translate: 0 0;
    opacity: 1;
  }
}

@utility tfps07-back {
  @supports (animation-timeline: view()) {
    @media (prefers-reduced-motion: no-preference) {
      animation: tfps07-back linear both;
      animation-timeline: --tfps07;
      animation-range: cover 0% cover 100%;
    }
  }
}

@utility tfps07-mid {
  @supports (animation-timeline: view()) {
    @media (prefers-reduced-motion: no-preference) {
      animation: tfps07-mid linear both;
      animation-timeline: --tfps07;
      animation-range: cover 0% cover 100%;
    }
  }
}

@utility tfps07-fore {
  @supports (animation-timeline: view()) {
    @media (prefers-reduced-motion: no-preference) {
      animation: tfps07-fore linear both;
      animation-timeline: --tfps07;
      animation-range: cover 12% cover 62%;
    }
  }
}
```
