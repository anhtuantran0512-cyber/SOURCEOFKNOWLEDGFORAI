---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/multi-step-onboarding-walkthrough/"
title: "Multi-Step Onboarding Walkthrough"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A modal wizard that introduces a dashboard across three steps with Back / Next pagination, a progress indicator and a Skip escape hatch — the first-run…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Step Onboarding Walkthrough
Source: https://codefronts.com/components/css-modals/multi-step-onboarding-walkthrough/

A modal wizard that introduces a dashboard across three steps with Back / Next pagination, a progress indicator and a Skip escape hatch — the first-run product tour that lifts activation without a separate page.
## HTML
```html
<div class="cm-14">
  <button class="cm-14__open" type="button">Start tour</button>

  <dialog class="cm-14__dlg" aria-labelledby="cm-14-title">
    <div class="cm-14__card">
      <button class="cm-14__skip" type="button">Skip</button>

      <div class="cm-14__stage">
        <section class="cm-14__step" data-step="0">
          <div class="cm-14__art" data-label="dashboard">📊</div>
          <h2 id="cm-14-title" class="cm-14__t" tabindex="-1">Welcome to your dashboard</h2>
          <p class="cm-14__p">Everything about your projects, in one live view. Let's take 30 seconds to get you oriented.</p>
        </section>
        <section class="cm-14__step" data-step="1" hidden>
          <div class="cm-14__art" data-label="filters">🔎</div>
          <h2 class="cm-14__t" tabindex="-1">Filter &amp; find anything</h2>
          <p class="cm-14__p">Slice by status, owner or date, then save the view. Your team sees the same filtered board instantly.</p>
        </section>
        <section class="cm-14__step" data-step="2" hidden>
          <div class="cm-14__art" data-label="invite">🤝</div>
          <h2 class="cm-14__t" tabindex="-1">Invite your team</h2>
          <p class="cm-14__p">Add teammates and assign roles. You can always change permissions later from Settings.</p>
        </section>
      </div>

      <div class="cm-14__foot">
        <div class="cm-14__dots" aria-hidden="true"><i class="is-on"></i><i></i><i></i></div>
        <p class="cm-14__count" aria-live="polite">Step 1 of 3</p>
        <div class="cm-14__nav">
          <button type="button" class="cm-14__back" disabled>Back</button>
          <button type="button" class="cm-14__next">Next</button>
        </div>
      </div>
    </div>
  </dialog>
</div>
```
## CSS
```css
.cm-14,
.cm-14 *,
.cm-14 *::before,
.cm-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-14 {
  --accent: oklch(0.7 0.16 275);
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#100e18,#08070c);
}

.cm-14__open {
  cursor: pointer;
  padding: 13px 26px;
  border-radius: 11px;
  color: #eae7fb;
  font: 600 15px system-ui;
  border: 1px solid color-mix(in oklch,var(--accent) 45%,#2b2740);
  background: color-mix(in oklch,var(--accent) 14%,#100e18);
  transition: background .2s,border-color .2s;
}

.cm-14__open:hover {
  border-color: var(--accent);
  background: color-mix(in oklch,var(--accent) 22%,#100e18);
}

.cm-14__open:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-14__dlg {
  margin: auto;
  width: min(440px,94vw);
  padding: 0;
  border: none;
  border-radius: 20px;
  color: #e9e7f3;
  background: linear-gradient(180deg,#161426,#100e1a);
  box-shadow: 0 40px 90px -30px #000,0 0 0 1px #2a2742;
  opacity: 0;
  transform: scale(.97);
  transition: opacity .28s,transform .28s,overlay .28s allow-discrete,display .28s allow-discrete;
}

.cm-14__dlg[open] {
  opacity: 1;
  transform: none;
}

@starting-style {
  .cm-14__dlg[open] {
    opacity: 0;
    transform: scale(.97);
  }
}

.cm-14__dlg::backdrop {
  background: rgba(6,5,10,0);
  backdrop-filter: blur(0);
  transition: background .3s,backdrop-filter .3s,overlay .3s allow-discrete,display .3s allow-discrete;
}

.cm-14__dlg[open]::backdrop {
  background: rgba(6,5,10,.64);
  backdrop-filter: blur(5px);
}

@starting-style {
  .cm-14__dlg[open]::backdrop {
    background: rgba(6,5,10,0);
    backdrop-filter: blur(0);
  }
}

.cm-14__card {
  position: relative;
  padding: 30px;
}

.cm-14__skip {
  position: absolute;
  top: 16px;
  right: 18px;
  background: none;
  border: none;
  color: #8b86a8;
  font: 600 13px system-ui;
  cursor: pointer;
  padding: 4px;
}

.cm-14__skip:hover {
  color: #c5c0dd;
}

.cm-14__skip:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 6px;
}

.cm-14__stage {
  min-height: 230px;
  padding-top: 14px;
}

.cm-14__step {
  text-align: center;
  animation: cm-14-in .35s ease both;
}

@keyframes cm-14-in {
  from {
    opacity: 0;
    transform: translateX(14px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.cm-14__art {
  width: 96px;
  height: 96px;
  margin: 0 auto 22px;
  border-radius: 22px;
  display: grid;
  place-items: center;
  font-size: 42px;
  background: color-mix(in oklch,var(--accent) 16%,#141225);
  box-shadow: inset 0 0 0 1px color-mix(in oklch,var(--accent) 30%,transparent),0 0 50px -14px var(--accent);
}

.cm-14__t {
  font-size: 22px;
  font-weight: 700;
  color: #f4f2fc;
  margin-bottom: 10px;
  outline: none;
}

.cm-14__p {
  font-size: 14.5px;
  line-height: 1.65;
  color: #a7a2c2;
  max-width: 34ch;
  margin: 0 auto;
}

.cm-14__foot {
  margin-top: 26px;
}

.cm-14__dots {
  display: flex;
  justify-content: center;
  gap: 7px;
  margin-bottom: 10px;
}

.cm-14__dots i {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #37324e;
  transition: all .25s;
}

.cm-14__dots i.is-on {
  background: var(--accent);
  width: 22px;
  border-radius: 4px;
}

.cm-14__count {
  text-align: center;
  font: 12px ui-monospace,monospace;
  letter-spacing: .12em;
  color: #847ea3;
  margin-bottom: 18px;
}

.cm-14__nav {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.cm-14__back,
.cm-14__next {
  padding: 13px;
  border-radius: 11px;
  font: 700 14.5px system-ui;
  cursor: pointer;
  transition: all .18s;
}

.cm-14__back {
  border: 1px solid #322d49;
  background: #191627;
  color: #d8d3ee;
}

.cm-14__back:hover:not(:disabled) {
  background: #211d33;
}

.cm-14__back:disabled {
  opacity: .4;
  cursor: not-allowed;
}

.cm-14__next {
  border: none;
  background: var(--accent);
  color: #0a0616;
}

.cm-14__next:hover {
  filter: brightness(1.08);
}

.cm-14__back:focus-visible,
.cm-14__next:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cm-14__dlg,
    .cm-14__dlg::backdrop {
    transition-duration: .001s;
  }

  .cm-14__step {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-14');
  var dlg = root.querySelector('.cm-14__dlg');
  var steps = root.querySelectorAll('.cm-14__step');
  var dots = root.querySelectorAll('.cm-14__dots i');
  var count = root.querySelector('.cm-14__count');
  var back = root.querySelector('.cm-14__back');
  var next = root.querySelector('.cm-14__next');
  var i = 0, total = steps.length;
  function render(){
    steps.forEach(function(s,n){ s.hidden = n !== i; });
    dots.forEach(function(d,n){ d.classList.toggle('is-on', n === i); });
    count.textContent = 'Step ' + (i+1) + ' of ' + total;
    back.disabled = i === 0;
    next.textContent = i === total-1 ? 'Get started' : 'Next';
    var h = steps[i].querySelector('.cm-14__t'); if(h) h.focus();
  }
  root.querySelector('.cm-14__open').addEventListener('click', function(){ i = 0; render(); dlg.showModal(); });
  root.querySelector('.cm-14__skip').addEventListener('click', function(){ dlg.close(); });
  back.addEventListener('click', function(){ if(i>0){ i--; render(); } });
  next.addEventListener('click', function(){ if(i<total-1){ i++; render(); } else dlg.close(); });
})();
```
