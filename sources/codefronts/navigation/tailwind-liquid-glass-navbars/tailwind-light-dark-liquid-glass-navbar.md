---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-light-dark-liquid-glass-navbar/"
title: "Tailwind Light / Dark Liquid Glass Navbar"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "A glass navbar that retunes its whole recipe &mdash; fill, rim, saturation, field colour &mdash; for light or dark, automatically from the OS and manually…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Light / Dark Liquid Glass Navbar
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-light-dark-liquid-glass-navbar/

A glass navbar that retunes its whole recipe &mdash; fill, rim, saturation, field colour &mdash; for light or dark, automatically from the OS and manually from a checkbox. The port makes a real architectural choice: rather than doubling every utility with a dark: twin, the bar reads four tokens and the tokens flip in two small CSS rules.
## HTML
```html
<section class="nbtw-21 grid place-items-center w-full min-h-svh p-5 font-nb21-sans" aria-label="Light and dark mode glass navbar demo">
  <div class="w-[min(720px,100%)] px-5.5 py-10 rounded-[22px] bg-[var(--nb21-stage)] transition-[background] duration-400 motion-reduce:transition-none">
    <input class="peer sr-only" type="checkbox" id="nbtw-21-toggle">
    <header class="flex flex-wrap items-center gap-x-4.5 gap-y-3 px-4 py-3.5 rounded-2xl text-[var(--nb21-fg)] bg-[var(--nb21-glass)] border border-[var(--nb21-rim)] shadow-[inset_0_1px_0_var(--nb21-rim),0_16px_38px_-22px_rgba(0,0,0,.5)] backdrop-blur-[20px] backdrop-saturate-(--nb21-sat) transition-[background-color,color,border-color] duration-400 peer-checked:[&_[data-knob]]:translate-x-[22px] peer-focus-visible:[&_label]:outline-2 peer-focus-visible:[&_label]:outline-current peer-focus-visible:[&_label]:outline-offset-2 motion-reduce:transition-none">
      <span class="text-base font-extrabold">◑ Adaptive</span>
      <nav class="flex flex-wrap gap-1 ms-auto" aria-label="Primary">
        <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-current opacity-80 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-[var(--nb21-field)] focus-visible:outline-2 focus-visible:outline-current focus-visible:outline-offset-2 aria-[current=page]:opacity-100 aria-[current=page]:bg-[var(--nb21-field)]" href="#nbtw-21" aria-current="page">Home</a>
        <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-current opacity-80 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-[var(--nb21-field)] focus-visible:outline-2 focus-visible:outline-current focus-visible:outline-offset-2" href="#nbtw-21">Notes</a>
        <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-current opacity-80 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-[var(--nb21-field)] focus-visible:outline-2 focus-visible:outline-current focus-visible:outline-offset-2" href="#nbtw-21">Files</a>
      </nav>
      <label class="flex items-center w-13 h-7.5 p-[3px] rounded-full cursor-pointer bg-[var(--nb21-field)] border border-[var(--nb21-rim)] transition-colors duration-300" for="nbtw-21-toggle" title="Toggle theme">
        <span class="size-5.5 rounded-full bg-current transition-transform duration-300 ease-nb21 motion-reduce:transition-none" data-knob aria-hidden="true"></span>
        <span class="sr-only">Toggle light / dark theme</span>
      </label>
    </header>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb21-sans: system-ui, 'Segoe UI', sans-serif;
  --ease-nb21: cubic-bezier(0.34, 1.4, 0.5, 1);
}
/* The light token set, and the reason this demo reads tokens instead of
   doubling every utility with a dark: twin. */

.nbtw-21 {
  --nb21-glass: rgba(255, 255, 255, 0.5);
  --nb21-rim: rgba(255, 255, 255, 0.8);
  --nb21-fg: #12131a;
  --nb21-field: rgba(0, 0, 0, 0.08);
  --nb21-sat: 1.7;
  --nb21-stage: linear-gradient(120deg, #dfe9f3, #ffffff);
}
/* Automatic: the OS setting repoints the same five tokens. */

@media (prefers-color-scheme: dark) {
  .nbtw-21 {
    --nb21-glass: rgba(20, 22, 34, 0.5);
    --nb21-rim: rgba(255, 255, 255, 0.4);
    --nb21-fg: #f2f3fb;
    --nb21-field: rgba(255, 255, 255, 0.1);
    --nb21-sat: 1.5;
    --nb21-stage: linear-gradient(120deg, #12141f, #242a44);
  }
}
/* Manual override, last so it wins over the media query. A checkbox read with
   :has() is the whole mechanism — no JavaScript, no flash. */

.nbtw-21:has(#nbtw-21-toggle:checked) {
  --nb21-glass: rgba(20, 22, 34, 0.5);
  --nb21-rim: rgba(255, 255, 255, 0.4);
  --nb21-fg: #f2f3fb;
  --nb21-field: rgba(255, 255, 255, 0.1);
  --nb21-sat: 1.5;
  --nb21-stage: linear-gradient(120deg, #12141f, #242a44);
}
```
