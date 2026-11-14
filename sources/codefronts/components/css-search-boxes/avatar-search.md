---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/avatar-search/"
title: "CSS People Search Bar with Avatar Chips"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "The team-picker: selected people sit in the field as avatar chips, and typing filters a list of teammates with photos, roles and presence dots."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS People Search Bar with Avatar Chips
Source: https://codefronts.com/components/css-search-boxes/avatar-search/

The team-picker: selected people sit in the field as avatar chips, and typing filters a list of teammates with photos, roles and presence dots. Click or press Enter to add, click the chip's &times; (or Backspace) to remove — the assignee/mention pattern from Linear, Jira and Slack.
## HTML
```html
<div class="sb-20">
  <button class="sb-20__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-20__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-20__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-20__stage">
    <div class="sb-20__wrap" role="search">
      <div class="sb-20__field" id="sb-20-field">
        <span class="sb-20__chip">
          <img src="https://picsum.photos/seed/sb20-alex/64/64" width="64" height="64" alt="" loading="lazy" decoding="async">
          Alex Chen
          <button class="sb-20__x" type="button" aria-label="Remove Alex Chen"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 7 10 10M17 7 7 17" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg></button>
        </span>
        <label class="sb-20__vh" for="sb-20-input">Search people to add</label>
        <input class="sb-20__input" id="sb-20-input" type="search" placeholder="Add people&hellip;" autocomplete="off" aria-controls="sb-20-list">
      </div>

      <ul class="sb-20__list" id="sb-20-list" role="listbox" aria-label="People">
        <li class="sb-20__row" role="option" aria-selected="false" data-name="Priya Sharma" data-role="Product lead" data-img="sb20-priya">
          <span class="sb-20__av"><img src="https://picsum.photos/seed/sb20-priya/80/80" width="80" height="80" alt="" loading="lazy" decoding="async"><i class="sb-20__dot sb-20__dot--on"></i></span>
          <span class="sb-20__who">Priya Sharma<small>Product lead &middot; online</small></span>
          <span class="sb-20__add" aria-hidden="true">Add</span>
        </li>
        <li class="sb-20__row" role="option" aria-selected="false" data-name="Jordan Lee" data-role="Staff engineer" data-img="sb20-jordan">
          <span class="sb-20__av"><img src="https://picsum.photos/seed/sb20-jordan/80/80" width="80" height="80" alt="" loading="lazy" decoding="async"><i class="sb-20__dot"></i></span>
          <span class="sb-20__who">Jordan Lee<small>Staff engineer &middot; away</small></span>
          <span class="sb-20__add" aria-hidden="true">Add</span>
        </li>
        <li class="sb-20__row" role="option" aria-selected="false" data-name="Sam Rivera" data-role="Design engineer" data-img="sb20-sam">
          <span class="sb-20__av"><img src="https://picsum.photos/seed/sb20-sam/80/80" width="80" height="80" alt="" loading="lazy" decoding="async"><i class="sb-20__dot sb-20__dot--on"></i></span>
          <span class="sb-20__who">Sam Rivera<small>Design engineer &middot; online</small></span>
          <span class="sb-20__add" aria-hidden="true">Add</span>
        </li>
        <li class="sb-20__row" role="option" aria-selected="false" data-name="Maya Okonkwo" data-role="Data science" data-img="sb20-maya">
          <span class="sb-20__av"><img src="https://picsum.photos/seed/sb20-maya/80/80" width="80" height="80" alt="" loading="lazy" decoding="async"><i class="sb-20__dot"></i></span>
          <span class="sb-20__who">Maya Okonkwo<small>Data science &middot; offline</small></span>
          <span class="sb-20__add" aria-hidden="true">Add</span>
        </li>
      </ul>
      <p class="sb-20__none">No teammates match that search</p>
      <p class="sb-20__vh" id="sb-20-status" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-20 {
  --bg: #f5f6f9;
  --card: #ffffff;
  --ink: #141821;
  --muted: #6a7180;
  --line: #e4e7ee;
  --acc: #4338ca;
  --wash: #eef0ff;
  --on: #22c55e;
  --ring: #4338ca;
  --shadow: rgba(20,24,33,.14);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-20 *,
.sb-20 *::before,
.sb-20 *::after {
  box-sizing: border-box;
}

.sb-20__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-20__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-20__wrap {
  inline-size: min(28rem,100%);
  padding: .5rem;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--card);
  box-shadow: 0 20px 44px -26px var(--shadow), 0 1px 2px rgba(20,24,33,.04);
}

.sb-20__field {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .35rem;
  min-block-size: 48px;
  padding: .35rem .5rem;
  border-radius: 11px;
  background: #f7f8fb;
  transition: box-shadow .2s, background .2s;
}

.sb-20__field:focus-within {
  background: var(--card);
  box-shadow: 0 0 0 2px var(--acc);
}

.sb-20__chip {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  block-size: 30px;
  padding-inline: .3rem .15rem;
  border-radius: 999px;
  background: var(--wash);
  color: var(--acc);
  font: 600 .82rem/1 inherit;
  white-space: nowrap;
  animation: sb-20-pop .18s cubic-bezier(.2,.9,.25,1);
}

@keyframes sb-20-pop {
  from {
    opacity: 0;
    scale: .9;
  }

  to {
    opacity: 1;
    scale: 1;
  }
}

.sb-20__chip img {
  inline-size: 22px;
  block-size: 22px;
  border-radius: 50%;
  object-fit: cover;
  background: #dfe3ee;
}

.sb-20__x {
  display: grid;
  place-items: center;
  inline-size: 24px;
  block-size: 24px;
  border: 0;
  border-radius: 50%;
  background: none;
  color: inherit;
  cursor: pointer;
  opacity: .65;
  transition: opacity .15s, background .15s;
}

.sb-20__x:hover {
  opacity: 1;
  background: rgba(67,56,202,.14);
}

.sb-20__x:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 1px;
  opacity: 1;
}

.sb-20__x svg {
  inline-size: 11px;
  block-size: 11px;
}

.sb-20__input {
  flex: 1 1 7ch;
  min-inline-size: 7ch;
  block-size: 30px;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .92rem/1 inherit;
}

.sb-20__input::placeholder {
  color: var(--muted);
}

.sb-20__input:focus {
  outline: none;
}

.sb-20__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-20__list {
  list-style: none;
  margin: .35rem 0 0;
  padding: 0;
  max-block-size: min(18rem,44vh);
  overflow: auto;
}

.sb-20__row {
  display: flex;
  align-items: center;
  gap: .7rem;
  min-block-size: 52px;
  padding: .35rem .5rem;
  border-radius: 11px;
  cursor: pointer;
  transition: background .14s;
}

.sb-20__row:hover,
.sb-20__row[aria-selected="true"] {
  background: #f5f6fa;
}

.sb-20__av {
  position: relative;
  flex: none;
  inline-size: 34px;
  block-size: 34px;
}

.sb-20__av img {
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  background: #dfe3ee;
}

.sb-20__dot {
  position: absolute;
  inset-block-end: -1px;
  inset-inline-end: -1px;
  inline-size: 11px;
  block-size: 11px;
  border: 2px solid var(--card);
  border-radius: 50%;
  background: #c3c8d4;
}

.sb-20__dot--on {
  background: var(--on);
}

.sb-20__who {
  display: block;
  flex: 1;
  min-inline-size: 0;
  font: 600 .9rem/1.25 inherit;
}

.sb-20__who small {
  display: block;
  margin-block-start: .1rem;
  color: var(--muted);
  font: 400 .76rem/1.3 inherit;
}

.sb-20__add {
  flex: none;
  padding: .3rem .6rem;
  border-radius: 8px;
  background: var(--wash);
  color: var(--acc);
  font: 600 .76rem/1 inherit;
  opacity: 0;
  translate: 4px 0;
  transition: opacity .16s, translate .16s;
}

.sb-20__row:hover .sb-20__add {
  opacity: 1;
  translate: 0 0;
}

.sb-20__none {
  display: none;
  margin: 0;
  padding: 1.4rem 0;
  text-align: center;
  color: var(--muted);
  font: 400 .86rem/1 inherit;
}

@supports selector(:has(*)) {
  .sb-20__wrap:has(.sb-20__list:not(:has(.sb-20__row:not([hidden])))) .sb-20__none {
    display: block;
  }
}

.sb-20 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-20__input:focus-visible {
  outline: none;
}

.sb-20[data-theme="dark"] {
  --bg: #0b0e15;
  --card: #141924;
  --ink: #e9edf6;
  --muted: #8b93a3;
  --line: #222a38;
  --acc: #a5b4fc;
  --wash: rgba(165,180,252,.14);
  --ring: #a5b4fc;
  --shadow: rgba(0,0,0,.7);
}

.sb-20[data-theme="dark"] .sb-20__field {
  background: #101520;
}

.sb-20[data-theme="dark"] .sb-20__row:hover {
  background: #1a2130;
}

@media (prefers-color-scheme: dark) {
  .sb-20:not([data-theme="light"]) {
    --bg: #0b0e15;
    --card: #141924;
    --ink: #e9edf6;
    --muted: #8b93a3;
    --line: #222a38;
    --acc: #a5b4fc;
    --wash: rgba(165,180,252,.14);
    --ring: #a5b4fc;
    --shadow: rgba(0,0,0,.7);
  }

  .sb-20:not([data-theme="light"]) .sb-20__field {
    background: #101520;
  }

  .sb-20:not([data-theme="light"]) .sb-20__row:hover {
    background: #1a2130;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-20 *,
    .sb-20 *::before,
    .sb-20 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .sb-20__wrap,
    .sb-20__field,
    .sb-20__chip {
    border: 1px solid CanvasText;
  }
}

.sb-20__theme {
  position: absolute;
  inset-block-start: clamp(.75rem,2vw,1.25rem);
  inset-inline-end: clamp(.75rem,2vw,1.25rem);
  z-index: 50;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid rgba(0,0,0,.12);
  color: currentColor;
  background: rgba(255,255,255,.72);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
}

.sb-20[data-theme="dark"] .sb-20__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-20:not([data-theme="light"]) .sb-20__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-20__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-20[data-theme="dark"] .sb-20__theme:hover,
.sb-20:not([data-theme="light"]) .sb-20__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-20__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-20__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-20__sun {
  display: none;
}

.sb-20__theme[aria-pressed="true"] .sb-20__sun {
  display: block;
}

.sb-20__theme[aria-pressed="true"] .sb-20__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-20__theme {
    transition: none;
  }

  .sb-20__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-20');
  if (!root) return;
  const field = root.querySelector('#sb-20-field');
  const input = root.querySelector('#sb-20-input');
  const rows = [...root.querySelectorAll('.sb-20__row')];
  const status = root.querySelector('#sb-20-status');

  const chip = (name, img) => {
    const el = document.createElement('span');
    el.className = 'sb-20__chip';
    el.dataset.name = name;
    const photo = document.createElement('img');
    photo.src = 'https://picsum.photos/seed/' + img + '/64/64';
    photo.width = photo.height = 64; photo.alt = ''; photo.loading = 'lazy';
    const btn = document.createElement('button');
    btn.type = 'button'; btn.className = 'sb-20__x'; btn.setAttribute('aria-label', 'Remove ' + name);
    btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="m7 7 10 10M17 7 7 17" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>';
    el.append(photo, document.createTextNode(name), btn);
    return el;
  };
  const filter = () => {
    const q = input.value.trim().toLowerCase();
    rows.forEach((r) => {
      if (r.dataset.picked === 'true') return;
      r.hidden = q !== '' && !(r.dataset.name + ' ' + r.dataset.role).toLowerCase().includes(q);
    });
  };
  const add = (row) => {
    field.insertBefore(chip(row.dataset.name, row.dataset.img), input);
    row.hidden = true; row.dataset.picked = 'true';
    status.textContent = row.dataset.name + ' added';
    input.value = ''; filter(); input.focus();
  };
  const remove = (el) => {
    const row = rows.find((r) => r.dataset.name === el.dataset.name);
    if (row) { row.hidden = false; delete row.dataset.picked; }
    status.textContent = (el.dataset.name || 'Person') + ' removed';
    el.remove(); input.focus();
  };

  input.addEventListener('input', filter);
  input.addEventListener('keydown', (e) => {
    const visible = rows.filter((r) => !r.hidden);
    if (e.key === 'Enter' && visible[0]) { e.preventDefault(); add(visible[0]); }
    if (e.key === 'Backspace' && input.value === '') {
      const last = [...field.querySelectorAll('.sb-20__chip')].at(-1);
      if (last) { e.preventDefault(); remove(last); }
    }
  });
  root.querySelector('#sb-20-list').addEventListener('click', (e) => {
    const row = e.target.closest('.sb-20__row');
    if (row) add(row);
  });
  field.addEventListener('click', (e) => {
    const x = e.target.closest('.sb-20__x');
    if (x) remove(x.closest('.sb-20__chip'));
  });
  [...field.querySelectorAll('.sb-20__chip')].forEach((c) => { c.dataset.name = c.textContent.trim(); });
})();
(()=>{const r=document.querySelector('.sb-20');if(!r)return;const t=r.querySelector('.sb-20__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
