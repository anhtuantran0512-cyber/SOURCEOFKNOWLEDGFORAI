---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/ledger-audit-log/"
title: "Live Activity Feed Timeline — Real-Time Events with :has() Filter"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "A team activity stream that behaves like a product, not a demo: new events arrive on top every few seconds with a height-then-fade entrance that never shoves…"
has_js: "true"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Live Activity Feed Timeline — Real-Time Events with :has() Filter
Source: https://codefronts.com/layouts/css-timelines/ledger-audit-log/

A team activity stream that behaves like a product, not a demo: new events arrive on top every few seconds with a height-then-fade entrance that never shoves the page, a 'Mentions only' toggle filters the feed with :has() and zero listener code, and the stream politely stops growing while your pointer is inside it — the courtesy every real feed (Slack, GitHub, Linear) implements and most tutorials skip.
## HTML
```html
<section class="tls-32" aria-label="Live activity feed timeline demo">
  <div class="tls-32__panel">
    <header class="tls-32__head">
      <p class="tls-32__title"><span class="tls-32__pulse" aria-hidden="true"></span>Team activity</p>
      <div class="tls-32__ctl">
        <span class="tls-32__queued" id="tls-32-queued" aria-live="polite"></span>
        <input class="tls-32__box" type="checkbox" id="tls-32-mentions">
        <label class="tls-32__toggle" for="tls-32-mentions">@ Mentions only</label>
      </div>
    </header>
    <ol class="tls-32__list" id="tls-32-list" role="list">
      <li class="tls-32__row"><div class="tls-32__item" data-kind="mention"><span class="tls-32__av" style="--a:#7c3aed">MK</span><p class="tls-32__txt"><b>Mara</b> mentioned you in <b>#payments</b>: “can @you sanity-check the retry logic?”</p><time class="tls-32__ts" datetime="2026-07-19T09:41">9:41</time></div></li>
      <li class="tls-32__row"><div class="tls-32__item" data-kind="deploy"><span class="tls-32__av" style="--a:#0f766e">CI</span><p class="tls-32__txt"><b>Deploy</b> v2.14.1 reached <b>production</b> — 3 min, all checks green</p><time class="tls-32__ts" datetime="2026-07-19T09:38">9:38</time></div></li>
      <li class="tls-32__row"><div class="tls-32__item" data-kind="comment"><span class="tls-32__av" style="--a:#b45309">DA</span><p class="tls-32__txt"><b>Dev</b> commented on <b>PR #482</b>: “subgrid fixes the alignment, nice”</p><time class="tls-32__ts" datetime="2026-07-19T09:31">9:31</time></div></li>
    </ol>
  </div>
</section>
```
## CSS
```css
.tls-32,
.tls-32 *,
.tls-32 *::before,
.tls-32 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-32 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #4f46e5;
  --tl-line: #27272e;
  --tl-bg: #131318;
  --tl-card: #1b1b22;
  --tl-ink: #e7e7ec;
  --tl-mut: #8e8e9c;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #0d0d11;
  padding: 64px 24px;
  display: grid;
  place-items: center;
}

.tls-32__panel {
  width: min(560px,100%);
  background: var(--tl-bg);
  border: 1px solid var(--tl-line);
  border-radius: 16px;
  overflow: hidden;
}

.tls-32__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 14px 18px;
  border-bottom: 1px solid var(--tl-line);
}

.tls-32__title {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 14px;
  font-weight: 750;
  color: var(--tl-ink);
}

.tls-32__pulse {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #34d399;
  box-shadow: 0 0 8px #34d39988;
}

@media (prefers-reduced-motion: no-preference) {
  .tls-32__pulse {
    animation: tls-32-pulse 1.8s ease-in-out infinite;
  }

  @keyframes tls-32-pulse {
    50% {
      opacity: .35;
    }
  }
}

.tls-32__ctl {
  display: flex;
  align-items: center;
  gap: 10px;
}

.tls-32__queued {
  font-size: 11px;
  font-weight: 700;
  color: #34d399;
}

.tls-32__box {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.tls-32__toggle {
  font-size: 11.5px;
  font-weight: 700;
  color: var(--tl-mut);
  border: 1px solid var(--tl-line);
  border-radius: 999px;
  padding: 5px 12px;
  cursor: pointer;
  user-select: none;
  transition: color .15s,border-color .15s;
}

.tls-32__box:checked + .tls-32__toggle {
  color: #c7c9ff;
  border-color: var(--tl-accent);
  background: rgb(79 70 229 / .15);
}

.tls-32__box:focus-visible + .tls-32__toggle {
  outline: 2px solid var(--tl-accent);
  outline-offset: 2px;
}

.tls-32:has(.tls-32__box:checked) .tls-32__item:not([data-kind="mention"]) {
  display: none;
}

.tls-32__list {
  list-style: none;
  padding: 10px 14px 14px;
  display: flex;
  flex-direction: column;
  max-height: 340px;
  overflow-y: auto;
}

.tls-32__row {
  display: grid;
  grid-template-rows: 1fr;
}

.tls-32__row--new {
  animation: tls-32-in .35s ease both;
}

.tls-32__row--new>.tls-32__item {
  min-height: 0;
  overflow: hidden;
}

@keyframes tls-32-in {
  from {
    grid-template-rows: 0fr;
    opacity: 0;
  }

  to {
    grid-template-rows: 1fr;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tls-32__row--new {
    animation: none;
  }
}

.tls-32__item {
  display: flex;
  align-items: center;
  gap: 12px;
  background: var(--tl-card);
  border: 1px solid var(--tl-line);
  border-radius: 10px;
  padding: 11px 13px;
  margin-top: 8px;
}

.tls-32__item[data-kind="mention"] {
  border-color: rgb(79 70 229 / .5);
}

.tls-32__av {
  flex: none;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 10.5px;
  font-weight: 800;
  color: #fff;
  background: var(--a,#52525b);
}

.tls-32__txt {
  flex: 1;
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--tl-mut);
}

.tls-32__txt b {
  color: var(--tl-ink);
  font-weight: 650;
}

.tls-32__ts {
  flex: none;
  font-size: 10.5px;
  color: #5c5c68;
  font-variant-numeric: tabular-nums;
  align-self: flex-start;
  padding-top: 2px;
}
```

