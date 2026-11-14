---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-responsive-app-shell-layout/"
title: "Tailwind Material Design Responsive App Shell Layout"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "The whole thing assembled: a sticky top app bar that gains elevation on scroll, a navigation rail that becomes a modal drawer under md, and a dashboard grid…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Responsive App Shell Layout
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-responsive-app-shell-layout/

The whole thing assembled: a sticky top app bar that gains elevation on scroll, a navigation rail that becomes a modal drawer under md, and a dashboard grid of the earlier demos' components. Every M3 layout breakpoint is a Tailwind responsive modifier, and the only JavaScript is the drawer's focus management and one scroll listener.
## HTML
```html
<section class="tmd-14 w-full min-h-svh bg-tmd14-bg font-tmd14-sans text-tmd14-onsurface" aria-label="Material Design app shell demo">
  <div class="relative grid md:grid-cols-[80px_1fr] lg:grid-cols-[256px_1fr] min-h-svh">
    <nav aria-label="Main" class="hidden md:grid content-start gap-1 py-3 px-2 bg-tmd14-surface2 border-r border-tmd14-outlinevariant">
      <span class="hidden lg:block px-4 py-3 font-tmd14-mono text-[11px] uppercase tracking-[0.12em] text-tmd14-onvariant">Hydrolab</span>
      <a href="#dash" aria-current="page" class="relative overflow-hidden grid lg:grid-cols-[auto_1fr] justify-items-center lg:justify-items-start items-center gap-1 lg:gap-3 min-h-14 px-2 lg:px-4 rounded-full no-underline text-[11px] lg:text-sm font-medium text-tmd14-onvariant transition-colors duration-200 aria-[current=page]:bg-tmd14-secondarycontainer aria-[current=page]:text-tmd14-onsecondarycontainer focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd14-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd14-icon text-[22px] leading-none" aria-hidden="true">dashboard</span>Overview</a>
      <a href="#stations" class="relative overflow-hidden grid lg:grid-cols-[auto_1fr] justify-items-center lg:justify-items-start items-center gap-1 lg:gap-3 min-h-14 px-2 lg:px-4 rounded-full no-underline text-[11px] lg:text-sm font-medium text-tmd14-onvariant transition-colors duration-200 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd14-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd14-icon text-[22px] leading-none" aria-hidden="true">sensors</span>Stations</a>
      <a href="#reports" class="relative overflow-hidden grid lg:grid-cols-[auto_1fr] justify-items-center lg:justify-items-start items-center gap-1 lg:gap-3 min-h-14 px-2 lg:px-4 rounded-full no-underline text-[11px] lg:text-sm font-medium text-tmd14-onvariant transition-colors duration-200 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd14-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd14-icon text-[22px] leading-none" aria-hidden="true">bar_chart</span>Reports</a>
      <a href="#team" class="relative overflow-hidden grid lg:grid-cols-[auto_1fr] justify-items-center lg:justify-items-start items-center gap-1 lg:gap-3 min-h-14 px-2 lg:px-4 rounded-full no-underline text-[11px] lg:text-sm font-medium text-tmd14-onvariant transition-colors duration-200 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd14-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd14-icon text-[22px] leading-none" aria-hidden="true">group</span>Team</a>
    </nav>

    <div id="tmd14-main" class="grid grid-rows-[auto_1fr] min-w-0">
      <header data-bar class="sticky top-0 z-20 flex items-center gap-2 h-16 px-3 bg-tmd14-surface/85 backdrop-blur-sm border-b border-transparent transition-[box-shadow,border-color] duration-200 data-scrolled:shadow-tmd14-2 data-scrolled:border-tmd14-outlinevariant motion-reduce:transition-none">
        <button type="button" data-drawer-open aria-expanded="false" aria-controls="tmd14-drawer" aria-label="Open navigation" class="md:hidden relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd14-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd14-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd14-icon text-[22px] leading-none" aria-hidden="true">menu</span></button>
        <h2 class="text-[17px] font-medium">Overview</h2>
        <div class="ml-auto flex items-center gap-1">
          <button type="button" aria-label="Search" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd14-onvariant focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd14-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd14-icon text-[22px] leading-none" aria-hidden="true">search</span></button>
          <span class="relative inline-block"><button type="button" aria-label="Alerts, 3 unread" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd14-onvariant focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd14-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd14-icon text-[22px] leading-none" aria-hidden="true">notifications</span></button><span class="absolute top-1 right-1 min-w-4 h-4 px-1 grid place-items-center rounded-full bg-tmd14-error text-white font-tmd14-mono text-[10px] pointer-events-none" aria-hidden="true">3</span></span>
          <span class="grid place-items-center w-9 h-9 ml-1 rounded-full bg-tmd14-primary text-white font-tmd14-mono text-xs" aria-hidden="true">MK</span>
        </div>
      </header>

      <main class="grid content-start gap-4 p-4 md:p-6">
        <div class="grid gap-4 grid-cols-[repeat(auto-fit,minmax(min(240px,100%),1fr))]">
          <article class="grid gap-1 p-5 rounded-3xl bg-tmd14-surface shadow-tmd14-1"><span class="font-tmd14-mono text-[11px] uppercase tracking-[0.08em] text-tmd14-onvariant">Stations online</span><b class="text-[32px] font-medium leading-tight tabular-nums">16<span class="text-base text-tmd14-onvariant"> / 18</span></b><div class="h-1 mt-2 rounded-full bg-tmd14-outlinevariant overflow-hidden"><div class="h-full w-[89%] rounded-full bg-tmd14-primary"></div></div></article>
          <article class="grid gap-1 p-5 rounded-3xl bg-tmd14-surface shadow-tmd14-1"><span class="font-tmd14-mono text-[11px] uppercase tracking-[0.08em] text-tmd14-onvariant">Readings today</span><b class="text-[32px] font-medium leading-tight tabular-nums">4 210</b><span class="text-xs text-tmd14-onvariant">+6.2% on yesterday</span></article>
          <article class="grid gap-1 p-5 rounded-3xl bg-tmd14-secondarycontainer text-tmd14-onsecondarycontainer"><span class="font-tmd14-mono text-[11px] uppercase tracking-[0.08em] opacity-80">Open alerts</span><b class="text-[32px] font-medium leading-tight tabular-nums">3</b><span class="text-xs opacity-80">1 offline &middot; 2 drift</span></article>
        </div>

        <div class="grid gap-4 lg:grid-cols-[1.4fr_1fr]">
          <article class="grid content-start gap-3 p-5 rounded-3xl bg-tmd14-surface shadow-tmd14-1">
            <div class="flex items-baseline justify-between gap-3"><b class="text-[15px] font-medium">Depth coverage</b><span class="font-tmd14-mono text-[11px] text-tmd14-onvariant">last 7 days</span></div>
            <div class="grid grid-cols-7 items-end gap-2 h-40" role="img" aria-label="Bar chart of depth coverage over seven days">
              <div class="h-[62%] rounded-t-lg bg-tmd14-primary/85"></div>
              <div class="h-[74%] rounded-t-lg bg-tmd14-primary/85"></div>
              <div class="h-[48%] rounded-t-lg bg-tmd14-primary/85"></div>
              <div class="h-[86%] rounded-t-lg bg-tmd14-primary/85"></div>
              <div class="h-[70%] rounded-t-lg bg-tmd14-primary/85"></div>
              <div class="h-[92%] rounded-t-lg bg-tmd14-primary"></div>
              <div class="h-[58%] rounded-t-lg bg-tmd14-primary/40"></div>
            </div>
          </article>
          <article class="grid content-start gap-2 p-5 rounded-3xl bg-tmd14-surface shadow-tmd14-1">
            <b class="text-[15px] font-medium">Recent activity</b>
            <ul role="list" class="list-none m-0 p-0 divide-y divide-tmd14-outlinevariant">
              <li class="grid grid-cols-[auto_1fr_auto] items-center gap-3 min-h-14"><span class="grid place-items-center w-9 h-9 rounded-full bg-tmd14-surface2 font-tmd14-icon text-[18px] leading-none text-tmd14-onvariant" aria-hidden="true">warning</span><span class="min-w-0 text-sm truncate">ST-047 went offline</span><small class="font-tmd14-mono text-[11px] text-tmd14-onvariant">12m</small></li>
              <li class="grid grid-cols-[auto_1fr_auto] items-center gap-3 min-h-14"><span class="grid place-items-center w-9 h-9 rounded-full bg-tmd14-surface2 font-tmd14-icon text-[18px] leading-none text-tmd14-onvariant" aria-hidden="true">check_circle</span><span class="min-w-0 text-sm truncate">ST-031 recalibrated</span><small class="font-tmd14-mono text-[11px] text-tmd14-onvariant">1h</small></li>
              <li class="grid grid-cols-[auto_1fr_auto] items-center gap-3 min-h-14"><span class="grid place-items-center w-9 h-9 rounded-full bg-tmd14-surface2 font-tmd14-icon text-[18px] leading-none text-tmd14-onvariant" aria-hidden="true">cloud_done</span><span class="min-w-0 text-sm truncate">Nightly sync complete</span><small class="font-tmd14-mono text-[11px] text-tmd14-onvariant">6h</small></li>
            </ul>
          </article>
        </div>
        <p class="text-xs text-tmd14-onvariant">Resize the frame: single column below <span class="font-tmd14-mono">md</span>, 80px rail at <span class="font-tmd14-mono">md</span>, 256px drawer at <span class="font-tmd14-mono">lg</span>. Scroll to elevate the bar.</p>
        <div class="h-40" aria-hidden="true"></div>
      </main>
    </div>

    <button type="button" data-scrim tabindex="-1" aria-label="Close navigation" class="md:hidden fixed inset-0 z-30 hidden border-0 bg-black/40 cursor-pointer data-open:block"></button>
    <nav id="tmd14-drawer" aria-label="Navigation drawer" class="md:hidden fixed inset-y-0 left-0 z-40 grid content-start gap-1 w-70 py-3 px-2 bg-tmd14-surface2 [transform:translateX(-100%)] transition-transform duration-300 ease-out data-open:[transform:translateX(0)] motion-reduce:transition-none">
      <div class="flex items-center gap-2 px-2 py-2">
        <button type="button" data-drawer-close aria-label="Close navigation" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd14-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd14-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd14-icon text-[22px] leading-none" aria-hidden="true">close</span></button>
        <span class="font-tmd14-mono text-[11px] uppercase tracking-[0.12em] text-tmd14-onvariant">Hydrolab</span>
      </div>
      <a href="#dash" aria-current="page" class="relative overflow-hidden flex items-center gap-3 min-h-14 px-4 rounded-full no-underline text-sm font-medium text-tmd14-onvariant aria-[current=page]:bg-tmd14-secondarycontainer aria-[current=page]:text-tmd14-onsecondarycontainer focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd14-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd14-icon text-[22px] leading-none" aria-hidden="true">dashboard</span>Overview</a>
      <a href="#stations" class="relative overflow-hidden flex items-center gap-3 min-h-14 px-4 rounded-full no-underline text-sm font-medium text-tmd14-onvariant focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd14-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd14-icon text-[22px] leading-none" aria-hidden="true">sensors</span>Stations</a>
      <a href="#reports" class="relative overflow-hidden flex items-center gap-3 min-h-14 px-4 rounded-full no-underline text-sm font-medium text-tmd14-onvariant focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd14-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd14-icon text-[22px] leading-none" aria-hidden="true">bar_chart</span>Reports</a>
      <a href="#team" class="relative overflow-hidden flex items-center gap-3 min-h-14 px-4 rounded-full no-underline text-sm font-medium text-tmd14-onvariant focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd14-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd14-icon text-[22px] leading-none" aria-hidden="true">group</span>Team</a>
    </nav>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd14-bg: #eef1f6;
  --color-tmd14-bg: oklch(0.957 0.007 260.7);
  --color-tmd14-surface: #ffffff;
  --color-tmd14-surface: oklch(1 0 89.9);
  --color-tmd14-surface2: #f4f6fa;
  --color-tmd14-surface2: oklch(0.973 0.006 264.5);
  --color-tmd14-primary: #1565c0;
  --color-tmd14-primary: oklch(0.513 0.16 255.7);
  --color-tmd14-secondarycontainer: #dbe7f7;
  --color-tmd14-secondarycontainer: oklch(0.924 0.025 255.6);
  --color-tmd14-onsecondarycontainer: #0a2a4a;
  --color-tmd14-onsecondarycontainer: oklch(0.281 0.07 251.8);
  --color-tmd14-onsurface: #1c1b1f;
  --color-tmd14-onsurface: oklch(0.225 0.008 297.2);
  --color-tmd14-onvariant: #4d5966;
  --color-tmd14-onvariant: oklch(0.459 0.026 250.5);
  --color-tmd14-outlinevariant: #dde1e7;
  --color-tmd14-outlinevariant: oklch(0.908 0.009 258.3);
  --color-tmd14-error: #b3261e;
  --color-tmd14-error: oklch(0.501 0.178 28.7);
  --font-tmd14-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd14-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd14-icon: 'Material Symbols Outlined';
  --shadow-tmd14-1: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 1px 3px 1px rgb(0 0 0 / 0.15);
  --shadow-tmd14-2: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 2px 6px 2px rgb(0 0 0 / 0.15);
}

.tmd-14 {
  width: 100%;
  min-height: 100svh;
}

.tmd-14 .font-tmd14-icon {
  font-feature-settings: 'liga';
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tmd-14').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var btn = root.querySelector('[data-drawer-open]'),
        closeBtn = root.querySelector('[data-drawer-close]'),
        drawer = root.querySelector('#tmd14-drawer'),
        scrim = root.querySelector('[data-scrim]'),
        main = root.querySelector('#tmd14-main'),
        bar = root.querySelector('[data-bar]'),
        scroller = root.closest('[data-scroll-root]') || document.scrollingElement;

    function set(open) {
      drawer.toggleAttribute('data-open', open);
      scrim.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      if (open) { main.setAttribute('inert', ''); drawer.querySelector('a').focus(); }
      else { main.removeAttribute('inert'); btn.focus(); }
    }
    btn.addEventListener('click', function () { set(true); });
    closeBtn.addEventListener('click', function () { set(false); });
    scrim.addEventListener('click', function () { set(false); });
    root.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.hasAttribute('data-open')) set(false);
    });

    function onScroll() {
      var y = scroller === document.scrollingElement ? window.scrollY : scroller.scrollTop;
      bar.toggleAttribute('data-scrolled', y > 4);
    }
    (scroller === document.scrollingElement ? window : scroller).addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  });
})();
```
