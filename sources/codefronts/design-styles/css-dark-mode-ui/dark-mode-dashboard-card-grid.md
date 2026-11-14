---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-dashboard-card-grid/"
title: "Dark Mode Dashboard Card Grid"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "Six metric cards — MRR, signups, churn, active users, response time, uptime — with inline SVG sparklines, tabular-figure readouts and delta chips that pair a…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Dashboard Card Grid
Source: https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-dashboard-card-grid/

Six metric cards — MRR, signups, churn, active users, response time, uptime — with inline SVG sparklines, tabular-figure readouts and delta chips that pair a direction arrow with colour so status never rests on hue alone. Cards sit on a gradient between two surface tokens, which is what stops a dark dashboard from reading as one flat black rectangle. Theme toggle in the header, pure CSS.
## HTML
```html
<div class="dmu-06">
  <div class="dmu-06__stage">
    <div class="dmu-06__shell">
      <header class="dmu-06__bar">
        <div class="dmu-06__title">
          <h1 class="dmu-06__h1">Growth</h1>
          <p class="dmu-06__sub">Last 30 days &middot; production</p>
        </div>
        <div class="dmu-06__barTools">
          <span class="dmu-06__range">30d</span>
          <input class="dmu-06__sr" type="checkbox" id="dmu-06-toggle">
          <label class="dmu-06__toggle" for="dmu-06-toggle">
            <svg class="dmu-06__sun" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.8v2M12 19.2v2M2.8 12h2M19.2 12h2M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
            <svg class="dmu-06__moon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4Z"/></svg>
            <span class="dmu-06__sr">Toggle theme</span>
          </label>
        </div>
      </header>

      <div class="dmu-06__grid">
        <article class="dmu-06__card">
          <div class="dmu-06__cardHead"><h2>MRR</h2><span class="dmu-06__chip dmu-06__chip--up"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 15l6-6 6 6"/></svg>12.4&#37; up</span></div>
          <p class="dmu-06__value">&#36;148,920</p>
          <svg class="dmu-06__spark" viewBox="0 0 100 32" preserveAspectRatio="none" aria-hidden="true"><path d="M0 26 12 24 24 25 36 19 48 20 60 13 72 14 84 7 100 4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <p class="dmu-06__foot">&#36;16.4k added this month</p>
        </article>

        <article class="dmu-06__card">
          <div class="dmu-06__cardHead"><h2>Signups</h2><span class="dmu-06__chip dmu-06__chip--up"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 15l6-6 6 6"/></svg>8.1&#37; up</span></div>
          <p class="dmu-06__value">3,284</p>
          <svg class="dmu-06__spark" viewBox="0 0 100 32" preserveAspectRatio="none" aria-hidden="true"><path d="M0 22 12 25 24 18 36 21 48 14 60 17 72 10 84 12 100 6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <p class="dmu-06__foot">412 from the launch post</p>
        </article>

        <article class="dmu-06__card dmu-06__card--warn">
          <div class="dmu-06__cardHead"><h2>Churn</h2><span class="dmu-06__chip dmu-06__chip--down"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>0.4pt down</span></div>
          <p class="dmu-06__value">2.1&#37;</p>
          <svg class="dmu-06__spark" viewBox="0 0 100 32" preserveAspectRatio="none" aria-hidden="true"><path d="M0 8 12 11 24 9 36 14 48 12 60 17 72 19 84 22 100 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <p class="dmu-06__foot">Lowest since March</p>
        </article>

        <article class="dmu-06__card">
          <div class="dmu-06__cardHead"><h2>Active users</h2><span class="dmu-06__chip dmu-06__chip--up"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 15l6-6 6 6"/></svg>3.6&#37; up</span></div>
          <p class="dmu-06__value">21,905</p>
          <svg class="dmu-06__spark" viewBox="0 0 100 32" preserveAspectRatio="none" aria-hidden="true"><path d="M0 20 12 17 24 19 36 15 48 16 60 12 72 13 84 9 100 8" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <p class="dmu-06__foot">7-day rolling average</p>
        </article>

        <article class="dmu-06__card">
          <div class="dmu-06__cardHead"><h2>Response time</h2><span class="dmu-06__chip dmu-06__chip--flat">holding flat</span></div>
          <p class="dmu-06__value">142<span>ms p95</span></p>
          <svg class="dmu-06__spark" viewBox="0 0 100 32" preserveAspectRatio="none" aria-hidden="true"><path d="M0 16 12 14 24 17 36 15 48 16 60 14 72 17 84 15 100 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <p class="dmu-06__foot">iad1 &middot; fra1 &middot; syd1</p>
        </article>

        <article class="dmu-06__card">
          <div class="dmu-06__cardHead"><h2>Uptime</h2><span class="dmu-06__chip dmu-06__chip--ok"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.8 4.2 4.2L19 7.4"/></svg>on target</span></div>
          <p class="dmu-06__value">99.98&#37;</p>
          <div class="dmu-06__bars" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i class="is-dip"></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
          <p class="dmu-06__foot">One 4-minute degradation</p>
        </article>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.dmu-06 {
  --bg: #08080b;
  --surface: #101015;
  --surface-elevated: #181820;
  --ink: #f5f5f7;
  --muted: #8f8f9d;
  --line: #242430;
  --sheen: rgba(255,255,255,.05);
  --accent: #7dd3fc;
  --accent-ink: #031c27;
  --good: #4ade80;
  --bad: #fb923c;
  --flat: #a1a1aa;
  --shadow: rgba(0,0,0,.75);
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(120% 90% at 50% -20%,rgba(125,211,252,.09),var(--bg) 62%),var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-06[data-theme="light"],
.dmu-06:has(#dmu-06-toggle:checked) {
  --bg: #f2f3f6;
  --surface: #ffffff;
  --surface-elevated: #ffffff;
  --ink: #0b0b12;
  --muted: #5c6270;
  --line: #e2e5ec;
  --sheen: rgba(11,11,18,.03);
  --accent: #0369a1;
  --accent-ink: #ffffff;
  --good: #15803d;
  --bad: #c2410c;
  --flat: #52525b;
  --shadow: rgba(11,11,18,.16);
  background: radial-gradient(120% 90% at 50% -20%,rgba(3,105,161,.10),var(--bg) 62%),var(--bg);
  color-scheme: light;
}

@media (prefers-color-scheme: light) {
  .dmu-06:not([data-theme="dark"]):not(:has(#dmu-06-toggle:checked)) {
    --bg: #f2f3f6;
    --surface: #ffffff;
    --surface-elevated: #ffffff;
    --ink: #0b0b12;
    --muted: #5c6270;
    --line: #e2e5ec;
    --sheen: rgba(11,11,18,.03);
    --accent: #0369a1;
    --accent-ink: #ffffff;
    --good: #15803d;
    --bad: #c2410c;
    --flat: #52525b;
    --shadow: rgba(11,11,18,.16);
    background: radial-gradient(120% 90% at 50% -20%,rgba(3,105,161,.10),var(--bg) 62%),var(--bg);
    color-scheme: light;
  }
  /* flip-back: light OS + checked restores the dark base */

  .dmu-06:has(#dmu-06-toggle:checked) {
    --bg: #08080b;
    --surface: #101015;
    --surface-elevated: #181820;
    --ink: #f5f5f7;
    --muted: #8f8f9d;
    --line: #242430;
    --sheen: rgba(255,255,255,.05);
    --accent: #7dd3fc;
    --accent-ink: #031c27;
    --good: #4ade80;
    --bad: #fb923c;
    --flat: #a1a1aa;
    --shadow: rgba(0,0,0,.75);
    background: radial-gradient(120% 90% at 50% -20%,rgba(125,211,252,.09),var(--bg) 62%),var(--bg);
    color-scheme: dark;
  }
}

.dmu-06,
.dmu-06 *,
.dmu-06 *::before,
.dmu-06 *::after {
  box-sizing: border-box;
}

.dmu-06__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-06__shell {
  width: min(74rem,100%);
  display: grid;
  gap: clamp(1rem,2.5vw,1.6rem);
}

.dmu-06__bar {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.dmu-06__h1 {
  margin: 0;
  font-size: clamp(1.5rem,3.4vw,2.1rem);
  font-weight: 650;
  letter-spacing: -.035em;
}

.dmu-06__sub {
  margin: .25rem 0 0;
  font-size: .82rem;
  color: var(--muted);
  font-family: var(--mono);
}

.dmu-06__barTools {
  display: flex;
  align-items: center;
  gap: .5rem;
}

.dmu-06__range {
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--muted);
  padding: .45rem .65rem;
  border: 1px solid var(--line);
  border-radius: .5rem;
  background: var(--surface);
}

.dmu-06__toggle {
  display: grid;
  place-items: center;
  width: 2.6rem;
  height: 2.6rem;
  border-radius: .7rem;
  cursor: pointer;
  background: var(--surface);
  border: 1px solid var(--line);
  color: var(--ink);
  transition: border-color .2s ease, translate .2s ease;
}

.dmu-06__toggle:hover {
  border-color: color-mix(in oklab,var(--accent) 55%,var(--line));
  translate: 0 -1px;
}

.dmu-06__toggle svg {
  width: 1.1rem;
  height: 1.1rem;
}

.dmu-06__sun {
  display: none;
}

.dmu-06__moon {
  display: block;
}

.dmu-06:has(#dmu-06-toggle:checked) .dmu-06__sun {
  display: block;
}

.dmu-06:has(#dmu-06-toggle:checked) .dmu-06__moon {
  display: none;
}

@media (prefers-color-scheme: light) {
  .dmu-06:not(:has(#dmu-06-toggle:checked)) .dmu-06__sun {
    display: block;
  }

  .dmu-06:not(:has(#dmu-06-toggle:checked)) .dmu-06__moon {
    display: none;
  }

  .dmu-06:has(#dmu-06-toggle:checked) .dmu-06__sun {
    display: none;
  }

  .dmu-06:has(#dmu-06-toggle:checked) .dmu-06__moon {
    display: block;
  }
}

.dmu-06:has(#dmu-06-toggle:focus-visible) .dmu-06__toggle {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.dmu-06__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(16rem,1fr));
}

.dmu-06__card {
  display: grid;
  gap: .6rem;
  padding: 1.15rem 1.2rem 1.05rem;
  border-radius: 1rem;
  color: var(--ink);
  background: linear-gradient(168deg,var(--surface-elevated),var(--surface));
  border: 1px solid var(--line);
  box-shadow: inset 0 1px 0 var(--sheen), 0 24px 46px -38px var(--shadow);
  transition: border-color .22s ease, translate .22s cubic-bezier(.16,1,.3,1);
}

.dmu-06__card:hover {
  translate: 0 -2px;
  border-color: color-mix(in oklab,var(--accent) 40%,var(--line));
}

.dmu-06__card--warn {
  --accent: var(--bad);
}

.dmu-06__cardHead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .6rem;
}

.dmu-06__cardHead h2 {
  margin: 0;
  font-size: .8rem;
  font-weight: 550;
  letter-spacing: .02em;
  color: var(--muted);
}

.dmu-06__chip {
  display: inline-flex;
  align-items: center;
  gap: .25rem;
  font-family: var(--mono);
  font-size: .68rem;
  padding: .24rem .45rem;
  border-radius: .4rem;
  border: 1px solid currentColor;
  white-space: nowrap;
}

.dmu-06__chip svg {
  width: .8rem;
  height: .8rem;
}

.dmu-06__chip--up,
.dmu-06__chip--down,
.dmu-06__chip--ok {
  color: var(--good);
}

.dmu-06__chip--flat {
  color: var(--flat);
}

.dmu-06__value {
  margin: 0;
  font-family: var(--mono);
  font-variant-numeric: tabular-nums;
  font-size: clamp(1.7rem,3.4vw,2.15rem);
  font-weight: 600;
  letter-spacing: -.045em;
  display: flex;
  align-items: baseline;
  gap: .45rem;
}

.dmu-06__value span {
  font-size: .7rem;
  font-weight: 400;
  letter-spacing: .04em;
  color: var(--muted);
}

.dmu-06__spark {
  display: block;
  width: 100%;
  height: 2.75rem;
  color: var(--accent);
  overflow: visible;
}

.dmu-06__spark path {
  vector-effect: non-scaling-stroke;
}

.dmu-06__bars {
  display: flex;
  align-items: flex-end;
  gap: .18rem;
  height: 2.75rem;
}

.dmu-06__bars i {
  flex: 1;
  height: 100%;
  border-radius: .15rem;
  background: color-mix(in oklab,var(--good) 55%,transparent);
}

.dmu-06__bars i.is-dip {
  height: 52%;
  background: var(--bad);
}

.dmu-06__foot {
  margin: 0;
  font-size: .76rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .dmu-06__card,
    .dmu-06__toggle {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-06__card,
    .dmu-06__toggle,
    .dmu-06__range {
    border-color: CanvasText;
    box-shadow: none;
    background: Canvas;
  }

  .dmu-06__spark {
    color: CanvasText;
  }

  .dmu-06__bars i {
    background: Highlight;
  }
}
```
