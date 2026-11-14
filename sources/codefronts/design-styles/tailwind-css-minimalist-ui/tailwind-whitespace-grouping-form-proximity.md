---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-whitespace-grouping-form-proximity/"
title: "Tailwind Whitespace That Groups Instead of Separates"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "Two identical checkout forms."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Whitespace That Groups Instead of Separates
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-whitespace-grouping-form-proximity/

Two identical checkout forms. The left one uses gap-4 everywhere, so label, field and next section are all equally far apart and nothing groups. The right one uses gap-1.5 inside a field, gap-2 inside a fieldset and gap-8 between fieldsets &mdash; a 1:4 ratio that makes the structure legible with no rules, boxes or colour.
## HTML
```html
<section class="tmu-06 relative w-full min-h-svh bg-tmu06-bg font-tmu06-ui text-tmu06-ink antialiased" aria-labelledby="tmu06-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu06-theme" type="checkbox" class="peer sr-only">
    <label for="tmu06-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu06-line bg-tmu06-surface text-tmu06-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu06-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu06-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[72rem] gap-12 px-6 pt-20 pb-20 md:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu06-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu06-ink-2"><span class="tabular-nums text-tmu06-acc">06</span><span aria-hidden="true" class="h-px w-6 bg-tmu06-line"></span>Proximity</p>
      <h2 id="tmu06-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">Space that groups, not space that separates</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu06-ink-2 text-pretty">Same fields, same order. Equal spacing makes everything a neighbour; unequal spacing tells you which label owns which field.</p>
    </header>
    <div class="grid gap-6 md:grid-cols-2">
      <article aria-labelledby="tmu06-a" class="relative grid min-w-0 content-start gap-6 overflow-hidden rounded-xl bg-tmu06-surface p-6 md:p-8">
        <header class="grid min-w-0 gap-0.5">
          <h3 id="tmu06-a" class="text-[0.8125rem] font-bold uppercase tracking-[0.1em]">Equal spacing</h3>
          <p class="font-tmu06-mono text-xs tabular-nums text-tmu06-ink-2">16px everywhere &middot; ratio 1:1</p>
        </header>
        <div class="grid min-w-0 gap-4">
          <fieldset class="grid min-w-0 gap-4">
            <legend class="mb-1 text-xs font-bold uppercase tracking-[0.08em] text-tmu06-ink-2">Billing contact</legend>
            <div class="grid min-w-0 gap-4">
              <label for="tmu06-a-name" class="text-sm font-medium">Full name</label>
              <input id="tmu06-a-name" type="text" autocomplete="name" value="Sam Rivera" class="min-h-11 w-full min-w-0 rounded-md border border-tmu06-line bg-tmu06-field px-3 text-[0.9375rem] text-tmu06-ink shadow-[inset_0_1px_1px_rgb(0_0_0/0.06)] transition-[border-color] duration-150 hover:border-tmu06-ink-2 focus-visible:border-tmu06-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu06-acc motion-reduce:transition-none">
            </div>
            <div class="grid min-w-0 gap-4">
              <label for="tmu06-a-mail" class="text-sm font-medium">Work email</label>
              <input id="tmu06-a-mail" type="email" autocomplete="email" value="[email protected]" class="min-h-11 w-full min-w-0 rounded-md border border-tmu06-line bg-tmu06-field px-3 text-[0.9375rem] text-tmu06-ink shadow-[inset_0_1px_1px_rgb(0_0_0/0.06)] transition-[border-color] duration-150 hover:border-tmu06-ink-2 focus-visible:border-tmu06-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu06-acc motion-reduce:transition-none">
            </div>
          </fieldset>
          <fieldset class="grid min-w-0 gap-4">
            <legend class="mb-1 text-xs font-bold uppercase tracking-[0.08em] text-tmu06-ink-2">Card</legend>
            <div class="grid min-w-0 gap-4">
              <label for="tmu06-a-card" class="text-sm font-medium">Card number</label>
              <input id="tmu06-a-card" type="text" inputmode="numeric" value="4242 4242 4242 4242" class="min-h-11 w-full min-w-0 rounded-md border border-tmu06-line bg-tmu06-field px-3 text-[0.9375rem] text-tmu06-ink shadow-[inset_0_1px_1px_rgb(0_0_0/0.06)] transition-[border-color] duration-150 hover:border-tmu06-ink-2 focus-visible:border-tmu06-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu06-acc motion-reduce:transition-none">
            </div>
            <div class="grid min-w-0 gap-4">
              <label for="tmu06-a-exp" class="text-sm font-medium">Expiry</label>
              <input id="tmu06-a-exp" type="text" inputmode="numeric" value="09 / 29" class="min-h-11 w-full min-w-0 rounded-md border border-tmu06-line bg-tmu06-field px-3 text-[0.9375rem] text-tmu06-ink shadow-[inset_0_1px_1px_rgb(0_0_0/0.06)] transition-[border-color] duration-150 hover:border-tmu06-ink-2 focus-visible:border-tmu06-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu06-acc motion-reduce:transition-none">
            </div>
          </fieldset>
        </div>
      </article>
      <article aria-labelledby="tmu06-b" class="relative grid min-w-0 content-start gap-6 overflow-hidden rounded-xl bg-tmu06-surface p-6 md:p-8 before:absolute before:inset-y-0 before:left-0 before:w-[3px] before:bg-tmu06-acc">
        <header class="grid min-w-0 gap-0.5">
          <h3 id="tmu06-b" class="text-[0.8125rem] font-bold uppercase tracking-[0.1em]">Proximity applied</h3>
          <p class="font-tmu06-mono text-xs tabular-nums text-tmu06-ink-2">6px &middot; 8px &middot; 32px &middot; ratio 1:4</p>
        </header>
        <div class="grid min-w-0 gap-8">
          <fieldset class="grid min-w-0 gap-2">
            <legend class="mb-1 text-xs font-bold uppercase tracking-[0.08em] text-tmu06-ink-2">Billing contact</legend>
            <div class="grid min-w-0 gap-1.5">
              <label for="tmu06-b-name" class="text-sm font-medium">Full name</label>
              <input id="tmu06-b-name" type="text" autocomplete="name" value="Sam Rivera" class="min-h-11 w-full min-w-0 rounded-md border border-tmu06-line bg-tmu06-field px-3 text-[0.9375rem] text-tmu06-ink shadow-[inset_0_1px_1px_rgb(0_0_0/0.06)] transition-[border-color] duration-150 hover:border-tmu06-ink-2 focus-visible:border-tmu06-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu06-acc motion-reduce:transition-none">
            </div>
            <div class="grid min-w-0 gap-1.5">
              <label for="tmu06-b-mail" class="text-sm font-medium">Work email</label>
              <input id="tmu06-b-mail" type="email" autocomplete="email" value="[email protected]" class="min-h-11 w-full min-w-0 rounded-md border border-tmu06-line bg-tmu06-field px-3 text-[0.9375rem] text-tmu06-ink shadow-[inset_0_1px_1px_rgb(0_0_0/0.06)] transition-[border-color] duration-150 hover:border-tmu06-ink-2 focus-visible:border-tmu06-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu06-acc motion-reduce:transition-none">
            </div>
          </fieldset>
          <fieldset class="grid min-w-0 gap-2">
            <legend class="mb-1 text-xs font-bold uppercase tracking-[0.08em] text-tmu06-ink-2">Card</legend>
            <div class="grid min-w-0 gap-1.5">
              <label for="tmu06-b-card" class="text-sm font-medium">Card number</label>
              <input id="tmu06-b-card" type="text" inputmode="numeric" value="4242 4242 4242 4242" class="min-h-11 w-full min-w-0 rounded-md border border-tmu06-line bg-tmu06-field px-3 text-[0.9375rem] text-tmu06-ink shadow-[inset_0_1px_1px_rgb(0_0_0/0.06)] transition-[border-color] duration-150 hover:border-tmu06-ink-2 focus-visible:border-tmu06-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu06-acc motion-reduce:transition-none">
            </div>
            <div class="grid min-w-0 gap-1.5">
              <label for="tmu06-b-exp" class="text-sm font-medium">Expiry</label>
              <input id="tmu06-b-exp" type="text" inputmode="numeric" value="09 / 29" class="min-h-11 w-full min-w-0 rounded-md border border-tmu06-line bg-tmu06-field px-3 text-[0.9375rem] text-tmu06-ink shadow-[inset_0_1px_1px_rgb(0_0_0/0.06)] transition-[border-color] duration-150 hover:border-tmu06-ink-2 focus-visible:border-tmu06-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu06-acc motion-reduce:transition-none">
            </div>
          </fieldset>
          <button type="button" class="inline-flex min-h-11 min-w-11 items-center justify-self-start rounded-md border border-tmu06-acc bg-tmu06-acc px-5 text-[0.9375rem] font-semibold text-tmu06-acc-ink cursor-pointer transition-[filter,translate] duration-150 hover:brightness-110 active:translate-y-px focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu06-ink motion-reduce:transition-none">Continue to payment</button>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu06-bg: light-dark(#f6f4f1, #1c1a18);
  --color-tmu06-bg: light-dark(oklch(96.5% 0.006 70), oklch(23% 0.008 60));
  --color-tmu06-surface: light-dark(#ffffff, #262320);
  --color-tmu06-surface: light-dark(oklch(100% 0 0), oklch(27.5% 0.009 60));
  --color-tmu06-field: light-dark(#ffffff, #322e2a);
  --color-tmu06-field: light-dark(oklch(100% 0 0), oklch(32% 0.01 60));
  --color-tmu06-ink: light-dark(#1c1a18, #f6f3f0);
  --color-tmu06-ink: light-dark(oklch(23% 0.008 60), oklch(96.5% 0.006 70));
  --color-tmu06-ink-2: light-dark(#55504a, #b6afa7);
  --color-tmu06-ink-2: light-dark(oklch(45% 0.012 65), oklch(77% 0.012 70));
  --color-tmu06-line: light-dark(#d5cfc7, #45403a);
  --color-tmu06-line: light-dark(oklch(85.5% 0.012 70), oklch(37% 0.011 65));
  --color-tmu06-acc: light-dark(#8a4a06, #f0a35c);
  --color-tmu06-acc: light-dark(oklch(45% 0.12 58), oklch(78% 0.13 62));
  --color-tmu06-acc-ink: light-dark(#ffffff, #201408);
  --color-tmu06-acc-ink: light-dark(oklch(100% 0 0), oklch(18% 0.03 60));
  --font-tmu06-ui: "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif;
  --font-tmu06-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-06:has(#tmu06-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-06:has(#tmu06-theme:checked) {
    color-scheme: light;
  }
}
```
