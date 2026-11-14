---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/neumorphic-tailwind-hamburger-toggle-button/"
title: "Neumorphic Tailwind Hamburger Toggle Button"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "Soft-UI physics done by the rules: the burger is a clay button raised by the canonical dual shadow, and pressing it does not move it &mdash; it inverts the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Tailwind Hamburger Toggle Button
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/neumorphic-tailwind-hamburger-toggle-button/

Soft-UI physics done by the rules: the burger is a clay button raised by the canonical dual shadow, and pressing it does not move it &mdash; it inverts the shadows to inset, so the button sinks INTO the surface. In utilities both shadow states sit in one class list, which makes the light-source discipline that neumorphism lives by impossible to get wrong by accident.
## HTML
```html
<section class="thb-26 w-full min-h-svh bg-thb26-clay font-thb26-sans text-thb26-ink px-5 py-9" aria-label="Neumorphic hamburger toggle demo">
  <div class="group relative min-h-120 flex flex-col items-center gap-6.5 px-7 py-8.5 rounded-[22px] bg-thb26-clay border border-thb26-edge">
    <input type="checkbox" id="thb26-t" class="peer absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">
    <div class="flex flex-col items-center gap-3.5">
      <label for="thb26-t" class="grid place-items-center w-18.5 h-18.5 rounded-[22px] bg-thb26-clay cursor-pointer select-none shadow-[-7px_-7px_14px_var(--color-thb26-lite),7px_7px_14px_var(--color-thb26-shade)] transition-[box-shadow] duration-300 hover:shadow-[-9px_-9px_18px_var(--color-thb26-lite),9px_9px_18px_var(--color-thb26-shade)] peer-focus-visible:outline-3 peer-focus-visible:outline-thb26-acc peer-focus-visible:outline-offset-3 group-has-checked:shadow-[inset_-5px_-5px_10px_var(--color-thb26-lite),inset_5px_5px_10px_var(--color-thb26-shade)]">
        <span class="relative block w-6 h-4" aria-hidden="true">
          <i class="absolute left-0 top-0 w-6 h-[2.6px] rounded-[3px] bg-thb26-ink transition-[translate,rotate,background] duration-300 ease-thb26 group-has-checked:translate-y-[6.7px] group-has-checked:rotate-45 group-has-checked:bg-thb26-acc motion-reduce:transition-none"></i>
          <i class="absolute left-0 top-[6.7px] w-6 h-[2.6px] rounded-[3px] bg-thb26-ink transition-[opacity,scale,background] duration-250 ease-thb26 group-has-checked:opacity-0 group-has-checked:scale-x-40 group-has-checked:bg-thb26-acc motion-reduce:transition-none"></i>
          <i class="absolute left-0 top-[13.4px] w-6 h-[2.6px] rounded-[3px] bg-thb26-ink transition-[translate,rotate,background] duration-300 ease-thb26 group-has-checked:-translate-y-[6.7px] group-has-checked:-rotate-45 group-has-checked:bg-thb26-acc motion-reduce:transition-none"></i>
        </span>
      </label>
      <span class="relative block h-4 overflow-hidden font-thb26-mono text-[11px] tracking-[0.22em] uppercase text-thb26-mut" aria-hidden="true">
        <b class="block h-4 leading-4 font-bold transition-[translate] duration-350 ease-thb26 group-has-checked:-translate-y-4">rest</b>
        <b class="block h-4 leading-4 font-bold transition-[translate] duration-350 ease-thb26 group-has-checked:-translate-y-4">pressed</b>
      </span>
    </div>
    <nav aria-label="Menu" class="grid gap-3.5 w-[min(280px,100%)] p-1.5">
      <a href="#home" style="--i:0" class="group/p flex items-center gap-3.25 min-h-13 px-5 rounded-2xl bg-thb26-clay text-thb26-ink text-sm font-bold no-underline shadow-[-6px_-6px_12px_var(--color-thb26-lite),6px_6px_12px_var(--color-thb26-shade)] opacity-0 translate-y-3 pointer-events-none transition-[box-shadow,opacity,translate,color] duration-350 ease-thb26 hover:text-thb26-acc focus-visible:outline-3 focus-visible:outline-thb26-acc focus-visible:outline-offset-2 active:shadow-[inset_-4px_-4px_8px_var(--color-thb26-lite),inset_4px_4px_8px_var(--color-thb26-shade)] group-has-checked:opacity-100 group-has-checked:translate-y-0 group-has-checked:pointer-events-auto group-has-checked:[transition-delay:calc(80ms+var(--i)*50ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">
        <i class="w-2 h-2 rounded-full bg-thb26-clay shadow-[inset_-2px_-2px_4px_var(--color-thb26-lite),inset_2px_2px_4px_var(--color-thb26-shade)] transition-[background,box-shadow] duration-200 group-hover/p:bg-thb26-acc group-hover/p:shadow-none group-focus-visible/p:bg-thb26-acc group-focus-visible/p:shadow-none" aria-hidden="true"></i>Home
      </a>
      <a href="#library" style="--i:1" class="group/p flex items-center gap-3.25 min-h-13 px-5 rounded-2xl bg-thb26-clay text-thb26-ink text-sm font-bold no-underline shadow-[-6px_-6px_12px_var(--color-thb26-lite),6px_6px_12px_var(--color-thb26-shade)] opacity-0 translate-y-3 pointer-events-none transition-[box-shadow,opacity,translate,color] duration-350 ease-thb26 hover:text-thb26-acc focus-visible:outline-3 focus-visible:outline-thb26-acc focus-visible:outline-offset-2 active:shadow-[inset_-4px_-4px_8px_var(--color-thb26-lite),inset_4px_4px_8px_var(--color-thb26-shade)] group-has-checked:opacity-100 group-has-checked:translate-y-0 group-has-checked:pointer-events-auto group-has-checked:[transition-delay:calc(80ms+var(--i)*50ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">
        <i class="w-2 h-2 rounded-full bg-thb26-clay shadow-[inset_-2px_-2px_4px_var(--color-thb26-lite),inset_2px_2px_4px_var(--color-thb26-shade)] transition-[background,box-shadow] duration-200 group-hover/p:bg-thb26-acc group-hover/p:shadow-none group-focus-visible/p:bg-thb26-acc group-focus-visible/p:shadow-none" aria-hidden="true"></i>Library
      </a>
      <a href="#stats" style="--i:2" class="group/p flex items-center gap-3.25 min-h-13 px-5 rounded-2xl bg-thb26-clay text-thb26-ink text-sm font-bold no-underline shadow-[-6px_-6px_12px_var(--color-thb26-lite),6px_6px_12px_var(--color-thb26-shade)] opacity-0 translate-y-3 pointer-events-none transition-[box-shadow,opacity,translate,color] duration-350 ease-thb26 hover:text-thb26-acc focus-visible:outline-3 focus-visible:outline-thb26-acc focus-visible:outline-offset-2 active:shadow-[inset_-4px_-4px_8px_var(--color-thb26-lite),inset_4px_4px_8px_var(--color-thb26-shade)] group-has-checked:opacity-100 group-has-checked:translate-y-0 group-has-checked:pointer-events-auto group-has-checked:[transition-delay:calc(80ms+var(--i)*50ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">
        <i class="w-2 h-2 rounded-full bg-thb26-clay shadow-[inset_-2px_-2px_4px_var(--color-thb26-lite),inset_2px_2px_4px_var(--color-thb26-shade)] transition-[background,box-shadow] duration-200 group-hover/p:bg-thb26-acc group-hover/p:shadow-none group-focus-visible/p:bg-thb26-acc group-focus-visible/p:shadow-none" aria-hidden="true"></i>Statistics
      </a>
      <a href="#settings" style="--i:3" class="group/p flex items-center gap-3.25 min-h-13 px-5 rounded-2xl bg-thb26-clay text-thb26-ink text-sm font-bold no-underline shadow-[-6px_-6px_12px_var(--color-thb26-lite),6px_6px_12px_var(--color-thb26-shade)] opacity-0 translate-y-3 pointer-events-none transition-[box-shadow,opacity,translate,color] duration-350 ease-thb26 hover:text-thb26-acc focus-visible:outline-3 focus-visible:outline-thb26-acc focus-visible:outline-offset-2 active:shadow-[inset_-4px_-4px_8px_var(--color-thb26-lite),inset_4px_4px_8px_var(--color-thb26-shade)] group-has-checked:opacity-100 group-has-checked:translate-y-0 group-has-checked:pointer-events-auto group-has-checked:[transition-delay:calc(80ms+var(--i)*50ms)] motion-reduce:translate-y-0 motion-reduce:duration-150">
        <i class="w-2 h-2 rounded-full bg-thb26-clay shadow-[inset_-2px_-2px_4px_var(--color-thb26-lite),inset_2px_2px_4px_var(--color-thb26-shade)] transition-[background,box-shadow] duration-200 group-hover/p:bg-thb26-acc group-hover/p:shadow-none group-focus-visible/p:bg-thb26-acc group-focus-visible/p:shadow-none" aria-hidden="true"></i>Settings
      </a>
    </nav>
    <p class="mt-auto max-w-[34ch] text-center text-xs leading-relaxed text-thb26-mut text-pretty" aria-hidden="true">same clay, two shadows &mdash; pressed = the pair goes <code class="font-thb26-mono text-[11px] px-1.5 py-0.5 rounded bg-thb26-code">inset</code>. Note the focus ring stays loud on purpose.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb26-clay: #e6e8ef;
  --color-thb26-clay: oklch(0.92 0.012 260);
  --color-thb26-lite: #fbfcff;
  --color-thb26-lite: oklch(0.99 0.005 260);
  --color-thb26-shade: #bcc0cd;
  --color-thb26-shade: oklch(0.78 0.02 260);
  --color-thb26-edge: #d5d8e2;
  --color-thb26-edge: oklch(0.87 0.014 260);
  --color-thb26-code: #d9dce6;
  --color-thb26-code: oklch(0.88 0.014 260);
  --color-thb26-ink: #454a5c;
  --color-thb26-ink: oklch(0.32 0.02 262);
  --color-thb26-mut: #6f7488;
  --color-thb26-mut: oklch(0.52 0.018 262);
  --color-thb26-acc: #3fa8b4;
  --color-thb26-acc: oklch(0.65 0.11 190);
  --font-thb26-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb26-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb26: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-26 {
  width: 100%;
  min-height: 100svh;
}
```
