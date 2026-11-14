---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-full-page-sections/accessible-tailwind-scroll-snap-with-keyboard-navigation/"
title: "Accessible Tailwind Scroll Snap with Keyboard Navigation"
section: "layouts"
category: "tailwind-css-full-page-sections"
category_name: "Tailwind CSS Full Page Sections"
description: "The panel that makes the pattern shippable: snap-proximity so nothing traps a keyboard user, arrow / Page&nbsp;Up / Page&nbsp;Down / Home / End navigation…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Tailwind Scroll Snap with Keyboard Navigation
Source: https://codefronts.com/layouts/tailwind-css-full-page-sections/accessible-tailwind-scroll-snap-with-keyboard-navigation/

The panel that makes the pattern shippable: snap-proximity so nothing traps a keyboard user, arrow / Page&nbsp;Up / Page&nbsp;Down / Home / End navigation that also moves focus, a skip link past the whole scroller, one labelled <section> per panel, a polite sr-only live region announcing position &mdash; mirrored in a visible pill for sighted keyboard users &mdash; and motion-reduce: turning snapping and smooth scrolling off entirely.
## HTML
```html
<div class="tfps-12 relative isolate w-full min-h-svh bg-tfps12-bg font-tfps12-sans text-tfps12-ink antialiased [&_code]:font-tfps12-mono [&_code]:text-[.92em]">
  <input class="peer sr-only" type="checkbox" id="tfps-12-theme">
  <label for="tfps-12-theme" class="fixed top-[1.15rem] right-[1.15rem] z-80 grid size-11 cursor-pointer place-items-center rounded-full border border-tfps12-ink/10 bg-white/60 text-tfps12-ink hover:bg-white/85 tfps12-dark:bg-white/[.07] tfps12-dark:hover:bg-white/15 shadow-[0_8px_24px_-12px_var(--color-tfps12-shade)] backdrop-blur-[10px] backdrop-saturate-150 transition-[background-color,scale] duration-200 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tfps12-acc forced-colors:border-[CanvasText]">
    <svg class="size-[1.05rem] tfps12-dark:hidden" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/></svg>
    <svg class="hidden size-[1.05rem] tfps12-dark:block" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="sr-only">Switch light or dark theme</span>
  </label>

  <a href="#tfps-12-end" class="fixed top-[1.15rem] left-[1.15rem] z-90 inline-flex min-h-11 -translate-y-[150%] items-center rounded-full border border-tfps12-acc/35 bg-tfps12-panel px-[1.1rem] py-3 text-[.87rem] text-tfps12-acc no-underline opacity-0 transition-[translate,opacity] duration-200 focus:translate-y-0 focus:opacity-100 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tfps12-acc motion-reduce:translate-y-0 motion-reduce:opacity-100">Skip the panel sequence</a>
  <p class="sr-only" role="status" aria-live="polite" data-tfps12-live></p>
  <p aria-hidden="true" data-tfps12-pos class="fixed bottom-4 left-1/2 z-70 -translate-x-1/2 rounded-full border border-tfps12-ink/10 bg-white/70 px-3.5 py-2 font-tfps12-mono text-[.72rem] whitespace-nowrap tabular-nums text-tfps12-ink/80 shadow-[0_14px_34px_-22px_var(--color-tfps12-shade)] backdrop-blur-md tfps12-dark:bg-white/[.07]">Panel 1 of 5 &middot; Proximity by default</p>

  <div data-tfps12-scroller class="h-dvh overflow-x-hidden overflow-y-auto snap-y snap-proximity scroll-smooth overscroll-y-contain [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps12-acc [@media(max-height:40rem)]:snap-proximity motion-reduce:snap-none motion-reduce:scroll-auto" tabindex="0" role="group" aria-label="Accessible panel sequence, five panels. Use arrow keys, Page Up and Page Down.">

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps12-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(4.5rem,10vh,6rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps12-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps12-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps12-shade)] forced-colors:border-[CanvasText] focus-visible:outline-2 focus-visible:-outline-offset-4 focus-visible:outline-tfps12-acc" tabindex="-1" data-label="Proximity by default" id="tfps-12-s1" aria-labelledby="tfps-12-h1">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] transition-[opacity,translate] duration-700 ease-out starting:translate-y-4 starting:opacity-0 motion-reduce:transition-none">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps12-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps12-acc">01 / 05</span><span class="rounded-[.45rem] border border-tfps12-ink/12 px-2 py-[.22rem] font-tfps12-mono text-[.7rem] text-tfps12-ink/75">snap-y snap-proximity</span></p>
        <h2 class="max-w-[20ch] text-[clamp(2rem,5.4vw,3.9rem)] leading-[1.02] font-semibold tracking-[-.042em] text-balance" id="tfps-12-h1">Snapping that never traps anyone</h2>
        <p class="max-w-[60ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps12-ink/75 [&_code]:text-tfps12-ink">Arrow keys, Page&nbsp;Up, Page&nbsp;Down, Home and End all move between panels and carry focus with them. The scrollport is focusable, so the keys work before a single line of script runs.</p>
        <ul class="grid w-full gap-1">
          <li class="flex flex-wrap items-center gap-2 border-t border-tfps12-ink/10 py-2.5"><kbd class="min-w-[2.1rem] rounded-[.45rem] border border-tfps12-ink/12 bg-tfps12-ink/[.04] px-[.45rem] py-[.28rem] text-center font-tfps12-mono text-[.75rem] shadow-[0_1px_0_color-mix(in_oklab,var(--color-tfps12-ink)_14%,transparent)]">&darr;</kbd><kbd class="min-w-[2.1rem] rounded-[.45rem] border border-tfps12-ink/12 bg-tfps12-ink/[.04] px-[.45rem] py-[.28rem] text-center font-tfps12-mono text-[.75rem] shadow-[0_1px_0_color-mix(in_oklab,var(--color-tfps12-ink)_14%,transparent)]">&uarr;</kbd><span class="ms-2 text-[.95rem] text-tfps12-ink/75">next / previous panel</span></li>
          <li class="flex flex-wrap items-center gap-2 border-t border-tfps12-ink/10 py-2.5"><kbd class="min-w-[2.1rem] rounded-[.45rem] border border-tfps12-ink/12 bg-tfps12-ink/[.04] px-[.45rem] py-[.28rem] text-center font-tfps12-mono text-[.75rem] shadow-[0_1px_0_color-mix(in_oklab,var(--color-tfps12-ink)_14%,transparent)]">PgDn</kbd><kbd class="min-w-[2.1rem] rounded-[.45rem] border border-tfps12-ink/12 bg-tfps12-ink/[.04] px-[.45rem] py-[.28rem] text-center font-tfps12-mono text-[.75rem] shadow-[0_1px_0_color-mix(in_oklab,var(--color-tfps12-ink)_14%,transparent)]">PgUp</kbd><span class="ms-2 text-[.95rem] text-tfps12-ink/75">same, one screen at a time</span></li>
          <li class="flex flex-wrap items-center gap-2 border-t border-tfps12-ink/10 py-2.5"><kbd class="min-w-[2.1rem] rounded-[.45rem] border border-tfps12-ink/12 bg-tfps12-ink/[.04] px-[.45rem] py-[.28rem] text-center font-tfps12-mono text-[.75rem] shadow-[0_1px_0_color-mix(in_oklab,var(--color-tfps12-ink)_14%,transparent)]">Home</kbd><kbd class="min-w-[2.1rem] rounded-[.45rem] border border-tfps12-ink/12 bg-tfps12-ink/[.04] px-[.45rem] py-[.28rem] text-center font-tfps12-mono text-[.75rem] shadow-[0_1px_0_color-mix(in_oklab,var(--color-tfps12-ink)_14%,transparent)]">End</kbd><span class="ms-2 text-[.95rem] text-tfps12-ink/75">first / last panel</span></li>
          <li class="flex flex-wrap items-center gap-2 border-t border-tfps12-ink/10 py-2.5"><kbd class="min-w-[2.1rem] rounded-[.45rem] border border-tfps12-ink/12 bg-tfps12-ink/[.04] px-[.45rem] py-[.28rem] text-center font-tfps12-mono text-[.75rem] shadow-[0_1px_0_color-mix(in_oklab,var(--color-tfps12-ink)_14%,transparent)]">Tab</kbd><span class="ms-2 text-[.95rem] text-tfps12-ink/75">next control &mdash; never trapped</span></li>
        </ul>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps12-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(4.5rem,10vh,6rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps12-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps12-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps12-shade)] forced-colors:border-[CanvasText] focus-visible:outline-2 focus-visible:-outline-offset-4 focus-visible:outline-tfps12-acc" tabindex="-1" data-label="Why mandatory can trap" id="tfps-12-s2" aria-labelledby="tfps-12-h2">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps12-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps12-acc">02 / 05</span><span class="rounded-[.45rem] border border-tfps12-ink/12 px-2 py-[.22rem] font-tfps12-mono text-[.7rem] text-tfps12-ink/75">the WCAG failure</span></p>
        <h2 class="max-w-[27ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-12-h2">How mandatory snapping hides focused content</h2>
        <p class="max-w-[60ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps12-ink/75 [&_code]:text-tfps12-ink">With <code>snap-mandatory</code>, the scrollport must always rest on a snap point. If a panel is taller than the screen &mdash; or a control sits below its fold &mdash; the browser can pull the scroll back to the panel edge, leaving the focused element off screen with no way to reach it.</p>
        <div class="grid w-full grid-cols-[repeat(auto-fit,minmax(14rem,1fr))] gap-[clamp(.8rem,2vw,1.4rem)]">
          <div class="grid content-start gap-2 rounded-[1.15rem] border border-tfps12-ink/10 bg-tfps12-ink/[.03] p-[clamp(1rem,2.2vw,1.35rem)] forced-colors:border-[CanvasText]"><p class="font-tfps12-mono text-[.7rem] tracking-[.1em] uppercase text-tfps12-no">snap-mandatory</p><p class="text-[.95rem] leading-[1.5] text-pretty text-tfps12-ink/75">Rests only on snap points. Content between them can become unreachable.</p></div>
          <div class="grid content-start gap-2 rounded-[1.15rem] border border-tfps12-ink/10 bg-tfps12-ink/[.03] p-[clamp(1rem,2.2vw,1.35rem)] forced-colors:border-[CanvasText]"><p class="font-tfps12-mono text-[.7rem] tracking-[.1em] uppercase text-tfps12-yes">snap-proximity</p><p class="text-[.95rem] leading-[1.5] text-pretty text-tfps12-ink/75">Snaps when the reader stops near an edge. Everything in between stays reachable.</p></div>
        </div>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps12-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(4.5rem,10vh,6rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps12-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps12-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps12-shade)] forced-colors:border-[CanvasText] focus-visible:outline-2 focus-visible:-outline-offset-4 focus-visible:outline-tfps12-acc" tabindex="-1" data-label="Focus follows the scroll" id="tfps-12-s3" aria-labelledby="tfps-12-h3">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps12-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps12-acc">03 / 05</span><span class="rounded-[.45rem] border border-tfps12-ink/12 px-2 py-[.22rem] font-tfps12-mono text-[.7rem] text-tfps12-ink/75">focus, preventScroll</span></p>
        <h2 class="max-w-[27ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-12-h3">Move the scroll and the focus together</h2>
        <pre class="w-full overflow-x-auto overflow-y-hidden rounded-2xl border border-tfps12-ink/10 bg-tfps12-ink/[.04] px-[1.1rem] py-4"><code class="text-[clamp(.78rem,1vw,.88rem)] leading-[1.75] whitespace-pre text-tfps12-ink/75 [&_mark]:rounded-[.25rem] [&_mark]:bg-tfps12-acc/15 [&_mark]:px-[.2rem] [&_mark]:text-tfps12-acc">scroller.scrollTo({ top: panels[n].offsetTop, behavior });
panels[n].focus({ <mark>preventScroll: true</mark> });</code></pre>
        <p class="max-w-[60ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps12-ink/75 [&_code]:text-tfps12-ink">Without <code>preventScroll</code> the browser performs its own scroll to the focused element, which fights the animated one and shows as a double jump. With it, focus lands silently and the next <kbd class="min-w-[2.1rem] rounded-[.45rem] border border-tfps12-ink/12 bg-tfps12-ink/[.04] px-[.45rem] py-[.28rem] text-center font-tfps12-mono text-[.75rem] shadow-[0_1px_0_color-mix(in_oklab,var(--color-tfps12-ink)_14%,transparent)]">Tab</kbd> continues from where the reader is actually looking.</p>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps12-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(4.5rem,10vh,6rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps12-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps12-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps12-shade)] forced-colors:border-[CanvasText] focus-visible:outline-2 focus-visible:-outline-offset-4 focus-visible:outline-tfps12-acc" tabindex="-1" data-label="Announcing position" id="tfps-12-s4" aria-labelledby="tfps-12-h4">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps12-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps12-acc">04 / 05</span><span class="rounded-[.45rem] border border-tfps12-ink/12 px-2 py-[.22rem] font-tfps12-mono text-[.7rem] text-tfps12-ink/75">aria-live: polite</span></p>
        <h2 class="max-w-[27ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-12-h4">Tell the reader where they are, quietly</h2>
        <p class="max-w-[60ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps12-ink/75 [&_code]:text-tfps12-ink">Each panel is a real <code>&lt;section&gt;</code> labelled by its own heading, so it is announced as a named region. Position (&ldquo;Panel 4 of 5&rdquo;) goes to a polite, <code>sr-only</code> live region after keyboard moves &mdash; and the same text shows in the pill below for sighted keyboard users.</p>
        <ul class="grid w-full gap-1">
          <li class="grid grid-cols-[7rem_1fr] items-baseline gap-4 border-t border-tfps12-ink/10 py-3"><strong class="font-tfps12-mono text-[.82rem] font-medium text-tfps12-acc tabular-nums">polite</strong><span class="text-[.95rem] text-tfps12-ink/75">queued behind whatever is being read</span></li>
          <li class="grid grid-cols-[7rem_1fr] items-baseline gap-4 border-t border-tfps12-ink/10 py-3"><strong class="font-tfps12-mono text-[.82rem] font-medium text-tfps12-acc tabular-nums">assertive</strong><span class="text-[.95rem] text-tfps12-ink/75">interrupts &mdash; wrong for a scroll position</span></li>
          <li class="grid grid-cols-[7rem_1fr] items-baseline gap-4 border-t border-tfps12-ink/10 py-3"><strong class="font-tfps12-mono text-[.82rem] font-medium text-tfps12-acc tabular-nums">tabindex -1</strong><span class="text-[.95rem] text-tfps12-ink/75">programmatic target, not a tab stop</span></li>
        </ul>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps12-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(4.5rem,10vh,6rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps12-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps12-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps12-shade)] forced-colors:border-[CanvasText] focus-visible:outline-2 focus-visible:-outline-offset-4 focus-visible:outline-tfps12-acc" tabindex="-1" data-label="Reduced motion" id="tfps-12-s5" aria-labelledby="tfps-12-h5">
      <div class="grid w-full max-w-[58rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps12-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps12-acc">05 / 05</span><span class="rounded-[.45rem] border border-tfps12-ink/12 px-2 py-[.22rem] font-tfps12-mono text-[.7rem] text-tfps12-ink/75">motion-reduce</span></p>
        <h2 class="max-w-[27ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-12-h5">Reduced motion switches the whole pattern off</h2>
        <p class="max-w-[60ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps12-ink/75 [&_code]:text-tfps12-ink"><code>motion-reduce:snap-none</code>, <code>motion-reduce:scroll-auto</code>, <code>motion-reduce:transition-none</code> &mdash; and programmatic scrolls switch to <code>auto</code>, because the script reads the same media query. What is left is an ordinary document with tall sections.</p>
        <p id="tfps-12-end" tabindex="-1" class="rounded-[.6rem] border border-dashed border-tfps12-acc/40 px-3 py-2 font-tfps12-mono text-[.8rem] text-tfps12-acc focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tfps12-acc">End of the sequence &mdash; the skip link lands here.</p>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfps12-bg: #f5faf6;
  --color-tfps12-bg: oklch(97.6% .01 150);
  --color-tfps12-panel: #ffffff;
  --color-tfps12-panel: oklch(1 0 0);
  --color-tfps12-panel2: #edf5ef;
  --color-tfps12-panel2: oklch(95% .015 150);
  --color-tfps12-ink: #071109;
  --color-tfps12-ink: oklch(12% .02 150);
  --color-tfps12-acc: #166534;
  --color-tfps12-acc: oklch(45% .13 150);
  --color-tfps12-yes: #166534;
  --color-tfps12-yes: oklch(45% .13 150);
  --color-tfps12-no: #9f1239;
  --color-tfps12-no: oklch(48% .16 12);
  --color-tfps12-shade: rgb(7 17 9 / .2);
  --font-tfps12-sans: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tfps12-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace;
}
/* Theme state. Dark = OS preference XOR the toggle, so the switch always flips what you see —
   the CSS original's checkbox did nothing for visitors whose OS was already dark. */

@custom-variant tfps12-dark {
  @media (prefers-color-scheme: light) {
    &:where(.tfps-12:has(#tfps-12-theme:checked), .tfps-12:has(#tfps-12-theme:checked) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: dark) {
    &:where(.tfps-12:not(:has(#tfps-12-theme:checked)), .tfps-12:not(:has(#tfps-12-theme:checked)) *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, stated before the browser build compiles. */

.tfps-12 {
  width: 100%;
  min-height: 100svh;

  @variant tfps12-dark {
    --color-tfps12-bg: #050a06;
    --color-tfps12-bg: oklch(0.136 0.014 151.5);
    --color-tfps12-panel: #080f0a;
    --color-tfps12-panel: oklch(0.159 0.015 153.8);
    --color-tfps12-panel2: #0d1710;
    --color-tfps12-panel2: oklch(0.192 0.02 153.6);
    --color-tfps12-ink: #eff7f1;
    --color-tfps12-ink: oklch(0.968 0.012 153.7);
    --color-tfps12-acc: #86efac;
    --color-tfps12-acc: oklch(0.871 0.136 154.4);
    --color-tfps12-yes: #86efac;
    --color-tfps12-yes: oklch(0.871 0.136 154.4);
    --color-tfps12-no: #fda4af;
    --color-tfps12-no: oklch(0.81 0.106 11.6);
    --color-tfps12-shade: rgb(0 0 0 / .7);
  }
}
```

