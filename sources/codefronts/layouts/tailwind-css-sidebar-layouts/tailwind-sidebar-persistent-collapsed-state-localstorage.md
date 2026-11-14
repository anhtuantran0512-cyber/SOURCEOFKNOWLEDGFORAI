---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-sidebar-persistent-collapsed-state-localstorage/"
title: "Tailwind Sidebar with Persistent Collapsed State in localStorage"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The collapse that survives a refresh."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sidebar with Persistent Collapsed State in localStorage
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-sidebar-persistent-collapsed-state-localstorage/

The collapse that survives a refresh. Geometry derives from one --w variable that a data-state attribute swaps; six lines of JavaScript move a string between localStorage and that attribute, restored before first paint so returning users never see the wrong-width flash.
## HTML
```html
<section id="tsl20" data-state="expanded" class="tsl-20 group/rail w-full h-svh min-h-svh grid grid-cols-[var(--w)_1fr] [--w:264px] data-[state=collapsed]:[--w:72px] transition-[grid-template-columns] duration-300 ease-[cubic-bezier(.4,0,.2,1)] font-tsl20-sans bg-tsl20-bg text-tsl20-ink motion-reduce:transition-none">
  <aside class="flex flex-col gap-0.5 px-3 py-4 bg-tsl20-panel border-r border-tsl20-line overflow-hidden">
    <div class="grid grid-cols-[26px_1fr] items-center gap-[11px] px-2.5 pt-1 pb-[18px] whitespace-nowrap">
      <span aria-hidden="true" class="w-[26px] h-[26px] rounded-lg bg-[conic-gradient(from_160deg,var(--color-tsl20-accent),oklch(0.6_0.15_250))]"></span>
      <span class="text-[15px] font-bold tracking-tight opacity-100 transition-opacity duration-[180ms] delay-[100ms] group-data-[state=collapsed]/rail:opacity-0">Keystone</span>
    </div>
    <nav aria-label="Main" class="flex flex-col gap-0.5">
      <a href="#" aria-current="page" class="grid grid-cols-[19px_1fr] items-center gap-3 min-h-11 px-3.5 rounded-[10px] text-sm font-medium whitespace-nowrap text-tsl20-mut no-underline transition-colors duration-200 hover:text-tsl20-ink hover:bg-tsl20-hover aria-[current=page]:text-tsl20-accent aria-[current=page]:bg-tsl20-tint focus-visible:outline-2 focus-visible:outline-tsl20-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><rect x="3" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.5"/></svg><span class="opacity-100 transition-opacity duration-[180ms] delay-[100ms] group-data-[state=collapsed]/rail:opacity-0">Home</span></a>
      <a href="#" class="grid grid-cols-[19px_1fr] items-center gap-3 min-h-11 px-3.5 rounded-[10px] text-sm font-medium whitespace-nowrap text-tsl20-mut no-underline transition-colors duration-200 hover:text-tsl20-ink hover:bg-tsl20-hover focus-visible:outline-2 focus-visible:outline-tsl20-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M4 20V10m6 10V4m6 16v-7"/></svg><span class="opacity-100 transition-opacity duration-[180ms] delay-[100ms] group-data-[state=collapsed]/rail:opacity-0">Metrics</span></a>
      <a href="#" class="grid grid-cols-[19px_1fr] items-center gap-3 min-h-11 px-3.5 rounded-[10px] text-sm font-medium whitespace-nowrap text-tsl20-mut no-underline transition-colors duration-200 hover:text-tsl20-ink hover:bg-tsl20-hover focus-visible:outline-2 focus-visible:outline-tsl20-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span class="opacity-100 transition-opacity duration-[180ms] delay-[100ms] group-data-[state=collapsed]/rail:opacity-0">Files</span></a>
      <a href="#" class="grid grid-cols-[19px_1fr] items-center gap-3 min-h-11 px-3.5 rounded-[10px] text-sm font-medium whitespace-nowrap text-tsl20-mut no-underline transition-colors duration-200 hover:text-tsl20-ink hover:bg-tsl20-hover focus-visible:outline-2 focus-visible:outline-tsl20-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg><span class="opacity-100 transition-opacity duration-[180ms] delay-[100ms] group-data-[state=collapsed]/rail:opacity-0">Settings</span></a>
    </nav>
    <button type="button" aria-expanded="true" aria-controls="tsl20" class="tsl-20-toggle mt-auto grid grid-cols-[19px_1fr] items-center gap-3 min-h-11 px-3.5 rounded-[10px] border-0 bg-transparent text-left text-sm font-medium whitespace-nowrap text-tsl20-mut cursor-pointer transition-colors duration-200 hover:text-tsl20-ink hover:bg-tsl20-hover focus-visible:outline-2 focus-visible:outline-tsl20-accent focus-visible:outline-offset-2">
      <svg viewBox="0 0 24 24" aria-hidden="true" class="w-[19px] h-[19px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-300 group-data-[state=collapsed]/rail:rotate-180 motion-reduce:transition-none"><path d="m14 6-6 6 6 6"/></svg>
      <span class="opacity-100 transition-opacity duration-[180ms] delay-[100ms] group-data-[state=collapsed]/rail:opacity-0">Collapse</span>
    </button>
  </aside>
  <main class="p-8 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">Home</h1>
    <p class="max-w-[47ch] text-sm leading-relaxed text-tsl20-mut text-pretty">Collapse the rail, then reload the page &mdash; the state restores from localStorage before first paint. No wrong-width flash.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl20-bg: #101617;
  --color-tsl20-bg: oklch(0.13 0.012 195);
  --color-tsl20-panel: #161f21;
  --color-tsl20-panel: oklch(0.17 0.015 195);
  --color-tsl20-ink: #e8eff0;
  --color-tsl20-ink: oklch(0.94 0.005 195);
  --color-tsl20-mut: #929d9e;
  --color-tsl20-mut: oklch(0.64 0.012 195);
  --color-tsl20-line: #333e40;
  --color-tsl20-line: oklch(0.28 0.016 195);
  --color-tsl20-accent: #5cd6d3;
  --color-tsl20-accent: oklch(0.78 0.13 185);
  --color-tsl20-hover: rgb(232 239 240 / 0.07);
  --color-tsl20-hover: color-mix(in oklab, oklch(0.94 0.005 195) 7%, transparent);
  --color-tsl20-tint: rgb(92 214 211 / 0.14);
  --color-tsl20-tint: color-mix(in oklab, oklch(0.78 0.13 185) 14%, transparent);
  --font-tsl20-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-20 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
```

## JavaScript
```js
(() => {
  const KEY = 'tsl20-sidebar';
  const shell = document.getElementById('tsl20');
  const btn = shell?.querySelector('.tsl-20-toggle');
  if (!shell || !btn) return;
  // Restore before paint: in production, inline this expression in a <script> right after the shell's opening tag.
  let saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  if (saved === 'collapsed' || saved === 'expanded') apply(saved);
  btn.addEventListener('click', () => {
    apply(shell.dataset.state === 'expanded' ? 'collapsed' : 'expanded');
  });
  function apply(state) {
    shell.dataset.state = state;                              // utilities read this
    btn.setAttribute('aria-expanded', String(state === 'expanded')); // AT reads this
    try { localStorage.setItem(KEY, state); } catch (e) {}    // tomorrow reads this
  }
})();
```
