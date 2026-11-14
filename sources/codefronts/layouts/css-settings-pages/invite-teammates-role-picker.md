---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/invite-teammates-role-picker/"
title: "Invite Teammates Form with Role Picker"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A fast, forgiving invite flow: paste a whole list of emails or type them one by one and they become validated chips (invalid ones turn red and are skipped),…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Invite Teammates Form with Role Picker
Source: https://codefronts.com/layouts/css-settings-pages/invite-teammates-role-picker/

A fast, forgiving invite flow: paste a whole list of emails or type them one by one and they become validated chips (invalid ones turn red and are skipped), pick a role from descriptive radio cards that explain exactly what each role can do, add an optional personal note, and send. The primary button counts invites live, a seat warning appears when you'd exceed your plan, and a shareable invite link has one-click copy.
## HTML
```html
<section class="csp-07">
  <form class="csp-07__card" data-form novalidate>
    <header class="csp-07__head">
      <h1>Invite teammates</h1>
      <p>They'll get an email to join <b>Northwind</b>. You have <b data-left>3</b> seats left.</p>
    </header>

    <div class="csp-07__group">
      <label class="csp-07__label" for="csp07-email">Email addresses</label>
      <div class="csp-07__chips" data-box>
        <input id="csp07-email" data-input type="text" autocomplete="off" placeholder="[email protected], …" aria-describedby="csp07-hint">
      </div>
      <p class="csp-07__hint" id="csp07-hint">Separate with commas or press Enter. Paste a list to add many at once.</p>
    </div>

    <fieldset class="csp-07__roles">
      <legend class="csp-07__label">Role</legend>
      <label class="csp-07__role">
        <input type="radio" name="csp07-role" value="Admin">
        <span class="csp-07__ico" style="--h:290">A</span>
        <span class="csp-07__rtext"><b>Admin</b><small>Manage members, billing and all workspace settings.</small></span>
      </label>
      <label class="csp-07__role">
        <input type="radio" name="csp07-role" value="Member" checked>
        <span class="csp-07__ico" style="--h:200">M</span>
        <span class="csp-07__rtext"><b>Member</b><small>Create and edit projects. Can't change billing.</small></span>
      </label>
      <label class="csp-07__role">
        <input type="radio" name="csp07-role" value="Viewer">
        <span class="csp-07__ico" style="--h:150">V</span>
        <span class="csp-07__rtext"><b>Viewer</b><small>View and comment only. Free — doesn't use a seat.</small></span>
      </label>
    </fieldset>

    <details class="csp-07__note">
      <summary>Add a personal message</summary>
      <textarea rows="3" maxlength="280" placeholder="Hey! Join us on Northwind so we can plan the Q4 launch together."></textarea>
    </details>

    <p class="csp-07__warn" data-warn hidden>You're inviting more people than you have seats. Extra members will be added to your next invoice at $24/seat.</p>

    <footer class="csp-07__foot">
      <button type="button" class="csp-07__ghost" data-copy><span data-copytext>Copy invite link</span></button>
      <button type="submit" class="csp-07__send" data-send disabled>Send invites</button>
    </footer>
    <p class="csp-07__sr" aria-live="polite" data-live></p>
  </form>
</section>
```
## CSS
```css
.csp-07,
.csp-07 *,
.csp-07 *::before,
.csp-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-07 {
  --bg: oklch(0.965 0.012 75);
  --surface: #fff;
  --ink: oklch(0.22 0.02 50);
  --muted: oklch(0.5 0.02 50);
  --line: oklch(0.9 0.012 70);
  --accent: oklch(0.5 0.2 285);
  --ring: oklch(0.5 0.2 285/.18);
  --bad: oklch(0.56 0.2 25);
  color-scheme: light;
  display: grid;
  align-items: center;
  justify-items: center;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 20px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: radial-gradient(60% 50% at 50% 0%,oklch(0.93 0.04 290/.7),transparent),var(--bg);
  color: var(--ink);
  accent-color: var(--accent);
  width: 100%;
}

.csp-07__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.csp-07__card {
  width: min(540px,100%);
  display: flex;
  flex-direction: column;
  gap: 22px;
  padding: 30px;
  border-radius: 24px;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 1px 2px oklch(0 0 0/.04),0 30px 60px -36px oklch(0.3 0.08 285/.45);
}

.csp-07__head h1 {
  font: 700 24px/1.15 system-ui,sans-serif;
  letter-spacing: -.02em;
}

.csp-07__head p {
  font: 400 14.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
}

.csp-07__head b {
  color: var(--ink);
  font-weight: 650;
}

.csp-07__group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.csp-07__label {
  font: 600 13.5px/1 system-ui,sans-serif;
  margin-bottom: 2px;
}

.csp-07__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  min-height: 52px;
  padding: 7px;
  border: 1px solid var(--line);
  border-radius: 13px;
  background: var(--surface);
  cursor: text;
  transition: border-color .15s,box-shadow .15s;
}

.csp-07__chips:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px var(--ring);
}

.csp-07__chips input {
  flex: 1 0 160px;
  min-height: 36px;
  padding: 0 8px;
  border: 0;
  outline: 0;
  background: transparent;
  font: 400 14.5px/1 system-ui,sans-serif;
  color: var(--ink);
}

.csp-07__chip {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  height: 36px;
  padding: 0 4px 0 12px;
  border-radius: 9px;
  font: 500 13.5px/1 system-ui,sans-serif;
  color: oklch(0.35 0.14 285);
  background: oklch(0.95 0.03 285);
  animation: csp07-pop .2s cubic-bezier(.3,.7,.3,1.4);
}

.csp-07__chip.is-bad {
  color: var(--bad);
  background: oklch(0.96 0.03 25);
  text-decoration: line-through wavy oklch(0.56 0.2 25/.5);
}

.csp-07__chip button {
  display: grid;
  place-items: center;
  width: 28px;
  height: 28px;
  border: 0;
  border-radius: 7px;
  background: transparent;
  color: inherit;
  font: 500 16px/1 system-ui,sans-serif;
  cursor: pointer;
}

.csp-07__chip button:hover {
  background: oklch(0 0 0/.06);
}

.csp-07__chip button:focus-visible {
  outline: 2px solid var(--accent);
}

.csp-07__hint {
  font: 400 12.5px/1.4 system-ui,sans-serif;
  color: var(--muted);
}

.csp-07__roles {
  border: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.csp-07__role {
  position: relative;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 64px;
  padding: 12px 44px 12px 14px;
  border: 1px solid var(--line);
  border-radius: 14px;
  cursor: pointer;
  transition: border-color .15s,background .15s,box-shadow .15s;
}

.csp-07__role:hover {
  border-color: oklch(0.82 0.02 285);
}

.csp-07__role input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.csp-07__role::after {
  content: "";
  position: absolute;
  right: 16px;
  top: 50%;
  width: 20px;
  height: 20px;
  margin-top: -10px;
  border-radius: 50%;
  border: 1.5px solid var(--line);
  transition: all .2s;
}

.csp-07__role:has(input:checked) {
  border-color: var(--accent);
  background: oklch(0.98 0.012 285);
  box-shadow: 0 0 0 1px var(--accent);
}

.csp-07__role:has(input:checked)::after {
  border-color: var(--accent);
  background: var(--accent) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='m6 10.2 2.6 2.6L14 7.4' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/20px;
}

.csp-07__role:has(input:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-07__ico {
  flex: none;
  display: grid;
  place-items: center;
  width: 38px;
  height: 38px;
  border-radius: 11px;
  font: 700 14px/1 system-ui,sans-serif;
  color: oklch(0.4 0.14 var(--h));
  background: oklch(0.94 0.05 var(--h));
}

.csp-07__rtext {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.csp-07__rtext b {
  font: 600 14.5px/1.2 system-ui,sans-serif;
}

.csp-07__rtext small {
  font: 400 13px/1.4 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.csp-07__note summary {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  min-height: 36px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: var(--accent);
  cursor: pointer;
  list-style: none;
}

.csp-07__note summary::-webkit-details-marker {
  display: none;
}

.csp-07__note summary::before {
  content: "+";
  font-size: 17px;
  transition: rotate .2s;
}

.csp-07__note[open] summary::before {
  rotate: 45deg;
}

.csp-07__note textarea {
  width: 100%;
  margin-top: 8px;
  padding: 12px 14px;
  border: 1px solid var(--line);
  border-radius: 12px;
  font: 400 14px/1.5 system-ui,sans-serif;
  color: var(--ink);
  resize: vertical;
}

.csp-07__note textarea:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px var(--ring);
}

.csp-07__warn {
  padding: 12px 14px;
  border-radius: 12px;
  font: 400 13px/1.5 system-ui,sans-serif;
  color: oklch(0.42 0.1 65);
  background: oklch(0.96 0.05 85);
}

.csp-07__foot {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  flex-wrap: wrap;
  padding-top: 18px;
  border-top: 1px solid var(--line);
}

.csp-07__ghost,
.csp-07__send {
  min-height: 46px;
  padding: 0 18px;
  border-radius: 12px;
  font: 650 14px/1 system-ui,sans-serif;
  cursor: pointer;
  transition: background .15s,opacity .15s,transform .1s;
}

.csp-07__ghost {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
}

.csp-07__ghost::before {
  content: "";
  width: 15px;
  height: 15px;
  background: currentColor;
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M6.5 9.5a3 3 0 0 0 4.2 0l2.3-2.3a3 3 0 0 0-4.2-4.2L8 3.8M9.5 6.5a3 3 0 0 0-4.2 0L3 8.8A3 3 0 0 0 7.2 13l.8-.8' fill='none' stroke='black' stroke-width='1.5' stroke-linecap='round'/%3E%3C/svg%3E") center/contain no-repeat;
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M6.5 9.5a3 3 0 0 0 4.2 0l2.3-2.3a3 3 0 0 0-4.2-4.2L8 3.8M9.5 6.5a3 3 0 0 0-4.2 0L3 8.8A3 3 0 0 0 7.2 13l.8-.8' fill='none' stroke='black' stroke-width='1.5' stroke-linecap='round'/%3E%3C/svg%3E") center/contain no-repeat;
}

.csp-07__ghost:hover {
  background: oklch(0.975 0.006 70);
}

.csp-07__ghost.is-done {
  color: oklch(0.45 0.12 155);
  border-color: oklch(0.85 0.06 155);
}

.csp-07__send {
  flex: 1 1 180px;
  border: 0;
  color: #fff;
  background: var(--accent);
}

.csp-07__send:hover:not(:disabled) {
  background: oklch(0.45 0.2 285);
}

.csp-07__send:active:not(:disabled) {
  transform: scale(.99);
}

.csp-07__send:disabled {
  opacity: .4;
  cursor: not-allowed;
}

.csp-07__ghost:focus-visible,
.csp-07__send:focus-visible,
.csp-07__note summary:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

@keyframes csp07-pop {
  from {
    scale: .7;
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-07 * {
    transition: none!important;
    animation: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-07');
  var form = root.querySelector('[data-form]'), box = root.querySelector('[data-box]'), input = root.querySelector('[data-input]');
  var send = root.querySelector('[data-send]'), warn = root.querySelector('[data-warn]'), live = root.querySelector('[data-live]');
  var seats = parseInt(root.querySelector('[data-left]').textContent, 10);
  var probe = document.createElement('input'); probe.type = 'email';
  var isEmail = function (v) { probe.value = v; return v.indexOf('@') > 0 && probe.checkValidity(); };
  var emails = [];

  function update() {
    var ok = emails.filter(function (e) { return e.ok; }).length;
    var role = form.querySelector('input[name=csp07-role]:checked').value;
    send.disabled = ok === 0;
    send.textContent = ok ? 'Send ' + ok + ' invite' + (ok > 1 ? 's' : '') : 'Send invites';
    warn.hidden = !(role !== 'Viewer' && ok > seats);
  }
  function addChip(raw) {
    var v = raw.trim().toLowerCase();
    if (!v || emails.some(function (e) { return e.v === v; })) return;
    var entry = { v: v, ok: isEmail(v) };
    emails.push(entry);
    var chip = document.createElement('span');
    chip.className = 'csp-07__chip' + (entry.ok ? '' : ' is-bad');
    chip.textContent = v;
    var x = document.createElement('button');
    x.type = 'button'; x.textContent = '×'; x.setAttribute('aria-label', 'Remove ' + v);
    x.addEventListener('click', function () { emails.splice(emails.indexOf(entry), 1); chip.remove(); update(); input.focus(); });
    chip.appendChild(x);
    box.insertBefore(chip, input);
  }
  function flush() { input.value.split(/[\s,;]+/).forEach(addChip); input.value = ''; update(); }

  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ',' || e.key === ' ') { e.preventDefault(); flush(); }
    if (e.key === 'Backspace' && !input.value && emails.length) { emails.pop(); box.querySelectorAll('.csp-07__chip')[emails.length].remove(); update(); }
  });
  input.addEventListener('paste', function (e) { e.preventDefault(); input.value = (e.clipboardData || window.clipboardData).getData('text'); flush(); });
  input.addEventListener('blur', flush);
  box.addEventListener('click', function (e) { if (e.target === box) input.focus(); });
  form.addEventListener('change', update);

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var ok = emails.filter(function (x) { return x.ok; }).length;
    if (!ok) return;
    live.textContent = ok + ' invites sent';
    send.textContent = '✓ ' + ok + ' invite' + (ok > 1 ? 's' : '') + ' sent';
    send.disabled = true;
    setTimeout(function () { emails = []; box.querySelectorAll('.csp-07__chip').forEach(function (c) { c.remove(); }); update(); }, 1800);
  });

  var copy = root.querySelector('[data-copy]');
  copy.addEventListener('click', function () {
    var link = 'https://app.northwind.co/join/7Kp2-xQ9v';
    var done = function () { copy.classList.add('is-done'); copy.querySelector('[data-copytext]').textContent = 'Link copied'; live.textContent = 'Invite link copied'; setTimeout(function () { copy.classList.remove('is-done'); copy.querySelector('[data-copytext]').textContent = 'Copy invite link'; }, 2000); };
    if (navigator.clipboard) navigator.clipboard.writeText(link).then(done, done); else done();
  });
  update();
})();
```
