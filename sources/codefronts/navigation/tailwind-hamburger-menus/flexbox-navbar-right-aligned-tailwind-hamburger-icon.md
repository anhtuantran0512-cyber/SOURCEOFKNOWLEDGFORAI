---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/flexbox-navbar-right-aligned-tailwind-hamburger-icon/"
title: "Flexbox Navbar Right-Aligned Tailwind Hamburger Icon"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The layout lesson behind every navbar, taught on the navbar itself &mdash; flip the X-ray switch and the bar reveals its own construction with dashed…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flexbox Navbar Right-Aligned Tailwind Hamburger Icon
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/flexbox-navbar-right-aligned-tailwind-hamburger-icon/

The layout lesson behind every navbar, taught on the navbar itself &mdash; flip the X-ray switch and the bar reveals its own construction with dashed outlines and callouts pinned to the three declarations doing all the work. In Tailwind the answer to &ldquo;how do I push the hamburger right?&rdquo; is two characters shorter and RTL-correct by default: ms-auto.
## HTML
```html
<section class="thb-23 w-full min-h-svh bg-thb23-bg font-thb23-sans text-thb23-ink px-5 py-9" aria-label="Flexbox navbar anatomy demo">
  <div class="group grid gap-2 p-6 rounded-[18px] border border-thb23-edge bg-thb23-bg">
    <div class="flex justify-end">
      <label for="thb23-x" class="flex items-center gap-2.5 min-h-11 px-1 text-[13px] font-bold cursor-pointer select-none">
        <input type="checkbox" id="thb23-x" class="peer absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">
        <i class="relative flex-none w-10 h-[23px] rounded-full bg-thb23-track transition-[background] duration-250 after:content-[''] after:absolute after:top-[2.5px] after:left-[2.5px] after:w-4.5 after:h-4.5 after:rounded-full after:bg-white after:shadow-[0_2px_5px_oklch(0.3_0.02_255/0.35)] after:transition-[translate] after:duration-250 group-has-checked:bg-thb23-blue group-has-checked:after:translate-x-[17px] peer-focus-visible:outline-2 peer-focus-visible:outline-thb23-blue peer-focus-visible:outline-offset-2" aria-hidden="true"></i>
        X-ray the layout
      </label>
    </div>
    <div class="relative px-2 pt-14 pb-10">
      <header class="relative flex items-center gap-6 min-h-15 px-5 rounded-[14px] bg-thb23-panel border border-thb23-edge shadow-[0_14px_34px_-26px_oklch(0.3_0.04_255/0.6)] outline-2 outline-dashed outline-offset-[5px] outline-transparent transition-[outline-color] duration-250 group-has-checked:outline-thb23-blue">
        <span class="flex items-center gap-2.25 text-[15px] font-extrabold">
          <i class="w-4.75 h-4.75 rounded-md bg-[conic-gradient(from_210deg,var(--color-thb23-blue),var(--color-thb23-violet))]" aria-hidden="true"></i>Framework
        </span>
        <nav aria-label="Primary" class="flex gap-1 rounded-lg outline-2 outline-dashed outline-offset-[3px] outline-transparent transition-[outline-color] duration-250 group-has-checked:outline-thb23-violet">
          <a href="#docs" class="px-3 py-2.25 rounded-lg text-[13.5px] font-semibold text-thb23-mut no-underline transition-[color,background] duration-150 hover:text-thb23-ink hover:bg-thb23-hover focus-visible:outline-2 focus-visible:outline-thb23-blue focus-visible:outline-offset-2">Docs</a>
          <a href="#examples" class="px-3 py-2.25 rounded-lg text-[13.5px] font-semibold text-thb23-mut no-underline transition-[color,background] duration-150 hover:text-thb23-ink hover:bg-thb23-hover focus-visible:outline-2 focus-visible:outline-thb23-blue focus-visible:outline-offset-2">Examples</a>
        </nav>
        <button type="button" aria-label="Open menu (demo)" class="ms-auto grid place-items-center w-11.5 h-11.5 rounded-[11px] border border-thb23-edge bg-thb23-panel text-thb23-ink cursor-pointer outline-2 outline-dashed outline-offset-[3px] outline-transparent transition-[background,outline-color] duration-250 hover:bg-thb23-hover group-has-checked:outline-thb23-amber focus-visible:outline-solid focus-visible:outline-thb23-blue focus-visible:outline-offset-2">
          <span class="relative block w-4.5 h-3" aria-hidden="true">
            <i class="absolute left-0 top-0 w-4.5 h-0.5 rounded-sm bg-current"></i>
            <i class="absolute left-0 top-[5px] w-4.5 h-0.5 rounded-sm bg-current"></i>
            <i class="absolute left-0 top-2.5 w-4.5 h-0.5 rounded-sm bg-current"></i>
          </span>
        </button>
        <span class="absolute -top-11 left-0 px-2.5 py-1.25 rounded-[7px] bg-thb23-blue text-white text-[11px] font-bold whitespace-nowrap opacity-0 translate-y-1.5 pointer-events-none transition-[opacity,translate] duration-300 ease-thb23 group-has-checked:opacity-100 group-has-checked:translate-y-0 after:content-[''] after:absolute after:top-full after:left-4.5 after:border-5 after:border-transparent after:border-t-thb23-blue"><code class="font-thb23-mono text-[10.5px] font-bold">display:flex &middot; align-items:center &middot; gap:24px</code></span>
        <span class="absolute -bottom-8.5 right-0 px-2.5 py-1.25 rounded-[7px] bg-thb23-amber text-white text-[11px] font-bold whitespace-nowrap opacity-0 translate-y-1.5 pointer-events-none transition-[opacity,translate] duration-300 ease-thb23 delay-[80ms] group-has-checked:opacity-100 group-has-checked:translate-y-0 after:content-[''] after:absolute after:bottom-full after:right-5 after:border-5 after:border-transparent after:border-b-thb23-amber"><code class="font-thb23-mono text-[10.5px] font-bold">ms-auto</code> &larr; pushes right</span>
        <span class="absolute -top-11 left-[44%] px-2.5 py-1.25 rounded-[7px] bg-thb23-violet text-white text-[11px] font-bold whitespace-nowrap opacity-0 translate-y-1.5 pointer-events-none transition-[opacity,translate] duration-300 ease-thb23 delay-[160ms] group-has-checked:opacity-100 group-has-checked:translate-y-0 after:content-[''] after:absolute after:top-full after:left-3.5 after:border-5 after:border-transparent after:border-t-thb23-violet"><code class="font-thb23-mono text-[10.5px] font-bold">gap</code></span>
      </header>
      <div class="absolute inset-x-2 bottom-2 flex items-center gap-2 font-thb23-mono text-[10px] font-bold tracking-[0.08em] text-thb23-blue opacity-0 transition-[opacity] duration-300 delay-200 group-has-checked:opacity-80" aria-hidden="true">
        <i class="flex-1 h-0.5 [background:repeating-linear-gradient(90deg,var(--color-thb23-blue)_0_8px,transparent_8px_14px)]"></i>main axis &rarr;
      </div>
    </div>
    <p class="text-center text-xs text-thb23-mut text-pretty" aria-hidden="true">the bar stays fully functional under the annotations &mdash; inspect a live specimen</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb23-bg: #fafafc;
  --color-thb23-bg: oklch(0.975 0.004 250);
  --color-thb23-panel: #ffffff;
  --color-thb23-panel: oklch(1 0 0);
  --color-thb23-hover: #f2f3f8;
  --color-thb23-hover: oklch(0.96 0.006 250);
  --color-thb23-edge: #e2e3ea;
  --color-thb23-edge: oklch(0.89 0.009 250);
  --color-thb23-track: #dcdde4;
  --color-thb23-track: oklch(0.88 0.01 250);
  --color-thb23-ink: #32354a;
  --color-thb23-ink: oklch(0.24 0.018 255);
  --color-thb23-mut: #70738a;
  --color-thb23-mut: oklch(0.53 0.014 255);
  --color-thb23-blue: #3f5fd9;
  --color-thb23-blue: oklch(0.55 0.18 255);
  --color-thb23-amber: #d09a3a;
  --color-thb23-amber: oklch(0.68 0.15 70);
  --color-thb23-violet: #8b3fd6;
  --color-thb23-violet: oklch(0.55 0.19 300);
  --font-thb23-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb23-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb23: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-23 {
  width: 100%;
  min-height: 100svh;
}
```
