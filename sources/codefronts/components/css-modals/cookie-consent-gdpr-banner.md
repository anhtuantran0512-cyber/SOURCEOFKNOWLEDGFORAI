---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/cookie-consent-gdpr-banner/"
title: "Cookie Consent / GDPR Banner"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A corner cookie sheet with Accept all, Reject all and an expandable Preferences panel of per-category toggles — semantic, keyboard-friendly and…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cookie Consent / GDPR Banner
Source: https://codefronts.com/components/css-modals/cookie-consent-gdpr-banner/

A corner cookie sheet with Accept all, Reject all and an expandable Preferences panel of per-category toggles — semantic, keyboard-friendly and persistence-ready. The GDPR/CCPA consent pattern that respects an explicit reject.
## HTML
```html
<div class="cm-13">
  <div class="cm-13__page">
    <p class="cm-13__demo-note">Demo content behind the banner — the page stays usable.</p>
    <button class="cm-13__reopen" type="button" hidden>Cookie settings</button>
  </div>

  <section class="cm-13__banner" role="region" aria-label="Cookie consent">
    <div class="cm-13__body">
      <h2 class="cm-13__title">We value your privacy</h2>
      <p class="cm-13__text">We use cookies to run the site and, with your consent, to analyse traffic and personalise content. <a href="#privacy">Cookie Policy</a>.</p>

      <div class="cm-13__prefs" hidden>
        <label class="cm-13__cat"><span><b>Strictly necessary</b><small>Required for the site to function.</small></span>
          <input type="checkbox" checked disabled aria-label="Strictly necessary (always on)"></label>
        <label class="cm-13__cat"><span><b>Analytics</b><small>Helps us understand usage.</small></span>
          <input type="checkbox" id="cm-13-an"></label>
        <label class="cm-13__cat"><span><b>Marketing</b><small>Personalised offers &amp; ads.</small></span>
          <input type="checkbox" id="cm-13-mk"></label>
      </div>

      <div class="cm-13__actions">
        <button type="button" class="cm-13__btn cm-13__reject">Reject all</button>
        <button type="button" class="cm-13__btn cm-13__manage">Preferences</button>
        <button type="button" class="cm-13__btn cm-13__save" hidden>Save choices</button>
        <button type="button" class="cm-13__btn cm-13__accept">Accept all</button>
      </div>
    </div>
  </section>
</div>
```
## CSS
```css
.cm-13,
.cm-13 *,
.cm-13 *::before,
.cm-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-13 {
  --accent: oklch(0.72 0.14 250);
  position: relative;
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#0e1016,#07080b);
}

.cm-13__page {
  min-height: calc(100dvh - 64px);
  display: grid;
  place-items: center;
  gap: 16px;
}

.cm-13__demo-note {
  font: 13px ui-monospace,monospace;
  letter-spacing: .1em;
  color: #5a6272;
}

.cm-13__reopen {
  cursor: pointer;
  padding: 10px 18px;
  border-radius: 10px;
  border: 1px solid #2a3342;
  background: #141822;
  color: #c7cedb;
  font: 600 13px system-ui;
}

.cm-13__reopen:hover {
  border-color: var(--accent);
}

.cm-13__reopen:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-13__banner {
  position: fixed;
  left: 24px;
  bottom: 24px;
  width: min(420px,calc(100vw - 48px));
  z-index: 10;
  border-radius: 16px;
  background: linear-gradient(180deg,#151a24,#10141c);
  border: 1px solid #273041;
  box-shadow: 0 30px 70px -24px #000;
  transform: translateY(140%);
  opacity: 0;
  transition: transform .4s cubic-bezier(.4,0,.2,1),opacity .4s;
}

.cm-13__banner.is-in {
  transform: none;
  opacity: 1;
}

.cm-13__body {
  padding: 22px 22px 20px;
}

.cm-13__title {
  font-size: 17px;
  font-weight: 700;
  color: #f1f4fa;
  margin-bottom: 8px;
}

.cm-13__text {
  font-size: 13px;
  line-height: 1.6;
  color: #9aa3b4;
  margin-bottom: 16px;
}

.cm-13__text a {
  color: var(--accent);
  text-decoration: none;
}

.cm-13__text a:hover {
  text-decoration: underline;
}

.cm-13__prefs {
  display: flex;
  flex-direction: column;
  gap: 2px;
  margin-bottom: 16px;
  border-top: 1px solid #232b39;
  padding-top: 8px;
}

.cm-13__cat {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 11px 2px;
  cursor: pointer;
}

.cm-13__cat span {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.cm-13__cat b {
  font-size: 13.5px;
  font-weight: 600;
  color: #e7ecf5;
}

.cm-13__cat small {
  font-size: 11.5px;
  color: #7f8798;
}

.cm-13__cat input {
  width: 42px;
  height: 24px;
  -webkit-appearance: none;
  appearance: none;
  border-radius: 12px;
  background: #2a3342;
  position: relative;
  cursor: pointer;
  transition: background .2s;
  flex: none;
}

.cm-13__cat input::after {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #8891a2;
  transition: transform .2s,background .2s;
}

.cm-13__cat input:checked {
  background: color-mix(in oklch,var(--accent) 55%,#2a3342);
}

.cm-13__cat input:checked::after {
  transform: translateX(18px);
  background: #fff;
}

.cm-13__cat input:disabled {
  opacity: .7;
  cursor: not-allowed;
}

.cm-13__cat input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-13__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.cm-13__btn {
  flex: 1;
  min-width: 96px;
  padding: 11px 14px;
  border-radius: 10px;
  font: 600 13px system-ui;
  cursor: pointer;
  transition: all .18s;
}

.cm-13__reject,
.cm-13__manage,
.cm-13__save {
  border: 1px solid #2e3849;
  background: #161b26;
  color: #d3d9e4;
}

.cm-13__reject:hover,
.cm-13__manage:hover,
.cm-13__save:hover {
  border-color: #3d4a5e;
  background: #1c2330;
}

.cm-13__accept {
  border: none;
  background: var(--accent);
  color: #06101f;
}

.cm-13__accept:hover {
  filter: brightness(1.08);
}

.cm-13__btn:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cm-13__banner {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-13');
  var banner = root.querySelector('.cm-13__banner');
  var prefs = root.querySelector('.cm-13__prefs');
  var reopen = root.querySelector('.cm-13__reopen');
  var saveBtn = root.querySelector('.cm-13__save');
  var KEY = 'cm13-consent';
  function store(v){ try{ localStorage.setItem(KEY, JSON.stringify(v)); }catch(e){} }
  function read(){ try{ return JSON.parse(localStorage.getItem(KEY)); }catch(e){ return null; } }
  function hide(){ banner.classList.remove('is-in'); setTimeout(function(){ banner.style.display='none'; }, 400); reopen.hidden=false; }
  function open(){ banner.style.display=''; reopen.hidden=true; requestAnimationFrame(function(){ banner.classList.add('is-in'); }); }
  root.querySelector('.cm-13__accept').addEventListener('click', function(){ store({necessary:true,analytics:true,marketing:true}); hide(); });
  root.querySelector('.cm-13__reject').addEventListener('click', function(){ store({necessary:true,analytics:false,marketing:false}); hide(); });
  root.querySelector('.cm-13__manage').addEventListener('click', function(){
    var showing = !prefs.hidden; prefs.hidden = showing; saveBtn.hidden = showing;
  });
  saveBtn.addEventListener('click', function(){
    store({necessary:true, analytics:root.querySelector('#cm-13-an').checked, marketing:root.querySelector('#cm-13-mk').checked});
    hide();
  });
  reopen.addEventListener('click', open);
  // reveal on load unless a choice already exists
  if(read()){ banner.style.display='none'; reopen.hidden=false; }
  else requestAnimationFrame(function(){ banner.classList.add('is-in'); });
})();
```
