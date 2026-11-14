---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-dark-mode-floating-label-light-dark/"
title: "Tailwind Dark Mode Floating Label Input with light-dark()"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "One set of tokens, two themes: every colour in @theme is a light-dark() pair, so the utilities themselves are theme-agnostic — bg-tfl11-card is white or ink…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Floating Label Input with light-dark()
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-dark-mode-floating-label-light-dark/

One set of tokens, two themes: every colour in @theme is a light-dark() pair, so the utilities themselves are theme-agnostic — bg-tfl11-card is white or ink depending on color-scheme. A role="switch" checkbox flips it with has-[#tfl-11-dark:checked]:scheme-dark on the root. No dark: variants anywhere.
## HTML
```html
<section class="tfl-11 group/root w-full min-h-svh scheme-light has-[#tfl-11-dark:checked]:scheme-dark font-tfl11-sans" aria-label="Dark mode floating label demo">
  <input type="checkbox" id="tfl-11-dark" role="switch" class="peer/switch sr-only">
  <div class="grid min-h-svh place-items-center bg-tfl11-bg px-5 py-12 transition-colors duration-300 motion-reduce:transition-none">
    <form class="flex w-full max-w-[380px] flex-col gap-5 rounded-3xl border border-tfl11-edge bg-tfl11-card p-8 shadow-[0_24px_60px_-32px_var(--color-tfl11-shadow)] transition-colors duration-300 motion-reduce:transition-none" novalidate>
      <div class="flex items-center justify-between gap-3">
        <h3 class="text-[22px] font-bold tracking-[-0.02em] text-tfl11-ink">Welcome back</h3>
        <label class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-full text-xs font-semibold text-tfl11-mut" for="tfl-11-dark">
          <span class="relative h-[22px] w-[38px] rounded-full bg-tfl11-track transition-colors duration-200 after:absolute after:top-[3px] after:left-[3px] after:size-4 after:rounded-full after:bg-white after:shadow-sm after:transition-[translate] after:duration-200 after:content-[''] group-has-[#tfl-11-dark:checked]/root:after:translate-x-4 group-has-[#tfl-11-dark:focus-visible]/root:outline-3 group-has-[#tfl-11-dark:focus-visible]/root:outline-offset-2 group-has-[#tfl-11-dark:focus-visible]/root:outline-tfl11-acc motion-reduce:after:transition-none" aria-hidden="true"></span>
          <span class="group-has-[#tfl-11-dark:checked]/root:hidden">Light</span><span class="hidden group-has-[#tfl-11-dark:checked]/root:inline">Dark</span>
          <span class="sr-only">theme</span>
        </label>
      </div>
      <div class="relative">
        <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl11-line bg-tfl11-field px-4 pt-[22px] pb-1.5 text-base text-tfl11-ink outline-hidden transition-[border-color,box-shadow,background-color] duration-200 focus:border-tfl11-acc focus:shadow-[0_0_0_4px_var(--color-tfl11-halo)] motion-reduce:transition-none" type="email" id="tfl-11-email" name="email" placeholder=" " autocomplete="email">
        <label class="pointer-events-none absolute left-4 top-1/2 origin-left -translate-y-1/2 text-base text-tfl11-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-72 peer-focus:tracking-[.04em] peer-focus:text-tfl11-acc peer-focus:[text-shadow:0_0_14px_var(--color-tfl11-glow)] peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-72 peer-[:not(:placeholder-shown)]:tracking-[.04em] peer-[:not(:placeholder-shown)]:[text-shadow:0_0_14px_var(--color-tfl11-glow)] motion-reduce:transition-none" for="tfl-11-email">Email address</label>
      </div>
      <div class="relative">
        <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl11-line bg-tfl11-field px-4 pt-[22px] pb-1.5 text-base text-tfl11-ink outline-hidden transition-[border-color,box-shadow,background-color] duration-200 focus:border-tfl11-acc focus:shadow-[0_0_0_4px_var(--color-tfl11-halo)] motion-reduce:transition-none" type="password" id="tfl-11-pass" name="password" placeholder=" " autocomplete="current-password">
        <label class="pointer-events-none absolute left-4 top-1/2 origin-left -translate-y-1/2 text-base text-tfl11-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-72 peer-focus:tracking-[.04em] peer-focus:text-tfl11-acc peer-focus:[text-shadow:0_0_14px_var(--color-tfl11-glow)] peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-72 peer-[:not(:placeholder-shown)]:tracking-[.04em] peer-[:not(:placeholder-shown)]:[text-shadow:0_0_14px_var(--color-tfl11-glow)] motion-reduce:transition-none" for="tfl-11-pass">Password</label>
      </div>
      <button class="min-h-12 cursor-pointer rounded-xl bg-tfl11-acc text-[15px] font-bold text-tfl11-on-acc transition-[filter,scale] duration-150 hover:brightness-110 active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl11-acc" type="button">Sign in</button>
    </form>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Every colour is a light-dark() pair; the hex line before each is the light-only fallback. */

@theme {
  --color-tfl11-bg: #eef0f5;
  --color-tfl11-bg: light-dark(#eef0f5, #0d1017);
  --color-tfl11-card: #ffffff;
  --color-tfl11-card: light-dark(#ffffff, #171c28);
  --color-tfl11-edge: #e3e6ee;
  --color-tfl11-edge: light-dark(#e3e6ee, #242c40);
  --color-tfl11-field: #ffffff;
  --color-tfl11-field: light-dark(#ffffff, #10141f);
  --color-tfl11-line: #c9cedb;
  --color-tfl11-line: light-dark(#c9cedb, #34405e);
  --color-tfl11-ink: #181c2a;
  --color-tfl11-ink: light-dark(#181c2a, #eef1fa);
  --color-tfl11-mut: #5f6479;
  --color-tfl11-mut: light-dark(#5f6479, #9ba3bd);
  --color-tfl11-acc: #3f46c8;
  --color-tfl11-acc: light-dark(oklch(0.5 0.19 270), oklch(0.76 0.13 270));
  --color-tfl11-on-acc: #ffffff;
  --color-tfl11-on-acc: light-dark(#ffffff, #0d1017);
  --color-tfl11-track: #b9bfd0;
  --color-tfl11-track: light-dark(#b9bfd0, oklch(0.62 0.15 270));
  --color-tfl11-halo: #3f46c82e;
  --color-tfl11-halo: light-dark(oklch(0.5 0.19 270 / 0.16), oklch(0.76 0.13 270 / 0.22));
  --color-tfl11-glow: transparent;
  --color-tfl11-glow: light-dark(transparent, oklch(0.76 0.13 270 / 0.85));
  --color-tfl11-shadow: #181c3c59;
  --color-tfl11-shadow: light-dark(oklch(0.3 0.06 270 / 0.35), oklch(0 0 0 / 0.7));
  --font-tfl11-sans: 'Sora', system-ui, sans-serif;
}

.tfl-11 {
  width: 100%;
  min-height: 100svh;
}
```
