---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-dark-mode-gradient-text-toggle/"
title: "Tailwind Dark Mode Gradient Text Toggle"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "One card, two palettes: vivid neon gradients on dark, rich jewel tones on light."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Gradient Text Toggle
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-dark-mode-gradient-text-toggle/

One card, two palettes: vivid neon gradients on dark, rich jewel tones on light. Because v4 utilities reference theme variables, the script just flips data-theme and a scoped rule re-points every --color-ttg20-* &mdash; headline, logo, chips and toggle all follow. It honours prefers-color-scheme on first load and remembers the choice.
## HTML
```html
<section class="ttg-20 group/t w-full min-h-svh grid place-items-center bg-ttg20-bg px-5 py-14 font-ttg20-sans text-ttg20-ink transition-colors duration-300 motion-reduce:transition-none" id="ttg20-root" aria-label="Dark mode vs light mode gradient text demo">
  <article class="w-full max-w-lg rounded-3xl border border-ttg20-line bg-ttg20-card p-9 shadow-[0_30px_60px_-30px_rgb(0_0_0/0.45)] transition-colors duration-300 motion-reduce:transition-none max-sm:p-7">
    <header class="flex items-center justify-between">
      <p class="flex items-center gap-2.5 text-xl font-extrabold tracking-[-0.02em]"><span aria-hidden="true" class="size-6 rounded-md bg-linear-135 from-ttg20-a via-ttg20-b to-ttg20-c"></span><span class="bg-linear-110 from-ttg20-a via-ttg20-b to-ttg20-c bg-clip-text text-transparent">Lumis</span></p>
      <button type="button" id="ttg20-toggle" aria-pressed="false" class="inline-flex min-h-11 items-center gap-2 rounded-full border border-ttg20-line bg-ttg20-chip px-4 text-sm font-semibold transition hover:border-ttg20-b focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttg20-b">
        <svg class="size-4 group-data-[theme=light]/t:hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
        <svg class="hidden size-4 group-data-[theme=light]/t:block" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
        <span data-ttg20-label>Dark</span>
      </button>
    </header>
    <h1 class="mt-9 text-[clamp(2rem,6vw,2.9rem)] leading-[1.08] font-bold tracking-[-0.035em]">Adaptive <span class="bg-linear-110 from-ttg20-a via-ttg20-b to-ttg20-c bg-clip-text text-transparent">colour</span><br>for every context</h1>
    <p class="mt-4 text-[15.5px]/[1.7] text-ttg20-mut text-pretty">Light, airy stops pop on dark grounds; deeper jewel tones hold contrast on light ones. One class list, two token sets.</p>
    <div class="mt-7 flex flex-wrap gap-2.5">
      <span class="rounded-full border border-ttg20-line bg-ttg20-chip px-3.5 py-1.5 text-[13px] font-bold"><span class="bg-linear-to-r from-ttg20-a to-ttg20-c bg-clip-text text-transparent">Dark · vivid neon</span></span>
      <span class="rounded-full border border-ttg20-line bg-ttg20-chip px-3.5 py-1.5 text-[13px] font-bold"><span class="bg-linear-to-r from-ttg20-d to-ttg20-e bg-clip-text text-transparent">Light · rich jewel</span></span>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Dark is the default token set. */

@theme {
  --color-ttg20-bg: #07050f;
  --color-ttg20-bg: oklch(0.13 0.02 290);
  --color-ttg20-card: #110f1c;
  --color-ttg20-card: oklch(0.18 0.025 290);
  --color-ttg20-chip: #1b1829;
  --color-ttg20-chip: oklch(0.22 0.03 290);
  --color-ttg20-line: #2b2740;
  --color-ttg20-line: oklch(0.3 0.035 290);
  --color-ttg20-ink: #f4effc;
  --color-ttg20-ink: oklch(0.96 0.015 305);
  --color-ttg20-mut: #bcb3cf;
  --color-ttg20-mut: oklch(0.79 0.035 300);
  --color-ttg20-a: #f2b0ff;
  --color-ttg20-a: oklch(0.84 0.13 320);
  --color-ttg20-b: #9aa1ff;
  --color-ttg20-b: oklch(0.75 0.14 278);
  --color-ttg20-c: #6fd2ff;
  --color-ttg20-c: oklch(0.83 0.12 225);
  --color-ttg20-d: #4ee3b0;
  --color-ttg20-d: oklch(0.84 0.14 165);
  --color-ttg20-e: #3cc8ea;
  --color-ttg20-e: oklch(0.79 0.12 215);
  --font-ttg20-sans: 'Outfit', system-ui, sans-serif;
}

.ttg-20 {
  width: 100%;
  min-height: 100svh;
}
/* Light token set — re-points the same variables, so every utility follows. */

.ttg-20[data-theme='light'] {
  --color-ttg20-bg: oklch(0.975 0.005 260);
  --color-ttg20-card: oklch(1 0 0);
  --color-ttg20-chip: oklch(0.965 0.008 270);
  --color-ttg20-line: oklch(0.91 0.012 270);
  --color-ttg20-ink: oklch(0.21 0.035 270);
  --color-ttg20-mut: oklch(0.47 0.03 265);
  --color-ttg20-a: oklch(0.5 0.22 275);
  --color-ttg20-b: oklch(0.5 0.24 295);
  --color-ttg20-c: oklch(0.5 0.22 325);
  --color-ttg20-d: oklch(0.5 0.1 180);
  --color-ttg20-e: oklch(0.5 0.13 235);
}

@media (prefers-color-scheme: light) {
  .ttg-20:not([data-theme]) {
    --color-ttg20-bg: oklch(0.975 0.005 260);
    --color-ttg20-card: oklch(1 0 0);
    --color-ttg20-chip: oklch(0.965 0.008 270);
    --color-ttg20-line: oklch(0.91 0.012 270);
    --color-ttg20-ink: oklch(0.21 0.035 270);
    --color-ttg20-mut: oklch(0.47 0.03 265);
    --color-ttg20-a: oklch(0.5 0.22 275);
    --color-ttg20-b: oklch(0.5 0.24 295);
    --color-ttg20-c: oklch(0.5 0.22 325);
    --color-ttg20-d: oklch(0.5 0.1 180);
    --color-ttg20-e: oklch(0.5 0.13 235);
  }
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('ttg20-root');
  const btn = document.getElementById('ttg20-toggle');
  if (!root || !btn || root.dataset.wired) return;
  root.dataset.wired = '1';
  const label = btn.querySelector('[data-ttg20-label]');
  const KEY = 'ttg20-theme';
  let saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  const prefersLight = window.matchMedia && matchMedia('(prefers-color-scheme: light)').matches;
  const apply = (theme) => {
    root.dataset.theme = theme;
    btn.setAttribute('aria-pressed', String(theme === 'light'));
    btn.setAttribute('aria-label', 'Switch to ' + (theme === 'light' ? 'dark' : 'light') + ' mode');
    label.textContent = theme === 'light' ? 'Light' : 'Dark';
  };
  apply(saved || (prefersLight ? 'light' : 'dark'));
  btn.addEventListener('click', () => {
    const next = root.dataset.theme === 'light' ? 'dark' : 'light';
    apply(next);
    try { localStorage.setItem(KEY, next); } catch (e) {}
  });
})();
```
