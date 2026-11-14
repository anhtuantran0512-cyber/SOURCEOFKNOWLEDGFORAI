---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-header-reading-progress-bar/"
title: "Tailwind Sticky Header with Reading Progress Bar"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "An article header with a hairline progress bar along its bottom edge, a live “4 min left” readout and the story title that slides into the bar once the…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Header with Reading Progress Bar
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-header-reading-progress-bar/

An article header with a hairline progress bar along its bottom edge, a live “4 min left” readout and the story title that slides into the bar once the headline scrolls away. The bar is origin-left scale-x-(--tsn09-p) — Tailwind v4's custom-property shorthand — so the script writes one number per frame and the compositor does the rest.
## HTML
```html
<div class="tsn-09 w-full min-h-svh bg-tsn09-bg font-tsn09-sans text-tsn09-ink antialiased" aria-label="Reading progress bar header demo">
  <header data-tsn09-header class="group/hdr sticky top-0 z-40 border-b border-tsn09-line bg-tsn09-bg/90 backdrop-blur-xl">
    <div class="flex h-14 items-center gap-4 px-[max(1.25rem,calc((100%-72rem)/2))]">
      <a href="#tsn-09-top" class="flex min-h-11 flex-none items-center gap-2 rounded text-[15px] font-semibold tracking-tight focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn09-acc"><span aria-hidden="true" class="size-2.5 rounded-full bg-tsn09-acc"></span>The Long Read</a>
      <p aria-hidden="true" class="min-w-0 flex-1 translate-y-2 truncate font-tsn09-serif text-[15px] italic text-tsn09-mut opacity-0 transition duration-300 group-data-scrolled/hdr:translate-y-0 group-data-scrolled/hdr:opacity-100 motion-reduce:transition-none max-sm:hidden">The quiet engineering of a sticky header</p>
      <p class="ms-auto flex-none rounded-full bg-tsn09-ink/6 px-3 py-1.5 font-tsn09-mono text-xs tabular-nums text-tsn09-mut"><span data-tsn09-left>12 min left</span></p>
    </div>
    <span data-tsn09-bar aria-hidden="true" style="--tsn09-p:0" class="absolute inset-x-0 bottom-0 h-[3px] origin-left scale-x-(--tsn09-p) bg-linear-to-r from-tsn09-acc to-tsn09-acc2"></span>
  </header>
  <article data-minutes="12" id="tsn-09-top" class="scroll-mt-20">
  <div class="px-[max(1.25rem,calc((100%-42rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn09-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn09-acc">Essay · 12 min read</p>
    <h1 class="mt-4 max-w-[18ch] font-tsn09-serif text-[clamp(38px,6vw,64px)] font-medium leading-[1.02] tracking-[-0.02em] text-balance">The quiet engineering of a sticky header</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn09-mut text-pretty">Scroll and watch the hairline under the header. It measures this article — not the page — and the readout counts down the minutes you have left.</p>
  </div>
  <main id="tsn-09-main" class="px-[max(1.25rem,calc((100%-42rem)/2))] grid pb-24">
    <section id="tsn-09-s1" class="scroll-mt-20 min-h-[48svh] border-t border-tsn09-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-09-h1">
      <p class="font-tsn09-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn09-acc">I</p>
      <h2 id="tsn-09-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">A bar you only notice when it’s gone</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn09-mut text-pretty">Readers rarely look at a progress bar directly. They glance at it the way you glance at a watch: to decide whether to keep going. That makes accuracy matter more than decoration.</p>
      <p class="mt-4 max-w-[58ch] font-tsn09-serif text-lg leading-[1.75] text-tsn09-ink/85">So the bar measures the article itself. Footers, comments and related links never count toward “done”, because nobody is reading them yet.</p>
    </section>
    <section id="tsn-09-s2" class="scroll-mt-20 min-h-[48svh] border-t border-tsn09-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-09-h2">
      <p class="font-tsn09-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn09-acc">II</p>
      <h2 id="tsn-09-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Scale, never width</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn09-mut text-pretty">The bar is drawn at full width and scaled down with <code class="rounded-md bg-tsn09-acc/10 px-1.5 py-0.5 font-tsn09-mono text-[0.86em] text-tsn09-ink">scale-x-(--tsn09-p)</code>. The compositor moves it; the layout engine never wakes up.</p>
      <p class="mt-4 max-w-[58ch] font-tsn09-serif text-lg leading-[1.75] text-tsn09-ink/85">Animating width instead would trigger layout on every frame — invisible on a laptop, noticeable on a three-year-old phone halfway through a long piece.</p>
    </section>
    <section id="tsn-09-s3" class="scroll-mt-20 min-h-[48svh] border-t border-tsn09-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-09-h3">
      <p class="font-tsn09-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn09-acc">III</p>
      <h2 id="tsn-09-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Minutes, not percent</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn09-mut text-pretty">Percent is a machine’s unit. “4 min left” is a reader’s. The article carries <code class="rounded-md bg-tsn09-acc/10 px-1.5 py-0.5 font-tsn09-mono text-[0.86em] text-tsn09-ink">data-minutes</code>, and the same tick that writes the bar writes the countdown.</p>
      <p class="mt-4 max-w-[58ch] font-tsn09-serif text-lg leading-[1.75] text-tsn09-ink/85">When the reader reaches the final paragraph, the pill says “Finished”, which is a small and genuinely satisfying moment.</p>
    </section>
    <section id="tsn-09-s4" class="scroll-mt-20 min-h-[48svh] border-t border-tsn09-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-09-h4">
      <p class="font-tsn09-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn09-acc">IV</p>
      <h2 id="tsn-09-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">The title earns its seat</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn09-mut text-pretty">Once the headline scrolls away, the story title slides into the bar in italic, so a reader who looks up always knows where they are.</p>
    </section>
  </main>
  <footer class="border-t border-tsn09-line px-[max(1.25rem,calc((100%-42rem)/2))] py-10 font-tsn09-mono text-xs text-tsn09-mut">Tailwind sticky navigation · pattern 09 of 25</footer>
  </article>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn09-bg: #faf7f2;
  --color-tsn09-bg: oklch(0.975 0.008 80);
  --color-tsn09-surface: #ffffff;
  --color-tsn09-surface: oklch(1 0 0);
  --color-tsn09-ink: #1d1a17;
  --color-tsn09-ink: oklch(0.22 0.01 60);
  --color-tsn09-mut: #5d5751;
  --color-tsn09-mut: oklch(0.46 0.012 60);
  --color-tsn09-acc: #c23a2b;
  --color-tsn09-acc: oklch(0.55 0.18 30);
  --color-tsn09-acc2: #e8873a;
  --color-tsn09-acc2: oklch(0.72 0.15 55);
  --color-tsn09-line: #1d1a171a;
  --color-tsn09-line: oklch(0.22 0.01 60 / 0.1);
  --font-tsn09-serif: 'Newsreader', Georgia, serif;
  --font-tsn09-sans: 'Geist', system-ui, sans-serif;
  --font-tsn09-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-09 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-09) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-09').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const hdr = root.querySelector('[data-tsn09-header]');
    const bar = root.querySelector('[data-tsn09-bar]');
    const left = root.querySelector('[data-tsn09-left]');
    const art = root.querySelector('article');
    const total = Number(art.dataset.minutes) || 1;
    let queued = false;
    const update = () => {
      queued = false;
      const r = art.getBoundingClientRect();
      const span = r.height - innerHeight + hdr.offsetHeight;
      const p = Math.min(1, Math.max(0, (hdr.offsetHeight - r.top) / Math.max(1, span)));
      bar.style.setProperty('--tsn09-p', p.toFixed(4));
      const mins = Math.ceil(total * (1 - p));
      left.textContent = p > 0.985 ? 'Finished' : mins + ' min left';
      hdr.toggleAttribute('data-scrolled', window.scrollY > 280);
    };
    const queue = () => { if (!queued) { queued = true; requestAnimationFrame(update); } };
    window.addEventListener('scroll', queue, { passive: true });
    window.addEventListener('resize', queue);
    update();
  });
})();
```
