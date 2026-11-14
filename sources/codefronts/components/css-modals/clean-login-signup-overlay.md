---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/clean-login-signup-overlay/"
title: "Clean Login / Signup Overlay"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A polished dual-tab authentication overlay: one native <dialog> flips between Sign in and Create account with pure-CSS tabs, floating-label inputs and a…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clean Login / Signup Overlay
Source: https://codefronts.com/components/css-modals/clean-login-signup-overlay/

A polished dual-tab authentication overlay: one native <dialog> flips between Sign in and Create account with pure-CSS tabs, floating-label inputs and a blurred backdrop. The most-searched auth modal, built the accessible way.
## HTML
```html
<div class="cm-01">
  <button class="cm-01__open" type="button">Sign in</button>

  <dialog class="cm-01__dlg" aria-labelledby="cm-01-title">
    <form class="cm-01__card" method="dialog">
      <button class="cm-01__x" type="submit" value="close" aria-label="Close dialog">&times;</button>

      <div class="cm-01__tabs">
        <input type="radio" name="cm-01-tab" id="cm-01-in" class="cm-01__radio" checked>
        <label for="cm-01-in" class="cm-01__tab">Sign in</label>
        <input type="radio" name="cm-01-tab" id="cm-01-up" class="cm-01__radio">
        <label for="cm-01-up" class="cm-01__tab">Create account</label>
        <span class="cm-01__ink" aria-hidden="true"></span>
      </div>

      <h2 id="cm-01-title" class="cm-01__title">
        <span class="cm-01__t-in">Welcome back</span><span class="cm-01__t-up">Create your account</span>
      </h2>

      <div class="cm-01__field cm-01__field--name">
        <input type="text" id="cm-01-name" class="cm-01__input" placeholder=" " autocomplete="name">
        <label for="cm-01-name" class="cm-01__label">Full name</label>
      </div>
      <div class="cm-01__field">
        <input type="email" id="cm-01-email" class="cm-01__input" placeholder=" " required autocomplete="email">
        <label for="cm-01-email" class="cm-01__label">Email address</label>
      </div>
      <div class="cm-01__field">
        <input type="password" id="cm-01-pass" class="cm-01__input" placeholder=" " required autocomplete="current-password">
        <label for="cm-01-pass" class="cm-01__label">Password</label>
      </div>

      <button type="button" class="cm-01__submit">
        <span class="cm-01__t-in">Sign in</span><span class="cm-01__t-up">Create account</span>
      </button>
      <p class="cm-01__alt">By continuing you agree to our Terms &amp; Privacy Policy.</p>
    </form>
  </dialog>
</div>
```
## CSS
```css
.cm-01,
.cm-01 *,
.cm-01 *::before,
.cm-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-01 {
  --accent: oklch(0.72 0.16 255);
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#12151c,#080a0e);
}

.cm-01__open {
  cursor: pointer;
  padding: 13px 28px;
  border-radius: 11px;
  color: #eaf0ff;
  font: 600 15px system-ui;
  border: 1px solid color-mix(in oklch,var(--accent) 45%,#2a2f3a);
  background: color-mix(in oklch,var(--accent) 14%,#0e1116);
  transition: background .2s,border-color .2s;
}

.cm-01__open:hover {
  background: color-mix(in oklch,var(--accent) 24%,#0e1116);
  border-color: var(--accent);
}

.cm-01__open:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-01__dlg {
  margin: auto;
  width: min(400px,94vw);
  padding: 0;
  border: none;
  border-radius: 18px;
  color: #e7ecf5;
  background: linear-gradient(180deg,#141821,#0f131b);
  box-shadow: 0 30px 80px -30px #000,0 0 0 1px #232a36;
  opacity: 0;
  transform: translateY(10px) scale(.98);
  transition: opacity .28s ease,transform .28s ease,overlay .28s allow-discrete,display .28s allow-discrete;
}

.cm-01__dlg[open] {
  opacity: 1;
  transform: none;
}

@starting-style {
  .cm-01__dlg[open] {
    opacity: 0;
    transform: translateY(10px) scale(.98);
  }
}

.cm-01__dlg::backdrop {
  background: rgba(6,8,12,0);
  backdrop-filter: blur(0px);
  transition: background .3s,backdrop-filter .3s,overlay .3s allow-discrete,display .3s allow-discrete;
}

.cm-01__dlg[open]::backdrop {
  background: rgba(6,8,12,.62);
  backdrop-filter: blur(5px);
}

@starting-style {
  .cm-01__dlg[open]::backdrop {
    background: rgba(6,8,12,0);
    backdrop-filter: blur(0px);
  }
}

.cm-01__card {
  position: relative;
  padding: 30px;
}

.cm-01__x {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #8b93a4;
  font-size: 22px;
  line-height: 1;
  cursor: pointer;
  transition: background .2s,color .2s;
}

.cm-01__x:hover {
  background: #1c2230;
  color: #e7ecf5;
}

.cm-01__x:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-01__tabs {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin: 4px 0 22px;
  background: #0c0f16;
  border: 1px solid #222937;
  border-radius: 10px;
  padding: 4px;
}

.cm-01__radio {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cm-01__tab {
  position: relative;
  z-index: 2;
  text-align: center;
  padding: 9px;
  border-radius: 7px;
  font: 600 13.5px system-ui;
  color: #9aa3b4;
  cursor: pointer;
  transition: color .2s;
}

.cm-01__ink {
  position: absolute;
  z-index: 1;
  top: 4px;
  bottom: 4px;
  left: 4px;
  width: calc(50% - 4px);
  border-radius: 7px;
  background: color-mix(in oklch,var(--accent) 26%,#161b25);
  border: 1px solid color-mix(in oklch,var(--accent) 40%,transparent);
  transition: transform .28s cubic-bezier(.4,0,.2,1);
}

.cm-01__card:has(#cm-01-up:checked) .cm-01__ink {
  transform: translateX(100%);
}

#cm-01-in:checked~.cm-01__tab[for="cm-01-in"],
#cm-01-up:checked~.cm-01__tab[for="cm-01-up"] {
  color: #fff;
}

.cm-01__tab:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-01__title {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -.01em;
  margin-bottom: 20px;
  color: #f3f6fc;
}

.cm-01__t-up {
  display: none;
}

.cm-01__card:has(#cm-01-up:checked) .cm-01__t-in {
  display: none;
}

.cm-01__card:has(#cm-01-up:checked) .cm-01__t-up {
  display: inline;
}

.cm-01__field {
  position: relative;
  margin-bottom: 14px;
}

.cm-01__field--name {
  display: none;
}

.cm-01__card:has(#cm-01-up:checked) .cm-01__field--name {
  display: block;
}

.cm-01__input {
  width: 100%;
  padding: 18px 14px 8px;
  border-radius: 10px;
  border: 1px solid #2a3140;
  background: #0c0f16;
  color: #eef2f9;
  font: 15px system-ui;
  transition: border-color .2s,box-shadow .2s;
}

.cm-01__input:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--accent) 30%,transparent);
}

.cm-01__label {
  position: absolute;
  left: 14px;
  top: 15px;
  color: #8992a3;
  font-size: 15px;
  pointer-events: none;
  transition: transform .18s,color .18s,font-size .18s;
  transform-origin: left;
}

.cm-01__input:focus+.cm-01__label,
.cm-01__input:not(:placeholder-shown)+.cm-01__label {
  transform: translateY(-10px);
  font-size: 11px;
  color: var(--accent);
}

.cm-01__submit {
  width: 100%;
  margin-top: 8px;
  padding: 14px;
  border: none;
  border-radius: 10px;
  background: var(--accent);
  color: #06101f;
  font: 700 15px system-ui;
  cursor: pointer;
  transition: filter .2s,transform .1s;
}

.cm-01__submit:hover {
  filter: brightness(1.08);
}

.cm-01__submit:active {
  transform: translateY(1px);
}

.cm-01__submit:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.cm-01__alt {
  margin-top: 16px;
  text-align: center;
  font-size: 12.5px;
  line-height: 1.5;
  color: #79808f;
}

@media (prefers-reduced-motion: reduce) {
  .cm-01__dlg,
    .cm-01__dlg::backdrop,
    .cm-01__ink,
    .cm-01__input,
    .cm-01__label {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-01');
  var dlg = root.querySelector('.cm-01__dlg');
  root.querySelector('.cm-01__open').addEventListener('click', function(){ dlg.showModal(); });
  root.querySelector('.cm-01__submit').addEventListener('click', function(){ dlg.close(); });
  // light-dismiss: close when the backdrop (outside the card) is clicked
  dlg.addEventListener('click', function(e){
    var c = dlg.querySelector('.cm-01__card').getBoundingClientRect();
    if(e.clientX < c.left || e.clientX > c.right || e.clientY < c.top || e.clientY > c.bottom) dlg.close();
  });
})();
```