## JavaScript
```js
// JS owns the DATA: it builds and prepends events. CSS owns entrance motion (grid-rows 0fr→1fr) and the mentions filter (:has(:checked) — no filter JS at all).
const list = document.getElementById('tls-32-list');
const queuedChip = document.getElementById('tls-32-queued');
const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;
const MAX_ITEMS = 12;
const pool = [
  { kind: 'deploy',  av: 'CI', c: '#0f766e', txt: '<b>Deploy</b> preview for <b>PR #491</b> is live' },
  { kind: 'comment', av: 'JW', c: '#dc2626', txt: '<b>Jess</b> commented on <b>Roadmap Q4</b>: \u201cself-hosted first?\u201d' },
  { kind: 'mention', av: 'TO', c: '#059669', txt: '<b>Tom</b> mentioned you in <b>#design</b>: \u201c@you the tokens PR is ready\u201d' },
  { kind: 'join',    av: 'AR', c: '#9333ea', txt: '<b>Ana</b> joined the <b>Platform</b> team' },
  { kind: 'deploy',  av: 'CI', c: '#0f766e', txt: '<b>Nightly build</b> passed \u00b7 214 tests, 0 flaky' },
  { kind: 'mention', av: 'MK', c: '#7c3aed', txt: '<b>Mara</b> mentioned you in <b>#payments</b>: \u201cretries look good @you\u201d' },
];
let hovering = false, queue = [], i = 0;

function insert(ev) {
  const t = new Date();
  const hhmm = t.getHours() + ':' + String(t.getMinutes()).padStart(2, '0');
  const li = document.createElement('li');
  li.className = 'tls-32__row' + (REDUCED ? '' : ' tls-32__row--new');
  li.innerHTML = '<div class="tls-32__item" data-kind="' + ev.kind + '">'
    + '<span class="tls-32__av" style="--a:' + ev.c + '">' + ev.av + '</span>'
    + '<p class="tls-32__txt">' + ev.txt + '</p>'
    + '<time class="tls-32__ts" datetime="' + t.toISOString() + '">' + hhmm + '</time></div>';
  list.prepend(li);
  // Trim oldest — only while not hovered, so rows never vanish mid-read.
  while (!hovering && list.children.length > MAX_ITEMS) list.lastElementChild.remove();
}
function tick() {
  const ev = pool[i++ % pool.length];
  if (hovering) { queue.push(ev); queuedChip.textContent = queue.length + ' new'; }
  else insert(ev);
}
list.addEventListener('pointerenter', () => { hovering = true; });
list.addEventListener('pointerleave', () => {
  hovering = false;
  queue.forEach(insert); queue = []; queuedChip.textContent = '';
});
setInterval(tick, 2800); // replace with your WebSocket handler calling insert(event)
```
