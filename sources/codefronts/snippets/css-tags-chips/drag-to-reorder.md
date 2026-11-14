---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/drag-to-reorder/"
title: "Draggable Tag List Reordering UI"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "Reorderable tags with no library — the HTML5 drag API for pointers, plus the part every tutorial skips: full keyboard reordering."
has_js: "true"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Draggable Tag List Reordering UI
Source: https://codefronts.com/snippets/css-tags-chips/drag-to-reorder/

Reorderable tags with no library — the HTML5 drag API for pointers, plus the part every tutorial skips: full keyboard reordering. Tab to a tag, press Space to lift it (the tag visibly floats), arrow keys walk it through the list, Space drops, Escape cancels — with every move announced through aria-live. Pointer drags compute the insertion point from cursor position, the lifted tag tilts 4° like a picked-up card, and neighbors shuffle aside with real transitions via a 10-line FLIP.
## HTML
```html
<section class="ctc-17" aria-label="Draggable tag reordering demo">
  <div class="ctc-17__stage">
    <div class="ctc-17__wrap">
      <header class="ctc-17__head">
        <p class="ctc-17__kicker">Drag to reorder · pointer + keyboard</p>
        <h1>Grab one. Mouse or Space bar.</h1>
        <p class="ctc-17__sub">Drag with the pointer, or Tab to a tag and press <kbd>Space</kbd> to lift, <kbd>←</kbd><kbd>→</kbd> to move, <kbd>Space</kbd> to drop, <kbd>Esc</kbd> to cancel.</p>
      </header>
      <div class="ctc-17__card">
        <p class="ctc-17__lab" id="ctc17-lab">Interview pipeline stages — priority order</p>
        <div class="ctc-17__list" role="list" aria-labelledby="ctc17-lab">
          <span class="ctc-17__tag" role="listitem" draggable="true" tabindex="0" style="--h:255"><i aria-hidden="true">⠿</i>screening</span>
          <span class="ctc-17__tag" role="listitem" draggable="true" tabindex="0" style="--h:200"><i aria-hidden="true">⠿</i>portfolio</span>
          <span class="ctc-17__tag" role="listitem" draggable="true" tabindex="0" style="--h:150"><i aria-hidden="true">⠿</i>pairing</span>
          <span class="ctc-17__tag" role="listitem" draggable="true" tabindex="0" style="--h:85"><i aria-hidden="true">⠿</i>system design</span>
          <span class="ctc-17__tag" role="listitem" draggable="true" tabindex="0" style="--h:40"><i aria-hidden="true">⠿</i>values</span>
          <span class="ctc-17__tag" role="listitem" draggable="true" tabindex="0" style="--h:320"><i aria-hidden="true">⠿</i>offer</span>
        </div>
        <p class="ctc-17__order">Current order: <output id="ctc17-out"></output></p>
        <p class="ctc-17__sr" aria-live="polite" id="ctc17-live"></p>
      </div>
      <ul class="ctc-17__why" aria-label="What makes this shippable">
        <li><b>Insertion by midpoint</b>dragover finds the first chip whose center is past the cursor — no index math.</li>
        <li><b>10-line FLIP</b>neighbors slide, not teleport: rect before, move, transform back to zero.</li>
        <li><b>Keyboard = first class</b>grab, walk, drop, cancel — every move narrated via <code>aria-live</code>.</li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-17,
.ctc-17 *,
.ctc-17 *::before,
.ctc-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-17 {
  --bg: oklch(0.96 0.01 260);
  --card: oklch(0.995 0.002 260);
  --ink: oklch(0.25 0.025 265);
  --mut: oklch(0.5 0.02 265);
  --line: oklch(0.88 0.012 260);
  --acc: oklch(0.55 0.18 262);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-17__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 10% -10%,color-mix(in oklch,var(--acc) 13%,transparent),transparent 62%),var(--bg);
  container: ctc17/inline-size;
}

.ctc-17__wrap {
  width: min(640px,100%);
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.ctc-17__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ctc-17__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.ctc-17__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 8px;
}

.ctc-17__sub {
  font-size: 13px;
  line-height: 1.6;
  color: var(--mut);
}

.ctc-17__sub kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .85em;
  font-weight: 700;
  background: oklch(1 0 0);
  border: 1px solid var(--line);
  border-bottom-width: 2px;
  border-radius: 5px;
  padding: 1px 6px;
}

.ctc-17__card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 18px;
  box-shadow: 0 20px 50px -30px oklch(0.3 0.05 265/.5);
}

.ctc-17__lab {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 13px;
}

.ctc-17__list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  min-height: 48px;
}

.ctc-17__tag {
  --c: oklch(0.6 0.14 var(--h,255));
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 17px 0 11px;
  border-radius: 12px;
  border: 1.5px solid color-mix(in oklch,var(--c) 30%,transparent);
  background: color-mix(in oklch,var(--c) 11%,oklch(1 0 0));
  color: color-mix(in oklch,var(--c) 72%,var(--ink));
  font-size: 13.5px;
  font-weight: 700;
  cursor: grab;
  user-select: none;
  transition: scale .2s,rotate .2s,box-shadow .2s,opacity .2s,border-color .2s;
}

.ctc-17__tag i {
  font-style: normal;
  font-size: 15px;
  opacity: .5;
  letter-spacing: -2px;
}

.ctc-17__tag:hover {
  border-color: color-mix(in oklch,var(--c) 55%,transparent);
  box-shadow: 0 6px 14px -8px var(--c);
}

.ctc-17__tag:focus-visible {
  outline: 2px solid var(--c);
  outline-offset: 2px;
}

.ctc-17__tag.is-drag {
  opacity: .35;
  scale: .97;
  cursor: grabbing;
}

.ctc-17__tag.is-grab {
  scale: 1.06;
  rotate: 4deg;
  box-shadow: 0 16px 30px -12px var(--c);
  border-color: var(--c);
  background: color-mix(in oklch,var(--c) 20%,oklch(1 0 0));
  z-index: 2;
}

.ctc-17__order {
  margin-top: 14px;
  padding-top: 13px;
  border-top: 1px dashed var(--line);
  font-size: 12.5px;
  color: var(--mut);
}

.ctc-17__order output {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  font-weight: 600;
  color: var(--ink);
}

.ctc-17__why {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(170px,1fr));
  gap: 10px;
  list-style: none;
}

.ctc-17__why li {
  background: oklch(1 0 0/.65);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 13px 15px;
  font-size: 12px;
  line-height: 1.55;
  color: var(--mut);
}

.ctc-17__why b {
  display: block;
  font-size: 12.5px;
  color: var(--ink);
  margin-bottom: 3px;
}

.ctc-17__why code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(0.93 0.008 260);
  padding: 1px 4px;
  border-radius: 4px;
}

@container ctc17 (width < 480px) {
  .ctc-17__why {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ctc-17 * {
    transition-duration: .01ms !important;
  }

  .ctc-17__tag.is-grab {
    rotate: 0deg;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ctc-17');
  if (!root || root.dataset.init) return;
  root.dataset.init = '1';
  const list = root.querySelector('.ctc-17__list');
  const live = root.querySelector('#ctc17-live');
  const out = root.querySelector('#ctc17-out');
  let dragging = null, grabbed = null, restore = null;
  const tags = () => [...list.querySelectorAll('.ctc-17__tag')];
  const names = () => tags().map((t) => t.textContent.replace('⠿', '').trim());
  const order = () => { out.textContent = names().join(' → '); };
  const pos = (el) => tags().indexOf(el) + 1;
  const say = (msg) => { live.textContent = msg; };
  const flip = (move) => {
    const before = new Map(tags().map((t) => [t, t.getBoundingClientRect()]));
    move();
    tags().forEach((t) => {
      const b = before.get(t); if (!b) return;
      const a = t.getBoundingClientRect();
      const dx = b.left - a.left, dy = b.top - a.top;
      if (!dx && !dy) return;
      t.animate([{ translate: dx + 'px ' + dy + 'px' }, { translate: '0 0' }], { duration: 220, easing: 'cubic-bezier(.2,.8,.2,1)' });
    });
    order();
  };
  list.addEventListener('dragstart', (e) => {
    dragging = e.target.closest('.ctc-17__tag');
    requestAnimationFrame(() => dragging && dragging.classList.add('is-drag'));
  });
  list.addEventListener('dragover', (e) => {
    e.preventDefault();
    if (!dragging) return;
    const after = tags().filter((t) => t !== dragging).find((t) => {
      const r = t.getBoundingClientRect();
      return e.clientY < r.top || (e.clientY <= r.bottom && e.clientX < r.left + r.width / 2);
    });
    if (after !== dragging.nextSibling) flip(() => (after ? list.insertBefore(dragging, after) : list.append(dragging)));
  });
  list.addEventListener('dragend', () => {
    if (!dragging) return;
    dragging.classList.remove('is-drag');
    say(dragging.textContent.replace('⠿', '').trim() + ' dropped at position ' + pos(dragging) + ' of ' + tags().length + '.');
    dragging = null; order();
  });
  list.addEventListener('keydown', (e) => {
    const tag = e.target.closest('.ctc-17__tag');
    if (!tag) return;
    const name = tag.textContent.replace('⠿', '').trim();
    if (e.key === ' ' || e.key === 'Enter') {
      e.preventDefault();
      if (grabbed === tag) {
        grabbed = null; restore = null; tag.classList.remove('is-grab'); tag.setAttribute('aria-pressed', 'false');
        say(name + ' dropped at position ' + pos(tag) + ' of ' + tags().length + '.');
      } else {
        if (grabbed) { grabbed.classList.remove('is-grab'); }
        grabbed = tag; restore = tags();
        tag.classList.add('is-grab'); tag.setAttribute('aria-pressed', 'true');
        say(name + ' grabbed. Position ' + pos(tag) + ' of ' + tags().length + '. Use arrow keys to move.');
      }
    } else if (grabbed === tag && (e.key === 'ArrowLeft' || e.key === 'ArrowRight')) {
      e.preventDefault();
      const sib = e.key === 'ArrowLeft' ? tag.previousElementSibling : tag.nextElementSibling;
      if (sib) {
        flip(() => (e.key === 'ArrowLeft' ? list.insertBefore(tag, sib) : list.insertBefore(sib, tag)));
        tag.focus();
        say(name + ' moved to position ' + pos(tag) + ' of ' + tags().length + '.');
      }
    } else if (grabbed === tag && e.key === 'Escape') {
      flip(() => restore.forEach((t) => list.append(t)));
      grabbed.classList.remove('is-grab'); grabbed.setAttribute('aria-pressed', 'false');
      say('Reorder cancelled. ' + name + ' back at position ' + pos(tag) + '.');
      grabbed = null; restore = null;
    }
  });
  order();
})();
```
