---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/css-footer-with-embedded-google-maps-and-office-hours/"
title: "CSS Footer with Embedded Google Maps & Office Hours"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "The local-SEO footer: address, an opening-hours table that knows whether you are open right now, and a responsive map panel that keeps its aspect ratio at…"
has_js: "true"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Footer with Embedded Google Maps & Office Hours
Source: https://codefronts.com/layouts/css-footer-designs/css-footer-with-embedded-google-maps-and-office-hours/

The local-SEO footer: address, an opening-hours table that knows whether you are open right now, and a responsive map panel that keeps its aspect ratio at every width. The map here is drawn in pure CSS so the demo never depends on a third-party iframe — swap in your embed with one tag, the frame is already sized.
## HTML
```html
<section class="ft-07" aria-label="Footer with map and office hours demo">
  <main class="ft-07__main">
    <p class="ft-07__eyebrow">aspect-ratio · &lt;time&gt; · LocalBusiness</p>
    <h1 class="ft-07__title">Where we are, when we're open</h1>
    <p class="ft-07__sub">A footer that answers the two questions local visitors arrive with — and marks them up so search engines can answer them too.</p>
  </main>
  <footer class="ft-07__foot">
    <div class="ft-07__grid">
      <section class="ft-07__mapwrap" aria-labelledby="ft-07-maph">
        <h2 class="ft-07__sr" id="ft-07-maph">Our location on a map</h2>
        <div class="ft-07__map">
          <div class="ft-07__canvas" role="img" aria-label="Map showing Harbourside Studio at 14 Ropewalk Lane, Bristol BS1 4RN">
            <span class="ft-07__park" aria-hidden="true"></span>
            <span class="ft-07__water" aria-hidden="true"></span>
            <span class="ft-07__pin" aria-hidden="true"><span class="ft-07__pulse"></span></span>
          </div>
          <p class="ft-07__mapnote">Replace this panel with your <code>&lt;iframe&gt;</code> embed — the frame is already responsive.</p>
        </div>
        <a class="ft-07__dir" href="#ft-07-a">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>
          Get directions
        </a>
      </section>
      <section class="ft-07__info" aria-labelledby="ft-07-infoh">
        <h2 class="ft-07__h" id="ft-07-infoh">Harbourside Studio</h2>
        <address class="ft-07__addr">
          14 Ropewalk Lane<br>Bristol BS1 4RN<br>United Kingdom
        </address>
        <ul class="ft-07__contact">
          <li><a class="ft-07__link" href="tel:+441179460000">+44 117 946 0000</a></li>
          <li><a class="ft-07__link" href="mailto:[email protected]">[email protected]</a></li>
        </ul>
        <p class="ft-07__transit">3 min from Wapping Wharf · step-free entrance on Museum St</p>
      </section>
      <section class="ft-07__hours" aria-labelledby="ft-07-hoursh">
        <div class="ft-07__hourhead">
          <h2 class="ft-07__h" id="ft-07-hoursh">Opening hours</h2>
          <p class="ft-07__state" id="ft-07-state" role="status" aria-live="polite"><span class="ft-07__dot" aria-hidden="true"></span><span id="ft-07-statetext">Checking…</span></p>
        </div>
        <dl class="ft-07__dl">
          <div class="ft-07__row" data-day="1" data-open="09:00" data-close="18:00"><dt>Monday</dt><dd><time datetime="09:00">09:00</time> – <time datetime="18:00">18:00</time></dd></div>
          <div class="ft-07__row" data-day="2" data-open="09:00" data-close="18:00"><dt>Tuesday</dt><dd><time datetime="09:00">09:00</time> – <time datetime="18:00">18:00</time></dd></div>
          <div class="ft-07__row" data-day="3" data-open="09:00" data-close="18:00"><dt>Wednesday</dt><dd><time datetime="09:00">09:00</time> – <time datetime="18:00">18:00</time></dd></div>
          <div class="ft-07__row" data-day="4" data-open="09:00" data-close="20:00"><dt>Thursday</dt><dd><time datetime="09:00">09:00</time> – <time datetime="20:00">20:00</time></dd></div>
          <div class="ft-07__row" data-day="5" data-open="09:00" data-close="20:00"><dt>Friday</dt><dd><time datetime="09:00">09:00</time> – <time datetime="20:00">20:00</time></dd></div>
          <div class="ft-07__row" data-day="6" data-open="10:00" data-close="16:00"><dt>Saturday</dt><dd><time datetime="10:00">10:00</time> – <time datetime="16:00">16:00</time></dd></div>
          <div class="ft-07__row" data-day="0"><dt>Sunday</dt><dd class="ft-07__closed">Closed</dd></div>
        </dl>
        <p class="ft-07__note">Bank holidays 11:00 – 15:00. Last workshop entry 45 minutes before close.</p>
      </section>
    </div>
    <div class="ft-07__bar">
      <p class="ft-07__copy">© <time datetime="2026">2026</time> Harbourside Studio Ltd · Company 09441120</p>
      <ul class="ft-07__legal"><li><a class="ft-07__slink" href="#ft-07-a">Privacy</a></li><li><a class="ft-07__slink" href="#ft-07-a">Accessibility</a></li><li><a class="ft-07__slink" href="#ft-07-a">Visit us</a></li></ul>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-07-bg);
  --ft-07-bg: oklch(0.975 0.006 230);
  --ft-07-foot: oklch(1 0 0);
  --ft-07-ink: oklch(0.22 0.025 250);
  --ft-07-mut: oklch(0.54 0.02 250);
  --ft-07-acc: oklch(0.55 0.16 235);
  --ft-07-ok: oklch(0.62 0.16 150);
  --ft-07-line: oklch(0.22 0.025 250/.11);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-07-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-07 *,
.ft-07 *::before,
.ft-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-07 ul {
  list-style: none;
}

.ft-07__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ft-07__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(40px,8vh,88px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1200px)/2));
}

.ft-07__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ft-07-acc);
}

.ft-07__title {
  font-size: clamp(30px,5.4vw,58px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 15ch;
  text-wrap: balance;
}

.ft-07__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-07-mut);
  max-width: 54ch;
  text-wrap: pretty;
}

.ft-07__foot {
  background: var(--ft-07-foot);
  border-top: 1px solid var(--ft-07-line);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1200px)/2));
}

.ft-07__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(17rem,100%),1fr));
  gap: clamp(24px,3.4vw,40px);
  padding-block: clamp(30px,4.5vw,52px);
}

.ft-07__mapwrap {
  display: grid;
  gap: 12px;
  align-content: start;
}

.ft-07__map {
  position: relative;
  aspect-ratio: 16/10;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid var(--ft-07-line);
  box-shadow: 0 18px 40px -28px oklch(0.22 0.025 250/.7);
}

.ft-07__map iframe {
  width: 100%;
  height: 100%;
  border: 0;
  display: block;
}

.ft-07__canvas {
  position: absolute;
  inset: 0;
  background: oklch(0.955 0.012 120);
  background-image: linear-gradient(oklch(1 0 0) 2px,transparent 2px),linear-gradient(90deg,oklch(1 0 0) 2px,transparent 2px),linear-gradient(oklch(1 0 0) 5px,transparent 5px),linear-gradient(90deg,oklch(1 0 0) 5px,transparent 5px);
  background-size: 34px 34px,34px 34px,170px 170px,170px 170px;
  background-position: -1px -1px,-1px -1px,-2px -2px,-2px -2px;
}

.ft-07__park {
  position: absolute;
  left: 6%;
  bottom: 8%;
  width: 33%;
  height: 38%;
  background: oklch(0.9 0.07 145);
  border-radius: 38% 62% 55% 45%/50% 40% 60% 50%;
}

.ft-07__water {
  position: absolute;
  right: -6%;
  top: -8%;
  width: 52%;
  height: 46%;
  background: oklch(0.88 0.06 230);
  border-radius: 50% 40% 60% 45%/45% 55% 40% 60%;
  transform: rotate(-12deg);
}

.ft-07__pin {
  position: absolute;
  left: 50%;
  top: 48%;
  width: 20px;
  height: 20px;
  translate: -50% -100%;
}

.ft-07__pin::after {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--ft-07-acc);
  border-radius: 50% 50% 50% 0;
  rotate: -45deg;
  box-shadow: 0 6px 14px -6px oklch(0.22 0.025 250/.9);
  border: 2.5px solid oklch(1 0 0);
}

.ft-07__pulse {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 14px;
  height: 14px;
  translate: -50% -50%;
  border-radius: 50%;
  background: color-mix(in oklch,var(--ft-07-acc) 45%,transparent);
  animation: ft-07-pulse 2.4s ease-out infinite;
}

@keyframes ft-07-pulse {
  0% {
    transform: scale(1);
    opacity: .8;
  }

  70% {
    transform: scale(4.2);
    opacity: 0;
  }

  100% {
    opacity: 0;
  }
}

.ft-07__mapnote {
  position: absolute;
  left: 10px;
  right: 10px;
  bottom: 10px;
  padding: 8px 12px;
  border-radius: 10px;
  background: oklch(1 0 0/.86);
  backdrop-filter: blur(8px);
  font-size: 11.5px;
  line-height: 1.45;
  color: var(--ft-07-mut);
}

.ft-07__mapnote code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .92em;
  color: var(--ft-07-acc);
}

.ft-07__dir {
  display: inline-flex;
  align-items: center;
  justify-self: start;
  gap: 8px;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 11px;
  background: var(--ft-07-ink);
  color: oklch(1 0 0);
  font-size: 14px;
  font-weight: 640;
  text-decoration: none;
  transition: background .2s ease,transform .2s ease;
}

.ft-07__dir:hover {
  background: var(--ft-07-acc);
  transform: translateY(-1px);
}

.ft-07__info,
.ft-07__hours {
  display: grid;
  align-content: start;
  gap: 12px;
  min-width: 0;
}

.ft-07__h {
  font-size: clamp(17px,1.8vw,20px);
  font-weight: 690;
  letter-spacing: -.02em;
}

.ft-07__addr {
  font-style: normal;
  font-size: 14.8px;
  line-height: 1.65;
  color: var(--ft-07-mut);
}

.ft-07__contact {
  display: grid;
  gap: 2px;
}

.ft-07__link {
  display: inline-flex;
  align-items: center;
  min-height: 38px;
  font-size: 14.8px;
  font-weight: 600;
  color: var(--ft-07-acc);
  text-decoration: underline;
  text-underline-offset: .25em;
  text-decoration-color: color-mix(in oklch,currentColor 30%,transparent);
  width: fit-content;
}

.ft-07__link:hover {
  text-decoration-color: currentColor;
}

.ft-07__link:focus-visible,
.ft-07__dir:focus-visible,
.ft-07__slink:focus-visible {
  outline: 2px solid var(--ft-07-acc);
  outline-offset: 3px;
  border-radius: 5px;
}

.ft-07__transit {
  font-size: 13px;
  line-height: 1.5;
  color: var(--ft-07-mut);
  padding: 10px 12px;
  border-radius: 10px;
  background: color-mix(in oklch,var(--ft-07-acc) 7%,transparent);
}

.ft-07__hourhead {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px;
}

.ft-07__state {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 12.5px;
  font-weight: 650;
  padding: 6px 12px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--ft-07-mut) 12%,transparent);
  color: var(--ft-07-mut);
}

.ft-07__state[data-open="true"] {
  background: color-mix(in oklch,var(--ft-07-ok) 14%,transparent);
  color: oklch(0.42 0.13 150);
}

.ft-07__dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: currentColor;
}

.ft-07__state[data-open="true"] .ft-07__dot {
  animation: ft-07-blink 2s ease-in-out infinite;
}

@keyframes ft-07-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .35;
  }
}

.ft-07__dl {
  display: grid;
  gap: 1px;
}

.ft-07__row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 12px;
  align-items: baseline;
  padding: 9px 10px;
  border-radius: 8px;
  font-size: 14px;
}

.ft-07__row dt {
  color: var(--ft-07-mut);
}

.ft-07__row dd {
  font-variant-numeric: tabular-nums;
  font-weight: 600;
}

.ft-07__row[aria-current="date"] {
  background: color-mix(in oklch,var(--ft-07-acc) 9%,transparent);
  outline: 1px solid color-mix(in oklch,var(--ft-07-acc) 22%,transparent);
}

.ft-07__row[aria-current="date"] dt {
  color: var(--ft-07-ink);
  font-weight: 650;
}

.ft-07__closed {
  color: var(--ft-07-mut);
  font-weight: 500;
}

.ft-07__note {
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--ft-07-mut);
}

.ft-07__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px 22px;
  padding-block: 20px;
  padding-bottom: calc(20px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-07-line);
}

.ft-07__copy {
  font-size: 13px;
  color: var(--ft-07-mut);
}

.ft-07__legal {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 16px;
  margin-inline-start: auto;
}

.ft-07__slink {
  display: flex;
  align-items: center;
  min-height: 36px;
  font-size: 13px;
  color: var(--ft-07-mut);
  text-decoration: none;
}

.ft-07__slink:hover {
  color: var(--ft-07-ink);
  text-decoration: underline;
  text-underline-offset: .25em;
}

@media (max-width: 560px) {
  .ft-07__legal {
    margin-inline-start: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-07 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ft-07');
  if (!root || root.dataset.ready) return;
  root.dataset.ready = '1';
  const rows = [...root.querySelectorAll('.ft-07__row')];
  const state = root.querySelector('#ft-07-state');
  const text = root.querySelector('#ft-07-statetext');
  const mins = (hhmm) => { const [h, m] = hhmm.split(':').map(Number); return h * 60 + m; };
  const fmt = (hhmm) => hhmm;
  const update = () => {
    const now = new Date();
    const day = now.getDay();
    const nowM = now.getHours() * 60 + now.getMinutes();
    let open = false, msg = '';
    rows.forEach((r) => {
      const isToday = Number(r.dataset.day) === day;
      if (isToday) r.setAttribute('aria-current', 'date'); else r.removeAttribute('aria-current');
      if (!isToday) return;
      if (!r.dataset.open) { msg = 'Closed today — open tomorrow'; return; }
      const o = mins(r.dataset.open), c = mins(r.dataset.close);
      if (nowM >= o && nowM < c) {
        open = true;
        const left = c - nowM;
        msg = left <= 60 ? 'Open — closing in ' + left + ' min' : 'Open now until ' + fmt(r.dataset.close);
      } else if (nowM < o) msg = 'Closed — opens at ' + fmt(r.dataset.open);
      else msg = 'Closed for today';
    });
    state.dataset.open = String(open);
    text.textContent = msg || 'Closed';
  };
  update();
  setInterval(update, 60000);
})();
```
