---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-navbar-magnetic-hover-effect/"
title: "Tailwind CSS Navbar with Magnetic Hover Effect"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "A creative-studio navbar whose links lean toward the cursor, with the label drifting further than its pill for a parallax feel, and a soft amber spotlight…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Navbar with Magnetic Hover Effect
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-navbar-magnetic-hover-effect/

A creative-studio navbar whose links lean toward the cursor, with the label drifting further than its pill for a parallax feel, and a soft amber spotlight that follows the pointer across the page. JS only writes four custom properties; Tailwind consumes them with translate-x-(--tnv13-dx) and a radial-gradient background. Eased with a rAF lerp, disabled for touch and reduced motion.
## HTML
```html
<div class="tnv-13 relative isolate min-h-svh w-full overflow-hidden bg-tnv13-bg bg-[radial-gradient(520px_circle_at_var(--tnv13-mx,50%)_var(--tnv13-my,-30%),rgb(251_191_36/0.09),transparent_70%)] font-tnv13-sans text-tnv13-ink antialiased selection:bg-tnv13-acc selection:text-black">
  <div aria-hidden="true" class="pointer-events-none absolute top-1/2 left-1/2 -z-10 size-[600px] -translate-1/2 rounded-full border border-white/[0.05]"></div>
  <div aria-hidden="true" class="pointer-events-none absolute top-1/2 left-1/2 -z-10 size-[920px] -translate-1/2 rounded-full border border-white/[0.03]"></div>
  <header class="fixed inset-x-0 top-0 z-20 flex items-center justify-between px-6 py-7 sm:px-12">
    <a href="#" class="text-2xl font-bold tracking-[-0.04em]">Arp<span class="text-tnv13-acc">.</span></a>
    <nav aria-label="Main" class="hidden md:block">
      <ul class="flex items-center gap-2 text-[15px] font-medium text-tnv13-mut [&_a]:relative [&_a]:block [&_a]:rounded-xl [&_a]:px-4 [&_a]:py-2.5 [&_a]:[--tnv13-dx:0px] [&_a]:[--tnv13-dy:0px] [&_a]:translate-x-(--tnv13-dx) [&_a]:translate-y-(--tnv13-dy) [&_a]:transition-colors [&_a]:before:absolute [&_a]:before:inset-0 [&_a]:before:-z-10 [&_a]:before:scale-75 [&_a]:before:rounded-xl [&_a]:before:bg-white/[0.06] [&_a]:before:opacity-0 [&_a]:before:transition-[scale,opacity] [&_a]:before:duration-300 [&_a]:before:ease-[cubic-bezier(.34,1.56,.64,1)] [&_a]:before:content-[''] [&_a:hover]:text-white [&_a:hover]:before:scale-100 [&_a:hover]:before:opacity-100 [&_a:focus-visible]:text-white [&_a:focus-visible]:outline-2 [&_a:focus-visible]:outline-tnv13-acc [&_a[aria-current]]:text-white [&_span]:block [&_span]:translate-x-[calc(var(--tnv13-dx)*0.6)] [&_span]:translate-y-[calc(var(--tnv13-dy)*0.6)]">
        <li><a href="#" data-magnet aria-current="page"><span>Work</span></a></li>
        <li><a href="#" data-magnet><span>Studio</span></a></li>
        <li><a href="#" data-magnet><span>Process</span></a></li>
        <li><a href="#" data-magnet><span>Journal</span></a></li>
      </ul>
    </nav>
    <a href="#" data-magnet class="inline-flex h-11 translate-x-(--tnv13-dx) translate-y-(--tnv13-dy) items-center gap-2 rounded-xl bg-tnv13-acc px-5 text-sm font-bold text-black transition-shadow [--tnv13-dx:0px] [--tnv13-dy:0px] hover:shadow-[0_0_36px_rgb(251_191_36/0.35)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnv13-acc">Let's talk<svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M7 17L17 7M8 7h9v9"/></svg></a>
  </header>
  <main class="grid min-h-svh place-items-center px-6 pt-32 pb-16 text-center [&_code]:rounded [&_code]:bg-white/[0.08] [&_code]:px-1.5 [&_code]:font-tnv13-mono [&_code]:text-[0.85em] [&_code]:text-tnv13-ink">
    <div>
      <p class="mb-6 font-tnv13-mono text-xs font-medium tracking-[0.2em] text-tnv13-acc uppercase">Creative direction &amp; design</p>
      <h1 class="text-[clamp(3rem,10vw,7.5rem)] leading-[0.92] font-bold tracking-[-0.055em]">Move the cursor<span class="sr-only"> near the nav</span><br><span aria-hidden="true" class="text-transparent [-webkit-text-stroke:1px_rgb(255_255_255/0.3)]">near the nav</span></h1>
      <p class="mx-auto mt-7 max-w-md text-base/[1.7] text-tnv13-mut text-pretty">Links lean toward the pointer while their labels drift further, and a spotlight follows you across the page. JS writes <code>--tnv13-dx</code>; Tailwind reads it with <code>translate-x-(--tnv13-dx)</code>.</p>
    </div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv13-bg: #070707;
  --color-tnv13-bg: oklch(0.12 0 0);
  --color-tnv13-ink: #fafafa;
  --color-tnv13-ink: oklch(0.985 0 0);
  --color-tnv13-mut: #a3a3a3;
  --color-tnv13-mut: oklch(0.708 0 0);
  --color-tnv13-acc: #fbbf24;
  --color-tnv13-acc: oklch(0.828 0.189 84);
  --font-tnv13-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tnv13-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tnv-13 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tnv-13');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const magnetic = matchMedia('(pointer: fine)').matches && !matchMedia('(prefers-reduced-motion: reduce)').matches;
  const els = [...root.querySelectorAll('[data-magnet]')];
  const st = els.map(() => ({ x: 0, y: 0 }));
  const RADIUS = 90, PULL = 0.3, MAX = 14, EASE = 0.18;
  const clamp = (v) => Math.max(-MAX, Math.min(MAX, v));
  let px = -1e4, py = -1e4, raf = 0;
  const frame = () => {
    raf = 0;
    let busy = false;
    els.forEach((el, i) => {
      const s = st[i];
      const r = el.getBoundingClientRect();
      const cx = r.left - s.x + r.width / 2, cy = r.top - s.y + r.height / 2;
      const dx = px - cx, dy = py - cy;
      const near = Math.hypot(dx, dy) < RADIUS + r.width / 2;
      const tx = near ? clamp(dx * PULL) : 0, ty = near ? clamp(dy * PULL) : 0;
      s.x += (tx - s.x) * EASE;
      s.y += (ty - s.y) * EASE;
      if (Math.abs(tx - s.x) > 0.05 || Math.abs(ty - s.y) > 0.05) busy = true;
      el.style.setProperty('--tnv13-dx', s.x.toFixed(2) + 'px');
      el.style.setProperty('--tnv13-dy', s.y.toFixed(2) + 'px');
    });
    if (busy) raf = requestAnimationFrame(frame);
  };
  const kick = () => { if (!raf) raf = requestAnimationFrame(frame); };
  root.addEventListener('pointermove', (e) => {
    const b = root.getBoundingClientRect();
    root.style.setProperty('--tnv13-mx', (e.clientX - b.left) + 'px');
    root.style.setProperty('--tnv13-my', (e.clientY - b.top) + 'px');
    if (magnetic) { px = e.clientX; py = e.clientY; kick(); }
  }, { passive: true });
  root.addEventListener('pointerleave', () => { px = py = -1e4; kick(); });
})();
```
