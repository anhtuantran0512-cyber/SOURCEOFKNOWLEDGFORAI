---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/newsletter-hero/"
title: "Full-Width CSS Footer with Email Newsletter Signup"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "A full-bleed subscribe band with the details most newsletter footers skip: inline validation that announces itself, a button that shows real pending state, a…"
has_js: "true"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Width CSS Footer with Email Newsletter Signup
Source: https://codefronts.com/layouts/css-footer-designs/newsletter-hero/

A full-bleed subscribe band with the details most newsletter footers skip: inline validation that announces itself, a button that shows real pending state, a success message that replaces the field rather than sitting next to it, and honest consent copy under the input. Everything below is what a conversion audit asks for.
## HTML
```html
<section class="ft-13" aria-label="Full width newsletter signup footer demo">
  <main class="ft-13__main">
    <p class="ft-13__eyebrow">:user-invalid · aria-live · pending state</p>
    <h1 class="ft-13__title">The subscribe box, audited</h1>
    <p class="ft-13__sub">Try an invalid address, then a valid one. Every state — hint, error, pending, success — is announced as well as shown.</p>
  </main>
  <footer class="ft-13__foot">
    <section class="ft-13__band" aria-labelledby="ft-13-bh">
      <div class="ft-13__bandin">
        <div class="ft-13__pitch">
          <p class="ft-13__kicker">Every second Tuesday · 12,900 readers</p>
          <h2 class="ft-13__h" id="ft-13-bh">Field Notes, from the build log</h2>
          <p class="ft-13__pdesc">One deep dive on a real production problem, the CSS we shipped to fix it, and nothing else. No sponsor slots, no digest padding.</p>
        </div>
        <div class="ft-13__signup" id="ft-13-signup">
          <div class="ft-13__row">
            <div class="ft-13__field">
              <label class="ft-13__label" for="ft-13-email">Email address</label>
              <input class="ft-13__input" id="ft-13-email" type="email" inputmode="email" autocomplete="email" placeholder="[email protected]" aria-describedby="ft-13-hint">
            </div>
            <button class="ft-13__btn" id="ft-13-btn" type="button"><span class="ft-13__btntext">Subscribe</span><span class="ft-13__spin" aria-hidden="true"></span></button>
          </div>
          <p class="ft-13__hint" id="ft-13-hint">Two emails a month. Unsubscribe in one click. We never share your address — <a class="ft-13__inline" href="#ft-13-a">privacy notice</a>.</p>
          <p class="ft-13__err" id="ft-13-err" role="alert" hidden></p>
        </div>
        <p class="ft-13__done" id="ft-13-done" hidden tabindex="-1">
          <span class="ft-13__check" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="M4 12.5l5 5L20 6.5"/></svg></span>
          <span><strong>Almost there.</strong> Check your inbox for a confirmation link — it expires in 24 hours.</span>
        </p>
      </div>
    </section>
    <div class="ft-13__cols">
      <div class="ft-13__brandcol">
        <div class="ft-13__brand"><span class="ft-13__mark" aria-hidden="true"></span>Fieldwork</div>
        <p class="ft-13__blurb">Front-end engineering notes from a small studio in Copenhagen.</p>
      </div>
      <nav class="ft-13__col" aria-labelledby="ft-13-c1"><h2 class="ft-13__ch" id="ft-13-c1">Writing</h2><ul class="ft-13__list"><li><a class="ft-13__link" href="#ft-13-a">Archive</a></li><li><a class="ft-13__link" href="#ft-13-a">Best of 2025</a></li><li><a class="ft-13__link" href="#ft-13-a">RSS feed</a></li></ul></nav>
      <nav class="ft-13__col" aria-labelledby="ft-13-c2"><h2 class="ft-13__ch" id="ft-13-c2">Studio</h2><ul class="ft-13__list"><li><a class="ft-13__link" href="#ft-13-a">Services</a></li><li><a class="ft-13__link" href="#ft-13-a">Case studies</a></li><li><a class="ft-13__link" href="#ft-13-a">Availability</a></li></ul></nav>
      <nav class="ft-13__col" aria-labelledby="ft-13-c3"><h2 class="ft-13__ch" id="ft-13-c3">Legal</h2><ul class="ft-13__list"><li><a class="ft-13__link" href="#ft-13-a">Privacy</a></li><li><a class="ft-13__link" href="#ft-13-a">Terms</a></li><li><a class="ft-13__link" href="#ft-13-a">Cookies</a></li></ul></nav>
    </div>
    <p class="ft-13__copy">© <time datetime="2026">2026</time> Fieldwork ApS · CVR 41 88 22 09</p>
  </footer>
</section>
```
## CSS
```css
.ft-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-13-bg);
  --ft-13-bg: oklch(0.97 0.008 80);
  --ft-13-foot: oklch(1 0 0);
  --ft-13-ink: oklch(0.2 0.02 265);
  --ft-13-mut: oklch(0.53 0.018 265);
  --ft-13-acc: oklch(0.52 0.2 268);
  --ft-13-bad: oklch(0.55 0.2 25);
  --ft-13-line: oklch(0.2 0.02 265/.11);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-13-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-13 *,
.ft-13 *::before,
.ft-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-13 [hidden] {
  display: none !important;
}

.ft-13 ul {
  list-style: none;
}

.ft-13__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(36px,7vh,80px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1140px)/2));
}

.ft-13__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ft-13-acc);
}

.ft-13__title {
  font-size: clamp(29px,5.2vw,56px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 14ch;
  text-wrap: balance;
}

.ft-13__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-13-mut);
  max-width: 52ch;
  text-wrap: pretty;
}

.ft-13__foot {
  background: var(--ft-13-foot);
  border-top: 1px solid var(--ft-13-line);
}

.ft-13__band {
  background: linear-gradient(145deg,oklch(0.24 0.07 275),oklch(0.19 0.05 268));
  color: oklch(0.97 0.008 268);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1140px)/2));
}

.ft-13__bandin {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(19rem,100%),1fr));
  gap: clamp(22px,3vw,44px);
  align-items: center;
  padding-block: clamp(30px,4.5vw,52px);
}

.ft-13__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: oklch(0.82 0.13 275);
}

.ft-13__h {
  margin-block: 8px 8px;
  font-size: clamp(21px,2.8vw,30px);
  line-height: 1.12;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.ft-13__pdesc {
  font-size: 14.6px;
  line-height: 1.6;
  color: oklch(0.84 0.02 268);
  max-width: 44ch;
  text-wrap: pretty;
}

.ft-13__signup {
  display: grid;
  gap: 10px;
}

.ft-13__row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.ft-13__field {
  flex: 1 1 min(15rem,100%);
  display: grid;
  gap: 6px;
  min-width: 0;
}

.ft-13__label {
  font-size: 12px;
  font-weight: 640;
  letter-spacing: .03em;
  color: oklch(0.84 0.02 268);
}

.ft-13__input {
  width: 100%;
  min-height: 52px;
  padding: 0 16px;
  border-radius: 13px;
  border: 1px solid oklch(0.97 0.008 268/.25);
  background: oklch(0.97 0.008 268/.07);
  color: oklch(0.98 0.005 268);
  font: inherit;
  font-size: 15.5px;
  transition: border-color .2s ease,background .2s ease,box-shadow .2s ease;
}

.ft-13__input::placeholder {
  color: oklch(0.72 0.02 268);
}

.ft-13__input:hover {
  background: oklch(0.97 0.008 268/.11);
}

.ft-13__input:focus-visible {
  outline: none;
  border-color: oklch(0.82 0.13 275);
  box-shadow: 0 0 0 3px oklch(0.82 0.13 275/.3);
}

.ft-13__input:user-invalid,
.ft-13__input[aria-invalid="true"] {
  border-color: var(--ft-13-bad);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--ft-13-bad) 25%,transparent);
}

.ft-13__btn {
  position: relative;
  align-self: end;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  min-height: 52px;
  padding: 0 26px;
  border: 0;
  border-radius: 13px;
  background: oklch(0.97 0.008 268);
  color: oklch(0.2 0.05 268);
  font: inherit;
  font-size: 15px;
  font-weight: 680;
  cursor: pointer;
  transition: transform .22s cubic-bezier(.34,1.56,.64,1),box-shadow .22s ease,opacity .2s ease;
}

.ft-13__btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 28px -14px oklch(0.97 0.008 268/.7);
}

.ft-13__btn:focus-visible,
.ft-13__inline:focus-visible,
.ft-13__link:focus-visible {
  outline: 2px solid oklch(0.86 0.11 275);
  outline-offset: 3px;
  border-radius: 6px;
}

.ft-13__btn[data-busy="true"] {
  opacity: .75;
  pointer-events: none;
}

.ft-13__spin {
  display: none;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: conic-gradient(from 0deg,transparent,currentColor);
  mask: radial-gradient(farthest-side,transparent calc(100% - 2.5px),#000 0);
  -webkit-mask: radial-gradient(farthest-side,transparent calc(100% - 2.5px),#000 0);
  animation: ft-13-spin .8s linear infinite;
}

.ft-13__btn[data-busy="true"] .ft-13__spin {
  display: block;
}

@keyframes ft-13-spin {
  to {
    rotate: 360deg;
  }
}

.ft-13__hint {
  font-size: 12.4px;
  line-height: 1.5;
  color: oklch(0.8 0.02 268);
  max-width: 46ch;
}

.ft-13__inline {
  color: oklch(0.97 0.008 268);
  text-decoration: underline;
  text-underline-offset: .22em;
}

.ft-13__err {
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 13px;
  font-weight: 620;
  color: oklch(0.82 0.15 25);
}

.ft-13__err::before {
  content: '!';
  display: grid;
  place-items: center;
  width: 18px;
  height: 18px;
  flex: none;
  border-radius: 50%;
  background: oklch(0.82 0.15 25);
  color: oklch(0.2 0.05 25);
  font-size: 12px;
  font-weight: 800;
}

.ft-13__done {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 18px;
  border-radius: 15px;
  background: oklch(0.97 0.008 268/.1);
  border: 1px solid oklch(0.8 0.16 155/.5);
  font-size: 14.8px;
  line-height: 1.5;
  animation: ft-13-in .45s cubic-bezier(.2,.8,.2,1) both;
}

.ft-13__done:focus-visible {
  outline: 2px solid oklch(0.86 0.11 275);
  outline-offset: 3px;
}

@keyframes ft-13-in {
  from {
    opacity: 0;
    transform: translateY(10px) scale(.98);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.ft-13__check {
  display: grid;
  place-items: center;
  width: 32px;
  height: 32px;
  flex: none;
  border-radius: 50%;
  background: oklch(0.8 0.16 155/.2);
  color: oklch(0.85 0.16 155);
}

.ft-13__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
  gap: clamp(24px,3.2vw,38px) clamp(16px,2.2vw,30px);
  padding-block: clamp(28px,3.8vw,44px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1140px)/2));
}

.ft-13__brandcol {
  display: grid;
  align-content: start;
  gap: 10px;
  min-width: 0;
}

.ft-13__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -.025em;
}

.ft-13__mark {
  width: 23px;
  height: 23px;
  border-radius: 7px;
  background: linear-gradient(145deg,var(--ft-13-acc),oklch(0.7 0.17 320));
}

.ft-13__blurb {
  font-size: 14px;
  line-height: 1.55;
  color: var(--ft-13-mut);
  max-width: 30ch;
}

.ft-13__col {
  display: grid;
  align-content: start;
  gap: 4px;
  min-width: 0;
}

.ft-13__ch {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  margin-block-end: 8px;
}

.ft-13__list {
  display: grid;
  gap: 1px;
}

.ft-13__link {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  font-size: 14.2px;
  color: var(--ft-13-mut);
  text-decoration: none;
  width: fit-content;
  transition: color .18s ease;
}

.ft-13__link:hover {
  color: var(--ft-13-acc);
}

.ft-13__copy {
  padding-block: 16px;
  padding-bottom: calc(16px + env(safe-area-inset-bottom,0px));
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1140px)/2));
  border-top: 1px solid var(--ft-13-line);
  font-size: 12.8px;
  color: var(--ft-13-mut);
}

@media (prefers-reduced-motion: reduce) {
  .ft-13 * {
    animation-duration: .01ms !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ft-13');
  if (!root || root.dataset.ready) return;
  root.dataset.ready = '1';
  const input = root.querySelector('#ft-13-email');
  const btn = root.querySelector('#ft-13-btn');
  const err = root.querySelector('#ft-13-err');
  const wrap = root.querySelector('#ft-13-signup');
  const done = root.querySelector('#ft-13-done');
  const describe = (extra) => input.setAttribute('aria-describedby', extra ? 'ft-13-hint ft-13-err' : 'ft-13-hint');
  const fail = (msg) => {
    err.textContent = msg; err.hidden = false;
    input.setAttribute('aria-invalid', 'true'); describe(true); input.focus();
  };
  const clear = () => { err.hidden = true; input.removeAttribute('aria-invalid'); describe(false); };
  const submit = () => {
    const v = input.value.trim();
    if (!v) return fail('Enter your email address to subscribe.');
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)) return fail('That does not look like an email address — try [email protected].');
    clear();
    btn.dataset.busy = 'true';
    btn.querySelector('.ft-13__btntext').textContent = 'Subscribing';
    setTimeout(() => {
      wrap.hidden = true; done.hidden = false; done.focus();
    }, 900);
  };
  btn.addEventListener('click', submit);
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); submit(); } });
  input.addEventListener('input', () => { if (!err.hidden) clear(); });
})();
```
