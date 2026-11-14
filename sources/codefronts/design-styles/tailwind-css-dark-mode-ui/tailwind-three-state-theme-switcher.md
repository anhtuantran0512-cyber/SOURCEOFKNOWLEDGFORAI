---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-three-state-theme-switcher/"
title: "Tailwind Three-State Theme Switcher (System / Light / Dark)"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "The control users actually expect: three states, not two."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Three-State Theme Switcher (System / Light / Dark)
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-three-state-theme-switcher/

The control users actually expect: three states, not two. System adds nothing and lets prefers-color-scheme through; Light and Dark pin a scheme that survives an OS change mid-session. Three radios, one sliding thumb, zero JavaScript — plus a live truth table that highlights the exact cell (OS × choice) you are in right now.
## HTML
```html
<div class="tdm-09 group/root scheme-light-dark has-[#tdm-09-light:checked]:scheme-light has-[#tdm-09-dark:checked]:scheme-dark grid w-full min-h-svh place-items-center bg-tdm09-bg bg-[radial-gradient(60%_50%_at_50%_0%,var(--color-tdm09-glow),transparent_70%)] px-4 py-12 font-tdm09-sans text-tdm09-ink antialiased transition-colors duration-300">
  <div class="w-full max-w-4xl overflow-hidden rounded-[28px] border border-tdm09-line bg-tdm09-surface shadow-tdm09-shell">
    <header class="flex flex-wrap items-center justify-between gap-4 border-b border-tdm09-line px-5 py-4">
      <div class="flex items-center gap-3">
        <span class="grid size-9 place-items-center rounded-xl bg-tdm09-acc text-tdm09-acc-ink"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 3 9 5-9 5-9-5Z"/><path d="m3 13 9 5 9-5"/></svg></span>
        <span class="font-semibold tracking-tight">Cadence</span>
        <span class="inline-flex items-center gap-1.5 rounded-full border border-tdm09-line px-2.5 py-1 font-tdm09-mono text-[11px] text-tdm09-mut"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8.5 20.5h7M12 17v3.5"/></svg>OS says <strong class="font-semibold text-tdm09-ink dark:hidden">light</strong><strong class="font-semibold text-tdm09-ink not-dark:hidden">dark</strong></span>
      </div>
      <fieldset class="group/seg relative grid grid-cols-3 rounded-2xl border border-tdm09-line bg-tdm09-track p-1">
        <legend class="sr-only">Theme</legend>
        <span aria-hidden="true" class="absolute inset-y-1 left-1 w-[calc((100%-0.5rem)/3)] rounded-xl bg-tdm09-raised shadow-[0_1px_2px_rgb(0_0_0/.18),inset_0_0_0_1px_var(--color-tdm09-line)] transition-transform duration-300 ease-[cubic-bezier(.3,1.3,.5,1)] group-has-[#tdm-09-light:checked]/seg:translate-x-full group-has-[#tdm-09-dark:checked]/seg:translate-x-[200%] motion-reduce:transition-none"></span>
        <label class="relative z-10 flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-xl px-3.5 text-[13px] font-medium text-tdm09-mut transition-colors hover:text-tdm09-ink has-checked:text-tdm09-ink has-focus-visible:outline-2 has-focus-visible:outline-tdm09-focus">
          <input type="radio" name="tdm-09-theme" id="tdm-09-system" class="sr-only" checked><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8.5 20.5h7M12 17v3.5"/></svg>System
        </label>
        <label class="relative z-10 flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-xl px-3.5 text-[13px] font-medium text-tdm09-mut transition-colors hover:text-tdm09-ink has-checked:text-tdm09-ink has-focus-visible:outline-2 has-focus-visible:outline-tdm09-focus">
          <input type="radio" name="tdm-09-theme" id="tdm-09-light" class="sr-only"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>Light
        </label>
        <label class="relative z-10 flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-xl px-3.5 text-[13px] font-medium text-tdm09-mut transition-colors hover:text-tdm09-ink has-checked:text-tdm09-ink has-focus-visible:outline-2 has-focus-visible:outline-tdm09-focus">
          <input type="radio" name="tdm-09-theme" id="tdm-09-dark" class="sr-only"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>Dark
        </label>
      </fieldset>
    </header>
    <div class="grid md:grid-cols-[minmax(0,1fr)_17rem]">
      <section class="grid content-start gap-5 p-6 sm:p-8">
        <div class="grid gap-2">
          <p class="font-tdm09-mono text-[11px] uppercase tracking-[0.16em] text-tdm09-acc-text">Appearance</p>
          <h1 class="text-[clamp(1.6rem,3vw,2.2rem)] font-semibold tracking-[-0.035em] text-balance">Three states, one radio group</h1>
          <p class="max-w-[54ch] text-[15px]/relaxed text-pretty text-tdm09-mut">System defers to the operating system. Light and Dark pin the theme and survive an OS change mid-session — including on machines whose preference already matches your default.</p>
        </div>
        <div class="overflow-hidden rounded-2xl border border-tdm09-line" role="table" aria-label="Resolved theme by OS and choice">
          <div role="row" class="grid grid-cols-4 border-b border-tdm09-line bg-tdm09-track font-tdm09-mono text-[11px] uppercase tracking-wide text-tdm09-mut"><span role="columnheader" class="px-3 py-2.5">OS</span><span role="columnheader" class="px-3 py-2.5">System</span><span role="columnheader" class="px-3 py-2.5">Light</span><span role="columnheader" class="px-3 py-2.5">Dark</span></div>
          <div role="row" class="grid grid-cols-4 gap-1.5 p-1.5 font-tdm09-mono text-[13px]"><span role="rowheader" class="flex items-center px-1.5 text-tdm09-mut">light</span><span role="cell" class="flex min-h-10 items-center gap-1.5 rounded-lg border border-transparent px-2.5 text-tdm09-mut transition not-dark:group-has-[#tdm-09-system:checked]/root:border-tdm09-acc/60 not-dark:group-has-[#tdm-09-system:checked]/root:bg-tdm09-acc/14 not-dark:group-has-[#tdm-09-system:checked]/root:text-tdm09-ink"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>light</span><span role="cell" class="flex min-h-10 items-center gap-1.5 rounded-lg border border-transparent px-2.5 text-tdm09-mut transition not-dark:group-has-[#tdm-09-light:checked]/root:border-tdm09-acc/60 not-dark:group-has-[#tdm-09-light:checked]/root:bg-tdm09-acc/14 not-dark:group-has-[#tdm-09-light:checked]/root:text-tdm09-ink"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>light</span><span role="cell" class="flex min-h-10 items-center gap-1.5 rounded-lg border border-transparent px-2.5 text-tdm09-mut transition not-dark:group-has-[#tdm-09-dark:checked]/root:border-tdm09-acc/60 not-dark:group-has-[#tdm-09-dark:checked]/root:bg-tdm09-acc/14 not-dark:group-has-[#tdm-09-dark:checked]/root:text-tdm09-ink"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>dark</span></div>
          <div role="row" class="grid grid-cols-4 gap-1.5 p-1.5 font-tdm09-mono text-[13px]"><span role="rowheader" class="flex items-center px-1.5 text-tdm09-mut">dark</span><span role="cell" class="flex min-h-10 items-center gap-1.5 rounded-lg border border-transparent px-2.5 text-tdm09-mut transition dark:group-has-[#tdm-09-system:checked]/root:border-tdm09-acc/60 dark:group-has-[#tdm-09-system:checked]/root:bg-tdm09-acc/14 dark:group-has-[#tdm-09-system:checked]/root:text-tdm09-ink"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>dark</span><span role="cell" class="flex min-h-10 items-center gap-1.5 rounded-lg border border-transparent px-2.5 text-tdm09-mut transition dark:group-has-[#tdm-09-light:checked]/root:border-tdm09-acc/60 dark:group-has-[#tdm-09-light:checked]/root:bg-tdm09-acc/14 dark:group-has-[#tdm-09-light:checked]/root:text-tdm09-ink"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>light</span><span role="cell" class="flex min-h-10 items-center gap-1.5 rounded-lg border border-transparent px-2.5 text-tdm09-mut transition dark:group-has-[#tdm-09-dark:checked]/root:border-tdm09-acc/60 dark:group-has-[#tdm-09-dark:checked]/root:bg-tdm09-acc/14 dark:group-has-[#tdm-09-dark:checked]/root:text-tdm09-ink"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>dark</span></div>
        </div>
      </section>
      <aside class="grid content-start gap-2 border-t border-tdm09-line bg-tdm09-track p-5 md:border-t-0 md:border-l">
        <label class="group/sw flex min-h-12 cursor-pointer items-center justify-between gap-3 rounded-xl px-3 text-sm transition hover:bg-tdm09-ink/5 has-focus-visible:outline-2 has-focus-visible:outline-tdm09-focus">
          Sync across devices<input type="checkbox" class="sr-only" checked>
          <span class="relative h-6 w-10 flex-none rounded-full bg-tdm09-ink/15 transition-colors group-has-checked/sw:bg-tdm09-acc" aria-hidden="true"><span class="absolute top-0.5 left-0.5 size-5 rounded-full bg-white shadow transition-transform group-has-checked/sw:translate-x-4"></span></span>
        </label>
        <label class="group/sw flex min-h-12 cursor-pointer items-center justify-between gap-3 rounded-xl px-3 text-sm transition hover:bg-tdm09-ink/5 has-focus-visible:outline-2 has-focus-visible:outline-tdm09-focus">
          Dim images in dark mode<input type="checkbox" class="sr-only" checked>
          <span class="relative h-6 w-10 flex-none rounded-full bg-tdm09-ink/15 transition-colors group-has-checked/sw:bg-tdm09-acc" aria-hidden="true"><span class="absolute top-0.5 left-0.5 size-5 rounded-full bg-white shadow transition-transform group-has-checked/sw:translate-x-4"></span></span>
        </label>
        <label class="group/sw flex min-h-12 cursor-pointer items-center justify-between gap-3 rounded-xl px-3 text-sm transition hover:bg-tdm09-ink/5 has-focus-visible:outline-2 has-focus-visible:outline-tdm09-focus">
          Reduce transparency<input type="checkbox" class="sr-only">
          <span class="relative h-6 w-10 flex-none rounded-full bg-tdm09-ink/15 transition-colors group-has-checked/sw:bg-tdm09-acc" aria-hidden="true"><span class="absolute top-0.5 left-0.5 size-5 rounded-full bg-white shadow transition-transform group-has-checked/sw:translate-x-4"></span></span>
        </label>
        <p class="px-3 pt-2 text-xs/relaxed text-tdm09-mut">Preference stored per workspace. Rendering stays pure CSS.</p>
      </aside>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm09-bg: light-dark(#f1f3ee, #0a0b0e);
  --color-tdm09-glow: light-dark(rgb(101 163 13 / .1), rgb(163 230 53 / .08));
  --color-tdm09-surface: light-dark(#ffffff, #12131a);
  --color-tdm09-raised: light-dark(#ffffff, #1e2029);
  --color-tdm09-track: light-dark(#f6f7f4, #0e0f15);
  --color-tdm09-ink: light-dark(#0e100b, #f4f4f7);
  --color-tdm09-mut: light-dark(#585e52, #9a9fad);
  --color-tdm09-line: light-dark(#e2e5dc, #262935);
  --color-tdm09-acc: light-dark(#4d7c0f, #a3e635);
  --color-tdm09-acc-text: light-dark(#3f6212, #bef264);
  --color-tdm09-acc-ink: light-dark(#ffffff, #131c05);
  --color-tdm09-focus: light-dark(#3f6212, #d9f99d);
  --shadow-tdm09-shell: 0 40px 90px -60px light-dark(rgb(20 30 10 / .35), rgb(0 0 0 / .9));
  --font-tdm09-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm09-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```
