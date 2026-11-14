---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-full-page-section-reveal-and-scale-on-scroll/"
title: "Tailwind Full Page Section Reveal and Scale on Scroll"
section: "layouts"
category: "tailwind-css-full-page-sections"
category_name: "Tailwind CSS Full Page Sections"
description: "Each incoming sheet rises from 92% scale and 30% opacity to full size exactly as it snaps into place, holds perfectly still, then recedes the same way on the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full Page Section Reveal and Scale on Scroll
Source: https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-full-page-section-reveal-and-scale-on-scroll/

Each incoming sheet rises from 92% scale and 30% opacity to full size exactly as it snaps into place, holds perfectly still, then recedes the same way on the way out &mdash; one keyframe set, one tfps08-reveal utility, both halves of the transition. Only scale and opacity animate, and an oversized hue-tinted numeral gives every sheet depth.
## HTML
```html
<div class="tfps-08 relative isolate w-full min-h-svh bg-tfps08-bg font-tfps08-sans text-tfps08-ink antialiased [&_code]:font-tfps08-mono [&_code]:text-[.92em]">
  <input class="peer sr-only" type="checkbox" id="tfps-08-theme">
  <label for="tfps-08-theme" class="fixed top-[1.15rem] right-[1.15rem] z-80 grid size-11 cursor-pointer place-items-center rounded-full border border-tfps08-ink/10 bg-white/60 text-tfps08-ink hover:bg-white/85 tfps08-dark:bg-white/[.07] tfps08-dark:hover:bg-white/15 shadow-[0_8px_24px_-12px_var(--color-tfps08-shade)] backdrop-blur-[10px] backdrop-saturate-150 transition-[background-color,scale] duration-200 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tfps08-acc forced-colors:border-[CanvasText]">
    <svg class="size-[1.05rem] tfps08-dark:hidden" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/></svg>
    <svg class="hidden size-[1.05rem] tfps08-dark:block" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="sr-only">Switch light or dark theme</span>
  </label>

  <div class="h-dvh overflow-x-hidden overflow-y-auto snap-y snap-mandatory scroll-smooth overscroll-y-contain [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps08-acc [@media(max-height:40rem)]:snap-proximity motion-reduce:snap-none motion-reduce:scroll-auto" tabindex="0" role="group" aria-label="Reveal and scale sections, five panels">

    <section class="[--h:300] [view-timeline-name:--tfps08] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center px-[clamp(.6rem,2.5vw,1.6rem)] py-[clamp(.6rem,2vh,1.4rem)]" id="tfps-08-s1" aria-labelledby="tfps-08-h1">
      <div class="tfps08-reveal relative isolate flex min-h-[calc(100dvh-clamp(1.2rem,4vh,2.8rem))] w-full items-center justify-center overflow-hidden rounded-[1.75rem] border border-tfps08-ink/10 bg-tfps08-panel bg-[radial-gradient(110%_80%_at_88%_8%,oklch(92%_.07_calc(var(--h)*1deg)),transparent_62%)] px-[clamp(1.25rem,5vw,4rem)] py-[clamp(2rem,5vh,3.5rem)] shadow-[0_30px_70px_-40px_var(--color-tfps08-shade)] tfps08-dark:bg-[radial-gradient(110%_80%_at_88%_8%,oklch(28%_.08_calc(var(--h)*1deg)),transparent_62%)] forced-colors:border-[CanvasText]">
        <span aria-hidden="true" class="pointer-events-none absolute right-[3%] -bottom-[.14em] -z-10 font-tfps08-mono text-[clamp(8rem,26vw,22rem)] leading-none font-medium tracking-[-.08em] text-[oklch(55%_.12_calc(var(--h)*1deg)/.1)] tfps08-dark:text-[oklch(80%_.1_calc(var(--h)*1deg)/.08)]">01</span>
        <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] transition-[opacity,translate] duration-700 ease-out starting:translate-y-4 starting:opacity-0 motion-reduce:transition-none">
          <p class="flex flex-wrap items-center gap-3"><span class="font-tfps08-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps08-acc">01 / 05</span><span class="rounded-[.45rem] border border-tfps08-ink/12 px-2 py-[.22rem] font-tfps08-mono text-[.7rem] text-tfps08-ink/75">scale .92 &rarr; 1</span></p>
          <h2 class="max-w-[20ch] text-[clamp(2rem,5.6vw,4rem)] leading-[1.02] font-semibold tracking-[-.042em] text-balance" id="tfps-08-h1">Every panel arrives by growing into place</h2>
          <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps08-ink/75 [&_code]:text-tfps08-ink">One keyframe set drives both halves of the transition: the incoming sheet rises from 92% and 30% opacity, holds perfectly still while it is snapped, then recedes the same way as it leaves.</p>
          <a href="#tfps-08-s2" class="inline-flex min-h-11 items-center gap-2.5 rounded-full pe-3 font-tfps08-mono text-[.82rem] text-tfps08-ink/75 no-underline transition-colors hover:text-tfps08-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfps08-acc"><svg class="size-[1.1rem] animate-tfps08-bob motion-reduce:animate-none" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Scroll &mdash; the next sheet is already growing</a>
        </div>
      </div>
    </section>

    <section class="[--h:255] [view-timeline-name:--tfps08] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center px-[clamp(.6rem,2.5vw,1.6rem)] py-[clamp(.6rem,2vh,1.4rem)]" id="tfps-08-s2" aria-labelledby="tfps-08-h2">
      <div class="tfps08-reveal relative isolate flex min-h-[calc(100dvh-clamp(1.2rem,4vh,2.8rem))] w-full items-center justify-center overflow-hidden rounded-[1.75rem] border border-tfps08-ink/10 bg-tfps08-panel bg-[radial-gradient(110%_80%_at_88%_8%,oklch(92%_.07_calc(var(--h)*1deg)),transparent_62%)] px-[clamp(1.25rem,5vw,4rem)] py-[clamp(2rem,5vh,3.5rem)] shadow-[0_30px_70px_-40px_var(--color-tfps08-shade)] tfps08-dark:bg-[radial-gradient(110%_80%_at_88%_8%,oklch(28%_.08_calc(var(--h)*1deg)),transparent_62%)] forced-colors:border-[CanvasText]">
        <span aria-hidden="true" class="pointer-events-none absolute right-[3%] -bottom-[.14em] -z-10 font-tfps08-mono text-[clamp(8rem,26vw,22rem)] leading-none font-medium tracking-[-.08em] text-[oklch(55%_.12_calc(var(--h)*1deg)/.1)] tfps08-dark:text-[oklch(80%_.1_calc(var(--h)*1deg)/.08)]">02</span>
        <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
          <p class="flex flex-wrap items-center gap-3"><span class="font-tfps08-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps08-acc">02 / 05</span><span class="rounded-[.45rem] border border-tfps08-ink/12 px-2 py-[.22rem] font-tfps08-mono text-[.7rem] text-tfps08-ink/75">one range, two directions</span></p>
          <h2 class="max-w-[26ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-08-h2">The cover range already knows the whole journey</h2>
          <pre class="w-full overflow-x-auto overflow-y-hidden rounded-2xl border border-tfps08-ink/10 bg-tfps08-ink/[.04] px-[1.1rem] py-4"><code class="text-[clamp(.78rem,1vw,.88rem)] leading-[1.75] whitespace-pre text-tfps08-ink/75 [&_mark]:rounded-[.25rem] [&_mark]:bg-tfps08-acc/15 [&_mark]:px-[.2rem] [&_mark]:text-tfps08-acc">@keyframes tfps08-reveal {
  0%      { scale: .92; opacity: .3 }
  <mark>44%, 56% { scale: 1;   opacity: 1  }</mark>
  100%    { scale: .92; opacity: .3 }
}
&lt;div class="<mark>tfps08-reveal</mark>"&gt;  &lt;!-- cover 0% → cover 100% --&gt;</code></pre>
          <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps08-ink/75 [&_code]:text-tfps08-ink">No entry animation fighting an exit animation, and no JavaScript deciding which one owns the middle of the screen.</p>
        </div>
      </div>
    </section>

    <section class="[--h:210] [view-timeline-name:--tfps08] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center px-[clamp(.6rem,2.5vw,1.6rem)] py-[clamp(.6rem,2vh,1.4rem)]" id="tfps-08-s3" aria-labelledby="tfps-08-h3">
      <div class="tfps08-reveal relative isolate flex min-h-[calc(100dvh-clamp(1.2rem,4vh,2.8rem))] w-full items-center justify-center overflow-hidden rounded-[1.75rem] border border-tfps08-ink/10 bg-tfps08-panel bg-[radial-gradient(110%_80%_at_88%_8%,oklch(92%_.07_calc(var(--h)*1deg)),transparent_62%)] px-[clamp(1.25rem,5vw,4rem)] py-[clamp(2rem,5vh,3.5rem)] shadow-[0_30px_70px_-40px_var(--color-tfps08-shade)] tfps08-dark:bg-[radial-gradient(110%_80%_at_88%_8%,oklch(28%_.08_calc(var(--h)*1deg)),transparent_62%)] forced-colors:border-[CanvasText]">
        <span aria-hidden="true" class="pointer-events-none absolute right-[3%] -bottom-[.14em] -z-10 font-tfps08-mono text-[clamp(8rem,26vw,22rem)] leading-none font-medium tracking-[-.08em] text-[oklch(55%_.12_calc(var(--h)*1deg)/.1)] tfps08-dark:text-[oklch(80%_.1_calc(var(--h)*1deg)/.08)]">03</span>
        <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
          <p class="flex flex-wrap items-center gap-3"><span class="font-tfps08-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps08-acc">03 / 05</span><span class="rounded-[.45rem] border border-tfps08-ink/12 px-2 py-[.22rem] font-tfps08-mono text-[.7rem] text-tfps08-ink/75">the plateau</span></p>
          <h2 class="max-w-[26ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-08-h3">Twelve percent of dead zone in the middle</h2>
          <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps08-ink/75 [&_code]:text-tfps08-ink">Hold full scale from 44% to 56% of the range and a snapped panel is visually locked. Remove the hold and the sheet breathes on every tiny trackpad nudge &mdash; the single most common reason this effect feels cheap.</p>
          <ul class="grid w-full gap-1">
          <li class="grid grid-cols-[6.5rem_1fr] items-baseline gap-4 border-t border-tfps08-ink/10 py-3"><strong class="font-tfps08-mono text-[.82rem] font-medium text-tfps08-acc tabular-nums">0&ndash;44%</strong><span class="text-[.95rem] text-tfps08-ink/75">entering &mdash; scale and opacity rise</span></li>
          <li class="grid grid-cols-[6.5rem_1fr] items-baseline gap-4 border-t border-tfps08-ink/10 py-3"><strong class="font-tfps08-mono text-[.82rem] font-medium text-tfps08-acc tabular-nums">44&ndash;56%</strong><span class="text-[.95rem] text-tfps08-ink/75">snapped &mdash; nothing moves</span></li>
          <li class="grid grid-cols-[6.5rem_1fr] items-baseline gap-4 border-t border-tfps08-ink/10 py-3"><strong class="font-tfps08-mono text-[.82rem] font-medium text-tfps08-acc tabular-nums">56&ndash;100%</strong><span class="text-[.95rem] text-tfps08-ink/75">leaving &mdash; recedes symmetrically</span></li>
        </ul>
        </div>
      </div>
    </section>

    <section class="[--h:165] [view-timeline-name:--tfps08] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center px-[clamp(.6rem,2.5vw,1.6rem)] py-[clamp(.6rem,2vh,1.4rem)]" id="tfps-08-s4" aria-labelledby="tfps-08-h4">
      <div class="tfps08-reveal relative isolate flex min-h-[calc(100dvh-clamp(1.2rem,4vh,2.8rem))] w-full items-center justify-center overflow-hidden rounded-[1.75rem] border border-tfps08-ink/10 bg-tfps08-panel bg-[radial-gradient(110%_80%_at_88%_8%,oklch(92%_.07_calc(var(--h)*1deg)),transparent_62%)] px-[clamp(1.25rem,5vw,4rem)] py-[clamp(2rem,5vh,3.5rem)] shadow-[0_30px_70px_-40px_var(--color-tfps08-shade)] tfps08-dark:bg-[radial-gradient(110%_80%_at_88%_8%,oklch(28%_.08_calc(var(--h)*1deg)),transparent_62%)] forced-colors:border-[CanvasText]">
        <span aria-hidden="true" class="pointer-events-none absolute right-[3%] -bottom-[.14em] -z-10 font-tfps08-mono text-[clamp(8rem,26vw,22rem)] leading-none font-medium tracking-[-.08em] text-[oklch(55%_.12_calc(var(--h)*1deg)/.1)] tfps08-dark:text-[oklch(80%_.1_calc(var(--h)*1deg)/.08)]">04</span>
        <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
          <p class="flex flex-wrap items-center gap-3"><span class="font-tfps08-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps08-acc">04 / 05</span><span class="rounded-[.45rem] border border-tfps08-ink/12 px-2 py-[.22rem] font-tfps08-mono text-[.7rem] text-tfps08-ink/75">compositor only</span></p>
          <h2 class="max-w-[26ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-08-h4">Two cheap properties, zero expensive ones</h2>
          <div class="grid w-full grid-cols-[repeat(auto-fit,minmax(12rem,1fr))] gap-[clamp(.8rem,2vw,1.4rem)]">
            <div class="grid content-start gap-3 rounded-[1.15rem] border border-tfps08-ink/10 bg-tfps08-ink/[.03] p-[clamp(1rem,2.2vw,1.4rem)]"><p class="font-tfps08-mono text-[.68rem] tracking-[.12em] uppercase text-tfps08-yes">Free on the compositor</p><ul class="grid gap-2 font-tfps08-mono text-[.87rem] text-tfps08-ink/75"><li>scale</li><li>opacity</li><li>translate</li><li>rotate</li></ul></div>
            <div class="grid content-start gap-3 rounded-[1.15rem] border border-tfps08-ink/10 bg-tfps08-ink/[.03] p-[clamp(1rem,2.2vw,1.4rem)]"><p class="font-tfps08-mono text-[.68rem] tracking-[.12em] uppercase text-tfps08-no">Repaints every frame</p><ul class="grid gap-2 font-tfps08-mono text-[.87rem] text-tfps08-ink/75"><li>filter: blur()</li><li>width / height</li><li>top / left</li><li>box-shadow, border-radius</li></ul></div>
          </div>
        </div>
      </div>
    </section>

    <section class="[--h:120] [view-timeline-name:--tfps08] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center px-[clamp(.6rem,2.5vw,1.6rem)] py-[clamp(.6rem,2vh,1.4rem)]" id="tfps-08-s5" aria-labelledby="tfps-08-h5">
      <div class="tfps08-reveal relative isolate flex min-h-[calc(100dvh-clamp(1.2rem,4vh,2.8rem))] w-full items-center justify-center overflow-hidden rounded-[1.75rem] border border-tfps08-ink/10 bg-tfps08-panel bg-[radial-gradient(110%_80%_at_88%_8%,oklch(92%_.07_calc(var(--h)*1deg)),transparent_62%)] px-[clamp(1.25rem,5vw,4rem)] py-[clamp(2rem,5vh,3.5rem)] shadow-[0_30px_70px_-40px_var(--color-tfps08-shade)] tfps08-dark:bg-[radial-gradient(110%_80%_at_88%_8%,oklch(28%_.08_calc(var(--h)*1deg)),transparent_62%)] forced-colors:border-[CanvasText]">
        <span aria-hidden="true" class="pointer-events-none absolute right-[3%] -bottom-[.14em] -z-10 font-tfps08-mono text-[clamp(8rem,26vw,22rem)] leading-none font-medium tracking-[-.08em] text-[oklch(55%_.12_calc(var(--h)*1deg)/.1)] tfps08-dark:text-[oklch(80%_.1_calc(var(--h)*1deg)/.08)]">05</span>
        <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
          <p class="flex flex-wrap items-center gap-3"><span class="font-tfps08-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps08-acc">05 / 05</span><span class="rounded-[.45rem] border border-tfps08-ink/12 px-2 py-[.22rem] font-tfps08-mono text-[.7rem] text-tfps08-ink/75">pick your floor</span></p>
          <h2 class="max-w-[26ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-08-h5">Why 0.92 and not 0.8</h2>
          <p class="max-w-[58ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps08-ink/75 [&_code]:text-tfps08-ink">At <code>.92</code> the displacement reads as depth while body copy stays legible the whole way in. Below roughly <code>.85</code> headlines visibly reflow, the effect starts to feel like a slideshow, and motion-sensitive readers notice immediately.</p>
          <figure class="grid max-w-[46ch] gap-2.5 border-s-2 border-tfps08-acc ps-[1.1rem]">
          <blockquote class="text-[clamp(1.05rem,1.9vw,1.35rem)] leading-[1.45] tracking-[-.02em] text-pretty"><p>&ldquo;We shipped the reveal at .92 with a held middle. Nobody described it as an animation &mdash; they described the page as feeling fast.&rdquo;</p></blockquote>
          <figcaption class="font-tfps08-mono text-[.68rem] tracking-[.1em] uppercase text-tfps08-ink/70">Sam Rivera &middot; product designer</figcaption>
        </figure>
        </div>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfps08-bg: #eceef2;
  --color-tfps08-bg: oklch(93.5% .006 300);
  --color-tfps08-panel: #ffffff;
  --color-tfps08-panel: oklch(1 0 0);
  --color-tfps08-ink: #0b0b12;
  --color-tfps08-ink: oklch(12% .015 300);
  --color-tfps08-acc: #a21caf;
  --color-tfps08-acc: oklch(52% .21 328);
  --color-tfps08-yes: #0f766e;
  --color-tfps08-yes: oklch(48% .1 175);
  --color-tfps08-no: #9f1239;
  --color-tfps08-no: oklch(48% .16 12);
  --color-tfps08-shade: rgb(11 11 18 / .45);
  --font-tfps08-sans: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tfps08-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace;
  --animate-tfps08-bob: tfps08-bob 2.4s ease-in-out infinite;

  @keyframes tfps08-bob {
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

@custom-variant tfps08-dark {
  @media (prefers-color-scheme: light) {
    &:where(.tfps-08:has(#tfps-08-theme:checked), .tfps-08:has(#tfps-08-theme:checked) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: dark) {
    &:where(.tfps-08:not(:has(#tfps-08-theme:checked)), .tfps-08:not(:has(#tfps-08-theme:checked)) *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, stated before the browser build compiles. */

.tfps-08 {
  width: 100%;
  min-height: 100svh;

  @variant tfps08-dark {
    --color-tfps08-bg: #070709;
    --color-tfps08-bg: oklch(0.13 0.005 285.7);
    --color-tfps08-panel: #0d0d13;
    --color-tfps08-panel: oklch(0.162 0.013 284.9);
    --color-tfps08-ink: #f3f2f8;
    --color-tfps08-ink: oklch(0.964 0.008 293.9);
    --color-tfps08-acc: #f0abfc;
    --color-tfps08-acc: oklch(0.833 0.132 321.4);
    --color-tfps08-yes: #5eead4;
    --color-tfps08-yes: oklch(0.855 0.125 181.1);
    --color-tfps08-no: #fda4af;
    --color-tfps08-no: oklch(0.81 0.106 11.6);
    --color-tfps08-shade: rgb(0 0 0 / .9);
  }
}
/* What stayed CSS: the reveal. One @utility keeps shorthand, timeline and range in order. */

@keyframes tfps08-reveal {
  0% {
    scale: .92;
    opacity: .3;
  }

  44%,
    56% {
    scale: 1;
    opacity: 1;
  }

  100% {
    scale: .92;
    opacity: .3;
  }
}

@utility tfps08-reveal {
  @supports (animation-timeline: view()) {
    @media (prefers-reduced-motion: no-preference) {
      animation: tfps08-reveal linear both;
      animation-timeline: --tfps08;
      animation-range: cover 0% cover 100%;
    }
  }
}
```
