---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-article-layout-typography/"
title: "Tailwind Minimalist Article Layout and Typography"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "A long-form column with nothing but measure, rhythm and one moment of emphasis: a 66ch column, a 1.6rem rhythm, a lead one step up the scale with a drop cap,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist Article Layout and Typography
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-article-layout-typography/

A long-form column with nothing but measure, rhythm and one moment of emphasis: a 66ch column, a 1.6rem rhythm, a lead one step up the scale with a drop cap, a single pull quote and a captioned figure. No typography plugin &mdash; every decision is a visible utility, and the drop cap upgrades to initial-letter where the browser supports it.
## HTML
```html
<section class="tmu-18 relative w-full min-h-svh bg-tmu18-bg font-tmu18-serif text-tmu18-ink antialiased" aria-labelledby="tmu18-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu18-theme" type="checkbox" class="peer sr-only">
    <label for="tmu18-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu18-line bg-tmu18-surface text-tmu18-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu18-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu18-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="grid w-full justify-items-center px-5 pt-20 pb-20 md:px-12 md:pt-24">
    <article class="w-full min-w-0 max-w-[66ch] text-(length:--tmu18-body) leading-[1.65]">
      <header class="mb-(--tmu18-rhythm) grid gap-3 border-b border-tmu18-line pb-(--tmu18-rhythm)">
        <p class="font-tmu18-ui text-xs font-semibold uppercase tracking-[0.14em] text-tmu18-acc">Craft</p>
        <h2 id="tmu18-title" class="text-[clamp(2rem,1.5rem+2.6vw,3.25rem)] font-semibold leading-[1.06] tracking-[-0.028em] text-balance">The column is the whole design</h2>
        <p class="flex flex-wrap items-center gap-x-2 gap-y-1 font-tmu18-ui text-[0.8125rem] text-tmu18-ink-2">
          <span aria-hidden="true" class="grid size-7 place-items-center rounded-full bg-tmu18-surface text-[0.6875rem] font-semibold text-tmu18-ink ring-1 ring-tmu18-line">AC</span>
          <span class="font-medium text-tmu18-ink">Alex Chen</span><span aria-hidden="true" class="text-tmu18-line">&middot;</span><span>8 min read</span><span aria-hidden="true" class="text-tmu18-line">&middot;</span><time datetime="2026-08-30">30 August 2026</time>
        </p>
      </header>
      <p data-tmu18-lead class="mb-(--tmu18-rhythm) text-[calc(var(--tmu18-body)*var(--tmu18-ratio))] leading-[1.45] tracking-[-0.012em] text-pretty first-letter:float-left first-letter:pt-[0.04em] first-letter:pr-[0.08em] first-letter:text-[3.1em] first-letter:font-semibold first-letter:leading-[0.84] first-letter:text-tmu18-acc">Measure, rhythm and one moment of emphasis. Everything else an article layout appears to need &mdash; rules, cards, sidebars, badges &mdash; is scaffolding around a column that was already working.</p>
      <p class="mb-(--tmu18-rhythm) text-pretty">Set the measure first. Between 60 and 75 characters is the band where continuous reading stays comfortable, and expressing it in character units rather than pixels means it follows the type size instead of fighting it. A reader who zooms to 140% keeps the same measure, because the measure was never a pixel value.</p>
      <p class="mb-(--tmu18-rhythm) text-pretty">Then set the rhythm. One unit, every margin a multiple of it, headings taking two units of leading where the body takes one. The effect is not decorative: it removes the small inconsistencies that make a page feel unfinished without ever giving the reader something specific to point at.</p>
      <h3 class="mt-[calc(var(--tmu18-rhythm)*1.5)] mb-(--tmu18-rhythm) font-tmu18-ui text-[0.8125rem] font-bold uppercase tracking-[0.12em] text-tmu18-ink-2">One moment of emphasis</h3>
      <p class="mb-(--tmu18-rhythm) text-pretty">The lead paragraph above is one step up the scale. Not three &mdash; one. A lead set at heading size becomes a second headline and the reader has to work out which of the two is the title, which is the exact cognitive cost the hierarchy was supposed to remove.</p>
      <blockquote class="my-[calc(var(--tmu18-rhythm)*1.5)] border-l-2 border-tmu18-acc pl-5">
        <p class="text-[calc(var(--tmu18-body)*var(--tmu18-ratio))] leading-[1.4] tracking-[-0.014em] text-pretty [hanging-punctuation:first]">A pull quote is a navigation device. If it does not reward stopping, it is a gap in the column with type in it.</p>
      </blockquote>
      <p class="mb-(--tmu18-rhythm) text-pretty">The same restraint applies to the quote. Set it in the body family, one or two steps up, and never repeat the sentence directly above it &mdash; a quote that echoes the previous line tells a scanning reader they have already read this part and can safely leave.</p>
      <figure class="my-[calc(var(--tmu18-rhythm)*1.5)]">
        <div role="img" aria-label="Tonal placeholder standing in for an article image, 16 by 9" class="mb-3 grid aspect-video w-full place-items-center rounded-lg border border-tmu18-line bg-tmu18-surface bg-[repeating-linear-gradient(135deg,transparent_0_10px,var(--color-tmu18-line)_10px_11px)]">
          <span class="rounded-full bg-tmu18-surface px-3 py-1 font-tmu18-ui text-xs uppercase tracking-[0.12em] text-tmu18-ink-2">16:9 image area</span>
        </div>
        <figcaption class="font-tmu18-ui text-[0.8125rem] leading-normal text-tmu18-ink-2 text-pretty">Captions sit in the interface face, one size below the body, so they read as apparatus rather than prose.</figcaption>
      </figure>
      <p class="text-pretty">What is deliberately absent: a reading-progress bar, related-article cards, a share rail, and an author box with a photograph. Each is defensible on some sites and none of them make this column easier to read, which is the only question this component has to answer.</p>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu18-bg: light-dark(#fbf8f2, #16130e);
  --color-tmu18-bg: light-dark(oklch(97.8% 0.01 92), oklch(18.5% 0.008 80));
  --color-tmu18-surface: light-dark(#f2ece0, #211d15);
  --color-tmu18-surface: light-dark(oklch(93.5% 0.016 90), oklch(24% 0.012 85));
  --color-tmu18-ink: light-dark(#1a1813, #f4f0e6);
  --color-tmu18-ink: light-dark(oklch(20% 0.008 80), oklch(96% 0.01 90));
  --color-tmu18-ink-2: light-dark(#56503f, #b2a992);
  --color-tmu18-ink-2: light-dark(oklch(45% 0.016 82), oklch(75% 0.018 88));
  --color-tmu18-line: light-dark(#ddd5c2, #3c352a);
  --color-tmu18-line: light-dark(oklch(87% 0.018 88), oklch(33% 0.014 85));
  --color-tmu18-acc: light-dark(#7a3b12, #e79a63);
  --color-tmu18-acc: light-dark(oklch(42% 0.11 50), oklch(76% 0.12 55));
  --font-tmu18-serif: ui-serif, Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
  --font-tmu18-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu18-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
  --tmu18-rhythm: 1.6rem;
  --tmu18-body: 1.125rem;
  --tmu18-ratio: 1.25;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-18:has(#tmu18-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-18:has(#tmu18-theme:checked) {
    color-scheme: light;
  }
}
/* initial-letter needs its -webkit- spelling for Safari, which a supports-[] variant cannot test
   alongside the standard one — so the upgrade stays in CSS. */

@supports (initial-letter: 3) or (-webkit-initial-letter: 3) {
  .tmu-18 [data-tmu18-lead]::first-letter {
    float: none;
    -webkit-initial-letter: 3;
    initial-letter: 3;
    font-size: inherit;
    line-height: inherit;
    padding: 0;
    margin-inline-end: 0.1em;
  }
}
```
