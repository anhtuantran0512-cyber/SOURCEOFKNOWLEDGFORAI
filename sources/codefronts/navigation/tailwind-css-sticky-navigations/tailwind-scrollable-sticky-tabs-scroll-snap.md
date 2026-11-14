---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-scrollable-sticky-tabs-scroll-snap/"
title: "Tailwind Scrollable Sticky Tabs with Scroll Snap"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "A news-style category rail that scrolls sideways with snap-x snap-mandatory, fades its edges only when there's more to see, shows arrow buttons on mouse…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scrollable Sticky Tabs with Scroll Snap
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-scrollable-sticky-tabs-scroll-snap/

A news-style category rail that scrolls sideways with snap-x snap-mandatory, fades its edges only when there's more to see, shows arrow buttons on mouse devices (pointer-coarse:hidden), and follows your reading: as each section passes, its tab becomes current and the rail glides to keep it centred.
## HTML
```html
<div class="tsn-24 w-full min-h-svh bg-tsn24-bg font-tsn24-sans text-tsn24-ink antialiased" aria-label="Sticky horizontal scroll tab bar with snap demo">
  <header class="sticky top-0 z-40 border-b border-tsn24-ink bg-tsn24-bg/95 backdrop-blur-md">
    <div class="flex h-14 items-center justify-between gap-4 px-[max(1.25rem,calc((100%-72rem)/2))]">
      <a href="#tsn-24-s1" class="flex min-h-11 items-center rounded font-tsn24-serif text-[28px] font-semibold tracking-[-0.02em] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn24-acc">The Gazette</a>
      <p class="font-tsn24-mono text-[11px] uppercase tracking-[0.14em] text-tsn24-mut max-sm:hidden">Sunday · 4 October 2026</p>
    </div>
    <div data-tsn24-wrap class="group/rail relative">
      <span aria-hidden="true" class="pointer-events-none absolute inset-y-0 left-0 z-10 w-14 bg-linear-to-r from-tsn24-bg to-transparent opacity-0 transition-opacity group-data-left/rail:opacity-100"></span>
      <span aria-hidden="true" class="pointer-events-none absolute inset-y-0 right-0 z-10 w-14 bg-linear-to-l from-tsn24-bg to-transparent opacity-0 transition-opacity group-data-right/rail:opacity-100"></span>
      <button type="button" data-tsn24-prev tabindex="-1" aria-hidden="true" class="invisible absolute left-2 top-1/2 z-20 grid size-9 -translate-y-1/2 place-items-center rounded-full border border-tsn24-line bg-tsn24-surface shadow-[0_2px_8px_rgb(0_0_0/0.12)] hover:border-tsn24-ink group-data-left/rail:visible pointer-coarse:hidden"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m15 6-6 6 6 6"/></svg></button>
      <button type="button" data-tsn24-next tabindex="-1" aria-hidden="true" class="invisible absolute right-2 top-1/2 z-20 grid size-9 -translate-y-1/2 place-items-center rounded-full border border-tsn24-line bg-tsn24-surface shadow-[0_2px_8px_rgb(0_0_0/0.12)] hover:border-tsn24-ink group-data-right/rail:visible pointer-coarse:hidden"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m9 6 6 6-6 6"/></svg></button>
      <nav data-tsn24-rail aria-label="Sections" class="flex snap-x snap-mandatory scroll-px-5 gap-1.5 overflow-x-auto px-[max(1.25rem,calc((100%-72rem)/2))] py-2.5 [scrollbar-width:none]">
        <a href="#tsn-24-s1" aria-current="true" class="inline-flex min-h-10 flex-none snap-start items-center rounded-full border border-tsn24-line px-4 text-[13.5px] font-semibold whitespace-nowrap text-tsn24-mut transition-colors hover:border-tsn24-ink hover:text-tsn24-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn24-acc aria-[current=true]:border-tsn24-ink aria-[current=true]:bg-tsn24-ink aria-[current=true]:text-tsn24-bg">Top stories</a>
        <a href="#tsn-24-s2" class="inline-flex min-h-10 flex-none snap-start items-center rounded-full border border-tsn24-line px-4 text-[13.5px] font-semibold whitespace-nowrap text-tsn24-mut transition-colors hover:border-tsn24-ink hover:text-tsn24-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn24-acc aria-[current=true]:border-tsn24-ink aria-[current=true]:bg-tsn24-ink aria-[current=true]:text-tsn24-bg">World</a>
        <a href="#tsn-24-s3" class="inline-flex min-h-10 flex-none snap-start items-center rounded-full border border-tsn24-line px-4 text-[13.5px] font-semibold whitespace-nowrap text-tsn24-mut transition-colors hover:border-tsn24-ink hover:text-tsn24-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn24-acc aria-[current=true]:border-tsn24-ink aria-[current=true]:bg-tsn24-ink aria-[current=true]:text-tsn24-bg">Politics</a>
        <a href="#tsn-24-s4" class="inline-flex min-h-10 flex-none snap-start items-center rounded-full border border-tsn24-line px-4 text-[13.5px] font-semibold whitespace-nowrap text-tsn24-mut transition-colors hover:border-tsn24-ink hover:text-tsn24-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn24-acc aria-[current=true]:border-tsn24-ink aria-[current=true]:bg-tsn24-ink aria-[current=true]:text-tsn24-bg">Business</a>
        <a href="#tsn-24-s5" class="inline-flex min-h-10 flex-none snap-start items-center rounded-full border border-tsn24-line px-4 text-[13.5px] font-semibold whitespace-nowrap text-tsn24-mut transition-colors hover:border-tsn24-ink hover:text-tsn24-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn24-acc aria-[current=true]:border-tsn24-ink aria-[current=true]:bg-tsn24-ink aria-[current=true]:text-tsn24-bg">Technology</a>
        <a href="#tsn-24-s6" class="inline-flex min-h-10 flex-none snap-start items-center rounded-full border border-tsn24-line px-4 text-[13.5px] font-semibold whitespace-nowrap text-tsn24-mut transition-colors hover:border-tsn24-ink hover:text-tsn24-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn24-acc aria-[current=true]:border-tsn24-ink aria-[current=true]:bg-tsn24-ink aria-[current=true]:text-tsn24-bg">Science</a>
        <a href="#tsn-24-s7" class="inline-flex min-h-10 flex-none snap-start items-center rounded-full border border-tsn24-line px-4 text-[13.5px] font-semibold whitespace-nowrap text-tsn24-mut transition-colors hover:border-tsn24-ink hover:text-tsn24-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn24-acc aria-[current=true]:border-tsn24-ink aria-[current=true]:bg-tsn24-ink aria-[current=true]:text-tsn24-bg">Climate</a>
        <a href="#tsn-24-s8" class="inline-flex min-h-10 flex-none snap-start items-center rounded-full border border-tsn24-line px-4 text-[13.5px] font-semibold whitespace-nowrap text-tsn24-mut transition-colors hover:border-tsn24-ink hover:text-tsn24-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn24-acc aria-[current=true]:border-tsn24-ink aria-[current=true]:bg-tsn24-ink aria-[current=true]:text-tsn24-bg">Health</a>
        <a href="#tsn-24-s9" class="inline-flex min-h-10 flex-none snap-start items-center rounded-full border border-tsn24-line px-4 text-[13.5px] font-semibold whitespace-nowrap text-tsn24-mut transition-colors hover:border-tsn24-ink hover:text-tsn24-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn24-acc aria-[current=true]:border-tsn24-ink aria-[current=true]:bg-tsn24-ink aria-[current=true]:text-tsn24-bg">Culture</a>
        <a href="#tsn-24-s10" class="inline-flex min-h-10 flex-none snap-start items-center rounded-full border border-tsn24-line px-4 text-[13.5px] font-semibold whitespace-nowrap text-tsn24-mut transition-colors hover:border-tsn24-ink hover:text-tsn24-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn24-acc aria-[current=true]:border-tsn24-ink aria-[current=true]:bg-tsn24-ink aria-[current=true]:text-tsn24-bg">Sport</a>
      </nav>
    </div>
  </header>
  <main id="tsn-24-main" class="px-[max(1.25rem,calc((100%-52rem)/2))] grid pt-[clamp(2rem,5vw,3.5rem)] pb-24">
    <section id="tsn-24-s1" class="scroll-mt-32 min-h-[48svh] border-t border-tsn24-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-24-h1">
      <p class="font-tsn24-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn24-acc">Top stories</p>
      <h2 id="tsn-24-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">A rail that follows your reading</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn24-mut text-pretty">The day’s most important reporting, chosen by editors rather than algorithms. Scroll the page: the current section’s tab lights up and the rail glides to keep it centred. On a mouse, arrows appear at whichever edge has more.</p>
    </section>
    <section id="tsn-24-s2" class="scroll-mt-32 min-h-[48svh] border-t border-tsn24-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-24-h2">
      <p class="font-tsn24-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn24-acc">World</p>
      <h2 id="tsn-24-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">World desk</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn24-mut text-pretty">Correspondents in forty countries file before dawn so you can read over breakfast.</p>
    </section>
    <section id="tsn-24-s3" class="scroll-mt-32 min-h-[48svh] border-t border-tsn24-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-24-h3">
      <p class="font-tsn24-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn24-acc">Politics</p>
      <h2 id="tsn-24-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Politics desk</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn24-mut text-pretty">Policy, not horse-race: what changed, who it affects, and what happens next.</p>
    </section>
    <section id="tsn-24-s4" class="scroll-mt-32 min-h-[48svh] border-t border-tsn24-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-24-h4">
      <p class="font-tsn24-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn24-acc">Business</p>
      <h2 id="tsn-24-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Business desk</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn24-mut text-pretty">Markets, earnings and the economics behind the headlines, explained plainly.</p>
    </section>
    <section id="tsn-24-s5" class="scroll-mt-32 min-h-[48svh] border-t border-tsn24-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-24-h5">
      <p class="font-tsn24-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn24-acc">Technology</p>
      <h2 id="tsn-24-h5" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Technology desk</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn24-mut text-pretty">How the tools we use every day are built, governed and occasionally broken.</p>
    </section>
    <section id="tsn-24-s6" class="scroll-mt-32 min-h-[48svh] border-t border-tsn24-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-24-h6">
      <p class="font-tsn24-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn24-acc">Science</p>
      <h2 id="tsn-24-h6" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Science desk</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn24-mut text-pretty">Discoveries worth your attention, with the caveats the press release left out.</p>
    </section>
    <section id="tsn-24-s7" class="scroll-mt-32 min-h-[48svh] border-t border-tsn24-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-24-h7">
      <p class="font-tsn24-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn24-acc">Climate</p>
      <h2 id="tsn-24-h7" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Climate desk</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn24-mut text-pretty">The changing planet, covered with data, field reporting and no false balance.</p>
    </section>
    <section id="tsn-24-s8" class="scroll-mt-32 min-h-[48svh] border-t border-tsn24-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-24-h8">
      <p class="font-tsn24-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn24-acc">Health</p>
      <h2 id="tsn-24-h8" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Health desk</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn24-mut text-pretty">Evidence-led reporting on medicine, wellbeing and the systems that deliver them.</p>
    </section>
    <section id="tsn-24-s9" class="scroll-mt-32 min-h-[48svh] border-t border-tsn24-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-24-h9">
      <p class="font-tsn24-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn24-acc">Culture</p>
      <h2 id="tsn-24-h9" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Culture desk</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn24-mut text-pretty">Books, film, music and the arguments they start.</p>
    </section>
    <section id="tsn-24-s10" class="scroll-mt-32 min-h-[48svh] border-t border-tsn24-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-24-h10">
      <p class="font-tsn24-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn24-acc">Sport</p>
      <h2 id="tsn-24-h10" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Sport desk</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn24-mut text-pretty">Results, analysis and the long reads that outlast the final whistle.</p>
    </section>
  </main>
  <footer class="border-t border-tsn24-line px-[max(1.25rem,calc((100%-52rem)/2))] py-10 font-tsn24-mono text-xs text-tsn24-mut">Tailwind sticky navigation · pattern 24 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn24-bg: #f6f3ec;
  --color-tsn24-bg: oklch(0.963 0.01 85);
  --color-tsn24-surface: #fffdf8;
  --color-tsn24-surface: oklch(0.994 0.006 85);
  --color-tsn24-ink: #14130f;
  --color-tsn24-ink: oklch(0.19 0.008 90);
  --color-tsn24-mut: #55524a;
  --color-tsn24-mut: oklch(0.44 0.012 90);
  --color-tsn24-acc: #b4232a;
  --color-tsn24-acc: oklch(0.5 0.18 25);
  --color-tsn24-line: #14130f26;
  --color-tsn24-line: oklch(0.19 0.008 90 / 0.15);
  --font-tsn24-serif: 'Newsreader', Georgia, serif;
  --font-tsn24-sans: 'Public Sans', system-ui, sans-serif;
  --font-tsn24-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-24 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-24) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-24').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const wrap = root.querySelector('[data-tsn24-wrap]');
    const rail = root.querySelector('[data-tsn24-rail]');
    const tabs = [...rail.querySelectorAll('a')];
    const edges = () => {
      wrap.toggleAttribute('data-left', rail.scrollLeft > 4);
      wrap.toggleAttribute('data-right', rail.scrollLeft + rail.clientWidth < rail.scrollWidth - 4);
    };
    rail.addEventListener('scroll', edges, { passive: true });
    new ResizeObserver(edges).observe(rail);
    const step = (dir) => rail.scrollBy({ left: dir * rail.clientWidth * 0.7, behavior: 'smooth' });
    root.querySelector('[data-tsn24-prev]').addEventListener('click', () => step(-1));
    root.querySelector('[data-tsn24-next]').addEventListener('click', () => step(1));
    const centre = (t) => rail.scrollTo({ left: t.offsetLeft - rail.clientWidth / 2 + t.offsetWidth / 2, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        const t = tabs.find((a) => a.hash === '#' + e.target.id);
        if (!t) return;
        tabs.forEach((a) => a.setAttribute('aria-current', String(a === t)));
        centre(t);
      });
    }, { rootMargin: '-140px 0px -60% 0px' });
    tabs.forEach((a) => { const s = root.querySelector(a.hash); if (s) io.observe(s); });
    edges();
  });
})();
```
