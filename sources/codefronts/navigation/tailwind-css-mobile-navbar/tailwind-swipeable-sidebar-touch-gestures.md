---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-swipeable-sidebar-touch-gestures/"
title: "Tailwind Swipeable Sidebar Menu with Touch Gestures"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "An edge-swipe sidebar that follows your finger 1:1, pushes the page aside with parallax, and snaps open or closed on distance or flick velocity."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Swipeable Sidebar Menu with Touch Gestures
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-swipeable-sidebar-touch-gestures/

An edge-swipe sidebar that follows your finger 1:1, pushes the page aside with parallax, and snaps open or closed on distance or flick velocity. The port moves from touch events to Pointer Events &mdash; so mouse and pen drag work too &mdash; and keeps every visual state in group-data-open: utilities; the script only toggles one attribute.
## HTML
```html
<section class="tmn-06 w-full min-h-svh grid place-items-center bg-tmn06-stage px-4 py-6 font-tmn06-sans antialiased" aria-label="Tailwind swipeable sidebar demo">
  <div data-tmn06 class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] overflow-hidden rounded-[2.25rem] bg-tmn06-bg text-tmn06-ink shadow-[0_40px_100px_-30px_oklch(0_0_0/0.85)] ring-1 ring-white/8 select-none">
    <main data-page class="absolute inset-0 overflow-y-auto px-5 pt-5 pb-6 transition-[translate] duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-data-open:translate-x-15 group-data-dragging:transition-none">
      <header class="mb-7 flex items-center justify-between">
        <button type="button" data-menu aria-expanded="false" aria-controls="tmn-06-sidebar" class="grid size-11 place-content-center gap-1 rounded-xl border border-tmn06-line bg-tmn06-surface transition-colors hover:border-tmn06-acc/60 focus-visible:ring-2 focus-visible:ring-tmn06-acc focus-visible:outline-none"><span class="sr-only">Open menu</span><span class="block h-0.5 w-4.5 rounded-full bg-current"></span><span class="block h-0.5 w-4.5 rounded-full bg-current"></span><span class="block h-0.5 w-3 rounded-full bg-current"></span></button>
        <p data-title class="text-lg font-bold">Canvas</p>
        <span class="grid size-11 place-items-center rounded-full bg-linear-135 from-tmn06-acc to-tmn06-acc2 text-sm font-bold text-tmn06-bg">CR</span>
      </header>
      <div class="mb-6 flex items-center gap-3 rounded-2xl border border-dashed border-tmn06-acc/40 p-4 text-[13px] leading-relaxed text-tmn06-mut">
        <svg viewBox="0 0 24 24" class="size-8 flex-none text-tmn06-acc" aria-hidden="true"><path d="M18 11V6a2 2 0 0 0-4 0M14 10V4a2 2 0 0 0-4 0v2M10 10.5V6a2 2 0 0 0-4 0v8"/><path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.9-6-2.4l-3.6-3.6a2 2 0 0 1 2.8-2.8L7 15"/></svg>
        <p><strong class="text-tmn06-ink">Swipe right</strong> from the left edge &mdash; or drag with a mouse &mdash; to open the sidebar.</p>
      </div>
      <article class="mb-3 rounded-2xl border border-tmn06-line bg-tmn06-surface p-5"><div class="mb-3 h-1 w-8 rounded-full bg-linear-to-r from-tmn06-acc to-tmn06-acc2"></div><h2 class="mb-1 text-[15px] font-semibold">Brand identity project</h2><p class="text-[13px] text-tmn06-mut">Updated 2 hours ago · 14 layers</p></article>
      <article class="mb-3 rounded-2xl border border-tmn06-line bg-tmn06-surface p-5"><div class="mb-3 h-1 w-8 rounded-full bg-teal-400"></div><h2 class="mb-1 text-[15px] font-semibold">App redesign</h2><p class="text-[13px] text-tmn06-mut">Updated yesterday · 38 layers</p></article>
      <article class="rounded-2xl border border-tmn06-line bg-tmn06-surface p-5"><div class="mb-3 h-1 w-8 rounded-full bg-amber-400"></div><h2 class="mb-1 text-[15px] font-semibold">Icon set v2</h2><p class="text-[13px] text-tmn06-mut">Updated Monday · 120 frames</p></article>
    </main>

    <div data-scrim aria-hidden="true" class="pointer-events-none absolute inset-0 z-10 bg-black/55 opacity-0 transition-opacity duration-300 group-data-open:pointer-events-auto group-data-open:opacity-100 group-data-dragging:transition-none"></div>

    <nav id="tmn-06-sidebar" data-side aria-label="Workspace" inert class="absolute inset-y-0 left-0 z-20 flex w-[min(280px,80%)] -translate-x-full touch-pan-y flex-col border-r border-tmn06-line bg-tmn06-surface transition-transform duration-300 ease-[cubic-bezier(.4,0,.2,1)] will-change-transform group-data-open:translate-x-0 group-data-dragging:transition-none">
      <div class="flex items-center gap-3 border-b border-tmn06-line bg-linear-135 from-tmn06-acc/16 to-tmn06-acc2/8 px-5 pt-10 pb-5">
        <span class="grid size-11 place-items-center rounded-full bg-linear-135 from-tmn06-acc to-tmn06-acc2 text-sm font-bold text-tmn06-bg">CR</span>
        <div><p class="text-[15px] font-semibold">Casey Rivera</p><p class="text-xs text-tmn06-mut">Pro designer</p></div>
      </div>
      <div class="flex-1 overflow-y-auto py-3 text-sm font-medium">
        <p class="px-5 pt-3 pb-1 text-[11px] font-bold tracking-[0.14em] text-tmn06-mut uppercase">Workspace</p>
        <a href="#" data-link aria-current="page" class="flex min-h-11 items-center gap-3 px-5 text-tmn06-mut transition-colors hover:bg-white/5 hover:text-tmn06-ink aria-[current=page]:bg-tmn06-acc/12 aria-[current=page]:text-tmn06-acc"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>Canvas</a>
        <a href="#" data-link class="flex min-h-11 items-center gap-3 px-5 text-tmn06-mut transition-colors hover:bg-white/5 hover:text-tmn06-ink aria-[current=page]:bg-tmn06-acc/12 aria-[current=page]:text-tmn06-acc"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 15h18M15 3v18"/></svg>Wireframes</a>
        <a href="#" data-link class="flex min-h-11 items-center gap-3 px-5 text-tmn06-mut transition-colors hover:bg-white/5 hover:text-tmn06-ink aria-[current=page]:bg-tmn06-acc/12 aria-[current=page]:text-tmn06-acc"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="m5 3 14 9-14 9z"/></svg>Prototypes</a>
        <a href="#" data-link class="flex min-h-11 items-center gap-3 px-5 text-tmn06-mut transition-colors hover:bg-white/5 hover:text-tmn06-ink aria-[current=page]:bg-tmn06-acc/12 aria-[current=page]:text-tmn06-acc"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M21 8 12 3 3 8v8l9 5 9-5zM3 8l9 5 9-5M12 13v8"/></svg>Assets</a>
        <p class="px-5 pt-5 pb-1 text-[11px] font-bold tracking-[0.14em] text-tmn06-mut uppercase">Team</p>
        <a href="#" data-link class="flex min-h-11 items-center gap-3 px-5 text-tmn06-mut transition-colors hover:bg-white/5 hover:text-tmn06-ink aria-[current=page]:bg-tmn06-acc/12 aria-[current=page]:text-tmn06-acc"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0M16 4a4 4 0 0 1 0 8M22 21a7 7 0 0 0-4-6.3"/></svg>Members</a>
        <a href="#" data-link class="flex min-h-11 items-center gap-3 px-5 text-tmn06-mut transition-colors hover:bg-white/5 hover:text-tmn06-ink aria-[current=page]:bg-tmn06-acc/12 aria-[current=page]:text-tmn06-acc"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L3 21l1.9-6.4A8 8 0 1 1 21 12z"/></svg>Comments</a>
      </div>
    </nav>

    <div data-edge aria-hidden="true" class="absolute inset-y-0 left-0 z-30 w-6 cursor-grab touch-pan-y group-data-open:hidden">
      <span class="absolute top-1/2 left-0 h-12 w-1 -translate-y-1/2 rounded-r-full bg-linear-to-b from-tmn06-acc to-tmn06-acc2 animate-tmn06-hint motion-reduce:animate-none"></span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn06-stage: #09090b;
  --color-tmn06-stage: oklch(0.14 0.005 285);
  --color-tmn06-bg: #18181b;
  --color-tmn06-bg: oklch(0.21 0.006 285);
  --color-tmn06-surface: #232327;
  --color-tmn06-surface: oklch(0.26 0.006 285);
  --color-tmn06-line: #3a3a41;
  --color-tmn06-line: oklch(0.35 0.01 285);
  --color-tmn06-ink: #fafafa;
  --color-tmn06-ink: oklch(0.985 0 0);
  --color-tmn06-mut: #a1a1aa;
  --color-tmn06-mut: oklch(0.71 0.013 286);
  --color-tmn06-acc: #a78bfa;
  --color-tmn06-acc: oklch(0.71 0.16 293);
  --color-tmn06-acc2: #f472b6;
  --color-tmn06-acc2: oklch(0.73 0.18 350);
  --font-tmn06-sans: 'Manrope', system-ui, sans-serif;
  --animate-tmn06-hint: tmn06-hint 2s ease-in-out infinite;

  @keyframes tmn06-hint {
    0%,
        100% {
      opacity: 0.25;
      scale: 1 0.8;
    }

    50% {
      opacity: 0.8;
      scale: 1 1;
    }
  }
}
/* Icon base: utilities still win because this sits in the base layer. */

@layer base {
  .tmn-06 svg {
    fill: none;
    stroke: currentColor;
    stroke-width: 1.8;
    stroke-linecap: round;
    stroke-linejoin: round;
    flex: none;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is
   sized before the browser build compiles. */

.tmn-06 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tmn06]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const side = root.querySelector('[data-side]');
    const page = root.querySelector('[data-page]');
    const scrim = root.querySelector('[data-scrim]');
    const edge = root.querySelector('[data-edge]');
    const btn = root.querySelector('[data-menu]');
    const title = root.querySelector('[data-title]');
    const W = () => side.offsetWidth;
    let open = false, drag = null, justDragged = false;

    const clear = () => { side.style.translate = ''; page.style.translate = ''; scrim.style.opacity = ''; root.removeAttribute('data-dragging'); };
    const set = (v, focus) => {
      open = v;
      clear();
      root.toggleAttribute('data-open', v);
      side.inert = !v;
      btn.setAttribute('aria-expanded', String(v));
      if (v && focus) side.querySelector('[aria-current]').focus({ preventScroll: true });
      if (!v && focus) btn.focus({ preventScroll: true });
    };

    const start = (e) => { if (e.button > 0) return; drag = { x: e.clientX, y: e.clientY, t: performance.now(), dx: 0, active: false, id: e.pointerId, el: e.currentTarget }; };
    const move = (e) => {
      if (!drag || e.pointerId !== drag.id) return;
      const dx = e.clientX - drag.x, dy = e.clientY - drag.y;
      if (!drag.active) {
        if (Math.abs(dy) > 12 && Math.abs(dy) > Math.abs(dx)) { drag = null; return; }
        if (Math.abs(dx) < 8) return;
        drag.active = true;
        root.setAttribute('data-dragging', '');
        try { drag.el.setPointerCapture(drag.id); } catch (err) {}
      }
      drag.dx = dx;
      const w = W();
      const off = open ? Math.min(0, Math.max(-w, dx)) : Math.max(0, Math.min(w, dx)) - w;
      const p = (off + w) / w;
      side.style.translate = off + 'px 0';
      page.style.translate = (p * 60) + 'px 0';
      scrim.style.opacity = String(p);
    };
    const end = () => {
      if (!drag) return;
      const d = drag; drag = null;
      if (!d.active) return;
      justDragged = true; setTimeout(() => { justDragged = false; }, 0);
      const v = d.dx / Math.max(1, performance.now() - d.t);
      if (!open) set(d.dx > W() / 3 || v > 0.5);
      else set(!(d.dx < -W() / 3 || v < -0.5));
    };

    [edge, side, scrim].forEach((el) => {
      el.addEventListener('pointerdown', start);
      el.addEventListener('pointermove', move);
      el.addEventListener('pointerup', end);
      el.addEventListener('pointercancel', end);
    });
    btn.addEventListener('click', () => set(!open, true));
    scrim.addEventListener('click', () => { if (!justDragged) set(false); });
    side.querySelectorAll('[data-link]').forEach((a) => a.addEventListener('click', (e) => {
      e.preventDefault();
      if (justDragged) return;
      side.querySelectorAll('[data-link]').forEach((x) => x.removeAttribute('aria-current'));
      a.setAttribute('aria-current', 'page');
      title.textContent = a.textContent.trim();
      set(false, true);
    }));
    root.addEventListener('keydown', (e) => { if (e.key === 'Escape' && open) set(false, true); });
  });
})();
```
