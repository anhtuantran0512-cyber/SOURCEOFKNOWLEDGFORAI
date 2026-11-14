---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-scroll-snap-stop-to-prevent-skipping-sections/"
title: "Tailwind Scroll Snap Stop to Prevent Skipping Sections"
section: "layouts"
category: "tailwind-css-full-page-sections"
category_name: "Tailwind CSS Full Page Sections"
description: "Two live scrollers side by side, identical except for one utility."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scroll Snap Stop to Prevent Skipping Sections
Source: https://codefronts.com/layouts/tailwind-css-full-page-sections/tailwind-scroll-snap-stop-to-prevent-skipping-sections/

Two live scrollers side by side, identical except for one utility. Flick the left one hard and it flies past two panels; flick the right one and snap-always catches it at the very next panel. Per-panel hues come from a single [--h:150] index feeding oklch() arbitrary values, a fade mask hints there's more below, and a table says when the utility helps and when it hurts.
## HTML
```html
<div class="tfps-03 relative isolate w-full min-h-svh bg-tfps03-bg font-tfps03-sans text-tfps03-ink antialiased [&_code]:font-tfps03-mono [&_code]:text-[.92em] [--hs:clamp(11rem,30vh,17rem)] [@media(max-height:40rem)]:[--hs:clamp(7.5rem,24vh,17rem)]">
  <input class="peer sr-only" type="checkbox" id="tfps-03-theme">
  <label for="tfps-03-theme" class="fixed top-[1.15rem] right-[1.15rem] z-80 grid size-11 cursor-pointer place-items-center rounded-full border border-tfps03-ink/10 bg-white/60 text-tfps03-ink hover:bg-white/85 tfps03-dark:bg-white/[.07] tfps03-dark:hover:bg-white/15 shadow-[0_8px_24px_-12px_var(--color-tfps03-shade)] backdrop-blur-[10px] backdrop-saturate-150 transition-[background-color,scale] duration-200 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tfps03-acc forced-colors:border-[CanvasText]">
    <svg class="size-[1.05rem] tfps03-dark:hidden" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/></svg>
    <svg class="hidden size-[1.05rem] tfps03-dark:block" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="sr-only">Switch light or dark theme</span>
  </label>

  <div class="h-dvh overflow-x-hidden overflow-y-auto snap-y snap-mandatory scroll-smooth overscroll-y-contain [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfps03-acc [@media(max-height:40rem)]:snap-proximity motion-reduce:snap-none motion-reduce:scroll-auto" tabindex="0" role="group" aria-label="Scroll snap stop demonstration, three panels">

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps03-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps03-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps03-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps03-shade)] forced-colors:border-[CanvasText]" id="tfps-03-s1" aria-labelledby="tfps-03-h1">
      <div class="grid w-full max-w-[68rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)] transition-[opacity,translate] duration-700 ease-out starting:translate-y-4 starting:opacity-0 motion-reduce:transition-none">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps03-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps03-acc">01 / 03</span><span class="rounded-[.45rem] border border-tfps03-ink/12 px-2 py-[.22rem] font-tfps03-mono text-[.7rem] text-tfps03-ink/75">snap-always</span></p>
        <h2 class="max-w-[22ch] text-[clamp(1.95rem,5.2vw,3.6rem)] leading-[1.02] font-semibold tracking-[-.042em] text-balance" id="tfps-03-h1">Stop the flick that skips your best section</h2>
        <p class="max-w-[60ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps03-ink/75 [&_code]:text-tfps03-ink">Default snapping only decides where momentum <em>ends</em>. One hard swipe can fly past two panels &mdash; and past whatever argument they carried. <code>snap-always</code> (<code>scroll-snap-stop: always</code>) makes each gesture advance exactly one panel.</p>
        <div class="grid w-full grid-cols-[repeat(auto-fit,minmax(14rem,1fr))] gap-[clamp(.9rem,2.5vw,1.75rem)]">
          <figure class="grid gap-2.5">
            <figcaption class="flex items-center gap-2 text-[.87rem] text-tfps03-ink/75"><span class="rounded-[.4rem] border px-[.45rem] py-[.2rem] font-tfps03-mono text-[.66rem] tracking-[.08em] text-tfps03-no">snap-normal</span>Flick hard &mdash; it skips</figcaption>
            <div tabindex="0" role="group" aria-label="Scroller without snap stop, five panels" class="h-(--hs) overflow-y-auto snap-y snap-mandatory scroll-smooth overscroll-contain rounded-[1.1rem] border border-tfps03-ink/10 bg-tfps03-ink/[.04] [mask-image:linear-gradient(to_bottom,#000_80%,transparent)] [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfps03-acc motion-reduce:snap-none motion-reduce:scroll-auto forced-colors:border-[CanvasText]">
              <div class="[--h:14] grid h-[calc(var(--hs)-1.8rem)] snap-start content-center gap-0.5 border-b border-tfps03-ink/10 bg-[oklch(95%_.045_calc(var(--h)*1deg))] px-[clamp(.9rem,2vw,1.4rem)] tfps03-dark:bg-[oklch(23%_.045_calc(var(--h)*1deg))]"><span class="font-tfps03-mono text-[clamp(1.6rem,4vw,2.4rem)] tracking-[-.03em] tabular-nums text-[oklch(48%_.16_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">01</span><p class="text-[.87rem] tracking-[.02em] text-[oklch(40%_.06_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(82%_.04_calc(var(--h)*1deg))]">Problem</p></div>
              <div class="[--h:34] grid h-[calc(var(--hs)-1.8rem)] snap-start content-center gap-0.5 border-b border-tfps03-ink/10 bg-[oklch(95%_.045_calc(var(--h)*1deg))] px-[clamp(.9rem,2vw,1.4rem)] tfps03-dark:bg-[oklch(23%_.045_calc(var(--h)*1deg))]"><span class="font-tfps03-mono text-[clamp(1.6rem,4vw,2.4rem)] tracking-[-.03em] tabular-nums text-[oklch(48%_.16_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">02</span><p class="text-[.87rem] tracking-[.02em] text-[oklch(40%_.06_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(82%_.04_calc(var(--h)*1deg))]">Approach</p></div>
              <div class="[--h:150] grid h-[calc(var(--hs)-1.8rem)] snap-start content-center gap-0.5 border-b border-tfps03-ink/10 bg-[oklch(95%_.045_calc(var(--h)*1deg))] px-[clamp(.9rem,2vw,1.4rem)] tfps03-dark:bg-[oklch(23%_.045_calc(var(--h)*1deg))]"><span class="font-tfps03-mono text-[clamp(1.6rem,4vw,2.4rem)] tracking-[-.03em] tabular-nums text-[oklch(48%_.16_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">03</span><p class="text-[.87rem] tracking-[.02em] text-[oklch(40%_.06_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(82%_.04_calc(var(--h)*1deg))]">Proof</p></div>
              <div class="[--h:200] grid h-[calc(var(--hs)-1.8rem)] snap-start content-center gap-0.5 border-b border-tfps03-ink/10 bg-[oklch(95%_.045_calc(var(--h)*1deg))] px-[clamp(.9rem,2vw,1.4rem)] tfps03-dark:bg-[oklch(23%_.045_calc(var(--h)*1deg))]"><span class="font-tfps03-mono text-[clamp(1.6rem,4vw,2.4rem)] tracking-[-.03em] tabular-nums text-[oklch(48%_.16_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">04</span><p class="text-[.87rem] tracking-[.02em] text-[oklch(40%_.06_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(82%_.04_calc(var(--h)*1deg))]">Pricing</p></div>
              <div class="[--h:265] grid h-[calc(var(--hs)-1.8rem)] snap-start content-center gap-0.5 border-b border-tfps03-ink/10 bg-[oklch(95%_.045_calc(var(--h)*1deg))] px-[clamp(.9rem,2vw,1.4rem)] tfps03-dark:bg-[oklch(23%_.045_calc(var(--h)*1deg))]"><span class="font-tfps03-mono text-[clamp(1.6rem,4vw,2.4rem)] tracking-[-.03em] tabular-nums text-[oklch(48%_.16_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">05</span><p class="text-[.87rem] tracking-[.02em] text-[oklch(40%_.06_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(82%_.04_calc(var(--h)*1deg))]">Sign up</p></div>
            </div>
          </figure>
          <figure class="grid gap-2.5">
            <figcaption class="flex items-center gap-2 text-[.87rem] text-tfps03-ink/75"><span class="rounded-[.4rem] border px-[.45rem] py-[.2rem] font-tfps03-mono text-[.66rem] tracking-[.08em] text-tfps03-yes">snap-always</span>Flick hard &mdash; it holds</figcaption>
            <div tabindex="0" role="group" aria-label="Scroller with snap stop, five panels" class="h-(--hs) overflow-y-auto snap-y snap-mandatory scroll-smooth overscroll-contain rounded-[1.1rem] border border-tfps03-ink/10 bg-tfps03-ink/[.04] [mask-image:linear-gradient(to_bottom,#000_80%,transparent)] [scrollbar-width:none] [&::-webkit-scrollbar]:hidden focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfps03-acc motion-reduce:snap-none motion-reduce:scroll-auto forced-colors:border-[CanvasText]">
              <div class="[--h:14] grid h-[calc(var(--hs)-1.8rem)] snap-start snap-always motion-reduce:snap-normal content-center gap-0.5 border-b border-tfps03-ink/10 bg-[oklch(95%_.045_calc(var(--h)*1deg))] px-[clamp(.9rem,2vw,1.4rem)] tfps03-dark:bg-[oklch(23%_.045_calc(var(--h)*1deg))]"><span class="font-tfps03-mono text-[clamp(1.6rem,4vw,2.4rem)] tracking-[-.03em] tabular-nums text-[oklch(48%_.16_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">01</span><p class="text-[.87rem] tracking-[.02em] text-[oklch(40%_.06_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(82%_.04_calc(var(--h)*1deg))]">Problem</p></div>
              <div class="[--h:34] grid h-[calc(var(--hs)-1.8rem)] snap-start snap-always motion-reduce:snap-normal content-center gap-0.5 border-b border-tfps03-ink/10 bg-[oklch(95%_.045_calc(var(--h)*1deg))] px-[clamp(.9rem,2vw,1.4rem)] tfps03-dark:bg-[oklch(23%_.045_calc(var(--h)*1deg))]"><span class="font-tfps03-mono text-[clamp(1.6rem,4vw,2.4rem)] tracking-[-.03em] tabular-nums text-[oklch(48%_.16_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">02</span><p class="text-[.87rem] tracking-[.02em] text-[oklch(40%_.06_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(82%_.04_calc(var(--h)*1deg))]">Approach</p></div>
              <div class="[--h:150] grid h-[calc(var(--hs)-1.8rem)] snap-start snap-always motion-reduce:snap-normal content-center gap-0.5 border-b border-tfps03-ink/10 bg-[oklch(95%_.045_calc(var(--h)*1deg))] px-[clamp(.9rem,2vw,1.4rem)] tfps03-dark:bg-[oklch(23%_.045_calc(var(--h)*1deg))]"><span class="font-tfps03-mono text-[clamp(1.6rem,4vw,2.4rem)] tracking-[-.03em] tabular-nums text-[oklch(48%_.16_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">03</span><p class="text-[.87rem] tracking-[.02em] text-[oklch(40%_.06_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(82%_.04_calc(var(--h)*1deg))]">Proof</p></div>
              <div class="[--h:200] grid h-[calc(var(--hs)-1.8rem)] snap-start snap-always motion-reduce:snap-normal content-center gap-0.5 border-b border-tfps03-ink/10 bg-[oklch(95%_.045_calc(var(--h)*1deg))] px-[clamp(.9rem,2vw,1.4rem)] tfps03-dark:bg-[oklch(23%_.045_calc(var(--h)*1deg))]"><span class="font-tfps03-mono text-[clamp(1.6rem,4vw,2.4rem)] tracking-[-.03em] tabular-nums text-[oklch(48%_.16_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">04</span><p class="text-[.87rem] tracking-[.02em] text-[oklch(40%_.06_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(82%_.04_calc(var(--h)*1deg))]">Pricing</p></div>
              <div class="[--h:265] grid h-[calc(var(--hs)-1.8rem)] snap-start snap-always motion-reduce:snap-normal content-center gap-0.5 border-b border-tfps03-ink/10 bg-[oklch(95%_.045_calc(var(--h)*1deg))] px-[clamp(.9rem,2vw,1.4rem)] tfps03-dark:bg-[oklch(23%_.045_calc(var(--h)*1deg))]"><span class="font-tfps03-mono text-[clamp(1.6rem,4vw,2.4rem)] tracking-[-.03em] tabular-nums text-[oklch(48%_.16_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(84%_.11_calc(var(--h)*1deg))]">05</span><p class="text-[.87rem] tracking-[.02em] text-[oklch(40%_.06_calc(var(--h)*1deg))] tfps03-dark:text-[oklch(82%_.04_calc(var(--h)*1deg))]">Sign up</p></div>
            </div>
          </figure>
        </div>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps03-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps03-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps03-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps03-shade)] forced-colors:border-[CanvasText]" id="tfps-03-s2" aria-labelledby="tfps-03-h2">
      <div class="grid w-full max-w-[68rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps03-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps03-acc">02 / 03</span><span class="rounded-[.45rem] border border-tfps03-ink/12 px-2 py-[.22rem] font-tfps03-mono text-[.7rem] text-tfps03-ink/75">where the utility goes</span></p>
        <h2 class="max-w-[28ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-03-h2">On the panel. Never on the scroller.</h2>
        <div class="grid w-full grid-cols-[repeat(auto-fit,minmax(15rem,1fr))] gap-[clamp(.85rem,2vw,1.5rem)]">
          <div class="overflow-hidden rounded-[1.15rem] border border-tfps03-ink/10 bg-tfps03-bg forced-colors:border-[CanvasText]">
            <p class="border-b border-tfps03-ink/10 px-4 py-3 font-tfps03-mono text-[.68rem] tracking-[.12em] uppercase text-tfps03-no">Does nothing</p>
            <pre class="overflow-x-auto overflow-y-hidden px-4 pt-4 pb-5"><code class="text-[clamp(.76rem,1vw,.86rem)] leading-[1.7] whitespace-pre text-tfps03-ink/75 [&_mark]:bg-transparent [&_mark]:text-tfps03-no">&lt;div class="snap-y snap-mandatory
            <mark>snap-always</mark>"&gt;  <mark>&lt;!-- ignored --&gt;</mark></code></pre>
          </div>
          <div class="overflow-hidden rounded-[1.15rem] border border-tfps03-ink/10 bg-tfps03-bg forced-colors:border-[CanvasText]">
            <p class="border-b border-tfps03-ink/10 px-4 py-3 font-tfps03-mono text-[.68rem] tracking-[.12em] uppercase text-tfps03-yes">Works</p>
            <pre class="overflow-x-auto overflow-y-hidden px-4 pt-4 pb-5"><code class="text-[clamp(.76rem,1vw,.86rem)] leading-[1.7] whitespace-pre text-tfps03-ink/75 [&_mark]:bg-transparent [&_mark]:text-tfps03-yes">&lt;section class="snap-start
                <mark>snap-always</mark>"&gt; <mark>&lt;!-- enforced --&gt;</mark></code></pre>
          </div>
        </div>
        <p class="max-w-[60ch] text-[clamp(1rem,1.4vw,1.15rem)] leading-[1.62] text-pretty text-tfps03-ink/75 [&_code]:text-tfps03-ink">It also needs an active <code>snap-start</code> on the same element &mdash; a snap stop with nothing to snap to is inert. And it constrains user gestures only: <code>scrollTo()</code> and anchor jumps still travel as far as you send them.</p>
      </div>
    </section>

    <section class="relative flex min-h-dvh snap-start items-center justify-center bg-tfps03-panel px-[clamp(1.25rem,5vw,4.5rem)] pt-[clamp(2rem,5vh,3.5rem)] pb-[calc(clamp(2rem,5vh,3.5rem)+4rem)] even:bg-tfps03-panel2 not-first:-mt-16 not-first:rounded-t-[1.75rem] not-first:border-t not-first:border-tfps03-ink/10 not-first:shadow-[0_-30px_64px_-34px_var(--color-tfps03-shade)] forced-colors:border-[CanvasText]" id="tfps-03-s3" aria-labelledby="tfps-03-h3">
      <div class="grid w-full max-w-[68rem] justify-items-start gap-[clamp(.95rem,2.3vh,1.5rem)]">
        <p class="flex flex-wrap items-center gap-3"><span class="font-tfps03-mono text-[.7rem] font-medium tracking-[.14em] uppercase text-tfps03-acc">03 / 03</span><span class="rounded-[.45rem] border border-tfps03-ink/12 px-2 py-[.22rem] font-tfps03-mono text-[.7rem] text-tfps03-ink/75">when not to use it</span></p>
        <h2 class="max-w-[28ch] text-[clamp(1.7rem,3.7vw,2.7rem)] leading-[1.06] font-semibold tracking-[-.032em] text-balance" id="tfps-03-h3">Short sequences yes, long pages no</h2>
        <dl class="grid w-full gap-1">
          <div class="grid grid-cols-[minmax(6.5rem,9rem)_1fr] gap-[clamp(.75rem,2vw,1.75rem)] border-t border-tfps03-ink/10 py-[clamp(.75rem,1.5vh,1.05rem)]"><dt class="font-tfps03-mono text-[.86rem] text-tfps03-acc">3&ndash;6 panels</dt><dd class="text-[.97rem] leading-[1.55] text-pretty text-tfps03-ink/75"><strong class="font-semibold text-tfps03-ink">Use it.</strong> Onboarding, a product tour, a pitch. Every panel carries a point the reader must not skip past.</dd></div>
          <div class="grid grid-cols-[minmax(6.5rem,9rem)_1fr] gap-[clamp(.75rem,2vw,1.75rem)] border-t border-tfps03-ink/10 py-[clamp(.75rem,1.5vh,1.05rem)]"><dt class="font-tfps03-mono text-[.86rem] text-tfps03-acc">7+ panels</dt><dd class="text-[.97rem] leading-[1.55] text-pretty text-tfps03-ink/75"><strong class="font-semibold text-tfps03-ink">Leave it off.</strong> One gesture per panel becomes friction, and skimmers &mdash; most of your traffic &mdash; cannot skim.</dd></div>
          <div class="grid grid-cols-[minmax(6.5rem,9rem)_1fr] gap-[clamp(.75rem,2vw,1.75rem)] border-t border-tfps03-ink/10 py-[clamp(.75rem,1.5vh,1.05rem)]"><dt class="font-tfps03-mono text-[.86rem] text-tfps03-acc">Selective</dt><dd class="text-[.97rem] leading-[1.55] text-pretty text-tfps03-ink/75"><strong class="font-semibold text-tfps03-ink">Best of both.</strong> Put <code>snap-always</code> on the two panels that matter (pricing, consent) and leave the rest on <code>snap-normal</code>.</dd></div>
          <div class="grid grid-cols-[minmax(6.5rem,9rem)_1fr] gap-[clamp(.75rem,2vw,1.75rem)] border-t border-tfps03-ink/10 py-[clamp(.75rem,1.5vh,1.05rem)]"><dt class="font-tfps03-mono text-[.86rem] text-tfps03-acc">Reduced motion</dt><dd class="text-[.97rem] leading-[1.55] text-pretty text-tfps03-ink/75"><strong class="font-semibold text-tfps03-ink">Reset it.</strong> With snapping off, forcing one panel per gesture makes no sense &mdash; pair it with <code>motion-reduce:snap-normal</code>.</dd></div>
        </dl>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfps03-bg: #fdfaf6;
  --color-tfps03-bg: oklch(98% .008 75);
  --color-tfps03-panel: #ffffff;
  --color-tfps03-panel: oklch(1 0 0);
  --color-tfps03-panel2: #f6f1ea;
  --color-tfps03-panel2: oklch(95% .014 75);
  --color-tfps03-ink: #171310;
  --color-tfps03-ink: oklch(16% .015 45);
  --color-tfps03-acc: #c2410c;
  --color-tfps03-acc: oklch(56% .18 42);
  --color-tfps03-yes: #15803d;
  --color-tfps03-yes: oklch(52% .14 148);
  --color-tfps03-no: #b91c1c;
  --color-tfps03-no: oklch(52% .19 27);
  --color-tfps03-shade: rgb(23 19 16 / .24);
  --font-tfps03-sans: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tfps03-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace;
}
/* Theme state. Dark = OS preference XOR the toggle, so the switch always flips what you see —
   the CSS original's checkbox did nothing for visitors whose OS was already dark. */

@custom-variant tfps03-dark {
  @media (prefers-color-scheme: light) {
    &:where(.tfps-03:has(#tfps-03-theme:checked), .tfps-03:has(#tfps-03-theme:checked) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: dark) {
    &:where(.tfps-03:not(:has(#tfps-03-theme:checked)), .tfps-03:not(:has(#tfps-03-theme:checked)) *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, stated before the browser build compiles. */

.tfps-03 {
  width: 100%;
  min-height: 100svh;

  @variant tfps03-dark {
    --color-tfps03-bg: #0a0806;
    --color-tfps03-bg: oklch(0.136 0.006 71.3);
    --color-tfps03-panel: #0f0c09;
    --color-tfps03-panel: oklch(0.157 0.008 67.5);
    --color-tfps03-panel2: #161210;
    --color-tfps03-panel2: oklch(0.186 0.008 48.3);
    --color-tfps03-ink: #f8f4ef;
    --color-tfps03-ink: oklch(0.969 0.008 73.7);
    --color-tfps03-acc: #fdba74;
    --color-tfps03-acc: oklch(0.837 0.117 66.3);
    --color-tfps03-yes: #86efac;
    --color-tfps03-yes: oklch(0.871 0.136 154.4);
    --color-tfps03-no: #fca5a5;
    --color-tfps03-no: oklch(0.808 0.103 19.6);
    --color-tfps03-shade: rgb(0 0 0 / .7);
  }
}
```
