---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-appearance-settings-page/"
title: "Tailwind Appearance Settings Page"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A live appearance panel with zero JavaScript: pick Light, Dark or System from mini window previews and the whole page re-themes through light-dark(); choose…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Appearance Settings Page
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-appearance-settings-page/

A live appearance panel with zero JavaScript: pick Light, Dark or System from mini window previews and the whole page re-themes through light-dark(); choose an accent, density, text size and high-contrast borders, and a live preview of the app updates beside the controls as you click.
## HTML
```html
<section class="tsp-14 w-full min-h-svh bg-tsp14-bg px-4 py-10 font-tsp14-sans text-tsp14-ink antialiased transition-colors duration-300 [color-scheme:light_dark] has-[#tsp-14-light:checked]:[color-scheme:light] has-[#tsp-14-dark:checked]:[color-scheme:dark] has-[#tsp-14-a-indigo:checked]:[--tsp14-acc:#6366f1] has-[#tsp-14-a-teal:checked]:[--tsp14-acc:#0d9488] has-[#tsp-14-a-rose:checked]:[--tsp14-acc:#e11d48] has-[#tsp-14-a-amber:checked]:[--tsp14-acc:#d97706] has-[#tsp-14-a-ink:checked]:[--tsp14-acc:light-dark(#18181b,#fafafa)] has-[#tsp-14-d-compact:checked]:[--tsp14-row:0.375rem] has-[#tsp-14-d-roomy:checked]:[--tsp14-row:0.95rem] has-[#tsp-14-fs-s:checked]:[--tsp14-fs:13px] has-[#tsp-14-fs-l:checked]:[--tsp14-fs:16.5px] has-[#tsp-14-hc:checked]:[--tsp14-line:light-dark(#71717a,#a1a1aa)] has-[#tsp-14-rm:checked]:[&_*]:transition-none! sm:px-8 sm:py-14" aria-labelledby="tsp-14-h">
  <div class="mx-auto grid w-full max-w-6xl gap-8 lg:grid-cols-[minmax(0,1fr)_minmax(0,26rem)]">
    <form class="grid min-w-0 content-start gap-8">
      <header><h1 id="tsp-14-h" class="text-3xl font-extrabold tracking-tight">Appearance</h1><p class="mt-1 text-tsp14-mut">Make Northwind look and feel the way you like. Changes preview instantly.</p></header>

      <fieldset class="grid gap-3">
        <legend class="mb-3 font-bold">Theme</legend>
        <div class="grid grid-cols-3 gap-3">
          <label class="group/t grid cursor-pointer gap-2 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tsp14-acc rounded-2xl"><input type="radio" name="theme" id="tsp-14-light" class="sr-only"><span class="grid aspect-[4/3] grid-cols-[28%_1fr] gap-1.5 overflow-hidden rounded-2xl border-2 border-tsp14-line bg-[#f4f4f5] p-2 transition group-has-checked/t:border-tsp14-acc group-has-checked/t:ring-4 group-has-checked/t:ring-tsp14-acc/20"><span class="rounded-md bg-white"></span><span class="grid content-start gap-1.5 rounded-md bg-white p-2"><span class="h-1.5 w-3/4 rounded-full bg-zinc-300"></span><span class="h-1.5 w-1/2 rounded-full bg-zinc-200"></span><span class="mt-1 h-3 w-8 rounded bg-tsp14-acc"></span></span></span><span class="text-center text-sm font-semibold">Light</span></label>
          <label class="group/t grid cursor-pointer gap-2 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tsp14-acc rounded-2xl"><input type="radio" name="theme" id="tsp-14-dark" class="sr-only"><span class="grid aspect-[4/3] grid-cols-[28%_1fr] gap-1.5 overflow-hidden rounded-2xl border-2 border-tsp14-line bg-[#09090b] p-2 transition group-has-checked/t:border-tsp14-acc group-has-checked/t:ring-4 group-has-checked/t:ring-tsp14-acc/20"><span class="rounded-md bg-[#18181b]"></span><span class="grid content-start gap-1.5 rounded-md bg-[#18181b] p-2"><span class="h-1.5 w-3/4 rounded-full bg-zinc-600"></span><span class="h-1.5 w-1/2 rounded-full bg-zinc-700"></span><span class="mt-1 h-3 w-8 rounded bg-tsp14-acc"></span></span></span><span class="text-center text-sm font-semibold">Dark</span></label>
          <label class="group/t grid cursor-pointer gap-2 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tsp14-acc rounded-2xl"><input type="radio" name="theme" id="tsp-14-system" class="sr-only" checked><span class="relative grid aspect-[4/3] place-items-center overflow-hidden rounded-2xl border-2 border-tsp14-line bg-[linear-gradient(135deg,#f4f4f5_50%,#09090b_50%)] transition group-has-checked/t:border-tsp14-acc group-has-checked/t:ring-4 group-has-checked/t:ring-tsp14-acc/20"><span class="grid size-9 place-items-center rounded-full bg-tsp14-card text-tsp14-ink shadow"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg></span></span><span class="text-center text-sm font-semibold">System</span></label>
        </div>
      </fieldset>

      <fieldset class="grid gap-3">
        <legend class="mb-3 font-bold">Accent colour</legend>
        <div class="flex flex-wrap gap-3">
          <label class="group/a grid size-11 cursor-pointer place-items-center rounded-full has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp14-ink"><input type="radio" name="accent" id="tsp-14-a-violet" class="sr-only" checked><span class="sr-only">Violet</span><span class="grid size-9 place-items-center rounded-full bg-[#7c3aed] ring-offset-2 ring-offset-tsp14-bg transition group-has-checked/a:ring-2 group-has-checked/a:ring-[#7c3aed]"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="size-4 opacity-0 group-has-checked/a:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span></label>
          <label class="group/a grid size-11 cursor-pointer place-items-center rounded-full has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp14-ink"><input type="radio" name="accent" id="tsp-14-a-indigo" class="sr-only"><span class="sr-only">Indigo</span><span class="grid size-9 place-items-center rounded-full bg-[#6366f1] ring-offset-2 ring-offset-tsp14-bg transition group-has-checked/a:ring-2 group-has-checked/a:ring-[#6366f1]"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="size-4 opacity-0 group-has-checked/a:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span></label>
          <label class="group/a grid size-11 cursor-pointer place-items-center rounded-full has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp14-ink"><input type="radio" name="accent" id="tsp-14-a-teal" class="sr-only"><span class="sr-only">Teal</span><span class="grid size-9 place-items-center rounded-full bg-[#0d9488] ring-offset-2 ring-offset-tsp14-bg transition group-has-checked/a:ring-2 group-has-checked/a:ring-[#0d9488]"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="size-4 opacity-0 group-has-checked/a:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span></label>
          <label class="group/a grid size-11 cursor-pointer place-items-center rounded-full has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp14-ink"><input type="radio" name="accent" id="tsp-14-a-rose" class="sr-only"><span class="sr-only">Rose</span><span class="grid size-9 place-items-center rounded-full bg-[#e11d48] ring-offset-2 ring-offset-tsp14-bg transition group-has-checked/a:ring-2 group-has-checked/a:ring-[#e11d48]"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="size-4 opacity-0 group-has-checked/a:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span></label>
          <label class="group/a grid size-11 cursor-pointer place-items-center rounded-full has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp14-ink"><input type="radio" name="accent" id="tsp-14-a-amber" class="sr-only"><span class="sr-only">Amber</span><span class="grid size-9 place-items-center rounded-full bg-[#d97706] ring-offset-2 ring-offset-tsp14-bg transition group-has-checked/a:ring-2 group-has-checked/a:ring-[#d97706]"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="size-4 opacity-0 group-has-checked/a:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span></label>
          <label class="group/a grid size-11 cursor-pointer place-items-center rounded-full has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp14-ink"><input type="radio" name="accent" id="tsp-14-a-ink" class="sr-only"><span class="sr-only">Monochrome</span><span class="grid size-9 place-items-center rounded-full bg-tsp14-ink ring-offset-2 ring-offset-tsp14-bg transition group-has-checked/a:ring-2 group-has-checked/a:ring-tsp14-ink"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="size-4 text-tsp14-bg opacity-0 group-has-checked/a:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span></label>
        </div>
      </fieldset>

      <div class="grid gap-6 sm:grid-cols-2">
        <fieldset class="grid gap-3"><legend class="mb-3 font-bold">Density</legend>
          <div class="grid grid-cols-3 gap-1 rounded-xl bg-tsp14-card p-1 ring-1 ring-tsp14-line">
            <label class="flex min-h-10 cursor-pointer items-center justify-center rounded-lg text-sm font-semibold text-tsp14-mut transition has-checked:bg-tsp14-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tsp14-acc"><input type="radio" name="density" id="tsp-14-d-compact" class="sr-only">Compact</label>
            <label class="flex min-h-10 cursor-pointer items-center justify-center rounded-lg text-sm font-semibold text-tsp14-mut transition has-checked:bg-tsp14-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tsp14-acc"><input type="radio" name="density" id="tsp-14-d-default" class="sr-only" checked>Default</label>
            <label class="flex min-h-10 cursor-pointer items-center justify-center rounded-lg text-sm font-semibold text-tsp14-mut transition has-checked:bg-tsp14-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tsp14-acc"><input type="radio" name="density" id="tsp-14-d-roomy" class="sr-only">Roomy</label>
          </div>
        </fieldset>
        <fieldset class="grid gap-3"><legend class="mb-3 font-bold">Text size</legend>
          <div class="grid grid-cols-3 gap-1 rounded-xl bg-tsp14-card p-1 ring-1 ring-tsp14-line">
            <label class="flex min-h-10 cursor-pointer items-center justify-center rounded-lg text-xs font-semibold text-tsp14-mut transition has-checked:bg-tsp14-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tsp14-acc"><input type="radio" name="fs" id="tsp-14-fs-s" class="sr-only">Aa</label>
            <label class="flex min-h-10 cursor-pointer items-center justify-center rounded-lg text-sm font-semibold text-tsp14-mut transition has-checked:bg-tsp14-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tsp14-acc"><input type="radio" name="fs" id="tsp-14-fs-m" class="sr-only" checked>Aa</label>
            <label class="flex min-h-10 cursor-pointer items-center justify-center rounded-lg text-base font-semibold text-tsp14-mut transition has-checked:bg-tsp14-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tsp14-acc"><input type="radio" name="fs" id="tsp-14-fs-l" class="sr-only">Aa</label>
          </div>
        </fieldset>
      </div>

      <div class="grid divide-y divide-tsp14-line rounded-2xl bg-tsp14-card ring-1 ring-tsp14-line">
        <label class="flex min-h-11 cursor-pointer items-center justify-between gap-4 p-4"><span><span class="block font-bold">High-contrast borders</span><span class="block text-sm text-tsp14-mut">Stronger dividers between rows and panels.</span></span><span class="relative flex-none"><input id="tsp-14-hc" type="checkbox" role="switch" class="peer sr-only"><span class="block h-6 w-11 rounded-full bg-tsp14-line transition peer-checked:bg-tsp14-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp14-acc"></span><span class="pointer-events-none absolute left-0.5 top-0.5 size-5 rounded-full bg-white shadow-sm transition peer-checked:translate-x-5"></span></span></label>
        <label class="flex min-h-11 cursor-pointer items-center justify-between gap-4 p-4"><span><span class="block font-bold">Reduce motion</span><span class="block text-sm text-tsp14-mut">Turn off transitions across the app.</span></span><span class="relative flex-none"><input id="tsp-14-rm" type="checkbox" role="switch" class="peer sr-only"><span class="block h-6 w-11 rounded-full bg-tsp14-line transition peer-checked:bg-tsp14-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp14-acc"></span><span class="pointer-events-none absolute left-0.5 top-0.5 size-5 rounded-full bg-white shadow-sm transition peer-checked:translate-x-5"></span></span></label>
      </div>
    </form>

    <aside class="min-w-0 lg:sticky lg:top-10 lg:self-start" aria-label="Live preview">
      <p class="mb-3 text-xs font-bold uppercase tracking-[0.14em] text-tsp14-mut">Live preview</p>
      <div class="overflow-hidden rounded-3xl bg-tsp14-card shadow-[0_30px_60px_-30px_rgb(0_0_0/0.35)] ring-1 ring-tsp14-line transition-colors duration-300">
        <div class="flex items-center gap-1.5 border-b border-tsp14-line px-4 py-3"><span class="size-2.5 rounded-full bg-[#ff5f57]"></span><span class="size-2.5 rounded-full bg-[#febc2e]"></span><span class="size-2.5 rounded-full bg-[#28c840]"></span><span class="ml-3 text-xs text-tsp14-mut">Northwind · Projects</span></div>
        <div class="grid grid-cols-[7.5rem_1fr] text-(length:--tsp14-fs)">
          <nav class="grid content-start gap-1 border-r border-tsp14-line p-2.5 text-[0.85em]" aria-hidden="true">
            <span class="rounded-lg bg-tsp14-acc/12 px-2.5 py-(--tsp14-row) font-bold text-tsp14-acc">Projects</span>
            <span class="rounded-lg px-2.5 py-(--tsp14-row) text-tsp14-mut">Inbox</span>
            <span class="rounded-lg px-2.5 py-(--tsp14-row) text-tsp14-mut">Reports</span>
            <span class="rounded-lg px-2.5 py-(--tsp14-row) text-tsp14-mut">Settings</span>
          </nav>
          <div class="grid content-start gap-3 p-4" aria-hidden="true">
            <div class="flex items-center justify-between"><span class="font-extrabold">Q4 launch</span><span class="rounded-lg bg-tsp14-acc px-2.5 py-1 text-[0.8em] font-bold text-white">New task</span></div>
            <div class="h-1.5 rounded-full bg-tsp14-line"><div class="h-full w-2/3 rounded-full bg-tsp14-acc transition-[width] duration-700"></div></div>
            <ul class="divide-y divide-tsp14-line rounded-xl ring-1 ring-tsp14-line">
              <li class="flex items-center gap-2.5 px-3 py-(--tsp14-row)"><span class="grid size-4 place-items-center rounded bg-tsp14-acc text-white"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" class="size-2.5"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-tsp14-mut line-through">Pricing page copy</span></li>
              <li class="flex items-center gap-2.5 px-3 py-(--tsp14-row)"><span class="size-4 rounded ring-2 ring-tsp14-line"></span>Launch email</li>
              <li class="flex items-center gap-2.5 px-3 py-(--tsp14-row)"><span class="size-4 rounded ring-2 ring-tsp14-line"></span>Partner webinar</li>
              <li class="flex items-center gap-2.5 px-3 py-(--tsp14-row)"><span class="size-4 rounded ring-2 ring-tsp14-line"></span>Press kit</li>
            </ul>
          </div>
        </div>
      </div>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp14-bg: light-dark(#f6f6f8, #0b0b0e);
  --color-tsp14-bg: light-dark(oklch(0.974 0.003 286), oklch(0.155 0.006 286));
  --color-tsp14-card: light-dark(#ffffff, #16161a);
  --color-tsp14-card: light-dark(oklch(1 0 0), oklch(0.2 0.007 286));
  --color-tsp14-ink: light-dark(#18181b, #f4f4f5);
  --color-tsp14-ink: light-dark(oklch(0.21 0.006 286), oklch(0.967 0.001 286));
  --color-tsp14-mut: light-dark(#63636e, #a1a1ab);
  --color-tsp14-mut: light-dark(oklch(0.505 0.014 286), oklch(0.72 0.012 286));
  --font-tsp14-sans: 'Urbanist', system-ui, sans-serif;
}
/* Runtime variables the radios rewrite — inline so utilities read them at the element, not :root. */

@theme inline {
  --color-tsp14-acc: var(--tsp14-acc);
  --color-tsp14-line: var(--tsp14-line);
}

.tsp-14 {
  width: 100%;
  min-height: 100svh;
}
/* Defaults live in a layer so the has-[…]:[--tsp14-*] utilities on the root can override them. */

@layer base {
  .tsp-14 {
    --tsp14-acc: #7c3aed;
    --tsp14-line: light-dark(#e6e6ea, #2a2a31);
    --tsp14-row: 0.6rem;
    --tsp14-fs: 14.5px;
  }
}
```
