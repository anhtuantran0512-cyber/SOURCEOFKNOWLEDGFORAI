---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/danger-zone-delete-account/"
title: "Danger Zone Delete Account Section"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A responsible danger zone: clearly separated destructive actions (transfer ownership, archive workspace, delete account) in a red-accented section, and a…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Danger Zone Delete Account Section
Source: https://codefronts.com/layouts/css-settings-pages/danger-zone-delete-account/

A responsible danger zone: clearly separated destructive actions (transfer ownership, archive workspace, delete account) in a red-accented section, and a delete flow in a native <dialog> that spells out exactly what will be lost, offers a data export first, requires typing the workspace name to enable the button, then confirms with a 30-day grace period and an Undo. Built to prevent accidents without feeling hostile.
## HTML
```html
<section class="csp-18">
  <div class="csp-18__wrap">
    <header class="csp-18__head"><h1>Workspace settings</h1><p>acme-studio · Business plan · 12 members</p></header>

    <div class="csp-18__zone" data-zone>
      <h2>Danger zone</h2>
      <div class="csp-18__row">
        <div><b>Transfer ownership</b><small>Make another admin the owner of this workspace. You'll become an admin.</small></div>
        <button type="button" class="csp-18__btn">Transfer</button>
      </div>
      <div class="csp-18__row">
        <div><b data-archtitle>Archive workspace</b><small data-archtext>Make the workspace read-only. Members keep access to view content. Reversible any time.</small></div>
        <button type="button" class="csp-18__btn" data-archive>Archive</button>
      </div>
      <div class="csp-18__row csp-18__row--delete">
        <div><b>Delete this workspace</b><small>Permanently remove the workspace, all projects, files and member access. This can't be undone after 30 days.</small></div>
        <button type="button" class="csp-18__btn csp-18__btn--danger" data-open>Delete workspace</button>
      </div>
      <div class="csp-18__scheduled" data-scheduled>
        <div><b>Scheduled for deletion on <span data-date></span></b><small>The workspace is locked. You can restore it until then.</small></div>
        <button type="button" class="csp-18__btn" data-undo>Undo deletion</button>
      </div>
    </div>
  </div>

  <dialog class="csp-18__dialog" data-dialog aria-labelledby="csp18-t">
    <form method="dialog" class="csp-18__dform" data-form>
      <span class="csp-18__warnico" aria-hidden="true"></span>
      <h2 id="csp18-t">Delete acme-studio?</h2>
      <p>This will be scheduled immediately and completed in 30 days:</p>
      <ul class="csp-18__list">
        <li><b>248 projects</b> and every file, comment and version</li>
        <li><b>12 members</b> lose access instantly</li>
        <li>Your <b>Business subscription</b> is cancelled — no further charges</li>
        <li>API keys and webhooks stop working</li>
      </ul>
      <a class="csp-18__export" href="#">Export your data first →</a>
      <label class="csp-18__confirm"><span>Type <code>acme-studio</code> to confirm</span><input data-input pattern="acme-studio" required autocomplete="off" spellcheck="false"></label>
      <div class="csp-18__dfoot">
        <button type="button" class="csp-18__btn" data-close autofocus>Cancel</button>
        <button type="submit" class="csp-18__btn csp-18__btn--danger csp-18__del" data-del disabled>Delete acme-studio</button>
      </div>
    </form>
  </dialog>
  <p class="csp-18__sr" aria-live="polite" data-live></p>
</section>
```
## CSS
```css
.csp-18,
.csp-18 *,
.csp-18 *::before,
.csp-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-18 {
  --bg: oklch(0.14 0.01 20);
  --surface: oklch(0.185 0.012 20);
  --raised: oklch(0.22 0.014 20);
  --text: oklch(0.95 0.006 20);
  --muted: oklch(0.7 0.015 20);
  --line: oklch(0.29 0.014 20);
  --danger: oklch(0.62 0.21 25);
  --danger-soft: oklch(0.62 0.21 25/.12);
  color-scheme: dark;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 20px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--text);
  width: 100%;
}

.csp-18__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.csp-18__wrap {
  max-width: 760px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.csp-18__head h1 {
  font: 700 28px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-18__head p {
  font: 400 14px/1.5 ui-monospace,Menlo,monospace;
  color: var(--muted);
  margin-top: 8px;
}

.csp-18__zone {
  border: 1px solid oklch(0.62 0.21 25/.45);
  border-radius: 18px;
  background: linear-gradient(180deg,oklch(0.62 0.21 25/.06),transparent 40%),var(--surface);
  overflow: hidden;
}

.csp-18__zone h2 {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 20px;
  font: 650 15px/1 system-ui,sans-serif;
  color: oklch(0.78 0.14 25);
  border-bottom: 1px solid oklch(0.62 0.21 25/.3);
}

.csp-18__zone h2::before {
  content: "";
  width: 18px;
  height: 18px;
  background: currentColor;
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M10 2.5 18 17H2z' fill='none' stroke='black' stroke-width='1.6' stroke-linejoin='round'/%3E%3Cpath d='M10 8v4M10 14.2v.3' stroke='black' stroke-width='1.8' stroke-linecap='round'/%3E%3C/svg%3E") center/contain no-repeat;
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M10 2.5 18 17H2z' fill='none' stroke='black' stroke-width='1.6' stroke-linejoin='round'/%3E%3Cpath d='M10 8v4M10 14.2v.3' stroke='black' stroke-width='1.8' stroke-linecap='round'/%3E%3C/svg%3E") center/contain no-repeat;
}

.csp-18__row,
.csp-18__scheduled {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 18px 20px;
}

.csp-18__row+.csp-18__row {
  border-top: 1px solid var(--line);
}

.csp-18__row b,
.csp-18__scheduled b {
  display: block;
  font: 600 14.5px/1.3 system-ui,sans-serif;
}

.csp-18__row small,
.csp-18__scheduled small {
  display: block;
  max-width: 460px;
  margin-top: 4px;
  font: 400 13px/1.5 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.csp-18__scheduled {
  display: none;
  background: var(--danger-soft);
}

.csp-18__zone.is-scheduled .csp-18__row {
  display: none;
}

.csp-18__zone.is-scheduled .csp-18__scheduled {
  display: flex;
}

.csp-18__zone.is-archived [data-archtitle]::after {
  content: "Archived";
  margin-left: 8px;
  padding: 3px 7px;
  border-radius: 999px;
  font: 650 10.5px/1 system-ui,sans-serif;
  color: oklch(0.82 0.13 75);
  background: oklch(0.82 0.13 75/.14);
  vertical-align: 2px;
}

.csp-18__btn {
  flex: none;
  min-height: 42px;
  padding: 0 16px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--raised);
  font: 600 13.5px/1 system-ui,sans-serif;
  color: var(--text);
  cursor: pointer;
  transition: all .15s;
  white-space: nowrap;
}

.csp-18__btn:hover {
  border-color: oklch(0.42 0.02 20);
}

.csp-18__btn--danger {
  color: #fff;
  background: var(--danger);
  border-color: transparent;
}

.csp-18__btn--danger:hover {
  background: oklch(0.56 0.21 25);
}

.csp-18__btn:focus-visible,
.csp-18__export:focus-visible {
  outline: 2px solid oklch(0.78 0.14 25);
  outline-offset: 3px;
}

.csp-18__dialog {
  margin: auto;
  width: min(480px,calc(100% - 32px));
  padding: 0;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: var(--surface);
  color: var(--text);
  box-shadow: 0 40px 90px -30px oklch(0 0 0/.85);
  transition: opacity .25s,translate .25s,overlay .25s allow-discrete,display .25s allow-discrete;
}

.csp-18__dialog::backdrop {
  background: oklch(0.08 0.02 20/.75);
  backdrop-filter: blur(4px);
}

@starting-style {
  .csp-18__dialog[open] {
    opacity: 0;
    translate: 0 14px;
  }
}

.csp-18__dform {
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding: 26px;
}

.csp-18__warnico {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: var(--danger-soft) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M4 7h16M9 7V4.5h6V7M6.5 7l1 13h9l1-13' fill='none' stroke='%23ff7a6b' stroke-width='1.7' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/24px no-repeat;
}

.csp-18__dform h2 {
  font: 700 20px/1.2 system-ui,sans-serif;
  letter-spacing: -.015em;
}

.csp-18__dform>p {
  font: 400 14px/1.5 system-ui,sans-serif;
  color: var(--muted);
}

.csp-18__list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 14px 16px;
  border-radius: 12px;
  background: var(--bg);
  border: 1px solid var(--line);
}

.csp-18__list li {
  display: flex;
  gap: 10px;
  font: 400 13.5px/1.45 system-ui,sans-serif;
  color: var(--muted);
}

.csp-18__list li::before {
  content: "";
  flex: none;
  width: 6px;
  height: 6px;
  margin-top: 7px;
  border-radius: 50%;
  background: var(--danger);
}

.csp-18__list b {
  color: var(--text);
  font-weight: 600;
}

.csp-18__export {
  align-self: flex-start;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: oklch(0.8 0.1 240);
  text-decoration: none;
}

.csp-18__export:hover {
  text-decoration: underline;
}

.csp-18__confirm {
  display: flex;
  flex-direction: column;
  gap: 8px;
  font: 500 13.5px/1.3 system-ui,sans-serif;
}

.csp-18__confirm code {
  padding: 2px 6px;
  border-radius: 5px;
  font: 600 12.5px/1 ui-monospace,Menlo,monospace;
  background: var(--raised);
  color: var(--text);
}

.csp-18__confirm input {
  min-height: 46px;
  padding: 0 14px;
  border: 1px solid var(--line);
  border-radius: 11px;
  background: var(--bg);
  font: 500 15px/1 ui-monospace,Menlo,monospace;
  color: var(--text);
  transition: border-color .15s,box-shadow .15s;
}

.csp-18__confirm input:focus {
  outline: none;
  border-color: var(--danger);
  box-shadow: 0 0 0 4px var(--danger-soft);
}

.csp-18__confirm input:valid {
  border-color: oklch(0.62 0.21 25/.8);
}

.csp-18__dfoot {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  padding-top: 6px;
}

.csp-18__del {
  opacity: .4;
  pointer-events: none;
}

.csp-18__dialog:has(input:valid) .csp-18__del {
  opacity: 1;
  pointer-events: auto;
}

.csp-18__del[data-busy] {
  opacity: .7;
  pointer-events: none;
}

@media (max-width: 560px) {
  .csp-18__row,
    .csp-18__scheduled {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-18 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-18');
  var dlg = root.querySelector('[data-dialog]'), form = root.querySelector('[data-form]');
  var input = root.querySelector('[data-input]'), del = root.querySelector('[data-del]');
  var zone = root.querySelector('[data-zone]'), live = root.querySelector('[data-live]');

  root.querySelector('[data-open]').addEventListener('click', function () { form.reset(); del.disabled = true; dlg.showModal(); input.focus(); });
  root.querySelector('[data-close]').addEventListener('click', function () { dlg.close(); });
  input.addEventListener('input', function () { del.disabled = !input.validity.valid; });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!input.validity.valid) return;
    del.dataset.busy = ''; del.textContent = 'Deleting…';
    setTimeout(function () {
      delete del.dataset.busy; del.textContent = 'Delete acme-studio';
      dlg.close();
      var d = new Date(); d.setDate(d.getDate() + 30);
      root.querySelector('[data-date]').textContent = d.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
      zone.classList.add('is-scheduled');
      live.textContent = 'Workspace scheduled for deletion in 30 days';
      root.querySelector('[data-undo]').focus();
    }, 900);
  });
  root.querySelector('[data-undo]').addEventListener('click', function () {
    zone.classList.remove('is-scheduled'); live.textContent = 'Deletion cancelled. Workspace restored.';
  });

  var arch = root.querySelector('[data-archive]');
  arch.addEventListener('click', function () {
    var on = zone.classList.toggle('is-archived');
    arch.textContent = on ? 'Unarchive' : 'Archive';
    root.querySelector('[data-archtext]').textContent = on ? 'The workspace is read-only. Unarchive to allow edits again.' : 'Make the workspace read-only. Members keep access to view content. Reversible any time.';
    live.textContent = on ? 'Workspace archived' : 'Workspace unarchived';
  });
})();
```
