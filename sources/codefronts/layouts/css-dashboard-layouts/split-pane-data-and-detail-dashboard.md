---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/split-pane-data-and-detail-dashboard/"
title: "Split-Pane Data & Detail Dashboard"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "The email-client trinity — 216px nav rail, 320px scrollable master list, fluid detail pane — built as one grid row."
has_js: "false"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split-Pane Data & Detail Dashboard
Source: https://codefronts.com/layouts/css-dashboard-layouts/split-pane-data-and-detail-dashboard/

The email-client trinity — 216px nav rail, 320px scrollable master list, fluid detail pane — built as one grid row. Selection is a radio group: click a conversation and :has() swaps the detail pane, highlights the row, and clears its unread dot, all without JavaScript. The list scrolls independently while nav and detail stay put; this is the skeleton under every CRM, inbox and ticketing tool you have ever used.
## HTML
```html
<section class="cdl-04" aria-label="Master-detail split pane demo">
  <div class="cdl-04__split">
    <nav class="cdl-04__nav" aria-label="Folders">
      <strong class="cdl-04__brand"><span aria-hidden="true"></span>Helpdesk</strong>
      <a href="#inbox" aria-current="page" class="cdl-04__on">Inbox<b>3</b></a>
      <a href="#assigned">Assigned to me<b>1</b></a>
      <a href="#snoozed">Snoozed</a>
      <a href="#done">Resolved</a>
      <a href="#spam">Spam</a>
    </nav>
    <div class="cdl-04__list" role="group" aria-label="Conversations — arrow keys change selection">
      <p class="cdl-04__listhead">Inbox · 3 open</p>
      <label class="cdl-04__row"><input type="radio" name="cdl04" id="cdl04-r1" checked>
        <i class="cdl-04__dot" aria-hidden="true"></i><span class="cdl-04__av" aria-hidden="true">MK</span>
        <span class="cdl-04__meta"><b>Maya Krishnan</b><em>Checkout fails on step 3</em><small>Payments · 12m</small></span>
      </label>
      <label class="cdl-04__row"><input type="radio" name="cdl04" id="cdl04-r2">
        <i class="cdl-04__dot" aria-hidden="true"></i><span class="cdl-04__av cdl-04__av2" aria-hidden="true">TW</span>
        <span class="cdl-04__meta"><b>Tom Whitely</b><em>Export CSV missing columns</em><small>Reports · 41m</small></span>
      </label>
      <label class="cdl-04__row"><input type="radio" name="cdl04" id="cdl04-r3">
        <i class="cdl-04__dot" aria-hidden="true"></i><span class="cdl-04__av cdl-04__av3" aria-hidden="true">LB</span>
        <span class="cdl-04__meta"><b>Lena Brandt</b><em>Upgrade to annual plan</em><small>Billing · 2h</small></span>
      </label>
      <label class="cdl-04__row cdl-04__read"><span class="cdl-04__av cdl-04__av4" aria-hidden="true">JP</span><input type="radio" name="cdl04" id="cdl04-r4">
        <span class="cdl-04__meta"><b>Jonas Peel</b><em>Thanks — all sorted!</em><small>Resolved · 1d</small></span>
      </label>
      <label class="cdl-04__row cdl-04__read"><span class="cdl-04__av" aria-hidden="true">SR</span><input type="radio" name="cdl04" id="cdl04-r5">
        <span class="cdl-04__meta"><b>Sofia Reyes</b><em>API key rotation question</em><small>Resolved · 2d</small></span>
      </label>
    </div>
    <main class="cdl-04__detail">
      <article class="cdl-04__pane cdl-04__pane--1">
        <header><h2>Checkout fails on step 3</h2><div class="cdl-04__chips"><span class="cdl-04__chip cdl-04__hot">Urgent</span><span class="cdl-04__chip">Payments</span><span class="cdl-04__chip">Pro plan</span></div></header>
        <div class="cdl-04__msgs">
          <p class="cdl-04__msg">Hi — card entry works but the confirm button spins forever on step 3. Console shows a 402 from /charge. Started this morning.</p>
          <p class="cdl-04__msg cdl-04__mine">Thanks Maya — we shipped a payments change at 09:20 UTC and are rolling it back now. Can you retry in ~10 minutes?</p>
          <p class="cdl-04__msg">Will do. Appreciate the fast reply!</p>
        </div>
        <footer class="cdl-04__reply"><span>Reply to Maya…</span><button type="button">Send</button></footer>
      </article>
      <article class="cdl-04__pane cdl-04__pane--2">
        <header><h2>Export CSV missing columns</h2><div class="cdl-04__chips"><span class="cdl-04__chip">Reports</span><span class="cdl-04__chip">Team plan</span></div></header>
        <div class="cdl-04__msgs">
          <p class="cdl-04__msg">The order export dropped the “tax region” and “SKU” columns after the last update. We rely on both for reconciliation.</p>
          <p class="cdl-04__msg cdl-04__mine">Confirmed — a regression in the new exporter. Fix is in review; I'll attach a corrected export for the meantime.</p>
        </div>
        <footer class="cdl-04__reply"><span>Reply to Tom…</span><button type="button">Send</button></footer>
      </article>
      <article class="cdl-04__pane cdl-04__pane--3">
        <header><h2>Upgrade to annual plan</h2><div class="cdl-04__chips"><span class="cdl-04__chip">Billing</span><span class="cdl-04__chip cdl-04__nice">Expansion</span></div></header>
        <div class="cdl-04__msgs">
          <p class="cdl-04__msg">We'd like to move our 14 seats to annual billing — is there a discount, and can the switch happen mid-cycle?</p>
          <p class="cdl-04__msg cdl-04__mine">Absolutely: annual is 2 months free, and we prorate the remainder of your current cycle automatically. I can apply it today if you confirm.</p>
        </div>
        <footer class="cdl-04__reply"><span>Reply to Lena…</span><button type="button">Send</button></footer>
      </article>
      <article class="cdl-04__pane cdl-04__pane--4"><div class="cdl-04__empty"><b>Resolved · Jonas Peel</b><p>“Thanks — all sorted!” This conversation is closed. Reopen it from the ··· menu.</p></div></article>
      <article class="cdl-04__pane cdl-04__pane--5"><div class="cdl-04__empty"><b>Resolved · Sofia Reyes</b><p>API keys can be rotated under Settings → Developers. This conversation is closed.</p></div></article>
    </main>
  </div>
</section>
```
## CSS
```css
.cdl-04,
.cdl-04 *,
.cdl-04 *::before,
.cdl-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-04 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --bg: oklch(0.98 0.004 250);
  --panel: oklch(1 0 0);
  --edge: oklch(0.91 0.01 250);
  --ink: oklch(0.26 0.02 250);
  --mut: oklch(0.55 0.02 250);
  --acc: oklch(0.55 0.18 255);
  --sel: color-mix(in oklch,oklch(0.55 0.18 255) 8%,white);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cdl-04__split {
  width: 100%;
  height: 100vh;
  display: grid;
  grid-template-columns: 216px 320px minmax(280px,1fr);
  min-width: min-content;
  border: 1px solid var(--edge);
  overflow: hidden;
  background: var(--panel);
  box-shadow: 0 24px 50px -30px oklch(0.4 0.04 250 / .3);
}

.cdl-04__nav {
  background: oklch(0.965 0.008 250);
  border-right: 1px solid var(--edge);
  padding: 16px 10px;
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.cdl-04__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 14.5px;
  padding: 0 10px;
  margin-bottom: 14px;
}

.cdl-04__brand span {
  width: 18px;
  height: 18px;
  border-radius: 6px;
  background: conic-gradient(from 210deg,var(--acc),oklch(0.7 0.13 200));
}

.cdl-04__nav a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 9px 12px;
  border-radius: 9px;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  color: var(--mut);
  transition: background .15s,color .15s;
}

.cdl-04__nav a:hover {
  background: oklch(0.93 0.01 250);
  color: var(--ink);
}

.cdl-04__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cdl-04__nav a.cdl-04__on {
  background: color-mix(in oklch,var(--acc) 11%,transparent);
  color: var(--acc);
}

.cdl-04__nav b {
  font-size: 10.5px;
  background: var(--acc);
  color: oklch(1 0 0);
  border-radius: 999px;
  padding: 1px 7px;
}

.cdl-04__nav a:not(.cdl-04__on) b {
  background: oklch(0.85 0.02 250);
  color: var(--mut);
}

.cdl-04__list {
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-gutter: stable;
  min-height: 0;
  border-right: 1px solid var(--edge);
  background: var(--bg);
}

.cdl-04__listhead {
  position: sticky;
  top: 0;
  z-index: 1;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
  padding: 12px 16px 9px;
  background: color-mix(in oklch,var(--bg) 85%,transparent);
  backdrop-filter: blur(6px);
}

.cdl-04__row {
  position: relative;
  display: flex;
  gap: 10px;
  align-items: center;
  padding: 13px 14px;
  border-bottom: 1px solid color-mix(in oklch,var(--edge) 55%,transparent);
  cursor: pointer;
  transition: background .15s;
  border-left: 3px solid transparent;
}

.cdl-04__row:hover {
  background: oklch(0.955 0.008 250);
}

.cdl-04__row input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cdl-04__row:has(:checked) {
  background: var(--sel);
  border-left-color: var(--acc);
}

.cdl-04__row:has(:focus-visible) {
  outline: 2px solid var(--acc);
  outline-offset: -3px;
}

.cdl-04__dot {
  width: 8px;
  height: 8px;
  flex: none;
  border-radius: 50%;
  background: var(--acc);
  transition: opacity .3s,scale .3s;
}

.cdl-04__row:has(:checked) .cdl-04__dot {
  opacity: 0;
  scale: .3;
}

.cdl-04__av {
  flex: none;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 11px;
  font-weight: 700;
  color: oklch(1 0 0);
  background: linear-gradient(140deg,oklch(0.62 0.15 255),oklch(0.55 0.16 290));
}

.cdl-04__av2 {
  background: linear-gradient(140deg,oklch(0.65 0.13 190),oklch(0.55 0.15 230));
}

.cdl-04__av3 {
  background: linear-gradient(140deg,oklch(0.68 0.14 60),oklch(0.6 0.17 25));
}

.cdl-04__av4 {
  background: linear-gradient(140deg,oklch(0.6 0.03 250),oklch(0.45 0.03 250));
}

.cdl-04__read {
  opacity: .72;
}

.cdl-04__meta {
  min-width: 0;
  display: grid;
  gap: 1px;
}

.cdl-04__meta b {
  font-size: 13px;
}

.cdl-04__meta em {
  font-style: normal;
  font-size: 12.5px;
  color: var(--ink);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cdl-04__read .cdl-04__meta em {
  color: var(--mut);
}

.cdl-04__meta small {
  font-size: 11px;
  color: var(--mut);
}

.cdl-04__detail {
  min-width: 0;
  background: var(--panel);
}

.cdl-04__pane {
  display: none;
  height: 100%;
  flex-direction: column;
}

.cdl-04__split:has(#cdl04-r1:checked) .cdl-04__pane--1 {
  display: flex;
}

.cdl-04__split:has(#cdl04-r2:checked) .cdl-04__pane--2 {
  display: flex;
}

.cdl-04__split:has(#cdl04-r3:checked) .cdl-04__pane--3 {
  display: flex;
}

.cdl-04__split:has(#cdl04-r4:checked) .cdl-04__pane--4 {
  display: flex;
}

.cdl-04__split:has(#cdl04-r5:checked) .cdl-04__pane--5 {
  display: flex;
}

.cdl-04__pane header {
  padding: 20px 24px 14px;
  border-bottom: 1px solid var(--edge);
}

.cdl-04__pane h2 {
  font-size: 17px;
  letter-spacing: -.01em;
  margin-bottom: 10px;
}

.cdl-04__chips {
  display: flex;
  gap: 7px;
  flex-wrap: wrap;
}

.cdl-04__chip {
  font-size: 11px;
  font-weight: 600;
  color: var(--mut);
  border: 1px solid var(--edge);
  border-radius: 999px;
  padding: 4px 10px;
  background: var(--bg);
}

.cdl-04__hot {
  color: oklch(0.55 0.19 25);
  border-color: color-mix(in oklch,oklch(0.55 0.19 25) 35%,transparent);
  background: color-mix(in oklch,oklch(0.55 0.19 25) 8%,white);
}

.cdl-04__nice {
  color: oklch(0.52 0.14 155);
  border-color: color-mix(in oklch,oklch(0.52 0.14 155) 35%,transparent);
  background: color-mix(in oklch,oklch(0.52 0.14 155) 8%,white);
}

.cdl-04__msgs {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: 20px 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.cdl-04__msg {
  max-width: 78%;
  font-size: 13.5px;
  line-height: 1.5;
  padding: 11px 15px;
  border-radius: 14px 14px 14px 4px;
  background: var(--bg);
  border: 1px solid var(--edge);
}

.cdl-04__mine {
  align-self: flex-end;
  border-radius: 14px 14px 4px 14px;
  background: color-mix(in oklch,var(--acc) 10%,white);
  border-color: color-mix(in oklch,var(--acc) 25%,var(--edge));
}

.cdl-04__reply {
  display: flex;
  gap: 10px;
  align-items: center;
  margin: 0 24px 20px;
  padding: 8px 8px 8px 16px;
  border: 1px solid var(--edge);
  border-radius: 12px;
  background: var(--bg);
}

.cdl-04__reply span {
  flex: 1;
  font-size: 13px;
  color: var(--mut);
}

.cdl-04__reply button {
  border: none;
  border-radius: 8px;
  padding: 9px 16px;
  font: 600 12.5px 'Segoe UI',system-ui,sans-serif;
  color: oklch(1 0 0);
  background: var(--acc);
  cursor: pointer;
}

.cdl-04__reply button:hover {
  background: color-mix(in oklch,var(--acc) 88%,black);
}

.cdl-04__reply button:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cdl-04__empty {
  margin: auto;
  max-width: 360px;
  text-align: center;
  display: grid;
  gap: 8px;
  padding: 24px;
}

.cdl-04__empty b {
  font-size: 14px;
}

.cdl-04__empty p {
  font-size: 13px;
  color: var(--mut);
  line-height: 1.55;
}

@container (max-width: 820px) {
  .cdl-04__split {
    grid-template-columns: 280px minmax(280px,1fr);
  }

  .cdl-04__nav {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cdl-04 * {
    transition: none !important;
  }
}
```
