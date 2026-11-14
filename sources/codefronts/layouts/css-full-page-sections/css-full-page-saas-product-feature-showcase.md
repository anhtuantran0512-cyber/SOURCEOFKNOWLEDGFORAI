---
source: "codefronts"
url: "https://codefronts.com/layouts/css-full-page-sections/css-full-page-saas-product-feature-showcase/"
title: "CSS Full Page SaaS Product Feature Showcase"
section: "layouts"
category: "css-full-page-sections"
category_name: "CSS Full Page Sections"
description: "The applied template: five full-viewport panels &mdash; hero, two feature panels with real interface mock-ups, a metrics panel and a closing call to action…"
has_js: "false"
---

Here's a working CSS Full Page Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Full Page SaaS Product Feature Showcase
Source: https://codefronts.com/layouts/css-full-page-sections/css-full-page-saas-product-feature-showcase/

The applied template: five full-viewport panels &mdash; hero, two feature panels with real interface mock-ups, a metrics panel and a closing call to action &mdash; for a release-orchestration product called Cadence. Pure CSS, inline SVG icons, no images to wait on, and copy you can swap for your own product in one pass.
## HTML
```html
<div class="fps-09">
  <input class="fps-09__sr" type="checkbox" id="fps-09-dark">
  <label class="fps-09__theme" for="fps-09-dark" title="Switch light or dark theme">
    <svg class="fps-09__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="fps-09__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="fps-09__vh">Switch light or dark theme</span>
  </label>

  <div class="fps-09__scroller" tabindex="0" role="group" aria-label="Cadence product tour, five panels">

    <section class="fps-09__panel fps-09__panel--hero" id="fps-09-s1" aria-labelledby="fps-09-h1">
      <div class="fps-09__stage">
        <p class="fps-09__brand">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M3 15.5l4.2-7.6 3.4 5.2 2.6-3.4 2.3 3.6L21 6.8" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Cadence
        </p>
        <h2 class="fps-09__title" id="fps-09-h1">Ship every service on the same heartbeat</h2>
        <p class="fps-09__lead">Cadence turns 40 independent deploy pipelines into one release train &mdash; with a rollback that takes eleven seconds instead of an incident channel.</p>
        <div class="fps-09__actions">
          <button class="fps-09__btn" type="button">Start a free workspace</button>
          <a class="fps-09__ghost" href="#fps-09-s2">See how it works</a>
        </div>
        <ul class="fps-09__trust">
          <li>SOC 2 Type II</li><li>Self-host or cloud</li><li>Terraform provider</li>
        </ul>
        <p class="fps-09__cue"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Five panels, one screen each</p>
      </div>
    </section>

    <section class="fps-09__panel" id="fps-09-s2" aria-labelledby="fps-09-h2">
      <div class="fps-09__stage fps-09__stage--split">
        <div class="fps-09__col">
          <p class="fps-09__eyebrow"><span class="fps-09__num">01 / 03</span><span class="fps-09__mono">release trains</span></p>
          <h2 class="fps-09__title fps-09__title--sm" id="fps-09-h2">One board for every service in flight</h2>
          <p class="fps-09__lead">Group services into trains, set a window, and Cadence sequences the rollout &mdash; holding anything whose checks are still amber and promoting the rest without a human in the loop.</p>
          <ul class="fps-09__feats">
            <li>
              <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12.5l4.4 4.2L19.5 6.4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span><strong>Gated promotion</strong>Checks, budgets and approvals evaluated per service, not per repo.</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 7.5v9M7.5 12h9" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="12" r="8.2" stroke="currentColor" stroke-width="1.7"/></svg>
              <span><strong>Eleven-second rollback</strong>Every train keeps the last good manifest warm.</span>
            </li>
          </ul>
        </div>
        <div class="fps-09__mock" role="img" aria-label="Cadence release board showing four services with staged rollout status">
          <div class="fps-09__mockbar"><span class="fps-09__dot"></span><span class="fps-09__dot"></span><span class="fps-09__dot"></span><em>release / train-04</em></div>
          <div class="fps-09__mockbody">
            <div class="fps-09__row"><span class="fps-09__svc">checkout-api</span><span class="fps-09__prog" style="--p:100%"></span><span class="fps-09__stat fps-09__stat--ok">live</span></div>
            <div class="fps-09__row"><span class="fps-09__svc">payments-worker</span><span class="fps-09__prog" style="--p:74%"></span><span class="fps-09__stat">74%</span></div>
            <div class="fps-09__row"><span class="fps-09__svc">search-index</span><span class="fps-09__prog" style="--p:38%"></span><span class="fps-09__stat">38%</span></div>
            <div class="fps-09__row"><span class="fps-09__svc">notify-fanout</span><span class="fps-09__prog fps-09__prog--hold" style="--p:12%"></span><span class="fps-09__stat fps-09__stat--hold">held</span></div>
            <p class="fps-09__mockfoot">Window closes 18:40 UTC &middot; 2 approvals pending</p>
          </div>
        </div>
      </div>
    </section>

    <section class="fps-09__panel" id="fps-09-s3" aria-labelledby="fps-09-h3">
      <div class="fps-09__stage fps-09__stage--split fps-09__stage--flip">
        <div class="fps-09__col">
          <p class="fps-09__eyebrow"><span class="fps-09__num">02 / 03</span><span class="fps-09__mono">change health</span></p>
          <h2 class="fps-09__title fps-09__title--sm" id="fps-09-h3">Every deploy scored before anyone is paged</h2>
          <p class="fps-09__lead">Cadence watches latency, error rate and saturation for eight minutes after each promotion, compares against the pre-deploy baseline, and pauses the train the moment a signal drifts.</p>
          <ul class="fps-09__feats">
            <li>
              <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M3.5 16.5l4.5-5.4 3.3 3 3-4.4 6.2 6.8" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span><strong>Baseline diffing</strong>Compared against the previous seven deploys, not a fixed threshold.</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.2l7.5 3.4v5.1c0 4-3.1 6.4-7.5 7.6-4.4-1.2-7.5-3.6-7.5-7.6V7.6L12 4.2Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
              <span><strong>Auto-hold, never auto-guess</strong>The train pauses and posts the diff; a human decides.</span>
            </li>
          </ul>
        </div>
        <div class="fps-09__mock" role="img" aria-label="Change health panel showing p95 latency, error rate and saturation against baseline">
          <div class="fps-09__mockbar"><span class="fps-09__dot"></span><span class="fps-09__dot"></span><span class="fps-09__dot"></span><em>health / checkout-api</em></div>
          <div class="fps-09__mockbody">
            <div class="fps-09__kpis">
              <div><dt>p95 latency</dt><dd>182<span>ms</span></dd><em>&minus;4% vs baseline</em></div>
              <div><dt>error rate</dt><dd>0.04<span>%</span></dd><em>flat</em></div>
              <div><dt>saturation</dt><dd>61<span>%</span></dd><em>+3 pts</em></div>
            </div>
            <div class="fps-09__spark" aria-hidden="true"><i style="--v:38%"></i><i style="--v:52%"></i><i style="--v:44%"></i><i style="--v:66%"></i><i style="--v:58%"></i><i style="--v:71%"></i><i style="--v:49%"></i><i style="--v:63%"></i><i style="--v:55%"></i><i style="--v:74%"></i><i style="--v:60%"></i><i style="--v:47%"></i></div>
            <p class="fps-09__mockfoot">Verdict: promote &middot; 8 min observation window met</p>
          </div>
        </div>
      </div>
    </section>

    <section class="fps-09__panel fps-09__panel--metrics" id="fps-09-s4" aria-labelledby="fps-09-h4">
      <div class="fps-09__stage">
        <p class="fps-09__eyebrow"><span class="fps-09__num">03 / 03</span><span class="fps-09__mono">measured across 8,400 workspaces</span></p>
        <h2 class="fps-09__title fps-09__title--sm" id="fps-09-h4">What changes in the first quarter</h2>
        <dl class="fps-09__metrics">
          <div><dt>41%</dt><dd>shorter median lead time from merge to production</dd></div>
          <div><dt>11s</dt><dd>median rollback, down from 6 minutes of manual steps</dd></div>
          <div><dt>99.98%</dt><dd>promotion success rate across 2.4M releases</dd></div>
          <div><dt>3.1&times;</dt><dd>more deploys per engineer per week, same headcount</dd></div>
        </dl>
        <p class="fps-09__foot">Figures from customer telemetry, rolling 90 days, medians not means.</p>
      </div>
    </section>

    <section class="fps-09__panel fps-09__panel--cta" id="fps-09-s5" aria-labelledby="fps-09-h5">
      <div class="fps-09__stage">
        <p class="fps-09__eyebrow"><span class="fps-09__mono">get started</span></p>
        <h2 class="fps-09__title" id="fps-09-h5">Put your first train on the board this afternoon</h2>
        <p class="fps-09__lead">Connect a repository, pick three services, set a window. Cadence runs the next release for you and shows the diff before it promotes anything.</p>
        <div class="fps-09__actions">
          <button class="fps-09__btn" type="button">Create a workspace</button>
          <button class="fps-09__ghost fps-09__ghost--btn" type="button">Book a 20-minute walkthrough</button>
        </div>
        <p class="fps-09__quote">&ldquo;We cut release night from four people and two hours to one person and a coffee.&rdquo;<span>Alex Chen &middot; platform lead, Northwind Retail</span></p>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fps-09 {
  --bg: #f7f8fc;
  --panel: #ffffff;
  --panel2: #f0f2f9;
  --deep: #0a0c18;
  --ink: #0a0c18;
  --muted: rgba(10,12,24,.62);
  --line: rgba(10,12,24,.10);
  --accent: #3538cd;
  --ok: #0f766e;
  --hold: #b45309;
  --sans: 'Geist',system-ui,-apple-system,'Segoe UI',sans-serif;
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  isolation: isolate;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% .1 250)) {
  .fps-09 {
    --accent: oklch(46% .2 274);
    --ok: oklch(48% .1 175);
    --hold: oklch(56% .13 62);
    --ink: oklch(12% .02 270);
    --bg: oklch(97.6% .006 270);
    --panel2: oklch(95% .01 270);
  }
}

.fps-09 * {
  box-sizing: border-box;
}

.fps-09 h2,
.fps-09 p,
.fps-09 ul,
.fps-09 dl,
.fps-09 dd,
.fps-09 dt {
  margin: 0;
}

.fps-09 code {
  font-family: var(--mono);
  font-size: .92em;
}

.fps-09__sr,
.fps-09__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-09__theme {
  position: fixed;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 80;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  cursor: pointer;
  color: var(--ink);
  background: rgba(255,255,255,.65);
  border: 1px solid var(--line);
  -webkit-backdrop-filter: blur(10px) saturate(150%);
  backdrop-filter: blur(10px) saturate(150%);
  box-shadow: 0 8px 24px -12px rgba(10,12,24,.35);
}

.fps-09__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.fps-09__theme svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fps-09__moon {
  display: none;
}

.fps-09__sr:focus-visible + .fps-09__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-09__scroller {
  block-size: 100dvh;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
  overscroll-behavior-y: contain;
  scrollbar-width: none;
}

.fps-09__scroller::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.fps-09__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.fps-09__panel {
  position: relative;
  min-block-size: 100dvh;
  scroll-snap-align: start;
  background: var(--panel);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(2rem,5vh,3.5rem) clamp(1.25rem,5vw,4.5rem) calc(clamp(2rem,5vh,3.5rem) + 4rem);
}

.fps-09__panel:nth-child(even) {
  background: var(--panel2);
}

.fps-09__panel + .fps-09__panel {
  margin-block-start: -4rem;
  border-start-start-radius: 1.9rem;
  border-start-end-radius: 1.9rem;
  border-block-start: 1px solid var(--line);
  box-shadow: 0 -30px 64px -34px rgba(10,12,24,.22);
}

@supports not (height: 100dvh) {
  .fps-09__scroller {
    block-size: 100vh;
  }

  .fps-09__panel {
    min-block-size: 100vh;
  }
}

.fps-09__panel--hero {
  background: radial-gradient(90% 70% at 82% 6%,color-mix(in srgb,var(--accent) 16%,transparent),transparent 68%), var(--panel);
}

.fps-09__panel--cta {
  background: var(--deep);
  color: #f6f7ff;
}

.fps-09__panel--cta .fps-09__lead,
.fps-09__panel--cta .fps-09__mono {
  color: rgba(246,247,255,.68);
}

.fps-09__panel--cta .fps-09__mono {
  border-color: rgba(246,247,255,.22);
}

.fps-09__panel--cta .fps-09__quote {
  border-color: #a5b4fc;
}

.fps-09__panel--cta .fps-09__quote span {
  color: rgba(246,247,255,.6);
}

.fps-09__panel--cta .fps-09__ghost {
  color: #c7d2fe;
  border-color: rgba(199,210,254,.4);
}

.fps-09__stage {
  inline-size: min(66rem,100%);
  display: grid;
  gap: clamp(.9rem,2.2vh,1.45rem);
  justify-items: start;
}

.fps-09__stage--split {
  grid-template-columns: 1fr 1fr;
  gap: clamp(1.5rem,4vw,3.25rem);
  align-items: center;
}

.fps-09__stage--flip .fps-09__col {
  order: 2;
}

@media (max-width: 60rem) {
  .fps-09__stage--split {
    grid-template-columns: 1fr;
    gap: clamp(1.1rem,3vh,1.75rem);
  }

  .fps-09__stage--flip .fps-09__col {
    order: 0;
  }
}

.fps-09__col {
  display: grid;
  gap: clamp(.85rem,2vh,1.3rem);
  justify-items: start;
}

.fps-09__brand {
  display: flex;
  align-items: center;
  gap: .5rem;
  font-size: 1.02rem;
  font-weight: 550;
  letter-spacing: -.02em;
}

.fps-09__brand svg {
  inline-size: 1.35rem;
  block-size: 1.35rem;
  color: var(--accent);
}

.fps-09__eyebrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
}

.fps-09__num {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.fps-09__mono {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
  padding: .22rem .5rem;
  border: 1px solid var(--line);
  border-radius: .45rem;
}

.fps-09__title {
  font-size: clamp(2rem,5.4vw,4.05rem);
  line-height: 1.02;
  letter-spacing: -.045em;
  font-weight: 600;
  max-inline-size: 21ch;
  text-wrap: balance;
}

.fps-09__title--sm {
  font-size: clamp(1.6rem,3.3vw,2.4rem);
  letter-spacing: -.035em;
  max-inline-size: 24ch;
}

.fps-09__lead {
  font-size: clamp(.98rem,1.35vw,1.15rem);
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 56ch;
  text-wrap: pretty;
}

.fps-09__cue {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-family: var(--mono);
  font-size: .8rem;
  color: var(--muted);
}

.fps-09__cue svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  animation: fps-09-bob 2.4s ease-in-out infinite;
}

@keyframes fps-09-bob {
  0%,
    100% {
    translate: 0 -2px;
  }

  50% {
    translate: 0 3px;
  }
}

.fps-09__actions {
  display: flex;
  flex-wrap: wrap;
  gap: .65rem;
  align-items: center;
}

.fps-09__btn {
  min-block-size: 2.75rem;
  padding: .75rem 1.25rem;
  border-radius: 999px;
  cursor: pointer;
  border: 1px solid transparent;
  font: inherit;
  font-size: .95rem;
  font-weight: 500;
  color: #fff;
  background: var(--accent);
  box-shadow: 0 14px 30px -18px color-mix(in srgb,var(--accent) 80%,black);
  transition: translate .18s ease, background .18s ease;
}

.fps-09__btn:hover {
  translate: 0 -2px;
}

.fps-09__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.fps-09__ghost {
  min-block-size: 2.75rem;
  display: inline-flex;
  align-items: center;
  padding: .75rem 1.15rem;
  border-radius: 999px;
  font: inherit;
  font-size: .95rem;
  text-decoration: none;
  cursor: pointer;
  color: var(--accent);
  background: transparent;
  border: 1px solid color-mix(in srgb,var(--accent) 38%,transparent);
  transition: background .18s ease;
}

.fps-09__ghost:hover {
  background: color-mix(in srgb,var(--accent) 8%,transparent);
}

.fps-09__ghost:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-09__trust {
  list-style: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 1.15rem;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--muted);
}

.fps-09__feats {
  list-style: none;
  padding: 0;
  display: grid;
  gap: .75rem;
  inline-size: 100%;
}

.fps-09__feats li {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .75rem;
  align-items: start;
  padding-block-start: .75rem;
  border-block-start: 1px solid var(--line);
}

.fps-09__feats svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
  color: var(--accent);
  margin-block-start: .15rem;
}

.fps-09__feats span {
  display: grid;
  gap: .15rem;
  font-size: .93rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.fps-09__feats strong {
  color: var(--ink);
  font-weight: 550;
  font-size: .98rem;
}

.fps-09__mock {
  inline-size: 100%;
  border-radius: 1.25rem;
  border: 1px solid var(--line);
  overflow: hidden;
  background: var(--bg);
  box-shadow: 0 30px 64px -38px rgba(10,12,24,.5);
}

.fps-09__mockbar {
  display: flex;
  align-items: center;
  gap: .4rem;
  padding: .65rem .85rem;
  border-block-end: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
}

.fps-09__dot {
  inline-size: .5rem;
  block-size: .5rem;
  border-radius: 999px;
  background: var(--line);
}

.fps-09__mockbar em {
  margin-inline-start: auto;
  font-family: var(--mono);
  font-style: normal;
  font-size: .66rem;
  color: var(--muted);
}

.fps-09__mockbody {
  padding: .85rem;
  display: grid;
  gap: .5rem;
}

.fps-09__row {
  display: grid;
  grid-template-columns: minmax(6rem,1fr) 1.4fr auto;
  gap: .7rem;
  align-items: center;
}

.fps-09__svc {
  font-family: var(--mono);
  font-size: .76rem;
  color: var(--ink);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.fps-09__prog {
  position: relative;
  block-size: .4rem;
  border-radius: 999px;
  background: color-mix(in srgb,var(--ink) 8%,transparent);
  overflow: hidden;
}

.fps-09__prog::after {
  content: '';
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: var(--p);
  border-radius: 999px;
  background: linear-gradient(90deg,var(--accent),color-mix(in srgb,var(--accent) 45%,transparent));
}

.fps-09__prog--hold::after {
  background: linear-gradient(90deg,var(--hold),color-mix(in srgb,var(--hold) 40%,transparent));
}

.fps-09__stat {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  min-inline-size: 2.6rem;
  text-align: end;
}

.fps-09__stat--ok {
  color: var(--ok);
}

.fps-09__stat--hold {
  color: var(--hold);
}

.fps-09__mockfoot {
  font-family: var(--mono);
  font-size: .66rem;
  color: var(--muted);
  padding-block-start: .5rem;
  border-block-start: 1px solid var(--line);
}

.fps-09__kpis {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .6rem;
}

.fps-09__kpis > div {
  display: grid;
  gap: .1rem;
  padding: .6rem .65rem;
  border-radius: .8rem;
  border: 1px solid var(--line);
}

.fps-09__kpis dt {
  font-family: var(--mono);
  font-size: .6rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
}

.fps-09__kpis dd {
  font-size: 1.15rem;
  font-weight: 550;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.fps-09__kpis dd span {
  font-size: .72rem;
  color: var(--muted);
  font-weight: 400;
  margin-inline-start: .1rem;
}

.fps-09__kpis em {
  font-family: var(--mono);
  font-style: normal;
  font-size: .62rem;
  color: var(--ok);
}

.fps-09__spark {
  display: flex;
  align-items: flex-end;
  gap: .28rem;
  block-size: 3.4rem;
  padding: .5rem .1rem 0;
}

.fps-09__spark i {
  flex: 1;
  block-size: var(--v);
  border-radius: .2rem .2rem 0 0;
  background: linear-gradient(to top,color-mix(in srgb,var(--accent) 55%,transparent),color-mix(in srgb,var(--accent) 18%,transparent));
}

.fps-09__metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
  gap: clamp(.85rem,2.5vw,1.75rem);
  inline-size: 100%;
}

.fps-09__metrics > div {
  display: grid;
  gap: .35rem;
  padding-block-start: .9rem;
  border-block-start: 2px solid var(--accent);
}

.fps-09__metrics dt {
  font-size: clamp(2rem,4.2vw,3.1rem);
  font-weight: 600;
  letter-spacing: -.045em;
  font-variant-numeric: tabular-nums;
  line-height: 1;
}

.fps-09__metrics dd {
  font-size: .9rem;
  line-height: 1.45;
  color: var(--muted);
  text-wrap: pretty;
}

.fps-09__foot {
  font-family: var(--mono);
  font-size: .68rem;
  color: var(--muted);
}

.fps-09__quote {
  font-size: clamp(1.05rem,1.9vw,1.35rem);
  line-height: 1.45;
  letter-spacing: -.02em;
  max-inline-size: 44ch;
  padding-inline-start: 1.05rem;
  border-inline-start: 2px solid var(--accent);
  display: grid;
  gap: .55rem;
  text-wrap: pretty;
}

.fps-09__quote span {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.fps-09[data-theme="dark"],
.fps-09:has(#fps-09-dark:checked) {
  --bg: #07080f;
  --panel: #0b0d16;
  --panel2: #10131e;
  --deep: #04050b;
  --ink: #f4f5fb;
  --muted: rgba(244,245,251,.62);
  --line: rgba(244,245,251,.13);
  --accent: #a5b4fc;
  --ok: #5eead4;
  --hold: #fbbf24;
}

.fps-09:has(#fps-09-dark:checked) .fps-09__theme {
  background: rgba(255,255,255,.07);
}

.fps-09:has(#fps-09-dark:checked) .fps-09__sun {
  display: none;
}

.fps-09:has(#fps-09-dark:checked) .fps-09__moon {
  display: block;
}

.fps-09:has(#fps-09-dark:checked) .fps-09__btn {
  color: #0a0c18;
}

@media (prefers-color-scheme: dark) {
  .fps-09:not([data-theme="light"]):not(:has(#fps-09-dark:checked)) {
    --bg: #07080f;
    --panel: #0b0d16;
    --panel2: #10131e;
    --deep: #04050b;
    --ink: #f4f5fb;
    --muted: rgba(244,245,251,.62);
    --line: rgba(244,245,251,.13);
    --accent: #a5b4fc;
    --ok: #5eead4;
    --hold: #fbbf24;
  }

  .fps-09:not([data-theme="light"]):not(:has(#fps-09-dark:checked)) .fps-09__theme {
    background: rgba(255,255,255,.07);
  }

  .fps-09:not([data-theme="light"]):not(:has(#fps-09-dark:checked)) .fps-09__sun {
    display: none;
  }

  .fps-09:not([data-theme="light"]):not(:has(#fps-09-dark:checked)) .fps-09__moon {
    display: block;
  }

  .fps-09:not([data-theme="light"]):not(:has(#fps-09-dark:checked)) .fps-09__btn {
    color: #0a0c18;
  }
}

@supports not selector(:has(*)) {
  .fps-09__theme {
    display: none;
  }
}

@media (max-width: 60rem) {
  .fps-09__scroller {
    scroll-snap-type: y proximity;
  }

  .fps-09__mockbody {
    gap: .35rem;
  }

  .fps-09__spark {
    block-size: 2.6rem;
  }
}

@media (max-height: 40rem) {
  .fps-09__scroller {
    scroll-snap-type: y proximity;
  }

  .fps-09__panel {
    padding-block: 1.25rem 3rem;
  }

  .fps-09__stage {
    gap: .7rem;
  }

  .fps-09__feats li {
    padding-block-start: .5rem;
  }

  .fps-09__spark {
    block-size: 2.4rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fps-09__scroller {
    scroll-snap-type: none;
    scroll-behavior: auto;
  }

  .fps-09 *,
    .fps-09 *::before,
    .fps-09 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fps-09__panel,
    .fps-09__mock,
    .fps-09__btn,
    .fps-09__ghost,
    .fps-09__theme,
    .fps-09__kpis > div {
    border: 1px solid CanvasText;
    box-shadow: none;
    background: Canvas;
    color: CanvasText;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .fps-09__prog::after,
    .fps-09__spark i {
    background: CanvasText;
  }
}
```
