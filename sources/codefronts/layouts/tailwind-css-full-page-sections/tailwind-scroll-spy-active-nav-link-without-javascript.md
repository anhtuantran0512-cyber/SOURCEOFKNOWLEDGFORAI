---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-scroll-spy-active-nav-link-without-javascript/"
title: "Tailwind Scroll Spy Active Nav Link Without JavaScript"
section: "layouts"
category: "tailwind-css-full-page-sections"
category_name: "Tailwind CSS Full Page Sections"
description: "A docs-style floating nav whose active link lights up as each full-viewport section passes &mdash; the before: lozenge fills and the label turns accent,…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scroll Spy Active Nav Link Without JavaScript
Source: https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-scroll-spy-active-nav-link-without-javascript/

A docs-style floating nav whose active link lights up as each full-viewport section passes &mdash; the before: lozenge fills and the label turns accent, driven entirely by view timelines through two tiny @utility blocks. A short IntersectionObserver exists only to keep aria-current truthful (read by aria-[current=true]: utilities as the visual fallback) and to keep the active link scrolled into view when the nav overflows on phones.
## HTML
```html
<div class="tfps-06 relative isolate w-full min-h-svh bg-tfps06-bg font-tfps06-sans text-tfps06-ink antialiased [&_code]:font-tfps06-mono [&_code]:text-[.92em] [timeline-scope:--tfps06-1,--tfps06-2,--tfps06-3,--tfps06-4,--tfps06-5]">
  <input class="peer sr-only" type="checkbox" id="tfps-06-theme">
  <label for="tfps-06-theme" class="fixed top-[1.15rem] right-[1.15rem] z-80 grid size-11 cursor-pointer place-items-center rounded-full border border-tfps06-ink/10 bg-white/60 text-tfps06-ink hover:bg-white/85 tfps06-dark:bg-white/[.07] tfps06-dark:hover:bg-white/15 shadow-[0_8px_24px_-12px_var(--color-tfps06-shade)] backdrop-blur-[10px] backdrop-saturate-150 transition-[background-color,scale] duration-200 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tfps06-acc forced-colors:border-[CanvasText]">
    <svg class="size-[1.05rem] tfps06-dark:hidden" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/></svg>
    <svg class="hidden size-[1.05rem] tfps06-dark:block" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="sr-only">Switch light or dark theme</span>
  </label>

  <nav aria-label="On this page" data-tfps06-nav class="fixed top-[1.15rem] left-1/2 z-70 flex max-w-[calc(100%-8rem)] -translate-x-1/2 items-center gap-0.5 overflow-x-auto rounded-full border border-tfps06-ink/10 bg-white/70 p-1 shadow-[0_14px_34px_-22px_var(--color-tfps06-shade)] backdrop-blur-[14px] backdrop-saturate-150 [scrollbar-width:none] [&::-webkit-scrollbar]:hidden tfps06-dark:bg-white/[.07] forced-colors:border-[CanvasText]">
    <a href="#tfps-06-s1" aria-current="true" class="[--tl:--tfps06-1] tfps06-ink before:tfps06-on relative isolate inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-[.87rem] whitespace-nowrap text-tfps06-ink/75 no-underline transition-colors duration-200 before:absolute before:inset-0 before:-z-10 before:scale-[.86] before:rounded-[inherit] before:border before:border-tfps06-acc/25 before:bg-tfps06-acc/12 before:opacity-0 before:transition-[opacity,scale] before:duration-200 before:content-[''] hover:text-tfps06-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps06-acc aria-[current=true]:text-tfps06-acc aria-[current=true]:before:scale-100 aria-[current=true]:before:opacity-100">Overview</a>
    <a href="#tfps-06-s2" class="[--tl:--tfps06-2] tfps06-ink before:tfps06-on relative isolate inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-[.87rem] whitespace-nowrap text-tfps06-ink/75 no-underline transition-colors duration-200 before:absolute before:inset-0 before:-z-10 before:scale-[.86] before:rounded-[inherit] before:border before:border-tfps06-acc/25 before:bg-tfps06-acc/12 before:opacity-0 before:transition-[opacity,scale] before:duration-200 before:content-[''] hover:text-tfps06-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps06-acc aria-[current=true]:text-tfps06-acc aria-[current=true]:before:scale-100 aria-[current=true]:before:opacity-100">Install</a>
    <a href="#tfps-06-s3" class="[--tl:--tfps06-3] tfps06-ink before:tfps06-on relative isolate inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-[.87rem] whitespace-nowrap text-tfps06-ink/75 no-underline transition-colors duration-200 before:absolute before:inset-0 before:-z-10 before:scale-[.86] before:rounded-[inherit] before:border before:border-tfps06-acc/25 before:bg-tfps06-acc/12 before:opacity-0 before:transition-[opacity,scale] before:duration-200 before:content-[''] hover:text-tfps06-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps06-acc aria-[current=true]:text-tfps06-acc aria-[current=true]:before:scale-100 aria-[current=true]:before:opacity-100">Tokens</a>
    <a href="#tfps-06-s4" class="[--tl:--tfps06-4] tfps06-ink before:tfps06-on relative isolate inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-[.87rem] whitespace-nowrap text-tfps06-ink/75 no-underline transition-colors duration-200 before:absolute before:inset-0 before:-z-10 before:scale-[.86] before:rounded-[inherit] before:border before:border-tfps06-acc/25 before:bg-tfps06-acc/12 before:opacity-0 before:transition-[opacity,scale] before:duration-200 before:content-[''] hover:text-tfps06-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps06-acc aria-[current=true]:text-tfps06-acc aria-[current=true]:before:scale-100 aria-[current=true]:before:opacity-100">Theming</a>
    <a href="#tfps-06-s5" class="[--tl:--tfps06-5] tfps06-ink before:tfps06-on relative isolate inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-[.87rem] whitespace-nowrap text-tfps06-ink/75 no-underline transition-colors duration-200 before:absolute before:inset-0 before:-z-10 before:scale-[.86] before:rounded-[inherit] before:border before:border-tfps06-acc/25 before:bg-tfps06-acc/12 before:opacity-0 before:transition-[opacity,scale] before:duration-200 before:content-[''] hover:text-tfps06-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps06-acc aria-[current=true]:text-tfps06-acc aria-[current=true]:before:scale-100 aria-[current=true]:before:opacity-100">Changelog</a>
  </nav>

  <div data-tfps06-scroller class="h-dvh overflow-x-hidden overflow-y-auto snap-y snap-mandatory scroll-smooth overscroll-y-contain [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps06-acc [@media(max-height:40rem)]:snap-proximity motion-reduce:snap-none motion-reduce:scroll-auto" tabindex="0" role="group" aria-label="Documentation sections, five panels">

    <section class="[view-timeline-name:--tfps06-1] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center bg-tfps06-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(4.75rem,10vh,6rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps06-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps06-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps06-shade)] forced-colors:border-[CanvasText]" id="tfps-06-s1" aria-labelledby="tfps-06-h1">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] transition-[opacity,translate] duration-700 ease-out starting:translate-y-4 starting:opacity-0 motion-reduce:transition-none">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps06-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps06-acc">01 / 05</span><span class="rounded-[.45rem] border border-tfps06-ink/12 px-2 py-[.22rem] font-tfps06-mono text-[.7rem] text-tfps06-ink/75">scroll spy</span></p>
        <h2 class="max-w-[21ch] text-[clamp(1.95rem,5.2vw,3.7rem)] leading-[1.02] font-semibold tracking-[-.042em] text-balance" id="tfps-06-h1">The nav link knows which section you are reading</h2>
        <p class="max-w-[60ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps06-ink/75 [&_code]:text-tfps06-ink">Five full-viewport sections, one fixed nav. Each section publishes a view timeline; each link consumes one. The active lozenge is computed by the compositor from geometry the browser already has &mdash; no scroll handler, no offset maths, no drift on a fast flick.</p>
        <a href="#tfps-06-s2" class="inline-flex min-h-11 items-center gap-2.5 rounded-full pe-3 font-tfps06-mono text-[.82rem] text-tfps06-ink/75 no-underline transition-colors hover:text-tfps06-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfps06-acc"><svg class="size-[1.1rem] animate-tfps06-bob motion-reduce:animate-none" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Scroll and watch the nav above</a>
      </div>
    </section>

    <section class="[view-timeline-name:--tfps06-2] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center bg-tfps06-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(4.75rem,10vh,6rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps06-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps06-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps06-shade)] forced-colors:border-[CanvasText]" id="tfps-06-s2" aria-labelledby="tfps-06-h2">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps06-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps06-acc">02 / 05</span><span class="rounded-[.45rem] border border-tfps06-ink/12 px-2 py-[.22rem] font-tfps06-mono text-[.7rem] text-tfps06-ink/75">install</span></p>
        <h2 class="max-w-[27ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-06-h2">Three arbitrary properties and a utility</h2>
        <pre class="w-full overflow-x-auto overflow-y-hidden rounded-2xl border border-tfps06-ink/10 bg-tfps06-ink/[.04] px-[1.1rem] py-4"><code class="text-[clamp(.78rem,1vw,.88rem)] leading-[1.75] whitespace-pre text-tfps06-ink/75 [&_mark]:rounded-[.25rem] [&_mark]:bg-tfps06-acc/15 [&_mark]:px-[.2rem] [&_mark]:text-tfps06-acc">&lt;div class="<mark>[timeline-scope:--tfps06-1,…,--tfps06-5]</mark>"&gt;
&lt;section class="<mark>[view-timeline-name:--tfps06-2]</mark>"&gt;
&lt;a class="[--tl:--tfps06-2] tfps06-ink <mark>before:tfps06-on</mark>
          aria-[current=true]:before:opacity-100"&gt;</code></pre>
        <p class="max-w-[60ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps06-ink/75 [&_code]:text-tfps06-ink">The scope class is the one people miss: a timeline name is visible only to descendants, and a fixed nav is not a descendant of the section it tracks.</p>
      </div>
    </section>

    <section class="[view-timeline-name:--tfps06-3] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center bg-tfps06-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(4.75rem,10vh,6rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps06-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps06-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps06-shade)] forced-colors:border-[CanvasText]" id="tfps-06-s3" aria-labelledby="tfps-06-h3">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps06-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps06-acc">03 / 05</span><span class="rounded-[.45rem] border border-tfps06-ink/12 px-2 py-[.22rem] font-tfps06-mono text-[.7rem] text-tfps06-ink/75">tokens</span></p>
        <h2 class="max-w-[27ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-06-h3">Only two properties animate</h2>
        <ul class="grid w-full gap-1">
          <li class="grid grid-cols-[6rem_1fr] items-baseline gap-4 border-t border-tfps06-ink/10 py-3"><strong class="font-tfps06-mono text-[.82rem] font-medium text-tfps06-acc tabular-nums">opacity</strong><span class="text-[.95rem] text-tfps06-ink/75">0 &rarr; 1 on the <code>before:</code> lozenge behind the label</span></li>
          <li class="grid grid-cols-[6rem_1fr] items-baseline gap-4 border-t border-tfps06-ink/10 py-3"><strong class="font-tfps06-mono text-[.82rem] font-medium text-tfps06-acc tabular-nums">scale</strong><span class="text-[.95rem] text-tfps06-ink/75">.86 &rarr; 1, so the fill feels like it lands</span></li>
          <li class="grid grid-cols-[6rem_1fr] items-baseline gap-4 border-t border-tfps06-ink/10 py-3"><strong class="font-tfps06-mono text-[.82rem] font-medium text-tfps06-acc tabular-nums">color</strong><span class="text-[.95rem] text-tfps06-ink/75">the label&rsquo;s ink swap &mdash; cheap, no layout</span></li>
        </ul>
        <p class="max-w-[60ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps06-ink/75 [&_code]:text-tfps06-ink">No width, no <code>left</code>, no box-shadow on the hot path, so the nav stays smooth while the main thread is busy hydrating the page.</p>
      </div>
    </section>

    <section class="[view-timeline-name:--tfps06-4] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center bg-tfps06-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(4.75rem,10vh,6rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps06-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps06-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps06-shade)] forced-colors:border-[CanvasText]" id="tfps-06-s4" aria-labelledby="tfps-06-h4">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps06-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps06-acc">04 / 05</span><span class="rounded-[.45rem] border border-tfps06-ink/12 px-2 py-[.22rem] font-tfps06-mono text-[.7rem] text-tfps06-ink/75">theming</span></p>
        <h2 class="max-w-[27ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-06-h4">What the few lines of JavaScript are for</h2>
        <p class="max-w-[60ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps06-ink/75 [&_code]:text-tfps06-ink">Exactly one thing CSS cannot do: write to the accessibility tree. The observer keeps <code>aria-current</code> truthful for screen-reader users &mdash; and where scroll-driven CSS is missing, <code>aria-[current=true]:</code> utilities make it the visual driver too.</p>
        <figure class="grid max-w-[46ch] gap-2.5 border-s-2 border-tfps06-acc ps-[1.1rem]">
          <blockquote class="text-[clamp(1.05rem,1.9vw,1.35rem)] leading-[1.45] tracking-[-.02em] text-pretty"><p>&ldquo;Two sources of truth for one piece of state is how scroll spies get flickery. Let CSS own the pixels and the observer own the semantics.&rdquo;</p></blockquote>
          <figcaption class="font-tfps06-mono text-[.68rem] tracking-[.1em] uppercase text-tfps06-ink/70">Maya Okonkwo &middot; accessibility engineer</figcaption>
        </figure>
      </div>
    </section>

    <section class="[view-timeline-name:--tfps06-5] [view-timeline-axis:block] relative flex min-h-dvh snap-start items-center justify-center bg-tfps06-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(4.75rem,10vh,6rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps06-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps06-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps06-shade)] forced-colors:border-[CanvasText]" id="tfps-06-s5" aria-labelledby="tfps-06-h5">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps06-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps06-acc">05 / 05</span><span class="rounded-[.45rem] border border-tfps06-ink/12 px-2 py-[.22rem] font-tfps06-mono text-[.7rem] text-tfps06-ink/75">changelog</span></p>
        <h2 class="max-w-[27ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-06-h5">Why not a scroll listener</h2>
        <p class="max-w-[60ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps06-ink/75 [&_code]:text-tfps06-ink">A <code>scroll</code> handler recomputing offsets fires up to sixty times a second on the main thread, reads layout, and still lags a hard flick. The view timeline is evaluated from geometry the compositor already holds, so the active link cannot fall behind.</p>
        <a class="inline-flex min-h-11 items-center gap-2 rounded-full border border-tfps06-acc/40 px-[1.15rem] py-3 text-[.9rem] text-tfps06-acc no-underline transition-colors hover:bg-tfps06-acc/10 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tfps06-acc" href="#tfps-06-s1"><svg class="size-4 -rotate-90" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12h13.5M12.6 6.5 18.2 12l-5.6 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Back to the top section</a>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfps06-bg: #f6f9f7;
  --color-tfps06-bg: oklch(97.5% .008 165);
  --color-tfps06-panel: #ffffff;
  --color-tfps06-panel: oklch(1 0 0);
  --color-tfps06-panel2: #eef4f0;
  --color-tfps06-panel2: oklch(95% .013 165);
  --color-tfps06-ink: #08120d;
  --color-tfps06-ink: oklch(13% .015 165);
  --color-tfps06-acc: #047857;
  --color-tfps06-acc: oklch(50% .12 165);
  --color-tfps06-shade: rgb(8 18 13 / .22);
  --font-tfps06-sans: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tfps06-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace;
  --animate-tfps06-bob: tfps06-bob 2.4s ease-in-out infinite;

  @keyframes tfps06-bob {
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

@custom-variant tfps06-dark {
  @media (prefers-color-scheme: light) {
    &:where(.tfps-06:has(#tfps-06-theme:checked), .tfps-06:has(#tfps-06-theme:checked) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: dark) {
    &:where(.tfps-06:not(:has(#tfps-06-theme:checked)), .tfps-06:not(:has(#tfps-06-theme:checked)) *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, stated before the browser build compiles. */

.tfps-06 {
  width: 100%;
  min-height: 100svh;

  @variant tfps06-dark {
    --color-tfps06-bg: #050b08;
    --color-tfps06-bg: oklch(0.141 0.013 165.1);
    --color-tfps06-panel: #08100c;
    --color-tfps06-panel: oklch(0.163 0.015 162.8);
    --color-tfps06-panel2: #0d1712;
    --color-tfps06-panel2: oklch(0.193 0.018 162.4);
    --color-tfps06-ink: #eff7f2;
    --color-tfps06-ink: oklch(0.969 0.011 158.8);
    --color-tfps06-acc: #6ee7b7;
    --color-tfps06-acc: oklch(0.845 0.13 165);
    --color-tfps06-shade: rgb(0 0 0 / .7);
  }
}
/* What stayed CSS: the two scrubbed effects. Shorthand + timeline + range must be declared in order,
   so each lives in one @utility, gated on support and on motion preference. */

@keyframes tfps06-on {
  0%,
    42% {
    opacity: 0;
    scale: .86;
  }

  48%,
    52% {
    opacity: 1;
    scale: 1;
  }

  58%,
    100% {
    opacity: 0;
    scale: .86;
  }
}

@keyframes tfps06-ink {
  0%,
    42% {
    color: color-mix(in oklab, var(--color-tfps06-ink) 75%, transparent);
  }

  48%,
    52% {
    color: var(--color-tfps06-acc);
  }

  58%,
    100% {
    color: color-mix(in oklab, var(--color-tfps06-ink) 75%, transparent);
  }
}

@utility tfps06-on {
  @supports (animation-timeline: view()) {
    @media (prefers-reduced-motion: no-preference) {
      animation: tfps06-on linear both;
      animation-timeline: var(--tl);
      animation-range: cover 0% cover 100%;
    }
  }
}

@utility tfps06-ink {
  @supports (animation-timeline: view()) {
    @media (prefers-reduced-motion: no-preference) {
      animation: tfps06-ink linear both;
      animation-timeline: var(--tl);
      animation-range: cover 0% cover 100%;
    }
  }
}
```

## JavaScript
```js
const tfps06 = document.querySelector('.tfps-06');
if (tfps06) {
  const scroller = tfps06.querySelector('[data-tfps06-scroller]');
  const nav = tfps06.querySelector('[data-tfps06-nav]');
  const links = [...nav.querySelectorAll('a')];
  const behavior = () => (matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth');
  const spy = new IntersectionObserver((entries) => {
    const seen = entries.find((e) => e.isIntersecting);
    if (!seen) return;
    for (const link of links) {
      if (link.hash !== '#' + seen.target.id) { link.removeAttribute('aria-current'); continue; }
      link.setAttribute('aria-current', 'true');
      // keep the active link visible when the nav overflows on phones
      nav.scrollTo({ left: link.offsetLeft - (nav.clientWidth - link.offsetWidth) / 2, behavior: behavior() });
    }
  }, { root: scroller, threshold: 0.6 });
  for (const panel of tfps06.querySelectorAll('section')) spy.observe(panel);
}
```
