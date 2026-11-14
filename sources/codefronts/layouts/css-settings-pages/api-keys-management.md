---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/api-keys-management/"
title: "API Keys Management Page"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A developer-grade API keys page: masked secret keys with copy-to-clipboard, scope and environment badges, created / last-used metadata, a safe two-step…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: API Keys Management Page
Source: https://codefronts.com/layouts/css-settings-pages/api-keys-management/

A developer-grade API keys page: masked secret keys with copy-to-clipboard, scope and environment badges, created / last-used metadata, a safe two-step revoke, and a native <dialog> to create new keys with name, permission level and expiry. The new secret is shown exactly once in a highlighted reveal panel with copy and a clear 'you won't see this again' warning — the pattern used by every serious API platform.
## HTML
```html
<section class="csp-09">
  <div class="csp-09__wrap">
    <header class="csp-09__head">
      <div><h1>API keys</h1><p>Authenticate requests to the Northwind REST API. Keep secret keys out of client-side code.</p></div>
      <button type="button" class="csp-09__btn" data-open>Create secret key</button>
    </header>

    <div class="csp-09__card">
      <div class="csp-09__thead" aria-hidden="true"><span>Name</span><span>Key</span><span>Created</span><span>Last used</span><span></span></div>
      <ul class="csp-09__list" data-list>
        <li class="csp-09__row">
          <span class="csp-09__name"><b>Production server</b><span class="csp-09__badges"><em class="is-live">Live</em><em>Full access</em></span></span>
          <span class="csp-09__key"><code>sk_live_••••••••••••3f9a</code><button type="button" class="csp-09__icon" data-copy="sk-demo-REDACTED_3f9a" aria-label="Copy key prefix">Copy</button></span>
          <span class="csp-09__meta">Mar 2, 2026</span>
          <span class="csp-09__meta"><i class="csp-09__dot"></i>2 minutes ago</span>
          <button type="button" class="csp-09__revoke" data-revoke>Revoke</button>
        </li>
        <li class="csp-09__row">
          <span class="csp-09__name"><b>Analytics pipeline</b><span class="csp-09__badges"><em class="is-live">Live</em><em>Read only</em></span></span>
          <span class="csp-09__key"><code>sk_live_••••••••••••a71c</code><button type="button" class="csp-09__icon" data-copy="sk-demo-REDACTED_a71c" aria-label="Copy key prefix">Copy</button></span>
          <span class="csp-09__meta">Jun 18, 2026</span>
          <span class="csp-09__meta">Yesterday</span>
          <button type="button" class="csp-09__revoke" data-revoke>Revoke</button>
        </li>
        <li class="csp-09__row">
          <span class="csp-09__name"><b>Local development</b><span class="csp-09__badges"><em class="is-test">Test</em><em>Restricted</em></span></span>
          <span class="csp-09__key"><code>sk_test_••••••••••••09be</code><button type="button" class="csp-09__icon" data-copy="sk-demo-REDACTED_09be" aria-label="Copy key prefix">Copy</button></span>
          <span class="csp-09__meta">Sep 30, 2026</span>
          <span class="csp-09__meta csp-09__meta--dim">Never</span>
          <button type="button" class="csp-09__revoke" data-revoke>Revoke</button>
        </li>
      </ul>
    </div>
    <p class="csp-09__foot">Keys inherit the permissions of their creator. <a href="#">Read the authentication docs →</a></p>
  </div>

  <dialog class="csp-09__dialog" data-dialog aria-labelledby="csp09-title">
    <form class="csp-09__dform" data-form>
      <div data-step="create">
        <h2 id="csp09-title">Create secret key</h2>
        <label class="csp-09__field"><span>Name</span><input name="name" required placeholder="e.g. Billing worker" autocomplete="off"></label>
        <fieldset class="csp-09__perms">
          <legend>Permissions</legend>
          <label><input type="radio" name="perm" value="Full access" checked><span><b>Full access</b><small>Read and write to every resource</small></span></label>
          <label><input type="radio" name="perm" value="Restricted"><span><b>Restricted</b><small>Choose specific scopes after creation</small></span></label>
          <label><input type="radio" name="perm" value="Read only"><span><b>Read only</b><small>GET requests only</small></span></label>
        </fieldset>
        <label class="csp-09__field"><span>Expires</span><select name="exp"><option>In 30 days</option><option selected>In 90 days</option><option>In 1 year</option><option>Never</option></select></label>
        <div class="csp-09__dfoot"><button type="button" class="csp-09__ghost" data-close>Cancel</button><button type="submit" class="csp-09__btn">Create key</button></div>
      </div>
      <div data-step="reveal" hidden>
        <h2>Save your key</h2>
        <p class="csp-09__warn">This is the only time the full key will be shown. Store it in your secrets manager now.</p>
        <div class="csp-09__secret"><code data-secret></code><button type="button" class="csp-09__btn" data-copysecret>Copy</button></div>
        <div class="csp-09__dfoot"><button type="button" class="csp-09__btn" data-close>Done</button></div>
      </div>
    </form>
  </dialog>
  <p class="csp-09__sr" aria-live="polite" data-live></p>
</section>
```
## CSS
```css
.csp-09,
.csp-09 *,
.csp-09 *::before,
.csp-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-09 {
  --bg: oklch(0.14 0.008 150);
  --surface: oklch(0.18 0.01 150);
  --raised: oklch(0.22 0.012 150);
  --text: oklch(0.95 0.008 150);
  --muted: oklch(0.68 0.015 150);
  --line: oklch(0.28 0.012 150);
  --accent: oklch(0.86 0.19 128);
  --accent-ink: oklch(0.22 0.06 128);
  --bad: oklch(0.68 0.19 25);
  color-scheme: dark;
  container-type: inline-size;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 22px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--text);
  accent-color: var(--accent);
  width: 100%;
}

.csp-09__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.csp-09__wrap {
  max-width: 980px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.csp-09__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px;
}

.csp-09__head h1 {
  font: 700 30px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-09__head p {
  max-width: 520px;
  font: 400 14.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
  text-wrap: pretty;
}

.csp-09__btn {
  min-height: 44px;
  padding: 0 18px;
  border: 0;
  border-radius: 10px;
  font: 650 14px/1 system-ui,sans-serif;
  color: var(--accent-ink);
  background: var(--accent);
  cursor: pointer;
  transition: filter .15s,transform .1s;
}

.csp-09__btn:hover {
  filter: brightness(1.07);
}

.csp-09__btn:active {
  transform: scale(.98);
}

.csp-09__ghost {
  min-height: 44px;
  padding: 0 18px;
  border: 1px solid var(--line);
  border-radius: 10px;
  font: 600 14px/1 system-ui,sans-serif;
  color: var(--text);
  background: transparent;
  cursor: pointer;
}

.csp-09__btn:focus-visible,
.csp-09__ghost:focus-visible,
.csp-09__icon:focus-visible,
.csp-09__revoke:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-09__card {
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--surface);
  overflow: hidden;
}

.csp-09__thead,
.csp-09__row {
  display: grid;
  grid-template-columns: minmax(0,1.3fr) minmax(0,1.6fr) 110px 130px 96px;
  align-items: center;
  gap: 14px;
  padding: 0 18px;
}

.csp-09__thead {
  min-height: 40px;
  font: 600 11.5px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
  border-bottom: 1px solid var(--line);
  background: oklch(1 0 0/.02);
}

.csp-09__list {
  list-style: none;
}

.csp-09__row {
  min-height: 72px;
  padding-block: 12px;
  border-bottom: 1px solid var(--line);
  transition: background .15s,opacity .3s;
}

.csp-09__row:last-child {
  border-bottom: 0;
}

.csp-09__row:hover {
  background: oklch(1 0 0/.025);
}

.csp-09__row.is-new {
  animation: csp09-flash 1.8s ease;
}

.csp-09__row.is-revoked {
  opacity: .45;
}

.csp-09__row.is-revoked code {
  text-decoration: line-through;
}

.csp-09__name {
  display: flex;
  flex-direction: column;
  gap: 6px;
  min-width: 0;
}

.csp-09__name b {
  font: 600 14px/1.2 system-ui,sans-serif;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.csp-09__badges {
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
}

.csp-09__badges em {
  font: 600 10.5px/1 system-ui,sans-serif;
  font-style: normal;
  padding: 4px 7px;
  border-radius: 5px;
  color: var(--muted);
  background: oklch(1 0 0/.06);
}

.csp-09__badges em.is-live {
  color: var(--accent);
  background: oklch(0.86 0.19 128/.12);
}

.csp-09__badges em.is-test {
  color: oklch(0.82 0.13 75);
  background: oklch(0.82 0.13 75/.12);
}

.csp-09__badges em.is-revoked {
  color: var(--bad);
  background: oklch(0.68 0.19 25/.14);
}

.csp-09__key {
  display: flex;
  align-items: center;
  gap: 8px;
  min-width: 0;
}

.csp-09__key code {
  flex: 1;
  min-width: 0;
  padding: 7px 10px;
  border-radius: 8px;
  font: 500 12.5px/1 ui-monospace,Menlo,monospace;
  font-variant-ligatures: none;
  color: var(--text);
  background: var(--bg);
  border: 1px solid var(--line);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.csp-09__icon {
  flex: none;
  min-height: 32px;
  padding: 0 10px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--raised);
  font: 600 12px/1 system-ui,sans-serif;
  color: var(--text);
  cursor: pointer;
  transition: all .15s;
}

.csp-09__icon:hover {
  border-color: oklch(0.4 0.02 150);
}

.csp-09__icon.is-done {
  color: var(--accent-ink);
  background: var(--accent);
  border-color: transparent;
}

.csp-09__meta {
  display: flex;
  align-items: center;
  gap: 7px;
  font: 400 13px/1.2 system-ui,sans-serif;
  color: var(--muted);
}

.csp-09__meta--dim {
  opacity: .6;
}

.csp-09__dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 0 3px oklch(0.86 0.19 128/.2);
}

.csp-09__revoke {
  justify-self: end;
  min-height: 36px;
  padding: 0 12px;
  border: 1px solid transparent;
  border-radius: 8px;
  background: transparent;
  font: 600 13px/1 system-ui,sans-serif;
  color: var(--muted);
  cursor: pointer;
  transition: all .15s;
  white-space: nowrap;
}

.csp-09__revoke:hover {
  color: var(--bad);
  border-color: oklch(0.68 0.19 25/.4);
}

.csp-09__revoke.is-confirm {
  color: #fff;
  background: oklch(0.55 0.2 25);
  border-color: transparent;
}

.csp-09__revoke:disabled {
  visibility: hidden;
}

.csp-09__foot {
  font: 400 13px/1.5 system-ui,sans-serif;
  color: var(--muted);
}

.csp-09__foot a {
  color: var(--accent);
  text-decoration: none;
  font-weight: 600;
}

.csp-09__dialog {
  margin: auto;
  width: min(460px,calc(100% - 32px));
  padding: 0;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: var(--surface);
  color: var(--text);
  box-shadow: 0 40px 80px -30px oklch(0 0 0/.8);
  opacity: 1;
  translate: 0 0;
  transition: opacity .25s,translate .25s,overlay .25s allow-discrete,display .25s allow-discrete;
}

.csp-09__dialog::backdrop {
  background: oklch(0.08 0.01 150/.7);
  backdrop-filter: blur(4px);
}

@starting-style {
  .csp-09__dialog[open] {
    opacity: 0;
    translate: 0 14px;
  }
}

.csp-09__dform {
  padding: 26px;
}

.csp-09__dform>div {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.csp-09__dform h2 {
  font: 700 20px/1.2 system-ui,sans-serif;
  letter-spacing: -.015em;
}

.csp-09__field {
  display: flex;
  flex-direction: column;
  gap: 7px;
  font: 550 13px/1 system-ui,sans-serif;
  color: var(--muted);
}

.csp-09__field input,
.csp-09__field select {
  min-height: 44px;
  padding: 0 12px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--bg);
  font: 400 14.5px/1 system-ui,sans-serif;
  color: var(--text);
}

.csp-09__field input:focus,
.csp-09__field select:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.86 0.19 128/.15);
}

.csp-09__perms {
  border: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.csp-09__perms legend {
  font: 550 13px/1 system-ui,sans-serif;
  color: var(--muted);
  margin-bottom: 8px;
}

.csp-09__perms label {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  border: 1px solid var(--line);
  border-radius: 11px;
  cursor: pointer;
  transition: border-color .15s,background .15s;
}

.csp-09__perms label:has(input:checked) {
  border-color: var(--accent);
  background: oklch(0.86 0.19 128/.06);
}

.csp-09__perms input {
  width: 17px;
  height: 17px;
}

.csp-09__perms span {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.csp-09__perms b {
  font: 600 13.5px/1.2 system-ui,sans-serif;
}

.csp-09__perms small {
  font: 400 12.5px/1.3 system-ui,sans-serif;
  color: var(--muted);
}

.csp-09__dfoot {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  padding-top: 4px;
}

.csp-09__warn {
  padding: 12px 14px;
  border-radius: 11px;
  font: 400 13.5px/1.5 system-ui,sans-serif;
  color: oklch(0.88 0.1 80);
  background: oklch(0.82 0.13 75/.1);
  border: 1px solid oklch(0.82 0.13 75/.25);
}

.csp-09__secret {
  display: flex;
  gap: 8px;
  align-items: stretch;
}

.csp-09__secret code {
  flex: 1;
  min-width: 0;
  padding: 12px;
  border-radius: 10px;
  font: 500 13px/1.4 ui-monospace,Menlo,monospace;
  font-variant-ligatures: none;
  word-break: break-all;
  color: var(--accent);
  background: var(--bg);
  border: 1px dashed oklch(0.86 0.19 128/.4);
}

@keyframes csp09-flash {
  0% {
    background: oklch(0.86 0.19 128/.16);
  }

  100% {
    background: transparent;
  }
}

@container (max-width: 760px) {
  .csp-09__thead {
    display: none;
  }

  .csp-09__row {
    grid-template-columns: minmax(0,1fr) auto;
    grid-template-areas: "name revoke" "key key" "c u";
  }

  .csp-09__name {
    grid-area: name;
  }

  .csp-09__key {
    grid-area: key;
  }

  .csp-09__revoke {
    grid-area: revoke;
  }

  .csp-09__row>.csp-09__meta:nth-of-type(3) {
    grid-area: c;
  }

  .csp-09__row>.csp-09__meta:nth-of-type(4) {
    grid-area: u;
    justify-self: end;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-09 * {
    transition: none!important;
    animation: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-09');
  var dlg = root.querySelector('[data-dialog]'), form = root.querySelector('[data-form]');
  var list = root.querySelector('[data-list]'), live = root.querySelector('[data-live]');
  var stepCreate = form.querySelector('[data-step=create]'), stepReveal = form.querySelector('[data-step=reveal]');

  function copy(text, btn) {
    var done = function () {
      var old = btn.textContent; btn.classList.add('is-done'); btn.textContent = 'Copied'; live.textContent = 'Copied to clipboard';
      setTimeout(function () { btn.classList.remove('is-done'); btn.textContent = old; }, 1600);
    };
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, done); else done();
  }
  function genKey() {
    var a = new Uint8Array(24), chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', s = '';
    crypto.getRandomValues(a); a.forEach(function (n) { s += chars[n % chars.length]; });
    return 'sk_live_' + s;
  }

  root.querySelector('[data-open]').addEventListener('click', function () {
    form.reset(); stepCreate.hidden = false; stepReveal.hidden = true; dlg.showModal();
  });
  root.querySelectorAll('[data-close]').forEach(function (b) { b.addEventListener('click', function () { dlg.close(); }); });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.reportValidity()) return;
    var name = form.elements.name.value.trim(), perm = form.elements.perm.value, key = genKey();
    var li = document.createElement('li');
    li.className = 'csp-09__row is-new';
    li.innerHTML = '<span class="csp-09__name"><b></b><span class="csp-09__badges"><em class="is-live">Live</em><em></em></span></span>' +
      '<span class="csp-09__key"><code></code><button type="button" class="csp-09__icon" aria-label="Copy key prefix">Copy</button></span>' +
      '<span class="csp-09__meta">Just now</span><span class="csp-09__meta csp-09__meta--dim">Never</span>' +
      '<button type="button" class="csp-09__revoke" data-revoke>Revoke</button>';
    li.querySelector('b').textContent = name;
    li.querySelectorAll('em')[1].textContent = perm;
    li.querySelector('code').textContent = 'sk_live_••••••••••••' + key.slice(-4);
    li.querySelector('.csp-09__icon').dataset.copy = key.slice(0, 12) + '…' + key.slice(-4);
    list.prepend(li);
    form.querySelector('[data-secret]').textContent = key;
    stepCreate.hidden = true; stepReveal.hidden = false;
  });
  form.querySelector('[data-copysecret]').addEventListener('click', function (e) { copy(form.querySelector('[data-secret]').textContent, e.currentTarget); });

  root.addEventListener('click', function (e) {
    var c = e.target.closest('[data-copy]'); if (c) copy(c.dataset.copy, c);
    var r = e.target.closest('[data-revoke]'); if (!r) return;
    if (!r.classList.contains('is-confirm')) {
      r.classList.add('is-confirm'); r.textContent = 'Confirm';
      clearTimeout(r._t); r._t = setTimeout(function () { r.classList.remove('is-confirm'); r.textContent = 'Revoke'; }, 4000);
      return;
    }
    var row = r.closest('.csp-09__row');
    row.classList.add('is-revoked');
    var badge = row.querySelector('.csp-09__badges em'); badge.className = 'is-revoked'; badge.textContent = 'Revoked';
    r.disabled = true; live.textContent = 'Key revoked';
  });
})();
```
