---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/roles-permissions-matrix/"
title: "Roles and Permissions Matrix"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A clear RBAC permissions matrix: permissions grouped by area down the side, roles across the top, custom checkbox cells, a locked Owner column, crosshair row…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Roles and Permissions Matrix
Source: https://codefronts.com/layouts/css-settings-pages/roles-permissions-matrix/

A clear RBAC permissions matrix: permissions grouped by area down the side, roles across the top, custom checkbox cells, a locked Owner column, crosshair row + column highlighting on hover powered entirely by :has(), per-role 'x of y' counters, a sticky first column for horizontal scrolling on small screens, and an unsaved-changes footer that tracks exactly how many permissions you've changed.
## HTML
```html
<section class="csp-08">
  <div class="csp-08__wrap">
    <header class="csp-08__head">
      <div><h1>Roles &amp; permissions</h1><p>Control what each role can do across the workspace.</p></div>
    </header>
    <div class="csp-08__card">
      <div class="csp-08__scroll">
        <table class="csp-08__table" data-table>
          <thead>
            <tr>
              <th scope="col" class="csp-08__perm">Permission</th>
              <th scope="col"><span>Owner</span><small data-c></small></th>
              <th scope="col"><span>Admin</span><small data-c></small></th>
              <th scope="col"><span>Editor</span><small data-c></small></th>
              <th scope="col"><span>Viewer</span><small data-c></small></th>
            </tr>
          </thead>
          <tbody>
            <tr class="csp-08__group"><th colspan="5" scope="colgroup">Projects</th></tr>
            <tr><th scope="row" class="csp-08__perm"><b>View projects</b><small>See all projects and their content</small></th><td><input type="checkbox" checked disabled aria-label="Owner: View projects"></td><td><input type="checkbox" checked aria-label="Admin: View projects"></td><td><input type="checkbox" checked aria-label="Editor: View projects"></td><td><input type="checkbox" checked aria-label="Viewer: View projects"></td></tr>
            <tr><th scope="row" class="csp-08__perm"><b>Create &amp; edit</b><small>Create projects and edit content</small></th><td><input type="checkbox" checked disabled aria-label="Owner: Create and edit"></td><td><input type="checkbox" checked aria-label="Admin: Create and edit"></td><td><input type="checkbox" checked aria-label="Editor: Create and edit"></td><td><input type="checkbox" aria-label="Viewer: Create and edit"></td></tr>
            <tr><th scope="row" class="csp-08__perm"><b>Delete projects</b><small>Permanently remove projects</small></th><td><input type="checkbox" checked disabled aria-label="Owner: Delete projects"></td><td><input type="checkbox" checked aria-label="Admin: Delete projects"></td><td><input type="checkbox" aria-label="Editor: Delete projects"></td><td><input type="checkbox" aria-label="Viewer: Delete projects"></td></tr>
            <tr class="csp-08__group"><th colspan="5" scope="colgroup">Members</th></tr>
            <tr><th scope="row" class="csp-08__perm"><b>Invite members</b><small>Send invitations to new people</small></th><td><input type="checkbox" checked disabled aria-label="Owner: Invite members"></td><td><input type="checkbox" checked aria-label="Admin: Invite members"></td><td><input type="checkbox" checked aria-label="Editor: Invite members"></td><td><input type="checkbox" aria-label="Viewer: Invite members"></td></tr>
            <tr><th scope="row" class="csp-08__perm"><b>Manage roles</b><small>Change roles and remove members</small></th><td><input type="checkbox" checked disabled aria-label="Owner: Manage roles"></td><td><input type="checkbox" checked aria-label="Admin: Manage roles"></td><td><input type="checkbox" aria-label="Editor: Manage roles"></td><td><input type="checkbox" aria-label="Viewer: Manage roles"></td></tr>
            <tr class="csp-08__group"><th colspan="5" scope="colgroup">Billing</th></tr>
            <tr><th scope="row" class="csp-08__perm"><b>View invoices</b><small>Download receipts and invoices</small></th><td><input type="checkbox" checked disabled aria-label="Owner: View invoices"></td><td><input type="checkbox" checked aria-label="Admin: View invoices"></td><td><input type="checkbox" aria-label="Editor: View invoices"></td><td><input type="checkbox" aria-label="Viewer: View invoices"></td></tr>
            <tr><th scope="row" class="csp-08__perm"><b>Manage subscription</b><small>Change plan, seats and payment</small></th><td><input type="checkbox" checked disabled aria-label="Owner: Manage subscription"></td><td><input type="checkbox" aria-label="Admin: Manage subscription"></td><td><input type="checkbox" aria-label="Editor: Manage subscription"></td><td><input type="checkbox" aria-label="Viewer: Manage subscription"></td></tr>
            <tr class="csp-08__group"><th colspan="5" scope="colgroup">Developer</th></tr>
            <tr><th scope="row" class="csp-08__perm"><b>API keys</b><small>Create and revoke API keys</small></th><td><input type="checkbox" checked disabled aria-label="Owner: API keys"></td><td><input type="checkbox" checked aria-label="Admin: API keys"></td><td><input type="checkbox" aria-label="Editor: API keys"></td><td><input type="checkbox" aria-label="Viewer: API keys"></td></tr>
            <tr><th scope="row" class="csp-08__perm"><b>Webhooks</b><small>Configure webhook endpoints</small></th><td><input type="checkbox" checked disabled aria-label="Owner: Webhooks"></td><td><input type="checkbox" checked aria-label="Admin: Webhooks"></td><td><input type="checkbox" aria-label="Editor: Webhooks"></td><td><input type="checkbox" aria-label="Viewer: Webhooks"></td></tr>
          </tbody>
        </table>
      </div>
      <footer class="csp-08__foot" data-foot>
        <span data-diff aria-live="polite">No unsaved changes</span>
        <div><button type="button" class="csp-08__btn" data-reset>Reset</button><button type="button" class="csp-08__btn csp-08__btn--primary" data-save>Save changes</button></div>
      </footer>
    </div>
  </div>
</section>
```
## CSS
```css
.csp-08,
.csp-08 *,
.csp-08 *::before,
.csp-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-08 {
  --bg: oklch(0.98 0.004 250);
  --surface: #fff;
  --ink: oklch(0.22 0.02 255);
  --muted: oklch(0.5 0.02 255);
  --line: oklch(0.92 0.007 255);
  --accent: oklch(0.55 0.19 255);
  --col: oklch(0.97 0.015 255);
  color-scheme: light;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 20px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--ink);
  width: 100%;
}

.csp-08__wrap {
  max-width: 900px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.csp-08__head h1 {
  font: 700 30px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-08__head p {
  font: 400 14.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
}

.csp-08__card {
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--surface);
  overflow: hidden;
  box-shadow: 0 1px 2px oklch(0 0 0/.03),0 14px 36px -26px oklch(0.3 0.06 255/.35);
}

.csp-08__scroll {
  overflow-x: auto;
}

.csp-08__table {
  width: 100%;
  min-width: 620px;
  border-collapse: separate;
  border-spacing: 0;
  font: 400 14px/1.3 system-ui,sans-serif;
}

.csp-08__table thead th {
  position: sticky;
  top: 0;
  padding: 16px 10px;
  background: var(--surface);
  border-bottom: 1px solid var(--line);
  text-align: center;
  vertical-align: bottom;
}

.csp-08__table thead th span {
  display: block;
  font: 650 13.5px/1.2 system-ui,sans-serif;
}

.csp-08__table thead th small {
  display: block;
  margin-top: 4px;
  font: 500 11.5px/1 system-ui,sans-serif;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.csp-08__table thead th.csp-08__perm {
  text-align: left;
  font: 600 12px/1 system-ui,sans-serif;
  letter-spacing: .04em;
  text-transform: uppercase;
  color: var(--muted);
}

.csp-08__perm {
  position: sticky;
  left: 0;
  z-index: 1;
  width: 42%;
  padding: 12px 18px;
  text-align: left;
  background: var(--surface);
}

.csp-08__perm b {
  display: block;
  font: 600 14px/1.3 system-ui,sans-serif;
}

.csp-08__perm small {
  display: block;
  font: 400 12.5px/1.35 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 2px;
}

.csp-08__table td {
  text-align: center;
  padding: 10px;
  border-bottom: 1px solid var(--line);
  transition: background .12s;
}

.csp-08__table tbody tr:not(.csp-08__group) th {
  border-bottom: 1px solid var(--line);
}

.csp-08__group th {
  padding: 18px 18px 8px;
  text-align: left;
  font: 650 11.5px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--accent);
  background: var(--surface);
  border-bottom: 1px solid var(--line);
}

.csp-08__table tbody tr:not(.csp-08__group):hover>* {
  background: var(--col);
}

.csp-08__table:has(td:nth-child(2):hover) :is(td,th):nth-child(2),
.csp-08__table:has(td:nth-child(3):hover) :is(td,th):nth-child(3),
.csp-08__table:has(td:nth-child(4):hover) :is(td,th):nth-child(4),
.csp-08__table:has(td:nth-child(5):hover) :is(td,th):nth-child(5) {
  background: var(--col);
}

.csp-08__table:has(td:nth-child(2):hover) .csp-08__group th,
.csp-08__table:has(td:nth-child(3):hover) .csp-08__group th,
.csp-08__table:has(td:nth-child(4):hover) .csp-08__group th,
.csp-08__table:has(td:nth-child(5):hover) .csp-08__group th {
  background: var(--surface);
}

.csp-08__table tr:hover td:hover {
  background: oklch(0.94 0.03 255);
}

.csp-08__table input {
  appearance: none;
  display: inline-grid;
  place-items: center;
  width: 24px;
  height: 24px;
  border-radius: 7px;
  border: 1.5px solid oklch(0.84 0.01 255);
  background: var(--surface);
  cursor: pointer;
  vertical-align: middle;
  transition: background .15s,border-color .15s,scale .15s;
}

.csp-08__table input::after {
  content: "";
  width: 14px;
  height: 14px;
  background: #fff;
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 14 14'%3E%3Cpath d='m3 7.3 2.6 2.6L11 4.4' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat;
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 14 14'%3E%3Cpath d='m3 7.3 2.6 2.6L11 4.4' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat;
  scale: 0;
  transition: scale .18s cubic-bezier(.3,.7,.3,1.5);
}

.csp-08__table input:checked {
  background: var(--accent);
  border-color: var(--accent);
}

.csp-08__table input:checked::after {
  scale: 1;
}

.csp-08__table input:hover:not(:disabled) {
  border-color: var(--accent);
}

.csp-08__table input:active:not(:disabled) {
  scale: .9;
}

.csp-08__table input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-08__table input:disabled {
  cursor: not-allowed;
  background: oklch(0.95 0.005 255);
  border-color: transparent;
}

.csp-08__table input:disabled::after {
  scale: 1;
  background: var(--muted);
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 14 14'%3E%3Crect x='3' y='6.3' width='8' height='5.7' rx='1.3' fill='black'/%3E%3Cpath d='M4.8 6.3V5a2.2 2.2 0 0 1 4.4 0v1.3' fill='none' stroke='black' stroke-width='1.4'/%3E%3C/svg%3E");
  mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 14 14'%3E%3Crect x='3' y='6.3' width='8' height='5.7' rx='1.3' fill='black'/%3E%3Cpath d='M4.8 6.3V5a2.2 2.2 0 0 1 4.4 0v1.3' fill='none' stroke='black' stroke-width='1.4'/%3E%3C/svg%3E");
}

.csp-08__table input.is-changed {
  box-shadow: 0 0 0 3px oklch(0.8 0.15 80/.6);
}

.csp-08__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
  padding: 14px 18px;
  border-top: 1px solid var(--line);
  background: oklch(0.985 0.004 250);
  font: 500 13.5px/1.3 system-ui,sans-serif;
  color: var(--muted);
}

.csp-08__foot.is-dirty span {
  color: oklch(0.48 0.12 65);
  font-weight: 600;
}

.csp-08__foot div {
  display: flex;
  gap: 8px;
}

.csp-08__btn {
  min-height: 42px;
  padding: 0 16px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--surface);
  font: 600 13.5px/1 system-ui,sans-serif;
  color: var(--ink);
  cursor: pointer;
}

.csp-08__btn--primary {
  border-color: transparent;
  color: #fff;
  background: var(--accent);
}

.csp-08__btn:disabled {
  opacity: .45;
  cursor: not-allowed;
}

.csp-08__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .csp-08 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-08');
  var table = root.querySelector('[data-table]');
  var boxes = Array.prototype.slice.call(table.querySelectorAll('tbody input'));
  var foot = root.querySelector('[data-foot]'), diff = root.querySelector('[data-diff]');
  var save = root.querySelector('[data-save]'), reset = root.querySelector('[data-reset]');
  var snap = boxes.map(function (b) { return b.checked; });
  var heads = table.querySelectorAll('[data-c]');

  function update() {
    heads.forEach(function (h, i) {
      var col = boxes.filter(function (b) { return b.parentElement.cellIndex === i + 1; });
      h.textContent = col.filter(function (b) { return b.checked; }).length + ' of ' + col.length;
    });
    var n = 0;
    boxes.forEach(function (b, i) { var ch = b.checked !== snap[i]; b.classList.toggle('is-changed', ch); if (ch) n++; });
    foot.classList.toggle('is-dirty', n > 0);
    diff.textContent = n ? n + ' unsaved change' + (n > 1 ? 's' : '') : 'No unsaved changes';
    save.disabled = reset.disabled = n === 0;
  }
  table.addEventListener('change', update);
  reset.addEventListener('click', function () { boxes.forEach(function (b, i) { b.checked = snap[i]; }); update(); });
  save.addEventListener('click', function () {
    snap = boxes.map(function (b) { return b.checked; });
    update(); diff.textContent = 'Permissions saved';
  });
  update();
})();
```