## JavaScript
```js
const tfps12 = document.querySelector('.tfps-12');
if (tfps12) {
  const scroller = tfps12.querySelector('[data-tfps12-scroller]');
  const live = tfps12.querySelector('[data-tfps12-live]');
  const pos = tfps12.querySelector('[data-tfps12-pos]');
  const panels = [...scroller.querySelectorAll('section')];
  const steps = { ArrowDown: 1, PageDown: 1, ArrowUp: -1, PageUp: -1 };
  const label = (n) => 'Panel ' + (n + 1) + ' of ' + panels.length + ' \u00b7 ' + panels[n].dataset.label;
  let at = 0; // tracks the visible panel, so keys work after mouse or touch scrolling too
  const seen = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { at = panels.indexOf(e.target); pos.textContent = label(at); }
  }, { root: scroller, threshold: 0.55 });
  panels.forEach((p) => seen.observe(p));
  const go = (i) => {
    at = Math.min(panels.length - 1, Math.max(0, i));
    const soft = matchMedia('(prefers-reduced-motion: reduce)').matches;
    scroller.scrollTo({ top: panels[at].offsetTop, behavior: soft ? 'auto' : 'smooth' });
    panels[at].focus({ preventScroll: true });
    live.textContent = label(at);
    pos.textContent = label(at);
  };
  scroller.addEventListener('keydown', (event) => {
    if (event.target.closest('input, textarea, select, [contenteditable]')) return;
    if (event.key in steps) { event.preventDefault(); go(at + steps[event.key]); }
    else if (event.key === 'Home') { event.preventDefault(); go(0); }
    else if (event.key === 'End') { event.preventDefault(); go(panels.length - 1); }
  });
}
```
