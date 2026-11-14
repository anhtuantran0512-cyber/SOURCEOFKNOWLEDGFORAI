---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-timeline-alert-feed-component/"
title: "CSS Timeline Alert Feed Component"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Feed architecture, twice: a timeline whose continuous rail is one border on the list (not per-item fragments), with color+shape-coded markers, semantic…"
has_js: "false"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Timeline Alert Feed Component
Source: https://codefronts.com/snippets/css-notifications/css-timeline-alert-feed-component/

Feed architecture, twice: a timeline whose continuous rail is one border on the list (not per-item fragments), with color+shape-coded markers, semantic <time> stamps, an unread divider and staggered entry — and a day-grouped scrolling feed where each date header position:stickies inside the panel and hands off to the next, the pattern every activity log ships.
## HTML
```html
<div class="ntf-29-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-29a" aria-label="Timeline alert feed with typed markers">
  <div class="ntf-29a__panel">
    <h2 class="ntf-29a__h">Activity</h2>
    <ul class="ntf-29a__feed">
      <li class="ntf-29a__item" style="--c:oklch(0.62 0.19 25);--i:0"><span class="ntf-29a__tx"><b>Sign-in blocked</b><small>wrong password × 3 · Lagos, NG</small></span><time class="ntf-29a__t" datetime="2027-02-18T14:02" title="14:02 today">2m</time></li>
      <li class="ntf-29a__item ntf-29a__item--ring" style="--c:oklch(0.68 0.15 65);--i:1"><span class="ntf-29a__tx"><b>Disk 85% on db-2</b><small>projected full in 9 days</small></span><time class="ntf-29a__t" datetime="2027-02-18T13:11" title="13:11 today">53m</time></li>
      <li class="ntf-29a__divider" role="separator" aria-label="Read below"><i></i><b>last seen</b><i></i></li>
      <li class="ntf-29a__item ntf-29a__item--sq" style="--c:oklch(0.62 0.13 250);--i:2"><span class="ntf-29a__tx"><b>Deploy #4020 finished</b><small>api · 3m 12s · no drift</small></span><time class="ntf-29a__t" datetime="2027-02-18T09:40" title="09:40 today">6h</time></li>
      <li class="ntf-29a__item" style="--c:oklch(0.62 0.15 155);--i:3"><span class="ntf-29a__tx"><b>Backups verified</b><small>nightly · 212 GB · checksums ok</small></span><time class="ntf-29a__t" datetime="2027-02-18T04:00" title="04:00 today">12h</time></li>
    </ul>
    <p class="ntf-29a__cap">one ::before rail on the list · markers typed by <b>color + shape</b> · real &lt;time datetime&gt; stamps</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-29b" aria-label="Scrolling feed with sticky day headers">
  <div class="ntf-29b__panel">
    <div class="ntf-29b__scroll">
      <section class="ntf-29b__day"><h3 class="ntf-29b__stick">Today</h3>
        <div class="ntf-29b__row"><i style="--c:oklch(0.72 0.16 25)" aria-hidden="true"></i><span><b>Payment retry failed</b><small>invoice #2047 · card expired</small></span><time datetime="2027-02-18T15:20">15:20</time></div>
        <div class="ntf-29b__row ntf-29b__row--new"><i style="--c:oklch(0.75 0.13 200)" aria-hidden="true"></i><span><b>New API key created</b><small>by dana@ · scope: read</small></span><time datetime="2027-02-18T11:05">11:05</time></div>
      </section>
      <section class="ntf-29b__day"><h3 class="ntf-29b__stick">Yesterday</h3>
        <div class="ntf-29b__row"><i style="--c:oklch(0.78 0.15 160)" aria-hidden="true"></i><span><b>Weekly report ready</b><small>opens: 41% · clicks: 9%</small></span><time datetime="2027-02-17T18:00">18:00</time></div>
        <div class="ntf-29b__row"><i style="--c:oklch(0.8 0.13 85)" aria-hidden="true"></i><span><b>3 members inactive 30d</b><small>seats you might reclaim</small></span><time datetime="2027-02-17T09:12">09:12</time></div>
      </section>
      <section class="ntf-29b__day"><h3 class="ntf-29b__stick">Feb 14</h3>
        <div class="ntf-29b__row"><i style="--c:oklch(0.62 0.13 250)" aria-hidden="true"></i><span><b>Domain verified</b><small>codefronts.com · DNS ok</small></span><time datetime="2027-02-14T16:44">16:44</time></div>
        <div class="ntf-29b__row"><i style="--c:oklch(0.78 0.15 160)" aria-hidden="true"></i><span><b>2FA enabled workspace-wide</b><small>enforced for 12 members</small></span><time datetime="2027-02-14T10:02">10:02</time></div>
      </section>
    </div>
    <p class="ntf-29b__cap">scroll the panel — two sticky headers at the same <b>top</b> push each other out; the handoff is native</p>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-29-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-29-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-29a,
.ntf-29a *,
.ntf-29a *::before,
.ntf-29a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-29a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f5f6f8,#eaecf0);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-29a__panel {
  --panel: #fff;
  width: min(420px,100%);
  padding: 24px;
  border-radius: 20px;
  background: var(--panel);
  border: 1px solid rgba(29,33,43,.1);
  box-shadow: 0 26px 60px -34px rgba(29,33,43,.5);
}

.ntf-29a__h {
  font-size: 19px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: #1d212b;
}

.ntf-29a__feed {
  position: relative;
  list-style: none;
  margin-top: 16px;
  padding-inline-start: 24px;
}

.ntf-29a__feed::before {
  content: "";
  position: absolute;
  inset-block: 8px;
  inset-inline-start: 5px;
  width: 2px;
  border-radius: 2px;
  background: rgba(29,33,43,.12);
}

.ntf-29a__item {
  position: relative;
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  padding: 11px 0;
  animation: ntf-29a-in .45s cubic-bezier(.22,1.2,.36,1) both;
  animation-delay: calc(var(--i) * .08s);
}

.ntf-29a__item::before {
  content: "";
  position: absolute;
  inset-inline-start: -24px;
  top: 16px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--c);
  border: 3px solid var(--panel);
  box-shadow: 0 0 0 1px color-mix(in oklch,var(--c),transparent 55%);
}

.ntf-29a__item--ring::before {
  background: var(--panel);
  border: 3px solid var(--c);
}

.ntf-29a__item--sq::before {
  border-radius: 3px;
}

.ntf-29a__tx {
  display: grid;
  gap: 1px;
  min-width: 0;
}

.ntf-29a__tx b {
  font-size: 13.5px;
  font-weight: 600;
  color: #1d212b;
}

.ntf-29a__tx small {
  font-size: 11.5px;
  color: rgba(29,33,43,.52);
}

.ntf-29a__t {
  flex: none;
  font-size: 11px;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  color: rgba(29,33,43,.45);
}

.ntf-29a__divider {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 0;
}

.ntf-29a__divider i {
  flex: 1;
  height: 1px;
  background: oklch(0.62 0.19 25 / .4);
}

.ntf-29a__divider b {
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.19 25);
}

.ntf-29a__cap {
  margin-top: 14px;
  font-size: 11.5px;
  line-height: 1.6;
  color: rgba(29,33,43,.45);
  text-wrap: pretty;
}

.ntf-29a__cap b {
  color: #1d212b;
}

@keyframes ntf-29a-in {
  from {
    opacity: 0;
    translate: 0 8px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-29a__item {
    animation: ntf-29a-rm .2s ease both;
    animation-delay: 0s;
  }

  @keyframes ntf-29a-rm {
    from {
      opacity: 0;
    }
  }
}

.ntf-29b,
.ntf-29b *,
.ntf-29b *::before,
.ntf-29b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-29b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#151a24,#0b0e14);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-29b__panel {
  width: min(410px,100%);
}

.ntf-29b__scroll {
  height: min(52vh,420px);
  overflow-y: auto;
  border-radius: 18px;
  background: rgba(255,255,255,.045);
  border: 1px solid rgba(165,190,230,.16);
  overscroll-behavior: contain;
}

.ntf-29b__stick {
  position: sticky;
  top: 0;
  z-index: 2;
  padding: 10px 18px 8px;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: rgba(212,224,246,.55);
  background: linear-gradient(180deg,#161b27 75%,rgba(22,27,39,0));
  backdrop-filter: blur(4px);
}

.ntf-29b__row {
  display: flex;
  align-items: baseline;
  gap: 12px;
  padding: 12px 18px;
  transition: background .15s;
}

.ntf-29b__row:hover {
  background: rgba(255,255,255,.04);
}

.ntf-29b__row i {
  flex: none;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--c);
  translate: 0 -1px;
}

.ntf-29b__row span {
  display: grid;
  gap: 1px;
  min-width: 0;
  flex: 1;
}

.ntf-29b__row b {
  font-size: 13px;
  font-weight: 600;
  color: #e9eefa;
}

.ntf-29b__row small {
  font-size: 11.5px;
  color: rgba(212,224,246,.5);
}

.ntf-29b__row time {
  flex: none;
  font-size: 10.5px;
  font-variant-numeric: tabular-nums;
  color: rgba(212,224,246,.4);
}

.ntf-29b__row--new {
  background: oklch(0.75 0.13 200 / .07);
  box-shadow: inset 2.5px 0 0 oklch(0.75 0.13 200);
}

.ntf-29b__cap {
  margin-top: 14px;
  font-size: 11.5px;
  line-height: 1.6;
  color: rgba(212,224,246,.45);
  text-align: center;
  text-wrap: pretty;
}

.ntf-29b__cap b {
  color: rgba(233,238,250,.85);
}
```

## JavaScript
```js
/* No JavaScript — the rail is one ::before on the UL (so it never gaps), markers punch out with a panel-colored border, and severity is encoded twice: color for the fast read, shape (dot/ring/square) for color-blind and grayscale contexts. */

/* No JavaScript — each day's h3 is position:sticky;top:0 inside the scrolling panel; when the next day's header arrives at the same top, the browser performs the push-out handoff natively. */
```
