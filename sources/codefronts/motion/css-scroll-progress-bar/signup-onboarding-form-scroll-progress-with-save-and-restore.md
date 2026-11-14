---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/signup-onboarding-form-scroll-progress-with-save-and-restore/"
title: "Signup / Onboarding Form Scroll Progress with Save-and-Restore"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "Long onboarding forms lose people."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Signup / Onboarding Form Scroll Progress with Save-and-Restore
Source: https://codefronts.com/motion/css-scroll-progress-bar/signup-onboarding-form-scroll-progress-with-save-and-restore/

Long onboarding forms lose people. This pattern fights both causes at once: a two-track indicator that separates how far down the page you are from how many answers you have actually given, and a draft that quietly saves every answer plus your scroll position so a closed tab is never a lost signup.
## HTML
```html
<section class="sp-13" aria-label="Onboarding form with scroll progress and draft restore demo">
  <div class="sp-13__rail" aria-hidden="true"><i class="sp-13__scroll"></i><i class="sp-13__done"></i></div>
  <header class="sp-13__bar">
    <a class="sp-13__brand" href="#sp-13-f1"><span class="sp-13__logo" aria-hidden="true"></span>Onboard</a>
    <p class="sp-13__count" id="sp-13-count" role="progressbar" aria-label="Fields completed" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">0 of 7 answered</p>
  </header>
  <div class="sp-13__restore" id="sp-13-restore" hidden>
    <p class="sp-13__rtext">We saved a draft from your last visit. Continue where you stopped?</p>
    <div class="sp-13__rbtns">
      <button class="sp-13__rbtn sp-13__rbtn--primary" type="button" id="sp-13-resume">Restore draft</button>
      <button class="sp-13__rbtn" type="button" id="sp-13-discard">Start fresh</button>
    </div>
  </div>
  <div class="sp-13__intro">
    <p class="sp-13__intro-eyebrow">two measurements, one rail</p>
    <h2 class="sp-13__intro-title">How far down ≠ how far through</h2>
    <p class="sp-13__intro-sub">The pale bar is your scroll position. The solid bar is how much you have actually answered. Type something, scroll away, then reload the page.</p>
  </div>
  <main class="sp-13__main">
    <section class="sp-13__set" id="sp-13-f1">
      <p class="sp-13__pk">About you</p>
      <div class="sp-13__grid">
        <label class="sp-13__field"><span class="sp-13__flab">Full name</span><input class="sp-13__input" type="text" name="name" autocomplete="name" required placeholder="Alex Whitfield"></label>
        <label class="sp-13__field"><span class="sp-13__flab">Work email</span><input class="sp-13__input" type="email" name="email" autocomplete="email" required placeholder="[email protected]"><span class="sp-13__hint">We only email about your account.</span></label>
      </div>
    </section>
    <section class="sp-13__set" id="sp-13-f2">
      <p class="sp-13__pk">Your team</p>
      <div class="sp-13__grid">
        <label class="sp-13__field"><span class="sp-13__flab">Company</span><input class="sp-13__input" type="text" name="company" autocomplete="organization" placeholder="Northbound Studio"></label>
        <label class="sp-13__field"><span class="sp-13__flab">Team size</span><select class="sp-13__input" name="size"><option value="">Choose one</option><option>Just me</option><option>2–10</option><option>11–50</option><option>51+</option></select></label>
      </div>
    </section>
    <section class="sp-13__set" id="sp-13-f3">
      <p class="sp-13__pk">What you are building</p>
      <div class="sp-13__grid">
        <label class="sp-13__field sp-13__field--wide"><span class="sp-13__flab">Project name</span><input class="sp-13__input" type="text" name="project" placeholder="Aurora redesign"></label>
        <label class="sp-13__field sp-13__field--wide"><span class="sp-13__flab">In one line, what does it do?</span><input class="sp-13__input" type="text" name="pitch" placeholder="A booking tool for independent studios"></label>
      </div>
    </section>
    <section class="sp-13__set" id="sp-13-f4">
      <p class="sp-13__pk">Last thing</p>
      <div class="sp-13__grid">
        <label class="sp-13__field sp-13__field--wide"><span class="sp-13__flab">How did you hear about us?</span><input class="sp-13__input" type="text" name="source" placeholder="A friend, a search, a talk…"></label>
      </div>
      <button class="sp-13__submit" type="button" id="sp-13-submit">Create account</button>
      <p class="sp-13__status" id="sp-13-status" role="status" aria-live="polite"></p>
    </section>
    <section class="sp-13__notes">
      <p class="sp-13__kicker">Why it works</p>
      <h3 class="sp-13__h">A closed tab should never cost a signup</h3>
      <p class="sp-13__p">Values and scroll offset are written to one <code>localStorage</code> key, debounced while typing and flushed on <code>pagehide</code> — the event that actually fires when a mobile tab is discarded. On return, the draft is offered, never silently applied.</p>
      <p class="sp-13__chip">1 storage key · 400ms debounce · 0 silent restores</p>
    </section>
  </main>
  <footer class="sp-13__pagefoot"><p class="sp-13__pagefootin">Scroll progress pattern 13 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-13-bg);
  --sp-13-bg: oklch(0.976 0.008 175);
  --sp-13-surface: oklch(1 0 0);
  --sp-13-ink: oklch(0.2 0.022 200);
  --sp-13-mut: oklch(0.52 0.016 200);
  --sp-13-acc: oklch(0.55 0.14 195);
  --sp-13-warn: oklch(0.62 0.18 30);
  --sp-13-line: oklch(0.2 0.022 200/.12);
  --sp-13-p: 0;
  --sp-13-done: 0;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-13-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-13 *,
.sp-13 *::before,
.sp-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-13__rail {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: 5px;
  z-index: 60;
  display: grid;
  background: color-mix(in oklch,var(--sp-13-acc) 10%,transparent);
  pointer-events: none;
}

.sp-13__scroll,
.sp-13__done {
  grid-area: 1/1;
  display: block;
  block-size: 100%;
  transform-origin: 0 50%;
}

.sp-13__scroll {
  transform: scaleX(var(--sp-13-p));
  background: color-mix(in oklch,var(--sp-13-acc) 28%,transparent);
}

.sp-13__done {
  transform: scaleX(var(--sp-13-done));
  background: linear-gradient(90deg,var(--sp-13-acc),oklch(0.68 0.15 160));
  box-shadow: 0 0 12px -2px var(--sp-13-acc);
  transition: transform .35s cubic-bezier(.32,.72,.3,1);
}

@supports (animation-timeline: scroll()) {
  .sp-13__scroll {
    transform: scaleX(0);
    animation: sp-13-fill linear both;
    animation-timeline: scroll(root block);
  }
}

@keyframes sp-13-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

.sp-13__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 60px;
  padding-block-start: 5px;
  background: color-mix(in oklch,var(--sp-13-surface) 84%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-block-end: 1px solid var(--sp-13-line);
}

.sp-13__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 730;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.sp-13__logo {
  inline-size: 18px;
  block-size: 18px;
  border-radius: 6px;
  background: linear-gradient(140deg,var(--sp-13-acc),oklch(0.7 0.14 155));
}

.sp-13__count {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.8px;
  font-variant-numeric: tabular-nums;
  color: var(--sp-13-acc);
  font-weight: 640;
}

.sp-13__restore {
  position: sticky;
  inset-block-start: 60px;
  z-index: 38;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px;
  padding: 12px clamp(18px,4vw,34px);
  background: color-mix(in oklch,var(--sp-13-acc) 12%,var(--sp-13-surface));
  border-block-end: 1px solid var(--sp-13-line);
}

.sp-13__rtext {
  font-size: 13.6px;
  font-weight: 620;
}

.sp-13__rbtns {
  display: flex;
  gap: 8px;
  margin-inline-start: auto;
}

.sp-13__rbtn {
  min-block-size: 38px;
  padding: 0 15px;
  border: 1px solid var(--sp-13-line);
  border-radius: 10px;
  background: var(--sp-13-surface);
  color: var(--sp-13-ink);
  font: inherit;
  font-size: 13.2px;
  font-weight: 640;
  cursor: pointer;
  transition: background .2s ease,color .2s ease;
}

.sp-13__rbtn--primary {
  background: var(--sp-13-acc);
  border-color: var(--sp-13-acc);
  color: oklch(1 0 0);
}

.sp-13__rbtn:hover {
  background: var(--sp-13-ink);
  border-color: var(--sp-13-ink);
  color: oklch(1 0 0);
}

.sp-13__rbtn:focus-visible,
.sp-13__submit:focus-visible,
.sp-13__brand:focus-visible {
  outline: 2px solid var(--sp-13-acc);
  outline-offset: 2px;
}

.sp-13__intro {
  display: grid;
  gap: 14px;
  padding-block: clamp(46px,10vh,110px) clamp(24px,5vh,52px);
}

.sp-13__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sp-13-acc);
}

.sp-13__intro-title {
  font-size: clamp(31px,5.6vw,64px);
  line-height: 1;
  letter-spacing: -.04em;
  font-weight: 730;
  max-inline-size: 17ch;
  text-wrap: balance;
}

.sp-13__intro-sub {
  font-size: clamp(14.5px,1.6vw,18px);
  line-height: 1.55;
  color: var(--sp-13-mut);
  max-inline-size: 54ch;
  text-wrap: pretty;
}

.sp-13__set {
  scroll-margin-top: 80px;
  display: grid;
  gap: 16px;
  align-content: center;
  min-block-size: 66svh;
  padding-block: clamp(24px,4vw,44px);
  border-block-end: 1px solid var(--sp-13-line);
}

.sp-13__pk {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--sp-13-acc);
}

.sp-13__grid {
  display: grid;
  grid-template-columns: repeat(2,minmax(0,1fr));
  gap: 14px;
  max-inline-size: 760px;
}

.sp-13__field {
  display: grid;
  gap: 6px;
}

.sp-13__field--wide {
  grid-column: 1/-1;
}

.sp-13__flab {
  font-size: 12.6px;
  font-weight: 640;
  color: var(--sp-13-mut);
}

.sp-13__hint {
  font-size: 11.6px;
  color: var(--sp-13-mut);
  opacity: .85;
}

.sp-13__input {
  min-block-size: 46px;
  padding: 0 14px;
  border: 1px solid var(--sp-13-line);
  border-radius: 12px;
  background: var(--sp-13-surface);
  font: inherit;
  font-size: 15px;
  color: var(--sp-13-ink);
  transition: border-color .2s ease,box-shadow .2s ease;
}

.sp-13__input::placeholder {
  color: color-mix(in oklch,var(--sp-13-mut) 60%,transparent);
}

.sp-13__input:focus-visible {
  outline: none;
  border-color: var(--sp-13-acc);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--sp-13-acc) 20%,transparent);
}

.sp-13__input:user-valid {
  border-color: color-mix(in oklch,var(--sp-13-acc) 55%,var(--sp-13-line));
}

.sp-13__input:user-invalid {
  border-color: var(--sp-13-warn);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--sp-13-warn) 16%,transparent);
}

.sp-13__submit {
  justify-self: start;
  min-block-size: 50px;
  padding: 0 26px;
  border: 0;
  border-radius: 13px;
  background: var(--sp-13-ink);
  color: oklch(1 0 0);
  font: inherit;
  font-size: 15px;
  font-weight: 680;
  cursor: pointer;
  transition: background .2s ease,translate .2s ease;
}

.sp-13__submit:hover {
  background: var(--sp-13-acc);
  translate: 0 -1px;
}

.sp-13__status {
  min-block-size: 20px;
  font-size: 13.2px;
  font-weight: 620;
  color: var(--sp-13-acc);
}

.sp-13__notes {
  display: grid;
  gap: 12px;
  padding-block: clamp(30px,6vh,64px);
}

.sp-13__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sp-13-acc);
}

.sp-13__h {
  font-size: clamp(21px,3vw,31px);
  line-height: 1.12;
  letter-spacing: -.032em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-13__p {
  max-inline-size: 62ch;
  font-size: 15.6px;
  line-height: 1.7;
  color: var(--sp-13-mut);
  text-wrap: pretty;
}

.sp-13__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.2 0.022 200/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-13__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-13-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-13-acc) 10%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-13-acc) 24%,transparent);
}

.sp-13__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(40px,8vh,100px) 24px;
  border-block-start: 1px solid var(--sp-13-line);
}

.sp-13__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-13-mut);
  text-align: center;
}

.sp-13__bar,
.sp-13__intro,
.sp-13__set,
.sp-13__notes {
  padding-inline: max(clamp(18px,4vw,34px),calc((100% - 960px)/2));
}

:root:has(.sp-13) {
  scroll-behavior: smooth;
  scroll-padding-top: 80px;
}

@media (max-width: 600px) {
  .sp-13__grid {
    grid-template-columns: minmax(0,1fr);
  }

  .sp-13__set {
    min-block-size: auto;
  }

  .sp-13__rbtns {
    margin-inline-start: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sp-13) {
    scroll-behavior: auto;
  }

  .sp-13 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-13');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const KEY = 'sp-13-draft';
  const MAX_AGE = 7 * 24 * 60 * 60 * 1000;
  const fields = [...root.querySelectorAll('[name]')];
  const count = root.querySelector('#sp-13-count');
  const status = root.querySelector('#sp-13-status');
  const restore = root.querySelector('#sp-13-restore');
  const native = CSS.supports('animation-timeline', 'scroll()');
  const store = {
    get() { try { return JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { return null; } },
    set(v) { try { localStorage.setItem(KEY, JSON.stringify(v)); } catch (e) { /* quota or private mode */ } },
    clear() { try { localStorage.removeItem(KEY); } catch (e) {} }
  };
  const values = () => Object.fromEntries(fields.map((f) => [f.name, f.value]));
  const meter = () => {
    const done = fields.filter((f) => f.value.trim() !== '').length;
    const ratio = done / fields.length;
    root.style.setProperty('--sp-13-done', ratio.toFixed(4));
    count.setAttribute('aria-valuenow', String(Math.round(ratio * 100)));
    count.textContent = ratio >= 1 ? 'All answered — nice' : (ratio > 0.8 ? 'Almost there · ' + done + ' of ' + fields.length : done + ' of ' + fields.length + ' answered');
  };
  let timer = 0;
  const save = () => store.set({ v: values(), y: scrollY, t: Date.now() });
  const debounced = () => { clearTimeout(timer); timer = setTimeout(save, 400); };
  fields.forEach((f) => { f.addEventListener('input', () => { meter(); debounced(); }); f.addEventListener('change', () => { meter(); debounced(); }); });
  addEventListener('pagehide', save);
  document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden') save(); });
  let ticking = false;
  const paint = () => {
    ticking = false;
    const d = document.documentElement;
    const max = d.scrollHeight - d.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, d.scrollTop / max)) : 0;
    if (!native) root.style.setProperty('--sp-13-p', p.toFixed(4));
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } }, { passive: true });
  paint(); meter();
  const draft = store.get();
  if (draft && draft.t && Date.now() - draft.t < MAX_AGE && Object.values(draft.v || {}).some((v) => v)) {
    restore.hidden = false;
    root.querySelector('#sp-13-resume').addEventListener('click', () => {
      fields.forEach((f) => { if (draft.v[f.name] != null) f.value = draft.v[f.name]; });
      meter();
      restore.hidden = true;
      requestAnimationFrame(() => scrollTo({ top: draft.y || 0, behavior: 'auto' }));
      status.textContent = 'Draft restored.';
    });
    root.querySelector('#sp-13-discard').addEventListener('click', () => { store.clear(); restore.hidden = true; });
  }
  root.querySelector('#sp-13-submit').addEventListener('click', () => {
    const missing = fields.filter((f) => f.required && !f.value.trim());
    if (missing.length) { missing[0].focus(); status.textContent = 'Add your ' + (missing[0].previousElementSibling ? missing[0].previousElementSibling.textContent.toLowerCase() : 'details') + ' to continue.'; return; }
    store.clear();
    status.textContent = 'Demo only — nothing was sent. Draft cleared.';
  });
})();
```
