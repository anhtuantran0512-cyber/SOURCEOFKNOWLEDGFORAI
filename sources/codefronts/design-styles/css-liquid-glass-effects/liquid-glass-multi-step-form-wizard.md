---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-multi-step-form-wizard/"
title: "Liquid Glass Multi-Step Form Wizard"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A sleek onboarding wizard on a Liquid Glass card, with a step indicator whose dots physically merge and morph like liquid drops as you move between steps (an…"
has_js: "true"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Multi-Step Form Wizard
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-multi-step-form-wizard/

A sleek onboarding wizard on a Liquid Glass card, with a step indicator whose dots physically merge and morph like liquid drops as you move between steps (an SVG gooey filter on the progress track). Each step slides in; light Vanilla JS drives navigation and validation.
## HTML
```html
<section class="lg-20" id="lg-20-root" aria-label="Liquid glass multi-step wizard">
  <svg width="0" height="0" aria-hidden="true" style="position:absolute"><filter id="lg-20-goo"><feGaussianBlur in="SourceGraphic" stdDeviation="5" result="b"/><feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -8"/></filter></svg>
  <form class="lg-20__card" novalidate>
    <div class="lg-20__prog" aria-hidden="true">
      <div class="lg-20__goo"><span class="lg-20__fill" id="lg-20-fill"></span><span class="lg-20__dot" data-s="0"></span><span class="lg-20__dot" data-s="1"></span><span class="lg-20__dot" data-s="2"></span></div>
    </div>
    <p class="lg-20__count" id="lg-20-count" aria-live="polite">Step 1 of 3</p>
    <div class="lg-20__steps">
      <fieldset class="lg-20__step lg-20__step--on" data-s="0"><legend class="lg-20__legend">Your details</legend><label class="lg-20__label" for="lg-20-name">Name</label><input class="lg-20__input" id="lg-20-name" type="text" required placeholder="Ada Lovelace"><label class="lg-20__label" for="lg-20-email">Email</label><input class="lg-20__input" id="lg-20-email" type="email" required placeholder="[email protected]"></fieldset>
      <fieldset class="lg-20__step" data-s="1"><legend class="lg-20__legend">Workspace</legend><label class="lg-20__label" for="lg-20-org">Organization</label><input class="lg-20__input" id="lg-20-org" type="text" required placeholder="Studio Lumen"><label class="lg-20__label" for="lg-20-role">Role</label><input class="lg-20__input" id="lg-20-role" type="text" placeholder="Design lead"></fieldset>
      <fieldset class="lg-20__step" data-s="2"><legend class="lg-20__legend">All set</legend><p class="lg-20__done">Review and finish — your Liquid Glass workspace is ready to launch. 🎉</p></fieldset>
    </div>
    <div class="lg-20__nav"><button class="lg-20__btn" id="lg-20-back" type="button" disabled>Back</button><button class="lg-20__btn lg-20__btn--next" id="lg-20-next" type="button">Next</button></div>
  </form>
</section>
```
## CSS
```css
.lg-20,
.lg-20 *,
.lg-20 *::before,
.lg-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-20 {
  --accent: oklch(0.66 0.19 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(circle at 25% 20%,#2a2350,#120f24 60%),radial-gradient(circle at 80% 90%,#1c2f55,#120f24 60%);
}

.lg-20__card {
  width: min(440px,94vw);
  padding: 30px;
  border-radius: 26px;
  color: #fff;
  background: color-mix(in oklab,white 11%,transparent);
  border: 1px solid rgba(255,255,255,.3);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.45),0 40px 80px -34px rgba(0,0,0,.7);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
}

.lg-20__prog {
  height: 26px;
  margin-bottom: 8px;
}

.lg-20__goo {
  position: relative;
  height: 26px;
  filter: url(#lg-20-goo);
}

.lg-20__fill {
  position: absolute;
  top: 9px;
  left: 9px;
  height: 8px;
  width: 0;
  border-radius: 999px;
  background: var(--accent);
  transition: width .5s cubic-bezier(.5,0,.2,1);
}

.lg-20__dot {
  position: absolute;
  top: 3px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: rgba(255,255,255,.25);
  transition: background .4s;
}

.lg-20__dot[data-s="0"] {
  left: 0;
}

.lg-20__dot[data-s="1"] {
  left: calc(50% - 10px);
}

.lg-20__dot[data-s="2"] {
  right: 0;
}

.lg-20__dot.lg-20__dot--on {
  background: var(--accent);
}

.lg-20__count {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: rgba(255,255,255,.7);
  margin-bottom: 18px;
}

.lg-20__steps {
  position: relative;
}

.lg-20__step {
  border: none;
  padding: 0;
  display: none;
  animation: lg-20-slide .4s ease;
}

.lg-20__step--on {
  display: block;
}

.lg-20__legend {
  font-size: 20px;
  font-weight: 800;
  margin-bottom: 16px;
  padding: 0;
}

.lg-20__label {
  display: block;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: rgba(255,255,255,.7);
  margin: 14px 0 7px;
}

.lg-20__input {
  width: 100%;
  font-size: 15px;
  color: #fff;
  padding: 12px 14px;
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,.25);
  background: color-mix(in oklab,white 8%,transparent);
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.lg-20__input::placeholder {
  color: rgba(255,255,255,.5);
}

.lg-20__input:focus {
  border-color: color-mix(in oklab,var(--accent) 70%,white);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--accent) 40%,transparent);
}

.lg-20__input.lg-20__invalid {
  border-color: oklch(0.65 0.2 25);
  box-shadow: 0 0 0 3px color-mix(in oklab,oklch(0.65 0.2 25) 40%,transparent);
}

.lg-20__done {
  font-size: 16px;
  line-height: 1.6;
  color: rgba(255,255,255,.9);
  padding: 12px 0;
}

.lg-20__nav {
  display: flex;
  gap: 12px;
  justify-content: space-between;
  margin-top: 24px;
}

.lg-20__btn {
  font-size: 15px;
  font-weight: 700;
  padding: 12px 24px;
  border-radius: 12px;
  cursor: pointer;
  color: #fff;
  border: 1px solid rgba(255,255,255,.3);
  background: rgba(255,255,255,.12);
  transition: background .2s,transform .15s,opacity .2s;
}

.lg-20__btn:disabled {
  opacity: .4;
  cursor: not-allowed;
}

.lg-20__btn--next {
  background: linear-gradient(180deg,color-mix(in oklab,var(--accent) 85%,white),var(--accent));
  border-color: color-mix(in oklab,var(--accent) 40%,white);
}

.lg-20__btn:not(:disabled):hover {
  transform: translateY(-2px);
}

.lg-20__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

@keyframes lg-20-slide {
  from {
    opacity: 0;
    transform: translateX(14px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .lg-20__step,
    .lg-20__fill,
    .lg-20__dot {
    animation: none;
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#lg-20-root');
  const steps = [...root.querySelectorAll('.lg-20__step')];
  const dots = [...root.querySelectorAll('.lg-20__dot')];
  const fill = root.querySelector('#lg-20-fill');
  const count = root.querySelector('#lg-20-count');
  const back = root.querySelector('#lg-20-back');
  const next = root.querySelector('#lg-20-next');
  let i = 0; const last = steps.length - 1;
  function paint(){
    steps.forEach((s,n) => s.classList.toggle('lg-20__step--on', n===i));
    dots.forEach((d,n) => { d.classList.toggle('lg-20__dot--on', n<=i); });
    fill.style.width = (i/last*100) + '%';
    count.textContent = 'Step ' + (i+1) + ' of ' + steps.length;
    back.disabled = i===0;
    next.textContent = i===last ? 'Finish' : 'Next';
    const f = steps[i].querySelector('input'); if (f) f.focus();
  }
  function validate(){
    const reqs = [...steps[i].querySelectorAll('input[required]')];
    let ok = true;
    reqs.forEach(inp => { const bad = !inp.value.trim() || (inp.type==='email' && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(inp.value)); inp.classList.toggle('lg-20__invalid', bad); if (bad) ok = false; });
    return ok;
  }
  next.addEventListener('click', () => { if (i===last){ count.textContent='Complete ✓'; return; } if (!validate()) return; i++; paint(); });
  back.addEventListener('click', () => { if (i>0){ i--; paint(); } });
  paint();
})();
```
