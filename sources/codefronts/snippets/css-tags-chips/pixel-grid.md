---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/pixel-grid/"
title: "Retro Pixel Art Style Category Tag"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "Genuine 8-bit construction, not a rounded pill wearing a costume: the stepped pixel border is four offset box-shadows (so the corners stay honestly empty),…"
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro Pixel Art Style Category Tag
Source: https://codefronts.com/snippets/css-tags-chips/pixel-grid/

Genuine 8-bit construction, not a rounded pill wearing a costume: the stepped pixel border is four offset box-shadows (so the corners stay honestly empty), the drop shadow is a hard 4px block that the tag physically presses into on click, the NEW! badge blinks at 2fps with steps() easing — because smooth easing is the one thing that instantly breaks the fiction — and an 8-bit heart is drawn live out of box-shadow pixels on a 3px element. Zero images, zero fonts to load.
## HTML
```html
<section class="ctc-13" aria-label="Retro pixel art category tag demo">
  <div class="ctc-13__stage">
    <div class="ctc-13__wrap">
      <header class="ctc-13__head">
        <p class="ctc-13__kicker">PLAYER 1 · CATEGORY SELECT</p>
        <h1>Every corner honestly empty</h1>
      </header>
      <div class="ctc-13__panel">
        <p class="ctc-13__lab">01 · Category tags — press one, it lands in its own shadow</p>
        <div class="ctc-13__row">
          <a class="ctc-13__px" style="--c:oklch(0.72 0.17 145)" href="#ctc13">GUIDES</a>
          <a class="ctc-13__px" style="--c:oklch(0.68 0.16 250)" href="#ctc13">SPEEDRUNS</a>
          <a class="ctc-13__px" style="--c:oklch(0.78 0.16 85)" href="#ctc13">HIGH SCORES</a>
          <a class="ctc-13__px" style="--c:oklch(0.65 0.21 25)" href="#ctc13">BOSS FIGHTS</a>
        </div>
      </div>
      <div class="ctc-13__panel">
        <p class="ctc-13__lab">02 · Badges — steps() or it doesn't count</p>
        <div class="ctc-13__row">
          <span class="ctc-13__px ctc-13__px--blink" style="--c:oklch(0.65 0.21 25)">NEW!</span>
          <span class="ctc-13__px" style="--c:oklch(0.78 0.16 85)"><i class="ctc-13__coin" aria-hidden="true"></i>×99</span>
          <span class="ctc-13__px" style="--c:oklch(0.72 0.17 145)"><i class="ctc-13__heart" aria-hidden="true"></i>3 LIVES</span>
          <span class="ctc-13__px ctc-13__px--ghost">LOCKED</span>
        </div>
      </div>
      <div class="ctc-13__panel">
        <p class="ctc-13__lab">03 · Scale — set --u once, the sprite sheet follows</p>
        <div class="ctc-13__row" style="align-items:center">
          <span class="ctc-13__px" style="--u:2px;--c:oklch(0.68 0.16 250)">--u: 2px</span>
          <span class="ctc-13__px" style="--c:oklch(0.68 0.16 250)">--u: 3px</span>
          <span class="ctc-13__px" style="--u:4px;--c:oklch(0.68 0.16 250)">--u: 4px</span>
        </div>
      </div>
      <p class="ctc-13__note">BORDER = 4 OFFSET BOX-SHADOWS. HEART = BOX-SHADOW BITMAP ON A 3PX DOT. PRESS = TRANSLATE INTO THE BLOCK SHADOW, <code>transition:none</code>.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-13,
.ctc-13 *,
.ctc-13 *::before,
.ctc-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-13 {
  --u: 3px;
  --bg: oklch(0.24 0.03 280);
  --panel: oklch(0.29 0.035 280);
  --ink: oklch(0.14 0.02 280);
  --paper: oklch(0.96 0.01 90);
  --mut: oklch(0.68 0.03 280);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  color: var(--paper);
  container-type: inline-size;
}

.ctc-13__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: repeating-linear-gradient(0deg,oklch(1 0 0/.025) 0 2px,transparent 2px 4px),var(--bg);
  container: ctc13/inline-size;
}

.ctc-13__wrap {
  width: min(660px,100%);
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ctc-13__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .22em;
  color: oklch(0.78 0.16 85);
}

.ctc-13__head h1 {
  font-size: clamp(21px,3.4cqi,32px);
  font-weight: 800;
  letter-spacing: .02em;
  text-transform: uppercase;
  margin: 10px 0 6px;
  text-shadow: var(--u) var(--u) 0 oklch(0.45 0.18 280);
}

.ctc-13__panel {
  background: var(--panel);
  padding: 18px;
  box-shadow: calc(var(--u)*-1) 0 0 0 var(--ink),var(--u) 0 0 0 var(--ink),0 calc(var(--u)*-1) 0 0 var(--ink),0 var(--u) 0 0 var(--ink);
}

.ctc-13__lab {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 14px;
}

.ctc-13__row {
  display: flex;
  flex-wrap: wrap;
  gap: calc(var(--u)*5);
}

.ctc-13__px {
  --c: oklch(0.7 0.15 250);
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: calc(var(--u)*3);
  min-height: 44px;
  padding: calc(var(--u)*3) calc(var(--u)*5);
  background: var(--c);
  color: var(--ink);
  font-family: inherit;
  font-size: calc(var(--u)*4.2);
  font-weight: 800;
  letter-spacing: .08em;
  text-decoration: none;
  white-space: nowrap;
  box-shadow: calc(var(--u)*-1) 0 0 0 var(--ink),var(--u) 0 0 0 var(--ink),0 calc(var(--u)*-1) 0 0 var(--ink),0 var(--u) 0 0 var(--ink),var(--u) calc(var(--u)*2) 0 0 var(--ink),calc(var(--u)*2) var(--u) 0 0 var(--ink),calc(var(--u)*2) calc(var(--u)*2) 0 0 var(--ink);
  transition: none;
}

a.ctc-13__px:hover,
a.ctc-13__px:focus-visible {
  filter: brightness(1.12);
}

a.ctc-13__px:focus-visible {
  outline: var(--u) dashed var(--paper);
  outline-offset: calc(var(--u)*2);
}

a.ctc-13__px:active {
  translate: var(--u) var(--u);
  box-shadow: calc(var(--u)*-1) 0 0 0 var(--ink),var(--u) 0 0 0 var(--ink),0 calc(var(--u)*-1) 0 0 var(--ink),0 var(--u) 0 0 var(--ink);
}

.ctc-13__px--blink {
  animation: ctc13-blink 1s steps(2,jump-none) infinite;
}

@keyframes ctc13-blink {
  50% {
    filter: brightness(1.35);
  }
}

.ctc-13__px--ghost {
  background: var(--panel);
  color: var(--mut);
  box-shadow: calc(var(--u)*-1) 0 0 0 var(--mut),var(--u) 0 0 0 var(--mut),0 calc(var(--u)*-1) 0 0 var(--mut),0 var(--u) 0 0 var(--mut);
}

.ctc-13__coin {
  width: calc(var(--u)*4);
  height: calc(var(--u)*4);
  border-radius: 0;
  background: oklch(0.85 0.14 90);
  box-shadow: inset 0 0 0 var(--u) oklch(0.62 0.13 75);
  animation: ctc13-spin 1.2s steps(4,jump-none) infinite;
}

@keyframes ctc13-spin {
  0% {
    scale: 1 1;
  }

  25% {
    scale: .4 1;
  }

  50% {
    scale: .1 1;
  }

  75% {
    scale: .4 1;
  }

  100% {
    scale: 1 1;
  }
}

.ctc-13__heart {
  width: var(--u);
  height: var(--u);
  margin: calc(var(--u)*1) calc(var(--u)*3.5) calc(var(--u)*2.5) calc(var(--u)*1.5);
  background: transparent;
  box-shadow: 0 0 0 0 oklch(0.55 0.22 20),var(--u) 0 0 0 oklch(0.55 0.22 20),calc(var(--u)*3) 0 0 0 oklch(0.55 0.22 20),calc(var(--u)*4) 0 0 0 oklch(0.55 0.22 20),calc(var(--u)*-1) var(--u) 0 0 oklch(0.55 0.22 20),0 var(--u) 0 0 oklch(0.55 0.22 20),var(--u) var(--u) 0 0 oklch(0.55 0.22 20),calc(var(--u)*2) var(--u) 0 0 oklch(0.55 0.22 20),calc(var(--u)*3) var(--u) 0 0 oklch(0.55 0.22 20),calc(var(--u)*4) var(--u) 0 0 oklch(0.55 0.22 20),calc(var(--u)*5) var(--u) 0 0 oklch(0.55 0.22 20),0 calc(var(--u)*2) 0 0 oklch(0.55 0.22 20),var(--u) calc(var(--u)*2) 0 0 oklch(0.55 0.22 20),calc(var(--u)*2) calc(var(--u)*2) 0 0 oklch(0.55 0.22 20),calc(var(--u)*3) calc(var(--u)*2) 0 0 oklch(0.55 0.22 20),calc(var(--u)*4) calc(var(--u)*2) 0 0 oklch(0.55 0.22 20),var(--u) calc(var(--u)*3) 0 0 oklch(0.55 0.22 20),calc(var(--u)*2) calc(var(--u)*3) 0 0 oklch(0.55 0.22 20),calc(var(--u)*3) calc(var(--u)*3) 0 0 oklch(0.55 0.22 20),calc(var(--u)*2) calc(var(--u)*4) 0 0 oklch(0.55 0.22 20);
}

.ctc-13__note {
  font-size: 11px;
  line-height: 1.8;
  letter-spacing: .06em;
  color: var(--mut);
}

.ctc-13__note code {
  background: oklch(1 0 0/.1);
  padding: 1px 5px;
  color: var(--paper);
}

@media (prefers-reduced-motion: reduce) {
  .ctc-13__px--blink,
    .ctc-13__coin {
    animation: none;
  }
}
```
