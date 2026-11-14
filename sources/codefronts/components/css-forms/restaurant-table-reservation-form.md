---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/restaurant-table-reservation-form/"
title: "Restaurant Table Reservation Form"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A fine-dining booking widget in candle-lit black and gold: a party-size stepper, a horizontally scrolling date strip built from radios with scroll-snap, a…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Restaurant Table Reservation Form
Source: https://codefronts.com/components/css-forms/restaurant-table-reservation-form/

A fine-dining booking widget in candle-lit black and gold: a party-size stepper, a horizontally scrolling date strip built from radios with scroll-snap, a time-slot grid where fully-booked slots are genuinely disabled (and say so), seating-area cards with photography, an occasion selector, and a live sentence summary — “Table for 4 · Fri 9 Oct · 8:00 pm · Terrace” — that updates as you choose.
## HTML
```html
<div class="frm-10">
  <button type="button" class="frm-10__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-10__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-10__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-10__stage">
    <div class="frm-10__card">
      <figure class="frm-10__hero">
        <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1000&h=500&fit=crop&auto=format&q=70" width="1000" height="500" alt="Warmly lit restaurant dining room with set tables" loading="lazy" decoding="async">
        <figcaption><span>Maison Ardent</span><small>Modern French · Mayfair, London</small></figcaption>
      </figure>
      <div class="frm-10__body" role="form" aria-labelledby="frm-10-title">
        <h2 id="frm-10-title">Reserve a table</h2>
        <div class="frm-10__party">
          <span id="frm-10-party-l">Guests</span>
          <div class="frm-10__stepper" role="group" aria-labelledby="frm-10-party-l">
            <button type="button" data-d="-1" aria-label="Fewer guests">−</button>
            <output aria-live="polite" class="frm-10__n">2</output>
            <button type="button" data-d="1" aria-label="More guests">+</button>
          </div>
        </div>
        <fieldset class="frm-10__fs"><legend>Date</legend><div class="frm-10__dates"></div></fieldset>
        <fieldset class="frm-10__fs"><legend>Time <span class="frm-10__avail"></span></legend><div class="frm-10__times"></div><p class="frm-10__large" hidden>For parties of 9 or more, please call <a href="tel:+442070000000">020 7000 0000</a>.</p></fieldset>
        <fieldset class="frm-10__fs">
          <legend>Seating</legend>
          <div class="frm-10__areas">
            <label><input type="radio" name="frm-10-area" value="Dining room" checked><img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=400&h=260&fit=crop&auto=format&q=60" width="400" height="260" alt="" loading="lazy" decoding="async"><span>Dining room</span></label>
            <label><input type="radio" name="frm-10-area" value="Terrace"><img src="https://images.unsplash.com/photo-1559339352-11d035aa65de?w=400&h=260&fit=crop&auto=format&q=60" width="400" height="260" alt="" loading="lazy" decoding="async"><span>Terrace</span></label>
            <label><input type="radio" name="frm-10-area" value="Chef's counter"><img src="https://images.unsplash.com/photo-1552566626-52f8b828add9?w=400&h=260&fit=crop&auto=format&q=60" width="400" height="260" alt="" loading="lazy" decoding="async"><span>Chef's counter</span></label>
          </div>
        </fieldset>
        <div class="frm-10__grid">
          <div class="frm-10__field"><label for="frm-10-name">Name</label><input id="frm-10-name" autocomplete="name" required></div>
          <div class="frm-10__field"><label for="frm-10-tel">Phone</label><input id="frm-10-tel" type="tel" autocomplete="tel" required></div>
        </div>
        <div class="frm-10__grid">
          <div class="frm-10__field"><label for="frm-10-occ">Occasion</label><select id="frm-10-occ"><option>None</option><option>Birthday</option><option>Anniversary</option><option>Business</option><option>Date night</option></select></div>
          <div class="frm-10__field"><label for="frm-10-req">Requests <span>Optional</span></label><input id="frm-10-req" placeholder="Allergies, high chair, quiet table…"></div>
        </div>
        <div class="frm-10__summary"><p role="status" class="frm-10__sum"></p><button type="button" class="frm-10__book">Confirm reservation</button></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Jost:wght@400;500;600&display=swap');

.frm-10 {
  --bg: #0d0b09;
  --card: #15120f;
  --raised: #1d1915;
  --ink: #f3ebdf;
  --muted: #a69a89;
  --line: #2e2821;
  --gold: #d4a95a;
  --gold-2: #f0d39a;
  --on-gold: #1a1206;
  --serif: "Cormorant Garamond",ui-serif,Georgia,serif;
  --sans: "Jost",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --ease: cubic-bezier(.16,1,.3,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(50rem 30rem at 50% 0%, #2a1e10, transparent 70%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.frm-10[data-theme="light"] {
  --bg: #f4eee4;
  --card: #fffaf2;
  --raised: #f6efe3;
  --ink: #2a2017;
  --muted: #7b6c5b;
  --line: #e5d9c6;
  --gold: #9a7232;
  --gold-2: #b88a3e;
  --on-gold: #fff;
  background: var(--bg);
}

.frm-10,
.frm-10 *,
.frm-10 *::before,
.frm-10 *::after {
  box-sizing: border-box;
}

.frm-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,5vw,4rem);
}

.frm-10__card {
  width: 100%;
  max-width: 40rem;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  overflow: hidden;
  box-shadow: 0 40px 90px -40px rgba(0,0,0,.9), 0 0 0 1px color-mix(in oklab,var(--gold) 12%,transparent);
}

.frm-10__hero {
  position: relative;
  margin: 0;
  height: 12rem;
  background: #2a1e10;
}

.frm-10__hero img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  filter: saturate(.9) contrast(1.05);
}

.frm-10__hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(transparent 20%, var(--card));
}

.frm-10__hero figcaption {
  position: absolute;
  z-index: 1;
  left: clamp(1.25rem,5vw,2.25rem);
  bottom: .5rem;
  display: grid;
}

.frm-10__hero figcaption span {
  font: 500 clamp(2rem,6vw,2.75rem)/1 var(--serif);
  letter-spacing: .01em;
  color: var(--gold-2);
}

.frm-10__hero small {
  font-size: .75rem;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--muted);
  margin-top: .3rem;
}

.frm-10__body {
  display: grid;
  gap: 1.4rem;
  padding: 1.25rem clamp(1.25rem,5vw,2.25rem) clamp(1.25rem,5vw,2.25rem);
}

.frm-10 h2 {
  margin: 0;
  font: italic 500 1.5rem var(--serif);
  color: var(--muted);
}

.frm-10__party {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: .75rem 1rem;
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: var(--raised);
}

.frm-10__party > span,
.frm-10 legend,
.frm-10 label {
  font-size: .75rem;
  font-weight: 500;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--muted);
}

.frm-10__stepper {
  display: flex;
  align-items: center;
  gap: .4rem;
}

.frm-10__stepper button {
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 50%;
  border: 1px solid var(--line);
  background: transparent;
  color: var(--gold-2);
  font-size: 1.25rem;
  cursor: pointer;
  transition: background .2s, border-color .2s;
}

.frm-10__stepper button:hover:not(:disabled) {
  border-color: var(--gold);
  background: color-mix(in oklab,var(--gold) 12%,transparent);
}

.frm-10__stepper button:disabled {
  opacity: .3;
  cursor: not-allowed;
}

.frm-10__stepper button:focus-visible {
  outline: 2px solid var(--gold);
  outline-offset: 2px;
}

.frm-10__n {
  min-width: 2.5rem;
  text-align: center;
  font: 600 1.75rem var(--serif);
  font-variant-numeric: lining-nums;
}

.frm-10__fs {
  border: 0;
  margin: 0;
  padding: 0;
  min-width: 0;
  display: grid;
  gap: .7rem;
}

.frm-10__fs legend {
  padding: 0;
  margin-bottom: .7rem;
  display: flex;
  gap: .6rem;
  align-items: baseline;
}

.frm-10__avail {
  letter-spacing: .04em;
  text-transform: none;
  color: var(--gold);
  font-size: .8rem;
}

.frm-10__dates {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 4.25rem;
  gap: .5rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scrollbar-width: none;
  padding: .2rem;
  margin: -.2rem;
  -webkit-mask: linear-gradient(90deg,#000 85%,transparent);
  mask: linear-gradient(90deg,#000 85%,transparent);
}

.frm-10__dates::-webkit-scrollbar {
  display: none;
}

.frm-10__dates label,
.frm-10__times label,
.frm-10__areas label {
  position: relative;
  letter-spacing: normal;
  text-transform: none;
}

.frm-10__dates label {
  scroll-snap-align: start;
}

.frm-10 :is(.frm-10__dates,.frm-10__times,.frm-10__areas) input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
  z-index: 1;
}

.frm-10__dates span {
  display: grid;
  justify-items: center;
  gap: .1rem;
  padding: .7rem 0;
  border-radius: 1rem;
  border: 1px solid var(--line);
  background: var(--raised);
  color: var(--ink);
  transition: all .25s var(--ease);
}

.frm-10__dates small {
  font-size: .66rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.frm-10__dates b {
  font: 600 1.6rem/1 var(--serif);
}

.frm-10__dates input:checked + span {
  background: linear-gradient(160deg,var(--gold-2),var(--gold));
  color: var(--on-gold);
  border-color: transparent;
  box-shadow: 0 10px 24px -12px var(--gold);
}

.frm-10__dates input:checked + span small {
  color: inherit;
  opacity: .8;
}

.frm-10 :is(.frm-10__dates,.frm-10__times) input:focus-visible + span {
  outline: 2px solid var(--gold-2);
  outline-offset: 2px;
}

.frm-10__times {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(5.25rem,1fr));
  gap: .45rem;
}

.frm-10__times span {
  display: grid;
  place-items: center;
  min-height: 2.75rem;
  border-radius: .7rem;
  border: 1px solid var(--line);
  color: var(--ink);
  font-size: .92rem;
  font-variant-numeric: tabular-nums;
  transition: all .2s;
}

.frm-10__times label:hover input:not(:disabled) + span {
  border-color: var(--gold);
}

.frm-10__times input:checked + span {
  background: color-mix(in oklab,var(--gold) 20%,transparent);
  border-color: var(--gold);
  color: var(--gold-2);
  font-weight: 600;
}

.frm-10__times input:disabled {
  cursor: not-allowed;
}

.frm-10__times input:disabled + span {
  text-decoration: line-through;
  opacity: .35;
}

.frm-10__times span {
  animation: frm-10-in .4s var(--ease) both;
  animation-delay: calc(var(--k,0) * 25ms);
}

@keyframes frm-10-in {
  from {
    opacity: 0;
    translate: 0 6px;
  }
}

.frm-10__large {
  margin: 0;
  color: var(--muted);
  font-size: .9rem;
}

.frm-10__large a {
  color: var(--gold-2);
}

.frm-10 a {
  color: var(--gold-2);
}

.frm-10 a:hover {
  color: var(--gold);
}

.frm-10__areas {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .6rem;
}

.frm-10__areas label {
  display: grid;
  border-radius: 1rem;
  overflow: hidden;
  border: 1px solid var(--line);
  background: var(--raised);
  transition: border-color .25s, box-shadow .25s;
}

.frm-10__areas img {
  width: 100%;
  aspect-ratio: 3/2;
  height: auto;
  object-fit: cover;
  display: block;
  background: #2a1e10;
  filter: grayscale(.6) brightness(.7);
  transition: filter .4s var(--ease), scale .6s var(--ease);
}

.frm-10__areas span {
  padding: .55rem .7rem;
  font-size: .85rem;
  color: var(--ink);
}

.frm-10__areas label:hover img {
  scale: 1.05;
}

.frm-10__areas label:has(:checked) {
  border-color: var(--gold);
  box-shadow: 0 0 0 1px var(--gold);
}

.frm-10__areas label:has(:checked) img {
  filter: none;
}

.frm-10__areas label:has(:focus-visible) {
  outline: 2px solid var(--gold-2);
  outline-offset: 2px;
}

@media (max-width: 30rem) {
  .frm-10__areas {
    grid-template-columns: 1fr;
  }

  .frm-10__areas label {
    grid-template-columns: 5rem 1fr;
    align-items: center;
  }
}

.frm-10__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,13rem),1fr));
}

.frm-10__field {
  display: grid;
  gap: .45rem;
}

.frm-10__field label span {
  text-transform: none;
  letter-spacing: 0;
  opacity: .7;
}

.frm-10__field input,
.frm-10__field select {
  width: 100%;
  min-height: 2.9rem;
  padding: .6rem .9rem;
  border-radius: .7rem;
  border: 1px solid var(--line);
  background: var(--raised);
  color: var(--ink);
  font: inherit;
  font-size: .95rem;
}

.frm-10__field :is(input,select):focus-visible {
  outline: none;
  border-color: var(--gold);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--gold) 22%,transparent);
}

.frm-10__field input:user-invalid {
  border-color: #e57373;
}

.frm-10__summary {
  display: grid;
  gap: .8rem;
  padding-top: 1.2rem;
  border-top: 1px solid var(--line);
}

.frm-10__sum {
  margin: 0;
  font: 500 1.25rem/1.3 var(--serif);
  color: var(--gold-2);
  text-align: center;
  text-wrap: balance;
}

.frm-10__book {
  min-height: 3.3rem;
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-size: .82rem;
  font-weight: 600;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--on-gold);
  background: linear-gradient(110deg,var(--gold),var(--gold-2),var(--gold));
  background-size: 200% 100%;
  transition: background-position .8s var(--ease), translate .2s var(--ease);
}

.frm-10__book:hover {
  background-position: 100% 0;
  translate: 0 -2px;
}

.frm-10__book:focus-visible {
  outline: 2px solid var(--gold-2);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .frm-10 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-10 :is(.frm-10__dates,.frm-10__times) input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .frm-10__areas label:has(:checked) {
    outline: 2px solid Highlight;
  }

  .frm-10__book {
    border: 1px solid ButtonText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-10 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-10__theme {
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

.frm-10__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-10__theme:active {
  transform: scale(.94);
}

.frm-10__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-10__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-10__theme .frm-10__sun,
.frm-10__theme[aria-pressed="true"] .frm-10__moon {
  display: none;
}

.frm-10__theme[aria-pressed="true"] .frm-10__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-10__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-10__theme {
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
  document.querySelectorAll('.frm-10').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : true);
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
  const root = document.querySelector('.frm-10');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const DAYS = 10, MAX = 12, SLOTS = ['17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00'];
  let party = 2;
  const wd = new Intl.DateTimeFormat('en-GB', { weekday: 'short' }), full = new Intl.DateTimeFormat('en-GB', { weekday: 'short', day: 'numeric', month: 'short' });
  const dates = $('.frm-10__dates'), times = $('.frm-10__times');
  const days = [...Array(DAYS)].map((_, i) => { const d = new Date(); d.setDate(d.getDate() + i); return d; });
  dates.innerHTML = days.map((d, i) => '<label><input type="radio" name="frm-10-date" value="' + i + '"' + (i === 0 ? ' checked' : '') + ' aria-label="' + full.format(d) + '"><span aria-hidden="true"><small>' + (i === 0 ? 'Today' : wd.format(d)) + '</small><b>' + d.getDate() + '</b></span></label>').join('');
  const fmt12 = (t) => { let [h, m] = t.split(':').map(Number); const ap = h >= 12 ? 'pm' : 'am'; h = h % 12 || 12; return h + ':' + String(m).padStart(2, '0') + ' ' + ap; };
  const isBooked = (dayIdx, slotIdx) => ((dayIdx * 7 + slotIdx * 3 + party * 5) % 10) < (party > 4 ? 6 : 3);
  const renderTimes = () => {
    const day = Number(root.querySelector('[name="frm-10-date"]:checked').value);
    const prev = (root.querySelector('[name="frm-10-time"]:checked') || {}).value;
    const large = party > 8;
    $('.frm-10__large').hidden = !large;
    times.hidden = large;
    times.innerHTML = SLOTS.map((t, i) => { const b = isBooked(day, i); return '<label><input type="radio" name="frm-10-time" value="' + t + '"' + (b ? ' disabled' : '') + (t === prev && !b ? ' checked' : '') + ' aria-label="' + fmt12(t) + (b ? ', fully booked' : '') + '"><span style="--k:' + i + '" aria-hidden="true">' + fmt12(t) + '</span></label>'; }).join('');
    const open = SLOTS.filter((_, i) => !isBooked(day, i)).length;
    $('.frm-10__avail').textContent = large ? '' : open + ' of ' + SLOTS.length + ' available';
    summary();
  };
  const summary = () => {
    const d = days[Number(root.querySelector('[name="frm-10-date"]:checked').value)];
    const t = root.querySelector('[name="frm-10-time"]:checked'), a = root.querySelector('[name="frm-10-area"]:checked').value;
    $('.frm-10__sum').textContent = 'Table for ' + party + ' · ' + full.format(d) + ' · ' + (t ? fmt12(t.value) : 'choose a time') + ' · ' + a;
  };
  root.querySelectorAll('.frm-10__stepper button').forEach((b) => b.addEventListener('click', () => {
    party = Math.max(1, Math.min(MAX, party + Number(b.dataset.d)));
    $('.frm-10__n').textContent = party;
    root.querySelector('[data-d="-1"]').disabled = party === 1; root.querySelector('[data-d="1"]').disabled = party === MAX;
    renderTimes();
  }));
  dates.addEventListener('change', renderTimes);
  root.addEventListener('change', (e) => { if (e.target.name === 'frm-10-time' || e.target.name === 'frm-10-area') summary(); });
  $('.frm-10__book').addEventListener('click', () => {
    if (!root.querySelector('[name="frm-10-time"]:checked')) { (times.querySelector('input:not(:disabled)') || $('.frm-10__book')).focus(); $('.frm-10__sum').textContent = 'Please choose a time.'; return; }
    const bad = [...root.querySelectorAll('[required]')].find((f) => !f.checkValidity());
    if (bad) { bad.reportValidity(); return; }
    $('.frm-10__sum').textContent = 'Confirmed — ' + $('.frm-10__sum').textContent + '. A confirmation text is on its way.';
    $('.frm-10__book').textContent = 'Reservation confirmed';
  });
  renderTimes();
})();
```
