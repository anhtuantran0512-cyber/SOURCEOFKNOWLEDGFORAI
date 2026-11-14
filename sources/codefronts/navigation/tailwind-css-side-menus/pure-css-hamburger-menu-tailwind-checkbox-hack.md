---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/pure-css-hamburger-menu-tailwind-checkbox-hack/"
title: "Pure CSS Hamburger Menu in Tailwind (Checkbox Hack, No JS)"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "The checkbox hack, explained by itself: a hamburger that springs into an ✕ on an overshoot curve, a drawer, a click-outside scrim, and a live state pill that…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Hamburger Menu in Tailwind (Checkbox Hack, No JS)
Source: https://codefronts.com/navigation/tailwind-css-side-menus/pure-css-hamburger-menu-tailwind-checkbox-hack/

The checkbox hack, explained by itself: a hamburger that springs into an ✕ on an overshoot curve, a drawer, a click-outside scrim, and a live state pill that flips between “closed” and “open” so you can watch the :checked state drive the UI. The code card shows the actual Tailwind classes doing the work. 0 lines of JavaScript.
## HTML
```html
<section class="tsm-13 group relative isolate w-full min-h-svh overflow-hidden bg-tsm13-bg font-tsm13-sans text-tsm13-ink" aria-label="Pure CSS hamburger menu checkbox hack demo">
  <input type="checkbox" id="tsm-13-chk" class="peer sr-only">
  <label for="tsm-13-chk" data-tsm13-burger class="absolute top-[18px] left-[18px] z-50 grid size-11 cursor-pointer place-content-center gap-1.5 rounded-[10px] border border-tsm13-acc/20 bg-tsm13-surface transition-colors hover:bg-tsm13-acc/15 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsm13-acc2">
    <span class="sr-only">Toggle navigation menu</span>
    <span aria-hidden="true" class="block h-0.5 w-5 rounded-full bg-tsm13-ink transition-[translate,rotate,opacity,width] duration-400 ease-[cubic-bezier(0.68,-0.55,0.27,1.55)] motion-reduce:transition-none group-has-checked:translate-y-2 group-has-checked:rotate-45"></span>
    <span aria-hidden="true" class="block h-0.5 w-5 rounded-full bg-tsm13-ink transition-[translate,rotate,opacity,width] duration-400 ease-[cubic-bezier(0.68,-0.55,0.27,1.55)] motion-reduce:transition-none group-has-checked:w-0 group-has-checked:opacity-0"></span>
    <span aria-hidden="true" class="block h-0.5 w-5 rounded-full bg-tsm13-ink transition-[translate,rotate,opacity,width] duration-400 ease-[cubic-bezier(0.68,-0.55,0.27,1.55)] motion-reduce:transition-none group-has-checked:-translate-y-2 group-has-checked:-rotate-45"></span>
  </label>
  <label for="tsm-13-chk" aria-hidden="true" class="pointer-events-none absolute inset-0 z-40 bg-black/0 transition-colors duration-400 group-has-checked:pointer-events-auto group-has-checked:bg-black/50"></label>
  <nav aria-label="Main" class="invisible absolute inset-y-0 left-0 z-50 flex w-[min(270px,86vw)] -translate-x-full flex-col border-r border-tsm13-acc/15 bg-tsm13-nav pt-[78px] pb-5 transition-[translate,visibility,box-shadow] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] before:absolute before:inset-x-0 before:top-0 before:h-0.5 before:bg-linear-to-r before:from-tsm13-acc before:via-tsm13-acc2 before:to-transparent group-has-checked:visible group-has-checked:translate-x-0 group-has-checked:shadow-[8px_0_32px_oklch(0_0_0/0.5)] motion-reduce:transition-none">
    <ul class="grid flex-1 content-start gap-1 px-2.5">
      <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-sm font-semibold text-tsm13-mut transition-colors hover:bg-tsm13-acc/10 hover:text-tsm13-ink focus-visible:outline-2 focus-visible:outline-tsm13-acc2 aria-[current=page]:bg-tsm13-acc/12 aria-[current=page]:text-tsm13-acc2" aria-current="page"><span aria-hidden="true" class="size-2 shrink-0 rotate-45 rounded-[2px] bg-tsm13-mut/60 transition-colors group-hover/l:bg-tsm13-acc2 group-aria-[current=page]/l:bg-tsm13-acc group-aria-[current=page]/l:shadow-[0_0_6px_var(--color-tsm13-acc)]"></span>Dashboard</a></li>
      <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-sm font-semibold text-tsm13-mut transition-colors hover:bg-tsm13-acc/10 hover:text-tsm13-ink focus-visible:outline-2 focus-visible:outline-tsm13-acc2 aria-[current=page]:bg-tsm13-acc/12 aria-[current=page]:text-tsm13-acc2"><span aria-hidden="true" class="size-2 shrink-0 rotate-45 rounded-[2px] bg-tsm13-mut/60 transition-colors group-hover/l:bg-tsm13-acc2 group-aria-[current=page]/l:bg-tsm13-acc group-aria-[current=page]/l:shadow-[0_0_6px_var(--color-tsm13-acc)]"></span>Analytics</a></li>
      <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-sm font-semibold text-tsm13-mut transition-colors hover:bg-tsm13-acc/10 hover:text-tsm13-ink focus-visible:outline-2 focus-visible:outline-tsm13-acc2 aria-[current=page]:bg-tsm13-acc/12 aria-[current=page]:text-tsm13-acc2"><span aria-hidden="true" class="size-2 shrink-0 rotate-45 rounded-[2px] bg-tsm13-mut/60 transition-colors group-hover/l:bg-tsm13-acc2 group-aria-[current=page]/l:bg-tsm13-acc group-aria-[current=page]/l:shadow-[0_0_6px_var(--color-tsm13-acc)]"></span>Content</a></li>
      <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-sm font-semibold text-tsm13-mut transition-colors hover:bg-tsm13-acc/10 hover:text-tsm13-ink focus-visible:outline-2 focus-visible:outline-tsm13-acc2 aria-[current=page]:bg-tsm13-acc/12 aria-[current=page]:text-tsm13-acc2"><span aria-hidden="true" class="size-2 shrink-0 rotate-45 rounded-[2px] bg-tsm13-mut/60 transition-colors group-hover/l:bg-tsm13-acc2 group-aria-[current=page]/l:bg-tsm13-acc group-aria-[current=page]/l:shadow-[0_0_6px_var(--color-tsm13-acc)]"></span>Audience</a></li>
      <li aria-hidden="true" class="mx-3.5 my-2 h-px bg-tsm13-acc/15"></li>
      <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-sm font-semibold text-tsm13-mut transition-colors hover:bg-tsm13-acc/10 hover:text-tsm13-ink focus-visible:outline-2 focus-visible:outline-tsm13-acc2 aria-[current=page]:bg-tsm13-acc/12 aria-[current=page]:text-tsm13-acc2"><span aria-hidden="true" class="size-2 shrink-0 rotate-45 rounded-[2px] bg-tsm13-mut/60 transition-colors group-hover/l:bg-tsm13-acc2 group-aria-[current=page]/l:bg-tsm13-acc group-aria-[current=page]/l:shadow-[0_0_6px_var(--color-tsm13-acc)]"></span>Help</a></li>
      <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-sm font-semibold text-tsm13-mut transition-colors hover:bg-tsm13-acc/10 hover:text-tsm13-ink focus-visible:outline-2 focus-visible:outline-tsm13-acc2 aria-[current=page]:bg-tsm13-acc/12 aria-[current=page]:text-tsm13-acc2"><span aria-hidden="true" class="size-2 shrink-0 rotate-45 rounded-[2px] bg-tsm13-mut/60 transition-colors group-hover/l:bg-tsm13-acc2 group-aria-[current=page]/l:bg-tsm13-acc group-aria-[current=page]/l:shadow-[0_0_6px_var(--color-tsm13-acc)]"></span>Settings</a></li>
    </ul>
    <div class="mx-[18px] flex items-center gap-2.5 border-t border-tsm13-acc/15 pt-4">
      <span aria-hidden="true" class="grid size-8 place-items-center rounded-lg bg-linear-135 from-tsm13-acc to-red-500 text-xs font-bold">CK</span>
      <div><p class="text-[13px] font-bold">C. Kim</p><p class="text-[11px] text-tsm13-mut">Publisher</p></div>
    </div>
  </nav>
  <div class="mx-auto w-full max-w-2xl px-6 pt-[86px] pb-8">
    <div class="flex flex-wrap items-center gap-3">
      <h1 class="text-xl font-bold">Checkbox-hack menu</h1>
      <span class="inline-flex items-center gap-1.5 rounded-full border border-tsm13-acc/30 px-2.5 py-1 font-tsm13-mono text-[11px] text-tsm13-acc2"><span aria-hidden="true" class="size-1.5 rounded-full bg-tsm13-mut group-has-checked:bg-tsm13-acc"></span>:checked = <span class="group-has-checked:hidden">false</span><span class="hidden group-has-checked:inline">true</span></span>
    </div>
    <p class="mt-1.5 mb-5 max-w-prose text-[13px] leading-relaxed text-tsm13-mut text-pretty">A hidden checkbox and Tailwind’s <code>group-has-checked:</code> variant drive the whole menu. Tab to the button and press Space — it works from the keyboard too.</p>
    <pre class="mb-3.5 overflow-x-auto rounded-xl border border-tsm13-acc/15 bg-tsm13-surface px-4 py-3.5 font-tsm13-mono text-xs leading-[1.8] text-tsm13-mut"><code><span class="text-tsm13-sel">&lt;input</span> <span class="text-tsm13-acc2">class</span>=<span class="text-emerald-300">"peer sr-only"</span><span class="text-tsm13-sel">&gt;</span>
<span class="text-tsm13-sel">&lt;nav</span> <span class="text-tsm13-acc2">class</span>=<span class="text-emerald-300">"-translate-x-full
  group-has-checked:translate-x-0"</span><span class="text-tsm13-sel">&gt;</span></code></pre>
    <div class="grid grid-cols-2 gap-2.5">
      <div class="rounded-xl border border-tsm13-acc/15 bg-tsm13-surface p-3.5"><p class="text-xl font-bold text-tsm13-acc2">0</p><p class="mt-1 text-[11px] text-tsm13-mut">Lines of JavaScript</p></div>
      <div class="rounded-xl border border-tsm13-acc/15 bg-tsm13-surface p-3.5"><p class="text-xl font-bold text-tsm13-acc2">1</p><p class="mt-1 text-[11px] text-tsm13-mut">Checkbox of state</p></div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm13-bg: #111113;
  --color-tsm13-bg: oklch(0.179 0.004 286);
  --color-tsm13-surface: #1c1c1f;
  --color-tsm13-surface: oklch(0.228 0.006 285.9);
  --color-tsm13-nav: #18181b;
  --color-tsm13-nav: oklch(0.21 0.006 285.9);
  --color-tsm13-acc: #f97316;
  --color-tsm13-acc: oklch(0.705 0.187 47.6);
  --color-tsm13-acc2: #fb923c;
  --color-tsm13-acc2: oklch(0.758 0.159 55.9);
  --color-tsm13-ink: #f4f4f5;
  --color-tsm13-ink: oklch(0.967 0.001 0);
  --color-tsm13-mut: #a1a1aa;
  --color-tsm13-mut: oklch(0.712 0.013 286.1);
  --color-tsm13-sel: #60a5fa;
  --color-tsm13-sel: oklch(0.714 0.143 254.6);
  --font-tsm13-sans: 'Rubik', system-ui, sans-serif;
  --font-tsm13-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-13 {
  width: 100%;
  min-height: 100svh;
}
```
