---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/active-sessions-devices/"
title: "Active Sessions and Devices Page"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A security-first sessions page that answers 'where am I signed in?' at a glance: the current device pinned at the top with a live pulse, every other session…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Active Sessions and Devices Page
Source: https://codefronts.com/layouts/css-settings-pages/active-sessions-devices/

A security-first sessions page that answers 'where am I signed in?' at a glance: the current device pinned at the top with a live pulse, every other session listed with device type, browser, OS, approximate location and last activity, an 'unrecognised sign-in' flag with a direct path to secure the account, per-device sign-out with a smooth collapse, and a 'Sign out all other sessions' action with a confirm step and empty state.
## HTML
```html
<section class="csp-11">
  <div class="csp-11__wrap">
    <header class="csp-11__head">
      <h1>Sessions &amp; devices</h1>
      <p>These devices are signed in to your account. Sign out anything you don't recognise.</p>
    </header>

    <article class="csp-11__current">
      <span class="csp-11__ico"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M1 20h22"/></svg></span>
      <div class="csp-11__info"><b>MacBook Pro · Chrome 129</b><small>San Francisco, US · 73.162.xx.xx</small></div>
      <span class="csp-11__live"><i></i>This device</span>
    </article>

    <div class="csp-11__card">
      <div class="csp-11__cardhead">
        <h2>Other sessions <span data-n>4</span></h2>
        <button type="button" class="csp-11__all" data-all>Sign out all other sessions</button>
      </div>
      <ul class="csp-11__list" data-list>
        <li class="csp-11__item"><div class="csp-11__row">
          <span class="csp-11__ico"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="7" y="2" width="10" height="20" rx="2.5"/><path d="M11 18h2"/></svg></span>
          <div class="csp-11__info"><b>iPhone 16 · Safari</b><small>London, UK · 2 hours ago</small></div>
          <button type="button" class="csp-11__out" data-out>Sign out</button></div></li>
        <li class="csp-11__item is-flag"><div class="csp-11__row">
          <span class="csp-11__ico"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg></span>
          <div class="csp-11__info"><b>Windows PC · Firefox 131 <em>Unrecognised</em></b><small>Frankfurt, DE · yesterday at 23:14 · <a href="#">Secure my account</a></small></div>
          <button type="button" class="csp-11__out" data-out>Sign out</button></div></li>
        <li class="csp-11__item"><div class="csp-11__row">
          <span class="csp-11__ico"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="2" width="16" height="20" rx="2.5"/><path d="M11 18h2"/></svg></span>
          <div class="csp-11__info"><b>iPad Air · Northwind app</b><small>Sydney, AU · 3 days ago</small></div>
          <button type="button" class="csp-11__out" data-out>Sign out</button></div></li>
        <li class="csp-11__item"><div class="csp-11__row">
          <span class="csp-11__ico"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M1 20h22"/></svg></span>
          <div class="csp-11__info"><b>ThinkPad · Chrome 128 on Linux</b><small>Toronto, CA · 2 weeks ago</small></div>
          <button type="button" class="csp-11__out" data-out>Sign out</button></div></li>
      </ul>
      <div class="csp-11__empty"><b>You're only signed in here</b><small>Every other session has been signed out.</small></div>
    </div>
    <p class="csp-11__tip">Sessions expire automatically after 30 days of inactivity. Turn on <a href="#">two-factor authentication</a> for extra protection.</p>
  </div>
  <p class="csp-11__sr" aria-live="polite" data-live></p>
</section>
```
## CSS
```css
.csp-11,
.csp-11 *,
.csp-11 *::before,
.csp-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-11 {
  --bg: oklch(0.15 0.01 240);
  --surface: oklch(0.195 0.012 240);
  --raised: oklch(0.235 0.014 240);
  --text: oklch(0.95 0.006 240);
  --muted: oklch(0.7 0.015 240);
  --line: oklch(0.29 0.014 240);
  --accent: oklch(0.78 0.13 220);
  --ok: oklch(0.78 0.16 155);
  --warn: oklch(0.8 0.15 70);
  --bad: oklch(0.68 0.19 25);
  color-scheme: dark;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 20px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: radial-gradient(80% 50% at 50% 0%,oklch(0.26 0.05 230/.6),transparent),var(--bg);
  color: var(--text);
  width: 100%;
}

.csp-11__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.csp-11__wrap {
  max-width: 680px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.csp-11__head h1 {
  font: 700 28px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-11__head p {
  font: 400 14.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
  text-wrap: pretty;
}

.csp-11__current,
.csp-11__row {
  display: flex;
  align-items: center;
  gap: 14px;
}

.csp-11__current {
  padding: 18px;
  border-radius: 18px;
  border: 1px solid oklch(0.78 0.16 155/.35);
  background: linear-gradient(135deg,oklch(0.78 0.16 155/.1),transparent 60%),var(--surface);
}

.csp-11__ico {
  flex: none;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: var(--raised);
  color: var(--accent);
}

.csp-11__ico svg {
  width: 22px;
  height: 22px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.6;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.csp-11__info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 0;
}

.csp-11__info b {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  font: 600 14.5px/1.25 system-ui,sans-serif;
}

.csp-11__info small {
  font: 400 13px/1.4 system-ui,sans-serif;
  color: var(--muted);
}

.csp-11__info a {
  color: var(--warn);
  font-weight: 600;
}

.csp-11__info em {
  font: 650 10.5px/1 system-ui,sans-serif;
  font-style: normal;
  padding: 4px 7px;
  border-radius: 999px;
  color: var(--warn);
  background: oklch(0.8 0.15 70/.14);
}

.csp-11__live {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 11px;
  border-radius: 999px;
  font: 600 12px/1 system-ui,sans-serif;
  color: var(--ok);
  background: oklch(0.78 0.16 155/.12);
  white-space: nowrap;
}

.csp-11__live i {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--ok);
  animation: csp11-pulse 2s infinite;
}

.csp-11__card {
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--surface);
  overflow: hidden;
}

.csp-11__cardhead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
  padding: 16px 18px;
  border-bottom: 1px solid var(--line);
}

.csp-11__cardhead h2 {
  display: flex;
  align-items: center;
  gap: 8px;
  font: 650 15px/1 system-ui,sans-serif;
}

.csp-11__cardhead h2 span {
  min-width: 22px;
  padding: 4px 7px;
  border-radius: 999px;
  font: 650 11.5px/1 system-ui,sans-serif;
  text-align: center;
  color: var(--muted);
  background: var(--raised);
}

.csp-11__all {
  min-height: 38px;
  padding: 0 14px;
  border: 1px solid oklch(0.68 0.19 25/.4);
  border-radius: 10px;
  background: transparent;
  font: 600 13px/1 system-ui,sans-serif;
  color: var(--bad);
  cursor: pointer;
  transition: all .15s;
}

.csp-11__all:hover,
.csp-11__all.is-armed {
  color: #fff;
  background: oklch(0.55 0.2 25);
  border-color: transparent;
}

.csp-11__all:disabled {
  opacity: .35;
  pointer-events: none;
}

.csp-11__list {
  list-style: none;
}

.csp-11__item {
  display: grid;
  grid-template-rows: 1fr;
  transition: grid-template-rows .35s cubic-bezier(.3,.7,.3,1),opacity .3s,translate .35s;
}

.csp-11__item.is-out {
  grid-template-rows: 0fr;
  opacity: 0;
  translate: 24px 0;
}

.csp-11__row {
  overflow: hidden;
  min-height: 0;
  padding: 14px 18px;
  border-bottom: 1px solid var(--line);
}

.csp-11__item:last-child .csp-11__row {
  border-bottom: 0;
}

.csp-11__item.is-flag .csp-11__ico {
  color: var(--warn);
  background: oklch(0.8 0.15 70/.12);
}

.csp-11__out {
  flex: none;
  min-height: 38px;
  padding: 0 14px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--raised);
  font: 600 13px/1 system-ui,sans-serif;
  color: var(--text);
  cursor: pointer;
  transition: all .15s;
}

.csp-11__out:hover {
  border-color: oklch(0.68 0.19 25/.5);
  color: var(--bad);
}

.csp-11 button:focus-visible,
.csp-11 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-11__empty {
  display: none;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 34px 18px;
  text-align: center;
}

.csp-11__empty::before {
  content: "";
  width: 44px;
  height: 44px;
  margin-bottom: 6px;
  border-radius: 50%;
  background: oklch(0.78 0.16 155/.14) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 3 5 6v5c0 4.5 3 7.8 7 9 4-1.2 7-4.5 7-9V6z' fill='none' stroke='%237fe0ad' stroke-width='1.7' stroke-linejoin='round'/%3E%3Cpath d='m9 12 2 2 4-4' fill='none' stroke='%237fe0ad' stroke-width='1.7' stroke-linecap='round'/%3E%3C/svg%3E") center/24px no-repeat;
}

.csp-11__empty b {
  font: 600 15px/1.2 system-ui,sans-serif;
}

.csp-11__empty small {
  font: 400 13px/1.4 system-ui,sans-serif;
  color: var(--muted);
}

.csp-11__list:not(:has(li))+.csp-11__empty {
  display: flex;
}

.csp-11__tip {
  font: 400 13px/1.5 system-ui,sans-serif;
  color: var(--muted);
}

.csp-11__tip a {
  color: var(--accent);
  font-weight: 600;
}

@keyframes csp11-pulse {
  0% {
    box-shadow: 0 0 0 0 oklch(0.78 0.16 155/.6);
  }

  70% {
    box-shadow: 0 0 0 9px oklch(0.78 0.16 155/0);
  }

  100% {
    box-shadow: 0 0 0 0 oklch(0.78 0.16 155/0);
  }
}

@media (max-width: 520px) {
  .csp-11__current {
    flex-wrap: wrap;
  }

  .csp-11__cardhead {
    flex-direction: column;
    align-items: stretch;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-11 * {
    animation: none!important;
    transition: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-11');
  var list = root.querySelector('[data-list]'), n = root.querySelector('[data-n]');
  var all = root.querySelector('[data-all]'), live = root.querySelector('[data-live]');
  var reduce = matchMedia('(prefers-reduced-motion:reduce)').matches;

  function count() {
    var c = list.querySelectorAll('li:not(.is-out)').length;
    n.textContent = c; all.disabled = c === 0;
  }
  function out(li, delay) {
    li.style.transitionDelay = (delay || 0) + 'ms';
    li.classList.add('is-out');
    var done = function () { li.remove(); count(); };
    if (reduce) done(); else setTimeout(done, 380 + (delay || 0));
    count();
  }
  list.addEventListener('click', function (e) {
    var b = e.target.closest('[data-out]'); if (!b) return;
    var li = b.closest('li');
    live.textContent = li.querySelector('b').firstChild.textContent.trim() + ' signed out';
    out(li);
  });
  all.addEventListener('click', function () {
    if (!all.classList.contains('is-armed')) {
      all.classList.add('is-armed'); all.textContent = 'Click again to confirm';
      clearTimeout(all._t); all._t = setTimeout(function () { all.classList.remove('is-armed'); all.textContent = 'Sign out all other sessions'; }, 4000);
      return;
    }
    clearTimeout(all._t);
    all.classList.remove('is-armed'); all.textContent = 'Sign out all other sessions';
    list.querySelectorAll('li:not(.is-out)').forEach(function (li, i) { out(li, i * 90); });
    live.textContent = 'All other sessions signed out';
  });
  count();
})();
```
