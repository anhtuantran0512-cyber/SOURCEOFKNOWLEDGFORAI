---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/progressive-disclosure-step-stack/"
title: "Progressive Disclosure Step Stack"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A multi-step form as a deck: the active step sits flat on top while future steps peek from behind."
has_js: "true"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Progressive Disclosure Step Stack
Source: https://codefronts.com/components/css-stacked-cards/progressive-disclosure-step-stack/

A multi-step form as a deck: the active step sits flat on top while future steps peek from behind. Pass validation and the current card drops to the back of the deck as the next one scales into focus — a friendlier alternative to a long scroll form.
## HTML
```html
<section class="scd-07" aria-label="Multi-step form stack">
  <div class="scd-07__wrap">
    <div class="scd-07__bar"><span id="scd-07-fill"></span></div>
    <form class="scd-07__deck" id="scd-07-deck" novalidate>
      <fieldset class="scd-07__card" data-step="0">
        <p class="scd-07__k">Step 1 of 3</p><h3>Your details</h3>
        <label>Full name<input required type="text" placeholder="Alex Rivera"></label>
        <label>Email<input required type="email" placeholder="[email protected]"></label>
        <div class="scd-07__row"><span></span><button type="button" class="scd-07__next">Continue</button></div>
      </fieldset>
      <fieldset class="scd-07__card" data-step="1">
        <p class="scd-07__k">Step 2 of 3</p><h3>Your project</h3>
        <label>Project name<input required type="text" placeholder="Northwind redesign"></label>
        <label>Budget<select required><option value="">Select…</option><option>&lt; $5k</option><option>$5k–$20k</option><option>$20k+</option></select></label>
        <div class="scd-07__row"><button type="button" class="scd-07__back">Back</button><button type="button" class="scd-07__next">Continue</button></div>
      </fieldset>
      <fieldset class="scd-07__card" data-step="2">
        <p class="scd-07__k">Step 3 of 3</p><h3>Almost done</h3>
        <label>Anything else?<textarea rows="3" placeholder="Timeline, links, context…"></textarea></label>
        <div class="scd-07__row"><button type="button" class="scd-07__back">Back</button><button type="button" class="scd-07__done">Submit ✓</button></div>
      </fieldset>
      <div class="scd-07__thanks" id="scd-07-thanks" hidden>Thanks — we'll be in touch within a day.</div>
    </form>
  </div>
</section>
```
## CSS
```css
.scd-07,
.scd-07 *,
.scd-07 *::before,
.scd-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-07 {
  --accent: oklch(0.62 0.17 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 50px 20px;
  background: #f2f3f7;
}

.scd-07__wrap {
  width: min(400px,100%);
}

.scd-07__bar {
  height: 6px;
  border-radius: 99px;
  background: #dde0e8;
  overflow: hidden;
  margin-bottom: 18px;
}

.scd-07__bar span {
  display: block;
  height: 100%;
  width: 33%;
  background: var(--accent);
  border-radius: 99px;
  transition: width .45s cubic-bezier(.3,.9,.3,1);
}

.scd-07__deck {
  position: relative;
  height: 340px;
}

.scd-07__card {
  position: absolute;
  inset: 0;
  border: none;
  background: #fff;
  border-radius: 20px;
  padding: 28px;
  box-shadow: 0 24px 50px -30px rgba(20,24,50,.5);
  display: flex;
  flex-direction: column;
  gap: 12px;
  transition: transform .5s cubic-bezier(.3,.9,.3,1),opacity .4s;
}

.scd-07__card[data-state="active"] {
  transform: translateY(0) scale(1);
  opacity: 1;
  z-index: 3;
}

.scd-07__card[data-state="next"] {
  transform: translateY(24px) scale(.93);
  opacity: .55;
  z-index: 2;
  pointer-events: none;
}

.scd-07__card[data-state="next2"] {
  transform: translateY(44px) scale(.86);
  opacity: .28;
  z-index: 1;
  pointer-events: none;
}

.scd-07__card[data-state="done"] {
  transform: translateY(80px) scale(.8);
  opacity: 0;
  z-index: 0;
  pointer-events: none;
}

.scd-07__k {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent);
}

.scd-07__card h3 {
  font-size: 23px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: #1a1d27;
}

.scd-07__card label {
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 13px;
  font-weight: 600;
  color: #4a4f5e;
}

.scd-07__card input,
.scd-07__card select,
.scd-07__card textarea {
  font: inherit;
  font-weight: 400;
  padding: 11px 13px;
  border: 1.5px solid #d6d9e2;
  border-radius: 11px;
  background: #f8f9fb;
  color: #1a1d27;
}

.scd-07__card input:focus,
.scd-07__card select:focus,
.scd-07__card textarea:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px oklch(0.62 0.17 250 / .18);
}

.scd-07__card input:user-invalid,
.scd-07__card select:user-invalid {
  border-color: oklch(0.62 0.2 22);
}

.scd-07__row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
}

.scd-07__next,
.scd-07__done {
  background: var(--accent);
  color: #fff;
  border: none;
  padding: 11px 20px;
  border-radius: 11px;
  font-weight: 700;
  font-size: 14px;
  cursor: pointer;
  transition: transform .12s,filter .2s;
}

.scd-07__next:hover,
.scd-07__done:hover {
  filter: brightness(1.08);
}

.scd-07__next:active,
.scd-07__done:active {
  transform: scale(.96);
}

.scd-07__back {
  background: none;
  border: none;
  color: #6a7080;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
}

.scd-07__back:hover {
  color: #1a1d27;
}

.scd-07__next:focus-visible,
.scd-07__done:focus-visible,
.scd-07__back:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
  border-radius: 11px;
}

.scd-07__thanks {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 30px;
  background: #fff;
  border-radius: 20px;
  font-size: 17px;
  font-weight: 600;
  color: #1a1d27;
  box-shadow: 0 24px 50px -30px rgba(20,24,50,.5);
  z-index: 4;
}

.scd-07__thanks[hidden] {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .scd-07__card,
    .scd-07__bar span {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.scd-07');
  const deck = root.querySelector('#scd-07-deck');
  const cards = [...deck.querySelectorAll('.scd-07__card')];
  const fill = root.querySelector('#scd-07-fill');
  const thanks = root.querySelector('#scd-07-thanks');
  let i = 0;
  function paint(){
    cards.forEach((c, idx) => {
      const s = idx < i ? 'done' : idx === i ? 'active' : idx === i+1 ? 'next' : 'next2';
      c.dataset.state = s;
      c.toggleAttribute('inert', idx !== i);
      c.setAttribute('aria-current', idx === i ? 'step' : 'false');
    });
    fill.style.width = ((i+1) / cards.length * 100) + '%';
    const first = cards[i].querySelector('input,select,textarea');
    if (first) setTimeout(() => first.focus(), 260);
  }
  function valid(card){
    const fields = [...card.querySelectorAll('input,select,textarea')];
    for (const f of fields){ if(!f.checkValidity()){ f.reportValidity(); return false; } }
    return true;
  }
  deck.addEventListener('click', e => {
    if (e.target.closest('.scd-07__next')){ if(valid(cards[i])){ i = Math.min(i+1, cards.length-1); paint(); } }
    if (e.target.closest('.scd-07__back')){ i = Math.max(i-1, 0); paint(); }
    if (e.target.closest('.scd-07__done')){
      if (valid(cards[i])){
        cards.forEach(c => { c.dataset.state='done'; c.setAttribute('inert',''); });
        fill.style.width='100%';
        thanks.hidden=false;
      }
    }
  });
  paint();
})();
```
