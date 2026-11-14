---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/flip-and-fallback-positions/"
title: "Flip and Fallback Positions"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "Collision handling used to be the main reason to install a positioning library."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flip and Fallback Positions
Source: https://codefronts.com/snippets/css-popovers/flip-and-fallback-positions/

Collision handling used to be the main reason to install a positioning library. position-try-fallbacks replaces it: list the placements you accept, and the browser tries them in order until the panel fits. This demo puts the anchor in a scrollable strip so you can drag it to an edge and watch the panel flip sides in real time rather than take it on faith.
## HTML
```html
<div class="pop-07">
  <div class="pop-07__stage">
    <div class="pop-07__term">
      <p class="pop-07__kicker">scroll the strip, then open the panel</p>
      <div class="pop-07__scroller">
        <div class="pop-07__strip">
          <span class="pop-07__col">idle</span>
          <span class="pop-07__col">idle</span>
          <span class="pop-07__col">idle</span>
          <button class="pop-07__node" type="button" popovertarget="pop-07-panel">
            node-07
            <svg viewBox="0 0 16 16" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>
          </button>
          <span class="pop-07__col">idle</span>
          <span class="pop-07__col">idle</span>
          <span class="pop-07__col">idle</span>
        </div>
      </div>
      <ul class="pop-07__order">
        <li class="pop-07__step">1 · position-area: block-end center</li>
        <li class="pop-07__step">2 · flip-block</li>
        <li class="pop-07__step">3 · flip-inline</li>
        <li class="pop-07__step">4 · @position-try --pop-07-side</li>
      </ul>
    </div>
  </div>

  <div class="pop-07__panel" popover="auto" id="pop-07-panel" role="group" aria-label="Node detail">
    <p class="pop-07__ptitle">node-07 · eu-west-1b</p>
    <p class="pop-07__pline">cpu 41% · mem 2.8/8 GiB · 14 pods</p>
    <p class="pop-07__pline">last drain 6d ago by Jordan Lee</p>
    <p class="pop-07__pfoot">I flip rather than clip.</p>
  </div>
</div>
```
## CSS
```css
.pop-07 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #05080a;
  --surface: #0a1014;
  --ink: #d6f5e3;
  --muted: #5e8a75;
  --phos: #3ff08c;
  --rule: #16241d;
  --font-mono: ui-monospace, "SFMono-Regular", Menlo, monospace;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-mono);
  padding: 36px 14px;
}

.pop-07__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 72px);
}

.pop-07__term {
  inline-size: 100%;
  max-inline-size: 34rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  padding: 18px 16px 16px;
}

.pop-07__kicker {
  margin: 0 0 14px;
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.pop-07__scroller {
  overflow-x: auto;
  overscroll-behavior-x: contain;
  border: 1px dashed var(--rule);
  padding: 14px 12px;
  scrollbar-color: var(--phos) var(--surface);
}

.pop-07__strip {
  display: flex;
  align-items: center;
  gap: 10px;
  inline-size: max-content;
}

.pop-07__col {
  flex: none;
  display: grid;
  place-items: center;
  inline-size: 74px;
  min-height: 44px;
  font-size: 11px;
  color: var(--muted);
  border: 1px solid var(--rule);
}

.pop-07__node {
  flex: none;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 13px;
  font: 650 12px/1 var(--font-mono);
  color: var(--bg);
  background: var(--phos);
  border: 1px solid var(--phos);
  border-radius: 0;
  cursor: pointer;
  anchor-name: --pop-07-anchor;
}

.pop-07__node:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 2px;
}

.pop-07__order {
  margin: 14px 0 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 5px;
}

.pop-07__step {
  font-size: 11.5px;
  line-height: 1.5;
  color: var(--muted);
  min-inline-size: 0;
}

.pop-07__panel {
  position: fixed;
  margin: 0;
  inline-size: min(17rem, calc(100vw - 24px));
  max-inline-size: calc(100vw - 24px);
  padding: 13px 14px;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--phos);
  border-radius: 0;
  box-shadow: 0 0 0 1px rgba(63, 240, 140, 0.12), 0 18px 40px -22px rgba(63, 240, 140, 0.4);
}

@supports (anchor-name: --a) {
  @position-try --pop-07-side {
    position-area: inline-end center;
    margin: 0 0 0 10px;
    max-inline-size: min(15rem, calc(100vw - 24px));
  }

  .pop-07__panel {
    position-anchor: --pop-07-anchor;
    position-area: block-end center;
    inset: auto;
    margin-block-start: 10px;
    position-try-fallbacks: flip-block, flip-inline, --pop-07-side;
  }
}

.pop-07__ptitle {
  margin: 0 0 9px;
  font-size: 12px;
  font-weight: 650;
  letter-spacing: 0.04em;
  color: var(--phos);
}

.pop-07__pline {
  margin: 0 0 6px;
  font-size: 11.5px;
  line-height: 1.55;
  color: var(--muted);
}

.pop-07__pfoot {
  margin: 10px 0 0;
  padding-block-start: 9px;
  border-block-start: 1px dashed var(--rule);
  font-size: 11px;
  color: var(--ink);
}

@media (prefers-color-scheme: light) {
  .pop-07 {
    --bg: #eef2ef;
    --surface: #ffffff;
    --ink: #0d1a14;
    --muted: #4a6b5b;
    --phos: #0f7a45;
    --rule: #cfdcd4;
  }

  .pop-07__node {
    color: #ffffff;
  }

  .pop-07__panel {
    box-shadow: 0 18px 40px -24px rgba(13, 26, 20, 0.35);
  }
}

[data-theme="dark"] .pop-07 {
  --bg: #05080a;
  --surface: #0a1014;
  --ink: #d6f5e3;
  --muted: #5e8a75;
  --phos: #3ff08c;
  --rule: #16241d;
}

[data-theme="dark"] .pop-07 .pop-07__node {
  color: var(--bg);
}
```
