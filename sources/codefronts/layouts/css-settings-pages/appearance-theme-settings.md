---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/appearance-theme-settings/"
title: "Appearance and Theme Settings"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A live appearance panel with zero JavaScript: pick Light, Dark or System theme from mini window previews and the entire page re-themes instantly with the CSS…"
has_js: "false"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Appearance and Theme Settings
Source: https://codefronts.com/layouts/css-settings-pages/appearance-theme-settings/

A live appearance panel with zero JavaScript: pick Light, Dark or System theme from mini window previews and the entire page re-themes instantly with the CSS light-dark() function; choose an accent colour, interface density, text size and corner style, or switch on high contrast — every change applies to a live preview app beside the controls. All state is native radios and checkboxes read by :has().
## HTML
```html
<section class="csp-14">
  <div class="csp-14__wrap">
    <header class="csp-14__head"><h1>Appearance</h1><p>Customise how the workspace looks on this device.</p></header>
    <div class="csp-14__grid">
      <div class="csp-14__controls">
        <fieldset class="csp-14__group">
          <legend>Theme</legend>
          <div class="csp-14__themes">
            <label class="csp-14__theme"><input type="radio" name="csp14-t" id="csp14-light" checked><span class="csp-14__mini csp-14__mini--light"><i></i><i></i><i></i></span><b>Light</b></label>
            <label class="csp-14__theme"><input type="radio" name="csp14-t" id="csp14-dark"><span class="csp-14__mini csp-14__mini--dark"><i></i><i></i><i></i></span><b>Dark</b></label>
            <label class="csp-14__theme"><input type="radio" name="csp14-t" id="csp14-system"><span class="csp-14__mini csp-14__mini--sys"><i></i><i></i><i></i></span><b>System</b></label>
          </div>
        </fieldset>
        <fieldset class="csp-14__group">
          <legend>Accent colour</legend>
          <div class="csp-14__swatches">
            <label style="--c:oklch(0.55 0.21 265)"><input type="radio" name="csp14-a" id="csp14-a1" checked><span class="csp-14__sr">Indigo</span></label>
            <label style="--c:oklch(0.6 0.2 300)"><input type="radio" name="csp14-a" id="csp14-a2"><span class="csp-14__sr">Violet</span></label>
            <label style="--c:oklch(0.6 0.16 155)"><input type="radio" name="csp14-a" id="csp14-a3"><span class="csp-14__sr">Green</span></label>
            <label style="--c:oklch(0.68 0.17 55)"><input type="radio" name="csp14-a" id="csp14-a4"><span class="csp-14__sr">Amber</span></label>
            <label style="--c:oklch(0.6 0.21 15)"><input type="radio" name="csp14-a" id="csp14-a5"><span class="csp-14__sr">Rose</span></label>
            <label style="--c:oklch(0.6 0.13 215)"><input type="radio" name="csp14-a" id="csp14-a6"><span class="csp-14__sr">Teal</span></label>
          </div>
        </fieldset>
        <fieldset class="csp-14__group csp-14__row">
          <legend>Density</legend>
          <div class="csp-14__seg"><input type="radio" name="csp14-d" id="csp14-comfy" checked><label for="csp14-comfy">Comfortable</label><input type="radio" name="csp14-d" id="csp14-compact"><label for="csp14-compact">Compact</label></div>
        </fieldset>
        <fieldset class="csp-14__group csp-14__row">
          <legend>Text size</legend>
          <div class="csp-14__seg"><input type="radio" name="csp14-f" id="csp14-fs"><label for="csp14-fs" style="font-size:12px">Aa</label><input type="radio" name="csp14-f" id="csp14-fm" checked><label for="csp14-fm" style="font-size:14px">Aa</label><input type="radio" name="csp14-f" id="csp14-fl"><label for="csp14-fl" style="font-size:17px">Aa</label></div>
        </fieldset>
        <fieldset class="csp-14__group csp-14__row">
          <legend>Corners</legend>
          <div class="csp-14__seg"><input type="radio" name="csp14-r" id="csp14-r0"><label for="csp14-r0">Sharp</label><input type="radio" name="csp14-r" id="csp14-r1" checked><label for="csp14-r1">Rounded</label><input type="radio" name="csp14-r" id="csp14-r2"><label for="csp14-r2">Soft</label></div>
        </fieldset>
        <label class="csp-14__group csp-14__row csp-14__toggle"><span><b>High contrast</b><small>Stronger borders and text</small></span><input type="checkbox" id="csp14-hc" role="switch"></label>
      </div>

      <div class="csp-14__previewwrap">
        <span class="csp-14__plabel">Live preview</span>
        <div class="csp-14__preview" aria-hidden="true">
          <aside class="csp-14__side"><span class="csp-14__brand"></span><i class="is-on"></i><i></i><i></i><i></i></aside>
          <div class="csp-14__main">
            <div class="csp-14__ptitle">Q4 launch plan</div>
            <div class="csp-14__ptext">Ship the new onboarding before Thanksgiving and measure activation weekly.</div>
            <div class="csp-14__pcard"><span class="csp-14__pchk"></span><span>Finalise pricing page copy</span><em>Today</em></div>
            <div class="csp-14__pcard"><span class="csp-14__pchk is-on"></span><span>Record product walkthrough</span><em>Done</em></div>
            <div class="csp-14__pbtns"><span class="csp-14__pbtn">Create task</span><span class="csp-14__pbtn csp-14__pbtn--ghost">Share</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.csp-14,
.csp-14 *,
.csp-14 *::before,
.csp-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-14 {
  color-scheme: light;
  --acc: oklch(0.55 0.21 265);
  --pad: 14px;
  --gap: 10px;
  --fs: 14px;
  --r: 12px;
  --bg: light-dark(oklch(0.975 0.004 270),oklch(0.15 0.01 270));
  --surface: light-dark(#fff,oklch(0.2 0.012 270));
  --sunk: light-dark(oklch(0.96 0.005 270),oklch(0.17 0.01 270));
  --ink: light-dark(oklch(0.22 0.02 270),oklch(0.95 0.006 270));
  --muted: light-dark(oklch(0.5 0.02 270),oklch(0.7 0.015 270));
  --line: light-dark(oklch(0.91 0.008 270),oklch(0.3 0.014 270));
  container-type: inline-size;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 22px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--ink);
  transition: background .3s,color .3s;
  width: 100%;
}

.csp-14:has(#csp14-dark:checked) {
  color-scheme: dark;
}

.csp-14:has(#csp14-system:checked) {
  color-scheme: light dark;
}

.csp-14:has(#csp14-a2:checked) {
  --acc: oklch(0.6 0.2 300);
}

.csp-14:has(#csp14-a3:checked) {
  --acc: oklch(0.6 0.16 155);
}

.csp-14:has(#csp14-a4:checked) {
  --acc: oklch(0.68 0.17 55);
}

.csp-14:has(#csp14-a5:checked) {
  --acc: oklch(0.6 0.21 15);
}

.csp-14:has(#csp14-a6:checked) {
  --acc: oklch(0.6 0.13 215);
}

.csp-14:has(#csp14-compact:checked) {
  --pad: 9px;
  --gap: 6px;
}

.csp-14:has(#csp14-fs:checked) {
  --fs: 12.5px;
}

.csp-14:has(#csp14-fl:checked) {
  --fs: 16.5px;
}

.csp-14:has(#csp14-r0:checked) {
  --r: 3px;
}

.csp-14:has(#csp14-r2:checked) {
  --r: 20px;
}

.csp-14:has(#csp14-hc:checked) {
  --line: light-dark(oklch(0.45 0.02 270),oklch(0.7 0.02 270));
  --muted: light-dark(oklch(0.3 0.02 270),oklch(0.88 0.01 270));
}

.csp-14__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.csp-14__wrap {
  max-width: 1000px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.csp-14__head h1 {
  font: 700 30px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-14__head p {
  font: 400 14.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
}

.csp-14__grid {
  display: grid;
  grid-template-columns: minmax(0,1fr) minmax(0,1.05fr);
  gap: 24px;
  align-items: start;
}

.csp-14__controls {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--surface);
  overflow: hidden;
  transition: background .3s,border-color .3s;
}

.csp-14__group {
  border: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 18px 20px;
}

.csp-14__group+.csp-14__group {
  border-top: 1px solid var(--line);
}

.csp-14__group legend {
  float: left;
  font: 600 13.5px/1 system-ui,sans-serif;
  margin-bottom: 12px;
}

.csp-14__row {
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
}

.csp-14__row legend {
  float: none;
  margin: 0;
  padding: 0;
}

.csp-14__themes {
  clear: both;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 10px;
}

.csp-14__theme {
  display: flex;
  flex-direction: column;
  gap: 8px;
  cursor: pointer;
}

.csp-14__theme input,
.csp-14__swatches input,
.csp-14__seg input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.csp-14__theme b {
  font: 550 13px/1 system-ui,sans-serif;
  text-align: center;
}

.csp-14__mini {
  position: relative;
  display: grid;
  grid-template-columns: 28% 1fr;
  grid-template-rows: auto 1fr;
  gap: 4px;
  aspect-ratio: 1.45;
  padding: 6px;
  border-radius: 12px;
  border: 2px solid var(--line);
  overflow: hidden;
  transition: border-color .2s,box-shadow .2s;
}

.csp-14__mini i {
  border-radius: 4px;
}

.csp-14__mini i:nth-child(1) {
  grid-row: span 2;
}

.csp-14__mini i:nth-child(2) {
  height: 8px;
}

.csp-14__mini--light {
  background: #f3f4f7;
}

.csp-14__mini--light i:nth-child(1) {
  background: #e3e5ec;
}

.csp-14__mini--light i:nth-child(2) {
  background: var(--acc);
}

.csp-14__mini--light i:nth-child(3) {
  background: #fff;
}

.csp-14__mini--dark {
  background: #15171d;
}

.csp-14__mini--dark i:nth-child(1) {
  background: #22252e;
}

.csp-14__mini--dark i:nth-child(2) {
  background: var(--acc);
}

.csp-14__mini--dark i:nth-child(3) {
  background: #1d2028;
}

.csp-14__mini--sys {
  background: linear-gradient(135deg,#f3f4f7 50%,#15171d 50%);
}

.csp-14__mini--sys i:nth-child(1) {
  background: #e3e5ec;
}

.csp-14__mini--sys i:nth-child(2) {
  background: var(--acc);
}

.csp-14__mini--sys i:nth-child(3) {
  background: linear-gradient(135deg,#fff 50%,#1d2028 50%);
}

.csp-14__theme:has(input:checked) .csp-14__mini {
  border-color: var(--acc);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--acc) 25%,transparent);
}

.csp-14__theme:has(input:focus-visible) .csp-14__mini {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.csp-14__swatches {
  clear: both;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.csp-14__swatches label {
  display: grid;
  place-items: center;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--c);
  cursor: pointer;
  box-shadow: inset 0 0 0 1px oklch(0 0 0/.1);
  transition: scale .15s,box-shadow .2s;
}

.csp-14__swatches label:hover {
  scale: 1.08;
}

.csp-14__swatches label:has(input:checked) {
  box-shadow: 0 0 0 3px var(--surface),0 0 0 5px var(--c);
}

.csp-14__swatches label:has(input:checked)::after {
  content: "";
  width: 12px;
  height: 7px;
  border: solid #fff;
  border-width: 0 0 2.2px 2.2px;
  rotate: -45deg;
  translate: 0 -2px;
}

.csp-14__swatches label:has(input:focus-visible) {
  outline: 2px solid var(--ink);
  outline-offset: 5px;
}

.csp-14__seg {
  display: flex;
  padding: 3px;
  border-radius: 11px;
  background: var(--sunk);
  border: 1px solid var(--line);
}

.csp-14__seg label {
  min-height: 34px;
  display: grid;
  place-items: center;
  padding: 0 12px;
  border-radius: 8px;
  font: 600 13px/1 system-ui,sans-serif;
  color: var(--muted);
  cursor: pointer;
  transition: all .15s;
}

.csp-14__seg input:checked+label {
  color: var(--ink);
  background: var(--surface);
  box-shadow: 0 1px 3px oklch(0 0 0/.12);
}

.csp-14__seg input:focus-visible+label {
  outline: 2px solid var(--acc);
}

.csp-14__toggle {
  cursor: pointer;
}

.csp-14__toggle b {
  display: block;
  font: 600 13.5px/1.2 system-ui,sans-serif;
}

.csp-14__toggle small {
  display: block;
  margin-top: 3px;
  font: 400 12.5px/1.3 system-ui,sans-serif;
  color: var(--muted);
}

.csp-14__toggle input {
  appearance: none;
  position: relative;
  width: 42px;
  height: 24px;
  border-radius: 999px;
  background: var(--line);
  cursor: pointer;
  transition: background .2s;
}

.csp-14__toggle input::before {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 3px oklch(0 0 0/.3);
  transition: translate .2s;
}

.csp-14__toggle input:checked {
  background: var(--acc);
}

.csp-14__toggle input:checked::before {
  translate: 18px 0;
}

.csp-14__toggle input:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.csp-14__previewwrap {
  position: sticky;
  top: 24px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.csp-14__plabel {
  font: 600 11px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.csp-14__preview {
  display: grid;
  grid-template-columns: 64px 1fr;
  min-height: 360px;
  border: 1px solid var(--line);
  border-radius: calc(var(--r) + 6px);
  background: var(--surface);
  overflow: hidden;
  box-shadow: 0 30px 60px -40px oklch(0.2 0.05 270/.6);
  font-size: var(--fs);
  transition: all .3s;
}

.csp-14__side {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--gap);
  padding: var(--pad) 0;
  background: var(--sunk);
  border-right: 1px solid var(--line);
}

.csp-14__brand {
  width: 30px;
  height: 30px;
  margin-bottom: 8px;
  border-radius: calc(var(--r) * .7);
  background: var(--acc);
}

.csp-14__side i {
  width: 30px;
  height: 30px;
  border-radius: calc(var(--r) * .7);
  background: color-mix(in oklab,var(--ink) 8%,transparent);
}

.csp-14__side i.is-on {
  background: color-mix(in oklab,var(--acc) 22%,transparent);
  box-shadow: inset 0 0 0 1.5px var(--acc);
}

.csp-14__main {
  display: flex;
  flex-direction: column;
  gap: var(--gap);
  padding: calc(var(--pad) * 1.5);
}

.csp-14__ptitle {
  font: 700 1.45em/1.15 system-ui,sans-serif;
  letter-spacing: -.02em;
}

.csp-14__ptext {
  font: 400 1em/1.55 system-ui,sans-serif;
  color: var(--muted);
  margin-bottom: 6px;
}

.csp-14__pcard {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: var(--pad);
  border: 1px solid var(--line);
  border-radius: var(--r);
  font: 500 .95em/1.3 system-ui,sans-serif;
  transition: all .3s;
}

.csp-14__pcard span:nth-child(2) {
  flex: 1;
}

.csp-14__pcard em {
  font-style: normal;
  font-size: .82em;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 999px;
  color: var(--acc);
  background: color-mix(in oklab,var(--acc) 14%,transparent);
}

.csp-14__pchk {
  width: 18px;
  height: 18px;
  border-radius: calc(var(--r) * .4);
  border: 1.5px solid var(--line);
}

.csp-14__pchk.is-on {
  background: var(--acc);
  border-color: var(--acc);
}

.csp-14__pbtns {
  display: flex;
  gap: 8px;
  margin-top: 6px;
}

.csp-14__pbtn {
  padding: calc(var(--pad) * .7) calc(var(--pad) * 1.2);
  border-radius: var(--r);
  font: 600 .95em/1 system-ui,sans-serif;
  color: #fff;
  background: var(--acc);
  transition: all .3s;
}

.csp-14__pbtn--ghost {
  color: var(--ink);
  background: transparent;
  border: 1px solid var(--line);
}

@container (max-width: 760px) {
  .csp-14__grid {
    grid-template-columns: minmax(0,1fr);
  }

  .csp-14__previewwrap {
    position: static;
    order: -1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-14,
    .csp-14 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript by design — light-dark(), color-scheme and :has() drive every setting. */
```
