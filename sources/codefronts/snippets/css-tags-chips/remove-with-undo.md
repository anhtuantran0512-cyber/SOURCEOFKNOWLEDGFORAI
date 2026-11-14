---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/remove-with-undo/"
title: "Dismissible Chip with Undo Toast Notification"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "Forgiving deletion, the pattern Gmail made mandatory — remove a chip and a toast slides up offering Undo — built from checkbox state alone."
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dismissible Chip with Undo Toast Notification
Source: https://codefronts.com/snippets/css-tags-chips/remove-with-undo/

Forgiving deletion, the pattern Gmail made mandatory — remove a chip and a toast slides up offering Undo — built from checkbox state alone. The dismissed chip's checkbox drives everything: chip collapses, its personal toast rises (bottom-center, stacked by DOM order), and the toast's Undo button is just a <label> pointed back at the same checkbox — click it and the chip re-inflates through the same transition it left by. State restoration as a hyperlink between two controls.
## HTML
```html
<section class="ctc-19" aria-label="Dismissible chip with undo toast demo">
  <form class="ctc-19__stage">
    <div class="ctc-19__wrap">
      <header class="ctc-19__head">
        <p class="ctc-19__kicker">Undo toasts · label[for] as time travel</p>
        <h1>Delete without fear</h1>
        <p class="ctc-19__sub">Dismiss a connected app — a toast offers the way back. Undo is a <code>&lt;label&gt;</code> for the same checkbox that deleted it.</p>
      </header>
      <div class="ctc-19__panel">
        <p class="ctc-19__lab">Connected apps</p>
        <div class="ctc-19__row">
          <span class="ctc-19__chip" style="--h:255"><i>F</i><span>Figma</span><input type="checkbox" id="ctc19-figma" aria-label="Disconnect Figma"></span>
          <span class="ctc-19__chip" style="--h:150"><i>S</i><span>Slack</span><input type="checkbox" id="ctc19-slack" aria-label="Disconnect Slack"></span>
          <span class="ctc-19__chip" style="--h:40"><i>L</i><span>Linear</span><input type="checkbox" id="ctc19-linear" aria-label="Disconnect Linear"></span>
          <span class="ctc-19__chip" style="--h:320"><i>N</i><span>Notion</span><input type="checkbox" id="ctc19-notion" aria-label="Disconnect Notion"></span>
          <span class="ctc-19__chip" style="--h:200"><i>G</i><span>GitHub</span><input type="checkbox" id="ctc19-github" aria-label="Disconnect GitHub"></span>
        </div>
        <button class="ctc-19__reset" type="reset">↺ Restore everything</button>
      </div>
      <div class="ctc-19__toasts" aria-label="Undo notifications">
        <div class="ctc-19__toast" data-for="figma" role="status"><b>Figma disconnected</b><label for="ctc19-figma">Undo</label><i></i></div>
        <div class="ctc-19__toast" data-for="slack" role="status"><b>Slack disconnected</b><label for="ctc19-slack">Undo</label><i></i></div>
        <div class="ctc-19__toast" data-for="linear" role="status"><b>Linear disconnected</b><label for="ctc19-linear">Undo</label><i></i></div>
        <div class="ctc-19__toast" data-for="notion" role="status"><b>Notion disconnected</b><label for="ctc19-notion">Undo</label><i></i></div>
        <div class="ctc-19__toast" data-for="github" role="status"><b>GitHub disconnected</b><label for="ctc19-github">Undo</label><i></i></div>
      </div>
      <p class="ctc-19__note">The drain bar signals urgency but CSS can't run timers — the toast politely waits. Auto-commit needs three lines of JS: on check, <code>setTimeout</code> the real deletion; Undo clears it.</p>
    </div>
  </form>
</section>
```
## CSS
```css
.ctc-19,
.ctc-19 *,
.ctc-19 *::before,
.ctc-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-19 {
  --bg: oklch(0.965 0.008 230);
  --panel: oklch(0.997 0.002 230);
  --ink: oklch(0.24 0.025 240);
  --mut: oklch(0.5 0.02 240);
  --line: oklch(0.88 0.012 230);
  --acc: oklch(0.55 0.16 230);
  --del: oklch(0.6 0.21 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-19__stage {
  position: relative;
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 88% -10%,color-mix(in oklch,var(--acc) 13%,transparent),transparent 62%),var(--bg);
  container: ctc19/inline-size;
  border: 0;
}

.ctc-19__wrap {
  width: min(620px,100%);
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ctc-19__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.ctc-19__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 6px;
}

.ctc-19__sub {
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--mut);
}

.ctc-19__sub code,
.ctc-19__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(0.92 0.01 230);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

.ctc-19__panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ctc-19__lab {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--mut);
}

.ctc-19__row {
  display: flex;
  flex-wrap: wrap;
}

.ctc-19__chip {
  --c: oklch(0.6 0.14 var(--h,230));
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-height: 44px;
  max-width: 300px;
  padding: 0 9px 0 7px;
  margin: 0 9px 9px 0;
  border-radius: 99px;
  border: 1.5px solid var(--line);
  background: oklch(0.98 0.004 230);
  font-size: 14px;
  font-weight: 650;
  white-space: nowrap;
  overflow: hidden;
  transition: max-width .4s,padding .4s,margin .4s,opacity .3s,scale .3s,border-color .2s;
}

.ctc-19__chip i {
  width: 30px;
  height: 30px;
  flex: none;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-style: normal;
  font-size: 12px;
  font-weight: 800;
  color: oklch(0.99 0 0);
  background: linear-gradient(140deg,oklch(0.66 0.13 var(--h)),oklch(0.48 0.14 calc(var(--h) + 45)));
}

.ctc-19__chip:hover {
  border-color: color-mix(in oklch,var(--c) 45%,var(--line));
}

.ctc-19__chip input {
  appearance: none;
  -webkit-appearance: none;
  position: relative;
  flex: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 0;
  background: color-mix(in oklch,var(--ink) 8%,transparent);
  cursor: pointer;
  transition: background .2s,rotate .25s;
  outline-offset: 2px;
}

.ctc-19__chip input::before,
.ctc-19__chip input::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 10px;
  height: 1.8px;
  border-radius: 2px;
  background: var(--mut);
  translate: -50% -50%;
}

.ctc-19__chip input::before {
  rotate: 45deg;
}

.ctc-19__chip input::after {
  rotate: -45deg;
}

.ctc-19__chip input:hover,
.ctc-19__chip input:focus-visible {
  background: color-mix(in oklch,var(--del) 16%,transparent);
  rotate: 90deg;
}

.ctc-19__chip input:focus-visible {
  outline: 2px solid var(--del);
}

.ctc-19__chip:has(:checked) {
  max-width: 0;
  padding-inline: 0;
  margin: 0;
  opacity: 0;
  scale: .7;
  pointer-events: none;
  border-color: transparent;
}

.ctc-19__reset {
  align-self: flex-start;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 12px;
  border: 1.5px solid var(--line);
  background: var(--panel);
  font: inherit;
  font-size: 13px;
  font-weight: 700;
  color: var(--ink);
  cursor: pointer;
  transition: border-color .2s,color .2s,translate .2s;
}

.ctc-19__reset:hover,
.ctc-19__reset:focus-visible {
  border-color: var(--acc);
  color: var(--acc);
  translate: 0 -1px;
}

.ctc-19__reset:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ctc-19__toasts {
  position: absolute;
  left: 50%;
  bottom: 22px;
  translate: -50% 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: min(400px,calc(100% - 32px));
  pointer-events: none;
  z-index: 5;
}

.ctc-19__toast {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  overflow: hidden;
  padding: 13px 16px;
  border-radius: 14px;
  background: oklch(0.23 0.02 240);
  color: oklch(0.96 0.005 230);
  box-shadow: 0 16px 40px -14px oklch(0.15 0.02 240/.6);
  opacity: 0;
  translate: 0 16px;
  scale: .96;
  pointer-events: none;
  max-height: 0;
  padding-block: 0;
  margin: 0;
  transition: opacity .35s,translate .35s cubic-bezier(.34,1.3,.64,1),scale .35s,max-height .35s,padding .35s;
}

.ctc-19__toast b {
  font-size: 13px;
  font-weight: 650;
}

.ctc-19__toast label {
  min-height: 32px;
  display: inline-flex;
  align-items: center;
  padding: 0 12px;
  border-radius: 9px;
  background: oklch(1 0 0/.12);
  color: oklch(0.85 0.1 230);
  font-size: 12.5px;
  font-weight: 800;
  letter-spacing: .02em;
  cursor: pointer;
  transition: background .2s;
}

.ctc-19__toast label:hover {
  background: oklch(1 0 0/.22);
}

.ctc-19__toast i {
  position: absolute;
  left: 0;
  bottom: 0;
  height: 2.5px;
  width: 100%;
  background: var(--acc);
  transform-origin: left;
}

.ctc-19__stage:has(#ctc19-figma:checked) .ctc-19__toast[data-for="figma"],
.ctc-19__stage:has(#ctc19-slack:checked) .ctc-19__toast[data-for="slack"],
.ctc-19__stage:has(#ctc19-linear:checked) .ctc-19__toast[data-for="linear"],
.ctc-19__stage:has(#ctc19-notion:checked) .ctc-19__toast[data-for="notion"],
.ctc-19__stage:has(#ctc19-github:checked) .ctc-19__toast[data-for="github"] {
  opacity: 1;
  translate: 0 0;
  scale: 1;
  pointer-events: auto;
  max-height: 70px;
  padding-block: 13px;
}

.ctc-19__stage:has(#ctc19-figma:checked) .ctc-19__toast[data-for="figma"] i,
.ctc-19__stage:has(#ctc19-slack:checked) .ctc-19__toast[data-for="slack"] i,
.ctc-19__stage:has(#ctc19-linear:checked) .ctc-19__toast[data-for="linear"] i,
.ctc-19__stage:has(#ctc19-notion:checked) .ctc-19__toast[data-for="notion"] i,
.ctc-19__stage:has(#ctc19-github:checked) .ctc-19__toast[data-for="github"] i {
  animation: ctc19-drain 5s linear forwards;
}

@keyframes ctc19-drain {
  from {
    scale: 1 1;
  }

  to {
    scale: 0 1;
  }
}

.ctc-19__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid var(--acc);
  padding-left: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .ctc-19 * {
    transition-duration: .01ms !important;
    animation-duration: .01ms !important;
  }
}
```
