---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/event-and-conference-registration/"
title: "Event & Conference Registration"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A vibrant conference registration flow — Contact → Tickets → Add-ons → Summary — with quantity steppers on ticket tiers, add-on toggle cards, and a running…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Event & Conference Registration
Source: https://codefronts.com/components/css-multi-step-form/event-and-conference-registration/

A vibrant conference registration flow — Contact → Tickets → Add-ons → Summary — with quantity steppers on ticket tiers, add-on toggle cards, and a running total that animates in the footer of every step. The total being always-visible is the trick: attendees never hit a surprise price at the end.
## HTML
```html
<section class="msf-07" aria-label="Event registration demo">
  <form class="msf-07__card" novalidate>
    <header class="msf-07__head">
      <div class="msf-07__brand"><b class="msf-07__glyph">◢◤</b><div><h3>FRONTIER CONF 2027</h3><p>Mar 12–14 · Austin, TX</p></div></div>
      <ol class="msf-07__mini"><li class="is-active" aria-current="step">Contact</li><li>Tickets</li><li>Add-ons</li><li>Summary</li></ol>
    </header>
    <fieldset class="msf-07__step">
      <h4 class="msf-07__title" tabindex="-1">Who's the primary contact?</h4>
      <div class="msf-07__grid">
        <label class="msf-07__field"><span>Full name</span><input type="text" name="name" autocomplete="name" required placeholder="Dana Whitfield"></label>
        <label class="msf-07__field"><span>Email</span><input type="email" name="email" autocomplete="email" required placeholder="[email protected]"></label>
        <label class="msf-07__field msf-07__field--full"><span>Company <em>(shows on badges)</em></span><input type="text" name="company" autocomplete="organization" placeholder="Studio North"></label>
      </div>
      <div class="msf-07__nav"><span></span><button type="button" class="msf-07__next">Choose tickets</button></div>
    </fieldset>
    <fieldset class="msf-07__step" hidden>
      <h4 class="msf-07__title" tabindex="-1">Pick your tickets</h4>
      <div class="msf-07__tickets">
        <div class="msf-07__ticket" data-price="349"><div><b>General</b><small>All talks + expo floor</small></div><span class="msf-07__price">$349</span>
          <div class="msf-07__qty"><button type="button" class="msf-07__minus" aria-label="Fewer General tickets">−</button><input type="text" name="qty-general" value="1" readonly aria-label="General ticket quantity"><button type="button" class="msf-07__plus" aria-label="More General tickets">+</button></div></div>
        <div class="msf-07__ticket msf-07__ticket--vip" data-price="749"><div><b>VIP <i>Popular</i></b><small>Front rows, speaker dinner, lounge</small></div><span class="msf-07__price">$749</span>
          <div class="msf-07__qty"><button type="button" class="msf-07__minus" aria-label="Fewer VIP tickets">−</button><input type="text" name="qty-vip" value="0" readonly aria-label="VIP ticket quantity"><button type="button" class="msf-07__plus" aria-label="More VIP tickets">+</button></div></div>
        <div class="msf-07__ticket" data-price="149"><div><b>Online</b><small>Live stream + recordings</small></div><span class="msf-07__price">$149</span>
          <div class="msf-07__qty"><button type="button" class="msf-07__minus" aria-label="Fewer Online tickets">−</button><input type="text" name="qty-online" value="0" readonly aria-label="Online ticket quantity"><button type="button" class="msf-07__plus" aria-label="More Online tickets">+</button></div></div>
      </div>
      <div class="msf-07__nav"><button type="button" class="msf-07__back">Back</button><button type="button" class="msf-07__next">Add-ons</button></div>
    </fieldset>
    <fieldset class="msf-07__step" hidden>
      <h4 class="msf-07__title" tabindex="-1">Make it a trip</h4>
      <div class="msf-07__addons">
        <label class="msf-07__addon" data-price="89"><input type="checkbox" name="addon" value="Workshop day"><div><b>Workshop day</b><small>Hands-on, day 0</small></div><span>+$89</span></label>
        <label class="msf-07__addon" data-price="45"><input type="checkbox" name="addon" value="After-party"><div><b>After-party</b><small>Rooftop, day 2</small></div><span>+$45</span></label>
        <label class="msf-07__addon" data-price="25"><input type="checkbox" name="addon" value="Swag kit"><div><b>Swag kit</b><small>Tee, cap, stickers</small></div><span>+$25</span></label>
      </div>
      <div class="msf-07__nav"><button type="button" class="msf-07__back">Back</button><button type="button" class="msf-07__next">Review order</button></div>
    </fieldset>
    <fieldset class="msf-07__step" hidden>
      <h4 class="msf-07__title" tabindex="-1">Your order</h4>
      <ul class="msf-07__lines"></ul>
      <div class="msf-07__nav"><button type="button" class="msf-07__back">Back</button><button type="button" class="msf-07__next msf-07__next--go">Pay &amp; register</button></div>
    </fieldset>
    <div class="msf-07__done" hidden><b>◢◤</b><h4 tabindex="-1">See you in Austin!</h4><p>Tickets and calendar holds are in your inbox.</p></div>
    <footer class="msf-07__foot"><span>Order total</span><b class="msf-07__total" aria-live="polite">$349</b></footer>
  </form>
</section>
```
## CSS
```css
.msf-07,
.msf-07 *,
.msf-07 *::before,
.msf-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-07 {
  width: 100%;
  min-height: 100vh;
  --pop: oklch(0.62 0.24 305);
  --pop2: oklch(0.7 0.19 40);
  --bg: oklch(0.15 0.02 300);
  --panel: oklch(0.19 0.022 300);
  --line: oklch(0.3 0.025 300);
  --txt: oklch(0.94 0.005 300);
  --mut: oklch(0.66 0.02 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--txt);
  padding: 48px 20px;
  background: radial-gradient(90% 120% at 15% 0%,oklch(0.24 0.07 305/.8),transparent 60%),radial-gradient(80% 100% at 100% 100%,oklch(0.22 0.06 40/.7),transparent 55%),var(--bg);
  display: grid;
  place-items: center;
}

.msf-07__card {
  width: min(620px,100%);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 40px 90px -40px rgb(0 0 0/.7);
}

.msf-07__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  padding: 22px 28px;
  border-bottom: 1px solid var(--line);
}

.msf-07__brand {
  display: flex;
  gap: 12px;
  align-items: center;
}

.msf-07__glyph {
  font-size: 20px;
  background: linear-gradient(90deg,var(--pop),var(--pop2));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.msf-07__brand h3 {
  font-size: 15px;
  letter-spacing: .06em;
}

.msf-07__brand p {
  font-size: 12px;
  color: var(--mut);
}

.msf-07__mini {
  display: flex;
  gap: 14px;
  list-style: none;
  font-size: 11.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .06em;
  color: var(--mut);
}

.msf-07__mini li {
  position: relative;
  padding-bottom: 4px;
}

.msf-07__mini li.is-active {
  color: var(--txt);
}

.msf-07__mini li.is-active::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 2px;
  border-radius: 2px;
  background: linear-gradient(90deg,var(--pop),var(--pop2));
}

.msf-07__mini li.is-done {
  color: var(--pop);
}

.msf-07__step {
  border: none;
  padding: 26px 28px;
}

.msf-07__step:not([hidden]) {
  animation: msf-07-in .35s cubic-bezier(.2,.8,.2,1);
}

.msf-07__title {
  font-size: 20px;
  letter-spacing: -.01em;
  margin-bottom: 18px;
  outline: none;
}

.msf-07__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

@media (max-width: 520px) {
  .msf-07__grid {
    grid-template-columns: 1fr;
  }
}

.msf-07__field {
  display: grid;
  gap: 6px;
  font-size: 12px;
  font-weight: 700;
  color: var(--mut);
}

.msf-07__field em {
  font-style: normal;
  font-weight: 400;
}

.msf-07__field--full {
  grid-column: 1/-1;
}

.msf-07__field input {
  font: inherit;
  font-weight: 500;
  color: var(--txt);
  padding: 11px 13px;
  background: oklch(0.15 0.02 300);
  border: 1.5px solid var(--line);
  border-radius: 10px;
  transition: border-color .2s,box-shadow .2s;
}

.msf-07__field input:focus-visible {
  outline: none;
  border-color: var(--pop);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--pop) 20%,transparent);
}

.msf-07__field input[aria-invalid="true"] {
  border-color: oklch(0.62 0.2 25);
}

.msf-07__err {
  grid-column: 1/-1;
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.74 0.15 25);
}

.msf-07__tickets {
  display: grid;
  gap: 10px;
}

.msf-07__ticket {
  display: grid;
  grid-template-columns: 1fr auto auto;
  gap: 14px;
  align-items: center;
  padding: 16px 18px;
  border: 1.5px solid var(--line);
  border-radius: 14px;
  background: oklch(0.165 0.02 300);
}

.msf-07__ticket--vip {
  border-color: color-mix(in oklab,var(--pop) 55%,var(--line));
  background: linear-gradient(120deg,color-mix(in oklab,var(--pop) 12%,transparent),transparent 60%),oklch(0.165 0.02 300);
}

.msf-07__ticket b {
  font-size: 15px;
  display: flex;
  gap: 8px;
  align-items: center;
}

.msf-07__ticket b i {
  font-style: normal;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--pop),var(--pop2));
  color: #fff;
}

.msf-07__ticket small {
  font-size: 12px;
  color: var(--mut);
}

.msf-07__price {
  font-size: 16px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.msf-07__qty {
  display: flex;
  align-items: center;
  gap: 2px;
  border: 1.5px solid var(--line);
  border-radius: 99px;
  padding: 3px;
}

.msf-07__qty button {
  width: 28px;
  height: 28px;
  border: none;
  border-radius: 50%;
  background: none;
  color: var(--txt);
  font-size: 16px;
  cursor: pointer;
  transition: background .15s;
}

.msf-07__qty button:hover {
  background: var(--line);
}

.msf-07__qty button:focus-visible {
  outline: 2px solid var(--pop);
  outline-offset: 1px;
}

.msf-07__qty input {
  width: 30px;
  text-align: center;
  font: inherit;
  font-weight: 800;
  color: var(--txt);
  background: none;
  border: none;
  font-variant-numeric: tabular-nums;
}

.msf-07__addons {
  display: grid;
  gap: 10px;
}

.msf-07__addon {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 12px;
  align-items: center;
  padding: 15px 18px;
  border: 1.5px solid var(--line);
  border-radius: 14px;
  cursor: pointer;
  background: oklch(0.165 0.02 300);
  transition: border-color .2s,background .2s;
}

.msf-07__addon input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-07__addon b {
  font-size: 14.5px;
  display: block;
}

.msf-07__addon small {
  font-size: 12px;
  color: var(--mut);
}

.msf-07__addon>span {
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  color: var(--mut);
}

.msf-07__addon:hover {
  border-color: color-mix(in oklab,var(--pop) 45%,var(--line));
}

.msf-07__addon:has(:checked) {
  border-color: var(--pop);
  background: color-mix(in oklab,var(--pop) 10%,oklch(0.165 0.02 300));
}

.msf-07__addon:has(:checked)>span {
  color: var(--pop);
}

.msf-07__addon:has(:checked) b::after {
  content: " ✓";
  color: var(--pop);
}

.msf-07__addon:has(:focus-visible) {
  outline: 3px solid var(--pop);
  outline-offset: 2px;
}

.msf-07__lines {
  list-style: none;
  display: grid;
  gap: 8px;
  font-size: 14px;
}

.msf-07__lines li {
  display: flex;
  justify-content: space-between;
  gap: 14px;
  padding: 11px 14px;
  background: oklch(0.165 0.02 300);
  border-radius: 10px;
  font-variant-numeric: tabular-nums;
}

.msf-07__lines li.is-total {
  border: 1.5px solid color-mix(in oklab,var(--pop) 45%,var(--line));
  font-weight: 800;
  font-size: 15px;
}

.msf-07__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 22px;
}

.msf-07__next,
.msf-07__back {
  font: inherit;
  font-weight: 800;
  cursor: pointer;
  border-radius: 999px;
  padding: 12px 24px;
  transition: transform .15s,filter .2s;
}

.msf-07__next {
  border: none;
  color: #fff;
  background: linear-gradient(90deg,var(--pop),var(--pop2));
  box-shadow: 0 12px 30px -12px var(--pop);
}

.msf-07__next:hover {
  transform: translateY(-1px);
  filter: brightness(1.1);
}

.msf-07__next:disabled {
  opacity: .45;
  cursor: not-allowed;
  transform: none;
}

.msf-07__back {
  border: 1.5px solid var(--line);
  background: none;
  color: var(--mut);
}

.msf-07__back:hover {
  color: var(--txt);
}

.msf-07__next:focus-visible,
.msf-07__back:focus-visible {
  outline: 3px solid var(--pop);
  outline-offset: 2px;
}

.msf-07__done[hidden] {
  display: none;
}

.msf-07__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 36px 0;
}

.msf-07__done b {
  font-size: 30px;
  background: linear-gradient(90deg,var(--pop),var(--pop2));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: msf-07-pop .5s cubic-bezier(.34,1.56,.64,1);
}

.msf-07__done p {
  color: var(--mut);
  font-size: 14px;
}

.msf-07__foot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 28px;
  border-top: 1px dashed var(--line);
  background: oklch(0.165 0.02 300);
  font-size: 13px;
  color: var(--mut);
}

.msf-07__total {
  font-size: 20px;
  font-weight: 800;
  color: var(--txt);
  font-variant-numeric: tabular-nums;
  background: linear-gradient(90deg,var(--pop),var(--pop2));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

@keyframes msf-07-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-07-pop {
  from {
    transform: scale(.4) rotate(-8deg);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-07 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-07'); if (!root) return;
  const form = root.querySelector('.msf-07__card');
  const steps = [...root.querySelectorAll('.msf-07__step')];
  const mini = [...root.querySelectorAll('.msf-07__mini li')];
  const total = root.querySelector('.msf-07__total');
  let cur = 0;
  const fmt = n => '$' + n.toLocaleString('en-US');
  const order = () => {
    const lines = [];
    root.querySelectorAll('.msf-07__ticket').forEach(t => {
      const q = +t.querySelector('input').value;
      if (q > 0) lines.push([q + '\u00d7 ' + t.querySelector('b').firstChild.textContent.trim(), q * +t.dataset.price]);
    });
    root.querySelectorAll('.msf-07__addon:has(:checked)').forEach(a => lines.push([a.querySelector('b').textContent.replace(' \u2713',''), +a.dataset.price]));
    return lines;
  };
  const recalc = () => {
    const lines = order();
    const sum = lines.reduce((s,[,p]) => s+p, 0);
    total.textContent = fmt(sum);
    const pay = root.querySelector('.msf-07__next--go'); if (pay) pay.disabled = sum === 0;
    return {lines, sum};
  };
  const validate = (fs) => {
    let ok = true;
    fs.querySelectorAll('.msf-07__err').forEach(e => e.remove());
    if (fs.querySelector('.msf-07__tickets') && recalc().sum === 0) {
      const err = document.createElement('p'); err.className='msf-07__err'; err.setAttribute('role','alert');
      err.textContent = 'Add at least one ticket to continue.';
      fs.querySelector('.msf-07__tickets').after(err); return false;
    }
    fs.querySelectorAll('input[required]').forEach(el => {
      const bad = !el.checkValidity(); el.setAttribute('aria-invalid', bad);
      if (bad && ok) { ok = false;
        const err = document.createElement('p'); err.className='msf-07__err'; err.setAttribute('role','alert');
        err.textContent = 'Please complete the highlighted fields.';
        el.closest('.msf-07__grid').append(err); el.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k!==i);
    mini.forEach((m,k) => {
      m.classList.toggle('is-active',k===i); m.classList.toggle('is-done',k<i);
      k===i ? m.setAttribute('aria-current','step') : m.removeAttribute('aria-current');
    });
    if (i === steps.length-1) {
      const {lines, sum} = recalc();
      root.querySelector('.msf-07__lines').innerHTML =
        lines.map(([l,p]) => '<li><span>'+l+'</span><span>'+fmt(p)+'</span></li>').join('') +
        '<li class="is-total"><span>Total</span><span>'+fmt(sum)+'</span></li>';
    }
    steps[i].querySelector('.msf-07__title').focus();
  };
  root.addEventListener('click', e => {
    const minus = e.target.closest('.msf-07__minus'), plus = e.target.closest('.msf-07__plus');
    if (minus || plus) {
      const inp = (minus||plus).closest('.msf-07__qty').querySelector('input');
      inp.value = Math.min(10, Math.max(0, +inp.value + (plus ? 1 : -1)));
      recalc(); return;
    }
    if (e.target.closest('.msf-07__next:not(.msf-07__next--go):not(.msf-07__submit):not(.msf-07__skip)')) { if (validate(steps[cur])) show(cur+1); }
    if (e.target.closest('.msf-07__back')) show(cur-1);
  });
  root.addEventListener('change', e => { if (e.target.matches('.msf-07__addon input')) recalc(); });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-07__next--go, .msf-07__submit, .msf-07__skip')) return;

    e.preventDefault();
    steps.forEach(s => s.hidden = true);
    mini.forEach(m => { m.classList.add('is-done'); m.classList.remove('is-active'); });
    const done = root.querySelector('.msf-07__done'); done.hidden = false; done.querySelector('h4').focus();
    });
  recalc();
})();
```
