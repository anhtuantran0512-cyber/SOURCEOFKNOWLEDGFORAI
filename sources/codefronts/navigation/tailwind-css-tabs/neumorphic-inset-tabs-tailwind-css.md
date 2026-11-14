---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/neumorphic-inset-tabs-tailwind-css/"
title: "Neumorphic Inset Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Brass legends on a slate tray; the chosen label sits in a chiselled well — a dark inset shadow on its top-left, a faint highlight on the far lip, letters…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Inset Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/neumorphic-inset-tabs-tailwind-css/

Brass legends on a slate tray; the chosen label sits in a chiselled well — a dark inset shadow on its top-left, a faint highlight on the far lip, letters with a hard engraving shadow. The port adds a small brass indicator lamp per well so the state doesn't depend on reading depth alone.
## HTML
```html
<section class="ttb-32 group/tabs grid min-h-svh w-full place-items-center bg-ttb32-bg px-5 py-14 font-ttb32-mono text-ttb32-brass" aria-label="Neumorphic inset tabs demo">
  <div class="grid w-full max-w-xl justify-items-center gap-7">
    <div class="w-full">
      <div role="radiogroup" aria-label="Process" class="flex gap-2 rounded-lg bg-ttb32-tray p-2 shadow-[inset_0_1px_0_rgb(255_255_255/0.06),0_10px_24px_-10px_rgb(0_0_0/0.6)]">
        <label class="group/tab flex min-h-14 flex-1 cursor-pointer items-center justify-center gap-2.5 rounded-md text-[12px] font-extrabold tracking-[0.22em] text-ttb32-brass-dim uppercase transition-[color,background-color,box-shadow] duration-300 hover:text-ttb32-brass has-checked:bg-ttb32-well has-checked:text-ttb32-brass has-checked:shadow-[inset_2px_2px_4px_rgb(0_0_0/0.55),inset_-1px_-1px_2px_rgb(255_255_255/0.08)] has-checked:[text-shadow:1px_1px_0_rgb(0_0_0/0.55)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb32-brass motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb32" id="ttb32-r1" checked><span aria-hidden="true" class="size-1.5 rounded-full bg-black/40 transition-[background-color,box-shadow] group-has-checked/tab:bg-ttb32-brass group-has-checked/tab:shadow-[0_0_6px_var(--color-ttb32-brass)]"></span>Etch</label>
        <label class="group/tab flex min-h-14 flex-1 cursor-pointer items-center justify-center gap-2.5 rounded-md text-[12px] font-extrabold tracking-[0.22em] text-ttb32-brass-dim uppercase transition-[color,background-color,box-shadow] duration-300 hover:text-ttb32-brass has-checked:bg-ttb32-well has-checked:text-ttb32-brass has-checked:shadow-[inset_2px_2px_4px_rgb(0_0_0/0.55),inset_-1px_-1px_2px_rgb(255_255_255/0.08)] has-checked:[text-shadow:1px_1px_0_rgb(0_0_0/0.55)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb32-brass motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb32" id="ttb32-r2"><span aria-hidden="true" class="size-1.5 rounded-full bg-black/40 transition-[background-color,box-shadow] group-has-checked/tab:bg-ttb32-brass group-has-checked/tab:shadow-[0_0_6px_var(--color-ttb32-brass)]"></span>Engrave</label>
        <label class="group/tab flex min-h-14 flex-1 cursor-pointer items-center justify-center gap-2.5 rounded-md text-[12px] font-extrabold tracking-[0.22em] text-ttb32-brass-dim uppercase transition-[color,background-color,box-shadow] duration-300 hover:text-ttb32-brass has-checked:bg-ttb32-well has-checked:text-ttb32-brass has-checked:shadow-[inset_2px_2px_4px_rgb(0_0_0/0.55),inset_-1px_-1px_2px_rgb(255_255_255/0.08)] has-checked:[text-shadow:1px_1px_0_rgb(0_0_0/0.55)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb32-brass motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb32" id="ttb32-r3"><span aria-hidden="true" class="size-1.5 rounded-full bg-black/40 transition-[background-color,box-shadow] group-has-checked/tab:bg-ttb32-brass group-has-checked/tab:shadow-[0_0_6px_var(--color-ttb32-brass)]"></span>Emboss</label>
      </div>
      <div class="pt-5 font-ttb32-serif text-[16px] text-ttb32-brass italic">
        <p class="hidden group-has-[#ttb32-r1:checked]/tabs:block">Acid bites the plate to print recessed lines.</p>
        <p class="hidden group-has-[#ttb32-r2:checked]/tabs:block">A burin cuts directly into the metal surface.</p>
        <p class="hidden group-has-[#ttb32-r3:checked]/tabs:block">Pressure raises the paper into a relief.</p>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb32-brass/20 px-3.5 py-2 text-[11.5px] text-ttb32-brass-dim">inset well · [text-shadow] engraving · brass lamp</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb32-bg: #3a3a42;
  --color-ttb32-bg: oklch(0.352 0.014 285.7);
  --color-ttb32-tray: #2a2a30;
  --color-ttb32-tray: oklch(0.287 0.011 285.7);
  --color-ttb32-well: #1f1f24;
  --color-ttb32-well: oklch(0.241 0.009 285.7);
  --color-ttb32-brass: #d4ab66;
  --color-ttb32-brass: oklch(0.764 0.100 79.4);
  --color-ttb32-brass-dim: #b3965f;
  --color-ttb32-brass-dim: oklch(0.687 0.081 82.7);
  --font-ttb32-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-ttb32-serif: 'Newsreader', Georgia, serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-32 {
  width: 100%;
  min-height: 100svh;
}
```
