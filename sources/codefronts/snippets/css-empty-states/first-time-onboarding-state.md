---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/first-time-onboarding-state/"
title: "First-Time Onboarding State"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "First run for a team workspace, where the empty state is the onboarding: three real setup steps, a progress ring in the sidebar that tracks them, and a…"
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: First-Time Onboarding State
Source: https://codefronts.com/snippets/css-empty-states/first-time-onboarding-state/

First run for a team workspace, where the empty state is the onboarding: three real setup steps, a progress ring in the sidebar that tracks them, and a template rail for people who would rather copy than configure. Ticking a step rewrites the heading and the body copy, so the surface earns its place instead of repeating itself .
## HTML
```html
<div class="est-02">
  <div class="est-02__shell">
    <aside class="est-02__side">
      <button class="est-02__ws" type="button">
        <span class="est-02__wsmark" aria-hidden="true">NL</span>
        <span class="est-02__wstext"><span class="est-02__wsname">Northline</span><span class="est-02__wsplan">Team workspace</span></span>
        <svg class="est-02__wschev" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m8 10 4 4 4-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <nav class="est-02__nav" aria-label="Workspace">
        <a class="est-02__nl est-02__nl--on" href="#est-02" aria-current="page"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="4" y="4.5" width="7" height="7" rx="2" stroke="currentColor" stroke-width="1.6"/><rect x="13" y="4.5" width="7" height="7" rx="2" stroke="currentColor" stroke-width="1.6"/><rect x="4" y="13.5" width="7" height="6" rx="2" stroke="currentColor" stroke-width="1.6"/><rect x="13" y="13.5" width="7" height="6" rx="2" stroke="currentColor" stroke-width="1.6"/></svg>Projects</a>
        <a class="est-02__nl" href="#est-02"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 6.5h14M5 12h14M5 17.5h9" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>My tasks</a>
        <a class="est-02__nl" href="#est-02"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="3.2" stroke="currentColor" stroke-width="1.6"/><path d="M3.5 19c0-3 2.5-5 5.5-5s5.5 2 5.5 5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="M16 7.2a3 3 0 0 1 0 5.6M17.5 19c0-2-.6-3.4-1.6-4.4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>People</a>
        <a class="est-02__nl" href="#est-02"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="7.5" stroke="currentColor" stroke-width="1.6"/><path d="M12 8.5v4l2.5 1.8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>Activity</a>
      </nav>
      <div class="est-02__sfoot">
        <span class="est-02__ring" id="est-02-ring" aria-hidden="true"><span class="est-02__ringtext" id="est-02-ringtext">0/3</span></span>
        <span class="est-02__sfoottext">Workspace setup</span>
      </div>
    </aside>

    <div class="est-02__main">
      <header class="est-02__top">
        <span class="est-02__crumb">Projects</span>
        <div class="est-02__topacts">
          <button class="est-02__ghost" type="button">Invite</button>
          <span class="est-02__ava" aria-hidden="true">EM</span>
        </div>
      </header>

      <div class="est-02__canvas">
        <section class="est-02__setup" id="est-02-setup">
          <div class="est-02__setuphead">
            <h1 class="est-02__h1" id="est-02-title">Three steps and Northline is yours</h1>
            <p class="est-02__sub" id="est-02-subtitle">Nothing here yet. Set the basics and your first board builds itself.</p>
          </div>

          <ol class="est-02__steps" id="est-02-steps">
            <li class="est-02__step">
              <button class="est-02__tick" type="button" data-step="1" aria-pressed="false">
                <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m6 12.5 4 4 8-9" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </button>
              <span class="est-02__stext"><span class="est-02__sname">Name your first project</span><span class="est-02__sdesc">Boards, timeline and docs come with it.</span></span>
            </li>
            <li class="est-02__step">
              <button class="est-02__tick" type="button" data-step="2" aria-pressed="false">
                <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m6 12.5 4 4 8-9" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </button>
              <span class="est-02__stext"><span class="est-02__sname">Invite two teammates</span><span class="est-02__sdesc">Assignees make the board useful.</span></span>
            </li>
            <li class="est-02__step">
              <button class="est-02__tick" type="button" data-step="3" aria-pressed="false">
                <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m6 12.5 4 4 8-9" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </button>
              <span class="est-02__stext"><span class="est-02__sname">Connect a repository</span><span class="est-02__sdesc">Commits close tasks automatically.</span></span>
            </li>
          </ol>

          <div class="est-02__cta">
            <button class="est-02__pri" type="button" id="est-02-pri">Create your first project</button>
            <button class="est-02__link" type="button" id="est-02-reset">Start over</button>
          </div>
        </section>

        <aside class="est-02__templates">
          <p class="est-02__tlabel">Start from a template</p>
          <ul class="est-02__tlist">
            <li><button class="est-02__tpl" type="button"><span class="est-02__tplg" data-g="sprint" aria-hidden="true"></span><span class="est-02__tpltext"><span class="est-02__tpln">Product sprint</span><span class="est-02__tpld">Backlog, sprint, review</span></span></button></li>
            <li><button class="est-02__tpl" type="button"><span class="est-02__tplg" data-g="launch" aria-hidden="true"></span><span class="est-02__tpltext"><span class="est-02__tpln">Go-to-market launch</span><span class="est-02__tpld">Assets, channels, dates</span></span></button></li>
            <li><button class="est-02__tpl" type="button"><span class="est-02__tplg" data-g="hiring" aria-hidden="true"></span><span class="est-02__tpltext"><span class="est-02__tpln">Hiring pipeline</span><span class="est-02__tpld">Stages and scorecards</span></span></button></li>
            <li><button class="est-02__tpl" type="button"><span class="est-02__tplg" data-g="support" aria-hidden="true"></span><span class="est-02__tpltext"><span class="est-02__tpln">Support triage</span><span class="est-02__tpld">Severity and rotation</span></span></button></li>
          </ul>
        </aside>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-02 {
  --bg: #f7f7f5;
  --surface: #ffffff;
  --sunk: #f1f0ec;
  --line: #e6e5e0;
  --line-2: #d9d8d2;
  --ink: #16161a;
  --muted: #5f6068;
  --faint: #8d8e95;
  --accent: #2b3a67;
  --ok: #2f6f4f;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-02 *,
.est-02 *::before,
.est-02 *::after {
  box-sizing: border-box;
}

.est-02 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-02 {
    --bg: oklch(0.975 0.003 85);
    --surface: oklch(1 0 0);
    --sunk: oklch(0.955 0.005 85);
    --line: oklch(0.912 0.005 85);
    --line-2: oklch(0.865 0.006 85);
    --ink: oklch(0.18 0.008 275);
    --muted: oklch(0.48 0.011 275);
    --faint: oklch(0.635 0.011 275);
    --accent: oklch(0.36 0.075 265);
    --ok: oklch(0.5 0.09 155);
  }
}

.est-02__shell {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-columns: min(17rem,26vw) minmax(0,1fr);
}

.est-02__side {
  display: grid;
  grid-template-rows: auto minmax(0,1fr) auto;
  gap: .5rem;
  padding: .85rem .7rem 1rem;
  border-inline-end: 1px solid var(--line);
  background: var(--surface);
}

.est-02__ws {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  gap: .6rem;
  align-items: center;
  text-align: start;
  padding: .55rem .6rem;
  cursor: pointer;
  background: transparent;
  border: 1px solid transparent;
  border-radius: 12px;
  transition: background .16s, border-color .16s;
}

.est-02__ws:hover {
  background: var(--sunk);
  border-color: var(--line);
}

.est-02__wsmark {
  inline-size: 2.1rem;
  block-size: 2.1rem;
  display: grid;
  place-items: center;
  border-radius: 9px;
  background: var(--accent);
  color: #fff;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .02em;
}

.est-02__wstext {
  min-inline-size: 0;
  display: grid;
}

.est-02__wsname {
  font-size: .9rem;
  font-weight: 600;
  letter-spacing: -.015em;
  color: var(--ink);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.est-02__wsplan {
  font-size: .72rem;
  color: var(--faint);
}

.est-02__wschev {
  inline-size: 1rem;
  block-size: 1rem;
  color: var(--faint);
}

.est-02__nav {
  display: grid;
  gap: .1rem;
  align-content: start;
}

.est-02__nl {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .5rem .6rem;
  border-radius: 9px;
  text-decoration: none;
  font-size: .875rem;
  font-weight: 500;
  color: var(--muted);
  transition: background .16s, color .16s;
}

.est-02__nl svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  flex: none;
  opacity: .85;
}

.est-02__nl:hover {
  background: var(--sunk);
  color: var(--ink);
}

.est-02__nl--on {
  background: var(--sunk);
  color: var(--ink);
  box-shadow: inset 0 0 0 1px var(--line);
}

.est-02__sfoot {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .7rem .6rem;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--sunk);
}

.est-02__ring {
  position: relative;
  inline-size: 2.15rem;
  block-size: 2.15rem;
  flex: none;
  display: grid;
  place-items: center;
  border-radius: 50%;
  --p: 0deg;
  background: conic-gradient(var(--accent) var(--p), color-mix(in oklab, var(--line-2) 70%, transparent) 0);
  transition: --p .5s ease;
}

.est-02__ring::after {
  content: '';
  position: absolute;
  inset: 3px;
  border-radius: 50%;
  background: var(--sunk);
}

.est-02__ringtext {
  position: relative;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .62rem;
  color: var(--muted);
}

.est-02__sfoottext {
  font-size: .8rem;
  color: var(--muted);
}

.est-02__main {
  min-inline-size: 0;
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
}

.est-02__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .85rem clamp(1rem,3vw,2rem);
  border-block-end: 1px solid var(--line);
  background: color-mix(in oklab, var(--surface) 80%, transparent);
  backdrop-filter: blur(6px);
}

.est-02__crumb {
  font-size: .9rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.est-02__topacts {
  display: flex;
  align-items: center;
  gap: .6rem;
}

.est-02__ghost {
  min-block-size: 2.25rem;
  padding: .45rem .8rem;
  font: inherit;
  font-size: .83rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line-2);
  border-radius: 9px;
  transition: background .16s;
}

.est-02__ghost:hover {
  background: var(--sunk);
}

.est-02__ava {
  inline-size: 1.9rem;
  block-size: 1.9rem;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: var(--sunk);
  border: 1px solid var(--line);
  font-size: .68rem;
  font-weight: 600;
  color: var(--muted);
}

.est-02__canvas {
  min-inline-size: 0;
  padding: clamp(1.25rem,4vw,3.25rem) clamp(1rem,3vw,2rem);
  display: grid;
  gap: clamp(1rem,2.5vw,2rem);
  grid-template-columns: repeat(auto-fit,minmax(min(19rem,100%),1fr));
  align-content: start;
  align-items: start;
  background: radial-gradient(120% 90% at 12% 0%, color-mix(in oklab, var(--accent) 5%, transparent), transparent 60%), var(--bg);
}

.est-02__setup {
  grid-column: span 2;
  inline-size: min(38rem,100%);
  display: grid;
  gap: 1.35rem;
  padding: clamp(1.25rem,3vw,2rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 20px;
  box-shadow: 0 1px 2px rgba(20,20,25,.04), 0 30px 60px -46px rgba(20,20,25,.4);
  animation: est-02-rise .55s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-02-rise {
  from {
    opacity: 0;
    translate: 0 10px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-02__setuphead {
  display: grid;
  gap: .45rem;
}

.est-02__h1 {
  margin: 0;
  font-size: clamp(1.4rem,3.2vw,1.95rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.12;
  text-wrap: balance;
}

.est-02__sub {
  margin: 0;
  max-inline-size: 44ch;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.est-02__steps {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .5rem;
}

.est-02__step {
  display: grid;
  grid-template-columns: auto minmax(0,1fr);
  gap: .85rem;
  align-items: center;
  padding: .8rem .9rem;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  transition: border-color .18s, background .18s;
}

.est-02__step:hover {
  border-color: var(--line-2);
  background: var(--sunk);
}

.est-02__tick {
  inline-size: 1.6rem;
  block-size: 1.6rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  flex: none;
  color: transparent;
  background: var(--surface);
  border: 1.5px solid var(--line-2);
  border-radius: 50%;
  transition: background .2s, border-color .2s, color .2s, scale .2s;
}

.est-02__tick svg {
  inline-size: .95rem;
  block-size: .95rem;
}

.est-02__tick:hover {
  border-color: var(--accent);
}

.est-02__tick[aria-pressed="true"] {
  color: #fff;
  background: var(--accent);
  border-color: var(--accent);
  scale: 1.04;
}

.est-02__stext {
  min-inline-size: 0;
  display: grid;
  gap: .15rem;
}

.est-02__sname {
  font-size: .92rem;
  font-weight: 500;
  letter-spacing: -.015em;
}

.est-02__step[data-done] .est-02__sname {
  color: var(--muted);
  text-decoration: line-through;
  text-decoration-color: var(--line-2);
}

.est-02__sdesc {
  font-size: .8rem;
  color: var(--faint);
}

.est-02__cta {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem;
  align-items: center;
}

.est-02__pri {
  min-block-size: 2.85rem;
  padding: .7rem 1.15rem;
  font: inherit;
  font-size: .9rem;
  font-weight: 500;
  cursor: pointer;
  color: #fff;
  background: var(--accent);
  border: 1px solid transparent;
  border-radius: 12px;
  transition: translate .16s, box-shadow .18s, background .16s;
  box-shadow: 0 8px 18px -12px color-mix(in oklab, var(--accent) 75%, transparent);
}

.est-02__pri:hover {
  translate: 0 -1px;
  box-shadow: 0 14px 26px -14px color-mix(in oklab, var(--accent) 70%, transparent);
}

.est-02__link {
  padding: .4rem .1rem;
  font: inherit;
  font-size: .85rem;
  cursor: pointer;
  color: var(--muted);
  background: none;
  border: 0;
  text-decoration: underline;
  text-decoration-color: var(--line-2);
  text-underline-offset: 3px;
}

.est-02__link:hover {
  color: var(--ink);
}

.est-02__tick:focus-visible,
.est-02__pri:focus-visible,
.est-02__link:focus-visible,
.est-02__tpl:focus-visible,
.est-02__ghost:focus-visible,
.est-02__ws:focus-visible,
.est-02__nl:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.est-02__templates {
  inline-size: min(22rem,100%);
  display: grid;
  gap: .6rem;
  align-content: start;
}

.est-02__tlabel {
  margin: 0;
  font-size: .8rem;
  font-weight: 500;
  color: var(--faint);
}

.est-02__tlist {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .4rem;
}

.est-02__tpl {
  inline-size: 100%;
  display: grid;
  grid-template-columns: auto minmax(0,1fr);
  gap: .7rem;
  align-items: center;
  text-align: start;
  padding: .7rem .8rem;
  cursor: pointer;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 13px;
  transition: translate .16s, border-color .16s, box-shadow .18s;
}

.est-02__tpl:hover {
  translate: 0 -1px;
  border-color: var(--line-2);
  box-shadow: 0 12px 24px -20px rgba(20,20,25,.5);
}

.est-02__tplg {
  inline-size: 2rem;
  block-size: 2rem;
  border-radius: 8px;
  background: var(--sunk);
  box-shadow: inset 0 0 0 1px var(--line);
  position: relative;
  overflow: hidden;
}

.est-02__tplg::after {
  content: '';
  position: absolute;
  inset: .35rem;
  border-radius: 3px;
  background: repeating-linear-gradient(90deg, color-mix(in oklab, var(--accent) 45%, transparent) 0 2px, transparent 2px 5px);
  opacity: .7;
}

.est-02__tplg[data-g="launch"]::after {
  background: conic-gradient(from 210deg, color-mix(in oklab, var(--accent) 50%, transparent), transparent 60%);
}

.est-02__tplg[data-g="hiring"]::after {
  background: linear-gradient(180deg, color-mix(in oklab, var(--accent) 45%, transparent) 0 30%, transparent 30% 45%, color-mix(in oklab, var(--accent) 30%, transparent) 45% 70%, transparent 70%);
}

.est-02__tplg[data-g="support"]::after {
  background: radial-gradient(circle at 50% 50%, color-mix(in oklab, var(--accent) 55%, transparent) 30%, transparent 32%);
}

.est-02__tpltext {
  min-inline-size: 0;
  display: grid;
  gap: .1rem;
}

.est-02__tpln {
  font-size: .87rem;
  font-weight: 500;
  letter-spacing: -.012em;
}

.est-02__tpld {
  font-size: .76rem;
  color: var(--faint);
}

.est-02__setup[data-ready] {
  border-color: color-mix(in oklab, var(--ok) 35%, var(--line));
}

@media (max-width: 900px) {
  .est-02__shell {
    grid-template-columns: 1fr;
  }

  .est-02__side {
    grid-template-rows: auto;
    grid-template-columns: auto minmax(0,1fr) auto;
    align-items: center;
    border-inline-end: 0;
    border-block-end: 1px solid var(--line);
  }

  .est-02__nav {
    display: none;
  }

  .est-02__setup {
    grid-column: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .est-02 *,
    .est-02 *::before,
    .est-02 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-02__setup,
    .est-02__step,
    .est-02__tpl,
    .est-02__pri {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-02'); if(!root) return;
  var ring = root.querySelector('#est-02-ring'), ringtext = root.querySelector('#est-02-ringtext'),
      title = root.querySelector('#est-02-title'), sub = root.querySelector('#est-02-subtitle'),
      setup = root.querySelector('#est-02-setup'), pri = root.querySelector('#est-02-pri'),
      reset = root.querySelector('#est-02-reset'), ticks = root.querySelectorAll('.est-02__tick');
  var copy = [
    ['Three steps and Northline is yours','Nothing here yet. Set the basics and your first board builds itself.'],
    ['Good start','Two more and the board fills with your own work.'],
    ['Almost there','One step left before Northline runs itself.'],
    ['Workspace ready','Create the project and your team lands straight in it.']
  ];
  function paint(){
    var done = 0;
    ticks.forEach(function(t){
      var on = t.getAttribute('aria-pressed') === 'true';
      if(on) done++;
      t.closest('.est-02__step').toggleAttribute('data-done', on);
    });
    ring.style.setProperty('--p', (done / 3 * 360) + 'deg');
    ringtext.textContent = done + '/3';
    title.textContent = copy[done][0];
    sub.textContent = copy[done][1];
    setup.toggleAttribute('data-ready', done === 3);
    pri.textContent = done === 3 ? 'Open your project' : 'Create your first project';
  }
  ticks.forEach(function(t){
    t.addEventListener('click', function(){
      t.setAttribute('aria-pressed', t.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
      paint();
    });
  });
  reset.addEventListener('click', function(){
    ticks.forEach(function(t){ t.setAttribute('aria-pressed','false'); });
    paint();
  });
  paint();
})();
```
