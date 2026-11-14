---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/gaming-esports/"
title: "Esports Gamer Review Card"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "Aggressive, angular, and technically the most interesting card here: clipped corners via clip-path, a neon edge painted as a second clipped layer behind the…"
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Esports Gamer Review Card
Source: https://codefronts.com/components/css-testimonials-reviews/gaming-esports/

Aggressive, angular, and technically the most interesting card here: clipped corners via clip-path, a neon edge painted as a second clipped layer behind the card, a scanline overlay and rank tags. Every effect is a gradient or a polygon — no images, no SVG filters, no blend-mode tricks that fall apart on mobile.
## HTML
```html
<section class="tr-20" aria-label="Esports gamer review card demo">
  <div class="tr-20__stage">
    <header class="tr-20__head">
      <p class="tr-20__eyebrow">Player verdicts</p>
      <h2 class="tr-20__title">Tested at 240Hz. Reviewed at 3am.</h2>
    </header>

    <div class="tr-20__row">
      <div class="tr-20__frame" style="--tr-20-neon:oklch(0.82 0.19 195)">
        <figure class="tr-20__card">
          <div class="tr-20__scan" aria-hidden="true"></div>
          <header class="tr-20__ph">
            <img src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of player VEXHOLLOW" width="48" height="48" loading="lazy" decoding="async">
            <div>
              <b>VEXHOLLOW <svg class="tr-20__v" viewBox="0 0 20 20" aria-label="Verified player"><circle cx="10" cy="10" r="8.4"/><path d="M6.4 10.2l2.4 2.4 4.8-5" fill="none" stroke="#04131a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></b>
              <span>RADIANT · 1,842 hrs · AU-SE</span>
            </div>
            <span class="tr-20__score">9.4</span>
          </header>
          <blockquote>Switched mid-season and my first-shot accuracy went up four points inside a week. The 0.6&nbsp;ms claim is marketing, but the polling actually is rock solid — no stutter in a full 12-hour scrim block.</blockquote>
          <ul class="tr-20__stats">
            <li><b>+4.1</b>first-shot %</li>
            <li><b>0.9</b>ms measured</li>
            <li><b>12h</b>scrim tested</li>
          </ul>
          <footer class="tr-20__f">
            <span class="tr-20__tag">GEAR · MOUSE</span>
            <time datetime="2026-07-04">4 July 2026</time>
          </footer>
        </figure>
      </div>

      <div class="tr-20__frame" style="--tr-20-neon:oklch(0.75 0.22 330)">
        <figure class="tr-20__card">
          <div class="tr-20__scan" aria-hidden="true"></div>
          <header class="tr-20__ph">
            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of player NOVAKIRI" width="48" height="48" loading="lazy" decoding="async">
            <div>
              <b>NOVAKIRI <svg class="tr-20__v" viewBox="0 0 20 20" aria-label="Verified player"><circle cx="10" cy="10" r="8.4"/><path d="M6.4 10.2l2.4 2.4 4.8-5" fill="none" stroke="#150414" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></b>
              <span>IMMORTAL 3 · 940 hrs · EU-W</span>
            </div>
            <span class="tr-20__score">8.7</span>
          </header>
          <blockquote>Panel is genuinely excellent. Stand wobbles if your desk does, and the OSD is a maze — but I have not thought about the monitor once during a match, which is the only review that matters.</blockquote>
          <ul class="tr-20__stats">
            <li><b>240</b>Hz native</li>
            <li><b>3.1</b>ms GtG</li>
            <li><b>0</b>dead pixels</li>
          </ul>
          <footer class="tr-20__f">
            <span class="tr-20__tag">GEAR · DISPLAY</span>
            <time datetime="2026-06-18">18 June 2026</time>
          </footer>
        </figure>
      </div>
    </div>
    <p class="tr-20__chip" aria-hidden="true">clip-path polygon() double-layer neon frame · scanline gradient · skewed sweep · rank tags</p>
  </div>
</section>
```
## CSS
```css
.tr-20,
.tr-20 *,
.tr-20 *::before,
.tr-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-20-bg: oklch(0.13 0.02 250);
  --tr-20-surf: oklch(0.175 0.022 250);
  --tr-20-ink: oklch(0.95 0.008 250);
  --tr-20-mut: oklch(0.68 0.02 250);
  background: var(--tr-20-bg);
  color: var(--tr-20-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
  background-image: radial-gradient(60% 40% at 50% 0%,oklch(0.3 0.09 260/.5),transparent 65%);
}

.tr-20__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3vw,32px);
  padding: clamp(20px,4vw,54px);
}

.tr-20__head {
  text-align: center;
  display: grid;
  gap: 9px;
}

.tr-20__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: oklch(0.82 0.19 195);
}

.tr-20__title {
  font-size: clamp(24px,4vw,42px);
  font-weight: 750;
  letter-spacing: -.04em;
  line-height: 1.06;
  text-transform: uppercase;
  text-wrap: balance;
}

.tr-20__row {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,320px),1fr));
  gap: clamp(16px,2.2vw,24px);
  width: min(100%,1000px);
  align-items: start;
}

.tr-20__frame {
  --tr-20-cut: 24px;
  --tr-20-shape: polygon(var(--tr-20-cut) 0,100% 0,100% calc(100% - var(--tr-20-cut)),calc(100% - var(--tr-20-cut)) 100%,0 100%,0 var(--tr-20-cut));
  position: relative;
  clip-path: var(--tr-20-shape);
  background: linear-gradient(150deg,var(--tr-20-neon),color-mix(in oklch,var(--tr-20-neon) 25%,transparent) 55%,var(--tr-20-neon));
  padding: 2px;
  animation: tr-20-in .75s cubic-bezier(.16,1,.3,1) both;
}

.tr-20__frame:nth-child(2) {
  animation-delay: .1s;
}

@keyframes tr-20-in {
  from {
    opacity: 0;
    translate: 0 18px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-20__frame::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background: var(--tr-20-neon);
  filter: blur(28px);
  opacity: .32;
  clip-path: var(--tr-20-shape);
}

.tr-20__card {
  position: relative;
  clip-path: var(--tr-20-shape);
  background: linear-gradient(165deg,color-mix(in oklch,var(--tr-20-neon) 8%,var(--tr-20-surf)),var(--tr-20-surf) 60%);
  padding: clamp(20px,2.6vw,26px);
  display: grid;
  gap: 16px;
  overflow: hidden;
}

.tr-20__scan {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(0deg,oklch(1 0 0/.045) 0 1px,transparent 1px 4px);
}

.tr-20__card::after {
  content: '';
  position: absolute;
  inset-block: -40%;
  inset-inline-start: -60%;
  inline-size: 40%;
  background: linear-gradient(100deg,transparent,oklch(1 0 0/.09) 50%,transparent);
  rotate: 12deg;
  animation: tr-20-sweep 6s linear infinite;
  pointer-events: none;
}

@keyframes tr-20-sweep {
  to {
    translate: 420% 0;
  }
}

.tr-20__ph {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
}

.tr-20__ph img {
  width: 48px;
  height: 48px;
  object-fit: cover;
  flex: none;
  clip-path: polygon(8px 0,100% 0,100% calc(100% - 8px),calc(100% - 8px) 100%,0 100%,0 8px);
  background: oklch(0.3 0.04 250);
}

.tr-20__ph div {
  display: grid;
  gap: 3px;
  min-width: 0;
}

.tr-20__ph b {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 14.5px;
  font-weight: 700;
  letter-spacing: .06em;
}

.tr-20__v {
  width: 15px;
  height: 15px;
  fill: var(--tr-20-neon);
}

.tr-20__ph span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .12em;
  color: var(--tr-20-mut);
}

.tr-20__score {
  margin-inline-start: auto;
  font-size: 26px;
  font-weight: 780;
  letter-spacing: -.05em;
  color: var(--tr-20-neon);
  font-variant-numeric: tabular-nums;
  text-shadow: 0 0 22px color-mix(in oklch,var(--tr-20-neon) 60%,transparent);
}

.tr-20__card blockquote {
  position: relative;
  font-size: 14.5px;
  line-height: 1.6;
  color: oklch(0.93 0.008 250);
  text-wrap: pretty;
}

.tr-20__stats {
  position: relative;
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.tr-20__stats li {
  display: grid;
  gap: 1px;
  padding: 9px 13px;
  background: oklch(1 0 0/.05);
  border: 1px solid oklch(1 0 0/.09);
  clip-path: polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--tr-20-mut);
}

.tr-20__stats b {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 17px;
  font-weight: 720;
  letter-spacing: -.03em;
  color: var(--tr-20-ink);
  font-variant-numeric: tabular-nums;
}

.tr-20__f {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding-top: 14px;
  border-top: 1px solid oklch(1 0 0/.1);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .12em;
  color: var(--tr-20-mut);
}

.tr-20__tag {
  padding: 4px 10px;
  background: color-mix(in oklch,var(--tr-20-neon) 18%,transparent);
  border: 1px solid color-mix(in oklch,var(--tr-20-neon) 40%,transparent);
  color: var(--tr-20-neon);
  font-weight: 700;
}

.tr-20__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-20-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .tr-20__frame {
    animation: none;
  }

  .tr-20__card::after {
    animation: none;
    opacity: 0;
  }
}
```
