---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/settings-profile-preferences-panel/"
title: "Settings / Profile Preferences Panel"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A tabbed preferences modal with a vertical nav separating Account, Appearance and Notifications — theme radios, custom toggle switches and clean form rows."
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Settings / Profile Preferences Panel
Source: https://codefronts.com/components/css-modals/settings-profile-preferences-panel/

A tabbed preferences modal with a vertical nav separating Account, Appearance and Notifications — theme radios, custom toggle switches and clean form rows. The settings surface, with pure-CSS tab switching and native focus management.
## HTML
```html
<div class="cm-17">
  <button class="cm-17__open" type="button"><span aria-hidden="true">⚙</span> Settings</button>

  <dialog class="cm-17__dlg" aria-labelledby="cm-17-title">
    <div class="cm-17__card">
      <input type="radio" name="cm-17-tab" id="cm-17-account" class="cm-17__r" checked>
      <input type="radio" name="cm-17-tab" id="cm-17-appear" class="cm-17__r">
      <input type="radio" name="cm-17-tab" id="cm-17-notif" class="cm-17__r">

      <button class="cm-17__x" type="button" aria-label="Close settings">&times;</button>
      <nav class="cm-17__nav" aria-label="Settings sections">
        <h2 id="cm-17-title" class="cm-17__brand">Settings</h2>
        <label for="cm-17-account" class="cm-17__tab"><span aria-hidden="true">👤</span> Account</label>
        <label for="cm-17-appear" class="cm-17__tab"><span aria-hidden="true">🎨</span> Appearance</label>
        <label for="cm-17-notif" class="cm-17__tab"><span aria-hidden="true">🔔</span> Notifications</label>
      </nav>

      <div class="cm-17__panels">
        <section class="cm-17__panel cm-17__panel--account">
          <h3>Account</h3>
          <div class="cm-17__field"><label for="cm-17-dn">Display name</label><input id="cm-17-dn" type="text" value="Alex Rivera"></div>
          <div class="cm-17__field"><label for="cm-17-em">Email</label><input id="cm-17-em" type="email" value="[email protected]"></div>
          <div class="cm-17__field"><label for="cm-17-tz">Time zone</label>
            <select id="cm-17-tz"><option>GMT−05:00 · New York</option><option>GMT+00:00 · London</option><option>GMT+05:30 · Mumbai</option></select></div>
        </section>
        <section class="cm-17__panel cm-17__panel--appear">
          <h3>Appearance</h3>
          <p class="cm-17__lbl">Theme</p>
          <div class="cm-17__themes">
            <label class="cm-17__theme"><input type="radio" name="cm-17-th" checked><span class="cm-17__sw2 cm-17__sw2--dark"></span>Dark</label>
            <label class="cm-17__theme"><input type="radio" name="cm-17-th"><span class="cm-17__sw2 cm-17__sw2--light"></span>Light</label>
            <label class="cm-17__theme"><input type="radio" name="cm-17-th"><span class="cm-17__sw2 cm-17__sw2--auto"></span>System</label>
          </div>
          <label class="cm-17__toggle"><span>Reduce motion</span><input type="checkbox"></label>
          <label class="cm-17__toggle"><span>Compact density</span><input type="checkbox" checked></label>
        </section>
        <section class="cm-17__panel cm-17__panel--notif">
          <h3>Notifications</h3>
          <label class="cm-17__toggle"><span>Product updates<small>New features &amp; releases</small></span><input type="checkbox" checked></label>
          <label class="cm-17__toggle"><span>Mentions &amp; replies<small>When someone tags you</small></span><input type="checkbox" checked></label>
          <label class="cm-17__toggle"><span>Weekly digest<small>A Monday summary email</small></span><input type="checkbox"></label>
          <label class="cm-17__toggle"><span>Marketing<span></span></span><input type="checkbox"></label>
        </section>
      </div>
    </div>
  </dialog>
</div>
```
## CSS
```css
.cm-17,
.cm-17 *,
.cm-17 *::before,
.cm-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-17 {
  --accent: oklch(0.72 0.15 285);
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#100e16,#08070b);
}

.cm-17__open {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  cursor: pointer;
  padding: 13px 24px;
  border-radius: 11px;
  color: #eae7f8;
  font: 600 14px system-ui;
  border: 1px solid #2a2740;
  background: #141222;
  transition: border-color .2s,background .2s;
}

.cm-17__open:hover {
  border-color: var(--accent);
  background: #1a1730;
}

.cm-17__open:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-17__dlg {
  margin: auto;
  width: min(620px,94vw);
  padding: 0;
  border: none;
  border-radius: 18px;
  color: #e8e6f2;
  background: linear-gradient(180deg,#14121e,#0f0d17);
  box-shadow: 0 40px 90px -30px #000,0 0 0 1px #272340;
  max-block-size: 90dvh;
  overflow: hidden;
  opacity: 0;
  transform: scale(.97);
  transition: opacity .26s,transform .26s,overlay .26s allow-discrete,display .26s allow-discrete;
}

.cm-17__dlg[open] {
  opacity: 1;
  transform: none;
}

@starting-style {
  .cm-17__dlg[open] {
    opacity: 0;
    transform: scale(.97);
  }
}

.cm-17__dlg::backdrop {
  background: rgba(6,5,9,0);
  backdrop-filter: blur(0);
  transition: background .3s,backdrop-filter .3s,overlay .3s allow-discrete,display .3s allow-discrete;
}

.cm-17__dlg[open]::backdrop {
  background: rgba(6,5,9,.64);
  backdrop-filter: blur(5px);
}

@starting-style {
  .cm-17__dlg[open]::backdrop {
    background: rgba(6,5,9,0);
    backdrop-filter: blur(0);
  }
}

.cm-17__card {
  position: relative;
  display: grid;
  grid-template-columns: 190px 1fr;
  min-height: 420px;
}

.cm-17__r {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cm-17__x {
  position: absolute;
  top: 12px;
  right: 14px;
  z-index: 3;
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #8b86a4;
  font-size: 22px;
  cursor: pointer;
}

.cm-17__x:hover {
  background: #221d33;
  color: #fff;
}

.cm-17__x:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-17__nav {
  padding: 24px 14px;
  border-right: 1px solid #241f38;
  background: #100e1a;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.cm-17__brand {
  font-size: 13px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #8781a2;
  padding: 0 12px;
  margin-bottom: 14px;
}

.cm-17__tab {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 11px 12px;
  border-radius: 9px;
  font: 600 14px system-ui;
  color: #b3aecb;
  cursor: pointer;
  transition: background .18s,color .18s;
}

.cm-17__tab:hover {
  background: #191627;
  color: #e6e2f5;
}

#cm-17-account:checked~.cm-17__nav .cm-17__tab[for="cm-17-account"],
#cm-17-appear:checked~.cm-17__nav .cm-17__tab[for="cm-17-appear"],
#cm-17-notif:checked~.cm-17__nav .cm-17__tab[for="cm-17-notif"] {
  background: color-mix(in oklch,var(--accent) 20%,#191627);
  color: #fff;
}

.cm-17__r:focus-visible~.cm-17__nav .cm-17__tab {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.cm-17__panels {
  padding: 28px 30px;
  overflow: auto;
}

.cm-17__panel {
  display: none;
  animation: cm-17-fade .25s ease;
}

@keyframes cm-17-fade {
  from {
    opacity: 0;
    transform: translateY(6px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

#cm-17-account:checked~.cm-17__panels .cm-17__panel--account,
#cm-17-appear:checked~.cm-17__panels .cm-17__panel--appear,
#cm-17-notif:checked~.cm-17__panels .cm-17__panel--notif {
  display: block;
}

.cm-17__panel h3 {
  font-size: 18px;
  font-weight: 700;
  color: #f2eefb;
  margin-bottom: 20px;
}

.cm-17__field {
  display: flex;
  flex-direction: column;
  gap: 7px;
  margin-bottom: 16px;
}

.cm-17__field label {
  font-size: 12.5px;
  font-weight: 600;
  color: #a8a3c2;
}

.cm-17__field input,
.cm-17__field select {
  width: 100%;
  padding: 11px 13px;
  border-radius: 10px;
  border: 1px solid #2c2842;
  background: #0d0b16;
  color: #eeecf7;
  font: 14px system-ui;
  transition: border-color .2s,box-shadow .2s;
}

.cm-17__field input:focus,
.cm-17__field select:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--accent) 24%,transparent);
}

.cm-17__lbl {
  font-size: 12.5px;
  font-weight: 600;
  color: #a8a3c2;
  margin-bottom: 12px;
}

.cm-17__themes {
  display: flex;
  gap: 12px;
  margin-bottom: 24px;
}

.cm-17__theme {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 9px;
  padding: 14px 8px;
  border-radius: 12px;
  border: 1px solid #2c2842;
  background: #0d0b16;
  cursor: pointer;
  font: 600 13px system-ui;
  color: #b8b3d0;
  transition: all .18s;
}

.cm-17__theme:has(:checked) {
  border-color: var(--accent);
  color: #fff;
  background: color-mix(in oklch,var(--accent) 14%,#0d0b16);
}

.cm-17__theme:has(:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-17__theme input {
  position: absolute;
  opacity: 0;
}

.cm-17__sw2 {
  width: 100%;
  height: 34px;
  border-radius: 8px;
  border: 1px solid #3a3556;
}

.cm-17__sw2--dark {
  background: #15131f;
}

.cm-17__sw2--light {
  background: #e8e6f0;
}

.cm-17__sw2--auto {
  background: linear-gradient(90deg,#15131f 50%,#e8e6f0 50%);
}

.cm-17__toggle {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 14px 0;
  border-top: 1px solid #211d33;
  cursor: pointer;
}

.cm-17__toggle>span {
  display: flex;
  flex-direction: column;
  gap: 3px;
  font-size: 14px;
  color: #ddd9ec;
}

.cm-17__toggle small {
  font-size: 12px;
  color: #847fa0;
}

.cm-17__toggle input {
  width: 44px;
  height: 25px;
  -webkit-appearance: none;
  appearance: none;
  border-radius: 13px;
  background: #2c2842;
  position: relative;
  cursor: pointer;
  transition: background .2s;
  flex: none;
}

.cm-17__toggle input::after {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 19px;
  height: 19px;
  border-radius: 50%;
  background: #8b86a4;
  transition: transform .2s,background .2s;
}

.cm-17__toggle input:checked {
  background: color-mix(in oklch,var(--accent) 55%,#2c2842);
}

.cm-17__toggle input:checked::after {
  transform: translateX(19px);
  background: #fff;
}

.cm-17__toggle input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 540px) {
  .cm-17__card {
    grid-template-columns: 1fr;
  }

  .cm-17__nav {
    flex-direction: row;
    overflow: auto;
    border-right: none;
    border-bottom: 1px solid #241f38;
  }

  .cm-17__brand {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cm-17__dlg,
    .cm-17__dlg::backdrop {
    transition-duration: .001s;
  }

  .cm-17__panel {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-17');
  var dlg = root.querySelector('.cm-17__dlg');
  root.querySelector('.cm-17__open').addEventListener('click', function(){ dlg.showModal(); });
  root.querySelector('.cm-17__x').addEventListener('click', function(){ dlg.close(); });
  dlg.addEventListener('click', function(e){
    var c = dlg.querySelector('.cm-17__card').getBoundingClientRect();
    if(e.clientX < c.left || e.clientX > c.right || e.clientY < c.top || e.clientY > c.bottom) dlg.close();
  });
})();
```
