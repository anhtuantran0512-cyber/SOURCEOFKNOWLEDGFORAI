---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-two-pane-webmail-list-reading-layout/"
title: "Tailwind Two-Pane Webmail Layout with List and Reading Pane"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The list/detail split every mail client, messenger and support inbox uses: folder rail, 320px message list, reading pane &mdash; three independent scroll…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Two-Pane Webmail Layout with List and Reading Pane
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-two-pane-webmail-list-reading-layout/

The list/detail split every mail client, messenger and support inbox uses: folder rail, 320px message list, reading pane &mdash; three independent scroll regions in one grid. The port's pleasure is line-clamp-2, which replaces the four-declaration -webkit-box incantation with one utility.
## HTML
```html
<section class="tsl-12 w-full h-svh min-h-svh grid grid-cols-[200px_320px_1fr] font-tsl12-sans bg-white text-tsl12-ink">
  <aside aria-label="Folders" class="bg-tsl12-panel border-r border-tsl12-line px-2.5 py-4 overflow-y-auto">
    <button type="button" class="w-full min-h-11 mb-3.5 rounded-[10px] border-0 bg-tsl12-accent text-white text-[13.5px] font-semibold cursor-pointer transition-[filter] duration-200 hover:brightness-110 focus-visible:outline-2 focus-visible:outline-tsl12-accent focus-visible:outline-offset-2">Compose</button>
    <nav class="flex flex-col gap-0.5">
      <a href="#" aria-current="page" class="flex items-center justify-between min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl12-mut no-underline transition-colors duration-150 hover:text-tsl12-ink hover:bg-tsl12-hover aria-[current=page]:text-tsl12-ink aria-[current=page]:bg-tsl12-tint aria-[current=page]:font-semibold focus-visible:outline-2 focus-visible:outline-tsl12-accent focus-visible:outline-offset-1">Inbox <span class="text-[11.5px] font-semibold text-tsl12-accent">12</span></a>
      <a href="#" class="flex items-center justify-between min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl12-mut no-underline transition-colors duration-150 hover:text-tsl12-ink hover:bg-tsl12-hover focus-visible:outline-2 focus-visible:outline-tsl12-accent focus-visible:outline-offset-1">Starred</a>
      <a href="#" class="flex items-center justify-between min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl12-mut no-underline transition-colors duration-150 hover:text-tsl12-ink hover:bg-tsl12-hover focus-visible:outline-2 focus-visible:outline-tsl12-accent focus-visible:outline-offset-1">Sent</a>
      <a href="#" class="flex items-center justify-between min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl12-mut no-underline transition-colors duration-150 hover:text-tsl12-ink hover:bg-tsl12-hover focus-visible:outline-2 focus-visible:outline-tsl12-accent focus-visible:outline-offset-1">Drafts <span class="text-[11.5px] font-semibold text-tsl12-accent">2</span></a>
      <a href="#" class="flex items-center justify-between min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl12-mut no-underline transition-colors duration-150 hover:text-tsl12-ink hover:bg-tsl12-hover focus-visible:outline-2 focus-visible:outline-tsl12-accent focus-visible:outline-offset-1">Archive</a>
    </nav>
  </aside>
  <div role="listbox" aria-label="Messages" class="border-r border-tsl12-line overflow-y-auto overscroll-contain [scrollbar-gutter:stable]">
    <a href="#" role="option" aria-selected="false" data-unread class="group grid grid-cols-[auto_1fr_auto] items-start gap-2.5 px-3.5 py-3 border-b border-tsl12-line no-underline text-inherit transition-colors duration-150 hover:bg-tsl12-rowhover aria-selected:bg-tsl12-tint aria-selected:shadow-[inset_2.5px_0_0_var(--color-tsl12-accent)] focus-visible:outline-2 focus-visible:outline-tsl12-accent focus-visible:-outline-offset-2"><span aria-hidden="true" class="w-[7px] h-[7px] mt-[7px] rounded-full bg-transparent group-data-unread:bg-tsl12-accent"></span><span class="min-w-0 grid gap-[3px]"><strong class="text-[13.5px] font-medium leading-tight group-data-unread:font-bold">Priya Raman</strong><em class="not-italic text-[12.5px] leading-[1.45] text-tsl12-mut line-clamp-2">Q3 roadmap review &mdash; the container query rollout is ahead of schedule and I think we can&hellip;</em></span><time class="mt-0.5 text-[11.5px] font-medium text-tsl12-mut">09:41</time></a>
    <a href="#" role="option" aria-selected="true" class="group grid grid-cols-[auto_1fr_auto] items-start gap-2.5 px-3.5 py-3 border-b border-tsl12-line no-underline text-inherit transition-colors duration-150 hover:bg-tsl12-rowhover aria-selected:bg-tsl12-tint aria-selected:shadow-[inset_2.5px_0_0_var(--color-tsl12-accent)] focus-visible:outline-2 focus-visible:outline-tsl12-accent focus-visible:-outline-offset-2"><span aria-hidden="true" class="w-[7px] h-[7px] mt-[7px] rounded-full bg-transparent group-data-unread:bg-tsl12-accent"></span><span class="min-w-0 grid gap-[3px]"><strong class="text-[13.5px] font-medium leading-tight group-data-unread:font-bold">Marcus Webb</strong><em class="not-italic text-[12.5px] leading-[1.45] text-tsl12-mut line-clamp-2">Re: Design tokens sync &mdash; agreed, let's move the semantic layer into the base package&hellip;</em></span><time class="mt-0.5 text-[11.5px] font-medium text-tsl12-mut">08:17</time></a>
    <a href="#" role="option" aria-selected="false" data-unread class="group grid grid-cols-[auto_1fr_auto] items-start gap-2.5 px-3.5 py-3 border-b border-tsl12-line no-underline text-inherit transition-colors duration-150 hover:bg-tsl12-rowhover aria-selected:bg-tsl12-tint aria-selected:shadow-[inset_2.5px_0_0_var(--color-tsl12-accent)] focus-visible:outline-2 focus-visible:outline-tsl12-accent focus-visible:-outline-offset-2"><span aria-hidden="true" class="w-[7px] h-[7px] mt-[7px] rounded-full bg-transparent group-data-unread:bg-tsl12-accent"></span><span class="min-w-0 grid gap-[3px]"><strong class="text-[13.5px] font-medium leading-tight group-data-unread:font-bold">Linear</strong><em class="not-italic text-[12.5px] leading-[1.45] text-tsl12-mut line-clamp-2">Weekly digest: 14 issues closed, 3 in review. Cycle 42 completes Friday.</em></span><time class="mt-0.5 text-[11.5px] font-medium text-tsl12-mut">Mon</time></a>
    <a href="#" role="option" aria-selected="false" class="group grid grid-cols-[auto_1fr_auto] items-start gap-2.5 px-3.5 py-3 border-b border-tsl12-line no-underline text-inherit transition-colors duration-150 hover:bg-tsl12-rowhover aria-selected:bg-tsl12-tint aria-selected:shadow-[inset_2.5px_0_0_var(--color-tsl12-accent)] focus-visible:outline-2 focus-visible:outline-tsl12-accent focus-visible:-outline-offset-2"><span aria-hidden="true" class="w-[7px] h-[7px] mt-[7px] rounded-full bg-transparent group-data-unread:bg-tsl12-accent"></span><span class="min-w-0 grid gap-[3px]"><strong class="text-[13.5px] font-medium leading-tight group-data-unread:font-bold">Amara Osei</strong><em class="not-italic text-[12.5px] leading-[1.45] text-tsl12-mut line-clamp-2">Accessibility audit results &mdash; great news on the focus-visible coverage, two items left&hellip;</em></span><time class="mt-0.5 text-[11.5px] font-medium text-tsl12-mut">Mon</time></a>
  </div>
  <main class="overflow-y-auto px-[38px] py-8 [scrollbar-gutter:stable]">
    <h1 class="text-xl font-bold leading-snug">Re: Design tokens sync</h1>
    <p class="mt-2.5 mb-[22px] text-[12.5px] font-medium text-tsl12-mut">Marcus Webb &middot; to Design Platform &middot; 08:17</p>
    <p class="max-w-[60ch] mb-3.5 text-sm leading-[1.7] text-tsl12-body text-pretty">Agreed &mdash; let's move the semantic layer into the base package. The component tokens can then alias into it, which keeps theming to a single override point.</p>
    <p class="max-w-[60ch] text-sm leading-[1.7] text-tsl12-body text-pretty">I'll draft the migration doc today. The mail list on your left scrolls independently of this pane &mdash; three scroll regions, one grid.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl12-panel: #f3f4f6;
  --color-tsl12-panel: oklch(0.965 0.005 240);
  --color-tsl12-ink: #363b43;
  --color-tsl12-ink: oklch(0.25 0.02 240);
  --color-tsl12-body: #4c525c;
  --color-tsl12-body: oklch(0.35 0.015 240);
  --color-tsl12-mut: #71767f;
  --color-tsl12-mut: oklch(0.5 0.015 240);
  --color-tsl12-line: #dfe1e5;
  --color-tsl12-line: oklch(0.89 0.007 240);
  --color-tsl12-accent: #3f5fd0;
  --color-tsl12-accent: oklch(0.52 0.17 255);
  --color-tsl12-hover: rgb(54 59 67 / 0.05);
  --color-tsl12-hover: color-mix(in oklab, oklch(0.25 0.02 240) 5%, transparent);
  --color-tsl12-rowhover: rgb(54 59 67 / 0.035);
  --color-tsl12-rowhover: color-mix(in oklab, oklch(0.25 0.02 240) 3.5%, transparent);
  --color-tsl12-tint: rgb(63 95 208 / 0.1);
  --color-tsl12-tint: color-mix(in oklab, oklch(0.52 0.17 255) 10%, transparent);
  --font-tsl12-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-12 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: light;
}
```
