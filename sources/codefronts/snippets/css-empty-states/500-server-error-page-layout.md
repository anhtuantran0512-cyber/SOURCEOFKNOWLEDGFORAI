---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/500-server-error-page-layout/"
title: "500 Server Error Page Layout"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "A 500 page that behaves like an incident view: a gradient-clipped error code, a plain-language explanation of what did and did not happen to the request, a…"
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 500 Server Error Page Layout
Source: https://codefronts.com/snippets/css-empty-states/500-server-error-page-layout/

A 500 page that behaves like an incident view: a gradient-clipped error code, a plain-language explanation of what did and did not happen to the request, a reference the user can quote, and a recovery log that appends real lines as you retry. The replay succeeds, the button becomes a completed state and the headline rewrites itself .
## HTML
```html
<div class="est-08">
  <header class="est-08__bar">
    <span class="est-08__brand">Tideline</span>
    <span class="est-08__env">production &middot; eu-west-1</span>
    <a class="est-08__statuslink" href="#est-08">Status page</a>
  </header>

  <main class="est-08__main">
    <section class="est-08__col">
      <p class="est-08__code" aria-hidden="true">500</p>
      <h1 class="est-08__h1" id="est-08-h">The request did not make it back</h1>
      <p class="est-08__p" id="est-08-p">Our edge accepted it, the upstream service did not answer in time. Nothing you sent has been lost &mdash; retry when you are ready.</p>

      <div class="est-08__acts">
        <button class="est-08__pri" type="button" id="est-08-retry">Retry request</button>
        <a class="est-08__ghost" href="#est-08">Copy incident reference</a>
      </div>

      <dl class="est-08__ref">
        <div><dt>Reference</dt><dd>req_9f2c41ba8e</dd></div>
        <div><dt>Region</dt><dd>eu-west-1b</dd></div>
        <div><dt>Time</dt><dd id="est-08-time">14:02:11 UTC</dd></div>
      </dl>
    </section>

    <aside class="est-08__console" aria-label="Recovery log">
      <div class="est-08__chead">
        <span class="est-08__cdot" aria-hidden="true"></span>
        <span class="est-08__ctitle">recovery log</span>
        <span class="est-08__cstate" id="est-08-state">idle</span>
      </div>
      <ol class="est-08__lines" id="est-08-lines">
        <li><span>14:02:09</span>POST /v2/ledger/settle &rarr; upstream timeout</li>
        <li><span>14:02:10</span>circuit breaker opened for ledger-api</li>
        <li><span>14:02:11</span>request queued for replay</li>
      </ol>
      <div class="est-08__prog" id="est-08-prog" hidden><span></span></div>
    </aside>
  </main>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-08 {
  --bg: #08080a;
  --panel: #101012;
  --panel-2: #17171b;
  --line: #212127;
  --line-2: #2d2d35;
  --text: #f2f2f4;
  --muted: #9c9ca6;
  --faint: #6a6a75;
  --hot: #f0803c;
  --ok: #66d9a0;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
  box-sizing: border-box;
  background: var(--bg);
  color: var(--text);
  color-scheme: dark;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-08 *,
.est-08 *::before,
.est-08 *::after {
  box-sizing: border-box;
}

.est-08 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-08 {
    --bg: oklch(0.14 0.004 285);
    --panel: oklch(0.18 0.006 285);
    --panel-2: oklch(0.215 0.008 285);
    --line: oklch(0.265 0.008 285);
    --line-2: oklch(0.32 0.01 285);
    --text: oklch(0.965 0.003 285);
    --muted: oklch(0.735 0.012 285);
    --faint: oklch(0.575 0.013 285);
    --hot: oklch(0.72 0.15 52);
    --ok: oklch(0.83 0.13 158);
  }
}

.est-08__bar {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem 1.25rem;
  align-items: center;
  padding: .85rem clamp(1rem,3vw,2.5rem);
  border-block-end: 1px solid var(--line);
  background: color-mix(in oklab, var(--panel) 70%, transparent);
  backdrop-filter: blur(8px);
}

.est-08__brand {
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.est-08__env {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .7rem;
  letter-spacing: .04em;
  color: var(--faint);
  padding: .2rem .45rem;
  border: 1px solid var(--line);
  border-radius: 6px;
}

.est-08__statuslink {
  margin-inline-start: auto;
  font-size: .83rem;
  color: var(--muted);
  text-decoration: none;
  border-block-end: 1px solid var(--line-2);
  transition: color .16s, border-color .16s;
}

.est-08__statuslink:hover {
  color: var(--text);
  border-color: var(--hot);
}

.est-08__main {
  min-inline-size: 0;
  align-content: center;
  padding: clamp(1.5rem,6vw,4.5rem) clamp(1rem,4vw,3rem);
  display: grid;
  gap: clamp(1.5rem,4vw,3.5rem);
  grid-template-columns: repeat(auto-fit,minmax(min(20rem,100%),1fr));
  align-items: center;
  background: radial-gradient(70% 55% at 18% 20%, color-mix(in oklab, var(--hot) 9%, transparent), transparent 65%), var(--bg);
}

.est-08__col {
  min-inline-size: 0;
  display: grid;
  gap: .7rem;
  animation: est-08-in .55s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-08-in {
  from {
    opacity: 0;
    translate: 0 10px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-08__code {
  margin: 0;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: clamp(3.5rem,11vw,6.5rem);
  font-weight: 500;
  line-height: .85;
  letter-spacing: -.06em;
  color: transparent;
  background: linear-gradient(180deg, color-mix(in oklab, var(--hot) 85%, var(--text)) 15%, color-mix(in oklab, var(--hot) 25%, transparent));
  -webkit-background-clip: text;
  background-clip: text;
}

.est-08__h1 {
  margin: .2rem 0 0;
  font-size: clamp(1.35rem,3.2vw,2rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.12;
  text-wrap: balance;
}

.est-08__p {
  margin: 0;
  max-inline-size: 46ch;
  font-size: .95rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.est-08__acts {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  margin-block-start: .85rem;
}

.est-08__pri {
  min-block-size: 2.85rem;
  padding: .7rem 1.15rem;
  font: inherit;
  font-size: .88rem;
  font-weight: 500;
  cursor: pointer;
  color: #160a03;
  background: var(--hot);
  border: 1px solid transparent;
  border-radius: 11px;
  box-shadow: 0 10px 26px -18px var(--hot);
  transition: translate .16s, background .16s;
}

.est-08__pri:hover {
  translate: 0 -1px;
  background: color-mix(in oklab, var(--hot) 88%, #fff);
}

.est-08__pri[data-busy] {
  color: var(--muted);
  background: var(--panel-2);
  border-color: var(--line-2);
  box-shadow: none;
  cursor: progress;
}

.est-08__pri[data-done] {
  color: #04170e;
  background: var(--ok);
  box-shadow: 0 10px 26px -18px var(--ok);
}

.est-08__ghost {
  min-block-size: 2.85rem;
  display: inline-flex;
  align-items: center;
  padding: .7rem 1.05rem;
  font-size: .88rem;
  font-weight: 500;
  color: var(--text);
  background: var(--panel-2);
  border: 1px solid var(--line-2);
  border-radius: 11px;
  text-decoration: none;
  transition: background .16s;
}

.est-08__ghost:hover {
  background: var(--line);
}

.est-08__ref {
  margin: 1.35rem 0 0;
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.est-08__ref div {
  display: grid;
  gap: .25rem;
}

.est-08__ref dt {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .65rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--faint);
}

.est-08__ref dd {
  margin: 0;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .8rem;
  color: var(--text);
}

.est-08__console {
  min-inline-size: 0;
  display: grid;
  gap: 0;
  align-content: start;
  overflow: hidden;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 16px;
  box-shadow: 0 40px 80px -60px #000;
  animation: est-08-in .55s .1s cubic-bezier(.2,.7,.3,1) both;
}

.est-08__chead {
  display: flex;
  align-items: center;
  gap: .55rem;
  padding: .7rem .9rem;
  border-block-end: 1px solid var(--line);
  background: var(--panel-2);
}

.est-08__cdot {
  inline-size: .5rem;
  block-size: .5rem;
  border-radius: 50%;
  background: var(--hot);
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--hot) 18%, transparent);
}

.est-08__ctitle {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .72rem;
  letter-spacing: .06em;
  color: var(--muted);
}

.est-08__cstate {
  margin-inline-start: auto;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .68rem;
  color: var(--faint);
  padding: .15rem .4rem;
  border: 1px solid var(--line-2);
  border-radius: 5px;
}

.est-08__lines {
  margin: 0;
  padding: .7rem .9rem 1rem;
  list-style: none;
  display: grid;
  gap: .45rem;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .76rem;
  line-height: 1.45;
  color: var(--muted);
}

.est-08__lines li {
  display: grid;
  grid-template-columns: 4.5rem minmax(0,1fr);
  gap: .6rem;
  animation: est-08-line .35s ease both;
}

.est-08__lines li span {
  color: var(--faint);
}

.est-08__lines li[data-ok] {
  color: var(--ok);
}

@keyframes est-08-line {
  from {
    opacity: 0;
    translate: -4px 0;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-08__prog {
  block-size: 2px;
  background: var(--line);
  overflow: hidden;
}

.est-08__prog span {
  display: block;
  block-size: 100%;
  inline-size: 35%;
  background: var(--hot);
  animation: est-08-slide 1.1s ease-in-out infinite;
}

@keyframes est-08-slide {
  0% {
    translate: -100% 0;
  }

  100% {
    translate: 320% 0;
  }
}

.est-08__pri:focus-visible,
.est-08__ghost:focus-visible,
.est-08__statuslink:focus-visible {
  outline: 2px solid var(--hot);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .est-08 *,
    .est-08 *::before,
    .est-08 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-08__console,
    .est-08__pri,
    .est-08__ghost {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-08'); if(!root) return;
  var retry = root.querySelector('#est-08-retry'), lines = root.querySelector('#est-08-lines'),
      prog = root.querySelector('#est-08-prog'), state = root.querySelector('#est-08-state'),
      h = root.querySelector('#est-08-h'), p = root.querySelector('#est-08-p'), time = root.querySelector('#est-08-time');
  function stamp(){
    var d = new Date();
    return [d.getUTCHours(), d.getUTCMinutes(), d.getUTCSeconds()].map(function(n){ return (n < 10 ? '0' : '') + n; }).join(':');
  }
  function line(text, ok){
    var li = document.createElement('li');
    li.innerHTML = '<span>' + stamp() + '</span>' + text;
    if(ok) li.setAttribute('data-ok','');
    lines.appendChild(li);
  }
  time.textContent = stamp() + ' UTC';
  retry.addEventListener('click', function(){
    if(retry.hasAttribute('data-busy') || retry.hasAttribute('data-done')) return;
    retry.setAttribute('data-busy',''); retry.textContent = 'Retrying';
    prog.hidden = false; state.textContent = 'replaying';
    line('replaying req_9f2c41ba8e');
    setTimeout(function(){ line('ledger-api handshake ok'); }, 700);
    setTimeout(function(){
      line('settled &mdash; 200 OK', true);
      prog.hidden = true; state.textContent = 'recovered';
      retry.removeAttribute('data-busy'); retry.setAttribute('data-done',''); retry.textContent = 'Request completed';
      h.textContent = 'It went through this time';
      p.textContent = 'The replay settled against the ledger. You can carry on where you left off.';
    }, 1600);
  });
})();
```
