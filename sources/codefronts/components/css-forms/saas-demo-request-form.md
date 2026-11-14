---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/saas-demo-request-form/"
title: "SaaS Demo Request Form"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A B2B ‘Book a demo’ that skips the back-and-forth email: work-email validation that politely flags Gmail/Outlook/Yahoo addresses and auto-fills the company…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Demo Request Form
Source: https://codefronts.com/components/css-forms/saas-demo-request-form/

A B2B ‘Book a demo’ that skips the back-and-forth email: work-email validation that politely flags Gmail/Outlook/Yahoo addresses and auto-fills the company from the domain, a company-size segmented control, role and interest chips, and an inline scheduler showing the next five business days with slots rendered in the visitor's own time zone (via Intl). Set on an animated mesh-gradient with social proof alongside.
## HTML
```html
<div class="frm-18">
  <button type="button" class="frm-18__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-18__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-18__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-18__mesh" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="frm-18__stage">
    <div class="frm-18__wrap">
      <div class="frm-18__grid">
        <section class="frm-18__pitch">
          <p class="frm-18__badge"><span></span>Orbit Analytics</p>
          <h2>See your whole funnel in <em>one live view.</em></h2>
          <ul class="frm-18__vals">
            <li><b>30-minute walkthrough</b> tailored to your stack</li>
            <li><b>Live Q&amp;A</b> with a solutions engineer, not an SDR</li>
            <li><b>Free 14-day pilot</b> on your own data afterwards</li>
          </ul>
          <figure class="frm-18__quote">
            <blockquote>“We replaced four dashboards and a weekly spreadsheet ritual in the first month.”</blockquote>
            <figcaption><img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=120&h=120&fit=crop&crop=faces&auto=format&q=70" width="44" height="44" alt="" loading="lazy" decoding="async"><span><b>Priya Raman</b>VP Growth, Larkspur</span></figcaption>
          </figure>
          <p class="frm-18__logos" aria-label="Trusted by teams at Northwind, Halcyon, Fernway and Quanta"><span>NORTHWIND</span><span>halcyon</span><span>Fernway</span><span>QUANTA</span></p>
        </section>
        <div class="frm-18__form" role="form" aria-labelledby="frm-18-title">
          <h3 id="frm-18-title">Book your demo</h3>
          <div class="frm-18__field frm-18__email" data-state="idle">
            <label for="frm-18-e">Work email</label>
            <input id="frm-18-e" type="email" autocomplete="email" required placeholder="[email protected]" aria-describedby="frm-18-e-msg">
            <p class="frm-18__msg" id="frm-18-e-msg" aria-live="polite"></p>
          </div>
          <div class="frm-18__two">
            <div class="frm-18__field"><label for="frm-18-n">Full name</label><input id="frm-18-n" autocomplete="name" required></div>
            <div class="frm-18__field"><label for="frm-18-c">Company</label><input id="frm-18-c" autocomplete="organization" required></div>
          </div>
          <fieldset class="frm-18__seg"><legend>Team size</legend>
            <label><input type="radio" name="frm-18-s" value="1-10"><span>1–10</span></label><label><input type="radio" name="frm-18-s" value="11-50" checked><span>11–50</span></label><label><input type="radio" name="frm-18-s" value="51-200"><span>51–200</span></label><label><input type="radio" name="frm-18-s" value="201-1k"><span>201–1k</span></label><label><input type="radio" name="frm-18-s" value="1k+"><span>1k+</span></label>
          </fieldset>
          <fieldset class="frm-18__chips"><legend>What do you want to see?</legend>
            <label><input type="checkbox" checked><span>Attribution</span></label><label><input type="checkbox"><span>Cohorts</span></label><label><input type="checkbox"><span>Revenue forecasting</span></label><label><input type="checkbox"><span>Warehouse sync</span></label><label><input type="checkbox"><span>SSO &amp; security</span></label>
          </fieldset>
          <fieldset class="frm-18__sched"><legend>Pick a time <span class="frm-18__tz"></span></legend>
            <div class="frm-18__days"></div>
            <div class="frm-18__slots"></div>
          </fieldset>
          <button type="button" class="frm-18__book"><span>Book demo</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
          <p class="frm-18__fine">By booking you agree to our <a href="#privacy">Privacy Policy</a>. We'll never share your data.</p>
          <p class="frm-18__status" role="status"></p>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800&display=swap');

.frm-18 {
  --bg: #05060d;
  --card: rgba(14,16,30,.72);
  --ink: #f1f2fb;
  --muted: #9ca0bd;
  --line: rgba(255,255,255,.1);
  --field: rgba(255,255,255,.05);
  --accent: #7c5cff;
  --accent-2: #22d3ee;
  --warm: #f472b6;
  --ok: #34d399;
  --warn: #fbbf24;
  --sans: "Onest",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --ease: cubic-bezier(.16,1,.3,1);
  position: relative;
  isolation: isolate;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.frm-18[data-theme="light"] {
  --bg: #f3f3fb;
  --card: rgba(255,255,255,.78);
  --ink: #11122a;
  --muted: #585c7d;
  --line: rgba(17,18,42,.1);
  --field: rgba(255,255,255,.75);
}

.frm-18,
.frm-18 *,
.frm-18 *::before,
.frm-18 *::after {
  box-sizing: border-box;
}

.frm-18__mesh {
  position: absolute;
  inset: 0;
  z-index: -1;
  filter: blur(80px);
  opacity: .6;
}

.frm-18__mesh i {
  position: absolute;
  width: 50vmax;
  height: 50vmax;
  border-radius: 50%;
  animation: frm-18-drift 22s ease-in-out infinite alternate;
}

.frm-18__mesh i:nth-child(1) {
  background: var(--accent);
  left: -15vmax;
  top: -20vmax;
}

.frm-18__mesh i:nth-child(2) {
  background: var(--accent-2);
  right: -20vmax;
  top: 10%;
  animation-delay: -8s;
  opacity: .55;
}

.frm-18__mesh i:nth-child(3) {
  background: var(--warm);
  left: 25%;
  bottom: -30vmax;
  animation-delay: -14s;
  opacity: .4;
}

@keyframes frm-18-drift {
  to {
    translate: 6vmax -5vmax;
    scale: 1.12;
  }
}

.frm-18::after {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px) 0 0/48px 48px, linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px) 0 0/48px 48px;
  -webkit-mask: radial-gradient(circle at 50% 40%,#000,transparent 75%);
  mask: radial-gradient(circle at 50% 40%,#000,transparent 75%);
  pointer-events: none;
}

.frm-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3.5rem);
}

.frm-18__wrap {
  width: 100%;
  max-width: 70rem;
  container-type: inline-size;
}

.frm-18__grid {
  display: grid;
  gap: clamp(1.5rem,5cqi,4rem);
  align-items: center;
}

@container (min-width: 56rem) {
  .frm-18__grid {
    grid-template-columns: minmax(0,1fr) minmax(0,27rem);
  }
}

.frm-18__pitch {
  display: grid;
  gap: 1.5rem;
}

.frm-18__badge {
  margin: 0;
  justify-self: start;
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  padding: .4rem .8rem .4rem .45rem;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: var(--field);
  font-size: .85rem;
  font-weight: 600;
}

.frm-18__badge span {
  width: 1.4rem;
  height: 1.4rem;
  border-radius: 50%;
  background: conic-gradient(from 90deg,var(--accent),var(--accent-2),var(--warm),var(--accent));
  animation: frm-18-spin 8s linear infinite;
}

@keyframes frm-18-spin {
  to {
    rotate: 1turn;
  }
}

.frm-18 h2 {
  margin: 0;
  font-size: clamp(2.1rem,6cqi,3.9rem);
  font-weight: 800;
  line-height: 1;
  letter-spacing: -.045em;
  text-wrap: balance;
}

.frm-18 h2 em {
  font-style: normal;
  background: linear-gradient(100deg,var(--accent-2),var(--accent) 50%,var(--warm));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.frm-18__vals {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .7rem;
  color: var(--muted);
}

.frm-18__vals li {
  display: flex;
  gap: .7rem;
  align-items: baseline;
  line-height: 1.45;
}

.frm-18__vals li::before {
  content: '';
  flex: none;
  width: .5rem;
  height: .5rem;
  border-radius: 50%;
  background: var(--accent-2);
  box-shadow: 0 0 12px var(--accent-2);
  translate: 0 -.1rem;
}

.frm-18__vals b {
  color: var(--ink);
  font-weight: 600;
}

.frm-18__quote {
  margin: 0;
  padding: 1.1rem 1.25rem;
  border-radius: 1rem;
  border: 1px solid var(--line);
  background: var(--field);
}

.frm-18__quote blockquote {
  margin: 0 0 .9rem;
  font-size: 1.02rem;
  line-height: 1.5;
}

.frm-18__quote figcaption {
  display: flex;
  align-items: center;
  gap: .7rem;
  font-size: .82rem;
  color: var(--muted);
}

.frm-18__quote img {
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 50%;
  object-fit: cover;
  background: #333;
}

.frm-18__quote b {
  display: block;
  color: var(--ink);
  font-weight: 600;
}

.frm-18__logos {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  align-items: center;
  color: var(--muted);
  opacity: .75;
  font-weight: 800;
  letter-spacing: .04em;
}

.frm-18__logos span:nth-child(2) {
  font-weight: 500;
  font-style: italic;
  letter-spacing: 0;
  font-size: 1.15rem;
}

.frm-18__logos span:nth-child(3) {
  font-weight: 600;
  letter-spacing: -.02em;
}

.frm-18__logos span:nth-child(4) {
  letter-spacing: .3em;
  font-size: .85rem;
}

.frm-18__form {
  display: grid;
  gap: 1rem;
  padding: clamp(1.25rem,4cqi,2rem);
  border-radius: 1.5rem;
  border: 1px solid var(--line);
  background: var(--card);
  -webkit-backdrop-filter: blur(24px) saturate(1.3);
  backdrop-filter: blur(24px) saturate(1.3);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.07), 0 40px 80px -30px rgba(0,0,0,.6);
}

.frm-18 h3 {
  margin: 0 0 .2rem;
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -.02em;
}

.frm-18__field {
  display: grid;
  gap: .4rem;
}

.frm-18__two {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,10rem),1fr));
}

.frm-18 label,
.frm-18 legend {
  font-size: .82rem;
  font-weight: 600;
}

.frm-18 input:not([type="radio"]):not([type="checkbox"]) {
  width: 100%;
  min-height: 2.9rem;
  padding: .6rem .9rem;
  border-radius: .75rem;
  border: 1px solid var(--line);
  background: var(--field);
  color: var(--ink);
  font: inherit;
  font-size: .97rem;
  transition: border-color .2s, box-shadow .2s;
}

.frm-18 ::placeholder {
  color: color-mix(in oklab,var(--muted) 70%,transparent);
}

.frm-18 input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--accent) 35%,transparent);
}

.frm-18 input:user-invalid {
  border-color: #fb7185;
}

.frm-18__msg {
  margin: 0;
  font-size: .78rem;
}

.frm-18__msg:empty {
  display: none;
}

.frm-18__email[data-state="free"] .frm-18__msg {
  color: var(--warn);
}

.frm-18__email[data-state="work"] .frm-18__msg {
  color: var(--ok);
}

.frm-18__email[data-state="work"] input {
  border-color: color-mix(in oklab,var(--ok) 60%,transparent);
}

.frm-18 fieldset {
  border: 0;
  margin: 0;
  padding: 0;
  min-width: 0;
}

.frm-18 legend {
  padding: 0;
  margin-bottom: .5rem;
  display: flex;
  gap: .5rem;
  align-items: baseline;
}

.frm-18__tz {
  font-weight: 400;
  color: var(--muted);
  font-size: .75rem;
}

.frm-18__seg {
  display: grid;
  grid-template-columns: repeat(5,1fr);
  gap: .2rem;
  padding: .2rem;
  border-radius: .8rem;
  background: var(--field);
  border: 1px solid var(--line);
}

.frm-18__seg legend {
  grid-column: 1/-1;
}

.frm-18 :is(.frm-18__seg,.frm-18__chips,.frm-18__days,.frm-18__slots) label {
  position: relative;
}

.frm-18 :is(.frm-18__seg,.frm-18__chips,.frm-18__days,.frm-18__slots) input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.frm-18__seg span {
  display: grid;
  place-items: center;
  min-height: 2.5rem;
  border-radius: .6rem;
  font-size: .8rem;
  font-weight: 600;
  color: var(--muted);
  transition: all .2s;
}

.frm-18__seg input:checked + span {
  background: var(--ink);
  color: var(--bg);
}

.frm-18__chips {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
}

.frm-18__chips legend {
  width: 100%;
}

.frm-18__chips span {
  display: inline-flex;
  align-items: center;
  min-height: 2.3rem;
  padding: 0 .85rem;
  border-radius: 99px;
  border: 1px solid var(--line);
  font-size: .8rem;
  font-weight: 500;
  color: var(--muted);
  transition: all .2s;
}

.frm-18__chips input:checked + span {
  color: var(--ink);
  border-color: color-mix(in oklab,var(--accent) 70%,transparent);
  background: color-mix(in oklab,var(--accent) 22%,transparent);
}

.frm-18__days {
  display: grid;
  grid-template-columns: repeat(5,1fr);
  gap: .35rem;
  margin-bottom: .5rem;
}

.frm-18__days span {
  display: grid;
  justify-items: center;
  padding: .5rem 0;
  border-radius: .7rem;
  border: 1px solid var(--line);
  background: var(--field);
  transition: all .2s;
}

.frm-18__days small {
  font-size: .66rem;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .08em;
}

.frm-18__days b {
  font-size: 1.05rem;
  font-weight: 700;
}

.frm-18__days input:checked + span {
  border-color: var(--accent);
  background: color-mix(in oklab,var(--accent) 25%,transparent);
}

.frm-18__slots {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(5.25rem,1fr));
  gap: .35rem;
}

.frm-18__slots span {
  display: grid;
  place-items: center;
  min-height: 2.5rem;
  border-radius: .6rem;
  border: 1px solid var(--line);
  font-size: .82rem;
  font-variant-numeric: tabular-nums;
  transition: all .2s;
  animation: frm-18-in .35s var(--ease) both;
  animation-delay: calc(var(--k) * 30ms);
}

@keyframes frm-18-in {
  from {
    opacity: 0;
    scale: .94;
  }
}

.frm-18__slots input:checked + span {
  background: linear-gradient(110deg,var(--accent),var(--accent-2));
  color: #06061a;
  border-color: transparent;
  font-weight: 700;
}

.frm-18 :is(.frm-18__seg,.frm-18__chips,.frm-18__days,.frm-18__slots) input:focus-visible + span {
  outline: 2px solid var(--accent-2);
  outline-offset: 2px;
}

.frm-18 :is(.frm-18__chips,.frm-18__days,.frm-18__slots) label:hover span {
  border-color: color-mix(in oklab,var(--ink) 30%,transparent);
}

.frm-18__book {
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .5rem;
  min-height: 3.2rem;
  border: 0;
  border-radius: .9rem;
  cursor: pointer;
  font: inherit;
  font-weight: 700;
  font-size: 1rem;
  color: #06061a;
  background: linear-gradient(110deg,var(--accent),var(--accent-2));
  box-shadow: 0 14px 30px -12px color-mix(in oklab,var(--accent) 80%,transparent);
  transition: translate .2s var(--ease), filter .2s;
}

.frm-18__book svg {
  width: 1.1rem;
  height: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.3;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: translate .3s var(--ease);
}

.frm-18__book::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg,transparent 30%,rgba(255,255,255,.45) 50%,transparent 70%);
  translate: -100% 0;
  transition: translate .8s var(--ease);
}

.frm-18__book:hover {
  translate: 0 -2px;
}

.frm-18__book:hover svg {
  translate: 3px 0;
}

.frm-18__book:hover::after {
  translate: 100% 0;
}

.frm-18__book:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.frm-18__fine {
  margin: -.3rem 0 0;
  font-size: .74rem;
  color: var(--muted);
  text-align: center;
}

.frm-18 a {
  color: var(--ink);
  text-underline-offset: 3px;
}

.frm-18 a:hover {
  color: var(--accent-2);
}

.frm-18__status {
  margin: 0;
  font-size: .88rem;
  text-align: center;
  font-weight: 600;
}

.frm-18__status:empty {
  display: none;
}

.frm-18__status[data-ok="true"] {
  color: var(--ok);
}

.frm-18__status[data-ok="false"] {
  color: #fb7185;
}

@media (prefers-reduced-motion: reduce) {
  .frm-18 *,
    .frm-18 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-18__mesh,
    .frm-18::after {
    display: none;
  }

  .frm-18 :is(.frm-18__seg,.frm-18__days,.frm-18__slots,.frm-18__chips) input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .frm-18__book {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-18 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-18__theme {
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

.frm-18__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-18__theme:active {
  transform: scale(.94);
}

.frm-18__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-18__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-18__theme .frm-18__sun,
.frm-18__theme[aria-pressed="true"] .frm-18__moon {
  display: none;
}

.frm-18__theme[aria-pressed="true"] .frm-18__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-18__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-18__theme {
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
  document.querySelectorAll('.frm-18').forEach((root) => {
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
  const root = document.querySelector('.frm-18');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const FREE = new Set(['gmail.com', 'googlemail.com', 'outlook.com', 'hotmail.com', 'live.com', 'yahoo.com', 'yahoo.co.uk', 'icloud.com', 'me.com', 'aol.com', 'proton.me', 'protonmail.com']);
  const email = $('#frm-18-e'), field = $('.frm-18__email'), msg = $('#frm-18-e-msg'), company = $('#frm-18-c');
  let autoCo = false;
  email.addEventListener('blur', () => {
    const domain = (email.value.split('@')[1] || '').toLowerCase();
    if (!email.checkValidity() || !domain) { field.dataset.state = 'idle'; msg.textContent = ''; return; }
    if (FREE.has(domain)) { field.dataset.state = 'free'; msg.textContent = 'Looks like a personal address — a work email helps us prepare a tailored demo.'; return; }
    field.dataset.state = 'work'; msg.textContent = '✓ Work email';
    if (!company.value || autoCo) { const n = domain.split('.')[0]; company.value = n.charAt(0).toUpperCase() + n.slice(1); autoCo = true; }
  });
  company.addEventListener('input', () => { autoCo = false; });
  const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC';
  const tzShort = new Intl.DateTimeFormat('en-US', { timeZoneName: 'short' }).formatToParts(new Date()).find((p) => p.type === 'timeZoneName');
  $('.frm-18__tz').textContent = '· ' + (tzShort ? tzShort.value : tz);
  const days = []; const d = new Date(); d.setHours(0, 0, 0, 0);
  while (days.length < 5) { d.setDate(d.getDate() + 1); if (d.getDay() % 6) days.push(new Date(d)); }
  const wd = new Intl.DateTimeFormat('en-US', { weekday: 'short' }), full = new Intl.DateTimeFormat('en-US', { weekday: 'long', month: 'short', day: 'numeric' });
  const tf = new Intl.DateTimeFormat('en-US', { hour: 'numeric', minute: '2-digit' });
  $('.frm-18__days').innerHTML = days.map((x, i) => '<label><input type="radio" name="frm-18-d" value="' + i + '"' + (i ? '' : ' checked') + ' aria-label="' + full.format(x) + '"><span aria-hidden="true"><small>' + wd.format(x) + '</small><b>' + x.getDate() + '</b></span></label>').join('');
  const slotsFor = (i) => { const base = days[i], out = []; [9, 10, 11, 13, 14, 15, 16].forEach((h, k) => { if ((i + k) % 3 !== 1) { const t = new Date(base); t.setHours(h, k % 2 ? 30 : 0); out.push(t); } }); return out; };
  const renderSlots = () => {
    const i = Number(root.querySelector('[name="frm-18-d"]:checked').value);
    $('.frm-18__slots').innerHTML = slotsFor(i).map((t, k) => '<label><input type="radio" name="frm-18-t" value="' + t.toISOString() + '" aria-label="' + tf.format(t) + '"><span style="--k:' + k + '" aria-hidden="true">' + tf.format(t) + '</span></label>').join('');
  };
  $('.frm-18__days').addEventListener('change', renderSlots); renderSlots();
  $('.frm-18__book').addEventListener('click', () => {
    const status = $('.frm-18__status');
    const bad = [...root.querySelectorAll('input[required]')].find((f) => !f.checkValidity());
    if (bad) { bad.reportValidity(); return; }
    const t = root.querySelector('[name="frm-18-t"]:checked');
    if (!t) { status.dataset.ok = 'false'; status.textContent = 'Choose a time slot to continue.'; root.querySelector('[name="frm-18-t"]').focus(); return; }
    const when = new Date(t.value);
    status.dataset.ok = 'true';
    status.textContent = 'Booked for ' + full.format(when) + ' at ' + tf.format(when) + '. Calendar invite sent to ' + email.value + '.';
    $('.frm-18__book span').textContent = 'Demo booked';
  });
})();
```
