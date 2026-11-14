---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/data-export-request/"
title: "Data Export Request Page"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A transparent, GDPR- and CCPA-friendly data export page: choose exactly which data to include from checkbox cards with size estimates, pick JSON or CSV and a…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Data Export Request Page
Source: https://codefronts.com/layouts/css-settings-pages/data-export-request/

A transparent, GDPR- and CCPA-friendly data export page: choose exactly which data to include from checkbox cards with size estimates, pick JSON or CSV and a date range, see a live summary of the estimated archive size, then request the export and watch a job card progress from Queued to Preparing to Ready with a download link and expiry. Previous exports are listed with their status.
## HTML
```html
<section class="csp-15">
  <div class="csp-15__wrap">
    <header class="csp-15__head"><h1>Export your data</h1><p>Download a copy of your workspace data at any time. We'll prepare an archive and keep it available for 7 days.</p></header>
    <div class="csp-15__grid">
      <form class="csp-15__form" data-form>
        <fieldset class="csp-15__sets">
          <legend>What to include</legend>
          <label class="csp-15__set"><input type="checkbox" data-mb="1240" checked><span><b>Projects &amp; documents</b><small>All pages, files and attachments</small></span><em>1.2 GB</em></label>
          <label class="csp-15__set"><input type="checkbox" data-mb="86" checked><span><b>Comments &amp; tasks</b><small>Threads, mentions and task history</small></span><em>86 MB</em></label>
          <label class="csp-15__set"><input type="checkbox" data-mb="2"><span><b>Members &amp; roles</b><small>Names, emails, roles and groups</small></span><em>2 MB</em></label>
          <label class="csp-15__set"><input type="checkbox" data-mb="34"><span><b>Audit log</b><small>Security and admin events</small></span><em>34 MB</em></label>
          <label class="csp-15__set"><input type="checkbox" data-mb="1"><span><b>Billing history</b><small>Invoices and payment records</small></span><em>1 MB</em></label>
        </fieldset>
        <div class="csp-15__opts">
          <fieldset class="csp-15__seg"><legend>Format</legend><div>
            <input type="radio" name="csp15-f" id="csp15-json" value="JSON" checked><label for="csp15-json">JSON</label>
            <input type="radio" name="csp15-f" id="csp15-csv" value="CSV"><label for="csp15-csv">CSV</label>
          </div></fieldset>
          <label class="csp-15__range"><span>Date range</span><select data-range><option>All time</option><option>Last 12 months</option><option>Last 30 days</option></select></label>
        </div>
      </form>

      <aside class="csp-15__summary">
        <h2>Summary</h2>
        <dl>
          <div><dt>Datasets</dt><dd data-sets>2</dd></div>
          <div><dt>Format</dt><dd data-fmt>JSON (.zip)</dd></div>
          <div><dt>Estimated size</dt><dd data-size>≈ 1.3 GB</dd></div>
        </dl>
        <button type="button" class="csp-15__btn" data-req>Request export</button>
        <p class="csp-15__fine">We'll email <b>[email protected]</b> when it's ready. Typical exports take 2–10 minutes.</p>
      </aside>
    </div>

    <div class="csp-15__jobs">
      <h2>Recent exports</h2>
      <ul data-jobs>
        <li class="csp-15__job" data-state="ready"><div class="csp-15__jtop"><b>Full workspace · JSON</b><span class="csp-15__jstate">Ready</span></div><small>Requested Oct 2, 2026 · 1.1 GB · expires Oct 9</small><div class="csp-15__jact"><a href="#" class="csp-15__dl">Download</a></div></li>
        <li class="csp-15__job" data-state="expired"><div class="csp-15__jtop"><b>Members &amp; roles · CSV</b><span class="csp-15__jstate">Expired</span></div><small>Requested Aug 11, 2026 · 2 MB</small></li>
      </ul>
    </div>
  </div>
  <p class="csp-15__sr" aria-live="polite" data-live></p>
</section>
```
## CSS
```css
.csp-15,
.csp-15 *,
.csp-15 *::before,
.csp-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-15 {
  --bg: oklch(0.975 0.006 230);
  --surface: #fff;
  --ink: oklch(0.22 0.02 240);
  --muted: oklch(0.5 0.02 240);
  --line: oklch(0.91 0.008 240);
  --accent: oklch(0.55 0.16 235);
  --track: oklch(0.93 0.01 240);
  --ok: oklch(0.55 0.14 155);
  color-scheme: light;
  container-type: inline-size;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 22px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--ink);
  accent-color: var(--accent);
  width: 100%;
}

.csp-15__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.csp-15__wrap {
  max-width: 960px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.csp-15__head h1 {
  font: 700 30px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-15__head p {
  max-width: 600px;
  font: 400 14.5px/1.55 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
  text-wrap: pretty;
}

.csp-15__grid {
  display: grid;
  grid-template-columns: minmax(0,1fr) 300px;
  gap: 20px;
  align-items: start;
}

.csp-15__form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.csp-15__sets {
  border: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.csp-15 legend {
  font: 600 13.5px/1 system-ui,sans-serif;
  margin-bottom: 10px;
}

.csp-15__set {
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 64px;
  padding: 12px 16px;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  cursor: pointer;
  transition: border-color .15s,background .15s,box-shadow .15s;
}

.csp-15__set:hover {
  border-color: oklch(0.84 0.02 240);
}

.csp-15__set:has(input:checked) {
  border-color: var(--accent);
  background: oklch(0.98 0.012 235);
  box-shadow: 0 0 0 1px var(--accent);
}

.csp-15__set:has(input:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-15__set input {
  width: 18px;
  height: 18px;
  flex: none;
}

.csp-15__set span {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.csp-15__set b {
  font: 600 14px/1.2 system-ui,sans-serif;
}

.csp-15__set small {
  font: 400 12.5px/1.3 system-ui,sans-serif;
  color: var(--muted);
}

.csp-15__set em {
  font: 600 12.5px/1 ui-monospace,Menlo,monospace;
  font-style: normal;
  color: var(--muted);
}

.csp-15__opts {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  align-items: flex-end;
}

.csp-15__seg {
  border: 0;
}

.csp-15__seg>div {
  display: flex;
  padding: 3px;
  border-radius: 11px;
  background: oklch(0.94 0.008 240);
}

.csp-15__seg input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.csp-15__seg label {
  min-height: 38px;
  display: grid;
  place-items: center;
  padding: 0 18px;
  border-radius: 8px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: var(--muted);
  cursor: pointer;
  transition: all .15s;
}

.csp-15__seg input:checked+label {
  color: var(--ink);
  background: var(--surface);
  box-shadow: 0 1px 3px oklch(0 0 0/.1);
}

.csp-15__seg input:focus-visible+label {
  outline: 2px solid var(--accent);
}

.csp-15__range {
  display: flex;
  flex-direction: column;
  gap: 10px;
  font: 600 13.5px/1 system-ui,sans-serif;
}

.csp-15__range select {
  min-height: 44px;
  padding: 0 12px;
  border: 1px solid var(--line);
  border-radius: 11px;
  background: var(--surface);
  font: 400 14px/1 system-ui,sans-serif;
  color: var(--ink);
}

.csp-15__summary {
  position: sticky;
  top: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: 20px;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--surface);
  box-shadow: 0 18px 40px -30px oklch(0.3 0.06 240/.4);
}

.csp-15__summary h2 {
  font: 650 15px/1 system-ui,sans-serif;
}

.csp-15__summary dl {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.csp-15__summary dl div {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  font: 400 13.5px/1.3 system-ui,sans-serif;
}

.csp-15__summary dt {
  color: var(--muted);
}

.csp-15__summary dd {
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.csp-15__summary dl div:last-child {
  padding-top: 10px;
  border-top: 1px solid var(--line);
}

.csp-15__summary dl div:last-child dd {
  font-size: 17px;
}

.csp-15__btn {
  min-height: 48px;
  border: 0;
  border-radius: 12px;
  font: 650 14.5px/1 system-ui,sans-serif;
  color: #fff;
  background: var(--accent);
  cursor: pointer;
  transition: background .15s,opacity .15s;
}

.csp-15__btn:hover:not(:disabled) {
  background: oklch(0.5 0.16 235);
}

.csp-15__btn:disabled {
  opacity: .4;
  cursor: not-allowed;
}

.csp-15__btn:focus-visible,
.csp-15__dl:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.csp-15__fine {
  font: 400 12.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
}

.csp-15__fine b {
  color: var(--ink);
  font-weight: 600;
}

.csp-15__jobs {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.csp-15__jobs h2 {
  font: 650 15px/1 system-ui,sans-serif;
}

.csp-15__jobs ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.csp-15__job {
  --tone: var(--muted);
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 16px 18px;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  animation: csp15-in .35s ease;
}

.csp-15__job[data-state="queued"] {
  --tone: oklch(0.6 0.12 70);
}

.csp-15__job[data-state="running"] {
  --tone: var(--accent);
  border-color: oklch(0.85 0.06 235);
}

.csp-15__job[data-state="ready"] {
  --tone: var(--ok);
}

.csp-15__job[data-state="expired"] {
  opacity: .65;
}

.csp-15__jtop {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}

.csp-15__jtop b {
  font: 600 14px/1.2 system-ui,sans-serif;
}

.csp-15__jstate {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border-radius: 999px;
  font: 600 12px/1 system-ui,sans-serif;
  color: var(--tone);
  background: color-mix(in oklab,var(--tone) 12%,transparent);
}

.csp-15__jstate::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
}

.csp-15__job[data-state="running"] .csp-15__jstate::before {
  animation: csp15-blink 1s infinite;
}

.csp-15__job small {
  font: 400 12.5px/1.4 system-ui,sans-serif;
  color: var(--muted);
}

.csp-15__job progress {
  appearance: none;
  -webkit-appearance: none;
  width: 100%;
  height: 8px;
  border: 0;
  border-radius: 99px;
  background: var(--track);
  overflow: hidden;
}

.csp-15__job progress::-webkit-progress-bar {
  background: transparent;
}

.csp-15__job progress::-webkit-progress-value {
  background: linear-gradient(90deg,oklch(0.7 0.12 210),var(--accent));
  border-radius: 99px;
  transition: width .3s;
}

.csp-15__job progress::-moz-progress-bar {
  background: var(--accent);
  border-radius: 99px;
}

.csp-15__jact {
  display: flex;
}

.csp-15__dl {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 38px;
  padding: 0 14px;
  border-radius: 10px;
  font: 600 13px/1 system-ui,sans-serif;
  text-decoration: none;
  color: #fff;
  background: var(--ok);
}

.csp-15__dl::before {
  content: "↓";
  font-weight: 700;
}

@keyframes csp15-in {
  from {
    opacity: 0;
    translate: 0 -6px;
  }
}

@keyframes csp15-blink {
  50% {
    opacity: .3;
  }
}

@container (max-width: 720px) {
  .csp-15__grid {
    grid-template-columns: minmax(0,1fr);
  }

  .csp-15__summary {
    position: static;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-15 * {
    transition: none!important;
    animation: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-15');
  var form = root.querySelector('[data-form]'), req = root.querySelector('[data-req]');
  var jobs = root.querySelector('[data-jobs]'), live = root.querySelector('[data-live]');
  var fmtSize = function (mb) { return mb >= 1000 ? '≈ ' + (mb / 1000).toFixed(1) + ' GB' : '≈ ' + mb + ' MB'; };

  function summary() {
    var sel = form.querySelectorAll('.csp-15__sets input:checked'), mb = 0;
    sel.forEach(function (c) { mb += +c.dataset.mb; });
    root.querySelector('[data-sets]').textContent = sel.length;
    root.querySelector('[data-fmt]').textContent = form.querySelector('[name=csp15-f]:checked').value + ' (.zip)';
    root.querySelector('[data-size]').textContent = sel.length ? fmtSize(mb) : '—';
    req.disabled = sel.length === 0;
    return { n: sel.length, mb: mb };
  }
  form.addEventListener('change', summary);

  req.addEventListener('click', function () {
    var s = summary(), fmt = form.querySelector('[name=csp15-f]:checked').value;
    var li = document.createElement('li');
    li.className = 'csp-15__job'; li.dataset.state = 'queued';
    li.innerHTML = '<div class="csp-15__jtop"><b></b><span class="csp-15__jstate">Queued</span></div><small>Requested just now · ' + fmtSize(s.mb) + '</small><progress max="100" value="0" aria-label="Export progress"></progress>';
    li.querySelector('b').textContent = s.n + ' dataset' + (s.n > 1 ? 's' : '') + ' · ' + fmt;
    jobs.prepend(li);
    req.disabled = true; req.textContent = 'Export in progress…';
    live.textContent = 'Export queued';
    var bar = li.querySelector('progress'), state = li.querySelector('.csp-15__jstate');
    setTimeout(function () {
      li.dataset.state = 'running'; state.textContent = 'Preparing'; live.textContent = 'Preparing export';
      var v = 0, iv = setInterval(function () {
        v = Math.min(100, v + 4 + Math.random() * 9); bar.value = v;
        if (v >= 100) {
          clearInterval(iv);
          li.dataset.state = 'ready'; state.textContent = 'Ready';
          bar.remove();
          li.querySelector('small').textContent = 'Requested just now · ' + fmtSize(s.mb) + ' · expires in 7 days';
          var act = document.createElement('div'); act.className = 'csp-15__jact';
          act.innerHTML = '<a href="#" class="csp-15__dl">Download</a>'; li.appendChild(act);
          req.textContent = 'Request export'; summary();
          live.textContent = 'Your export is ready to download';
        }
      }, 180);
    }, 900);
  });
  summary();
})();
```
