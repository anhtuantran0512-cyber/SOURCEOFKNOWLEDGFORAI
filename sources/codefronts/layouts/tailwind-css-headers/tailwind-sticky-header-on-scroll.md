---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-sticky-header-on-scroll/"
title: "Tailwind Sticky Header on Scroll with Scroll-Driven Animation"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "The reference sticky header, rebuilt in utilities: sticky top-0, fully transparent at the top, gaining its surface, blur and a glowing gradient rim as the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Header on Scroll with Scroll-Driven Animation
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-sticky-header-on-scroll/

The reference sticky header, rebuilt in utilities: sticky top-0, fully transparent at the top, gaining its surface, blur and a glowing gradient rim as the reader passes the first 80&nbsp;px. No listeners, no position: fixed, no layout shift — and browsers without scroll timelines get the finished bar from the first pixel.
## HTML
```html
<div class="thd-12 group/thd12 w-full min-h-svh bg-thd12-bg bg-[radial-gradient(60rem_30rem_at_50%_-10%,var(--color-thd12-glow),transparent_65%)] font-thd12-sans text-thd12-ink antialiased">
  <a href="#thd-12-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-lg focus:bg-thd12-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-thd12-on">Skip to content</a>
  <header class="thd12-surface sticky top-0 z-40 bg-thd12-bg/80 backdrop-blur-xl after:thd12-rim after:absolute after:inset-x-0 after:bottom-0 after:h-px after:bg-[linear-gradient(90deg,transparent,var(--color-thd12-acc),#22d3ee,transparent)] after:content-['']">
    <div class="mx-auto flex h-16 max-w-6xl items-center gap-4 px-[clamp(.75rem,3vw,1.5rem)]">
      <a href="#thd-12-main" class="flex items-center gap-2.5 text-lg font-semibold tracking-tight"><span aria-hidden="true" class="relative grid size-7 place-items-center rounded-full border border-thd12-acc/60"><span class="size-2.5 rounded-full bg-thd12-acc shadow-[0_0_12px_var(--color-thd12-acc)]"></span><span class="absolute -right-0.5 top-0 size-1.5 rounded-full bg-cyan-300"></span></span>Orbital</a>
      <nav aria-label="Main" class="mx-auto hidden md:block">
        <ul class="flex items-center gap-1 text-sm">
          <li><a href="#thd-12-main" class="rounded-full px-3.5 py-2 text-thd12-mut transition-colors hover:bg-white/5 hover:text-thd12-ink">Overview</a></li>
          <li><a href="#thd-12-main" class="rounded-full px-3.5 py-2 text-thd12-mut transition-colors hover:bg-white/5 hover:text-thd12-ink">Regions</a></li>
          <li><a href="#thd-12-main" class="rounded-full px-3.5 py-2 text-thd12-mut transition-colors hover:bg-white/5 hover:text-thd12-ink">Pricing</a></li>
          <li><a href="#thd-12-main" class="rounded-full px-3.5 py-2 text-thd12-mut transition-colors hover:bg-white/5 hover:text-thd12-ink">Docs</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-1.5 md:ml-0">
        <input id="thd-12-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-12-t" class="grid size-11 cursor-pointer place-items-center rounded-full text-thd12-mut hover:bg-thd12-ink/8 hover:text-thd12-ink peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd12-acc">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="size-[18px] group-has-[#thd-12-t:checked]/thd12:hidden"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-12-t:checked]/thd12:block"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-12-main" class="hidden rounded-full px-3 py-2 text-sm text-thd12-mut hover:text-thd12-ink sm:block">Sign in</a>
        <a href="#thd-12-main" class="relative grid min-h-11 place-items-center overflow-hidden rounded-full bg-thd12-acc px-5 text-sm font-semibold text-thd12-on shadow-[0_0_24px_-6px_var(--color-thd12-acc)] transition hover:shadow-[0_0_32px_-4px_var(--color-thd12-acc)]">Deploy free</a>
      </div>
    </div>
  </header>
  <main id="thd-12-main" class="mx-auto max-w-6xl px-[clamp(.75rem,3vw,1.5rem)] pb-20 pt-[clamp(3rem,10vw,7rem)] text-center">
    <p class="mx-auto inline-flex items-center gap-2 rounded-full border border-thd12-line px-3 py-1 text-xs text-thd12-mut"><span class="size-1.5 rounded-full bg-emerald-400"></span>18 regions live</p>
    <h1 class="mx-auto mt-5 max-w-[15ch] text-[clamp(2.4rem,7vw,4.8rem)] font-semibold leading-[1] tracking-[-.04em] text-balance">Compute that follows your users.</h1>
    <p class="mx-auto mt-5 max-w-[46ch] text-lg text-thd12-mut">Scroll: the bar starts invisible and gains its surface, blur and gradient rim over the first 80px.</p>
    <ul class="mx-auto mt-14 grid max-w-4xl grid-cols-[repeat(auto-fit,minmax(min(100%,14rem),1fr))] gap-3 text-left">
      <li class="rounded-2xl border border-thd12-line bg-thd12-panel p-5"><p class="font-semibold">Anycast by default</p><p class="mt-1 text-sm text-thd12-mut">One IP, nearest region, sub-50ms p50.</p></li>
      <li class="rounded-2xl border border-thd12-line bg-thd12-panel p-5"><p class="font-semibold">Cold starts &lt; 5ms</p><p class="mt-1 text-sm text-thd12-mut">Snapshots restored, not booted.</p></li>
      <li class="rounded-2xl border border-thd12-line bg-thd12-panel p-5"><p class="font-semibold">Per-request billing</p><p class="mt-1 text-sm text-thd12-mut">Idle costs nothing. Truly nothing.</p></li>
    </ul>
    <div aria-hidden="true" class="h-[80svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd12-bg: var(--thd12-bg);
  --color-thd12-panel: var(--thd12-panel);
  --color-thd12-ink: var(--thd12-ink);
  --color-thd12-mut: var(--thd12-mut);
  --color-thd12-line: var(--thd12-line);
  --color-thd12-acc: var(--thd12-acc);
  --color-thd12-on: var(--thd12-on);
  --color-thd12-glow: var(--thd12-glow);
}

@theme {
  --font-thd12-sans: 'Sora', system-ui, sans-serif;
}

.thd-12 {
  width: 100%;
  min-height: 100svh;
  --thd12-bg: #07071a;
  --thd12-panel: #0f0f26;
  --thd12-ink: #eeeefe;
  --thd12-mut: #a3a3c2;
  --thd12-line: rgb(255 255 255 / 0.08);
  --thd12-acc: #8b5cf6;
  --thd12-on: #ffffff;
  --thd12-glow: rgb(139 92 246 / 0.25);
}

.thd-12:has(#thd-12-t:checked) {
  --thd12-bg: #f7f7fc;
  --thd12-panel: #ffffff;
  --thd12-ink: #12122b;
  --thd12-mut: #55557a;
  --thd12-line: rgb(18 18 43 / 0.09);
  --thd12-acc: #6d28d9;
  --thd12-on: #ffffff;
  --thd12-glow: rgb(109 40 217 / 0.12);
}

@utility thd12-surface {
  @supports (animation-timeline: scroll()) {
    animation: thd12-surface linear both;
    animation-timeline: scroll(root);
    animation-range: 0 80px;
  }
}

@utility thd12-rim {
  @supports (animation-timeline: scroll()) {
    animation: thd12-rim linear both;
    animation-timeline: scroll(root);
    animation-range: 0 80px;
  }
}

@keyframes thd12-surface {
  from {
    background-color: transparent;
    backdrop-filter: none;
  }
}

@keyframes thd12-rim {
  from {
    opacity: 0;
  }
}
```
