---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-marketing-header-sticky-cta-on-scroll/"
title: "Tailwind Marketing Header with Sticky CTA on Scroll"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "A landing-page header that stays quiet until it has earned the ask: logo, nav and a text link at rest, then a solid Start free trial button slides in once…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Marketing Header with Sticky CTA on Scroll
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-marketing-header-sticky-cta-on-scroll/

A landing-page header that stays quiet until it has earned the ask: logo, nav and a text link at rest, then a solid Start free trial button slides in once the reader passes 240&nbsp;px. It is a custom @utility on a scroll(root) timeline — no scroll listener — and where scroll-driven animation is unsupported the button is simply visible from the start.
## HTML
```html
<div class="thd-05 group/thd05 w-full min-h-svh bg-thd05-bg font-thd05-sans text-thd05-ink antialiased">
  <a href="#thd-05-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-lg focus:bg-thd05-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-white">Skip to content</a>
  <div class="sticky top-0 z-40 px-3 pt-3">
    <header class="mx-auto flex max-w-5xl items-center gap-3 rounded-full border border-thd05-line bg-thd05-panel/85 py-1.5 pl-5 pr-1.5 shadow-[0_10px_40px_-20px_rgb(0_0_0/.25)] backdrop-blur-xl">
      <a href="#thd-05-main" class="flex items-center gap-2 text-lg font-extrabold tracking-tight"><span aria-hidden="true" class="flex gap-[3px]"><span class="h-4 w-1 rounded-full bg-thd05-acc"></span><span class="h-4 w-1 translate-y-1 rounded-full bg-thd05-acc/60"></span><span class="h-4 w-1 rounded-full bg-thd05-acc/30"></span></span>Cadence</a>
      <nav aria-label="Main" class="mx-auto hidden md:block">
        <ul class="flex items-center gap-1 text-[15px] font-medium">
          <li><a href="#thd-05-main" class="rounded-full px-3 py-2 text-thd05-mut transition-colors hover:bg-thd05-ink/5 hover:text-thd05-ink">Platform</a></li>
          <li><a href="#thd-05-main" class="rounded-full px-3 py-2 text-thd05-mut transition-colors hover:bg-thd05-ink/5 hover:text-thd05-ink">Customers</a></li>
          <li><a href="#thd-05-main" class="rounded-full px-3 py-2 text-thd05-mut transition-colors hover:bg-thd05-ink/5 hover:text-thd05-ink">Pricing</a></li>
          <li><a href="#thd-05-main" class="rounded-full px-3 py-2 text-thd05-mut transition-colors hover:bg-thd05-ink/5 hover:text-thd05-ink">Resources</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-1 md:ml-0">
        <input id="thd-05-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-05-t" class="grid size-11 cursor-pointer place-items-center rounded-full text-thd05-mut hover:bg-thd05-ink/5 hover:text-thd05-ink peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd05-acc">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-[18px] group-has-[#thd-05-t:checked]/thd05:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-05-t:checked]/thd05:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-05-main" class="thd05-shrink hidden rounded-full px-3 py-2 text-[15px] font-semibold sm:block">Sign in</a>
        <a href="#thd-05-main" class="thd05-reveal flex min-h-11 items-center gap-1.5 whitespace-nowrap rounded-full bg-thd05-acc px-5 text-[15px] font-bold text-white shadow-[0_8px_24px_-8px_var(--color-thd05-acc)] transition-[filter] hover:brightness-110">Start free trial <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="size-4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </div>
    </header>
  </div>
  <main id="thd-05-main" class="mx-auto max-w-5xl px-5 pb-20 pt-[clamp(3.5rem,11vw,7rem)] text-center">
    <p class="mx-auto inline-flex rounded-full bg-thd05-acc/10 px-3 py-1 text-sm font-semibold text-thd05-acc">Scroll 240px &darr;</p>
    <h1 class="mx-auto mt-5 max-w-[16ch] text-[clamp(2.4rem,7.5vw,5rem)] font-extrabold leading-[.98] tracking-[-.04em] text-balance">Meetings that end with a decision.</h1>
    <p class="mx-auto mt-5 max-w-[48ch] text-lg text-thd05-mut text-pretty">Watch the header: the trial button waits until you have read this far, then slides in as <em>Sign in</em> steps aside.</p>
    <div class="mx-auto mt-14 grid max-w-4xl gap-3 text-left sm:grid-cols-3">
      <div class="rounded-3xl bg-thd05-panel p-6 shadow-sm ring-1 ring-thd05-line"><p class="text-3xl font-extrabold tabular-nums text-thd05-acc">31%</p><p class="mt-1 text-sm text-thd05-mut">fewer follow-up meetings</p></div>
      <div class="rounded-3xl bg-thd05-panel p-6 shadow-sm ring-1 ring-thd05-line"><p class="text-3xl font-extrabold tabular-nums text-thd05-acc">4.8/5</p><p class="mt-1 text-sm text-thd05-mut">average G2 rating</p></div>
      <div class="rounded-3xl bg-thd05-panel p-6 shadow-sm ring-1 ring-thd05-line"><p class="text-3xl font-extrabold tabular-nums text-thd05-acc">12 min</p><p class="mt-1 text-sm text-thd05-mut">to first agenda</p></div>
    </div>
    <div aria-hidden="true" class="h-[90svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd05-bg: var(--thd05-bg);
  --color-thd05-panel: var(--thd05-panel);
  --color-thd05-ink: var(--thd05-ink);
  --color-thd05-mut: var(--thd05-mut);
  --color-thd05-line: var(--thd05-line);
  --color-thd05-acc: var(--thd05-acc);
}

@theme {
  --font-thd05-sans: 'Bricolage Grotesque', system-ui, sans-serif;
}

.thd-05 {
  width: 100%;
  min-height: 100svh;
  --thd05-bg: #fbf8f3;
  --thd05-panel: #ffffff;
  --thd05-ink: #1c1917;
  --thd05-mut: #5c544d;
  --thd05-line: rgb(28 25 23 / 0.08);
  --thd05-acc: #e0480f;
}

.thd-05:has(#thd-05-t:checked) {
  --thd05-bg: #121010;
  --thd05-panel: #1c1917;
  --thd05-ink: #f6f1ec;
  --thd05-mut: #b0a79f;
  --thd05-line: rgb(255 255 255 / 0.09);
  --thd05-acc: #ff6a33;
}
/* Scroll-driven utilities: shorthand first, timeline second — one utility guarantees the order. */

@utility thd05-reveal {
  @supports (animation-timeline: scroll()) {
    animation: thd05-reveal linear both;
    animation-timeline: scroll(root);
    animation-range: 200px 280px;
  }
}

@utility thd05-shrink {
  @supports (animation-timeline: scroll()) {
    animation: thd05-shrink linear both;
    animation-timeline: scroll(root);
    animation-range: 200px 280px;
  }
}

@keyframes thd05-reveal {
  from {
    opacity: 0;
    translate: 1.5rem 0;
    scale: 0.92;
  }
}

@keyframes thd05-shrink {
  to {
    opacity: 0.55;
  }
}

@media (prefers-reduced-motion: reduce) {
  .thd05-reveal {
    animation: none !important;
  }
}
```
