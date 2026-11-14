---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-vertical-rhythm-baseline-grid/"
title: "Tailwind Vertical Rhythm with a Consistent Baseline"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "An article column where every line and block boundary lands on a 1.5rem rhythm, set once as --tmu07-rhythm and consumed through leading-(--tmu07-rhythm) and…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vertical Rhythm with a Consistent Baseline
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-vertical-rhythm-baseline-grid/

An article column where every line and block boundary lands on a 1.5rem rhythm, set once as --tmu07-rhythm and consumed through leading-(--tmu07-rhythm) and mb-(--tmu07-rhythm). Press the button (or G) to draw the baseline grid over it &mdash; a data-grid: variant swaps in a repeating-linear-gradient background, and the image block shows where strict rhythm stops being free.
## HTML
```html
<section class="tmu-07 relative w-full min-h-svh bg-tmu07-bg font-tmu07-ui text-tmu07-ink antialiased" aria-labelledby="tmu07-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu07-theme" type="checkbox" class="peer sr-only">
    <label for="tmu07-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu07-line bg-tmu07-surface text-tmu07-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu07-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu07-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[60rem] gap-12 px-6 pt-20 pb-24 md:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu07-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu07-ink-2"><span class="tabular-nums text-tmu07-acc">07</span><span aria-hidden="true" class="h-px w-6 bg-tmu07-line"></span>Rhythm</p>
      <h2 id="tmu07-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">One unit, every line</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu07-ink-2 text-pretty">Body lines take one unit, headings take two, gaps take one. Turn the overlay on: every block starts on a rule.</p>
    </header>
    <div class="flex flex-wrap items-center gap-x-4 gap-y-3">
      <button id="tmu07-grid-btn" type="button" aria-pressed="false" class="group inline-flex min-h-11 min-w-11 items-center gap-2 rounded-md border border-tmu07-line bg-tmu07-surface px-4 text-sm font-medium text-tmu07-ink cursor-pointer shadow-[0_1px_2px_rgb(0_0_0/0.05)] transition-[border-color,color] duration-150 hover:border-tmu07-acc aria-pressed:border-tmu07-acc aria-pressed:text-tmu07-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu07-acc motion-reduce:transition-none">
        <svg class="size-[18px] flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 6h18M3 12h18M3 18h18" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>
        Baseline overlay
        <kbd class="ml-1 rounded border border-tmu07-line px-1.5 font-tmu07-mono text-[0.6875rem] text-tmu07-ink-2 group-aria-pressed:border-tmu07-acc group-aria-pressed:text-tmu07-acc">G</kbd>
      </button>
      <p class="text-[0.8125rem] tabular-nums text-tmu07-ink-2">Unit <b class="font-semibold text-tmu07-ink">1.5rem</b> &middot; 24px at a 16px root</p>
    </div>
    <article id="tmu07-article" class="relative min-w-0 max-w-[66ch] font-tmu07-serif text-[1.0625rem] leading-(--tmu07-rhythm) text-pretty data-grid:bg-[repeating-linear-gradient(to_bottom,var(--color-tmu07-grid)_0,var(--color-tmu07-grid)_1px,transparent_1px,transparent_var(--tmu07-rhythm))]">
      <h3 class="mb-(--tmu07-rhythm) text-2xl font-semibold leading-[calc(var(--tmu07-rhythm)*2)] tracking-[-0.018em] text-balance">Rhythm survives real content, grids do not</h3>
      <p class="mb-(--tmu07-rhythm) text-[1.1875rem] leading-[calc(var(--tmu07-rhythm)*1.5)]">Set the rhythm once and the column composes itself. Body copy takes one unit per line, a heading takes two, and the gap between blocks takes one &mdash; so the eye reads order it cannot name.</p>
      <p class="mb-(--tmu07-rhythm)">Turn the overlay on and the mechanism becomes obvious: every line of prose sits on a rule, and every block boundary lands on one too. Nothing here is hand-nudged. The whole column is derived from a single custom property, which means the rhythm can be retuned for a different reading size in one edit.</p>
      <h4 class="mt-[calc(var(--tmu07-rhythm)*2)] mb-(--tmu07-rhythm) font-tmu07-ui text-[0.8125rem] font-bold uppercase leading-(--tmu07-rhythm) tracking-[0.1em] text-tmu07-ink-2">Where it stops being free</h4>
      <p class="mb-(--tmu07-rhythm)">The image below is 3:2, which is not a multiple of anything. Its caption is smaller than the body, so its own line height is not a whole unit either. A strict per-line grid would need padding calculated from the image height &mdash; a value that changes with the viewport, so the correction cannot be static.</p>
      <figure class="mt-[calc(var(--tmu07-rhythm)*2)] mb-(--tmu07-rhythm)">
        <div role="img" aria-label="Tonal placeholder standing in for an article image, 3 by 2" class="mb-(--tmu07-rhythm) grid aspect-[3/2] w-full place-items-center rounded-lg border border-tmu07-line bg-tmu07-surface bg-[repeating-linear-gradient(135deg,transparent_0_10px,var(--color-tmu07-line)_10px_11px)]">
          <span class="rounded-full bg-tmu07-surface px-3 py-1 font-tmu07-ui text-xs uppercase tracking-[0.1em] text-tmu07-ink-2">3:2 image area</span>
        </div>
        <figcaption class="font-tmu07-ui text-[0.8125rem] leading-(--tmu07-rhythm) text-tmu07-ink-2">A block on the grid, with an interior that is not. This is the compromise that keeps the system usable.</figcaption>
      </figure>
      <p class="mb-(--tmu07-rhythm)">The practical answer is rhythm at the block level. Each block <em>starts</em> on the grid; its interior may not. That is nine-tenths of the perceived order at a tenth of the fragility, and it holds when an editor adds a pull quote, a table, or an embed you did not plan for.</p>
      <blockquote class="my-[calc(var(--tmu07-rhythm)*2)] border-l-2 border-tmu07-acc pl-5">
        <p class="text-[1.3125rem] leading-[calc(var(--tmu07-rhythm)*1.5)] tracking-[-0.014em]">If the correction has to be recalculated every time the content changes, it is not a system.</p>
      </blockquote>
      <p>Where a print designer can force every element onto the baseline because the page is fixed, a web page is not. Accepting that is what separates a rhythm that ships from a grid that gets quietly deleted in the third sprint.</p>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu07-bg: light-dark(#faf6ee, #14120e);
  --color-tmu07-bg: light-dark(oklch(97.5% 0.012 88), oklch(18% 0.009 70));
  --color-tmu07-surface: light-dark(#fffdf8, #1c1914);
  --color-tmu07-surface: light-dark(oklch(99.2% 0.006 88), oklch(22.5% 0.01 72));
  --color-tmu07-ink: light-dark(#1a1712, #f4efe4);
  --color-tmu07-ink: light-dark(oklch(20% 0.01 70), oklch(96% 0.012 88));
  --color-tmu07-ink-2: light-dark(#57503f, #b3a993);
  --color-tmu07-ink-2: light-dark(oklch(45% 0.018 78), oklch(76% 0.02 85));
  --color-tmu07-line: light-dark(#ddd4c1, #3b342a);
  --color-tmu07-line: light-dark(oklch(87% 0.02 85), oklch(33% 0.015 78));
  --color-tmu07-grid: light-dark(rgba(139, 74, 20, 0.22), rgba(232, 168, 106, 0.24));
  --color-tmu07-acc: light-dark(#8b4a14, #e8a86a);
  --color-tmu07-acc: light-dark(oklch(45% 0.12 55), oklch(79% 0.11 60));
  --font-tmu07-serif: ui-serif, Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
  --font-tmu07-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu07-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
  --tmu07-rhythm: 1.5rem;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-07:has(#tmu07-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-07:has(#tmu07-theme:checked) {
    color-scheme: light;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tmu-07');
  if (!root) return;
  const btn = root.querySelector('#tmu07-grid-btn');
  const article = root.querySelector('#tmu07-article');
  if (!btn || !article) return;

  const setGrid = (on) => {
    btn.setAttribute('aria-pressed', String(on));
    article.toggleAttribute('data-grid', on);
  };
  const onClick = () => setGrid(btn.getAttribute('aria-pressed') !== 'true');
  const onKey = (e) => {
    if (e.target.closest('input, textarea, select, [contenteditable]')) return;
    if (e.key.toLowerCase() === 'g' && !e.metaKey && !e.ctrlKey && !e.altKey) onClick();
  };

  btn.addEventListener('click', onClick);
  document.addEventListener('keydown', onKey);

  root.__tmuCleanup = () => {
    btn.removeEventListener('click', onClick);
    document.removeEventListener('keydown', onKey);
    setGrid(false);
  };
})();
```
