---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/retro-windows-95-ui-css-template/"
title: "Windows 95 Desktop Interface"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "A full desktop: icon field, taskbar with a working Start menu, a window with title bar and system buttons, and a modal-style dialog."
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Windows 95 Desktop Interface
Source: https://codefronts.com/design-styles/css-retro-designs/retro-windows-95-ui-css-template/

A full desktop: icon field, taskbar with a working Start menu, a window with title bar and system buttons, and a modal-style dialog. Every raised and sunken edge is the four-inset bevel rather than an ad-hoc border, so the whole interface scales from one bevel unit and the pressed states are geometrically correct rather than approximated.
## HTML
```html
<section class="rt-09" aria-labelledby="rt-09-title">
  <h2 class="rt-09__sr" id="rt-09-title">Windows 95 style desktop interface</h2>

  <div class="rt-09__theme">
    <input class="rt-09__theme-input" type="checkbox" id="rt-09-theme">
    <label class="rt-09__theme-label" for="rt-09-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-09__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-09__desk">
    <ul class="rt-09__icons">
      <li><button class="rt-09__icon" type="button"><span class="rt-09__gl rt-09__gl--pc" aria-hidden="true"></span>My Computer</button></li>
      <li><button class="rt-09__icon" type="button"><span class="rt-09__gl rt-09__gl--net" aria-hidden="true"></span>Network</button></li>
      <li><button class="rt-09__icon" type="button"><span class="rt-09__gl rt-09__gl--bin" aria-hidden="true"></span>Recycle Bin</button></li>
    </ul>

    <div class="rt-09__win">
      <div class="rt-09__cap">
        <span class="rt-09__cap-ic" aria-hidden="true"></span>
        <span class="rt-09__cap-t">Program Manager</span>
        <span class="rt-09__cap-b">
          <button class="rt-09__sys" type="button" aria-label="Minimise"><i class="rt-09__sg rt-09__sg--min" aria-hidden="true"></i></button>
          <button class="rt-09__sys" type="button" aria-label="Maximise"><i class="rt-09__sg rt-09__sg--max" aria-hidden="true"></i></button>
          <button class="rt-09__sys" type="button" aria-label="Close"><i class="rt-09__sg rt-09__sg--cls" aria-hidden="true"></i></button>
        </span>
      </div>
      <nav class="rt-09__mb" aria-label="Program Manager menu">
        <ul>
          <li><button type="button"><u>F</u>ile</button></li>
          <li><button type="button"><u>E</u>dit</button></li>
          <li><button type="button"><u>V</u>iew</button></li>
          <li><button type="button"><u>H</u>elp</button></li>
        </ul>
      </nav>
      <div class="rt-09__client">
        <ul class="rt-09__tiles">
          <li><span class="rt-09__tile"><i class="rt-09__gl rt-09__gl--doc" aria-hidden="true"></i>Notepad</span></li>
          <li><span class="rt-09__tile"><i class="rt-09__gl rt-09__gl--doc" aria-hidden="true"></i>Paint</span></li>
          <li><span class="rt-09__tile"><i class="rt-09__gl rt-09__gl--doc" aria-hidden="true"></i>Minesweeper</span></li>
          <li><span class="rt-09__tile"><i class="rt-09__gl rt-09__gl--doc" aria-hidden="true"></i>Defrag</span></li>
        </ul>
      </div>
      <div class="rt-09__status">
        <span class="rt-09__well">4 objects</span>
        <span class="rt-09__well">Memory: 71% free</span>
      </div>
    </div>

    <dialog class="rt-09__dlg" open aria-labelledby="rt-09-dlg-t">
      <div class="rt-09__cap rt-09__cap--dlg">
        <span class="rt-09__cap-t" id="rt-09-dlg-t">Confirm File Delete</span>
        <span class="rt-09__cap-b">
          <button class="rt-09__sys" type="button" aria-label="Close dialog"><i class="rt-09__sg rt-09__sg--cls" aria-hidden="true"></i></button>
        </span>
      </div>
      <div class="rt-09__dlg-body">
        <span class="rt-09__warn" aria-hidden="true">?</span>
        <p class="rt-09__dlg-p">Are you sure you want to send AUTOEXEC.BAT to the Recycle Bin?</p>
      </div>
      <div class="rt-09__dlg-btns">
        <button class="rt-09__btn rt-09__btn--def" type="button">Yes</button>
        <button class="rt-09__btn" type="button">No</button>
      </div>
    </dialog>

    <div class="rt-09__taskbar">
      <input class="rt-09__start-cb" type="checkbox" id="rt-09-start">
      <label class="rt-09__start" for="rt-09-start"><span class="rt-09__flag" aria-hidden="true"></span>Start</label>
      <ul class="rt-09__tasks">
        <li><button class="rt-09__task rt-09__task--on" type="button">Program Manager</button></li>
        <li><button class="rt-09__task" type="button">Read Me</button></li>
      </ul>
      <span class="rt-09__tray"><span class="rt-09__tray-ic" aria-hidden="true"></span>11:42</span>

      <nav class="rt-09__menu" aria-label="Start menu">
        <span class="rt-09__banner" aria-hidden="true">Windows 95</span>
        <ul class="rt-09__menu-list">
          <li><button type="button"><i class="rt-09__gl rt-09__gl--doc" aria-hidden="true"></i>Programs</button></li>
          <li><button type="button"><i class="rt-09__gl rt-09__gl--doc" aria-hidden="true"></i>Documents</button></li>
          <li><button type="button"><i class="rt-09__gl rt-09__gl--doc" aria-hidden="true"></i>Settings</button></li>
          <li><button type="button"><i class="rt-09__gl rt-09__gl--doc" aria-hidden="true"></i>Find</button></li>
          <li class="rt-09__menu-sep"></li>
          <li><button type="button"><i class="rt-09__gl rt-09__gl--doc" aria-hidden="true"></i>Shut Down…</button></li>
        </ul>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
.rt-09 {
  --rt-09-b: 2px;
  --rt-09-face: #c0c0c0;
  --rt-09-hi: #ffffff;
  --rt-09-lt: #dfdfdf;
  --rt-09-sh: #808080;
  --rt-09-dk: #000000;
  --rt-09-cap-a: #000080;
  --rt-09-cap-b: #1084d0;
  --rt-09-desktop: #008080;
  --rt-09-sans: system-ui, -apple-system, "Segoe UI", Tahoma, Verdana, Arial, sans-serif;
  --rt-09-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --rt-09-acc: #0a3fa8;
  --rt-09-acc: oklch(40% 0.19 262);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-09-desktop);
  color: #101010;
  font-family: var(--rt-09-sans);
  -webkit-text-size-adjust: 100%;
}

.rt-09 *,
.rt-09 *::before,
.rt-09 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-09 {
    --rt-09-desktop: #06393c;
    --rt-09-desktop: oklch(31% 0.05 197);
  }
}

.rt-09[data-theme="dark"],
.rt-09:has(.rt-09__theme-input:checked) {
  --rt-09-desktop: #06393c;
  --rt-09-desktop: oklch(31% 0.05 197);
}

@media (prefers-color-scheme: light) {
  .rt-09:has(.rt-09__theme-input:checked) {
    --rt-09-desktop: #06393c;
    --rt-09-desktop: oklch(31% 0.05 197);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-09:has(.rt-09__theme-input:checked) {
    --rt-09-desktop: #008080;
  }
}

.rt-09__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.rt-09__theme {
  position: absolute;
  inset-block-start: 0.75rem;
  inset-inline-end: 0.75rem;
  z-index: 20;
}

.rt-09__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-09__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  cursor: pointer;
  background: var(--rt-09-face);
  color: #101010;
  box-shadow: inset var(--rt-09-b) var(--rt-09-b) 0 0 var(--rt-09-hi), inset calc(var(--rt-09-b) * -1) calc(var(--rt-09-b) * -1) 0 0 var(--rt-09-dk), inset calc(var(--rt-09-b) * 2) calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-lt), inset calc(var(--rt-09-b) * -2) calc(var(--rt-09-b) * -2) 0 0 var(--rt-09-sh);
}

.rt-09__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-09__theme-input:focus-visible + .rt-09__theme-label {
  outline: 2px dotted var(--rt-09-dk);
  outline-offset: -6px;
}

.rt-09__desk {
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: 1rem clamp(0.6rem, 0.4rem + 1.5vw, 2rem) calc(56px + 1.5rem);
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
  align-content: start;
  max-inline-size: 76rem;
  margin-inline: auto;
}

.rt-09__icons {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.rt-09__icon {
  inline-size: 88px;
  min-block-size: 88px;
  padding: 0.5rem 0.25rem;
  border: 0;
  cursor: pointer;
  background: transparent;
  color: #ffffff;
  font: inherit;
  font-size: 0.72rem;
  line-height: 1.25;
  display: grid;
  justify-items: center;
  gap: 0.35rem;
  text-shadow: 1px 1px 0 rgba(0,0,0,0.6);
}

.rt-09__icon:focus-visible {
  outline: 2px dotted #ffffff;
  outline-offset: -3px;
}

.rt-09__gl {
  inline-size: 30px;
  block-size: 26px;
  background: #d8d8d0;
  display: block;
}

.rt-09__gl--pc {
  background: linear-gradient(#e8e8e0 60%, #9a9a92 60%);
  clip-path: polygon(6% 0, 94% 0, 94% 62%, 66% 62%, 72% 80%, 28% 80%, 34% 62%, 6% 62%);
}

.rt-09__gl--net {
  background: #cfd6de;
  clip-path: polygon(0 20%, 46% 20%, 46% 0, 100% 0, 100% 62%, 54% 62%, 54% 82%, 0 82%);
}

.rt-09__gl--bin {
  background: linear-gradient(#cfd2cf, #8f938f);
  clip-path: polygon(18% 12%, 82% 12%, 74% 100%, 26% 100%);
}

.rt-09__gl--doc {
  inline-size: 18px;
  block-size: 18px;
  background: #f4f4ee;
  clip-path: polygon(0 0, 70% 0, 100% 26%, 100% 100%, 0 100%);
  border: 0;
  flex: none;
}

.rt-09__win,
.rt-09__dlg {
  min-inline-size: 0;
  background: var(--rt-09-face);
  padding: 3px;
  border: 0;
  color: #101010;
  box-shadow: inset var(--rt-09-b) var(--rt-09-b) 0 0 var(--rt-09-hi), inset calc(var(--rt-09-b) * -1) calc(var(--rt-09-b) * -1) 0 0 var(--rt-09-dk), inset calc(var(--rt-09-b) * 2) calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-lt), inset calc(var(--rt-09-b) * -2) calc(var(--rt-09-b) * -2) 0 0 var(--rt-09-sh);
}

.rt-09__dlg {
  position: static;
  margin: 0;
  max-inline-size: 30rem;
}

.rt-09__cap {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  margin: 3px;
  padding: 0.25rem 0.25rem 0.25rem 0.5rem;
  min-inline-size: 0;
  background: linear-gradient(90deg, var(--rt-09-cap-a), var(--rt-09-cap-b));
}

.rt-09__cap-ic {
  inline-size: 16px;
  block-size: 16px;
  flex: none;
  background: #f4f4ee;
  clip-path: polygon(0 0, 70% 0, 100% 26%, 100% 100%, 0 100%);
}

.rt-09__cap-t {
  flex: 1 1 auto;
  min-inline-size: 0;
  color: #ffffff;
  font-size: 0.85rem;
  font-weight: 700;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.rt-09__cap-b {
  display: flex;
  gap: 2px;
  flex: none;
}

.rt-09__sys {
  inline-size: 44px;
  block-size: 44px;
  padding: 0;
  border: 0;
  cursor: pointer;
  display: grid;
  place-items: center;
  background: var(--rt-09-face);
  box-shadow: inset var(--rt-09-b) var(--rt-09-b) 0 0 var(--rt-09-hi), inset calc(var(--rt-09-b) * -1) calc(var(--rt-09-b) * -1) 0 0 var(--rt-09-dk), inset calc(var(--rt-09-b) * 2) calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-lt), inset calc(var(--rt-09-b) * -2) calc(var(--rt-09-b) * -2) 0 0 var(--rt-09-sh);
}

.rt-09__sys:active {
  box-shadow: inset var(--rt-09-b) var(--rt-09-b) 0 0 var(--rt-09-dk), inset calc(var(--rt-09-b) * -1) calc(var(--rt-09-b) * -1) 0 0 var(--rt-09-hi), inset calc(var(--rt-09-b) * 2) calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-sh), inset calc(var(--rt-09-b) * -2) calc(var(--rt-09-b) * -2) 0 0 var(--rt-09-lt);
}

.rt-09__sys:focus-visible {
  outline: 2px dotted var(--rt-09-dk);
  outline-offset: -7px;
}

.rt-09__sg {
  display: block;
  background: #101010;
}

.rt-09__sg--min {
  inline-size: 10px;
  block-size: 3px;
  margin-block-start: 8px;
}

.rt-09__sg--max {
  inline-size: 12px;
  block-size: 10px;
  background: transparent;
  border: 2px solid #101010;
  border-block-start-width: 3px;
}

.rt-09__sg--cls {
  inline-size: 12px;
  block-size: 12px;
  background: transparent;
  background-image: linear-gradient(45deg, transparent 44%, #101010 44% 56%, transparent 56%), linear-gradient(-45deg, transparent 44%, #101010 44% 56%, transparent 56%);
}

.rt-09__mb {
  margin: 0 3px;
  min-inline-size: 0;
}

.rt-09__mb ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
}

.rt-09__mb button {
  min-block-size: 44px;
  min-inline-size: 44px;
  padding-inline: 0.6rem;
  border: 0;
  background: transparent;
  font: inherit;
  font-size: 0.82rem;
  color: #101010;
  cursor: pointer;
}

.rt-09__mb button:hover {
  background: var(--rt-09-cap-a);
  color: #ffffff;
}

.rt-09__mb button:focus-visible {
  outline: 2px dotted var(--rt-09-dk);
  outline-offset: -5px;
}

.rt-09__client {
  margin: 3px;
  padding: 0.75rem;
  background: #ffffff;
  min-inline-size: 0;
  box-shadow: inset var(--rt-09-b) var(--rt-09-b) 0 0 var(--rt-09-sh), inset calc(var(--rt-09-b) * -1) calc(var(--rt-09-b) * -1) 0 0 var(--rt-09-hi), inset calc(var(--rt-09-b) * 2) calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-dk), inset calc(var(--rt-09-b) * -2) calc(var(--rt-09-b) * -2) 0 0 var(--rt-09-lt);
}

.rt-09__tiles {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 8rem), 1fr));
  gap: 0.5rem;
}

.rt-09__tile {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-block-size: 44px;
  padding: 0.4rem 0.5rem;
  font-size: 0.82rem;
  min-inline-size: 0;
}

.rt-09__status {
  display: flex;
  flex-wrap: wrap;
  gap: 3px;
  margin: 3px;
}

.rt-09__well {
  flex: 1 1 8rem;
  min-inline-size: 0;
  padding: 0.4rem 0.6rem;
  font-size: 0.78rem;
  box-shadow: inset 1px 1px 0 0 var(--rt-09-sh), inset -1px -1px 0 0 var(--rt-09-hi);
}

.rt-09__dlg-body {
  display: flex;
  gap: 0.85rem;
  padding: 1rem 0.75rem;
  align-items: flex-start;
  min-inline-size: 0;
}

.rt-09__warn {
  inline-size: 34px;
  block-size: 34px;
  flex: none;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: #000080;
  color: #ffffff;
  font-weight: 700;
  font-size: 1.2rem;
}

.rt-09__dlg-p {
  margin: 0;
  font-size: 0.88rem;
  line-height: 1.5;
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-09__dlg-btns {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  padding: 0 0.75rem 0.85rem;
}

.rt-09__btn {
  min-block-size: 44px;
  min-inline-size: 5.5rem;
  padding: 0.5rem 1rem;
  border: 0;
  cursor: pointer;
  font: inherit;
  font-size: 0.85rem;
  background: var(--rt-09-face);
  color: #101010;
  box-shadow: inset var(--rt-09-b) var(--rt-09-b) 0 0 var(--rt-09-hi), inset calc(var(--rt-09-b) * -1) calc(var(--rt-09-b) * -1) 0 0 var(--rt-09-dk), inset calc(var(--rt-09-b) * 2) calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-lt), inset calc(var(--rt-09-b) * -2) calc(var(--rt-09-b) * -2) 0 0 var(--rt-09-sh);
}

.rt-09__btn:active {
  box-shadow: inset var(--rt-09-b) var(--rt-09-b) 0 0 var(--rt-09-dk), inset calc(var(--rt-09-b) * -1) calc(var(--rt-09-b) * -1) 0 0 var(--rt-09-hi), inset calc(var(--rt-09-b) * 2) calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-sh), inset calc(var(--rt-09-b) * -2) calc(var(--rt-09-b) * -2) 0 0 var(--rt-09-lt);
}

.rt-09__btn:focus-visible {
  outline: 2px dotted var(--rt-09-dk);
  outline-offset: -6px;
}

.rt-09__btn--def {
  box-shadow: inset 0 0 0 1px var(--rt-09-dk), inset var(--rt-09-b) var(--rt-09-b) 0 0 var(--rt-09-hi), inset calc(var(--rt-09-b) * -1) calc(var(--rt-09-b) * -1) 0 0 var(--rt-09-dk), inset calc(var(--rt-09-b) * 2) calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-lt), inset calc(var(--rt-09-b) * -2) calc(var(--rt-09-b) * -2) 0 0 var(--rt-09-sh);
}

.rt-09__taskbar {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  z-index: 15;
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 3px;
  min-block-size: 56px;
  background: var(--rt-09-face);
  min-inline-size: 0;
  box-shadow: inset 0 var(--rt-09-b) 0 0 var(--rt-09-hi), inset 0 calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-lt);
}

.rt-09__start-cb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  margin: 0;
}

.rt-09__start {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  min-block-size: 44px;
  padding: 0.35rem 0.75rem;
  font-weight: 700;
  font-size: 0.88rem;
  cursor: pointer;
  flex: none;
  background: var(--rt-09-face);
  box-shadow: inset var(--rt-09-b) var(--rt-09-b) 0 0 var(--rt-09-hi), inset calc(var(--rt-09-b) * -1) calc(var(--rt-09-b) * -1) 0 0 var(--rt-09-dk), inset calc(var(--rt-09-b) * 2) calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-lt), inset calc(var(--rt-09-b) * -2) calc(var(--rt-09-b) * -2) 0 0 var(--rt-09-sh);
}

.rt-09__start-cb:checked + .rt-09__start {
  box-shadow: inset var(--rt-09-b) var(--rt-09-b) 0 0 var(--rt-09-dk), inset calc(var(--rt-09-b) * -1) calc(var(--rt-09-b) * -1) 0 0 var(--rt-09-hi), inset calc(var(--rt-09-b) * 2) calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-sh), inset calc(var(--rt-09-b) * -2) calc(var(--rt-09-b) * -2) 0 0 var(--rt-09-lt);
}

.rt-09__start-cb:focus-visible + .rt-09__start {
  outline: 2px dotted var(--rt-09-dk);
  outline-offset: -6px;
}

.rt-09__flag {
  inline-size: 18px;
  block-size: 16px;
  flex: none;
  background: linear-gradient(135deg, #ff3b30 0 50%, #ffd60a 50% 100%);
  clip-path: polygon(0 14%, 46% 0, 100% 10%, 100% 88%, 46% 100%, 0 86%);
}

.rt-09__tasks {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  gap: 3px;
  flex: 1 1 auto;
  min-inline-size: 0;
  overflow: hidden;
}

.rt-09__task {
  min-block-size: 44px;
  padding: 0.35rem 0.7rem;
  border: 0;
  cursor: pointer;
  font: inherit;
  font-size: 0.8rem;
  background: var(--rt-09-face);
  color: #101010;
  max-inline-size: 12rem;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  box-shadow: inset var(--rt-09-b) var(--rt-09-b) 0 0 var(--rt-09-hi), inset calc(var(--rt-09-b) * -1) calc(var(--rt-09-b) * -1) 0 0 var(--rt-09-dk), inset calc(var(--rt-09-b) * 2) calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-lt), inset calc(var(--rt-09-b) * -2) calc(var(--rt-09-b) * -2) 0 0 var(--rt-09-sh);
}

.rt-09__task--on {
  font-weight: 700;
  background-color: var(--rt-09-face);
  background-image: repeating-conic-gradient(var(--rt-09-hi) 0% 25%, var(--rt-09-face) 0% 50%);
  background-size: 2px 2px;
  box-shadow: inset var(--rt-09-b) var(--rt-09-b) 0 0 var(--rt-09-dk), inset calc(var(--rt-09-b) * -1) calc(var(--rt-09-b) * -1) 0 0 var(--rt-09-hi), inset calc(var(--rt-09-b) * 2) calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-sh), inset calc(var(--rt-09-b) * -2) calc(var(--rt-09-b) * -2) 0 0 var(--rt-09-lt);
}

.rt-09__task:focus-visible {
  outline: 2px dotted var(--rt-09-dk);
  outline-offset: -6px;
}

.rt-09__tray {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  flex: none;
  min-block-size: 44px;
  padding-inline: 0.6rem;
  font-size: 0.8rem;
  font-variant-numeric: tabular-nums;
  box-shadow: inset 1px 1px 0 0 var(--rt-09-sh), inset -1px -1px 0 0 var(--rt-09-hi);
}

.rt-09__tray-ic {
  inline-size: 14px;
  block-size: 14px;
  background: #6a6a62;
  clip-path: polygon(0 34%, 30% 34%, 62% 6%, 62% 94%, 30% 66%, 0 66%);
}

.rt-09__menu {
  position: absolute;
  inset-block-end: calc(100% + 3px);
  inset-inline-start: 3px;
  inline-size: min(20rem, calc(100vw - 1.5rem));
  display: none;
  background: var(--rt-09-face);
  padding: 3px;
  box-shadow: inset var(--rt-09-b) var(--rt-09-b) 0 0 var(--rt-09-hi), inset calc(var(--rt-09-b) * -1) calc(var(--rt-09-b) * -1) 0 0 var(--rt-09-dk), inset calc(var(--rt-09-b) * 2) calc(var(--rt-09-b) * 2) 0 0 var(--rt-09-lt), inset calc(var(--rt-09-b) * -2) calc(var(--rt-09-b) * -2) 0 0 var(--rt-09-sh);
}

.rt-09:has(.rt-09__start-cb:checked) .rt-09__menu {
  display: flex;
}

.rt-09__banner {
  flex: none;
  inline-size: 30px;
  background: linear-gradient(180deg, #000080, #1084d0);
  color: #ffffff;
  font-weight: 700;
  font-size: 0.9rem;
  letter-spacing: 0.04em;
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  display: grid;
  align-items: end;
  justify-items: center;
  padding-block: 0.6rem;
}

.rt-09__menu-list {
  list-style: none;
  margin: 0;
  padding: 0.2rem;
  flex: 1 1 auto;
  min-inline-size: 0;
}

.rt-09__menu-list button {
  inline-size: 100%;
  min-block-size: 44px;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.4rem 0.6rem;
  border: 0;
  background: transparent;
  font: inherit;
  font-size: 0.88rem;
  color: #101010;
  cursor: pointer;
  text-align: start;
}

.rt-09__menu-list button:hover {
  background: var(--rt-09-cap-a);
  color: #ffffff;
}

.rt-09__menu-list button:focus-visible {
  outline: 2px dotted var(--rt-09-dk);
  outline-offset: -5px;
}

.rt-09__menu-sep {
  block-size: 2px;
  margin: 0.3rem 0.4rem;
  box-shadow: inset 0 1px 0 0 var(--rt-09-sh), inset 0 -1px 0 0 var(--rt-09-hi);
}

@media (min-width: 56rem) {
  .rt-09__desk {
    grid-template-columns: 7rem minmax(0, 1fr);
    align-items: start;
  }

  .rt-09__icons {
    flex-direction: column;
  }

  .rt-09__dlg {
    grid-column: 2;
    justify-self: start;
  }
}
```
