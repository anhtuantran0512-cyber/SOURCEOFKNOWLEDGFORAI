---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/search-command-palette-cmd-k/"
title: "Search Command Palette (Cmd + K)"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A top-drop command palette opened with ⌘K / Ctrl+K: fuzzy-filter a list of actions, navigate with arrow keys, run with Enter — the developer-tool-style…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Search Command Palette (Cmd + K)
Source: https://codefronts.com/components/css-modals/search-command-palette-cmd-k/

A top-drop command palette opened with ⌘K / Ctrl+K: fuzzy-filter a list of actions, navigate with arrow keys, run with Enter — the developer-tool-style launcher power users now expect in every dashboard.
## HTML
```html
<div class="cm-18">
  <button class="cm-18__open" type="button">Search <kbd class="cm-18__kbd">⌘K</kbd></button>

  <dialog class="cm-18__dlg" aria-label="Command palette">
    <div class="cm-18__card">
      <div class="cm-18__search">
        <span class="cm-18__ico" aria-hidden="true">⌕</span>
        <input class="cm-18__input" type="text" role="combobox" aria-expanded="true" aria-controls="cm-18-list"
          aria-autocomplete="list" placeholder="Type a command or search…" autocomplete="off">
        <kbd class="cm-18__esc">esc</kbd>
      </div>
      <ul class="cm-18__list" id="cm-18-list" role="listbox" aria-label="Commands"></ul>
      <div class="cm-18__empty" hidden>No commands match “<span class="cm-18__q"></span>”.</div>
      <p class="cm-18__count" aria-live="polite"></p>
      <footer class="cm-18__foot">
        <span><kbd>↑</kbd><kbd>↓</kbd> navigate</span><span><kbd>↵</kbd> select</span><span><kbd>esc</kbd> close</span>
      </footer>
    </div>
  </dialog>
</div>
```
## CSS
```css
.cm-18,
.cm-18 *,
.cm-18 *::before,
.cm-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-18 {
  --accent: oklch(0.74 0.14 265);
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#0d0e15,#08080d);
}

.cm-18__open {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  padding: 12px 16px 12px 22px;
  border-radius: 11px;
  color: #c9cee0;
  font: 500 14px system-ui;
  border: 1px solid #262a3c;
  background: #12141e;
  min-width: 220px;
  justify-content: space-between;
  transition: border-color .2s,background .2s;
}

.cm-18__open:hover {
  border-color: var(--accent);
  background: #171a26;
}

.cm-18__open:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-18__kbd,
.cm-18 kbd {
  font: 600 11px ui-monospace,monospace;
  background: #232838;
  color: #aab0c6;
  padding: 2px 6px;
  border-radius: 5px;
  border: 1px solid #333a4e;
}

.cm-18__dlg {
  width: min(560px,94vw);
  margin: 12vh auto 0;
  padding: 0;
  border: none;
  border-radius: 16px;
  color: #e7eaf3;
  background: linear-gradient(180deg,#161824,#111320);
  box-shadow: 0 50px 100px -28px #000,0 0 0 1px #282d40;
  opacity: 0;
  transform: translateY(-16px) scale(.98);
  transition: opacity .24s,transform .24s,overlay .24s allow-discrete,display .24s allow-discrete;
}

.cm-18__dlg[open] {
  opacity: 1;
  transform: none;
}

@starting-style {
  .cm-18__dlg[open] {
    opacity: 0;
    transform: translateY(-16px) scale(.98);
  }
}

.cm-18__dlg::backdrop {
  background: rgba(5,6,10,0);
  backdrop-filter: blur(0);
  transition: background .28s,backdrop-filter .28s,overlay .28s allow-discrete,display .28s allow-discrete;
}

.cm-18__dlg[open]::backdrop {
  background: rgba(5,6,10,.6);
  backdrop-filter: blur(5px);
}

@starting-style {
  .cm-18__dlg[open]::backdrop {
    background: rgba(5,6,10,0);
    backdrop-filter: blur(0);
  }
}

.cm-18__search {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 18px;
  border-bottom: 1px solid #23283a;
}

.cm-18__ico {
  font-size: 19px;
  color: #6f7690;
}

.cm-18__input {
  flex: 1;
  background: none;
  border: none;
  outline: none;
  color: #f1f3fa;
  font: 16px system-ui;
}

.cm-18__input::placeholder {
  color: #6f7590;
}

.cm-18__esc {
  font: 600 10px ui-monospace,monospace;
  background: #232838;
  color: #9aa0b6;
  padding: 3px 7px;
  border-radius: 5px;
  border: 1px solid #333a4e;
}

.cm-18__list {
  list-style: none;
  max-height: 320px;
  overflow: auto;
  padding: 8px;
}

.cm-18__grp {
  font-size: 11px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #6d7590;
  padding: 12px 12px 6px;
}

.cm-18__item {
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 11px 12px;
  border-radius: 9px;
  cursor: pointer;
  color: #d3d8e6;
  font-size: 14.5px;
  scroll-margin: 8px;
}

.cm-18__item .cm-18__i {
  width: 26px;
  height: 26px;
  border-radius: 7px;
  display: grid;
  place-items: center;
  font-size: 14px;
  background: #212636;
  color: #c3c9dc;
  flex: none;
}

.cm-18__item .cm-18__sc {
  margin-left: auto;
  display: flex;
  gap: 4px;
}

.cm-18__item[aria-selected="true"] {
  background: color-mix(in oklch,var(--accent) 24%,#1a1e2c);
}

.cm-18__item[aria-selected="true"] .cm-18__i {
  background: color-mix(in oklch,var(--accent) 40%,#212636);
  color: #fff;
}

.cm-18__empty {
  padding: 34px 20px;
  text-align: center;
  font-size: 14px;
  color: #7c8299;
}

.cm-18__foot {
  display: flex;
  gap: 18px;
  padding: 12px 18px;
  border-top: 1px solid #23283a;
  font-size: 12px;
  color: #828aa0;
}

.cm-18__foot span {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.cm-18__count {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cm-18__dlg,
    .cm-18__dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-18');
  var dlg = root.querySelector('.cm-18__dlg');
  var input = root.querySelector('.cm-18__input');
  var list = root.querySelector('.cm-18__list');
  var empty = root.querySelector('.cm-18__empty');
  var count = root.querySelector('.cm-18__count');
  var COMMANDS = [
    {group:'Actions', i:'✎', label:'New document', keys:'create file', sc:['⌘','N']},
    {group:'Actions', i:'⬆', label:'Upload files', keys:'import media', sc:['⌘','U']},
    {group:'Actions', i:'🖇', label:'Invite teammate', keys:'add member share', sc:['⌘','I']},
    {group:'Navigate', i:'⌂', label:'Go to Dashboard', keys:'home overview', sc:['G','H']},
    {group:'Navigate', i:'▤', label:'Go to Projects', keys:'boards work', sc:['G','P']},
    {group:'Navigate', i:'⚙', label:'Open Settings', keys:'preferences account', sc:['⌘',',']},
    {group:'Help', i:'?', label:'Keyboard shortcuts', keys:'keys help', sc:['⌘','/']},
    {group:'Help', i:'✉', label:'Contact support', keys:'email ticket', sc:[]}
  ];
  var active = 0, visible = [];
  function render(q){
    q = (q||'').trim().toLowerCase();
    list.innerHTML = ''; visible = [];
    var lastGroup = null;
    COMMANDS.forEach(function(c){
      if(q && (c.label + ' ' + c.keys).toLowerCase().indexOf(q) === -1) return;
      if(c.group !== lastGroup){
        var h = document.createElement('li'); h.className = 'cm-18__grp'; h.textContent = c.group; h.setAttribute('role','presentation');
        list.appendChild(h); lastGroup = c.group;
      }
      var li = document.createElement('li');
      li.className = 'cm-18__item'; li.setAttribute('role','option');
      var sc = c.sc.map(function(k){ return '<kbd>'+k+'</kbd>'; }).join('');
      li.innerHTML = '<span class="cm-18__i">'+c.i+'</span>'+c.label+'<span class="cm-18__sc">'+sc+'</span>';
      li.addEventListener('mousemove', function(){ setActive(visible.indexOf(li)); });
      li.addEventListener('click', function(){ run(li); });
      list.appendChild(li); visible.push(li);
    });
    empty.hidden = visible.length > 0;
    if(!empty.hidden) root.querySelector('.cm-18__q').textContent = q;
    active = 0; paint();
    count.textContent = visible.length + ' commands';
  }
  function paint(){
    visible.forEach(function(li,n){ li.setAttribute('aria-selected', n === active ? 'true' : 'false'); });
    if(visible[active]) visible[active].scrollIntoView({block:'nearest'});
  }
  function setActive(n){ if(n<0||n>=visible.length) return; active = n; paint(); }
  function run(li){ input.value = li.textContent.replace(/[⌘↵]/g,'').trim(); dlg.close(); }
  input.addEventListener('input', function(){ render(input.value); });
  input.addEventListener('keydown', function(e){
    if(e.key === 'ArrowDown'){ e.preventDefault(); setActive(Math.min(active+1, visible.length-1)); }
    else if(e.key === 'ArrowUp'){ e.preventDefault(); setActive(Math.max(active-1, 0)); }
    else if(e.key === 'Enter'){ e.preventDefault(); if(visible[active]) run(visible[active]); }
  });
  function open(){ input.value=''; render(''); dlg.showModal(); setTimeout(function(){ input.focus(); }, 20); }
  root.querySelector('.cm-18__open').addEventListener('click', open);
  document.addEventListener('keydown', function(e){
    if((e.metaKey || e.ctrlKey) && (e.key === 'k' || e.key === 'K')){ e.preventDefault(); if(!dlg.open) open(); }
  });
  dlg.addEventListener('click', function(e){
    var c = dlg.querySelector('.cm-18__card').getBoundingClientRect();
    if(e.clientX < c.left || e.clientX > c.right || e.clientY < c.top || e.clientY > c.bottom) dlg.close();
  });
})();
```
