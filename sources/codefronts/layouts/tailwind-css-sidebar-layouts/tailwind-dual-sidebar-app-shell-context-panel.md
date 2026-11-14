---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-dual-sidebar-app-shell-context-panel/"
title: "Tailwind Dual Sidebar App Shell with Left Nav and Context Panel"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The Notion/Discord-class shell: primary nav left, contextual panel right, content between."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dual Sidebar App Shell with Left Nav and Context Panel
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-dual-sidebar-app-shell-context-panel/

The Notion/Discord-class shell: primary nav left, contextual panel right, content between. The most valuable line in the demo is minmax(0,1fr) on the middle track &mdash; the answer to the most-asked grid question on the internet, and one that reads more clearly as a utility than as CSS.
## HTML
```html
<section class="tsl-13 w-full h-svh min-h-svh grid grid-cols-[232px_minmax(0,1fr)_280px] max-xl:grid-cols-[232px_minmax(0,1fr)] font-tsl13-sans bg-tsl13-bg text-tsl13-ink">
  <aside aria-label="Workspace" class="bg-tsl13-panel border-r border-tsl13-line px-2.5 py-4 overflow-y-auto">
    <div class="flex items-center gap-2.5 px-2.5 pt-0.5 pb-4 text-[14.5px] font-bold tracking-tight"><span aria-hidden="true" class="grid place-items-center w-[26px] h-[26px] rounded-lg text-xs font-bold text-white bg-[linear-gradient(135deg,var(--color-tsl13-accent),oklch(0.6_0.18_260))]">L</span>Loomcraft</div>
    <div class="px-2.5 pt-3.5 pb-1.5 text-[10.5px] font-semibold uppercase tracking-[0.09em] text-tsl13-mut">Projects</div>
    <nav class="flex flex-col gap-px">
      <a href="#" aria-current="page" class="flex items-center min-h-11 px-3 rounded-lg text-[13.5px] font-medium text-tsl13-mut no-underline transition-colors duration-150 hover:text-tsl13-ink hover:bg-tsl13-hover aria-[current=page]:text-tsl13-ink aria-[current=page]:bg-tsl13-tint focus-visible:outline-2 focus-visible:outline-tsl13-accent focus-visible:outline-offset-1"># brand-refresh <span class="ml-auto rounded-full px-[7px] py-[3px] text-[10.5px] font-bold text-white bg-tsl13-accent">3</span></a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-lg text-[13.5px] font-medium text-tsl13-mut no-underline transition-colors duration-150 hover:text-tsl13-ink hover:bg-tsl13-hover focus-visible:outline-2 focus-visible:outline-tsl13-accent focus-visible:outline-offset-1"># website-v4</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-lg text-[13.5px] font-medium text-tsl13-mut no-underline transition-colors duration-150 hover:text-tsl13-ink hover:bg-tsl13-hover focus-visible:outline-2 focus-visible:outline-tsl13-accent focus-visible:outline-offset-1"># mobile-app <span class="ml-auto rounded-full px-[7px] py-[3px] text-[10.5px] font-bold text-white bg-tsl13-accent">12</span></a>
    </nav>
    <div class="px-2.5 pt-3.5 pb-1.5 text-[10.5px] font-semibold uppercase tracking-[0.09em] text-tsl13-mut">Team</div>
    <nav class="flex flex-col gap-px">
      <a href="#" class="flex items-center min-h-11 px-3 rounded-lg text-[13.5px] font-medium text-tsl13-mut no-underline transition-colors duration-150 hover:text-tsl13-ink hover:bg-tsl13-hover focus-visible:outline-2 focus-visible:outline-tsl13-accent focus-visible:outline-offset-1"># design-crit</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-lg text-[13.5px] font-medium text-tsl13-mut no-underline transition-colors duration-150 hover:text-tsl13-ink hover:bg-tsl13-hover focus-visible:outline-2 focus-visible:outline-tsl13-accent focus-visible:outline-offset-1"># announcements</a>
    </nav>
  </aside>
  <main class="overflow-y-auto px-[34px] py-[30px] [scrollbar-gutter:stable]">
    <h1 class="mb-3 text-xl font-bold leading-tight"># brand-refresh</h1>
    <p class="max-w-[60ch] text-sm leading-[1.7] text-tsl13-mut text-pretty">The centre track is <code class="font-tsl13-mono text-[12.5px] px-1.5 py-0.5 rounded-[5px] bg-tsl13-hover text-tsl13-ink">minmax(0,1fr)</code> &mdash; wide content shrinks and scrolls instead of crushing the context panel. Narrow the window past 1280px: the right panel yields first, the nav survives.</p>
  </main>
  <aside aria-label="Activity" class="max-xl:hidden border-l border-tsl13-line bg-tsl13-panel px-4 py-5 overflow-y-auto">
    <h2 class="mb-4 text-xs font-semibold uppercase tracking-[0.08em] text-tsl13-mut">Activity</h2>
    <ol class="list-none m-0 p-0 grid">
      <li class="relative grid grid-cols-[28px_1fr] gap-3 pb-5 before:content-[''] before:absolute before:left-[13.5px] before:top-8 before:bottom-0.5 before:w-px before:bg-tsl13-line last:before:hidden"><span aria-hidden="true" class="grid place-items-center w-7 h-7 rounded-full text-[9.5px] font-bold text-white bg-[linear-gradient(135deg,oklch(0.6_0.15_300),oklch(0.55_0.15_240))]">PR</span><div class="text-[12.5px] leading-[1.5] text-tsl13-mut"><strong class="font-semibold text-tsl13-ink">Priya</strong> shipped the new wordmark<time class="block mt-0.5 text-[11px] text-tsl13-faint">2h ago</time></div></li>
      <li class="relative grid grid-cols-[28px_1fr] gap-3 pb-5 before:content-[''] before:absolute before:left-[13.5px] before:top-8 before:bottom-0.5 before:w-px before:bg-tsl13-line last:before:hidden"><span aria-hidden="true" class="grid place-items-center w-7 h-7 rounded-full text-[9.5px] font-bold text-white bg-[linear-gradient(135deg,oklch(0.6_0.15_300),oklch(0.55_0.15_240))]">MW</span><div class="text-[12.5px] leading-[1.5] text-tsl13-mut"><strong class="font-semibold text-tsl13-ink">Marcus</strong> commented on palette v3<time class="block mt-0.5 text-[11px] text-tsl13-faint">4h ago</time></div></li>
      <li class="relative grid grid-cols-[28px_1fr] gap-3 pb-5 before:content-[''] before:absolute before:left-[13.5px] before:top-8 before:bottom-0.5 before:w-px before:bg-tsl13-line last:before:hidden"><span aria-hidden="true" class="grid place-items-center w-7 h-7 rounded-full text-[9.5px] font-bold text-white bg-[linear-gradient(135deg,oklch(0.6_0.15_300),oklch(0.55_0.15_240))]">AO</span><div class="text-[12.5px] leading-[1.5] text-tsl13-mut"><strong class="font-semibold text-tsl13-ink">Amara</strong> uploaded 6 explorations<time class="block mt-0.5 text-[11px] text-tsl13-faint">Yesterday</time></div></li>
    </ol>
  </aside>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl13-bg: #16141c;
  --color-tsl13-bg: oklch(0.14 0.014 290);
  --color-tsl13-panel: #1c1a25;
  --color-tsl13-panel: oklch(0.17 0.018 290);
  --color-tsl13-ink: #e9e7ef;
  --color-tsl13-ink: oklch(0.93 0.005 290);
  --color-tsl13-mut: #99949f;
  --color-tsl13-mut: oklch(0.63 0.012 290);
  --color-tsl13-faint: #6f6b76;
  --color-tsl13-faint: oklch(0.5 0.01 290);
  --color-tsl13-line: #3a3545;
  --color-tsl13-line: oklch(0.28 0.018 290);
  --color-tsl13-accent: #b07ae8;
  --color-tsl13-accent: oklch(0.7 0.16 300);
  --color-tsl13-hover: rgb(233 231 239 / 0.06);
  --color-tsl13-hover: color-mix(in oklab, oklch(0.93 0.005 290) 6%, transparent);
  --color-tsl13-tint: rgb(176 122 232 / 0.17);
  --color-tsl13-tint: color-mix(in oklab, oklch(0.7 0.16 300) 17%, transparent);
  --font-tsl13-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsl13-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tsl-13 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
```
