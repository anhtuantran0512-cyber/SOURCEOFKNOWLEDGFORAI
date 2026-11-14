---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/connected-apps-integrations/"
title: "Connected Apps and Integrations Page"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "An integrations marketplace-style settings page: category tabs that filter cards in pure CSS with :has(), instant search, monogram app tiles, clear connected…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Connected Apps and Integrations Page
Source: https://codefronts.com/layouts/css-settings-pages/connected-apps-integrations/

An integrations marketplace-style settings page: category tabs that filter cards in pure CSS with :has(), instant search, monogram app tiles, clear connected / not-connected status, a connect button that runs through an OAuth-style 'Connecting…' state before flipping to Connected, a Manage / Disconnect pair for connected apps, and a live connected-count badge. The card grid fluidly reflows with auto-fill and minmax.
## HTML
```html
<section class="csp-13">
  <div class="csp-13__wrap">
    <header class="csp-13__head">
      <div><h1>Integrations <span class="csp-13__count" data-count>3 connected</span></h1><p>Connect the tools your team already uses. Data syncs in real time.</p></div>
      <label class="csp-13__search"><span class="csp-13__sr">Search integrations</span><input type="search" placeholder="Search apps" data-q></label>
    </header>

    <fieldset class="csp-13__tabs">
      <legend class="csp-13__sr">Category</legend>
      <input type="radio" name="csp13-c" id="csp13-all" checked><label for="csp13-all">All</label>
      <input type="radio" name="csp13-c" id="csp13-on"><label for="csp13-on">Connected</label>
      <input type="radio" name="csp13-c" id="csp13-comm"><label for="csp13-comm">Communication</label>
      <input type="radio" name="csp13-c" id="csp13-dev"><label for="csp13-dev">Developer</label>
      <input type="radio" name="csp13-c" id="csp13-prod"><label for="csp13-prod">Productivity</label>
    </fieldset>

    <div class="csp-13__grid" data-grid>
      <article class="csp-13__app is-on" data-cat="comm"><div class="csp-13__top"><span class="csp-13__logo" style="--h:330">Sl</span><span class="csp-13__status">Connected</span></div><h2>Slack</h2><p>Post updates to channels and get alerts in DMs.</p><div class="csp-13__act"><button type="button" class="csp-13__btn" data-connect aria-label="Connect Slack">Connect</button><button type="button" class="csp-13__ghost" aria-label="Manage Slack">Manage</button><button type="button" class="csp-13__ghost csp-13__ghost--bad" data-disconnect aria-label="Disconnect Slack">Disconnect</button></div></article>
      <article class="csp-13__app is-on" data-cat="dev"><div class="csp-13__top"><span class="csp-13__logo" style="--h:270">Gh</span><span class="csp-13__status">Connected</span></div><h2>GitHub</h2><p>Link pull requests and commits to tasks automatically.</p><div class="csp-13__act"><button type="button" class="csp-13__btn" data-connect aria-label="Connect GitHub">Connect</button><button type="button" class="csp-13__ghost" aria-label="Manage GitHub">Manage</button><button type="button" class="csp-13__ghost csp-13__ghost--bad" data-disconnect aria-label="Disconnect GitHub">Disconnect</button></div></article>
      <article class="csp-13__app" data-cat="prod"><div class="csp-13__top"><span class="csp-13__logo" style="--h:145">Gd</span><span class="csp-13__status">Connected</span></div><h2>Google Drive</h2><p>Attach Docs, Sheets and Slides with live previews.</p><div class="csp-13__act"><button type="button" class="csp-13__btn" data-connect aria-label="Connect Google Drive">Connect</button><button type="button" class="csp-13__ghost" aria-label="Manage Google Drive">Manage</button><button type="button" class="csp-13__ghost csp-13__ghost--bad" data-disconnect aria-label="Disconnect Google Drive">Disconnect</button></div></article>
      <article class="csp-13__app is-on" data-cat="prod dev"><div class="csp-13__top"><span class="csp-13__logo" style="--h:20">Fi</span><span class="csp-13__status">Connected</span></div><h2>Figma</h2><p>Embed frames that stay in sync with the source file.</p><div class="csp-13__act"><button type="button" class="csp-13__btn" data-connect aria-label="Connect Figma">Connect</button><button type="button" class="csp-13__ghost" aria-label="Manage Figma">Manage</button><button type="button" class="csp-13__ghost csp-13__ghost--bad" data-disconnect aria-label="Disconnect Figma">Disconnect</button></div></article>
      <article class="csp-13__app" data-cat="dev"><div class="csp-13__top"><span class="csp-13__logo" style="--h:250">Li</span><span class="csp-13__status">Connected</span></div><h2>Linear</h2><p>Two-way sync issues, status and assignees.</p><div class="csp-13__act"><button type="button" class="csp-13__btn" data-connect aria-label="Connect Linear">Connect</button><button type="button" class="csp-13__ghost" aria-label="Manage Linear">Manage</button><button type="button" class="csp-13__ghost csp-13__ghost--bad" data-disconnect aria-label="Disconnect Linear">Disconnect</button></div></article>
      <article class="csp-13__app" data-cat="comm"><div class="csp-13__top"><span class="csp-13__logo" style="--h:230">Te</span><span class="csp-13__status">Connected</span></div><h2>Microsoft Teams</h2><p>Share projects and receive notifications in Teams.</p><div class="csp-13__act"><button type="button" class="csp-13__btn" data-connect aria-label="Connect Microsoft Teams">Connect</button><button type="button" class="csp-13__ghost" aria-label="Manage Microsoft Teams">Manage</button><button type="button" class="csp-13__ghost csp-13__ghost--bad" data-disconnect aria-label="Disconnect Microsoft Teams">Disconnect</button></div></article>
      <article class="csp-13__app" data-cat="prod"><div class="csp-13__top"><span class="csp-13__logo" style="--h:60">Za</span><span class="csp-13__status">Connected</span></div><h2>Zapier</h2><p>Automate workflows with 6,000+ apps — no code.</p><div class="csp-13__act"><button type="button" class="csp-13__btn" data-connect aria-label="Connect Zapier">Connect</button><button type="button" class="csp-13__ghost" aria-label="Manage Zapier">Manage</button><button type="button" class="csp-13__ghost csp-13__ghost--bad" data-disconnect aria-label="Disconnect Zapier">Disconnect</button></div></article>
      <article class="csp-13__app" data-cat="dev"><div class="csp-13__top"><span class="csp-13__logo" style="--h:200">Sn</span><span class="csp-13__status">Connected</span></div><h2>Sentry</h2><p>Turn production errors into tracked tasks.</p><div class="csp-13__act"><button type="button" class="csp-13__btn" data-connect aria-label="Connect Sentry">Connect</button><button type="button" class="csp-13__ghost" aria-label="Manage Sentry">Manage</button><button type="button" class="csp-13__ghost csp-13__ghost--bad" data-disconnect aria-label="Disconnect Sentry">Disconnect</button></div></article>
    </div>
    <p class="csp-13__empty">No integrations match. Try another category or search term.</p>
  </div>
  <p class="csp-13__sr" aria-live="polite" data-live></p>
</section>
```
## CSS
```css
.csp-13,
.csp-13 *,
.csp-13 *::before,
.csp-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-13 {
  --bg: oklch(0.975 0.006 300);
  --surface: #fff;
  --ink: oklch(0.22 0.02 290);
  --muted: oklch(0.5 0.02 290);
  --line: oklch(0.91 0.01 290);
  --accent: oklch(0.5 0.2 290);
  --ok: oklch(0.58 0.15 155);
  color-scheme: light;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 22px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--ink);
  width: 100%;
}

.csp-13__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.csp-13__wrap {
  max-width: 1040px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.csp-13__head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}

.csp-13__head h1 {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  font: 700 30px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-13__head p {
  font: 400 14.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
}

.csp-13__count {
  padding: 5px 11px;
  border-radius: 999px;
  font: 650 12px/1 system-ui,sans-serif;
  letter-spacing: 0;
  color: var(--ok);
  background: oklch(0.95 0.04 155);
}

.csp-13__search {
  flex: 0 1 280px;
}

.csp-13__search input {
  width: 100%;
  min-height: 44px;
  padding: 0 14px 0 40px;
  border: 1px solid var(--line);
  border-radius: 12px;
  font: 400 14.5px/1 system-ui,sans-serif;
  color: var(--ink);
  background: var(--surface) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Ccircle cx='9' cy='9' r='5.5' fill='none' stroke='%23889' stroke-width='1.6'/%3E%3Cpath d='m13 13 3.5 3.5' stroke='%23889' stroke-width='1.6' stroke-linecap='round'/%3E%3C/svg%3E") 14px center/18px no-repeat;
}

.csp-13__search input:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.5 0.2 290/.15);
}

.csp-13__tabs {
  border: 0;
  min-width: 0;
  max-width: 100%;
  display: flex;
  gap: 6px;
  overflow-x: auto;
  scrollbar-width: none;
  padding-bottom: 2px;
}

.csp-13__tabs input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.csp-13__tabs label {
  flex: none;
  min-height: 38px;
  display: grid;
  place-items: center;
  padding: 0 15px;
  border-radius: 999px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: var(--muted);
  cursor: pointer;
  transition: all .15s;
}

.csp-13__tabs label:hover {
  color: var(--ink);
  background: oklch(0.95 0.01 290);
}

.csp-13__tabs input:checked+label {
  color: #fff;
  background: var(--ink);
}

.csp-13__tabs input:focus-visible+label {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-13__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(260px,1fr));
  gap: 14px;
}

.csp-13__app {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 20px;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--surface);
  transition: border-color .2s,box-shadow .2s,transform .2s;
  animation: csp13-in .3s ease;
}

.csp-13__app:hover {
  border-color: oklch(0.85 0.02 290);
  box-shadow: 0 16px 36px -24px oklch(0.3 0.08 290/.4);
  transform: translateY(-2px);
}

.csp-13__app.is-on {
  border-color: oklch(0.85 0.06 155);
}

.csp-13__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 6px;
}

.csp-13__logo {
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  border-radius: 13px;
  font: 750 16px/1 system-ui,sans-serif;
  color: #fff;
  background: linear-gradient(140deg,oklch(0.65 0.17 var(--h)),oklch(0.48 0.17 calc(var(--h) + 30)));
  box-shadow: inset 0 1px 0 oklch(1 0 0/.3),0 6px 14px -8px oklch(0.4 0.17 var(--h));
}

.csp-13__status {
  display: none;
  align-items: center;
  gap: 6px;
  font: 600 12px/1 system-ui,sans-serif;
  color: var(--ok);
}

.csp-13__status::before {
  content: "";
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: currentColor;
}

.csp-13__app.is-on .csp-13__status {
  display: inline-flex;
}

.csp-13__app h2 {
  font: 650 16px/1.2 system-ui,sans-serif;
}

.csp-13__app p {
  flex: 1;
  font: 400 13.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.csp-13__act {
  display: flex;
  gap: 8px;
  margin-top: 8px;
}

.csp-13__btn,
.csp-13__ghost {
  min-height: 40px;
  padding: 0 14px;
  border-radius: 10px;
  font: 600 13.5px/1 system-ui,sans-serif;
  cursor: pointer;
  transition: all .15s;
}

.csp-13__btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 0;
  color: #fff;
  background: var(--accent);
}

.csp-13__btn:hover {
  background: oklch(0.45 0.2 290);
}

.csp-13__btn[data-state="busy"] {
  opacity: .75;
  pointer-events: none;
}

.csp-13__btn[data-state="busy"]::before {
  content: "";
  width: 12px;
  height: 12px;
  border: 2px solid #fff;
  border-right-color: transparent;
  border-radius: 50%;
  animation: csp13-spin .7s linear infinite;
}

.csp-13__ghost {
  display: none;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
}

.csp-13__ghost:hover {
  background: var(--bg);
}

.csp-13__ghost--bad:hover {
  color: oklch(0.55 0.2 25);
  border-color: oklch(0.85 0.06 25);
}

.csp-13__app.is-on .csp-13__btn {
  display: none;
}

.csp-13__app.is-on .csp-13__ghost {
  display: inline-block;
}

.csp-13 button:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-13:has(#csp13-on:checked) .csp-13__app:not(.is-on),
.csp-13:has(#csp13-comm:checked) .csp-13__app:not([data-cat~="comm"]),
.csp-13:has(#csp13-dev:checked) .csp-13__app:not([data-cat~="dev"]),
.csp-13:has(#csp13-prod:checked) .csp-13__app:not([data-cat~="prod"]) {
  display: none;
}

.csp-13__empty {
  display: none;
  padding: 40px;
  text-align: center;
  font: 500 14px/1.4 system-ui,sans-serif;
  color: var(--muted);
}

@keyframes csp13-in {
  from {
    opacity: 0;
    translate: 0 6px;
  }
}

@keyframes csp13-spin {
  to {
    rotate: 1turn;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-13 * {
    transition: none!important;
    animation: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-13');
  var q = root.querySelector('[data-q]'), count = root.querySelector('[data-count]');
  var live = root.querySelector('[data-live]'), empty = root.querySelector('.csp-13__empty');
  var apps = root.querySelectorAll('.csp-13__app');

  function refresh() {
    var on = root.querySelectorAll('.csp-13__app.is-on').length;
    count.textContent = on + ' connected';
    var visible = Array.prototype.some.call(apps, function (a) { return a.offsetParent !== null; });
    empty.style.display = visible ? 'none' : 'block';
  }
  q.addEventListener('input', function () {
    var t = q.value.trim().toLowerCase();
    apps.forEach(function (a) { a.hidden = t && a.textContent.toLowerCase().indexOf(t) === -1; });
    refresh();
  });
  root.addEventListener('change', refresh);
  root.addEventListener('click', function (e) {
    var app = e.target.closest('.csp-13__app'); if (!app) return;
    var name = app.querySelector('h2').textContent;
    var c = e.target.closest('[data-connect]');
    if (c) {
      c.dataset.state = 'busy'; c.textContent = 'Connecting…';
      setTimeout(function () {
        c.removeAttribute('data-state'); c.textContent = 'Connect';
        app.classList.add('is-on'); live.textContent = name + ' connected'; refresh();
      }, 1100);
    }
    if (e.target.closest('[data-disconnect]')) { app.classList.remove('is-on'); live.textContent = name + ' disconnected'; refresh(); }
  });
  refresh();
})();
```
