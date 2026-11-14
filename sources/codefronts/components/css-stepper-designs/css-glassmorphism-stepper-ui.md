---
source: "codefronts"
url: "https://codefronts.com/components/css-stepper-designs/css-glassmorphism-stepper-ui/"
title: "CSS Glassmorphism Stepper UI"
section: "components"
category: "css-stepper-designs"
category_name: "CSS Steppers"
description: "Frosted-glass step cards layered over an animated aurora background, with backdrop-filter blur, cyan/teal accents, layered radial gradient orbs, and a…"
has_js: "true"
---

Here's a working CSS Stepper from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glassmorphism Stepper UI
Source: https://codefronts.com/components/css-stepper-designs/css-glassmorphism-stepper-ui/

Frosted-glass step cards layered over an animated aurora background, with backdrop-filter blur, cyan/teal accents, layered radial gradient orbs, and a multi-step panel flow inside the glass container.
## HTML
```html
<div class="stp-10">
  <div class="stp-10__blob"></div>
  <div class="stp-10__blob"></div>

  <div class="stp-10__card">
    <div class="stp-10__steps" id="stp-10-steps">
      <div class="stp-10__item done" data-i="1">
        <div class="stp-10__bubble">✓</div>
        <span class="stp-10__item-label">Account</span>
      </div>
      <div class="stp-10__item done" data-i="2">
        <div class="stp-10__bubble">✓</div>
        <span class="stp-10__item-label">Details</span>
      </div>
      <div class="stp-10__item active" data-i="3">
        <div class="stp-10__bubble">3</div>
        <span class="stp-10__item-label">Plan</span>
      </div>
      <div class="stp-10__item" data-i="4">
        <div class="stp-10__bubble">4</div>
        <span class="stp-10__item-label">Payment</span>
      </div>
    </div>

    <div class="stp-10__title" id="stp-10-title">Choose Your Plan</div>
    <div class="stp-10__subtitle" id="stp-10-sub">Select the tier that fits your needs</div>

    <div class="stp-10__pane" data-pane="1">
      <div class="stp-10__field"><label class="stp-10__fl">Email Address</label><input class="stp-10__in" placeholder="[email protected]"></div>
      <div class="stp-10__field"><label class="stp-10__fl">Password</label><input class="stp-10__in" type="password" placeholder="••••••••••"></div>
    </div>

    <div class="stp-10__pane" data-pane="2">
      <div class="stp-10__row">
        <div class="stp-10__field"><label class="stp-10__fl">First Name</label><input class="stp-10__in" placeholder="Jordan"></div>
        <div class="stp-10__field"><label class="stp-10__fl">Last Name</label><input class="stp-10__in" placeholder="Blake"></div>
      </div>
      <div class="stp-10__field"><label class="stp-10__fl">Company (optional)</label><input class="stp-10__in" placeholder="Acme Inc."></div>
    </div>

    <div class="stp-10__pane active" data-pane="3">
      <div class="stp-10__plans">
        <div class="stp-10__plan">
          <div class="stp-10__plan-name">Starter</div>
          <div class="stp-10__plan-price">Free</div>
          <div class="stp-10__plan-desc">5 projects</div>
        </div>
        <div class="stp-10__plan sel">
          <div class="stp-10__plan-name">Pro</div>
          <div class="stp-10__plan-price">$29</div>
          <div class="stp-10__plan-desc">Unlimited</div>
        </div>
        <div class="stp-10__plan">
          <div class="stp-10__plan-name">Team</div>
          <div class="stp-10__plan-price">$79</div>
          <div class="stp-10__plan-desc">10 seats</div>
        </div>
      </div>
    </div>

    <div class="stp-10__pane" data-pane="4">
      <div class="stp-10__field"><label class="stp-10__fl">Card Number</label><input class="stp-10__in" placeholder="4242 4242 4242 4242"></div>
      <div class="stp-10__row">
        <div class="stp-10__field"><label class="stp-10__fl">Expiry</label><input class="stp-10__in" placeholder="MM / YY"></div>
        <div class="stp-10__field"><label class="stp-10__fl">CVV</label><input class="stp-10__in" placeholder="•••"></div>
      </div>
    </div>

    <div class="stp-10__nav">
      <button class="stp-10__btn stp-10__btn--ghost" id="stp-10-back">← Back</button>
      <div class="stp-10__dots" id="stp-10-dots">
        <div class="stp-10__dot"></div>
        <div class="stp-10__dot"></div>
        <div class="stp-10__dot active"></div>
        <div class="stp-10__dot"></div>
      </div>
      <button class="stp-10__btn stp-10__btn--primary" id="stp-10-next">Continue →</button>
    </div>
  </div>
</div>
```
## CSS
```css
.stp-10,
.stp-10 *,
.stp-10 *::before,
.stp-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.stp-10 ::selection {
  background: rgba(255,255,255,.4);
  color: #fff;
}

.stp-10 {
  --cyan: #22d3ee;
  --blue: #38bdf8;
  --violet: #818cf8;
  --white: #fff;
  --glass: rgba(255,255,255,.08);
  --glass-border: rgba(255,255,255,.15);
  --text: rgba(255,255,255,.9);
  --muted: rgba(255,255,255,.4);
  font-family: 'Segoe UI',system-ui,sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  position: relative;
  overflow: hidden;
  background: #0a0e1a;
}
/* aurora background */

.stp-10::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 20% 30%,rgba(34,211,238,.25) 0%,transparent 50%), radial-gradient(ellipse at 80% 70%,rgba(129,140,248,.2) 0%,transparent 50%), radial-gradient(ellipse at 60% 20%,rgba(56,189,248,.15) 0%,transparent 40%);
  animation: stp-10-aurora 8s ease-in-out infinite alternate;
}

@keyframes stp-10-aurora {
  0% {
    opacity: .6;
  }

  50% {
    opacity: 1;
    filter: blur(2px);
  }

  100% {
    opacity: .7;
  }
}
/* floating blobs */

.stp-10__blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(70px);
  pointer-events: none;
}

.stp-10__blob:nth-child(1) {
  width: 400px;
  height: 400px;
  background: rgba(34,211,238,.12);
  top: -100px;
  left: -100px;
  animation: stp-10-float 12s ease-in-out infinite;
}

.stp-10__blob:nth-child(2) {
  width: 300px;
  height: 300px;
  background: rgba(129,140,248,.1);
  bottom: -80px;
  right: -80px;
  animation: stp-10-float 10s ease-in-out infinite reverse;
}

@keyframes stp-10-float {
  0%,
    100% {
    transform: translate(0,0);
  }

  50% {
    transform: translate(40px,30px);
  }
}
/* glass card */

.stp-10__card {
  position: relative;
  z-index: 1;
  max-width: 580px;
  width: 100%;
  background: var(--glass);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1px solid var(--glass-border);
  border-radius: 24px;
  padding: 40px 36px;
  box-shadow: 0 32px 80px rgba(0,0,0,.4),inset 0 1px 0 rgba(255,255,255,.1);
}
/* stepper */

.stp-10__steps {
  display: flex;
  align-items: center;
  margin-bottom: 36px;
}

.stp-10__item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  position: relative;
}

.stp-10__item:not(:last-child)::after {
  content: '';
  position: absolute;
  top: 24px;
  left: calc(50% + 24px);
  width: calc(100% - 48px);
  height: 1px;
  background: var(--glass-border);
  transition: background .5s;
}

.stp-10__item.done::after {
  background: linear-gradient(90deg,var(--cyan),var(--blue));
}

.stp-10__bubble {
  width: 48px;
  height: 48px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 700;
  background: rgba(255,255,255,.06);
  border: 1px solid var(--glass-border);
  color: var(--muted);
  transition: all .4s cubic-bezier(.34,1.56,.64,1);
  backdrop-filter: blur(8px);
  position: relative;
  overflow: hidden;
}

.stp-10__bubble::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg,rgba(255,255,255,.12),transparent);
  opacity: 0;
  transition: opacity .3s;
}

.stp-10__item.done .stp-10__bubble {
  background: rgba(34,211,238,.2);
  border-color: rgba(34,211,238,.4);
  color: var(--cyan);
  box-shadow: 0 0 24px rgba(34,211,238,.2),inset 0 1px 0 rgba(255,255,255,.15);
}

.stp-10__item.done .stp-10__bubble::before {
  opacity: 1;
}

.stp-10__item.active .stp-10__bubble {
  background: rgba(56,189,248,.2);
  border-color: rgba(56,189,248,.5);
  color: var(--blue);
  box-shadow: 0 0 0 4px rgba(56,189,248,.1),0 0 32px rgba(56,189,248,.25),inset 0 1px 0 rgba(255,255,255,.15);
  animation: stp-10-glow 2s ease-in-out infinite;
}

@keyframes stp-10-glow {
  0%,
    100% {
    box-shadow: 0 0 0 4px rgba(56,189,248,.1),0 0 32px rgba(56,189,248,.25);
  }

  50% {
    box-shadow: 0 0 0 8px rgba(56,189,248,.06),0 0 48px rgba(56,189,248,.35);
  }
}

.stp-10__item-label {
  font-size: 11px;
  color: var(--muted);
  text-align: center;
  letter-spacing: .06em;
  text-transform: uppercase;
  transition: color .3s;
}

.stp-10__item.done .stp-10__item-label {
  color: rgba(34,211,238,.8);
}

.stp-10__item.active .stp-10__item-label {
  color: var(--text);
}
/* content */

.stp-10__title {
  font-size: 22px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 6px;
}

.stp-10__subtitle {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 24px;
}

.stp-10__pane {
  display: none;
  animation: stp-10-in .35s ease;
}

.stp-10__pane.active {
  display: block;
}

@keyframes stp-10-in {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.stp-10__field {
  margin-bottom: 14px;
}

.stp-10__fl {
  font-size: 11px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 6px;
  display: block;
}

.stp-10__in {
  width: 100%;
  padding: 12px 16px;
  background: rgba(255,255,255,.06);
  backdrop-filter: blur(8px);
  border: 1px solid var(--glass-border);
  border-radius: 10px;
  color: var(--text);
  font-size: 14px;
  outline: none;
  transition: border-color .2s,background .2s,box-shadow .2s;
}

.stp-10__in::placeholder {
  color: var(--muted);
}

.stp-10__in:focus {
  background: rgba(255,255,255,.1);
  border-color: rgba(56,189,248,.5);
  box-shadow: 0 0 0 3px rgba(56,189,248,.1);
}

.stp-10__row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
/* plan cards */

.stp-10__plans {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
  margin-bottom: 8px;
}

.stp-10__plan {
  padding: 14px;
  border-radius: 12px;
  background: rgba(255,255,255,.04);
  border: 1px solid var(--glass-border);
  cursor: pointer;
  transition: all .25s;
  text-align: center;
}

.stp-10__plan:hover {
  background: rgba(255,255,255,.08);
  border-color: rgba(56,189,248,.3);
}

.stp-10__plan.sel {
  background: rgba(56,189,248,.12);
  border-color: rgba(56,189,248,.5);
  box-shadow: 0 0 20px rgba(56,189,248,.1);
}

.stp-10__plan-name {
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
}

.stp-10__plan-price {
  font-size: 19px;
  font-weight: 800;
  color: var(--blue);
  margin: 4px 0;
}

.stp-10__plan-desc {
  font-size: 10px;
  color: var(--muted);
}
/* nav */

.stp-10__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 28px;
}

.stp-10__btn {
  padding: 11px 26px;
  border-radius: 10px;
  border: none;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all .2s;
}

.stp-10__btn--ghost {
  background: rgba(255,255,255,.06);
  backdrop-filter: blur(8px);
  border: 1px solid var(--glass-border);
  color: var(--muted);
}

.stp-10__btn--ghost:hover {
  background: rgba(255,255,255,.1);
  color: var(--text);
}

.stp-10__btn--primary {
  background: linear-gradient(135deg,var(--cyan),var(--blue));
  color: #000;
  font-weight: 700;
  box-shadow: 0 4px 20px rgba(34,211,238,.3);
}

.stp-10__btn--primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 32px rgba(34,211,238,.4);
}

.stp-10__dots {
  display: flex;
  gap: 6px;
}

.stp-10__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--glass-border);
  transition: all .3s;
}

.stp-10__dot.active {
  width: 18px;
  border-radius: 3px;
  background: var(--cyan);
}

@media (prefers-reduced-motion: reduce) {
  .stp-10::before,
    .stp-10__blob {
    animation: none;
  }

  .stp-10__item.active .stp-10__bubble {
    animation: none;
  }

  .stp-10__pane.active {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  let cur=3;
  const total=4;
  const items=document.querySelectorAll('.stp-10__item');
  const panes=document.querySelectorAll('.stp-10__pane');
  const dots=document.querySelectorAll('.stp-10__dot');
  const title=document.getElementById('stp-10-title');
  const sub=document.getElementById('stp-10-sub');
  const nextBtn=document.getElementById('stp-10-next');

  const info=[
    {t:'Create Your Account',s:'Start with your email and password'},
    {t:'Personal Details',s:'Tell us a bit about yourself'},
    {t:'Choose Your Plan',s:'Select the tier that fits your needs'},
    {t:'Payment Info',s:'Secure checkout — cancel anytime'},
  ];

  function update(){
    items.forEach((item,i)=>{
      item.classList.remove('done','active');
      const b=item.querySelector('.stp-10__bubble');
      if(i+1<cur){item.classList.add('done');b.textContent='✓';}
      else if(i+1===cur){item.classList.add('active');b.textContent=cur;}
      else b.textContent=i+1;
    });
    panes.forEach(p=>{
      p.classList.remove('active');
      if(parseInt(p.dataset.pane)===cur) p.classList.add('active');
    });
    dots.forEach((d,i)=>{
      d.classList.remove('active');
      if(i+1===cur) d.classList.add('active');
    });
    const inf=info[cur-1];
    title.textContent=inf.t;
    sub.textContent=inf.s;
    nextBtn.textContent=cur===total?'Complete Setup ✓':'Continue →';
    document.getElementById('stp-10-back').style.display=cur<=1?'none':'';
  }

  document.querySelectorAll('.stp-10__plan').forEach(p=>{
    p.addEventListener('click',()=>{
      document.querySelectorAll('.stp-10__plan').forEach(x=>x.classList.remove('sel'));
      p.classList.add('sel');
    });
  });
  document.getElementById('stp-10-back').addEventListener('click',()=>{cur=Math.max(1,cur-1);update();});
  document.getElementById('stp-10-next').addEventListener('click',()=>{cur=Math.min(total,cur+1);update();});
  update();
})();
```
