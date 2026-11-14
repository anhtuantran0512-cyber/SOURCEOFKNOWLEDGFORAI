---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/notification-preferences-matrix/"
title: "Notification Preferences Matrix"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A notification settings matrix that respects people's attention: event types grouped by category down the side, Email / Push / In-app channels across the…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Notification Preferences Matrix
Source: https://codefronts.com/layouts/css-settings-pages/notification-preferences-matrix/

A notification settings matrix that respects people's attention: event types grouped by category down the side, Email / Push / In-app channels across the top, compact switch cells, column 'select all' toggles with true indeterminate states, locked security alerts that can't be turned off, a pause-all switch that dims the matrix via :has(), quiet hours, and a digest-frequency segmented control.
## HTML
```html
<section class="csp-12">
  <div class="csp-12__wrap">
    <header class="csp-12__head">
      <div><h1>Notifications</h1><p>Choose what you hear about, and where.</p></div>
      <label class="csp-12__pause"><input type="checkbox" id="csp12-pause" class="csp-12__sw" role="switch"> Pause all</label>
    </header>
    <p class="csp-12__banner">Notifications are paused. You'll still receive security alerts.</p>

    <div class="csp-12__card csp-12__matrix">
      <table class="csp-12__table" data-table>
        <thead><tr>
          <th scope="col" class="csp-12__ev">Activity</th>
          <th scope="col"><label><span>Email</span><input type="checkbox" class="csp-12__all" aria-label="All email notifications"></label></th>
          <th scope="col"><label><span>Push</span><input type="checkbox" class="csp-12__all" aria-label="All push notifications"></label></th>
          <th scope="col"><label><span>In-app</span><input type="checkbox" class="csp-12__all" aria-label="All in-app notifications"></label></th>
        </tr></thead>
        <tbody>
          <tr class="csp-12__grp"><th colspan="4">Collaboration</th></tr>
          <tr><th scope="row" class="csp-12__ev"><b>Mentions &amp; replies</b><small>Someone @mentions you or replies to your comment</small></th><td><input type="checkbox" class="csp-12__sw" checked aria-label="Email: Mentions and replies"></td><td><input type="checkbox" class="csp-12__sw" checked aria-label="Push: Mentions and replies"></td><td><input type="checkbox" class="csp-12__sw" checked aria-label="In-app: Mentions and replies"></td></tr>
          <tr><th scope="row" class="csp-12__ev"><b>Comments on your files</b><small>New comments on documents you own</small></th><td><input type="checkbox" class="csp-12__sw" aria-label="Email: Comments on your files"></td><td><input type="checkbox" class="csp-12__sw" checked aria-label="Push: Comments on your files"></td><td><input type="checkbox" class="csp-12__sw" checked aria-label="In-app: Comments on your files"></td></tr>
          <tr><th scope="row" class="csp-12__ev"><b>Task assigned to you</b><small>You're added as an assignee</small></th><td><input type="checkbox" class="csp-12__sw" checked aria-label="Email: Task assigned"></td><td><input type="checkbox" class="csp-12__sw" checked aria-label="Push: Task assigned"></td><td><input type="checkbox" class="csp-12__sw" checked aria-label="In-app: Task assigned"></td></tr>
          <tr class="csp-12__grp"><th colspan="4">Updates</th></tr>
          <tr><th scope="row" class="csp-12__ev"><b>Weekly summary</b><small>A Monday recap of your workspace</small></th><td><input type="checkbox" class="csp-12__sw" checked aria-label="Email: Weekly summary"></td><td><input type="checkbox" class="csp-12__sw" aria-label="Push: Weekly summary"></td><td><input type="checkbox" class="csp-12__sw" aria-label="In-app: Weekly summary"></td></tr>
          <tr><th scope="row" class="csp-12__ev"><b>Product announcements</b><small>New features and improvements</small></th><td><input type="checkbox" class="csp-12__sw" aria-label="Email: Product announcements"></td><td><input type="checkbox" class="csp-12__sw" aria-label="Push: Product announcements"></td><td><input type="checkbox" class="csp-12__sw" checked aria-label="In-app: Product announcements"></td></tr>
          <tr class="csp-12__grp"><th colspan="4">Account</th></tr>
          <tr class="csp-12__locked"><th scope="row" class="csp-12__ev"><b>Security alerts</b><small>New sign-ins, password and 2FA changes — always on</small></th><td><input type="checkbox" class="csp-12__sw" checked disabled aria-label="Email: Security alerts, required"></td><td><input type="checkbox" class="csp-12__sw" checked aria-label="Push: Security alerts"></td><td><input type="checkbox" class="csp-12__sw" checked disabled aria-label="In-app: Security alerts, required"></td></tr>
        </tbody>
      </table>
    </div>

    <div class="csp-12__card csp-12__extra">
      <div class="csp-12__line">
        <div><b>Email digest</b><small>Bundle non-urgent emails instead of sending them one by one.</small></div>
        <fieldset class="csp-12__seg"><legend class="csp-12__sr">Digest frequency</legend>
          <input type="radio" name="csp12-d" id="csp12-d1"><label for="csp12-d1">Off</label>
          <input type="radio" name="csp12-d" id="csp12-d2" checked><label for="csp12-d2">Daily</label>
          <input type="radio" name="csp12-d" id="csp12-d3"><label for="csp12-d3">Weekly</label>
        </fieldset>
      </div>
      <div class="csp-12__line">
        <div><b>Quiet hours</b><small>Mute push notifications overnight.</small></div>
        <input type="checkbox" id="csp12-quiet" class="csp-12__sw" role="switch" checked aria-label="Quiet hours">
      </div>
      <div class="csp-12__times"><label>From <input type="time" value="22:00"></label><label>To <input type="time" value="07:30"></label><span>Pacific Time</span></div>
    </div>
    <p class="csp-12__saved" data-saved aria-live="polite"></p>
  </div>
</section>
```
## CSS
```css
.csp-12,
.csp-12 *,
.csp-12 *::before,
.csp-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-12 {
  --bg: oklch(0.98 0.005 150);
  --surface: #fff;
  --ink: oklch(0.22 0.02 160);
  --muted: oklch(0.5 0.02 160);
  --line: oklch(0.92 0.008 160);
  --accent: oklch(0.55 0.14 160);
  color-scheme: light;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 20px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--ink);
  width: 100%;
}

.csp-12__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.csp-12__wrap {
  max-width: 820px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.csp-12__head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}

.csp-12__head h1 {
  font: 700 30px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-12__head p {
  font: 400 14.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
}

.csp-12__pause {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 44px;
  padding: 0 14px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--surface);
  font: 600 13.5px/1 system-ui,sans-serif;
  cursor: pointer;
}

.csp-12__banner {
  display: none;
  padding: 12px 16px;
  border-radius: 12px;
  font: 500 13.5px/1.4 system-ui,sans-serif;
  color: oklch(0.42 0.1 65);
  background: oklch(0.96 0.05 85);
}

.csp-12:has(#csp12-pause:checked) .csp-12__banner {
  display: block;
}

.csp-12__card {
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--surface);
  box-shadow: 0 1px 2px oklch(0 0 0/.03);
}

.csp-12__matrix {
  overflow-x: auto;
  transition: opacity .25s,filter .25s;
}

.csp-12:has(#csp12-pause:checked) .csp-12__matrix {
  opacity: .45;
  filter: grayscale(1);
  pointer-events: none;
}

.csp-12__table {
  width: 100%;
  min-width: 540px;
  border-collapse: collapse;
}

.csp-12__table thead th {
  padding: 14px 10px;
  border-bottom: 1px solid var(--line);
  text-align: center;
  vertical-align: bottom;
}

.csp-12__table thead label {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  font: 650 13px/1 system-ui,sans-serif;
  cursor: pointer;
}

.csp-12__table thead th.csp-12__ev {
  text-align: left;
  padding-left: 20px;
  font: 600 12px/1 system-ui,sans-serif;
  letter-spacing: .04em;
  text-transform: uppercase;
  color: var(--muted);
}

.csp-12__ev {
  width: 52%;
  padding: 13px 20px;
  text-align: left;
}

.csp-12__ev b {
  display: block;
  font: 600 14px/1.3 system-ui,sans-serif;
}

.csp-12__ev small {
  display: block;
  margin-top: 2px;
  font: 400 12.5px/1.35 system-ui,sans-serif;
  color: var(--muted);
}

.csp-12__table td {
  text-align: center;
  padding: 10px;
}

.csp-12__table tbody tr:not(.csp-12__grp) {
  border-top: 1px solid var(--line);
  transition: background .12s;
}

.csp-12__table tbody tr:not(.csp-12__grp):hover {
  background: oklch(0.985 0.006 160);
}

.csp-12__grp th {
  padding: 18px 20px 8px;
  text-align: left;
  font: 650 11.5px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--accent);
}

.csp-12__grp+tr {
  border-top: 0!important;
}

.csp-12__all {
  appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 6px;
  border: 1.5px solid oklch(0.82 0.01 160);
  display: grid;
  place-items: center;
  cursor: pointer;
  transition: all .15s;
}

.csp-12__all:checked,
.csp-12__all:indeterminate {
  background: var(--accent);
  border-color: var(--accent);
}

.csp-12__all:checked::after {
  content: "";
  width: 10px;
  height: 6px;
  border: solid #fff;
  border-width: 0 0 2px 2px;
  rotate: -45deg;
  translate: 0 -1px;
}

.csp-12__all:indeterminate::after {
  content: "";
  width: 10px;
  height: 2px;
  border-radius: 2px;
  background: #fff;
}

.csp-12__sw {
  appearance: none;
  position: relative;
  flex: none;
  width: 38px;
  height: 22px;
  border-radius: 999px;
  background: oklch(0.89 0.008 160);
  cursor: pointer;
  vertical-align: middle;
  transition: background .2s;
}

.csp-12__sw::before {
  content: "";
  position: absolute;
  top: 2px;
  left: 2px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 3px oklch(0 0 0/.25);
  transition: translate .2s cubic-bezier(.3,.7,.4,1.3);
}

.csp-12__sw:checked {
  background: var(--accent);
}

.csp-12__sw:checked::before {
  translate: 16px 0;
}

.csp-12__sw:disabled {
  cursor: not-allowed;
  background: oklch(0.8 0.04 160);
}

.csp-12__sw:disabled::before {
  background: #fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 18 18'%3E%3Crect x='5.5' y='8.2' width='7' height='5' rx='1.2' fill='%23889990'/%3E%3Cpath d='M7 8.2V7a2 2 0 0 1 4 0v1.2' fill='none' stroke='%23889990' stroke-width='1.3'/%3E%3C/svg%3E") center/18px;
}

.csp-12__sw:focus-visible,
.csp-12__all:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.csp-12__extra {
  display: flex;
  flex-direction: column;
}

.csp-12__line {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
  padding: 16px 20px;
}

.csp-12__line+.csp-12__line {
  border-top: 1px solid var(--line);
}

.csp-12__line b {
  display: block;
  font: 600 14px/1.3 system-ui,sans-serif;
}

.csp-12__line small {
  display: block;
  margin-top: 2px;
  font: 400 12.5px/1.4 system-ui,sans-serif;
  color: var(--muted);
}

.csp-12__seg {
  border: 0;
  display: flex;
  padding: 3px;
  border-radius: 11px;
  background: oklch(0.95 0.006 160);
}

.csp-12__seg input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.csp-12__seg label {
  min-height: 36px;
  display: grid;
  place-items: center;
  padding: 0 14px;
  border-radius: 8px;
  font: 600 13px/1 system-ui,sans-serif;
  color: var(--muted);
  cursor: pointer;
  transition: all .15s;
}

.csp-12__seg input:checked+label {
  color: var(--ink);
  background: var(--surface);
  box-shadow: 0 1px 3px oklch(0 0 0/.1);
}

.csp-12__seg input:focus-visible+label {
  outline: 2px solid var(--accent);
}

.csp-12__times {
  display: none;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  padding: 0 20px 18px;
  font: 500 13px/1 system-ui,sans-serif;
  color: var(--muted);
}

.csp-12:has(#csp12-quiet:checked) .csp-12__times {
  display: flex;
}

.csp-12__times label {
  display: flex;
  align-items: center;
  gap: 8px;
}

.csp-12__times input {
  min-height: 40px;
  padding: 0 10px;
  border: 1px solid var(--line);
  border-radius: 9px;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--ink);
  background: var(--surface);
}

.csp-12__saved {
  min-height: 16px;
  font: 500 12.5px/1 system-ui,sans-serif;
  color: var(--accent);
  text-align: right;
}

@media (prefers-reduced-motion: reduce) {
  .csp-12 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-12');
  var table = root.querySelector('[data-table]');
  var masters = table.querySelectorAll('.csp-12__all');
  var saved = root.querySelector('[data-saved]'), t = 0;
  var cells = function (i) { return Array.prototype.slice.call(table.querySelectorAll('tbody tr td:nth-child(' + (i + 2) + ') input')); };

  function sync(i) {
    var boxes = cells(i).filter(function (b) { return !b.disabled; });
    var on = boxes.filter(function (b) { return b.checked; }).length;
    masters[i].checked = on === boxes.length;
    masters[i].indeterminate = on > 0 && on < boxes.length;
  }
  masters.forEach(function (m, i) {
    m.addEventListener('change', function () { cells(i).forEach(function (b) { if (!b.disabled) b.checked = m.checked; }); sync(i); });
    sync(i);
  });
  root.addEventListener('change', function (e) {
    var td = e.target.closest('td');
    if (td) sync(td.cellIndex - 1);
    clearTimeout(t); saved.textContent = 'Saving…';
    t = setTimeout(function () { saved.textContent = 'Preferences saved ✓'; }, 600);
  });
})();
```
