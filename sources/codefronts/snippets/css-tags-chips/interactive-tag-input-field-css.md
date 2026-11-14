---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/interactive-tag-input-field-css/"
title: "Interactive Tag Input Field CSS"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "The form control every CMS, job board and email client needs: type, hit Enter or comma, and the text crystallizes into a chip."
has_js: "true"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Tag Input Field CSS
Source: https://codefronts.com/snippets/css-tags-chips/interactive-tag-input-field-css/

The form control every CMS, job board and email client needs: type, hit Enter or comma, and the text crystallizes into a chip. Backspace on an empty input plucks the last tag back off; every chip is a real <button> whose whole 44px body removes it; duplicates shake instead of duplicating; a polite aria-live region narrates every change for screen readers. The CSS owns 100% of the look and motion — the 40-line script only moves DOM nodes.
## HTML
```html
<section class="ctc-02" aria-label="Interactive tag input field demo">
  <div class="ctc-02__stage">
    <div class="ctc-02__wrap">
      <header class="ctc-02__head">
        <p class="ctc-02__kicker">Tag input · chips from keystrokes</p>
        <h1>Type. <kbd>Enter</kbd>. It's a chip.</h1>
        <p class="ctc-02__sub">Press <kbd>Enter</kbd> or <kbd>,</kbd> to commit a tag — <kbd>⌫</kbd> on an empty field removes the last one. Click any chip to delete it.</p>
      </header>
      <form class="ctc-02__card" onsubmit="return false">
        <div class="ctc-02__row">
          <label class="ctc-02__lab" for="ctc02-in">Topics</label>
          <output class="ctc-02__count" id="ctc02-count">2/8</output>
        </div>
        <label class="ctc-02__field" for="ctc02-in">
          <span class="ctc-02__sr">Add topic tags</span>
          <button type="button" class="ctc-02__tag" data-v="css" aria-label="Remove tag css"><span>css</span><i aria-hidden="true"></i></button>
          <button type="button" class="ctc-02__tag" data-v="frontend" aria-label="Remove tag frontend"><span>frontend</span><i aria-hidden="true"></i></button>
          <input id="ctc02-in" type="text" autocomplete="off" spellcheck="false" placeholder="Add a tag…">
        </label>
        <div class="ctc-02__suggest">
          <span>Suggested</span>
          <button type="button" data-tag="animation">animation</button>
          <button type="button" data-tag="ui-design">ui-design</button>
          <button type="button" data-tag="accessibility">accessibility</button>
          <button type="button" data-tag="oklch">oklch</button>
        </div>
        <p aria-live="polite" class="ctc-02__sr" id="ctc02-live"></p>
      </form>
      <ul class="ctc-02__why" aria-label="Why this pattern works">
        <li><b>Real buttons</b>Every chip is a 44px <code>&lt;button&gt;</code> — click or keyboard, same result.</li>
        <li><b>Live narration</b><code>aria-live</code> announces “Added css. 3 of 8 tags.”</li>
        <li><b>Physical validation</b>Duplicates shake the existing chip. Try adding <em>css</em> twice.</li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-02,
.ctc-02 *,
.ctc-02 *::before,
.ctc-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-02 {
  --bg: oklch(0.27 0.032 285);
  --card: oklch(0.985 0.004 285);
  --ink: oklch(0.25 0.03 285);
  --mut: oklch(0.52 0.02 285);
  --line: oklch(0.9 0.012 285);
  --acc: oklch(0.58 0.2 292);
  --warn: oklch(0.72 0.15 75);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-02__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 60cqi at 12% -8%,oklch(0.42 0.09 292/.6),transparent 62%),radial-gradient(60cqi 55cqi at 108% 108%,oklch(0.4 0.1 250/.55),transparent 60%),var(--bg);
  container: ctc02/inline-size;
}

.ctc-02__wrap {
  width: min(600px,100%);
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.ctc-02__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ctc-02__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.78 0.12 292);
}

.ctc-02__head {
  color: oklch(0.97 0.005 285);
}

.ctc-02__head h1 {
  font-size: clamp(26px,4cqi,40px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin-top: 8px;
}

.ctc-02__sub {
  margin-top: 10px;
  font-size: 13.5px;
  line-height: 1.6;
  color: oklch(0.78 0.02 285);
}

.ctc-02__head kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .82em;
  font-weight: 700;
  background: oklch(1 0 0/.12);
  border: 1px solid oklch(1 0 0/.2);
  border-bottom-width: 2px;
  border-radius: 6px;
  padding: 1px 7px;
}

.ctc-02__card {
  background: var(--card);
  border-radius: 20px;
  padding: clamp(18px,3cqi,26px);
  box-shadow: 0 30px 80px -30px oklch(0.1 0.03 285/.75),0 0 0 1px oklch(1 0 0/.1);
}

.ctc-02__row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 10px;
}

.ctc-02__lab {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .01em;
}

.ctc-02__count {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  font-weight: 700;
  color: var(--mut);
  background: oklch(0.94 0.008 285);
  padding: 4px 10px;
  border-radius: 99px;
  transition: background .2s,color .2s;
}

.ctc-02__card:has(.is-full) .ctc-02__count {
  color: oklch(0.48 0.13 75);
  background: color-mix(in oklch,var(--warn) 22%,transparent);
}

.ctc-02__field {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 7px;
  padding: 9px;
  border: 1.5px solid var(--line);
  border-radius: 14px;
  background: oklch(0.975 0.005 285);
  cursor: text;
  transition: border-color .2s,box-shadow .2s;
}

.ctc-02__field:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 4px color-mix(in oklch,var(--acc) 16%,transparent);
}

.ctc-02__field.is-full {
  border-color: var(--warn);
  box-shadow: 0 0 0 4px color-mix(in oklch,var(--warn) 18%,transparent);
}

.ctc-02__field input {
  flex: 1;
  min-width: 130px;
  min-height: 44px;
  border: 0;
  outline: 0;
  background: none;
  font: inherit;
  font-size: 14.5px;
  color: var(--ink);
  padding: 0 6px;
}

.ctc-02__field input::placeholder {
  color: color-mix(in oklch,var(--mut) 70%,transparent);
}

.ctc-02__tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 9px 0 15px;
  border: 0;
  border-radius: 11px;
  background: color-mix(in oklch,var(--acc) 12%,transparent);
  color: color-mix(in oklch,var(--acc) 75%,var(--ink));
  font: inherit;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  animation: ctc02-pop .35s cubic-bezier(.34,1.56,.64,1);
  transition: background .2s,color .2s,translate .2s;
}

.ctc-02__tag i {
  position: relative;
  width: 20px;
  height: 20px;
  border-radius: 7px;
  display: grid;
  place-items: center;
  background: color-mix(in oklch,var(--acc) 14%,transparent);
  transition: background .2s,rotate .25s;
}

.ctc-02__tag i::before,
.ctc-02__tag i::after {
  content: "";
  position: absolute;
  width: 9px;
  height: 1.8px;
  border-radius: 2px;
  background: currentColor;
}

.ctc-02__tag i::before {
  rotate: 45deg;
}

.ctc-02__tag i::after {
  rotate: -45deg;
}

.ctc-02__tag:hover,
.ctc-02__tag:focus-visible {
  background: oklch(0.32 0.05 292);
  color: oklch(0.97 0.005 285);
  translate: 0 -1px;
}

.ctc-02__tag:hover i,
.ctc-02__tag:focus-visible i {
  background: oklch(1 0 0/.16);
  rotate: 90deg;
}

.ctc-02__tag:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ctc-02__tag.is-dup {
  animation: ctc02-shake .4s;
}

.ctc-02__field.shake {
  animation: ctc02-shake .4s;
}

@keyframes ctc02-pop {
  from {
    scale: .6;
    opacity: 0;
  }
}

@keyframes ctc02-shake {
  20%,
    60% {
    translate: -5px 0;
  }

  40%,
    80% {
    translate: 5px 0;
  }
}

.ctc-02__suggest {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  margin-top: 16px;
  padding-top: 15px;
  border-top: 1px dashed var(--line);
}

.ctc-02__suggest span {
  font-size: 11px;
  font-weight: 800;
  color: var(--mut);
  text-transform: uppercase;
  letter-spacing: .09em;
}

.ctc-02__suggest button {
  min-height: 38px;
  padding: 0 14px;
  border-radius: 99px;
  border: 1.5px dashed color-mix(in oklch,var(--acc) 40%,var(--line));
  background: none;
  font: inherit;
  font-size: 13px;
  font-weight: 650;
  color: var(--mut);
  cursor: pointer;
  transition: border-color .2s,color .2s,background .2s,border-style .2s;
}

.ctc-02__suggest button::before {
  content: "+ ";
}

.ctc-02__suggest button:hover,
.ctc-02__suggest button:focus-visible {
  border-style: solid;
  border-color: var(--acc);
  color: var(--acc);
  background: color-mix(in oklch,var(--acc) 8%,transparent);
}

.ctc-02__suggest button:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ctc-02__why {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(160px,1fr));
  gap: 10px;
  list-style: none;
}

.ctc-02__why li {
  background: oklch(1 0 0/.07);
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 14px;
  padding: 13px 15px;
  font-size: 12px;
  line-height: 1.55;
  color: oklch(0.85 0.015 285);
}

.ctc-02__why b {
  display: block;
  font-size: 12.5px;
  color: oklch(0.98 0.005 285);
  margin-bottom: 3px;
}

.ctc-02__why code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  color: oklch(0.85 0.1 292);
}

@container ctc02 (width < 520px) {
  .ctc-02__why {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ctc-02 * {
    animation-duration: .01ms !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ctc-02');
  if (!root || root.dataset.init) return;
  root.dataset.init = '1';
  const field = root.querySelector('.ctc-02__field');
  const input = root.querySelector('#ctc02-in');
  const live = root.querySelector('#ctc02-live');
  const count = root.querySelector('#ctc02-count');
  const MAX = 8;
  const tags = () => [...field.querySelectorAll('.ctc-02__tag')];
  const say = (msg) => { live.textContent = msg + ' ' + tags().length + ' of ' + MAX + ' tags.'; };
  const update = () => {
    count.textContent = tags().length + '/' + MAX;
    field.classList.toggle('is-full', tags().length >= MAX);
  };
  const add = (raw) => {
    const t = raw.trim().replace(/,+$/, '').toLowerCase();
    if (!t) return;
    const dup = tags().find((el) => el.dataset.v === t);
    if (dup) { dup.classList.remove('is-dup'); void dup.offsetWidth; dup.classList.add('is-dup'); input.value = ''; return; }
    if (tags().length >= MAX) { field.classList.remove('shake'); void field.offsetWidth; field.classList.add('shake'); return; }
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'ctc-02__tag'; b.dataset.v = t;
    b.setAttribute('aria-label', 'Remove tag ' + t);
    const s = document.createElement('span'); s.textContent = t;
    const i = document.createElement('i'); i.setAttribute('aria-hidden', 'true');
    b.append(s, i);
    field.insertBefore(b, input);
    input.value = ''; update(); say('Added ' + t + '.');
  };
  const remove = (el) => { const t = el.dataset.v; el.remove(); update(); say('Removed ' + t + '.'); input.focus(); };
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ',') { e.preventDefault(); add(input.value); }
    else if (e.key === 'Backspace' && !input.value && tags().length) remove(tags().at(-1));
  });
  field.addEventListener('click', (e) => { const b = e.target.closest('.ctc-02__tag'); if (b) remove(b); else input.focus(); });
  root.querySelectorAll('.ctc-02__suggest [data-tag]').forEach((b) => b.addEventListener('click', () => add(b.dataset.tag)));
  update();
})();
```
