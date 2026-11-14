---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-3d-flip-business-card-keyboard-reveal/"
title: "Tailwind 3D Flip Business Card with Keyboard Reveal"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A gilt-on-navy calling card that turns on hover and focus-within, so the contact details on the back are reachable by keyboard."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Flip Business Card with Keyboard Reveal
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-3d-flip-business-card-keyboard-reveal/

A gilt-on-navy calling card that turns on hover and focus-within, so the contact details on the back are reachable by keyboard. The port's win is the reduced-motion path: instead of cancelling the flip and hiding the back face forever, it becomes an opacity crossfade &mdash; same information, no spatial motion.
## HTML
```html
<section class="twc-16 w-full min-h-svh flex items-center justify-center px-5 py-9 bg-twc16-bg [background-image:radial-gradient(ellipse_at_30%_20%,#1e293b_0%,transparent_60%),radial-gradient(ellipse_at_80%_80%,#0f172a_0%,transparent_60%)] font-twc16-sans">

  <div tabindex="0" aria-label="Business card for Alex Chen — reveals contact details" class="group w-90 h-55 max-[420px]:w-full max-[420px]:max-w-[360px] rounded-[14px] [perspective:1000px] focus-visible:outline-2 focus-visible:outline-twc16-gilt focus-visible:outline-offset-6">
    <div class="relative size-full [transform-style:preserve-3d] transition-transform duration-700 ease-[cubic-bezier(0.34,1.2,0.64,1)] group-hover:[transform:rotateY(180deg)] group-focus-within:[transform:rotateY(180deg)] shadow-[0_30px_60px_-12px_oklch(0_0_0/0.6),0_18px_36px_-18px_oklch(0.75_0.1_85/0.35)] motion-reduce:transition-none motion-reduce:group-hover:[transform:none] motion-reduce:group-focus-within:[transform:none]">

      <div class="absolute inset-0 flex flex-col justify-between overflow-hidden rounded-[14px] px-7 py-6.5 border border-twc16-gilt/28 [backface-visibility:hidden] [-webkit-backface-visibility:hidden] [background:linear-gradient(135deg,oklch(0.75_0.1_85/0.14)_0%,transparent_40%,transparent_60%,oklch(0.75_0.1_85/0.06)_100%),linear-gradient(160deg,#16213e_0%,#0f172a_50%,#050815_100%)] before:absolute before:top-0 before:right-0 before:w-3/5 before:h-3/5 before:pointer-events-none before:content-[''] before:[background:radial-gradient(circle_at_top_right,oklch(0.87_0.11_90/0.18),transparent_60%)]">
        <div aria-hidden="true" class="flex items-center gap-2.5">
          <span class="relative size-8 rounded-full [background:linear-gradient(135deg,#f5d97b_0%,#d4b063_50%,#9a7a3d_100%)] shadow-[inset_0_-2px_4px_oklch(0_0_0/0.25),inset_0_2px_4px_oklch(1_0_0/0.3),0_2px_6px_oklch(0.75_0.1_85/0.35)] before:absolute before:inset-2 before:rounded-full before:content-[''] before:[background:linear-gradient(135deg,#050815,#16213e)] after:absolute after:inset-0 after:flex after:items-center after:justify-center after:content-['A'] after:font-twc16-serif after:text-[15px] after:font-bold after:text-twc16-giltlite after:[text-shadow:0_1px_2px_oklch(0_0_0/0.6)]"></span>
          <span class="font-twc16-serif text-[11px] font-semibold tracking-[0.24em] uppercase text-twc16-gilt">CHEN &amp; CO</span>
        </div>
        <div class="mb-3">
          <h3 class="m-0 mb-1 font-twc16-serif text-[26px]/[1.1] font-bold tracking-[-0.005em] text-twc16-ink">Alex Chen</h3>
          <p class="m-0 text-[11px] font-medium tracking-[0.14em] uppercase text-twc16-giltlite/85">Principal Designer</p>
        </div>
        <span class="self-end text-[9.5px] tracking-[0.14em] uppercase text-twc16-faint">Hover or tab to flip</span>
      </div>

      <div class="absolute inset-0 flex flex-col justify-between overflow-hidden rounded-[14px] px-7 py-6.5 border border-twc16-gilt/28 [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden] [background:linear-gradient(135deg,oklch(0.75_0.1_85/0.14)_0%,transparent_40%,transparent_60%,oklch(0.75_0.1_85/0.06)_100%),linear-gradient(160deg,#16213e_0%,#0f172a_50%,#050815_100%)] motion-reduce:[transform:none] motion-reduce:[backface-visibility:visible] motion-reduce:opacity-0 motion-reduce:transition-opacity motion-reduce:duration-200 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-within:opacity-100">
        <span class="font-twc16-serif text-[10.5px] font-semibold tracking-[0.28em] uppercase text-twc16-gilt/75">CHEN &amp; CO</span>
        <address class="flex flex-col not-italic">
          <div class="flex items-center gap-3 min-h-11 border-b border-twc16-gilt/15">
            <svg aria-hidden="true" focusable="false" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="flex-none text-twc16-gilt"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            <a href="mailto:[email protected]" class="text-[13px] font-medium tracking-[0.01em] text-twc16-ink2 no-underline transition-colors duration-200 hover:text-twc16-giltlite focus-visible:outline-2 focus-visible:outline-twc16-gilt focus-visible:outline-offset-2">[email protected]</a>
          </div>
          <div class="flex items-center gap-3 min-h-11 border-b border-twc16-gilt/15">
            <svg aria-hidden="true" focusable="false" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="flex-none text-twc16-gilt"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <a href="tel:+14155550142" class="text-[13px] font-medium tracking-[0.01em] text-twc16-ink2 no-underline transition-colors duration-200 hover:text-twc16-giltlite focus-visible:outline-2 focus-visible:outline-twc16-gilt focus-visible:outline-offset-2">+1 (415) 555-0142</a>
          </div>
          <div class="flex items-center gap-3 min-h-11">
            <svg aria-hidden="true" focusable="false" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="flex-none text-twc16-gilt"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            <a href="#site" class="text-[13px] font-medium tracking-[0.01em] text-twc16-ink2 no-underline transition-colors duration-200 hover:text-twc16-giltlite focus-visible:outline-2 focus-visible:outline-twc16-gilt focus-visible:outline-offset-2">alexchen.design</a>
          </div>
        </address>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc16-bg: #050815;
  --color-twc16-bg: oklch(0.13 0.03 265);
  --color-twc16-ink: #f8fafc;
  --color-twc16-ink: oklch(0.98 0.005 250);
  --color-twc16-ink2: #e2e8f0;
  --color-twc16-ink2: oklch(0.92 0.01 250);
  --color-twc16-faint: #94a3b8;
  --color-twc16-faint: oklch(0.7 0.03 250);
  --color-twc16-gilt: #d4b063;
  --color-twc16-gilt: oklch(0.75 0.1 85);
  --color-twc16-giltlite: #f5d97b;
  --color-twc16-giltlite: oklch(0.87 0.11 90);
  --font-twc16-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc16-serif: 'Cormorant Garamond', Georgia, 'Times New Roman', serif;
}
/* 3D transform properties, backface hiding and perspective have no utilities
   and should not: they are structural, not design-scale. They ship as
   arbitrary properties in the markup. */

.twc-16 {
  width: 100%;
  min-height: 100svh;
}
```
