---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-input-with-icon-and-floating-label/"
title: "Tailwind Input with Icon Inside and Floating Label"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "Search, email and username fields where the inline SVG icon never collides with the label: at rest the label sits beside the icon; on focus the icon spins…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Input with Icon Inside and Floating Label
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-input-with-icon-and-floating-label/

Search, email and username fields where the inline SVG icon never collides with the label: at rest the label sits beside the icon; on focus the icon spins out (group-focus-within:-rotate-25 group-focus-within:opacity-0) and the label slides left and up into its place with translate-x-[-30px]. One focus-within:text-tfl12-acc on the field tints icon, border and label together.
## HTML
```html
<section class="tfl-12 w-full min-h-svh grid place-items-center bg-tfl12-bg px-5 py-12 font-tfl12-sans" aria-label="Floating label with icon demo">
  <form class="flex w-full max-w-[390px] flex-col gap-5 rounded-3xl bg-white p-8 shadow-[0_24px_60px_-32px_oklch(0.3_0.08_300/0.4)] ring-1 ring-tfl12-ink/5" novalidate>
    <div class="grid gap-1">
      <h3 class="text-2xl font-bold tracking-[-0.02em] text-tfl12-ink">Find your team</h3>
      <p class="text-sm text-tfl12-mut">Search by workspace name or domain.</p>
    </div>
    <div class="group relative text-tfl12-mut focus-within:text-tfl12-acc">
      <svg class="pointer-events-none absolute left-[15px] top-1/2 -translate-y-1/2 transition-[opacity,translate,rotate] duration-[250ms] group-focus-within:translate-x-[-10px] group-focus-within:-rotate-25 group-focus-within:opacity-0 motion-reduce:transition-none" aria-hidden="true" focusable="false" viewBox="0 0 20 20" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="9" cy="9" r="6"></circle><path d="m14 14 4 4"></path></svg>
      <input class="peer h-14 w-full appearance-none rounded-xl border-[1.5px] border-tfl12-line bg-white pt-[22px] pr-4 pb-1.5 pl-[46px] text-base text-tfl12-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl12-line-hover focus:border-tfl12-acc focus:ring-4 focus:ring-tfl12-acc/15 [&::-webkit-search-cancel-button]:appearance-none" type="search" id="tfl-12-search" name="q" placeholder=" ">
      <label class="pointer-events-none absolute left-[46px] top-1/2 origin-left -translate-y-1/2 text-base text-tfl12-mut transition-[translate,scale,color] duration-200 peer-focus:translate-x-[-30px] peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-72 peer-focus:text-tfl12-acc peer-[:not(:placeholder-shown)]:translate-x-[-30px] peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-72 motion-reduce:transition-none" for="tfl-12-search">Search workspaces</label>
    </div>
    <div class="group relative text-tfl12-mut focus-within:text-tfl12-acc">
      <svg class="pointer-events-none absolute left-[15px] top-1/2 -translate-y-1/2 transition-[opacity,translate,rotate] duration-[250ms] group-focus-within:translate-x-[-10px] group-focus-within:-rotate-25 group-focus-within:opacity-0 motion-reduce:transition-none" aria-hidden="true" focusable="false" viewBox="0 0 20 20" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="16" height="12" rx="2"></rect><path d="m2.5 5.5 7.5 6 7.5-6"></path></svg>
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl12-line bg-white pt-[22px] pr-4 pb-1.5 pl-[46px] text-base text-tfl12-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl12-line-hover focus:border-tfl12-acc focus:ring-4 focus:ring-tfl12-acc/15" type="email" id="tfl-12-email" name="email" placeholder=" " autocomplete="email">
      <label class="pointer-events-none absolute left-[46px] top-1/2 origin-left -translate-y-1/2 text-base text-tfl12-mut transition-[translate,scale,color] duration-200 peer-focus:translate-x-[-30px] peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-72 peer-focus:text-tfl12-acc peer-[:not(:placeholder-shown)]:translate-x-[-30px] peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-72 motion-reduce:transition-none" for="tfl-12-email">Work email</label>
    </div>
    <div class="group relative text-tfl12-mut focus-within:text-tfl12-acc">
      <svg class="pointer-events-none absolute left-[15px] top-1/2 -translate-y-1/2 transition-[opacity,translate,rotate] duration-[250ms] group-focus-within:translate-x-[-10px] group-focus-within:-rotate-25 group-focus-within:opacity-0 motion-reduce:transition-none" aria-hidden="true" focusable="false" viewBox="0 0 20 20" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="10" cy="7" r="3.5"></circle><path d="M3.5 17c1.2-3 3.6-4.5 6.5-4.5s5.3 1.5 6.5 4.5"></path></svg>
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl12-line bg-white pt-[22px] pr-4 pb-1.5 pl-[46px] text-base text-tfl12-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl12-line-hover focus:border-tfl12-acc focus:ring-4 focus:ring-tfl12-acc/15" type="text" id="tfl-12-user" name="username" placeholder=" " autocomplete="username">
      <label class="pointer-events-none absolute left-[46px] top-1/2 origin-left -translate-y-1/2 text-base text-tfl12-mut transition-[translate,scale,color] duration-200 peer-focus:translate-x-[-30px] peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-72 peer-focus:text-tfl12-acc peer-[:not(:placeholder-shown)]:translate-x-[-30px] peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-72 motion-reduce:transition-none" for="tfl-12-user">Username</label>
    </div>
    <button class="min-h-12 cursor-pointer rounded-xl bg-tfl12-acc text-[15px] font-semibold text-white shadow-[0_10px_24px_-12px_var(--color-tfl12-acc)] transition-[filter,scale] duration-150 hover:brightness-110 active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl12-acc/50" type="button">Continue</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl12-bg: #f3f0f7;
  --color-tfl12-bg: oklch(0.96 0.01 300);
  --color-tfl12-ink: #221c30;
  --color-tfl12-ink: oklch(0.23 0.03 300);
  --color-tfl12-mut: #6c6481;
  --color-tfl12-mut: oklch(0.51 0.04 300);
  --color-tfl12-line: #ded9ea;
  --color-tfl12-line: oklch(0.89 0.02 300);
  --color-tfl12-line-hover: #bfb6d3;
  --color-tfl12-line-hover: oklch(0.79 0.035 300);
  --color-tfl12-acc: #8a3fc8;
  --color-tfl12-acc: oklch(0.52 0.19 302);
  --font-tfl12-sans: 'Outfit', system-ui, sans-serif;
}

.tfl-12 {
  width: 100%;
  min-height: 100svh;
}
```
