---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/irreversible-deletion-confirmation/"
title: "Irreversible Deletion Confirmation"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A stark danger dialog that guards a destructive action: a warning icon, red accents and a type-to-confirm field that keeps the Delete button disabled until…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Irreversible Deletion Confirmation
Source: https://codefronts.com/components/css-modals/irreversible-deletion-confirmation/

A stark danger dialog that guards a destructive action: a warning icon, red accents and a type-to-confirm field that keeps the Delete button disabled until the user types the exact keyword. The friction that prevents accidental account deletion.
## HTML
```html
<div class="cm-11">
  <button class="cm-11__open" type="button">Delete account</button>

  <dialog class="cm-11__dlg" aria-labelledby="cm-11-title" aria-describedby="cm-11-desc">
    <div class="cm-11__card">
      <div class="cm-11__icon" aria-hidden="true">&#9888;</div>
      <h2 id="cm-11-title" class="cm-11__title">Delete your account?</h2>
      <p id="cm-11-desc" class="cm-11__desc">This <b>permanently</b> deletes your account, 3 projects and all associated data. This action <b>cannot be undone</b>.</p>
      <label for="cm-11-confirm" class="cm-11__lbl">Type <code>DELETE</code> to confirm</label>
      <input id="cm-11-confirm" class="cm-11__input" type="text" autocomplete="off" placeholder="DELETE">
      <div class="cm-11__actions">
        <button type="button" class="cm-11__cancel" autofocus>Cancel</button>
        <button type="button" class="cm-11__delete" disabled>Delete account</button>
      </div>
    </div>
  </dialog>
</div>
```
## CSS
```css
.cm-11,
.cm-11 *,
.cm-11 *::before,
.cm-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-11 {
  --danger: oklch(0.62 0.22 22);
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#12100f,#080706);
}

.cm-11__open {
  cursor: pointer;
  padding: 13px 26px;
  border-radius: 11px;
  color: #ffd9d4;
  font: 600 15px system-ui;
  border: 1px solid color-mix(in oklch,var(--danger) 50%,#3a2420);
  background: color-mix(in oklch,var(--danger) 14%,#140f0e);
  transition: background .2s,border-color .2s;
}

.cm-11__open:hover {
  border-color: var(--danger);
  background: color-mix(in oklch,var(--danger) 24%,#140f0e);
}

.cm-11__open:focus-visible {
  outline: 2px solid var(--danger);
  outline-offset: 2px;
}

.cm-11__dlg {
  margin: auto;
  width: min(420px,94vw);
  padding: 0;
  border: none;
  border-radius: 18px;
  color: #eee4e2;
  background: linear-gradient(180deg,#1a1513,#130f0e);
  box-shadow: 0 40px 90px -30px #000,0 0 0 1px #33231f;
  opacity: 0;
  transform: translateY(10px) scale(.97);
  transition: opacity .26s,transform .26s,overlay .26s allow-discrete,display .26s allow-discrete;
}

.cm-11__dlg[open] {
  opacity: 1;
  transform: none;
}

@starting-style {
  .cm-11__dlg[open] {
    opacity: 0;
    transform: translateY(10px) scale(.97);
  }
}

.cm-11__dlg::backdrop {
  background: rgba(6,4,3,0);
  backdrop-filter: blur(0);
  transition: background .3s,backdrop-filter .3s,overlay .3s allow-discrete,display .3s allow-discrete;
}

.cm-11__dlg[open]::backdrop {
  background: rgba(6,4,3,.62);
  backdrop-filter: blur(5px);
}

@starting-style {
  .cm-11__dlg[open]::backdrop {
    background: rgba(6,4,3,0);
    backdrop-filter: blur(0);
  }
}

.cm-11__card {
  padding: 32px 30px 26px;
}

.cm-11__icon {
  width: 56px;
  height: 56px;
  margin-bottom: 18px;
  border-radius: 14px;
  display: grid;
  place-items: center;
  font-size: 26px;
  color: var(--danger);
  background: color-mix(in oklch,var(--danger) 16%,#140f0e);
  box-shadow: inset 0 0 0 1px color-mix(in oklch,var(--danger) 35%,transparent);
}

.cm-11__title {
  font-size: 22px;
  font-weight: 700;
  color: #fbeeeb;
  margin-bottom: 10px;
}

.cm-11__desc {
  font-size: 14px;
  line-height: 1.6;
  color: #c2aca7;
  margin-bottom: 22px;
}

.cm-11__desc b {
  color: #f4d9d3;
}

.cm-11__lbl {
  display: block;
  font-size: 12.5px;
  color: #b39a95;
  margin-bottom: 8px;
}

.cm-11__lbl code {
  background: #241816;
  padding: 2px 6px;
  border-radius: 5px;
  color: #f0c9c1;
  font-weight: 700;
  letter-spacing: .06em;
}

.cm-11__input {
  width: 100%;
  padding: 12px 14px;
  border-radius: 10px;
  border: 1px solid #3a2723;
  background: #0e0a09;
  color: #f2e6e3;
  font: 15px ui-monospace,monospace;
  letter-spacing: .1em;
  margin-bottom: 22px;
  transition: border-color .2s,box-shadow .2s;
}

.cm-11__input:focus {
  outline: none;
  border-color: var(--danger);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--danger) 26%,transparent);
}

.cm-11__actions {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.cm-11__cancel,
.cm-11__delete {
  padding: 13px;
  border-radius: 11px;
  font: 700 14.5px system-ui;
  cursor: pointer;
  transition: all .18s;
}

.cm-11__cancel {
  border: 1px solid #3a2b28;
  background: #1c1614;
  color: #e6d7d3;
}

.cm-11__cancel:hover {
  background: #241c19;
  border-color: #4a3833;
}

.cm-11__delete {
  border: none;
  background: var(--danger);
  color: #fff;
}

.cm-11__delete:hover:not(:disabled) {
  filter: brightness(1.08);
}

.cm-11__delete:disabled {
  opacity: .4;
  cursor: not-allowed;
}

.cm-11__cancel:focus-visible,
.cm-11__delete:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cm-11__dlg,
    .cm-11__dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-11');
  var dlg = root.querySelector('.cm-11__dlg');
  var input = root.querySelector('.cm-11__input');
  var del = root.querySelector('.cm-11__delete');
  var KEYWORD = 'DELETE';
  function openDlg(){ input.value = ''; del.disabled = true; dlg.showModal(); }
  root.querySelector('.cm-11__open').addEventListener('click', openDlg);
  root.querySelector('.cm-11__cancel').addEventListener('click', function(){ dlg.close(); });
  input.addEventListener('input', function(){ del.disabled = input.value.trim() !== KEYWORD; });
  del.addEventListener('click', function(){
    del.textContent = 'Deleting…';
    setTimeout(function(){ dlg.close(); del.textContent = 'Delete account'; }, 900);
  });
})();
```
