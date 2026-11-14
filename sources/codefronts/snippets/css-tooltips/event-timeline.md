---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/event-timeline/"
title: "Event Timeline"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A horizontal seven-event company timeline (seed → IPO) with alternating labels above and below the track."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Event Timeline
Source: https://codefronts.com/snippets/css-tooltips/event-timeline/

A horizontal seven-event company timeline (seed → IPO) with alternating labels above and below the track. Hovering any dot reveals an event card with quarter, headline, body prose, and a metric badge (valuation, ARR, market cap). For about pages, investor pages, retrospectives.
## HTML
```html
<div class="tp-19">
  <div class="tp-19__track">
    <div class="tp-19__events">
      <div class="tp-19__event">
        <div class="tp-19__label">Seed Round</div>
        <div class="tp-19__dot"></div>
        <div class="tp-19__year">2018</div>
        <div class="tp-19__card">
          <div class="tp-19__card-top"><div class="tp-19__card-year">Q3 · 2018</div><div class="tp-19__card-title">Seed Funding Closed</div><span class="tp-19__badge tp-19__badge-mile">Milestone</span></div>
          <div class="tp-19__body">$2.4M raised from 12 angel investors. The round was led by two former founders from the enterprise SaaS sector, providing both capital and key industry connections.</div>
          <div class="tp-19__impact"><span class="tp-19__impact-label">Runway</span><span class="tp-19__impact-val">18 months secured</span></div>
        </div>
      </div>
      <div class="tp-19__event">
        <div class="tp-19__label">Public Beta</div>
        <div class="tp-19__dot"></div>
        <div class="tp-19__year">2019</div>
        <div class="tp-19__card">
          <div class="tp-19__card-top"><div class="tp-19__card-year">Q1 · 2019</div><div class="tp-19__card-title">Public Beta Launch</div><span class="tp-19__badge tp-19__badge-prod">Product</span></div>
          <div class="tp-19__body">First 1,000 paying customers acquired within 90 days. Net Promoter Score of 72 in initial surveys. Product-market fit validated across legal, healthcare, fintech.</div>
          <div class="tp-19__impact"><span class="tp-19__impact-label">ARR at launch</span><span class="tp-19__impact-val">$480K</span></div>
        </div>
      </div>
      <div class="tp-19__event">
        <div class="tp-19__label">Series A</div>
        <div class="tp-19__dot"></div>
        <div class="tp-19__year">2020</div>
        <div class="tp-19__card">
          <div class="tp-19__card-top"><div class="tp-19__card-year">Q2 · 2020</div><div class="tp-19__card-title">Series A — $12M</div><span class="tp-19__badge tp-19__badge-mile">Milestone</span></div>
          <div class="tp-19__body">$12M Series A led by Sequoia Capital. Round closed despite pandemic uncertainty, reflecting strong retention. Funds used to double engineering headcount.</div>
          <div class="tp-19__impact"><span class="tp-19__impact-label">Post-money</span><span class="tp-19__impact-val">$68M</span></div>
        </div>
      </div>
      <div class="tp-19__event">
        <div class="tp-19__label">EU Expansion</div>
        <div class="tp-19__dot"></div>
        <div class="tp-19__year">2021</div>
        <div class="tp-19__card">
          <div class="tp-19__card-top"><div class="tp-19__card-year">Q3 · 2021</div><div class="tp-19__card-title">100K Users · EU Launch</div><span class="tp-19__badge tp-19__badge-prod">Growth</span></div>
          <div class="tp-19__body">Crossed 100,000 active users and launched GDPR-compliant EU data centres in Frankfurt and Dublin. Opened London office with 24 hires. MRR surpassed $1M.</div>
          <div class="tp-19__impact"><span class="tp-19__impact-label">EU share</span><span class="tp-19__impact-val">31% of new ARR</span></div>
        </div>
      </div>
      <div class="tp-19__event">
        <div class="tp-19__label">Series B</div>
        <div class="tp-19__dot"></div>
        <div class="tp-19__year">2022</div>
        <div class="tp-19__card">
          <div class="tp-19__card-top"><div class="tp-19__card-year">Q1 · 2022</div><div class="tp-19__card-title">Series B — $45M · Profitable</div><span class="tp-19__badge tp-19__badge-mile">Milestone</span></div>
          <div class="tp-19__body">$45M Series B led by Andreessen Horowitz. Achieved first profitable quarter ahead of schedule. Capital allocated to enterprise sales infrastructure.</div>
          <div class="tp-19__impact"><span class="tp-19__impact-label">Valuation</span><span class="tp-19__impact-val">$320M post-money</span></div>
        </div>
      </div>
      <div class="tp-19__event">
        <div class="tp-19__label">Acquisition</div>
        <div class="tp-19__dot"></div>
        <div class="tp-19__year">2023</div>
        <div class="tp-19__card">
          <div class="tp-19__card-top"><div class="tp-19__card-year">Q2 · 2023</div><div class="tp-19__card-title">Acquired Synapse Labs</div><span class="tp-19__badge tp-19__badge-acq">M&amp;A</span></div>
          <div class="tp-19__body">Acquired Synapse Labs, a 22-person AI workflow automation startup, for $280M. The deal added Synapse's LLM orchestration layer, accelerating the roadmap.</div>
          <div class="tp-19__impact"><span class="tp-19__impact-label">ARR added</span><span class="tp-19__impact-val">$8.4M</span></div>
        </div>
      </div>
      <div class="tp-19__event">
        <div class="tp-19__label">IPO Filed</div>
        <div class="tp-19__dot"></div>
        <div class="tp-19__year">2024</div>
        <div class="tp-19__card">
          <div class="tp-19__card-top"><div class="tp-19__card-year">Q3 · 2024</div><div class="tp-19__card-title">S-1 Filed · NASDAQ</div><span class="tp-19__badge tp-19__badge-ipo">Public Markets</span></div>
          <div class="tp-19__body">Filed S-1 registration with the SEC. IPO priced at $18/share, valuing the company at $1.2B. Shares began trading on NASDAQ under the ticker SNYP, closing up 38% on day one.</div>
          <div class="tp-19__impact"><span class="tp-19__impact-label">Market cap</span><span class="tp-19__impact-val">$1.65B (day 1)</span></div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-19 {
  width: 100%;
  min-height: 100vh;
  background: #0e0c14;
  /* Top + bottom room — event cards alternate above and below the
       track. Odd events flip column-reverse so the label lands above
       the dot and the card pops up. Cards are ~220px tall. */
  padding: 240px 24px;
  font-family: 'Inter', system-ui, sans-serif;
  position: relative;
  overflow: hidden;
}

.tp-19::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 60% 50% at 50% 50%, rgba(80, 40, 120, 0.08) 0%, transparent 70%);
  pointer-events: none;
}

.tp-19__track {
  max-width: 760px;
  margin: 0 auto;
  position: relative;
  padding: 40px 0;
}

.tp-19__track::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(to right, transparent, rgba(120, 80, 200, 0.3) 10%, rgba(120, 80, 200, 0.3) 90%, transparent);
  transform: translateY(-50%);
}

.tp-19__events {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
}

.tp-19__event {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: help;
}

.tp-19__event:nth-child(odd) {
  flex-direction: column-reverse;
}

.tp-19__label {
  font-size: 9px;
  color: rgba(180, 140, 240, 0.5);
  text-align: center;
  margin: 11px 0;
  letter-spacing: 0.08em;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
}

.tp-19__year {
  font-size: 11px;
  font-weight: 700;
  color: rgba(180, 140, 240, 0.7);
  text-align: center;
  margin: 11px 0;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  letter-spacing: 0.04em;
}

.tp-19__dot {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: rgba(120, 80, 200, 0.6);
  border: 2px solid rgba(120, 80, 200, 0.3);
  transition: background .15s, box-shadow .15s, transform .15s;
  position: relative;
  z-index: 2;
  flex-shrink: 0;
}

.tp-19__event:hover .tp-19__dot {
  background: rgba(160, 110, 240, 0.9);
  box-shadow: 0 0 14px 4px rgba(120, 80, 200, 0.25);
  transform: scale(1.3);
}

.tp-19__card {
  position: absolute;
  left: 50%;
  transform: translateX(-50%) translateY(-6px);
  z-index: 200;
  width: 250px;
  background: rgba(14, 12, 22, 0.97);
  border: 1px solid rgba(120, 80, 200, 0.2);
  border-radius: 10px;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .2s, transform .2s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .2s;
  box-shadow: 0 16px 44px rgba(0, 0, 0, 0.9), 0 0 0 1px rgba(120, 80, 200, 0.08);
  overflow: hidden;
  text-align: left;
}

.tp-19__event:nth-child(odd) .tp-19__card {
  bottom: calc(100% + 10px);
  top: auto;
}

.tp-19__event:nth-child(even) .tp-19__card {
  top: calc(100% + 10px);
  bottom: auto;
}

.tp-19__event:hover .tp-19__card {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
  transition-delay: 0s;
}

.tp-19__card-top {
  padding: 12px 13px 10px;
  border-bottom: 1px solid rgba(120, 80, 200, 0.1);
}

.tp-19__card-year {
  font-size: 8.5px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  color: rgba(160, 110, 240, 0.5);
  letter-spacing: 0.1em;
  margin-bottom: 4px;
}

.tp-19__card-title {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.88);
  line-height: 1.3;
  font-family: Georgia, serif;
}

.tp-19__badge {
  display: inline-block;
  font-size: 7.5px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  padding: 2px 7px;
  border-radius: 3px;
  margin-top: 7px;
  letter-spacing: 0.07em;
  text-transform: uppercase;
}

.tp-19__badge-mile {
  background: rgba(80, 160, 80, 0.15);
  color: rgba(120, 200, 120, 0.8);
  border: 1px solid rgba(80, 160, 80, 0.2);
}

.tp-19__badge-prod {
  background: rgba(80, 120, 200, 0.15);
  color: rgba(120, 160, 240, 0.8);
  border: 1px solid rgba(80, 120, 200, 0.2);
}

.tp-19__badge-acq {
  background: rgba(200, 120, 40, 0.15);
  color: rgba(240, 160, 80, 0.8);
  border: 1px solid rgba(200, 120, 40, 0.2);
}

.tp-19__badge-ipo {
  background: rgba(160, 80, 200, 0.15);
  color: rgba(200, 120, 240, 0.8);
  border: 1px solid rgba(160, 80, 200, 0.2);
}

.tp-19__body {
  padding: 9px 13px;
  font-size: 11px;
  color: rgba(255, 255, 255, 0.5);
  line-height: 1.55;
  border-bottom: 1px solid rgba(120, 80, 200, 0.06);
  font-style: italic;
  font-family: Georgia, serif;
}

.tp-19__impact {
  padding: 9px 13px;
  display: flex;
  justify-content: space-between;
  font-size: 9.5px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
}

.tp-19__impact-label {
  color: rgba(120, 80, 200, 0.5);
}

.tp-19__impact-val {
  color: rgba(200, 160, 255, 0.7);
}
```
