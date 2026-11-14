---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-with-svg-icons-and-text-labels/"
title: "Vertical Tabs with SVG Icons and Text Labels"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "The pattern that gets alignment wrong in 90% of tutorials: an inline SVG next to a text label that stays optically centred at every font size and never…"
has_js: "false"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Tabs with SVG Icons and Text Labels
Source: https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-with-svg-icons-and-text-labels/

The pattern that gets alignment wrong in 90% of tutorials: an inline SVG next to a text label that stays optically centred at every font size and never shifts when the label wraps. Icons inherit colour through currentColor, animate their stroke on activation, and the whole rail is measured in a single --icon token so scaling the set is a one-line change.
## HTML
```html
<section class="vt-03" aria-label="Vertical tabs with SVG icons demo">
  <div class="vt-03__stage">
    <div class="vt-03__card" role="radiogroup" aria-label="Workspace sections">
      <div class="vt-03__rail">
        <p class="vt-03__brand"><span class="vt-03__dot" aria-hidden="true"></span>Northwind</p>
        <input class="vt-03__radio" type="radio" name="vt-03" id="vt-03-t1" checked>
        <label class="vt-03__tab" for="vt-03-t1"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z" stroke-width="1.7" stroke-linejoin="round"/></svg>Dashboard<span class="vt-03__badge">4</span></label>
        <input class="vt-03__radio" type="radio" name="vt-03" id="vt-03-t2">
        <label class="vt-03__tab" for="vt-03-t2"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 19V5m0 14h16M8 16V9m4 7V6m4 10v-4" stroke-width="1.7" stroke-linecap="round"/></svg>Analytics</label>
        <input class="vt-03__radio" type="radio" name="vt-03" id="vt-03-t3">
        <label class="vt-03__tab" for="vt-03-t3"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="9" cy="8" r="3.2" stroke-width="1.7"/><path d="M3 20a6 6 0 0 1 12 0m2.5-11.6a3 3 0 0 1 0 5.9M18 20a5.6 5.6 0 0 0-2-4.2" stroke-width="1.7" stroke-linecap="round"/></svg>Audience</label>
        <input class="vt-03__radio" type="radio" name="vt-03" id="vt-03-t4">
        <label class="vt-03__tab" for="vt-03-t4"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="3" stroke-width="1.7"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09a1.65 1.65 0 0 0-1-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09a1.65 1.65 0 0 0 1.51-1 1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33h.01a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82v.01a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>Settings</label>
      </div>
      <div class="vt-03__panels">
        <article class="vt-03__panel" id="vt-03-p1"><p class="vt-03__kicker">Dashboard</p><h3 class="vt-03__h">flex · align-items:center · gap</h3><p class="vt-03__p">Three declarations keep an inline SVG optically locked to its label at any type scale. The badge floats right with <code>margin-inline-start:auto</code>.</p></article>
        <article class="vt-03__panel" id="vt-03-p2"><p class="vt-03__kicker">Analytics</p><h3 class="vt-03__h">flex:none, or it squishes</h3><p class="vt-03__p">An SVG is a shrinkable flex item by default. Long labels compress it into an ellipse — the bug that only appears in production copy.</p></article>
        <article class="vt-03__panel" id="vt-03-p3"><p class="vt-03__kicker">Audience</p><h3 class="vt-03__h">currentColor does the theming</h3><p class="vt-03__p">Every icon strokes with <code>currentColor</code>, so hover, active and focus states need no icon-specific CSS at all.</p></article>
        <article class="vt-03__panel" id="vt-03-p4"><p class="vt-03__kicker">Settings</p><h3 class="vt-03__h">The active icon draws itself</h3><p class="vt-03__p">A <code>stroke-dashoffset</code> sweep plus a 1.08 scale pop, both compositor-only and both silent under reduced motion.</p></article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-03-bg);
  --vt-03-bg: oklch(0.965 0.012 85);
  --vt-03-card: oklch(1 0 0);
  --vt-03-rail: oklch(0.985 0.008 85);
  --vt-03-ink: oklch(0.25 0.03 60);
  --vt-03-mut: oklch(0.56 0.025 60);
  --vt-03-acc: oklch(0.58 0.17 32);
  --vt-03-line: oklch(0.25 0.03 60/.12);
  --vt-03-icon: 20px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-03-ink);
}

.vt-03 *,
.vt-03 *::before,
.vt-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-03__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  padding: clamp(20px,5vw,64px);
  background: radial-gradient(85% 60% at 50% 100%,oklch(0.94 0.045 45/.6),transparent);
}

.vt-03__card {
  width: min(94vw,880px);
  display: grid;
  grid-template-columns: clamp(180px,30%,262px) 1fr;
  background: var(--vt-03-card);
  border: 1px solid var(--vt-03-line);
  border-radius: 20px;
  box-shadow: 0 24px 64px -30px oklch(0.25 0.03 60/.4);
  overflow: hidden;
}

.vt-03__rail {
  display: grid;
  align-content: start;
  gap: 2px;
  padding: 14px 10px;
  background: var(--vt-03-rail);
  border-right: 1px solid var(--vt-03-line);
}

.vt-03__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  padding: 6px 10px 14px;
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: .02em;
  color: var(--vt-03-mut);
}

.vt-03__dot {
  inline-size: 9px;
  block-size: 9px;
  border-radius: 99px;
  background: var(--vt-03-acc);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--vt-03-acc) 18%,transparent);
}

.vt-03__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.vt-03__tab {
  display: flex;
  align-items: center;
  gap: .7rem;
  min-height: 46px;
  padding: 0 12px;
  border-radius: 11px;
  font-size: 14.4px;
  font-weight: 600;
  color: var(--vt-03-mut);
  cursor: pointer;
  transition: color .2s ease,background .2s ease;
}

.vt-03__tab svg {
  inline-size: var(--vt-03-icon);
  block-size: var(--vt-03-icon);
  flex: none;
  stroke: currentColor;
  stroke-dasharray: 96;
  stroke-dashoffset: 0;
  transition: transform .34s cubic-bezier(.34,1.4,.5,1);
}

.vt-03__badge {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--vt-03-acc) 14%,transparent);
  color: var(--vt-03-acc);
}

.vt-03__tab:hover {
  color: var(--vt-03-ink);
  background: oklch(0.25 0.03 60/.05);
}

.vt-03__radio:checked+.vt-03__tab {
  color: var(--vt-03-acc);
  background: color-mix(in oklch,var(--vt-03-acc) 11%,transparent);
}

.vt-03__radio:checked+.vt-03__tab svg {
  transform: scale(1.08);
  animation: vt-03-draw .62s cubic-bezier(.4,.6,.3,1);
}

.vt-03__radio:focus-visible+.vt-03__tab {
  outline: 2px solid var(--vt-03-acc);
  outline-offset: 2px;
}

@keyframes vt-03-draw {
  from {
    stroke-dashoffset: 96;
  }

  to {
    stroke-dashoffset: 0;
  }
}

.vt-03__panels {
  display: grid;
  min-height: clamp(240px,32vw,290px);
  padding: clamp(22px,3.6vw,42px);
}

.vt-03__panel {
  grid-area: 1/1;
  align-content: center;
  display: grid;
  gap: 11px;
  opacity: 0;
  visibility: hidden;
  transform: translateX(10px);
  transition: opacity .3s ease,transform .36s cubic-bezier(.32,.72,.3,1),visibility 0s .36s;
}

.vt-03__card:has(#vt-03-t1:checked) #vt-03-p1,
.vt-03__card:has(#vt-03-t2:checked) #vt-03-p2,
.vt-03__card:has(#vt-03-t3:checked) #vt-03-p3,
.vt-03__card:has(#vt-03-t4:checked) #vt-03-p4 {
  opacity: 1;
  visibility: visible;
  transform: none;
  transition-delay: 0s;
}

.vt-03__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--vt-03-acc);
}

.vt-03__h {
  font-size: clamp(19px,2.4vw,25px);
  line-height: 1.2;
  letter-spacing: -.022em;
  font-weight: 680;
  text-wrap: balance;
}

.vt-03__p {
  max-width: 44ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--vt-03-mut);
  text-wrap: pretty;
}

.vt-03__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.25 0.03 60/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (max-width: 640px) {
  .vt-03__card {
    grid-template-columns: 1fr;
  }

  .vt-03__rail {
    border-right: 0;
    border-bottom: 1px solid var(--vt-03-line);
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-03 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
