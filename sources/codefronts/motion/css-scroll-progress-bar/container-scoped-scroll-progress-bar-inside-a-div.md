---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/container-scoped-scroll-progress-bar-inside-a-div/"
title: "Container-Scoped Scroll Progress Bar (Inside a Div)"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "The version nobody documents: the thing that scrolls is not the page, it is a panel."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Container-Scoped Scroll Progress Bar (Inside a Div)
Source: https://codefronts.com/motion/css-scroll-progress-bar/container-scoped-scroll-progress-bar-inside-a-div/

The version nobody documents: the thing that scrolls is not the page, it is a panel. App shells, modals, chat logs, terms-and-conditions boxes and dashboard cards all scroll their own overflow container — where scroll(root) is permanently zero. Named scroll timelines plus timeline-scope are the correct answer, and this demo is the complete recipe.
## HTML
```html
<section class="sp-08" aria-label="Container-scoped scroll progress bar demo">
  <header class="sp-08__bar">
    <a class="sp-08__brand" href="#sp-08-panel"><span class="sp-08__logo" aria-hidden="true"></span>Panelworks</a>
    <p class="sp-08__meta">scroll-timeline-name</p>
  </header>
  <div class="sp-08__intro">
    <p class="sp-08__intro-eyebrow">the page is not always the scroller</p>
    <h2 class="sp-08__intro-title">Progress for a div, not a document</h2>
    <p class="sp-08__intro-sub">Scroll <em>inside</em> the panel below. The bar in its header is bound to the panel's own named timeline — the page behind it never moves.</p>
  </div>
  <div class="sp-08__panel" id="sp-08-panel">
    <div class="sp-08__phead">
      <div class="sp-08__ptitle">
        <span class="sp-08__pdot" aria-hidden="true"></span>
        <h3 class="sp-08__ph">Terms of Service</h3>
      </div>
      <p class="sp-08__ppct" id="sp-08-pct" role="progressbar" aria-label="Terms read" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">0%</p>
      <i class="sp-08__pfill" aria-hidden="true"></i>
    </div>
    <div class="sp-08__body" id="sp-08-body" tabindex="0" role="region" aria-label="Terms of Service, scrollable">
      <p class="sp-08__lede">This panel owns its own scroll port. Everything below lives inside it, and the hairline in the header above tracks only this box.</p>
      <h4 class="sp-08__sh">1. Named timelines</h4>
      <p class="sp-08__bp">An anonymous <code>scroll()</code> timeline can only look up the tree. A header sitting above the scroller is a sibling, so it needs a name it can reference from anywhere in the scope.</p>
      <h4 class="sp-08__sh">2. Scope</h4>
      <p class="sp-08__bp">The panel declares <code>timeline-scope</code>. That single property lifts the name out of the scroller's subtree and makes it visible to the header, a sidebar, or a toolbar three levels away.</p>
      <h4 class="sp-08__sh">3. Containment</h4>
      <p class="sp-08__bp">A flick that reaches the bottom of a panel should stop there, not throw the page behind it. <code>overscroll-behavior: contain</code> is one line and prevents the most-reported bug in modal scroll areas.</p>
      <h4 class="sp-08__sh">4. Gutter stability</h4>
      <p class="sp-08__bp"><code>scrollbar-gutter: stable</code> reserves the scrollbar's width up front, so content does not shift sideways the moment a list grows past one screen.</p>
      <h4 class="sp-08__sh">5. Keyboard access</h4>
      <p class="sp-08__bp">A scrollable region that is not focusable cannot be scrolled by keyboard alone. It carries <code>tabindex="0"</code> and a <code>role</code> with a name, so arrow keys and Page Down work as expected.</p>
      <h4 class="sp-08__sh">6. Listening in the right place</h4>
      <p class="sp-08__bp">Window scroll events never fire for an inner div. The fallback listener is attached to this element, which is also the correct instinct for any nested scroller.</p>
      <h4 class="sp-08__sh">7. Bounded height</h4>
      <p class="sp-08__bp">A scroller with no height constraint never overflows, and a timeline over a non-overflowing scroller has zero length — the animation sits frozen at its start value with no error anywhere.</p>
      <h4 class="sp-08__sh">8. Multiple panels</h4>
      <p class="sp-08__bp">Names are scoped, so a dashboard of six cards is six declarations. Each bar tracks its own card and nothing coordinates through JavaScript.</p>
      <p class="sp-08__end">You have reached the end of the panel. The header hairline is full; the page behind you has not moved a pixel.</p>
    </div>
  </div>
  <section class="sp-08__after">
    <p class="sp-08__kicker">Why it matters</p>
    <h3 class="sp-08__h">Most real apps scroll a div</h3>
    <p class="sp-08__p">Fixed sidebars, sticky toolbars, virtualised lists, modals, drawers — in all of them the document body is pinned and an inner element does the scrolling. Every <code>scroll(root)</code> snippet on the internet quietly breaks in that layout.</p>
    <p class="sp-08__chip">1 name · 1 scope · 0 coordination code</p>
  </section>
  <footer class="sp-08__pagefoot"><p class="sp-08__pagefootin">Scroll progress pattern 08 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-08-bg);
  --sp-08-bg: oklch(0.965 0.008 245);
  --sp-08-surface: oklch(1 0 0);
  --sp-08-ink: oklch(0.2 0.022 255);
  --sp-08-mut: oklch(0.52 0.018 255);
  --sp-08-acc: oklch(0.58 0.16 235);
  --sp-08-line: oklch(0.2 0.022 255/.11);
  --sp-08-p: 0;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-08-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-08 *,
.sp-08 *::before,
.sp-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-08__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 58px;
  background: color-mix(in oklch,var(--sp-08-surface) 82%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-block-end: 1px solid var(--sp-08-line);
}

.sp-08__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 730;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.sp-08__brand:focus-visible {
  outline: 2px solid var(--sp-08-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.sp-08__logo {
  inline-size: 18px;
  block-size: 18px;
  border-radius: 5px;
  border: 2px solid var(--sp-08-acc);
  background: linear-gradient(180deg,transparent 55%,var(--sp-08-acc) 55%);
}

.sp-08__meta {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  color: var(--sp-08-mut);
}

.sp-08__intro {
  display: grid;
  gap: 14px;
  justify-items: center;
  text-align: center;
  padding-block: clamp(44px,9vh,96px) clamp(24px,5vh,48px);
}

.sp-08__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sp-08-acc);
}

.sp-08__intro-title {
  font-size: clamp(32px,5.6vw,64px);
  line-height: 1;
  letter-spacing: -.04em;
  font-weight: 730;
  max-inline-size: 20ch;
  text-wrap: balance;
}

.sp-08__intro-sub {
  font-size: clamp(14.5px,1.6vw,18px);
  line-height: 1.55;
  color: var(--sp-08-mut);
  max-inline-size: 52ch;
  text-wrap: pretty;
}

.sp-08__panel {
  timeline-scope: --sp-08-tl;
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
  block-size: min(66svh,560px);
  margin-inline: auto;
  max-inline-size: min(760px,calc(100% - clamp(24px,6vw,64px)));
  border: 1px solid var(--sp-08-line);
  border-radius: 18px;
  background: var(--sp-08-surface);
  overflow: hidden;
  box-shadow: 0 26px 60px -40px oklch(0.2 0.022 255/.7);
}

.sp-08__phead {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 18px;
  border-block-end: 1px solid var(--sp-08-line);
  background: color-mix(in oklch,var(--sp-08-surface) 92%,var(--sp-08-acc) 8%);
}

.sp-08__ptitle {
  display: flex;
  align-items: center;
  gap: 9px;
  min-inline-size: 0;
}

.sp-08__pdot {
  inline-size: 9px;
  block-size: 9px;
  border-radius: 50%;
  background: var(--sp-08-acc);
  box-shadow: 0 0 0 4px color-mix(in oklch,var(--sp-08-acc) 18%,transparent);
}

.sp-08__ph {
  font-size: 14.5px;
  font-weight: 700;
  letter-spacing: -.015em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sp-08__ppct {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  font-variant-numeric: tabular-nums;
  font-weight: 650;
  color: var(--sp-08-acc);
}

.sp-08__pfill {
  position: absolute;
  inset: auto 0 0 0;
  block-size: 3px;
  transform-origin: 0 50%;
  transform: scaleX(var(--sp-08-p));
  background: linear-gradient(90deg,var(--sp-08-acc),oklch(0.72 0.15 200));
}

.sp-08__body {
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-gutter: stable;
  scrollbar-width: thin;
  scrollbar-color: color-mix(in oklch,var(--sp-08-acc) 55%,transparent) transparent;
  padding: 20px clamp(16px,3vw,26px) 28px;
  display: grid;
  gap: 12px;
  align-content: start;
}

@supports (animation-timeline: scroll()) {
  .sp-08__body {
    scroll-timeline-name: --sp-08-tl;
    scroll-timeline-axis: block;
  }

  .sp-08__pfill {
    transform: scaleX(0);
    animation: sp-08-fill linear both;
    animation-timeline: --sp-08-tl;
  }
}

@keyframes sp-08-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

.sp-08__body:focus-visible {
  outline: 2px solid var(--sp-08-acc);
  outline-offset: -3px;
}

.sp-08__lede {
  font-size: 15.5px;
  line-height: 1.65;
  color: var(--sp-08-ink);
  text-wrap: pretty;
}

.sp-08__sh {
  margin-block-start: 8px;
  font-size: 13.4px;
  font-weight: 700;
  letter-spacing: .01em;
  color: var(--sp-08-acc);
}

.sp-08__bp {
  font-size: 14.6px;
  line-height: 1.68;
  color: var(--sp-08-mut);
  text-wrap: pretty;
}

.sp-08__bp code,
.sp-08__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.2 0.022 255/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-08__end {
  margin-block-start: 10px;
  padding: 12px 14px;
  border-radius: 12px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--sp-08-acc);
  background: color-mix(in oklch,var(--sp-08-acc) 9%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-08-acc) 22%,transparent);
}

.sp-08__after {
  display: grid;
  gap: 12px;
  padding-block: clamp(40px,8vh,90px);
}

.sp-08__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sp-08-acc);
}

.sp-08__h {
  font-size: clamp(22px,3.2vw,32px);
  line-height: 1.12;
  letter-spacing: -.032em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-08__p {
  max-inline-size: 62ch;
  font-size: 15.8px;
  line-height: 1.7;
  color: var(--sp-08-mut);
  text-wrap: pretty;
}

.sp-08__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-08-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-08-acc) 10%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-08-acc) 24%,transparent);
}

.sp-08__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(40px,8vh,100px) 24px;
  border-block-start: 1px solid var(--sp-08-line);
}

.sp-08__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-08-mut);
  text-align: center;
}

.sp-08__bar {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1180px)/2));
}

.sp-08__intro,
.sp-08__after {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 760px)/2));
}

@media (max-width: 640px) {
  .sp-08__panel {
    block-size: min(70svh,480px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-08 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-08');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const body = root.querySelector('#sp-08-body');
  const pct = root.querySelector('#sp-08-pct');
  const native = CSS.supports('animation-timeline', 'scroll()');
  let ticking = false;
  const paint = () => {
    ticking = false;
    const max = body.scrollHeight - body.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, body.scrollTop / max)) : 0;
    if (!native) root.style.setProperty('--sp-08-p', p.toFixed(4));
    const n = Math.round(p * 100);
    pct.textContent = n + '%';
    pct.setAttribute('aria-valuenow', String(n));
  };
  // note: listen on the panel, never on window — window scroll never fires for an inner div
  body.addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } }, { passive: true });
  addEventListener('resize', () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } }, { passive: true });
  paint();
})();
```
