---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-grid-template-areas-dashboard-layout/"
title: "Tailwind CSS Grid Template Areas Dashboard Layout"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "Tailwind has no grid-areas utility &mdash; and this demo shows you do not need one."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Grid Template Areas Dashboard Layout
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-grid-template-areas-dashboard-layout/

Tailwind has no grid-areas utility &mdash; and this demo shows you do not need one. The whole header / sidebar / main / aside / footer shell is an arbitrary property, [grid-template-areas:'header_header_header'_'sidebar_main_aside'_'footer_footer_footer'], re-drawn under @max-[41rem]/stage:. Drag the stage edge and a live badge reports which template is active.
## HTML
```html
<section class="tdl-06 grid w-full min-h-svh place-items-center bg-tdl06-bg p-3 font-tdl06-sans text-tdl06-ink antialiased sm:p-5" aria-label="grid-template-areas dashboard demo">
  <div class="@container/stage h-[calc(100svh-2.5rem)] min-h-[32rem] w-full max-w-full min-w-[20rem] resize-x overflow-auto rounded-2xl border border-tdl06-edge bg-tdl06-paper bg-[radial-gradient(var(--color-tdl06-dot)_1px,transparent_1px)] bg-size-[16px_16px] p-3.5">
    <div class="grid h-full grid-cols-[12.5rem_minmax(0,1fr)_14.5rem] grid-rows-[3.375rem_minmax(0,1fr)_2.75rem] gap-3 [grid-template-areas:'header_header_header'_'sidebar_main_aside'_'footer_footer_footer'] @max-[41rem]/stage:grid-cols-[4rem_minmax(0,1fr)] @max-[41rem]/stage:grid-rows-[3.375rem_minmax(0,1fr)_auto_2.75rem] @max-[41rem]/stage:[grid-template-areas:'header_header'_'sidebar_main'_'aside_aside'_'footer_footer'] *:relative *:min-w-0 *:rounded-xl *:border-[1.5px] *:border-dashed *:border-tdl06-line/55 *:bg-linear-150 *:from-tdl06-fill2 *:to-tdl06-fill *:px-3.5 *:py-3 *:transition-colors *:hover:border-tdl06-acc *:hover:bg-tdl06-hover [&>*>b]:absolute [&>*>b]:-top-px [&>*>b]:-left-px [&>*>b]:rounded-[10px_0_10px_0] [&>*>b]:bg-tdl06-line [&>*>b]:px-2.5 [&>*>b]:py-1 [&>*>b]:font-tdl06-mono [&>*>b]:text-[10px] [&>*>b]:font-bold [&>*>b]:tracking-[0.06em] [&>*>b]:text-white [&>*:hover>b]:bg-tdl06-acc">
      <header class="flex items-center gap-3.5 pl-24! [grid-area:header]"><b>header</b><span class="truncate font-tdl06-mono text-[11px] font-semibold text-tdl06-mut">[grid-area:header]</span>
        <span class="ml-auto flex flex-none items-center gap-1.5 rounded-full bg-tdl06-acc/10 px-2.5 py-1 text-[10.5px] font-bold tracking-[0.06em] text-tdl06-acc uppercase"><i aria-hidden="true" class="size-1.5 rounded-full bg-tdl06-acc"></i><span class="@max-[41rem]/stage:hidden">3-column template</span><span class="hidden @max-[41rem]/stage:inline">2-column template</span></span>
      </header>
      <nav aria-label="Demo sidebar" class="flex flex-col gap-1.25 pt-8.5! [grid-area:sidebar] @max-[41rem]/stage:px-2! [&>a]:flex [&>a]:h-10 [&>a]:items-center [&>a]:gap-2.5 [&>a]:rounded-lg [&>a]:px-2.5 [&>a]:text-[12.5px] [&>a]:font-semibold [&>a]:whitespace-nowrap [&>a]:text-tdl06-mut [&>a]:no-underline [&>a]:transition-colors [&>a:hover]:bg-tdl06-acc/8 [&>a:hover]:text-tdl06-ink [&>a:focus-visible]:outline-2 [&>a:focus-visible]:-outline-offset-2 [&>a:focus-visible]:outline-tdl06-acc [&>a[aria-current=page]]:bg-tdl06-acc/12 [&>a[aria-current=page]]:text-tdl06-acc @max-[41rem]/stage:[&>a]:justify-center @max-[41rem]/stage:[&>a]:px-0 [&_i]:size-4 [&_i]:flex-none [&_i]:rounded-[5px] [&_i]:bg-tdl06-line/45 [&>a[aria-current=page]_i]:bg-tdl06-acc"><b>sidebar</b>
        <a href="#dash" aria-current="page"><i aria-hidden="true"></i><span class="@max-[41rem]/stage:sr-only">Dashboard</span></a>
        <a href="#reports"><i aria-hidden="true"></i><span class="@max-[41rem]/stage:sr-only">Reports</span></a>
        <a href="#team"><i aria-hidden="true"></i><span class="@max-[41rem]/stage:sr-only">Team</span></a>
        <a href="#settings"><i aria-hidden="true"></i><span class="@max-[41rem]/stage:sr-only">Settings</span></a>
      </nav>
      <main class="pt-9! [grid-area:main]"><b>main</b>
        <div aria-hidden="true" class="grid gap-3 *:block *:h-3.75 *:w-(--w) *:rounded-full *:bg-tdl06-line/25"><span style="--w:72%"></span><span style="--w:94%"></span><span style="--w:58%"></span><span style="--w:86%"></span><span style="--w:66%"></span></div>
        <div aria-hidden="true" class="mt-5 grid grid-cols-3 gap-3 *:h-16 *:rounded-lg *:border *:border-tdl06-line/25 *:bg-white/70"><span></span><span></span><span></span></div>
      </main>
      <aside class="flex flex-col gap-3.5 pt-9! [grid-area:aside] @max-[41rem]/stage:flex-row @max-[41rem]/stage:pt-8!"><b>aside</b>
        <p class="grid gap-1.75 text-xs font-semibold text-tdl06-mut @max-[41rem]/stage:flex-1">Quota · 64%<span class="h-2 overflow-hidden rounded-full bg-tdl06-line/22"><i class="block h-full w-[64%] rounded-full bg-linear-to-r from-tdl06-acc to-tdl06-line"></i></span></p>
        <p class="grid gap-1.75 text-xs font-semibold text-tdl06-mut @max-[41rem]/stage:flex-1">Storage · 38%<span class="h-2 overflow-hidden rounded-full bg-tdl06-line/22"><i class="block h-full w-[38%] rounded-full bg-linear-to-r from-tdl06-acc to-tdl06-line"></i></span></p>
      </aside>
      <footer class="flex items-center gap-3 overflow-hidden pl-22! [grid-area:footer]"><b>footer</b>
        <code class="truncate font-tdl06-mono text-[10.5px] font-semibold text-tdl06-mut @max-[41rem]/stage:hidden">'header header header' 'sidebar main aside' 'footer footer footer'</code>
        <code class="hidden truncate font-tdl06-mono text-[10.5px] font-semibold text-tdl06-mut @max-[41rem]/stage:block">'header header' 'sidebar main' 'aside aside' 'footer footer'</code>
      </footer>
    </div>
  </div>
  <p class="mt-2 flex items-center gap-2 text-xs font-semibold text-tdl06-mut"><span aria-hidden="true" class="font-tdl06-mono text-tdl06-acc">⤡</span>Drag the stage's bottom-right corner to cross the 41rem breakpoint</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl06-bg: #eef2f7;
  --color-tdl06-bg: oklch(0.96 0.01 245);
  --color-tdl06-paper: #f8fafc;
  --color-tdl06-paper: oklch(0.982 0.005 245);
  --color-tdl06-dot: #dbe3ee;
  --color-tdl06-dot: oklch(0.91 0.015 250);
  --color-tdl06-edge: #d8dfe9;
  --color-tdl06-edge: oklch(0.9 0.015 250);
  --color-tdl06-ink: #2b3445;
  --color-tdl06-ink: oklch(0.3 0.03 255);
  --color-tdl06-mut: #556079;
  --color-tdl06-mut: oklch(0.48 0.04 260);
  --color-tdl06-line: #4f7cc6;
  --color-tdl06-line: oklch(0.58 0.12 258);
  --color-tdl06-fill: #e9f0fb;
  --color-tdl06-fill: oklch(0.95 0.02 255);
  --color-tdl06-fill2: #f5f8fd;
  --color-tdl06-fill2: oklch(0.977 0.01 255);
  --color-tdl06-hover: #eef3fd;
  --color-tdl06-hover: oklch(0.965 0.018 260);
  --color-tdl06-acc: #2c5fd6;
  --color-tdl06-acc: oklch(0.53 0.18 262);
  --font-tdl06-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tdl06-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tdl-06 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tdl-06 * {
    transition: none !important;
  }
}
```
