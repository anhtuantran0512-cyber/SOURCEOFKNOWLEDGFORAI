---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/counter-chip/"
title: "Tag Badge with Notification Count Label"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "Count badges engineered like the platform teams do it: min-width so 1, 12 and 99+ all keep shape, tabular numerals so 8→9 doesn't wiggle the pill, a…"
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tag Badge with Notification Count Label
Source: https://codefronts.com/snippets/css-tags-chips/counter-chip/

Count badges engineered like the platform teams do it: min-width so 1, 12 and 99+ all keep shape, tabular numerals so 8→9 doesn't wiggle the pill, a surface-colored ring so the badge reads as punched through its icon, and @starting-style pop-in so a badge that appears mid-session announces itself. The live half is pure CSS: mark inbox rows read and a CSS counter re-renders the tab's badge — including hiding it entirely at zero, via :has().
## HTML
```html
<section class="ctc-20" aria-label="Notification count badge demo">
  <div class="ctc-20__stage">
    <div class="ctc-20__wrap">
      <header class="ctc-20__head">
        <p class="ctc-20__kicker">Count badges · anatomy + live counter</p>
        <h1>1, 12 and 99+ keep their shape</h1>
      </header>
      <div class="ctc-20__panel">
        <p class="ctc-20__lab">01 · Anatomy — min-width circle→pill, cutout ring, tabular digits</p>
        <div class="ctc-20__row">
          <span class="ctc-20__icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v12H8l-4 4z"/></svg><b class="ctc-20__badge">1</b></span>
          <span class="ctc-20__icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v12H8l-4 4z"/></svg><b class="ctc-20__badge">12</b></span>
          <span class="ctc-20__icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v12H8l-4 4z"/></svg><b class="ctc-20__badge">99+</b></span>
          <span class="ctc-20__icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 19v-8a6 6 0 0 1 12 0v8M4 19h16M10 21h4"/></svg><b class="ctc-20__badge ctc-20__badge--dot" aria-label="new notifications"></b></span>
          <span class="ctc-20__icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h14v16H5zM9 8h6M9 12h6M9 16h4"/></svg><b class="ctc-20__badge ctc-20__badge--mut">3</b></span>
        </div>
      </div>
      <div class="ctc-20__panel ctc-20__app">
        <p class="ctc-20__lab">02 · Live — tick rows read; the tab badge is a CSS counter, gone at zero</p>
        <nav class="ctc-20__tabs" aria-label="Mail folders">
          <span class="ctc-20__tab is-on">Inbox<b class="ctc-20__badge ctc-20__tabbadge" aria-hidden="true"></b><i class="ctc-20__sr">unread messages in inbox</i></span>
          <span class="ctc-20__tab">Drafts<b class="ctc-20__badge ctc-20__badge--mut">2</b></span>
          <span class="ctc-20__tab">Archive</span>
        </nav>
        <ul class="ctc-20__mail">
          <li><label><input type="checkbox" class="ctc-20__sr"><span class="ctc-20__read" aria-hidden="true"></span><b>Mara Voss</b><span>Design review notes — 14 comments resolved…</span><time>09:12</time></label></li>
          <li><label><input type="checkbox" class="ctc-20__sr"><span class="ctc-20__read" aria-hidden="true"></span><b>Linear</b><span>4 issues moved to In Progress by the auto…</span><time>08:47</time></label></li>
          <li><label><input type="checkbox" class="ctc-20__sr" checked><span class="ctc-20__read" aria-hidden="true"></span><b>Jonas Reid</b><span>Re: token naming — agreed, shipping the…</span><time>Yesterday</time></label></li>
          <li><label><input type="checkbox" class="ctc-20__sr"><span class="ctc-20__read" aria-hidden="true"></span><b>Vercel</b><span>Deployment ready: codefronts.com (prod)…</span><time>Yesterday</time></label></li>
        </ul>
        <p class="ctc-20__hint">Each checkbox = read state. Unread rows <code>counter-increment</code>; the badge's <code>::after</code> renders the total; <code>:has()</code> hides it at zero instead of showing “0”.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-20,
.ctc-20 *,
.ctc-20 *::before,
.ctc-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-20 {
  --bg: oklch(0.965 0.008 255);
  --panel: oklch(0.997 0.002 255);
  --ink: oklch(0.24 0.025 260);
  --mut: oklch(0.5 0.02 260);
  --line: oklch(0.88 0.012 255);
  --red: oklch(0.6 0.21 25);
  --acc: oklch(0.55 0.17 262);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-20__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 12% -10%,color-mix(in oklch,var(--red) 9%,transparent),transparent 62%),var(--bg);
  container: ctc20/inline-size;
}

.ctc-20__wrap {
  width: min(640px,100%);
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ctc-20__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ctc-20__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--red);
}

.ctc-20__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 4px;
}

.ctc-20__panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
}

.ctc-20__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 16px;
}

.ctc-20__row {
  display: flex;
  flex-wrap: wrap;
  gap: 26px;
  align-items: center;
  padding: 6px 4px;
}

.ctc-20__icon {
  position: relative;
  display: inline-grid;
  place-items: center;
  width: 46px;
  height: 46px;
  border-radius: 14px;
  background: oklch(0.94 0.008 255);
  border: 1px solid var(--line);
}

.ctc-20__icon svg {
  width: 22px;
  height: 22px;
  fill: none;
  stroke: var(--mut);
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.ctc-20__badge {
  position: absolute;
  top: -7px;
  right: -7px;
  min-width: 20px;
  height: 20px;
  padding: 0 6px;
  border-radius: 99px;
  border: 2.5px solid var(--panel);
  background: var(--red);
  color: oklch(0.98 0.005 255);
  font-size: 11px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  font-style: normal;
  display: grid;
  place-items: center;
  line-height: 1;
}

.ctc-20__badge--dot {
  min-width: 13px;
  height: 13px;
  padding: 0;
  top: -4px;
  right: -4px;
}

.ctc-20__badge--mut {
  background: oklch(0.6 0.02 260);
}

.ctc-20__tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
}

.ctc-20__tab {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 40px;
  padding: 0 16px;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: oklch(0.975 0.005 255);
  font-size: 13px;
  font-weight: 700;
  color: var(--mut);
}

.ctc-20__tab.is-on {
  background: var(--ink);
  border-color: var(--ink);
  color: oklch(0.97 0.005 255);
}

.ctc-20__tab .ctc-20__badge {
  position: static;
  border-width: 0;
  min-width: 19px;
  height: 19px;
}

.ctc-20__tabbadge {
  transition: scale .35s cubic-bezier(.34,1.56,.64,1),opacity .3s;
}

.ctc-20__tabbadge::after {
  content: counter(ctc20n);
}

.ctc-20__app {
  counter-reset: ctc20n;
}

.ctc-20__app:not(:has(.ctc-20__mail input:not(:checked))) .ctc-20__tabbadge {
  display: none;
}

@starting-style {
  .ctc-20__tabbadge {
    scale: .3;
    opacity: 0;
  }
}

.ctc-20__mail {
  list-style: none;
  display: flex;
  flex-direction: column;
}

.ctc-20__mail li:not(:has(:checked)) {
  counter-increment: ctc20n;
}

.ctc-20__mail label {
  display: grid;
  grid-template-columns: auto auto 1fr auto;
  align-items: center;
  gap: 11px;
  padding: 11px 10px;
  border-radius: 11px;
  cursor: pointer;
  transition: background .18s;
}

.ctc-20__mail label:hover {
  background: oklch(0.955 0.008 255);
}

.ctc-20__mail li:has(:focus-visible) label {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.ctc-20__read {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--acc);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--acc) 22%,transparent);
  transition: background .25s,box-shadow .25s,scale .25s;
}

.ctc-20__mail li:has(:checked) .ctc-20__read {
  background: transparent;
  box-shadow: inset 0 0 0 1.5px var(--line);
  scale: .85;
}

.ctc-20__mail b {
  font-size: 13.5px;
  font-weight: 750;
  white-space: nowrap;
}

.ctc-20__mail li:has(:checked) b {
  font-weight: 550;
  color: var(--mut);
}

.ctc-20__mail label>span:not(.ctc-20__read) {
  font-size: 12.5px;
  color: var(--mut);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.ctc-20__mail time {
  font-size: 11px;
  color: var(--mut);
  font-variant-numeric: tabular-nums;
}

.ctc-20__hint {
  margin-top: 10px;
  padding-top: 12px;
  border-top: 1px dashed var(--line);
  font-size: 12px;
  line-height: 1.6;
  color: var(--mut);
}

.ctc-20__hint code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(0.93 0.008 255);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

@container ctc20 (width < 480px) {
  .ctc-20__mail label {
    grid-template-columns: auto auto 1fr;
  }

  .ctc-20__mail time {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ctc-20 * {
    transition-duration: .01ms !important;
  }
}
```
