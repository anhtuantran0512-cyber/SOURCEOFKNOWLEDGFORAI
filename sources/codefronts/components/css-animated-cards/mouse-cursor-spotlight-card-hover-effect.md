---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/mouse-cursor-spotlight-card-hover-effect/"
title: "Mouse Cursor Spotlight Card Hover Effect"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "Not six independent hover states &mdash; one light."
has_js: "true"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mouse Cursor Spotlight Card Hover Effect
Source: https://codefronts.com/components/css-animated-cards/mouse-cursor-spotlight-card-hover-effect/

Not six independent hover states &mdash; one light. A single source with inertia drifts toward your cursor, and every card computes its own distance and direction from it: brightness falls off with the square of distance, text lightens as the light approaches, icon tiles cast shadows away from it, and a specular dot slides across each tile toward it. The grid keeps breathing when you leave (the light drifts on a Lissajous path), keyboard focus walks the light to the focused card, and reduced motion parks it dead centre with no loop at all.
## HTML
```html
<section class="ac-21" aria-label="Cursor spotlight card hover demo">
  <div class="ac-21__stage">
    <header class="ac-21__head">
      <p class="ac-21__eyebrow">One light, six surfaces</p>
      <h2 class="ac-21__title">Move your cursor &mdash; the grid is lit, not hovered</h2>
      <p class="ac-21__sub">Brightness falls off with distance. Every shadow points away from the light.</p>
    </header>
    <div class="ac-21__grid" data-grid>
      <span class="ac-21__orb" data-orb aria-hidden="true"></span>
      <article class="ac-21__card" data-card tabindex="0">
        <span class="ac-21__fill" aria-hidden="true"></span>
        <span class="ac-21__edge" aria-hidden="true"></span>
        <span class="ac-21__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h8l-1 8 10-12h-8l1-8z"/></svg><i class="ac-21__spec"></i></span>
        <h3 class="ac-21__name">Edge runtime</h3>
        <p class="ac-21__copy">Cold starts under 12 ms in 34 regions. Deploy from a git push.</p>
      </article>
      <article class="ac-21__card" data-card tabindex="0">
        <span class="ac-21__fill" aria-hidden="true"></span>
        <span class="ac-21__edge" aria-hidden="true"></span>
        <span class="ac-21__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 4h18v16H3z M3 10h18 M8 4v16"/></svg><i class="ac-21__spec"></i></span>
        <h3 class="ac-21__name">Preview environments</h3>
        <p class="ac-21__copy">Every pull request gets a URL, a database branch and its own seed data.</p>
      </article>
      <article class="ac-21__card" data-card tabindex="0">
        <span class="ac-21__fill" aria-hidden="true"></span>
        <span class="ac-21__edge" aria-hidden="true"></span>
        <span class="ac-21__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 4v6c0 4.4-3.4 7-8 8-4.6-1-8-3.6-8-8V7l8-4z M9 12l2 2 4-4"/></svg><i class="ac-21__spec"></i></span>
        <h3 class="ac-21__name">Zero-config TLS</h3>
        <p class="ac-21__copy">Certificates issued, renewed and stapled without a dashboard visit.</p>
      </article>
      <article class="ac-21__card" data-card tabindex="0">
        <span class="ac-21__fill" aria-hidden="true"></span>
        <span class="ac-21__edge" aria-hidden="true"></span>
        <span class="ac-21__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19V9m5 10V5m5 14v-7m5 7V8"/></svg><i class="ac-21__spec"></i></span>
        <h3 class="ac-21__name">Real-user metrics</h3>
        <p class="ac-21__copy">p75 Core Web Vitals per route, per country, streamed live.</p>
      </article>
      <article class="ac-21__card" data-card tabindex="0">
        <span class="ac-21__fill" aria-hidden="true"></span>
        <span class="ac-21__edge" aria-hidden="true"></span>
        <span class="ac-21__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18z M3 12h18 M12 3a15 15 0 0 1 0 18a15 15 0 0 1 0-18z"/></svg><i class="ac-21__spec"></i></span>
        <h3 class="ac-21__name">Anycast network</h3>
        <p class="ac-21__copy">One IP, 120 points of presence, automatic failover on packet loss.</p>
      </article>
      <article class="ac-21__card" data-card tabindex="0">
        <span class="ac-21__fill" aria-hidden="true"></span>
        <span class="ac-21__edge" aria-hidden="true"></span>
        <span class="ac-21__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M7 8l-4 4 4 4M17 8l4 4-4 4M14 4l-4 16"/></svg><i class="ac-21__spec"></i></span>
        <h3 class="ac-21__name">Typed API client</h3>
        <p class="ac-21__copy">Generated from your schema on every deploy. No drift, no guessing.</p>
      </article>
    </div>
    <p class="ac-21__chip" aria-hidden="true">single light source &middot; inverse falloff &rarr; --n &middot; direction &rarr; --dx/--dy &middot; shadows cast away &middot; idle orbit &middot; focus moves the light</p>
  </div>
</section>
```
## CSS
```css
.ac-21,
.ac-21 *,
.ac-21 *::before,
.ac-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-21 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-21-bg: oklch(0.115 0.012 265);
  --ac-21-card: oklch(0.165 0.014 265);
  --ac-21-ink: oklch(0.97 0.004 260);
  --ac-21-mut: oklch(0.50 0.018 265);
  --ac-21-acc: oklch(0.83 0.15 228);
  --ac-21-line: oklch(1 0 0/.07);
  background: var(--ac-21-bg);
  color: var(--ac-21-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-21__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(18px,3vw,30px);
  padding: clamp(20px,5vw,58px);
}

.ac-21__head {
  display: grid;
  justify-items: center;
  gap: 9px;
  text-align: center;
  max-width: 60ch;
}

.ac-21__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-21-acc);
}

.ac-21__title {
  font-size: clamp(23px,3.4vw,38px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-21__sub {
  font-size: 14px;
  color: oklch(0.62 0.02 265);
  text-wrap: pretty;
}

.ac-21__grid {
  position: relative;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(240px,1fr));
  gap: 14px;
  width: min(100%,940px);
  isolation: isolate;
}

.ac-21__orb {
  position: absolute;
  left: 0;
  top: 0;
  width: 300px;
  height: 300px;
  margin: -150px 0 0 -150px;
  border-radius: 50%;
  pointer-events: none;
  z-index: 4;
  translate: var(--ac-21-lx,50%) var(--ac-21-ly,50%);
  background: radial-gradient(closest-side,color-mix(in oklch,var(--ac-21-acc) 26%,transparent),transparent 68%);
  filter: blur(18px);
  opacity: var(--ac-21-lit,0);
  transition: opacity .5s;
  mix-blend-mode: screen;
}

.ac-21__card {
  --ac-21-n: 0;
  --ac-21-dx: 0;
  --ac-21-dy: 0;
  position: relative;
  display: grid;
  gap: 11px;
  padding: 24px 22px;
  border-radius: 18px;
  background: var(--ac-21-card);
  border: 1px solid var(--ac-21-line);
  isolation: isolate;
  translate: 0 calc(var(--ac-21-n) * -5px);
  transition: translate .45s cubic-bezier(.16,1,.3,1),border-color .45s;
}

.ac-21__card:focus-visible {
  outline: 2px solid var(--ac-21-acc);
  outline-offset: 3px;
}

.ac-21__fill {
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: 18px;
  pointer-events: none;
  opacity: calc(var(--ac-21-n) * .95);
  background: radial-gradient(300px circle at var(--ac-21-x,50%) var(--ac-21-y,50%),color-mix(in oklch,var(--ac-21-acc) 22%,transparent),transparent 62%);
}

.ac-21__edge {
  position: absolute;
  inset: 0;
  border-radius: 18px;
  padding: 1px;
  pointer-events: none;
  opacity: var(--ac-21-n);
  background: radial-gradient(240px circle at var(--ac-21-x,50%) var(--ac-21-y,50%),color-mix(in oklch,var(--ac-21-acc) 95%,transparent),transparent 58%);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
}

.ac-21__ico {
  position: relative;
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border-radius: 13px;
  background: color-mix(in oklch,var(--ac-21-acc) calc(8% + var(--ac-21-n) * 16%),oklch(0.22 0.02 265));
  color: color-mix(in oklch,var(--ac-21-acc) calc(45% + var(--ac-21-n) * 55%),oklch(0.55 0.03 265));
  box-shadow: calc(var(--ac-21-dx) * -9px) calc(var(--ac-21-dy) * -9px) calc(10px + var(--ac-21-n) * 14px) oklch(0 0 0/calc(.3 + var(--ac-21-n) * .4)),inset 0 1px 0 oklch(1 0 0/calc(var(--ac-21-n) * .3));
}

.ac-21__spec {
  position: absolute;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  pointer-events: none;
  left: calc(50% + var(--ac-21-dx) * 34%);
  top: calc(50% + var(--ac-21-dy) * 34%);
  translate: -50% -50%;
  background: radial-gradient(closest-side,oklch(1 0 0/.85),transparent 70%);
  opacity: calc(var(--ac-21-n) * .9);
}

.ac-21__name {
  font-size: 15.5px;
  font-weight: 650;
  letter-spacing: -.022em;
  color: color-mix(in oklch,oklch(0.66 0.015 265),var(--ac-21-ink) calc(var(--ac-21-n) * 100%));
}

.ac-21__copy {
  font-size: 13.5px;
  line-height: 1.55;
  text-wrap: pretty;
  color: color-mix(in oklch,var(--ac-21-mut),oklch(0.80 0.015 265) calc(var(--ac-21-n) * 100%));
}

.ac-21__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-21-mut);
  padding: 8px 15px;
  border: 1px solid var(--ac-21-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,880px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-21__card {
    transition: none;
    translate: none;
  }

  .ac-21__orb {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const R = 560;            // light radius in px — beyond this a card is unlit
  const EASE = 0.14;        // lerp factor: the light has inertia, it does not snap
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.querySelectorAll('.ac-21').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const grid = root.querySelector('[data-grid]');
    const orb = root.querySelector('[data-orb]');
    const cards = [...grid.querySelectorAll('[data-card]')];
    let rects = [], gridRect = null;
    let lx = 0, ly = 0, tx = 0, ty = 0, lit = 0, pointing = false, raf = 0, t0 = performance.now();

    const measure = () => {
      gridRect = grid.getBoundingClientRect();
      rects = cards.map((c) => c.getBoundingClientRect());
      if (!lx && !ly) { lx = tx = gridRect.width / 2; ly = ty = gridRect.height / 2; }
    };
    measure();
    addEventListener('resize', measure, { passive: true });
    addEventListener('scroll', measure, { passive: true, capture: true });

    // Idle: the light drifts on a Lissajous path so the grid is alive before anyone touches it.
    const idle = (t) => {
      const w = gridRect.width, h = gridRect.height;
      tx = w * (0.5 + 0.34 * Math.sin(t / 3700));
      ty = h * (0.5 + 0.38 * Math.sin(t / 2300));
    };

    const frame = (now) => {
      raf = 0;
      if (!pointing) idle(now - t0);
      lx += (tx - lx) * EASE;                       // inertia
      ly += (ty - ly) * EASE;
      const target = pointing ? 1 : 0.72;
      lit += (target - lit) * 0.08;

      grid.style.setProperty('--ac-21-lit', lit.toFixed(3));
      orb.style.setProperty('--ac-21-lx', lx.toFixed(1) + 'px');
      orb.style.setProperty('--ac-21-ly', ly.toFixed(1) + 'px');

      for (let i = 0; i < cards.length; i++) {
        const r = rects[i], c = cards[i];
        const ox = r.left - gridRect.left, oy = r.top - gridRect.top;
        // light position relative to THIS card — one source, six local coordinate systems
        const px = lx - ox, py = ly - oy;
        c.style.setProperty('--ac-21-x', px.toFixed(1) + 'px');
        c.style.setProperty('--ac-21-y', py.toFixed(1) + 'px');
        // distance from the card's centre drives brightness, with a squared falloff
        const dx = lx - (ox + r.width / 2), dy = ly - (oy + r.height / 2);
        const dist = Math.hypot(dx, dy);
        const n = Math.max(0, 1 - dist / R);
        c.style.setProperty('--ac-21-n', (n * n * lit).toFixed(3));
        // unit vector toward the light: shadows are cast along its negative
        const len = dist || 1;
        c.style.setProperty('--ac-21-dx', (dx / len).toFixed(3));
        c.style.setProperty('--ac-21-dy', (dy / len).toFixed(3));
      }
      if (!document.hidden) raf = requestAnimationFrame(frame);
    };

    const kick = () => { if (!raf && !document.hidden) raf = requestAnimationFrame(frame); };

    if (reduce) {                                   // static light, dead centre, no loop at all
      lx = gridRect.width / 2; ly = gridRect.height / 2; lit = 1; pointing = true;
      frame(0); cancelAnimationFrame(raf); raf = 0;
    } else kick();

    grid.addEventListener('pointermove', (e) => {
      if (e.pointerType === 'touch') return;
      pointing = true;
      tx = e.clientX - gridRect.left;
      ty = e.clientY - gridRect.top;
      kick();
    }, { passive: true });
    grid.addEventListener('pointerleave', () => { pointing = false; t0 = performance.now(); });

    // Keyboard parity: focusing a card walks the light over to it.
    cards.forEach((c, i) => c.addEventListener('focus', () => {
      pointing = true;
      const r = rects[i];
      tx = r.left - gridRect.left + r.width / 2;
      ty = r.top - gridRect.top + r.height / 2;
      kick();
    }));
    grid.addEventListener('focusout', (e) => { if (!grid.contains(e.relatedTarget)) pointing = false; });

    document.addEventListener('visibilitychange', () => { if (!document.hidden && !reduce) kick(); });
  });
})();
```
