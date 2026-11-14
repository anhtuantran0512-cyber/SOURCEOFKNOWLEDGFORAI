---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-macos-window-layout-vibrancy-sidebar/"
title: "Tailwind macOS Window Layout with Vibrancy Sidebar"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A native-feeling desktop notes app: translucent source list with grouped folders and counts, a unified toolbar spanning both columns, and a document pane…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind macOS Window Layout with Vibrancy Sidebar
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-macos-window-layout-vibrancy-sidebar/

A native-feeling desktop notes app: translucent source list with grouped folders and counts, a unified toolbar spanning both columns, and a document pane that owns the only scrollbar — vibrancy in two utilities.
## HTML
```html
<section class="tgx-26 w-full min-h-svh font-tgx26-sans p-6 bg-[linear-gradient(140deg,oklch(0.75_0.08_300),oklch(0.7_0.09_220)_50%,oklch(0.78_0.07_170))]">
  <div class="grid grid-cols-[224px_minmax(0,1fr)] grid-rows-[auto_minmax(0,1fr)] max-sm:grid-cols-[minmax(0,1fr)] h-[400px] w-[min(680px,100%)] mx-auto rounded-2xl overflow-hidden border border-white/40 shadow-[0_30px_70px_-30px_oklch(0.2_0.05_260/0.7)]">
    <header class="col-span-2 max-sm:col-span-1 flex items-center gap-4 px-3.5 py-2.5 bg-white/85 backdrop-blur-lg border-b border-tgx26-hair">
      <span aria-hidden="true" class="flex gap-[7px]"><i class="size-[11px] rounded-full bg-[oklch(0.68_0.19_25)]"></i><i class="size-[11px] rounded-full bg-[oklch(0.8_0.15_85)]"></i><i class="size-[11px] rounded-full bg-[oklch(0.75_0.17_145)]"></i></span>
      <strong class="text-[0.82rem] text-tgx26-ink">Fieldnotes</strong>
      <span class="text-[0.72rem] text-tgx26-dim max-sm:hidden">Edited 14:06</span>
      <button type="button" class="ml-auto text-[0.75rem] font-medium text-tgx26-accent bg-tgx26-accenttint border border-tgx26-accent/30 rounded-lg px-3 min-h-9 cursor-pointer transition-colors hover:bg-tgx26-accenthover focus-visible:outline-2 focus-visible:outline-tgx26-accent focus-visible:outline-offset-2">＋ New note</button>
    </header>
    <nav aria-label="Folders" class="max-sm:hidden overflow-y-auto bg-white/60 backdrop-blur-xl backdrop-saturate-150 border-r border-tgx26-hair px-2 py-2.5 flex flex-col gap-0.5">
      <p class="text-[0.62rem] font-bold tracking-[0.08em] uppercase text-tgx26-dim px-2 pt-2 pb-1">iCloud</p>
      <a href="#0" aria-current="page" class="grid grid-cols-[1.3em_minmax(0,1fr)_auto] items-center gap-x-2 text-[0.8rem] no-underline text-tgx26-ink px-2 min-h-8 rounded-lg transition-colors hover:bg-black/5 aria-[current=page]:bg-tgx26-sel aria-[current=page]:font-semibold focus-visible:outline-2 focus-visible:outline-tgx26-accent focus-visible:-outline-offset-2"><span aria-hidden="true">📝</span>All Notes<em class="not-italic text-[0.68rem] tabular-nums text-tgx26-dim">128</em></a>
      <a href="#0" class="grid grid-cols-[1.3em_minmax(0,1fr)_auto] items-center gap-x-2 text-[0.8rem] no-underline text-tgx26-ink px-2 min-h-8 rounded-lg transition-colors hover:bg-black/5 focus-visible:outline-2 focus-visible:outline-tgx26-accent focus-visible:-outline-offset-2"><span aria-hidden="true">📌</span>Pinned<em class="not-italic text-[0.68rem] tabular-nums text-tgx26-dim">6</em></a>
      <a href="#0" class="grid grid-cols-[1.3em_minmax(0,1fr)_auto] items-center gap-x-2 text-[0.8rem] no-underline text-tgx26-ink px-2 min-h-8 rounded-lg transition-colors hover:bg-black/5 focus-visible:outline-2 focus-visible:outline-tgx26-accent focus-visible:-outline-offset-2"><span aria-hidden="true">🗂️</span>Field trips<em class="not-italic text-[0.68rem] tabular-nums text-tgx26-dim">34</em></a>
      <a href="#0" class="grid grid-cols-[1.3em_minmax(0,1fr)_auto] items-center gap-x-2 text-[0.8rem] no-underline text-tgx26-ink px-2 min-h-8 rounded-lg transition-colors hover:bg-black/5 focus-visible:outline-2 focus-visible:outline-tgx26-accent focus-visible:-outline-offset-2"><span aria-hidden="true">🗑️</span>Recently deleted<em class="not-italic text-[0.68rem] tabular-nums text-tgx26-dim">3</em></a>
      <p class="text-[0.62rem] font-bold tracking-[0.08em] uppercase text-tgx26-dim px-2 pt-3 pb-1">Tags</p>
      <a href="#0" class="grid grid-cols-[1.3em_minmax(0,1fr)_auto] items-center gap-x-2 text-[0.8rem] no-underline text-tgx26-ink px-2 min-h-8 rounded-lg transition-colors hover:bg-black/5 focus-visible:outline-2 focus-visible:outline-tgx26-accent focus-visible:-outline-offset-2"><span aria-hidden="true" class="text-tgx26-accent">#</span>coast-road<em class="not-italic text-[0.68rem] tabular-nums text-tgx26-dim">12</em></a>
      <a href="#0" class="grid grid-cols-[1.3em_minmax(0,1fr)_auto] items-center gap-x-2 text-[0.8rem] no-underline text-tgx26-ink px-2 min-h-8 rounded-lg transition-colors hover:bg-black/5 focus-visible:outline-2 focus-visible:outline-tgx26-accent focus-visible:-outline-offset-2"><span aria-hidden="true" class="text-tgx26-accent">#</span>ferries<em class="not-italic text-[0.68rem] tabular-nums text-tgx26-dim">9</em></a>
    </nav>
    <main class="overflow-y-auto bg-white p-5 flex flex-col gap-3">
      <p class="text-[0.7rem] text-tgx26-dim">Thursday 18 September · 14:06</p>
      <h2 class="text-[1.05rem] font-semibold text-tgx26-ink">Vestmanna, day three</h2>
      <p class="text-[0.84rem] leading-[1.7] text-tgx26-body">Ferry ran at 17:20 after all. The sound was flat for about an hour, which is apparently all anyone needs. Shot the ridge from the top of the pass while the light held — four minutes, maybe five.</p>
      <figure class="flex flex-col gap-1.5">
        <div class="aspect-[16/9] overflow-hidden rounded-lg bg-tgx26-cell"><img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=800&h=450&q=80&auto=format&fit=crop" alt="Coastal ridge with low cloud breaking above dark water" loading="lazy" class="w-full h-full object-cover"></div>
        <figcaption class="text-[0.7rem] text-tgx26-dim">IMG_4471.heic · attached from Photos</figcaption>
      </figure>
      <p class="text-[0.84rem] leading-[1.7] text-tgx26-body">Note for the edit: the sidebar of this app is the layout worth stealing — translucent fill, blur plus saturate over the window's own backdrop, and a three-track row grid so icon, label and count line up on every row.</p>
      <ul class="flex flex-col gap-1.5 text-[0.84rem] leading-[1.6] text-tgx26-body list-disc list-inside marker:text-tgx26-accent">
        <li>Check the 06:40 bus on Sunday</li>
        <li>Ask about the harbour light schedule</li>
      </ul>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx26-ink: #2a2b33;
  --color-tgx26-ink: oklch(0.29 0.01 270);
  --color-tgx26-body: #4c505c;
  --color-tgx26-body: oklch(0.43 0.015 265);
  --color-tgx26-dim: #6c707c;
  --color-tgx26-dim: oklch(0.55 0.015 265);
  --color-tgx26-hair: #d4d6dd;
  --color-tgx26-hair: oklch(0.86 0.01 265);
  --color-tgx26-cell: #e8eaef;
  --color-tgx26-cell: oklch(0.92 0.008 265);
  --color-tgx26-accent: #4257c4;
  --color-tgx26-accent: oklch(0.47 0.18 265);
  --color-tgx26-accenttint: #eceefb;
  --color-tgx26-accenttint: oklch(0.95 0.02 265);
  --color-tgx26-accenthover: #dfe3f8;
  --color-tgx26-accenthover: oklch(0.92 0.03 265);
  --color-tgx26-sel: #dde2f9;
  --color-tgx26-sel: oklch(0.91 0.04 265);
  --font-tgx26-sans: 'Inter Tight', system-ui, -apple-system, sans-serif;
}

.tgx-26 {
  width: 100%;
  min-height: 100svh;
}
/* Safari < 16.4 prefixes for the toolbar and the source list. */

.tgx-26 header {
  -webkit-backdrop-filter: blur(16px);
}

.tgx-26 nav {
  -webkit-backdrop-filter: blur(24px) saturate(150%);
}
```
