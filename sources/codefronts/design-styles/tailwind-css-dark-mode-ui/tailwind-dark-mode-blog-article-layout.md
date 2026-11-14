---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-blog-article-layout/"
title: "Tailwind Dark Mode Blog Article Reading Layout"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "A reading surface tuned for length: a green-tinted near-black that scatters less than pure black, ink at a deliberate 12:1 rather than a harsh 18:1, a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Blog Article Reading Layout
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-blog-article-layout/

A reading surface tuned for length: a green-tinted near-black that scatters less than pure black, ink at a deliberate 12:1 rather than a harsh 18:1, a 68-character measure, a drop cap and generous leading. A pure-CSS text-size picker writes one custom property; the hero image dims only when the effective theme is dark.
## HTML
```html
<div class="tdm-16 group/root scheme-light-dark has-[#tdm-16-toggle:checked]:scheme-dark dark:has-[#tdm-16-toggle:checked]:scheme-light [--tdm16-size:1.125rem] has-[#tdm-16-sm:checked]:[--tdm16-size:1rem] has-[#tdm-16-lg:checked]:[--tdm16-size:1.25rem] w-full min-h-svh bg-tdm16-forest font-tdm16-serif text-tdm16-ink antialiased transition-colors duration-300">
  <article class="mx-auto grid max-w-[46rem] gap-8 px-5 py-12 sm:px-8 sm:py-16">
    <header class="grid gap-5">
      <div class="flex flex-wrap items-center justify-between gap-3 font-tdm16-sans">
        <p class="text-xs font-medium uppercase tracking-[0.16em] text-tdm16-acc">Craft · 9 min read</p>
        <div class="flex items-center gap-2">
          <fieldset class="flex rounded-xl border border-tdm16-line bg-tdm16-surface p-1">
            <legend class="sr-only">Text size</legend>
            <label class="grid size-9 cursor-pointer place-items-center rounded-lg font-tdm16-serif text-[13px] text-tdm16-muted transition hover:text-tdm16-ink has-checked:bg-tdm16-raised has-checked:text-tdm16-ink has-focus-visible:outline-2 has-focus-visible:outline-tdm16-focus"><input type="radio" name="tdm-16-size" id="tdm-16-sm" class="sr-only"><span aria-hidden="true">A</span><span class="sr-only">Small text</span></label>
            <label class="grid size-9 cursor-pointer place-items-center rounded-lg font-tdm16-serif text-[16px] text-tdm16-muted transition hover:text-tdm16-ink has-checked:bg-tdm16-raised has-checked:text-tdm16-ink has-focus-visible:outline-2 has-focus-visible:outline-tdm16-focus"><input type="radio" name="tdm-16-size" id="tdm-16-md" class="sr-only" checked><span aria-hidden="true">A</span><span class="sr-only">Medium text</span></label>
            <label class="grid size-9 cursor-pointer place-items-center rounded-lg font-tdm16-serif text-[19px] text-tdm16-muted transition hover:text-tdm16-ink has-checked:bg-tdm16-raised has-checked:text-tdm16-ink has-focus-visible:outline-2 has-focus-visible:outline-tdm16-focus"><input type="radio" name="tdm-16-size" id="tdm-16-lg" class="sr-only"><span aria-hidden="true">A</span><span class="sr-only">Large text</span></label>
          </fieldset>
          <label class="relative grid size-11 flex-none cursor-pointer place-items-center rounded-xl border border-tdm16-line bg-tdm16-surface transition duration-200 hover:-translate-y-px hover:border-tdm16-acc/60 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm16-focus motion-reduce:transition-none ">
        <input id="tdm-16-toggle" type="checkbox" class="sr-only">
        <span class="sr-only">Toggle light and dark theme</span>
        <svg class="col-start-1 row-start-1 size-5 text-tdm16-sun transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>
        <svg class="col-start-1 row-start-1 size-5 text-tdm16-moon transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>
      </label>
        </div>
      </div>
      <h1 class="text-[clamp(2.2rem,5.5vw,3.4rem)] font-medium leading-[1.08] tracking-[-0.02em] text-balance">The quiet discipline of reading at night</h1>
      <p class="flex items-center gap-3 font-tdm16-sans text-sm text-tdm16-muted"><span class="grid size-9 place-items-center rounded-full bg-tdm16-acc/15 text-xs font-semibold text-tdm16-acc" aria-hidden="true">PS</span><span>By <strong class="font-semibold text-tdm16-ink">Priya Sharma</strong> · <time datetime="2026-08-14">14 August 2026</time></span></p>
    </header>
    <figure class="grid gap-3">
      <img src="https://picsum.photos/seed/forest-dim-2048/1200/700" width="1200" height="700" alt="Forest at dusk — replace with your article hero image" loading="lazy" decoding="async" class="aspect-[12/7] w-full rounded-2xl object-cover transition-[filter] duration-300 dark:brightness-[.85] dark:group-has-[#tdm-16-toggle:checked]/root:brightness-100! not-dark:group-has-[#tdm-16-toggle:checked]/root:brightness-[.85]">
      <figcaption class="font-tdm16-sans text-[13px] text-tdm16-muted">Images dim to 85% only in the dark theme, so a bright photograph never blows out the page.</figcaption>
    </figure>
    <div class="grid max-w-[68ch] gap-[1.1em] text-(length:--tdm16-size) leading-[1.8] font-[420] text-pretty">
      <p class="first-letter:float-left first-letter:mt-[0.08em] first-letter:mr-3 first-letter:font-tdm16-serif first-letter:text-[3.4em] first-letter:leading-[0.85] first-letter:font-semibold first-letter:text-tdm16-acc">The first thing you notice when you read for four hours on a dark screen is that contrast is not the same as legibility. Pure white on pure black measures beautifully and behaves badly: the letterforms bloom, the counters fill in, and by the third chapter your eyes are doing the work your typographer should have done.</p>
      <p>What actually helps is unglamorous. Give the text a measure it can return from — sixty-eight characters, not a hundred. Set the leading wider than you would on paper, because a backlit line has no physical edge to guide the eye. Then pull the ink back until it sits comfortably above the substrate rather than shouting off it.</p>
      <p>The tint matters more than it should. A substrate with a few degrees of green or blue in it scatters less across the retina than neutral black, which is why the best reading apps have never used <code class="rounded bg-tdm16-surface px-1.5 py-0.5 font-tdm16-mono text-[0.85em]">#000000</code>. It is a small choice that survives every other decision you make.</p>
      <p>None of this is a style. It is the same information architecture as the light theme, designed a second time for a different room and a different hour — which is the only definition of dark mode worth keeping.</p>
    </div>
    <footer class="flex flex-wrap gap-2 border-t border-tdm16-line pt-6 font-tdm16-sans">
      <a href="#tdm-16" class="inline-flex min-h-9 items-center rounded-full border border-tdm16-line px-3.5 text-[13px] text-tdm16-muted transition hover:border-tdm16-acc/60 hover:text-tdm16-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm16-focus">Typography</a>
      <a href="#tdm-16" class="inline-flex min-h-9 items-center rounded-full border border-tdm16-line px-3.5 text-[13px] text-tdm16-muted transition hover:border-tdm16-acc/60 hover:text-tdm16-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm16-focus">Accessibility</a>
      <a href="#tdm-16" class="inline-flex min-h-9 items-center rounded-full border border-tdm16-line px-3.5 text-[13px] text-tdm16-muted transition hover:border-tdm16-acc/60 hover:text-tdm16-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm16-focus">Dark mode</a>
    </footer>
  </article>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm16-forest: light-dark(#f5f7f2, #0a1210);
  --color-tdm16-surface: light-dark(#ebefe7, #0e1815);
  --color-tdm16-raised: light-dark(#ffffff, #16271f);
  --color-tdm16-ink: light-dark(#17221d, #dfe9e2);
  --color-tdm16-muted: light-dark(#4f6158, #9cb0a5);
  --color-tdm16-line: light-dark(rgb(23 34 29 / .13), rgb(226 240 232 / .12));
  --color-tdm16-acc: light-dark(#1f7a50, #7fd6a8);
  --color-tdm16-focus: light-dark(#1f7a50, #a7e8c6);
  --color-tdm16-sun: light-dark(#b45309, transparent);
  --color-tdm16-moon: light-dark(transparent, #a7e8c6);
  --font-tdm16-serif: 'Newsreader', 'Iowan Old Style', Georgia, serif;
  --font-tdm16-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm16-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```
