---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/postcard/"
title: "Card Layout Footer with Contact Details"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "Four contact routes as tappable cards — sales, support, press, HQ — each one a real link (tel:, mailto:, a map URL) with a copy-to-clipboard shortcut for the…"
has_js: "true"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Card Layout Footer with Contact Details
Source: https://codefronts.com/layouts/css-footer-designs/postcard/

Four contact routes as tappable cards — sales, support, press, HQ — each one a real link (tel:, mailto:, a map URL) with a copy-to-clipboard shortcut for the times a visitor is on a desktop and wants the address, not a dialer. The card grid reflows on its own; the hover tilt is transform-only.
## HTML
```html
<section class="ft-14" aria-label="Card layout footer with contact details demo">
  <main class="ft-14__main">
    <p class="ft-14__eyebrow">Stretched links · tel: · clipboard</p>
    <h1 class="ft-14__title">Four ways in, none of them a contact form</h1>
    <p class="ft-14__sub">Every card is one real link with a full-card hit area, plus a copy button that stays clickable above the overlay. Tilt on hover, flat on touch.</p>
  </main>
  <footer class="ft-14__foot">
    <section class="ft-14__wrap" aria-labelledby="ft-14-h">
      <div class="ft-14__head">
        <h2 class="ft-14__h" id="ft-14-h">Talk to a person</h2>
        <p class="ft-14__hsub">Median first reply: 41 minutes, 09:00–19:00 CET, Monday to Friday.</p>
      </div>
      <ul class="ft-14__cards" id="ft-14-cards">
        <li class="ft-14__card" style="--ft-14-acc:oklch(0.68 0.17 250)">
          <span class="ft-14__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="M4 5h6l2 5-3 1.5a12 12 0 0 0 5 5L15.5 13l5 2v6a1 1 0 0 1-1.1 1A17 17 0 0 1 3 6.1 1 1 0 0 1 4 5z"/></svg></span>
          <p class="ft-14__ctitle"><a class="ft-14__clink" href="tel:+441179460188">Sales</a></p>
          <p class="ft-14__cval">+44 117 946 0188</p>
          <p class="ft-14__cnote">Quotes, volume pricing, procurement paperwork.</p>
          <button class="ft-14__copy" type="button" data-copy="+441179460188" aria-label="Copy the sales phone number">Copy</button>
        </li>
        <li class="ft-14__card" style="--ft-14-acc:oklch(0.72 0.16 165)">
          <span class="ft-14__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" focusable="false"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M3.5 7.5l8.5 6 8.5-6"/></svg></span>
          <p class="ft-14__ctitle"><a class="ft-14__clink" href="mailto:[email protected]?subject=Support%20request">Support</a></p>
          <p class="ft-14__cval">[email protected]</p>
          <p class="ft-14__cnote">Bugs, outages, account access. Subject pre-filled.</p>
          <button class="ft-14__copy" type="button" data-copy="[email protected]" aria-label="Copy the support email address">Copy</button>
        </li>
        <li class="ft-14__card" style="--ft-14-acc:oklch(0.75 0.15 60)">
          <span class="ft-14__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="M4 6h11v12H4z"/><path d="M15 9h4l1 3v6h-5"/><path d="M7 9h5M7 12h5M7 15h3"/></svg></span>
          <p class="ft-14__ctitle"><a class="ft-14__clink" href="mailto:[email protected]">Press</a></p>
          <p class="ft-14__cval">[email protected]</p>
          <p class="ft-14__cnote">Logos, screenshots, founder bios in the press kit.</p>
          <button class="ft-14__copy" type="button" data-copy="[email protected]" aria-label="Copy the press email address">Copy</button>
        </li>
        <li class="ft-14__card" style="--ft-14-acc:oklch(0.7 0.17 340)">
          <span class="ft-14__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/></svg></span>
          <p class="ft-14__ctitle"><a class="ft-14__clink" href="#ft-14-a">Headquarters</a></p>
          <p class="ft-14__cval">Prinsengracht 263, Amsterdam</p>
          <p class="ft-14__cnote">Visits by appointment. Step-free entrance at the rear.</p>
          <button class="ft-14__copy" type="button" data-copy="Prinsengracht 263, 1016 GV Amsterdam" aria-label="Copy the office address">Copy</button>
        </li>
      </ul>
      <p class="ft-14__live" id="ft-14-live" role="status" aria-live="polite"></p>
    </section>
    <div class="ft-14__bar">
      <div class="ft-14__brand"><span class="ft-14__mark" aria-hidden="true"></span>Relaystack</div>
      <nav class="ft-14__nav" aria-label="Footer"><a class="ft-14__link" href="#ft-14-a">Status</a><a class="ft-14__link" href="#ft-14-a">Docs</a><a class="ft-14__link" href="#ft-14-a">Privacy</a><a class="ft-14__link" href="#ft-14-a">Terms</a></nav>
      <p class="ft-14__copyline">© <time datetime="2026">2026</time> Relaystack B.V. · KvK 74129055</p>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-14-bg);
  --ft-14-bg: oklch(0.97 0.006 240);
  --ft-14-foot: oklch(0.19 0.022 255);
  --ft-14-ink: oklch(0.2 0.025 255);
  --ft-14-mut: oklch(0.53 0.02 255);
  --ft-14-fink: oklch(0.97 0.006 255);
  --ft-14-fmut: oklch(0.74 0.015 255);
  --ft-14-line: oklch(0.97 0.006 255/.14);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-14-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-14 *,
.ft-14 *::before,
.ft-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-14 ul {
  list-style: none;
}

.ft-14__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(38px,7.5vh,84px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1200px)/2));
}

.ft-14__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: oklch(0.5 0.16 250);
}

.ft-14__title {
  font-size: clamp(29px,5.2vw,56px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 16ch;
  text-wrap: balance;
}

.ft-14__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-14-mut);
  max-width: 56ch;
  text-wrap: pretty;
}

.ft-14__foot {
  background: var(--ft-14-foot);
  color: var(--ft-14-fink);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1200px)/2));
}

.ft-14__wrap {
  display: grid;
  gap: 18px;
  padding-block: clamp(30px,4.4vw,52px);
}

.ft-14__head {
  display: grid;
  gap: 6px;
}

.ft-14__h {
  font-size: clamp(19px,2.3vw,25px);
  font-weight: 690;
  letter-spacing: -.025em;
}

.ft-14__hsub {
  font-size: 14px;
  color: var(--ft-14-fmut);
}

.ft-14__cards {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(14rem,100%),1fr));
  gap: clamp(12px,1.6vw,18px);
}

.ft-14__card {
  position: relative;
  display: grid;
  align-content: start;
  gap: 5px;
  padding: 18px;
  border-radius: 18px;
  background: oklch(0.97 0.006 255/.05);
  border: 1px solid var(--ft-14-line);
  transform-style: preserve-3d;
  transition: transform .3s cubic-bezier(.2,.8,.2,1),border-color .3s ease,background .3s ease,box-shadow .3s ease;
}

.ft-14__card:hover,
.ft-14__card:focus-within {
  border-color: color-mix(in oklch,var(--ft-14-acc) 55%,transparent);
  background: color-mix(in oklch,var(--ft-14-acc) 9%,transparent);
  box-shadow: 0 24px 48px -30px var(--ft-14-acc);
}

.ft-14__ico {
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border-radius: 13px;
  background: color-mix(in oklch,var(--ft-14-acc) 18%,transparent);
  color: var(--ft-14-acc);
  margin-block-end: 6px;
}

.ft-14__ctitle {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ft-14-fmut);
}

.ft-14__clink {
  color: inherit;
  text-decoration: none;
}

.ft-14__clink::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
}

.ft-14__clink:focus-visible::after {
  outline: 2px solid var(--ft-14-acc);
  outline-offset: 3px;
}

.ft-14__cval {
  font-size: 15.5px;
  font-weight: 650;
  letter-spacing: -.015em;
  overflow-wrap: anywhere;
}

.ft-14__cnote {
  font-size: 12.8px;
  line-height: 1.5;
  color: var(--ft-14-fmut);
  text-wrap: pretty;
}

.ft-14__copy {
  position: relative;
  z-index: 1;
  justify-self: start;
  min-height: 36px;
  margin-block-start: 8px;
  padding: 0 14px;
  border: 1px solid var(--ft-14-line);
  border-radius: 9px;
  background: transparent;
  color: var(--ft-14-fmut);
  font: inherit;
  font-size: 12.5px;
  font-weight: 640;
  cursor: pointer;
  transition: color .2s ease,border-color .2s ease,background .2s ease;
}

.ft-14__copy:hover {
  color: var(--ft-14-acc);
  border-color: color-mix(in oklch,var(--ft-14-acc) 60%,transparent);
  background: color-mix(in oklch,var(--ft-14-acc) 12%,transparent);
}

.ft-14__copy:focus-visible,
.ft-14__link:focus-visible {
  outline: 2px solid var(--ft-14-acc,oklch(0.7 0.15 250));
  outline-offset: 3px;
}

.ft-14__copy[data-done="true"] {
  color: oklch(0.82 0.15 155);
  border-color: oklch(0.82 0.15 155/.5);
}

.ft-14__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.ft-14__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px 24px;
  padding-block: 20px;
  padding-bottom: calc(20px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-14-line);
}

.ft-14__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.ft-14__mark {
  width: 21px;
  height: 21px;
  border-radius: 7px;
  background: linear-gradient(140deg,oklch(0.68 0.17 250),oklch(0.7 0.17 340));
}

.ft-14__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 2px;
  margin-inline-start: auto;
}

.ft-14__link {
  display: flex;
  align-items: center;
  min-height: 40px;
  padding: 0 11px;
  border-radius: 9px;
  font-size: 13.5px;
  color: var(--ft-14-fmut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.ft-14__link:hover {
  color: var(--ft-14-fink);
  background: oklch(0.97 0.006 255/.07);
}

.ft-14__copyline {
  font-size: 12.8px;
  color: var(--ft-14-fmut);
}

@media (max-width: 760px) {
  .ft-14__nav {
    margin-inline-start: 0;
  }
}

@media (hover: none) {
  .ft-14__card {
    transform: none !important;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-14__card {
    transform: none !important;
  }

  .ft-14 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ft-14');
  if (!root || root.dataset.ready) return;
  root.dataset.ready = '1';
  const live = root.querySelector('#ft-14-live');
  const cards = [...root.querySelectorAll('.ft-14__card')];
  const canTilt = matchMedia('(hover: hover)').matches && !matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (canTilt) cards.forEach((card) => {
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width - 0.5;
      const py = (e.clientY - r.top) / r.height - 0.5;
      card.style.transform = 'perspective(760px) rotateX(' + (-py * 5).toFixed(2) + 'deg) rotateY(' + (px * 6).toFixed(2) + 'deg) translateY(-3px)';
    });
    card.addEventListener('pointerleave', () => { card.style.transform = ''; });
  });
  const copy = async (btn) => {
    const value = btn.dataset.copy;
    let ok = false;
    try {
      if (navigator.clipboard && window.isSecureContext) { await navigator.clipboard.writeText(value); ok = true; }
      else throw new Error('fallback');
    } catch (e) {
      const tmp = document.createElement('input');
      tmp.value = value; tmp.setAttribute('readonly', '');
      tmp.style.cssText = 'position:absolute;opacity:0;pointer-events:none';
      root.appendChild(tmp); tmp.select();
      try { ok = document.execCommand('copy'); } catch (e2) { ok = false; }
      tmp.remove();
    }
    live.textContent = ok ? value + ' copied to the clipboard' : 'Copy blocked here — the value is ' + value;
    btn.dataset.done = String(ok);
    const label = btn.textContent;
    btn.textContent = ok ? 'Copied' : 'Select it';
    setTimeout(() => { btn.textContent = label; btn.removeAttribute('data-done'); }, 2200);
  };
  root.querySelectorAll('.ft-14__copy').forEach((b) => b.addEventListener('click', (e) => { e.preventDefault(); copy(b); }));
})();
```
