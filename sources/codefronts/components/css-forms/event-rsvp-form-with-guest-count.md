---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/event-rsvp-form-with-guest-count/"
title: "Event RSVP Form with Guest Count"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "An elegant invitation-style RSVP: accept, decline or maybe as large radio cards; a guest-count stepper that generates a named row (with meal choice and child…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Event RSVP Form with Guest Count
Source: https://codefronts.com/components/css-forms/event-rsvp-form-with-guest-count/

An elegant invitation-style RSVP: accept, decline or maybe as large radio cards; a guest-count stepper that generates a named row (with meal choice and child toggle) for each extra guest and removes them cleanly; dietary chips; a song request for the dance floor; and a decline path that hides everything irrelevant and offers a note to the hosts — powered by :has() so the layout always matches the answer.
## HTML
```html
<div class="frm-13">
  <button type="button" class="frm-13__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-13__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-13__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-13__stage">
    <div class="frm-13__card">
      <figure class="frm-13__hero">
        <img src="https://images.unsplash.com/photo-1511795409834-ef04bbd61622?w=1000&h=520&fit=crop&auto=format&q=70" width="1000" height="520" alt="Candle-lit reception tables with flowers" loading="lazy" decoding="async">
      </figure>
      <div class="frm-13__body" role="form" aria-labelledby="frm-13-title">
        <header class="frm-13__invite">
          <p class="frm-13__kicker">Together with their families</p>
          <h2 id="frm-13-title">Amelia <span>&amp;</span> Theo</h2>
          <p class="frm-13__when">Saturday, 12 June 2027 · 4 pm<br>Hedsor House, Buckinghamshire</p>
          <p class="frm-13__by">Kindly reply by 1 May</p>
        </header>
        <div class="frm-13__field"><label for="frm-13-name">Your name</label><input id="frm-13-name" autocomplete="name" required placeholder="As written on your invitation"></div>
        <fieldset class="frm-13__attend">
          <legend>Will you be joining us?</legend>
          <label><input type="radio" name="frm-13-a" value="yes" checked><span><b>Joyfully accept</b><small>Count me in</small></span></label>
          <label><input type="radio" name="frm-13-a" value="maybe"><span><b>Not sure yet</b><small>I'll confirm soon</small></span></label>
          <label><input type="radio" name="frm-13-a" value="no"><span><b>Regretfully decline</b><small>Celebrating in spirit</small></span></label>
        </fieldset>
        <div class="frm-13__yes">
          <div class="frm-13__field"><label for="frm-13-meal">Your meal</label>
            <select id="frm-13-meal"><option>Herb-crusted lamb</option><option>Pan-roasted sea bass</option><option>Wild mushroom risotto (V)</option><option>Vegan garden plate (VG)</option></select></div>
          <div class="frm-13__count">
            <div><span id="frm-13-g-l" class="frm-13__lbl">Additional guests</span><small>Your invitation includes up to 3</small></div>
            <div class="frm-13__stepper" role="group" aria-labelledby="frm-13-g-l">
              <button type="button" data-d="-1" aria-label="Remove a guest" disabled>−</button>
              <output aria-live="polite">0</output>
              <button type="button" data-d="1" aria-label="Add a guest">+</button>
            </div>
          </div>
          <div class="frm-13__guests"></div>
          <fieldset class="frm-13__chips"><legend>Dietary needs in your party</legend>
            <label><input type="checkbox"><span>Gluten-free</span></label><label><input type="checkbox"><span>Nut allergy</span></label><label><input type="checkbox"><span>Dairy-free</span></label><label><input type="checkbox"><span>Halal</span></label><label><input type="checkbox"><span>Kosher</span></label>
          </fieldset>
          <div class="frm-13__field"><label for="frm-13-song">A song that'll get you dancing <span class="frm-13__opt">Optional</span></label><input id="frm-13-song" placeholder="e.g. September — Earth, Wind &amp; Fire"></div>
        </div>
        <div class="frm-13__no"><label for="frm-13-note">Leave a note for the couple</label><textarea id="frm-13-note" rows="3" placeholder="We'll miss you!"></textarea></div>
        <button type="button" class="frm-13__send">Send RSVP</button>
        <p class="frm-13__status" role="status"></p>
      </div>
    </div>
  </div>
  <template class="frm-13__tpl">
    <div class="frm-13__guest">
      <span class="frm-13__gnum" aria-hidden="true"></span>
      <div class="frm-13__field"><label data-for="gn">Guest name</label><input data-id="gn" placeholder="Full name"></div>
      <div class="frm-13__field"><label data-for="gm">Meal</label><select data-id="gm"><option>Herb-crusted lamb</option><option>Pan-roasted sea bass</option><option>Wild mushroom risotto (V)</option><option>Vegan garden plate (VG)</option><option>Children's menu</option></select></div>
    </div>
  </template>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400&family=Manrope:wght@400;500;600;700&display=swap');

.frm-13 {
  --bg: #efe9df;
  --card: #fffdf8;
  --ink: #231d17;
  --muted: #7a6f63;
  --line: #e8dfd1;
  --soft: #f8f4ec;
  --accent: #3f4a3c;
  --on-accent: #fdfaf3;
  --foil: linear-gradient(100deg,#a07a3c,#e6c983 35%,#b08a48 60%,#f2dca2);
  --serif: "Bodoni Moda",ui-serif,Didot,Georgia,serif;
  --sans: "Manrope",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --ease: cubic-bezier(.16,1,.3,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(circle at 20% 20%, #f7f1e6, transparent 50%), radial-gradient(circle at 80% 80%, #e5dccd, transparent 55%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: dark) {
  .frm-13:not([data-theme="light"]) {
    --bg: #141210;
    --card: #1c1916;
    --ink: #f1e9dc;
    --muted: #a99d8e;
    --line: #332d26;
    --soft: #221e1a;
    --accent: #c9d3b8;
    --on-accent: #171a14;
    background: var(--bg);
  }
}

.frm-13[data-theme="dark"] {
  --bg: #141210;
  --card: #1c1916;
  --ink: #f1e9dc;
  --muted: #a99d8e;
  --line: #332d26;
  --soft: #221e1a;
  --accent: #c9d3b8;
  --on-accent: #171a14;
  background: var(--bg);
}

.frm-13,
.frm-13 *,
.frm-13 *::before,
.frm-13 *::after {
  box-sizing: border-box;
}

.frm-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,5vw,4rem);
}

.frm-13__card {
  position: relative;
  width: 100%;
  max-width: 36rem;
  background: var(--card);
  border-radius: .5rem;
  overflow: hidden;
  box-shadow: 0 1px 0 var(--line), 0 40px 80px -40px rgba(50,35,15,.5);
}

.frm-13__card::before {
  content: '';
  position: absolute;
  inset: .6rem;
  border: 1px solid color-mix(in oklab,#b08a48 45%,transparent);
  border-radius: .25rem;
  pointer-events: none;
  z-index: 2;
}

.frm-13__hero {
  margin: 0;
  height: 11rem;
  background: #cdbfa8;
}

.frm-13__hero img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.frm-13__body {
  display: grid;
  gap: 1.3rem;
  padding: clamp(1.5rem,6vw,2.75rem);
}

.frm-13__invite {
  text-align: center;
  display: grid;
  gap: .5rem;
  padding-bottom: 1.4rem;
  border-bottom: 1px solid var(--line);
}

.frm-13__kicker,
.frm-13__by {
  margin: 0;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--muted);
}

.frm-13 h2 {
  margin: .2rem 0;
  font: 400 clamp(2.4rem,9vw,3.5rem)/1 var(--serif);
  letter-spacing: -.01em;
  background: var(--foil);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  background-size: 200% 100%;
  animation: frm-13-foil 6s ease-in-out infinite alternate;
}

.frm-13 h2 span {
  font-style: italic;
}

@keyframes frm-13-foil {
  to {
    background-position: 100% 0;
  }
}

.frm-13__when {
  margin: 0;
  font: italic 400 1.1rem/1.5 var(--serif);
}

.frm-13__field {
  display: grid;
  gap: .4rem;
}

.frm-13 label,
.frm-13 legend,
.frm-13__lbl {
  font-size: .82rem;
  font-weight: 600;
}

.frm-13__opt {
  font-weight: 400;
  color: var(--muted);
}

.frm-13 input:not([type="radio"]):not([type="checkbox"]),
.frm-13 select,
.frm-13 textarea {
  width: 100%;
  min-height: 2.9rem;
  padding: .6rem .1rem;
  border: 0;
  border-bottom: 1px solid var(--line);
  border-radius: 0;
  background: transparent;
  color: var(--ink);
  font: inherit;
  font-size: 1rem;
  transition: border-color .2s;
}

.frm-13 select {
  cursor: pointer;
}

.frm-13 textarea {
  border: 1px solid var(--line);
  border-radius: .4rem;
  padding: .7rem .85rem;
  resize: vertical;
}

.frm-13 :is(input,select,textarea):focus-visible {
  outline: none;
  border-color: var(--ink);
  box-shadow: 0 1px 0 var(--ink);
}

.frm-13 textarea:focus-visible {
  box-shadow: 0 0 0 1px var(--ink);
}

.frm-13 input:user-invalid {
  border-color: #b42318;
}

.frm-13 fieldset {
  border: 0;
  margin: 0;
  padding: 0;
  min-width: 0;
}

.frm-13 legend {
  padding: 0;
  margin-bottom: .65rem;
}

.frm-13__attend {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .5rem;
}

.frm-13__attend label {
  position: relative;
}

.frm-13__attend input,
.frm-13__chips input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
  z-index: 1;
}

.frm-13__attend span {
  display: grid;
  gap: .2rem;
  height: 100%;
  padding: 1rem .8rem;
  text-align: center;
  border: 1px solid var(--line);
  border-radius: .4rem;
  background: var(--soft);
  transition: all .3s var(--ease);
}

.frm-13__attend b {
  font: 400 1rem/1.2 var(--serif);
}

.frm-13__attend small {
  font-size: .72rem;
  color: var(--muted);
}

.frm-13__attend input:checked + span {
  background: var(--accent);
  color: var(--on-accent);
  border-color: var(--accent);
}

.frm-13__attend input:checked + span small {
  color: inherit;
  opacity: .75;
}

.frm-13__attend input:focus-visible + span {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

@media (max-width: 28rem) {
  .frm-13__attend {
    grid-template-columns: 1fr;
  }
}

.frm-13__yes {
  display: grid;
  gap: 1.3rem;
}

.frm-13__no {
  display: none;
  gap: .5rem;
}

.frm-13:has([value="no"]:checked) .frm-13__yes {
  display: none;
}

.frm-13:has([value="no"]:checked) .frm-13__no {
  display: grid;
  animation: frm-13-in .4s var(--ease);
}

@keyframes frm-13-in {
  from {
    opacity: 0;
    translate: 0 8px;
  }
}

.frm-13__count {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .9rem 1rem;
  border: 1px solid var(--line);
  border-radius: .4rem;
  background: var(--soft);
}

.frm-13__count small {
  display: block;
  font-size: .78rem;
  color: var(--muted);
  margin-top: .15rem;
}

.frm-13__stepper {
  display: flex;
  align-items: center;
  gap: .3rem;
}

.frm-13__stepper button {
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 50%;
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--ink);
  font-size: 1.2rem;
  cursor: pointer;
  transition: background .2s, border-color .2s;
}

.frm-13__stepper button:hover:not(:disabled) {
  border-color: var(--ink);
}

.frm-13__stepper button:disabled {
  opacity: .35;
  cursor: not-allowed;
}

.frm-13__stepper button:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.frm-13__stepper output {
  min-width: 2rem;
  text-align: center;
  font: 400 1.6rem var(--serif);
}

.frm-13__guests {
  display: grid;
  gap: .75rem;
}

.frm-13__guests:empty {
  display: none;
}

.frm-13__guest {
  display: grid;
  grid-template-columns: auto 1fr 1fr;
  gap: .9rem;
  align-items: end;
  padding: .25rem 0 .5rem;
  transition: opacity .45s var(--ease), translate .45s var(--ease);
}

@starting-style {
  .frm-13__guest {
    opacity: 0;
    translate: 0 10px;
  }
}

.frm-13__gnum {
  display: grid;
  place-items: center;
  width: 2rem;
  height: 2rem;
  margin-bottom: .45rem;
  border-radius: 50%;
  font: italic 400 .95rem var(--serif);
  border: 1px solid color-mix(in oklab,#b08a48 60%,transparent);
  color: #a07a3c;
}

@media (max-width: 28rem) {
  .frm-13__guest {
    grid-template-columns: auto 1fr;
  }

  .frm-13__guest .frm-13__field:last-child {
    grid-column: 2;
  }
}

.frm-13__chips {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
}

.frm-13__chips legend {
  width: 100%;
}

.frm-13__chips label {
  position: relative;
}

.frm-13__chips span {
  display: inline-flex;
  align-items: center;
  min-height: 2.4rem;
  padding: 0 .9rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  font-size: .82rem;
  font-weight: 500;
  transition: all .2s;
}

.frm-13__chips input:checked + span {
  border-color: var(--ink);
  background: var(--ink);
  color: var(--card);
}

.frm-13__chips input:focus-visible + span {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.frm-13__send {
  min-height: 3.2rem;
  border: 0;
  border-radius: .35rem;
  cursor: pointer;
  font: inherit;
  font-size: .8rem;
  font-weight: 700;
  letter-spacing: .24em;
  text-transform: uppercase;
  background: var(--accent);
  color: var(--on-accent);
  transition: filter .2s, translate .2s var(--ease);
}

.frm-13__send:hover {
  filter: brightness(1.12);
  translate: 0 -1px;
}

.frm-13__send:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.frm-13__status {
  margin: -.4rem 0 0;
  text-align: center;
  font: italic 400 1.1rem var(--serif);
}

.frm-13__status:empty {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .frm-13 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-13 h2 {
    color: CanvasText;
    background: none;
  }

  .frm-13__attend input:checked + span,
    .frm-13__chips input:checked + span {
    background: Highlight;
    color: HighlightText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-13 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-13__theme {
  position: absolute;
  top: 16px;
  right: 16px;
  z-index: 20;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in srgb, currentColor 22%, transparent);
  background: color-mix(in srgb, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background-color .2s, transform .2s;
}

.frm-13__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-13__theme:active {
  transform: scale(.94);
}

.frm-13__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-13__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-13__theme .frm-13__sun,
.frm-13__theme[aria-pressed="true"] .frm-13__moon {
  display: none;
}

.frm-13__theme[aria-pressed="true"] .frm-13__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-13__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-13__theme {
    border-color: ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.frm-13').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : mq.matches);
    const sync = () => {
      const dark = isDark();
      btn.setAttribute('aria-pressed', String(dark));
      btn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    };
    btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
    mq.addEventListener('change', sync);
    new MutationObserver(sync).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    sync();
  });
})();
(() => {
  const root = document.querySelector('.frm-13');
  if (!root) return;
  const MAX = 3;
  const wrap = root.querySelector('.frm-13__guests'), tpl = root.querySelector('.frm-13__tpl'), out = root.querySelector('.frm-13__stepper output');
  const minus = root.querySelector('[data-d="-1"]'), plus = root.querySelector('[data-d="1"]');
  let n = 0;
  const addRow = (k) => {
    const row = tpl.content.firstElementChild.cloneNode(true);
    row.querySelector('.frm-13__gnum').textContent = k;
    row.querySelectorAll('[data-id]').forEach((el) => { el.id = 'frm-13-' + el.dataset.id + '-' + k; });
    row.querySelectorAll('[data-for]').forEach((el) => { el.htmlFor = 'frm-13-' + el.dataset.for + '-' + k; el.textContent += ' ' + k; });
    wrap.append(row);
    return row;
  };
  const set = (next) => {
    next = Math.max(0, Math.min(MAX, next));
    if (next > n) { for (let k = n + 1; k <= next; k++) { const r = addRow(k); if (k === next) r.querySelector('input').focus(); } }
    else { while (wrap.children.length > next) wrap.lastElementChild.remove(); }
    n = next; out.textContent = n; minus.disabled = n === 0; plus.disabled = n === MAX;
  };
  minus.addEventListener('click', () => { set(n - 1); if (minus.disabled) plus.focus(); });
  plus.addEventListener('click', () => { set(n + 1); });
  root.querySelector('.frm-13__send').addEventListener('click', () => {
    const name = root.querySelector('#frm-13-name'), status = root.querySelector('.frm-13__status');
    if (!name.value.trim()) { name.focus(); name.reportValidity(); return; }
    const a = root.querySelector('[name="frm-13-a"]:checked').value, first = name.value.trim().split(' ')[0];
    status.textContent = a === 'no' ? 'Thank you, ' + first + ' — you will be missed.' : a === 'maybe' ? 'Thanks, ' + first + '. We\'ll hold a place until 1 May.' : 'Wonderful! See you there, ' + first + (n ? ' + ' + n + ' guest' + (n > 1 ? 's' : '') : '') + '.';
  });
})();
```
