---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/webhooks-settings/"
title: "Webhooks Settings Page"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A complete webhook endpoint manager: an endpoint list with health indicators and success-rate bars, a detail view with the endpoint URL, an enable switch,…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Webhooks Settings Page
Source: https://codefronts.com/layouts/css-settings-pages/webhooks-settings/

A complete webhook endpoint manager: an endpoint list with health indicators and success-rate bars, a detail view with the endpoint URL, an enable switch, subscribed-event chips, a masked signing secret with reveal / copy / roll, and a recent deliveries log with colour-coded HTTP status, latency and one-click retry. 'Send test event' fires a simulated delivery that slides into the log in real time.
## HTML
```html
<section class="csp-17">
  <div class="csp-17__wrap">
    <header class="csp-17__head">
      <div><h1>Webhooks</h1><p>Receive real-time HTTP POST notifications when events happen in your workspace.</p></div>
      <a class="csp-17__ghost" href="#">+ Add endpoint</a>
    </header>
    <div class="csp-17__grid">
      <fieldset class="csp-17__eps">
        <legend class="csp-17__sr">Endpoints</legend>
        <label class="csp-17__ep" data-url="https://api.northwind.co/hooks/billing" data-rate="99.2%"><input type="radio" name="csp17-ep" checked><span class="csp-17__eptext"><b>Billing service</b><small>api.northwind.co/hooks/billing</small></span><span class="csp-17__spark" aria-hidden="true"><i style="--v:.8"></i><i style="--v:.95"></i><i style="--v:.7"></i><i style="--v:.9"></i><i style="--v:.4" data-fail></i><i style="--v:.85"></i><i style="--v:1"></i><i style="--v:.75"></i></span></label>
        <label class="csp-17__ep" data-url="https://hooks.zapier.com/catch/18833/abc" data-rate="100%"><input type="radio" name="csp17-ep"><span class="csp-17__eptext"><b>Zapier automation</b><small>hooks.zapier.com/catch/…</small></span><span class="csp-17__spark" aria-hidden="true"><i style="--v:.5"></i><i style="--v:.6"></i><i style="--v:.55"></i><i style="--v:.7"></i><i style="--v:.65"></i><i style="--v:.8"></i><i style="--v:.6"></i><i style="--v:.7"></i></span></label>
        <label class="csp-17__ep is-failing" data-url="https://legacy.example.com/webhook" data-rate="61.0%"><input type="radio" name="csp17-ep"><span class="csp-17__eptext"><b>Legacy CRM</b><small>legacy.example.com/webhook</small></span><span class="csp-17__spark" aria-hidden="true"><i style="--v:.6" data-fail></i><i style="--v:.3"></i><i style="--v:.7" data-fail></i><i style="--v:.5" data-fail></i><i style="--v:.4"></i><i style="--v:.8" data-fail></i><i style="--v:.6" data-fail></i><i style="--v:.5"></i></span></label>
      </fieldset>

      <div class="csp-17__detail">
        <div class="csp-17__urlrow">
          <code data-url>https://api.northwind.co/hooks/billing</code>
          <label class="csp-17__enable"><input type="checkbox" id="csp17-on" checked role="switch"> Enabled</label>
        </div>
        <p class="csp-17__paused">This endpoint is disabled. Events are not being delivered.</p>
        <div class="csp-17__stats"><div><small>Success rate (24h)</small><b data-rate>99.2%</b></div><div><small>Avg. latency</small><b>184 ms</b></div><div><small>Events</small><b>4 subscribed</b></div></div>

        <div class="csp-17__block">
          <h2>Events</h2>
          <div class="csp-17__events"><span>invoice.paid</span><span>invoice.payment_failed</span><span>subscription.updated</span><span>customer.deleted</span></div>
        </div>

        <div class="csp-17__block">
          <h2>Signing secret</h2>
          <div class="csp-17__secret"><code data-secret data-real="whsec_example_placeholder">whsec_••••••••••••••••••••</code><button type="button" class="csp-17__sbtn" data-reveal aria-pressed="false">Reveal</button><button type="button" class="csp-17__sbtn" data-copy>Copy</button><button type="button" class="csp-17__sbtn" data-roll>Roll</button></div>
          <small class="csp-17__hint">Verify the <code>Northwind-Signature</code> header with HMAC-SHA256 to confirm requests come from us.</small>
        </div>

        <div class="csp-17__block csp-17__deliv">
          <div class="csp-17__dhead"><h2>Recent deliveries</h2><button type="button" class="csp-17__btn" data-test>Send test event</button></div>
          <ul class="csp-17__log" data-log>
            <li data-code="200"><span class="csp-17__code">200</span><span class="csp-17__evn">invoice.paid</span><span class="csp-17__ms">142 ms</span><time>2 min ago</time><span></span></li>
            <li data-code="200"><span class="csp-17__code">200</span><span class="csp-17__evn">subscription.updated</span><span class="csp-17__ms">208 ms</span><time>18 min ago</time><span></span></li>
            <li data-code="500"><span class="csp-17__code">500</span><span class="csp-17__evn">invoice.payment_failed</span><span class="csp-17__ms">3,012 ms</span><time>1 hour ago</time><button type="button" class="csp-17__retry" data-retry>Retry</button></li>
            <li data-code="200"><span class="csp-17__code">200</span><span class="csp-17__evn">invoice.paid</span><span class="csp-17__ms">167 ms</span><time>3 hours ago</time><span></span></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <p class="csp-17__sr" aria-live="polite" data-live></p>
</section>
```
## CSS
```css
.csp-17,
.csp-17 *,
.csp-17 *::before,
.csp-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-17 {
  --bg: oklch(0.975 0.005 200);
  --surface: #fff;
  --ink: oklch(0.22 0.02 220);
  --muted: oklch(0.5 0.02 220);
  --line: oklch(0.91 0.008 220);
  --accent: oklch(0.52 0.13 200);
  --ok: oklch(0.6 0.15 155);
  --bad: oklch(0.6 0.2 25);
  --warn: oklch(0.7 0.15 70);
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

.csp-17__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.csp-17__wrap {
  max-width: 1040px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.csp-17__head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}

.csp-17__head h1 {
  font: 700 30px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-17__head p {
  font: 400 14.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
}

.csp-17__ghost {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 16px;
  border: 1px solid var(--line);
  border-radius: 11px;
  background: var(--surface);
  font: 600 14px/1 system-ui,sans-serif;
  color: var(--ink);
  text-decoration: none;
}

.csp-17__grid {
  display: grid;
  grid-template-columns: 300px minmax(0,1fr);
  gap: 18px;
  align-items: start;
}

.csp-17__eps {
  border: 0;
  min-width: 0;
  max-width: 100%;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.csp-17__ep {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 14px 16px;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  cursor: pointer;
  transition: border-color .15s,box-shadow .15s;
}

.csp-17__ep:hover {
  border-color: oklch(0.84 0.02 220);
}

.csp-17__ep input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.csp-17__ep:has(input:checked) {
  border-color: var(--accent);
  box-shadow: 0 0 0 1px var(--accent);
}

.csp-17__ep:has(input:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-17__eptext {
  display: flex;
  flex-direction: column;
  gap: 3px;
  min-width: 0;
}

.csp-17__eptext b {
  display: flex;
  align-items: center;
  gap: 8px;
  font: 600 14px/1.2 system-ui,sans-serif;
}

.csp-17__eptext b::before {
  content: "";
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--ok);
}

.csp-17__ep.is-failing .csp-17__eptext b::before {
  background: var(--bad);
}

.csp-17__eptext small {
  font: 400 12px/1.3 ui-monospace,Menlo,monospace;
  color: var(--muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.csp-17__spark {
  display: flex;
  align-items: flex-end;
  gap: 3px;
  height: 22px;
}

.csp-17__spark i {
  flex: 1;
  height: calc(var(--v) * 100%);
  border-radius: 2px;
  background: oklch(0.6 0.15 155/.55);
}

.csp-17__spark i[data-fail] {
  background: var(--bad);
}

.csp-17__detail {
  display: flex;
  flex-direction: column;
  gap: 0;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--surface);
  overflow: hidden;
}

.csp-17__urlrow {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  padding: 18px 20px;
  border-bottom: 1px solid var(--line);
}

.csp-17__urlrow code {
  flex: 1;
  min-width: 0;
  font: 600 13.5px/1.3 ui-monospace,Menlo,monospace;
  word-break: break-all;
}

.csp-17__urlrow code::before {
  content: "POST";
  margin-right: 10px;
  padding: 3px 7px;
  border-radius: 5px;
  font-size: 11px;
  color: var(--accent);
  background: oklch(0.95 0.03 200);
}

.csp-17__enable {
  display: flex;
  align-items: center;
  gap: 10px;
  font: 600 13.5px/1 system-ui,sans-serif;
  cursor: pointer;
}

.csp-17__enable input {
  appearance: none;
  position: relative;
  width: 40px;
  height: 24px;
  border-radius: 999px;
  background: oklch(0.88 0.01 220);
  cursor: pointer;
  transition: background .2s;
}

.csp-17__enable input::before {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 3px oklch(0 0 0/.25);
  transition: translate .2s;
}

.csp-17__enable input:checked {
  background: var(--ok);
}

.csp-17__enable input:checked::before {
  translate: 16px 0;
}

.csp-17__enable input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.csp-17__paused {
  display: none;
  padding: 12px 20px;
  font: 500 13.5px/1.4 system-ui,sans-serif;
  color: oklch(0.45 0.1 65);
  background: oklch(0.96 0.05 85);
  border-bottom: 1px solid var(--line);
}

.csp-17:has(#csp17-on:not(:checked)) .csp-17__paused {
  display: block;
}

.csp-17:has(#csp17-on:not(:checked)) .csp-17__deliv,
.csp-17:has(#csp17-on:not(:checked)) .csp-17__stats {
  opacity: .45;
  filter: grayscale(1);
  pointer-events: none;
}

.csp-17__stats {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  border-bottom: 1px solid var(--line);
}

.csp-17__stats div {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 16px 20px;
}

.csp-17__stats div+div {
  border-left: 1px solid var(--line);
}

.csp-17__stats small {
  font: 500 12px/1 system-ui,sans-serif;
  color: var(--muted);
}

.csp-17__stats b {
  font: 700 20px/1 system-ui,sans-serif;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
}

.csp-17__block {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 18px 20px;
  border-bottom: 1px solid var(--line);
}

.csp-17__block:last-child {
  border-bottom: 0;
}

.csp-17__block h2 {
  font: 650 14px/1 system-ui,sans-serif;
}

.csp-17__events {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.csp-17__events span {
  padding: 6px 10px;
  border-radius: 8px;
  font: 500 12.5px/1 ui-monospace,Menlo,monospace;
  background: oklch(0.96 0.008 220);
  border: 1px solid var(--line);
}

.csp-17__secret {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.csp-17__secret code {
  flex: 1 1 220px;
  min-width: 0;
  display: flex;
  align-items: center;
  min-height: 40px;
  padding: 0 12px;
  border-radius: 9px;
  font: 500 13px/1 ui-monospace,Menlo,monospace;
  font-variant-ligatures: none;
  background: var(--bg);
  border: 1px solid var(--line);
  overflow: hidden;
  white-space: nowrap;
}

.csp-17__sbtn {
  min-height: 40px;
  padding: 0 12px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: var(--surface);
  font: 600 12.5px/1 system-ui,sans-serif;
  color: var(--ink);
  cursor: pointer;
}

.csp-17__sbtn:hover {
  background: var(--bg);
}

.csp-17__hint {
  font: 400 12.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
}

.csp-17__hint code {
  font: 600 12px/1 ui-monospace,Menlo,monospace;
  color: var(--ink);
}

.csp-17__dhead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.csp-17__btn {
  min-height: 40px;
  padding: 0 14px;
  border: 0;
  border-radius: 10px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: #fff;
  background: var(--accent);
  cursor: pointer;
}

.csp-17__btn:disabled {
  opacity: .5;
}

.csp-17 button:focus-visible,
.csp-17 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-17__log {
  list-style: none;
  display: flex;
  flex-direction: column;
}

.csp-17__log li {
  --tone: var(--ok);
  display: grid;
  grid-template-columns: 56px minmax(0,1fr) 80px 90px 64px;
  align-items: center;
  gap: 12px;
  min-height: 46px;
  border-top: 1px solid var(--line);
  font: 400 13px/1.2 system-ui,sans-serif;
  animation: csp17-in .4s cubic-bezier(.2,.8,.2,1);
}

.csp-17__log li:first-child {
  border-top: 0;
}

.csp-17__log li[data-code^="4"],
.csp-17__log li[data-code^="5"] {
  --tone: var(--bad);
}

.csp-17__log li[data-code="…"] {
  --tone: var(--warn);
}

.csp-17__code {
  justify-self: start;
  padding: 4px 8px;
  border-radius: 6px;
  font: 700 12px/1 ui-monospace,Menlo,monospace;
  color: var(--tone);
  background: color-mix(in oklab,var(--tone) 12%,transparent);
}

.csp-17__evn {
  font: 500 12.5px/1.3 ui-monospace,Menlo,monospace;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.csp-17__ms,
.csp-17__log time {
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  text-align: right;
}

.csp-17__retry {
  justify-self: end;
  min-height: 32px;
  padding: 0 10px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--surface);
  font: 600 12px/1 system-ui,sans-serif;
  color: var(--ink);
  cursor: pointer;
}

@keyframes csp17-in {
  from {
    opacity: 0;
    translate: 0 -8px;
  }
}

@container (max-width: 800px) {
  .csp-17__grid {
    grid-template-columns: minmax(0,1fr);
  }

  .csp-17__eps {
    flex-direction: row;
    overflow-x: auto;
  }

  .csp-17__ep {
    flex: 0 0 240px;
  }
}

@container (max-width: 560px) {
  .csp-17__log li {
    grid-template-columns: 52px minmax(0,1fr) 60px;
  }

  .csp-17__ms,
    .csp-17__log time {
    display: none;
  }

  .csp-17__stats {
    grid-template-columns: 1fr;
  }

  .csp-17__stats div+div {
    border-left: 0;
    border-top: 1px solid var(--line);
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-17 * {
    transition: none!important;
    animation: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-17');
  var log = root.querySelector('[data-log]'), live = root.querySelector('[data-live]');
  var secret = root.querySelector('[data-secret]'), reveal = root.querySelector('[data-reveal]');
  var mask = 'whsec_••••••••••••••••••••';

  root.querySelectorAll('.csp-17__ep input').forEach(function (r) {
    r.addEventListener('change', function () {
      var ep = r.closest('.csp-17__ep');
      root.querySelector('code[data-url]').textContent = ep.dataset.url;
      root.querySelector('[data-rate]').textContent = ep.dataset.rate;
    });
  });
  reveal.addEventListener('click', function () {
    var on = reveal.getAttribute('aria-pressed') !== 'true';
    reveal.setAttribute('aria-pressed', on); reveal.textContent = on ? 'Hide' : 'Reveal';
    secret.textContent = on ? secret.dataset.real : mask;
  });
  root.querySelector('[data-copy]').addEventListener('click', function (e) {
    var b = e.currentTarget;
    if (navigator.clipboard) navigator.clipboard.writeText(secret.dataset.real).catch(function () {});
    b.textContent = 'Copied'; live.textContent = 'Signing secret copied';
    setTimeout(function () { b.textContent = 'Copy'; }, 1500);
  });
  root.querySelector('[data-roll]').addEventListener('click', function (e) {
    var b = e.currentTarget;
    if (b.dataset.armed !== '1') { b.dataset.armed = '1'; b.textContent = 'Confirm roll'; setTimeout(function () { b.dataset.armed = ''; b.textContent = 'Roll'; }, 3500); return; }
    var a = new Uint8Array(20), c = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789', s = '';
    crypto.getRandomValues(a); a.forEach(function (n) { s += c[n % c.length]; });
    secret.dataset.real = 'whsec_' + s;
    if (reveal.getAttribute('aria-pressed') === 'true') secret.textContent = secret.dataset.real;
    b.dataset.armed = ''; b.textContent = 'Rolled ✓'; live.textContent = 'New signing secret generated. The old secret stays valid for 24 hours.';
    setTimeout(function () { b.textContent = 'Roll'; }, 1800);
  });

  function deliver(evn, li) {
    if (!li) {
      li = document.createElement('li');
      li.innerHTML = '<span class="csp-17__code"></span><span class="csp-17__evn"></span><span class="csp-17__ms">—</span><time>just now</time><span></span>';
      li.querySelector('.csp-17__evn').textContent = evn;
      log.prepend(li);
    }
    li.dataset.code = '…'; li.querySelector('.csp-17__code').textContent = '…';
    setTimeout(function () {
      li.dataset.code = '200'; li.querySelector('.csp-17__code').textContent = '200';
      li.querySelector('.csp-17__ms').textContent = (90 + Math.round(Math.random() * 160)) + ' ms';
      li.querySelector('time').textContent = 'just now';
      var last = li.lastElementChild; if (last.tagName === 'BUTTON') last.replaceWith(document.createElement('span'));
      live.textContent = evn + ' delivered, 200 OK';
    }, 900);
  }
  var test = root.querySelector('[data-test]');
  test.addEventListener('click', function () {
    test.disabled = true; deliver('test.ping'); setTimeout(function () { test.disabled = false; }, 1000);
  });
  log.addEventListener('click', function (e) {
    var r = e.target.closest('[data-retry]'); if (!r) return;
    var li = r.closest('li'); r.disabled = true; r.textContent = '…';
    deliver(li.querySelector('.csp-17__evn').textContent, li);
  });
})();
```
