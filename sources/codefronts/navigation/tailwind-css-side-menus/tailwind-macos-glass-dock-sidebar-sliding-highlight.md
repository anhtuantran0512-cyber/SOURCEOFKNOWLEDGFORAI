---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-macos-glass-dock-sidebar-sliding-highlight/"
title: "Tailwind macOS-Style Glass Dock Sidebar with Sliding Highlight"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "A floating vertical dock in dark frosted glass: icons at rest, labels springing open on hover or focus, and a glowing highlight pill that slides to whichever…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind macOS-Style Glass Dock Sidebar with Sliding Highlight
Source: https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-macos-glass-dock-sidebar-sliding-highlight/

A floating vertical dock in dark frosted glass: icons at rest, labels springing open on hover or focus, and a glowing highlight pill that slides to whichever item you point at. The port makes the dock actually work — clicking an item moves aria-current, updates the page title and parks the highlight there; arrow keys move focus up and down the dock.
## HTML
```html
<section class="tsm-17 flex w-full min-h-svh items-center gap-8 bg-[radial-gradient(120%_120%_at_10%_10%,var(--color-tsm17-bg1),var(--color-tsm17-bg2)_70%)] p-6 font-tsm17-sans text-white" aria-label="macOS-style glass dock sidebar demo">
  <nav data-tsm17-dock aria-label="Primary" class="group/dock relative isolate flex w-[66px] shrink-0 flex-col gap-1.5 overflow-hidden rounded-[22px] border border-white/16 bg-white/8 p-3 shadow-[inset_0_1px_0_oklch(1_0_0/0.28),0_30px_60px_-28px_oklch(0_0_0/0.8)] backdrop-blur-[22px] backdrop-saturate-160 transition-[width] duration-500 ease-[cubic-bezier(0.34,1.35,0.5,1)] hover:w-[210px] focus-within:w-[210px] motion-reduce:transition-none">
    <span data-hl aria-hidden="true" class="pointer-events-none absolute top-0 right-3 left-3 h-11 translate-y-[var(--tsm17-y,12px)] rounded-xl bg-tsm17-acc/70 shadow-[0_6px_18px_-6px_var(--color-tsm17-acc)] transition-[translate] duration-400 ease-[cubic-bezier(0.34,1.35,0.5,1)] motion-reduce:transition-none"></span>
    <a href="#" class="group/it relative z-10 flex min-h-11 items-center gap-3.5 rounded-xl px-3 text-[14.5px] font-semibold whitespace-nowrap text-white/80 transition-colors hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white aria-[current=page]:text-white" aria-current="page"><svg class="size-5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V20h14V9.5"/><path d="M10 20v-6h4v6"/></svg><span class="max-w-0 overflow-hidden opacity-0 transition-[max-width,opacity] duration-500 ease-[cubic-bezier(0.34,1.35,0.5,1)] group-hover/dock:max-w-32 group-hover/dock:opacity-100 group-focus-within/dock:max-w-32 group-focus-within/dock:opacity-100 motion-reduce:transition-none">Dashboard</span></a>
    <a href="#" class="group/it relative z-10 flex min-h-11 items-center gap-3.5 rounded-xl px-3 text-[14.5px] font-semibold whitespace-nowrap text-white/80 transition-colors hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white aria-[current=page]:text-white"><svg class="size-5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/></svg><span class="max-w-0 overflow-hidden opacity-0 transition-[max-width,opacity] duration-500 ease-[cubic-bezier(0.34,1.35,0.5,1)] group-hover/dock:max-w-32 group-hover/dock:opacity-100 group-focus-within/dock:max-w-32 group-focus-within/dock:opacity-100 motion-reduce:transition-none">Analytics</span></a>
    <a href="#" class="group/it relative z-10 flex min-h-11 items-center gap-3.5 rounded-xl px-3 text-[14.5px] font-semibold whitespace-nowrap text-white/80 transition-colors hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white aria-[current=page]:text-white"><svg class="size-5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span class="max-w-0 overflow-hidden opacity-0 transition-[max-width,opacity] duration-500 ease-[cubic-bezier(0.34,1.35,0.5,1)] group-hover/dock:max-w-32 group-hover/dock:opacity-100 group-focus-within/dock:max-w-32 group-focus-within/dock:opacity-100 motion-reduce:transition-none">Projects</span></a>
    <a href="#" class="group/it relative z-10 flex min-h-11 items-center gap-3.5 rounded-xl px-3 text-[14.5px] font-semibold whitespace-nowrap text-white/80 transition-colors hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white aria-[current=page]:text-white"><svg class="size-5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg><span class="max-w-0 overflow-hidden opacity-0 transition-[max-width,opacity] duration-500 ease-[cubic-bezier(0.34,1.35,0.5,1)] group-hover/dock:max-w-32 group-hover/dock:opacity-100 group-focus-within/dock:max-w-32 group-focus-within/dock:opacity-100 motion-reduce:transition-none">Messages</span></a>
    <a href="#" class="group/it relative z-10 flex min-h-11 items-center gap-3.5 rounded-xl px-3 text-[14.5px] font-semibold whitespace-nowrap text-white/80 transition-colors hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white aria-[current=page]:text-white"><svg class="size-5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h9"/><path d="M19 6h1"/><circle cx="16" cy="6" r="2.5"/><path d="M4 12h2"/><path d="M12 12h8"/><circle cx="9" cy="12" r="2.5"/><path d="M4 18h11"/><circle cx="18" cy="18" r="2.5"/></svg><span class="max-w-0 overflow-hidden opacity-0 transition-[max-width,opacity] duration-500 ease-[cubic-bezier(0.34,1.35,0.5,1)] group-hover/dock:max-w-32 group-hover/dock:opacity-100 group-focus-within/dock:max-w-32 group-focus-within/dock:opacity-100 motion-reduce:transition-none">Settings</span></a>
  </nav>
  <div class="min-w-0">
    <p class="text-xs font-semibold tracking-[0.14em] text-white/60 uppercase">Current page</p>
    <h1 data-tsm17-title class="mt-1 text-[clamp(28px,5vw,44px)] font-bold tracking-tight">Dashboard</h1>
    <p class="mt-2 max-w-xs text-sm leading-relaxed text-white/70 text-pretty">Hover or Tab into the dock. Click an item — or use the arrow keys — and the highlight slides with you.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm17-bg1: #1e1b3a;
  --color-tsm17-bg1: oklch(0.243 0.058 285.7);
  --color-tsm17-bg2: #0b0a17;
  --color-tsm17-bg2: oklch(0.154 0.027 286.2);
  --color-tsm17-acc: #7b6cf6;
  --color-tsm17-acc: oklch(0.617 0.199 283.8);
  --font-tsm17-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-17 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tsm17-dock]').forEach((dock) => {
    if (dock.dataset.wired) return;
    dock.dataset.wired = '1';
    const hl = dock.querySelector('[data-hl]');
    const items = [...dock.querySelectorAll('a')];
    const title = dock.closest('.tsm-17')?.querySelector('[data-tsm17-title]');
    const current = () => dock.querySelector('[aria-current="page"]') || items[0];
    const move = (el) => hl.style.setProperty('--tsm17-y', el.offsetTop + 'px');
    // The browser build compiles after this runs, so re-measure once styles, fonts and size settle.
    const home = () => { if (!dock.matches(':hover, :focus-within')) move(current()); };
    home();
    window.addEventListener('load', home);
    if (window.ResizeObserver) new ResizeObserver(home).observe(dock);
    items.forEach((it, i) => {
      it.addEventListener('pointerenter', () => move(it));
      it.addEventListener('focus', () => move(it));
      it.addEventListener('click', (e) => {
        e.preventDefault();
        current().removeAttribute('aria-current');
        it.setAttribute('aria-current', 'page');
        if (title) title.textContent = it.textContent.trim();
        move(it);
      });
      it.addEventListener('keydown', (e) => {
        const d = e.key === 'ArrowDown' ? 1 : e.key === 'ArrowUp' ? -1 : 0;
        if (!d) return;
        e.preventDefault();
        items[(i + d + items.length) % items.length].focus();
      });
    });
    dock.addEventListener('pointerleave', () => move(current()));
    dock.addEventListener('focusout', (e) => { if (!dock.contains(e.relatedTarget)) move(current()); });
  });
})();
```
