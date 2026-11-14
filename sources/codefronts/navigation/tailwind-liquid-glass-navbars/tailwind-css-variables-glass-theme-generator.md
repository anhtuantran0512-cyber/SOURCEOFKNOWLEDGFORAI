---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-css-variables-glass-theme-generator/"
title: "Tailwind CSS Variables Glass Theme Generator"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "The demo that draws the most important line in the whole port: @theme is compile-time."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Variables Glass Theme Generator
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-css-variables-glass-theme-generator/

The demo that draws the most important line in the whole port: @theme is compile-time. Values a user retunes at runtime &mdash; blur radius, tint alpha, hue &mdash; must stay ordinary custom properties, and utilities read them with backdrop-blur-(--nb11-blur) and bracketed color-mix(). Sliders write the variables; nothing recompiles, nothing re-renders.
## HTML
```html
<section class="nbtw-11 group relative flex flex-col items-center justify-center gap-5.5 w-full min-h-svh p-6 font-nb11-sans bg-[radial-gradient(circle_at_30%_20%,oklch(0.5_0.22_var(--nb11-hue)),#0a0a12_70%)] transition-[background] duration-400 data-[theme=light]:bg-[radial-gradient(circle_at_30%_20%,oklch(0.9_0.09_var(--nb11-hue)),#e7e7ef_70%)] motion-reduce:transition-none" id="nbtw-11-root" data-theme="dark" style="--nb11-blur:22px;--nb11-alpha:14%;--nb11-hue:265;--nb11-fg:#ffffff;--nb11-accent:oklch(0.66 0.2 265)" aria-label="CSS variables glass theme generator demo">
  <header class="flex flex-wrap items-center gap-x-4.5 gap-y-3 w-[min(720px,100%)] px-4 py-3.5 rounded-[18px] text-[var(--nb11-fg)] bg-[color-mix(in_oklab,var(--nb11-fg)_var(--nb11-alpha),transparent)] border border-[color-mix(in_oklab,var(--nb11-fg)_30%,transparent)] shadow-[inset_0_1px_0_color-mix(in_oklab,var(--nb11-fg)_45%,transparent),0_18px_40px_-22px_rgba(0,0,0,.6)] backdrop-blur-(--nb11-blur) backdrop-saturate-[1.8] transition-[background-color,backdrop-filter] duration-300 group-data-[theme=light]:text-[#101018] motion-reduce:transition-none">
    <span class="text-base font-extrabold">◈ Themer</span>
    <nav class="flex flex-wrap gap-1 ms-auto" aria-label="Primary">
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-current opacity-[0.82] text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 focus-visible:outline-2 focus-visible:outline-[var(--nb11-accent)] focus-visible:outline-offset-2 aria-[current=page]:opacity-100 aria-[current=page]:bg-[color-mix(in_oklab,currentColor_18%,transparent)]" href="#nbtw-11" aria-current="page">Home</a>
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-current opacity-[0.82] text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 focus-visible:outline-2 focus-visible:outline-[var(--nb11-accent)] focus-visible:outline-offset-2" href="#nbtw-11">Tokens</a>
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-current opacity-[0.82] text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 focus-visible:outline-2 focus-visible:outline-[var(--nb11-accent)] focus-visible:outline-offset-2" href="#nbtw-11">Export</a>
    </nav>
    <button class="min-h-10 px-4.5 rounded-[10px] border-0 bg-[var(--nb11-accent)] text-white text-sm font-bold cursor-pointer focus-visible:outline-2 focus-visible:outline-[var(--nb11-accent)] focus-visible:outline-offset-2" type="button">Save</button>
  </header>
  <form class="flex flex-wrap items-center gap-x-5.5 gap-y-3.5 w-[min(720px,100%)] p-4 rounded-2xl text-[var(--nb11-fg)] bg-[color-mix(in_oklab,var(--nb11-fg)_8%,transparent)] border border-[color-mix(in_oklab,var(--nb11-fg)_20%,transparent)] backdrop-blur-[12px] group-data-[theme=light]:text-[#101018]" aria-label="Theme controls">
    <label class="flex flex-col gap-1.5 text-xs font-semibold">Blur<input class="accent-[var(--nb11-accent)]" type="range" id="nbtw-11-blur" min="4" max="40" value="22"></label>
    <label class="flex flex-col gap-1.5 text-xs font-semibold">Tint alpha<input class="accent-[var(--nb11-accent)]" type="range" id="nbtw-11-alpha" min="4" max="40" value="14"></label>
    <label class="flex flex-col gap-1.5 text-xs font-semibold">Hue<input class="accent-[var(--nb11-accent)]" type="range" id="nbtw-11-hue" min="0" max="360" value="265"></label>
    <fieldset class="flex items-center gap-3.5 border-0 text-[13px]">
      <legend class="float-none mr-1 text-xs font-bold">Mode</legend>
      <label class="flex items-center gap-1.5 cursor-pointer"><input class="accent-[var(--nb11-accent)]" type="radio" name="nbtw-11-mode" value="dark" checked> Dark</label>
      <label class="flex items-center gap-1.5 cursor-pointer"><input class="accent-[var(--nb11-accent)]" type="radio" name="nbtw-11-mode" value="light"> Light</label>
    </fieldset>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb11-sans: system-ui, 'Segoe UI', sans-serif;
}
/* Registered so the browser can interpolate them while a slider is dragged.
   An unregistered custom property is an untyped string: it still resolves,
   but nothing tweens and the drag feels stepped. */

@property --nb11-hue {
  syntax: '<number>';
  inherits: true;
  initial-value: 265;
}

@property --nb11-alpha {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 14%;
}
/* The light token set. These are runtime values, so they cannot live in
   @theme — a slider has to be able to rewrite them. */

.nbtw-11[data-theme="light"] {
  --nb11-fg: #101018;
  --nb11-accent: oklch(0.55 0.2 var(--nb11-hue));
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#nbtw-11-root');
  if (!root) return;
  const set = (k, v) => root.style.setProperty(k, v);
  root.querySelector('#nbtw-11-blur').addEventListener('input', (e) => set('--nb11-blur', e.target.value + 'px'));
  root.querySelector('#nbtw-11-alpha').addEventListener('input', (e) => set('--nb11-alpha', e.target.value + '%'));
  root.querySelector('#nbtw-11-hue').addEventListener('input', (e) => {
    set('--nb11-hue', e.target.value);
    set('--nb11-accent', 'oklch(0.66 0.2 ' + e.target.value + ')');
  });
  root.querySelectorAll('input[name="nbtw-11-mode"]').forEach((r) =>
    r.addEventListener('change', (e) => { root.dataset.theme = e.target.value; }));
})();
```
