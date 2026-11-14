---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/auto-vs-manual-popover-behavior/"
title: "Auto vs Manual Popover Behavior"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "Two panels open at once, side by side, so the difference between the auto and manual states is something you can click rather than read."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Auto vs Manual Popover Behavior
Source: https://codefronts.com/snippets/css-popovers/auto-vs-manual-popover-behavior/

Two panels open at once, side by side, so the difference between the auto and manual states is something you can click rather than read. Auto light-dismisses, answers Escape, and forces other auto popovers closed; manual ignores all three and waits for an explicit hide. The same board also wires the three popovertargetaction values to separate buttons.
## HTML
```html
<div class="pop-02">
  <div class="pop-02__stage">
    <section class="pop-02__board" aria-label="Popover state comparison">
      <header class="pop-02__head">
        <h2 class="pop-02__h">Dismissal is a state, not a style</h2>
        <p class="pop-02__sub">Open both. Then click the empty board area.</p>
      </header>

      <div class="pop-02__cols">
        <div class="pop-02__col">
          <p class="pop-02__tag pop-02__tag--auto">popover="auto"</p>
          <div class="pop-02__btns">
            <button class="pop-02__btn" type="button" popovertarget="pop-02-auto">Toggle notifications</button>
            <button class="pop-02__btn pop-02__btn--ghost" type="button" popovertarget="pop-02-auto2">Toggle activity</button>
          </div>
          <ul class="pop-02__rules">
            <li class="pop-02__rule">Outside click closes it</li>
            <li class="pop-02__rule">Escape closes it</li>
            <li class="pop-02__rule">Opening another auto closes it</li>
          </ul>
        </div>

        <div class="pop-02__col">
          <p class="pop-02__tag pop-02__tag--manual">popover="manual"</p>
          <div class="pop-02__btns">
            <button class="pop-02__btn" type="button" popovertarget="pop-02-manual" popovertargetaction="show">Show inspector</button>
            <button class="pop-02__btn pop-02__btn--ghost" type="button" popovertarget="pop-02-manual" popovertargetaction="hide">Hide inspector</button>
          </div>
          <ul class="pop-02__rules">
            <li class="pop-02__rule">Outside click does nothing</li>
            <li class="pop-02__rule">Escape does nothing</li>
            <li class="pop-02__rule">You own dismissal</li>
          </ul>
        </div>
      </div>
    </section>
  </div>

  <div class="pop-02__panel pop-02__panel--a" popover="auto" id="pop-02-auto" role="group" aria-label="Notifications">
    <p class="pop-02__ptitle">Notifications</p>
    <p class="pop-02__pline">Priya Sharma approved deploy <span class="pop-02__mono">web-4821</span>.</p>
    <p class="pop-02__pline">Nightly export finished in 4m 12s.</p>
    <p class="pop-02__pfoot">Auto · light dismiss on</p>
  </div>

  <div class="pop-02__panel pop-02__panel--b" popover="auto" id="pop-02-auto2" role="group" aria-label="Activity">
    <p class="pop-02__ptitle">Activity</p>
    <p class="pop-02__pline">Jordan Lee opened a draft on Billing.</p>
    <p class="pop-02__pfoot">Opening me closed the other auto panel</p>
  </div>

  <div class="pop-02__panel pop-02__panel--m" popover="manual" id="pop-02-manual" role="group" aria-label="Request inspector">
    <div class="pop-02__phead">
      <p class="pop-02__ptitle">Request inspector</p>
      <button class="pop-02__x" type="button" popovertarget="pop-02-manual" popovertargetaction="hide" aria-label="Close inspector">
        <svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8"/></svg>
      </button>
    </div>
    <p class="pop-02__pline"><span class="pop-02__mono">GET /v2/accounts</span> · 200 · 84ms</p>
    <p class="pop-02__pline"><span class="pop-02__mono">POST /v2/tokens</span> · 201 · 132ms</p>
    <p class="pop-02__pfoot">Manual · nothing dismisses me but that button</p>
  </div>
</div>
```
## CSS
```css
.pop-02 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --navy: #0d1b33;
  --navy-2: #142545;
  --surface: #1b3054;
  --ink: #eaf1fb;
  --muted: #9db2d4;
  --rule: #274468;
  --accent: #5fd3c4;
  --warn: #f4b26a;
  --radius: 2px;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SFMono-Regular", Menlo, monospace;
  background: var(--navy);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 34px 16px;
}

.pop-02__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 68px);
}

.pop-02__board {
  inline-size: 100%;
  max-inline-size: 44rem;
  min-inline-size: 0;
  background: var(--navy-2);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  padding: 24px 20px 26px;
}

.pop-02__head {
  margin-bottom: 22px;
}

.pop-02__h {
  margin: 0 0 6px;
  font: 600 clamp(20px, 4.4vw, 26px)/1.2 var(--font-ui);
  letter-spacing: -0.02em;
}

.pop-02__sub {
  margin: 0;
  font-size: 13px;
  color: var(--muted);
}

.pop-02__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
  gap: 18px;
}

.pop-02__col {
  min-inline-size: 0;
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  padding: 16px 14px;
  background: var(--navy);
}

.pop-02__tag {
  display: inline-block;
  margin: 0 0 14px;
  padding: 5px 9px;
  font: 650 11px/1 var(--font-mono);
  border-radius: var(--radius);
}

.pop-02__tag--auto {
  color: var(--navy);
  background: var(--accent);
}

.pop-02__tag--manual {
  color: var(--navy);
  background: var(--warn);
}

.pop-02__btns {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}

.pop-02__btn {
  flex: 1 1 auto;
  min-inline-size: 0;
  min-height: 44px;
  padding: 0 14px;
  font: 600 12.5px/1 var(--font-ui);
  color: var(--navy);
  background: var(--ink);
  border: 1px solid var(--ink);
  border-radius: var(--radius);
  cursor: pointer;
}

.pop-02__btn--ghost {
  color: var(--ink);
  background: transparent;
  border-color: var(--rule);
}

.pop-02__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.pop-02__rules {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 7px;
}

.pop-02__rule {
  position: relative;
  padding-inline-start: 16px;
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--muted);
  min-inline-size: 0;
}

.pop-02__rule::before {
  content: "";
  position: absolute;
  inset-inline-start: 0;
  inset-block-start: 7px;
  inline-size: 6px;
  block-size: 6px;
  background: var(--muted);
}

.pop-02__panel {
  position: fixed;
  margin: 0;
  inline-size: min(19rem, calc(100vw - 28px));
  max-inline-size: calc(100vw - 28px);
  padding: 15px 16px 14px;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  box-shadow: 0 26px 50px -24px rgba(0, 0, 0, 0.85);
}

.pop-02__panel--a {
  inset: auto auto 26px 26px;
}

.pop-02__panel--b {
  inset: 26px 26px auto auto;
}

.pop-02__panel--m {
  inset: auto 26px 26px auto;
  border-color: var(--warn);
}

@media (max-width: 560px) {
  .pop-02__panel--a {
    inset: auto 14px 14px 14px;
  }

  .pop-02__panel--b {
    inset: 14px 14px auto 14px;
  }

  .pop-02__panel--m {
    inset: auto 14px 84px 14px;
  }
}

.pop-02__phead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.pop-02__ptitle {
  margin: 0 0 8px;
  font: 650 12px/1 var(--font-ui);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.pop-02__x {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  min-height: 44px;
  margin: -14px -12px 0 0;
  color: var(--warn);
  background: none;
  border: 0;
  cursor: pointer;
}

.pop-02__x:focus-visible {
  outline: 3px solid var(--warn);
  outline-offset: 1px;
}

.pop-02__pline {
  margin: 0 0 7px;
  font-size: 13px;
  line-height: 1.55;
}

.pop-02__mono {
  font: 0.9em/1 var(--font-mono);
  color: var(--accent);
}

.pop-02__pfoot {
  margin: 10px 0 0;
  padding-top: 10px;
  border-top: 1px solid var(--rule);
  font-size: 11.5px;
  color: var(--muted);
}

.pop-02__panel--m .pop-02__pfoot {
  color: var(--warn);
}

@media (prefers-color-scheme: light) {
  .pop-02 {
    --navy: #eef2f8;
    --navy-2: #ffffff;
    --surface: #ffffff;
    --ink: #10203a;
    --muted: #5b7196;
    --rule: #d3dded;
    --accent: #12766b;
    --warn: #9a5b12;
  }

  .pop-02__btn {
    color: #ffffff;
    background: var(--ink);
    border-color: var(--ink);
  }

  .pop-02__btn--ghost {
    color: var(--ink);
    background: transparent;
    border-color: var(--rule);
  }

  .pop-02__tag--auto,
    .pop-02__tag--manual {
    color: #ffffff;
  }

  .pop-02__panel {
    box-shadow: 0 22px 44px -26px rgba(16, 32, 58, 0.45);
  }
}

[data-theme="dark"] .pop-02 {
  --navy: #0d1b33;
  --navy-2: #142545;
  --surface: #1b3054;
  --ink: #eaf1fb;
  --muted: #9db2d4;
  --rule: #274468;
  --accent: #5fd3c4;
  --warn: #f4b26a;
}
```
