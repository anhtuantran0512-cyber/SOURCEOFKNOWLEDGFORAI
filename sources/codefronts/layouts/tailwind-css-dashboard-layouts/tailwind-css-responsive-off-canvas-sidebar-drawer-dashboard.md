---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-responsive-off-canvas-sidebar-drawer-dashboard/"
title: "Tailwind CSS Responsive Off-Canvas Sidebar Drawer Dashboard"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "One markup, two behaviours, side by side: in a wide panel the sidebar sits in-flow; in the phone frame @max-[35rem]/app: turns it into an off-canvas drawer…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Responsive Off-Canvas Sidebar Drawer Dashboard
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-responsive-off-canvas-sidebar-drawer-dashboard/

One markup, two behaviours, side by side: in a wide panel the sidebar sits in-flow; in the phone frame @max-[35rem]/app: turns it into an off-canvas drawer with a blurred click-to-close backdrop. One data-open attribute drives the slide (group-data-open/app:translate-x-0). The script now does what the CSS original only promised in a comment: inert on the closed drawer, focus moved in on open and restored on close, plus Esc and a close button.
## HTML
```html
<section class="tdl-07 grid w-full min-h-svh place-items-center bg-tdl07-bg p-4 font-tdl07-sans text-tdl07-ink antialiased sm:p-6" aria-label="Off-canvas drawer demo — same component at two container widths">
  <div class="flex w-full max-w-6xl flex-wrap items-start justify-center gap-6">
    <figure class="grid min-w-0 flex-[1_1_38rem] gap-2.5">
      <figcaption class="flex items-center gap-2 text-[11px] font-bold tracking-[0.09em] text-tdl07-mut uppercase"><span class="rounded-full bg-tdl07-acc/12 px-2 py-0.5 text-tdl07-acc">≥ 35rem</span>Sidebar in-flow</figcaption>
      <div data-app class="group/app @container/app relative flex h-[min(30rem,80svh)] overflow-hidden rounded-[18px] border border-tdl07-edge bg-tdl07-bg shadow-[0_20px_44px_-28px_var(--color-tdl07-shadow)]">
        <div data-veil aria-hidden="true" class="invisible absolute inset-0 z-10 bg-tdl07-veil/45 opacity-0 backdrop-blur-[2px] transition-[opacity,visibility] duration-300 group-data-open/app:visible group-data-open/app:opacity-100"></div>
        <nav id="tdl07-nav-a" aria-label="Primary" class="z-20 flex w-55 flex-none flex-col gap-1 bg-tdl07-side p-3 pt-4 text-tdl07-sideink transition-transform duration-300 ease-[cubic-bezier(.2,.7,.2,1)] @max-[35rem]/app:absolute @max-[35rem]/app:inset-y-0 @max-[35rem]/app:left-0 @max-[35rem]/app:w-[min(80%,18rem)] @max-[35rem]/app:-translate-x-[105%] @max-[35rem]/app:shadow-[0_0_60px_oklch(0_0_0/0.35)] @max-[35rem]/app:group-data-open/app:translate-x-0 [&>a]:flex [&>a]:min-h-11 [&>a]:items-center [&>a]:rounded-xl [&>a]:px-3 [&>a]:text-[14px] [&>a]:font-medium [&>a]:text-tdl07-sidemut [&>a]:no-underline [&>a]:transition-colors [&>a:hover]:bg-tdl07-sidehover [&>a:hover]:text-white [&>a:focus-visible]:outline-2 [&>a:focus-visible]:-outline-offset-2 [&>a:focus-visible]:outline-tdl07-glow [&>a[aria-current=page]]:bg-tdl07-sideon [&>a[aria-current=page]]:text-white [&>a[aria-current=page]]:shadow-[inset_3px_0_0_var(--color-tdl07-glow)]">
          <div class="mb-3.5 flex items-center justify-between px-2.5"><strong class="flex items-center gap-2.5 text-[15px] font-semibold"><span aria-hidden="true" class="size-5 rounded-md bg-[conic-gradient(from_210deg,var(--color-tdl07-glow),var(--color-tdl07-lime),var(--color-tdl07-glow))]"></span>Fieldkit</strong>
            <button data-close type="button" aria-label="Close navigation" class="hidden size-11 place-items-center rounded-xl text-tdl07-sidemut transition-colors hover:bg-tdl07-sidehover hover:text-white focus-visible:outline-2 focus-visible:outline-tdl07-glow @max-[35rem]/app:grid"><svg viewBox="0 0 24 24" class="size-4.5 fill-none stroke-current stroke-2 [stroke-linecap:round]" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button></div>
          <a href="#home" aria-current="page">Home</a><a href="#jobs">Jobs</a><a href="#crew">Crew</a><a href="#invoices">Invoices</a><a href="#settings">Settings</a>
        </nav>
        <div class="flex min-w-0 flex-1 flex-col">
          <header class="flex h-15 flex-none items-center gap-3 border-b border-tdl07-edge bg-tdl07-panel px-3">
            <button data-burger type="button" aria-expanded="false" aria-controls="tdl07-nav-a" aria-label="Open navigation" class="hidden size-11 place-items-center rounded-xl text-tdl07-ink transition-colors hover:bg-tdl07-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdl07-acc @max-[35rem]/app:grid"><svg viewBox="0 0 24 24" class="size-4.5 fill-none stroke-current stroke-2 [stroke-linecap:round]" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg></button>
            <h2 class="pl-1 text-base font-semibold tracking-tight">Today's jobs</h2><span class="rounded-full bg-tdl07-acc/12 px-2.25 py-0.75 text-[11px] font-bold text-tdl07-acc">6</span>
          </header>
          <div class="grid min-h-0 content-start gap-2.5 overflow-y-auto overscroll-contain p-3.5 [&>article]:grid [&>article]:grid-cols-[minmax(0,1fr)_auto] [&>article]:items-center [&>article]:gap-x-2.5 [&>article]:gap-y-0.5 [&>article]:rounded-xl [&>article]:border [&>article]:border-tdl07-edge [&>article]:bg-tdl07-panel [&>article]:px-3.75 [&>article]:py-3.25 [&_b]:truncate [&_b]:text-sm [&_b]:font-semibold [&_span]:col-start-1 [&_span]:text-xs [&_span]:text-tdl07-mut [&_i]:col-start-2 [&_i]:row-span-2 [&_i]:row-start-1 [&_i]:rounded-full [&_i]:border [&_i]:px-2.5 [&_i]:py-1 [&_i]:text-[10.5px] [&_i]:font-bold [&_i]:tracking-[0.04em] [&_i]:not-italic">
            <article><b>Deck repair — Hartley</b><span>08:30 · Crew A</span><i class="border-tdl07-acc/40 bg-tdl07-acc/10 text-tdl07-acc">On site</i></article>
            <article><b>Gutter install — Novak</b><span>10:00 · Crew B</span><i class="border-tdl07-edge bg-tdl07-bg text-tdl07-mut">Scheduled</i></article>
            <article><b>Fence quote — Ellis</b><span>13:30 · Sam</span><i class="border-tdl07-edge bg-tdl07-bg text-tdl07-mut">Scheduled</i></article>
            <article><b>Roof check — Winter Rd</b><span>15:00 · Crew A</span><i class="border-tdl07-hold/40 bg-tdl07-hold/10 text-tdl07-holdink">Weather hold</i></article>
          </div>
        </div>
      </div>
    </figure>
    <figure class="grid w-[19rem] max-w-full flex-none gap-2.5">
      <figcaption class="flex items-center gap-2 text-[11px] font-bold tracking-[0.09em] text-tdl07-mut uppercase"><span class="rounded-full bg-tdl07-acc/12 px-2 py-0.5 text-tdl07-acc">&lt; 35rem</span>Off-canvas drawer</figcaption>
      <div data-app class="group/app @container/app relative flex h-[min(30rem,80svh)] overflow-hidden rounded-[28px] border-[6px] border-tdl07-frame bg-tdl07-bg shadow-[0_20px_44px_-24px_var(--color-tdl07-shadow)]">
        <div data-veil aria-hidden="true" class="invisible absolute inset-0 z-10 bg-tdl07-veil/45 opacity-0 backdrop-blur-[2px] transition-[opacity,visibility] duration-300 group-data-open/app:visible group-data-open/app:opacity-100"></div>
        <nav id="tdl07-nav-b" aria-label="Primary" class="z-20 flex w-55 flex-none flex-col gap-1 bg-tdl07-side p-3 pt-4 text-tdl07-sideink transition-transform duration-300 ease-[cubic-bezier(.2,.7,.2,1)] @max-[35rem]/app:absolute @max-[35rem]/app:inset-y-0 @max-[35rem]/app:left-0 @max-[35rem]/app:w-[min(80%,18rem)] @max-[35rem]/app:-translate-x-[105%] @max-[35rem]/app:shadow-[0_0_60px_oklch(0_0_0/0.35)] @max-[35rem]/app:group-data-open/app:translate-x-0 [&>a]:flex [&>a]:min-h-11 [&>a]:items-center [&>a]:rounded-xl [&>a]:px-3 [&>a]:text-[14px] [&>a]:font-medium [&>a]:text-tdl07-sidemut [&>a]:no-underline [&>a]:transition-colors [&>a:hover]:bg-tdl07-sidehover [&>a:hover]:text-white [&>a:focus-visible]:outline-2 [&>a:focus-visible]:-outline-offset-2 [&>a:focus-visible]:outline-tdl07-glow [&>a[aria-current=page]]:bg-tdl07-sideon [&>a[aria-current=page]]:text-white [&>a[aria-current=page]]:shadow-[inset_3px_0_0_var(--color-tdl07-glow)]">
          <div class="mb-3.5 flex items-center justify-between px-2.5"><strong class="flex items-center gap-2.5 text-[15px] font-semibold"><span aria-hidden="true" class="size-5 rounded-md bg-[conic-gradient(from_210deg,var(--color-tdl07-glow),var(--color-tdl07-lime),var(--color-tdl07-glow))]"></span>Fieldkit</strong>
            <button data-close type="button" aria-label="Close navigation" class="hidden size-11 place-items-center rounded-xl text-tdl07-sidemut transition-colors hover:bg-tdl07-sidehover hover:text-white focus-visible:outline-2 focus-visible:outline-tdl07-glow @max-[35rem]/app:grid"><svg viewBox="0 0 24 24" class="size-4.5 fill-none stroke-current stroke-2 [stroke-linecap:round]" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button></div>
          <a href="#home" aria-current="page">Home</a><a href="#jobs">Jobs</a><a href="#crew">Crew</a><a href="#invoices">Invoices</a><a href="#settings">Settings</a>
        </nav>
        <div class="flex min-w-0 flex-1 flex-col">
          <header class="flex h-15 flex-none items-center gap-3 border-b border-tdl07-edge bg-tdl07-panel px-3">
            <button data-burger type="button" aria-expanded="false" aria-controls="tdl07-nav-b" aria-label="Open navigation" class="hidden size-11 place-items-center rounded-xl text-tdl07-ink transition-colors hover:bg-tdl07-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdl07-acc @max-[35rem]/app:grid"><svg viewBox="0 0 24 24" class="size-4.5 fill-none stroke-current stroke-2 [stroke-linecap:round]" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg></button>
            <h2 class="text-base font-semibold tracking-tight">Today's jobs</h2><span class="rounded-full bg-tdl07-acc/12 px-2.25 py-0.75 text-[11px] font-bold text-tdl07-acc">6</span>
          </header>
          <div class="grid min-h-0 content-start gap-2.5 overflow-y-auto overscroll-contain p-3 [&>article]:grid [&>article]:grid-cols-[minmax(0,1fr)_auto] [&>article]:items-center [&>article]:gap-x-2.5 [&>article]:gap-y-0.5 [&>article]:rounded-xl [&>article]:border [&>article]:border-tdl07-edge [&>article]:bg-tdl07-panel [&>article]:px-3.5 [&>article]:py-3 [&_b]:truncate [&_b]:text-sm [&_b]:font-semibold [&_span]:col-start-1 [&_span]:text-xs [&_span]:text-tdl07-mut [&_i]:col-start-2 [&_i]:row-span-2 [&_i]:row-start-1 [&_i]:rounded-full [&_i]:border [&_i]:px-2.5 [&_i]:py-1 [&_i]:text-[10.5px] [&_i]:font-bold [&_i]:tracking-[0.04em] [&_i]:not-italic">
            <article><b>Deck repair — Hartley</b><span>08:30 · Crew A</span><i class="border-tdl07-acc/40 bg-tdl07-acc/10 text-tdl07-acc">On site</i></article>
            <article><b>Gutter install — Novak</b><span>10:00 · Crew B</span><i class="border-tdl07-edge bg-tdl07-bg text-tdl07-mut">Scheduled</i></article>
            <article><b>Fence quote — Ellis</b><span>13:30 · Sam</span><i class="border-tdl07-edge bg-tdl07-bg text-tdl07-mut">Scheduled</i></article>
            <article><b>Roof check — Winter Rd</b><span>15:00 · Crew A</span><i class="border-tdl07-hold/40 bg-tdl07-hold/10 text-tdl07-holdink">Hold</i></article>
          </div>
        </div>
      </div>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl07-bg: #f4f8f5;
  --color-tdl07-bg: oklch(0.975 0.006 150);
  --color-tdl07-panel: #ffffff;
  --color-tdl07-panel: oklch(1 0 0);
  --color-tdl07-hover: #edf2ee;
  --color-tdl07-hover: oklch(0.955 0.01 150);
  --color-tdl07-edge: #dbe4dd;
  --color-tdl07-edge: oklch(0.91 0.015 150);
  --color-tdl07-ink: #1f2d26;
  --color-tdl07-ink: oklch(0.27 0.025 160);
  --color-tdl07-mut: #53635a;
  --color-tdl07-mut: oklch(0.48 0.025 160);
  --color-tdl07-acc: #0f7f5b;
  --color-tdl07-acc: oklch(0.52 0.12 162);
  --color-tdl07-side: #11302a;
  --color-tdl07-side: oklch(0.26 0.04 170);
  --color-tdl07-sidehover: #1b3f37;
  --color-tdl07-sidehover: oklch(0.32 0.045 170);
  --color-tdl07-sideon: #22493f;
  --color-tdl07-sideon: oklch(0.36 0.05 170);
  --color-tdl07-sideink: #eef6f2;
  --color-tdl07-sideink: oklch(0.96 0.01 165);
  --color-tdl07-sidemut: #b2c7bf;
  --color-tdl07-sidemut: oklch(0.8 0.03 170);
  --color-tdl07-glow: #4fd3a0;
  --color-tdl07-glow: oklch(0.78 0.14 162);
  --color-tdl07-lime: #c6e070;
  --color-tdl07-lime: oklch(0.86 0.14 115);
  --color-tdl07-hold: #d69524;
  --color-tdl07-hold: oklch(0.71 0.14 75);
  --color-tdl07-holdink: #8a5a00;
  --color-tdl07-holdink: oklch(0.48 0.1 72);
  --color-tdl07-veil: #14261f;
  --color-tdl07-veil: oklch(0.22 0.03 165);
  --color-tdl07-frame: #1d2622;
  --color-tdl07-frame: oklch(0.25 0.015 160);
  --color-tdl07-shadow: #3b5a4c;
  --color-tdl07-shadow: oklch(0.4 0.05 160 / 0.5);
  --font-tdl07-sans: 'Outfit', system-ui, sans-serif;
}

.tdl-07 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tdl-07 * {
    transition-duration: 0.01s !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tdl-07 [data-app]').forEach((app) => {
    if (app.dataset.bound) return; app.dataset.bound = '1';
    const btn = app.querySelector('[data-burger]');
    const nav = app.querySelector('nav');
    const isDrawer = () => getComputedStyle(btn).display !== 'none';
    const set = (open, restoreFocus) => {
      app.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      nav.inert = isDrawer() && !open;
      if (open) setTimeout(() => { const a = nav.querySelector('a'); if (a) a.focus(); }, 60);
      else if (restoreFocus) btn.focus();
    };
    set(false, false);
    btn.addEventListener('click', () => set(!app.hasAttribute('data-open'), true));
    app.querySelector('[data-veil]').addEventListener('click', () => set(false, true));
    app.querySelector('[data-close]').addEventListener('click', () => set(false, true));
    app.addEventListener('keydown', (e) => { if (e.key === 'Escape' && app.hasAttribute('data-open')) set(false, true); });
    new ResizeObserver(() => { if (!app.hasAttribute('data-open')) nav.inert = isDrawer(); }).observe(app);
  });
})();
```
