---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/portfolio-project-card/"
title: "Portfolio Project Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Portfolio tile with a CSS-drawn dashboard mockup (top bar, side nav, KPI row, bar chart), category chip, project title, description, tags, and a client +…"
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Portfolio Project Card
Source: https://codefronts.com/components/css-cards/portfolio-project-card/

Portfolio tile with a CSS-drawn dashboard mockup (top bar, side nav, KPI row, bar chart), category chip, project title, description, tags, and a client + "View project →" footer.
## HTML
```html
<section class="card-14">
  <article class="card-14__card">
    <div class="card-14__thumb">
      <div class="card-14__mock" aria-hidden="true">
        <div class="card-14__mock-top"></div>
        <div class="card-14__mock-body">
          <div class="card-14__mock-side">
            <span></span><span></span><span></span><span></span>
          </div>
          <div class="card-14__mock-main">
            <div class="card-14__mock-kpi"><span></span><span></span><span></span></div>
            <div class="card-14__mock-chart">
              <span style="height:35%"></span>
              <span style="height:55%"></span>
              <span style="height:40%"></span>
              <span style="height:70%"></span>
              <span style="height:60%"></span>
              <span style="height:85%"></span>
              <span style="height:50%"></span>
              <span style="height:75%"></span>
            </div>
          </div>
        </div>
      </div>
      <div class="card-14__overlay" aria-hidden="true"></div>
    </div>
    <div class="card-14__body">
      <span class="card-14__chip">SAAS &middot; DASHBOARD</span>
      <h3 class="card-14__title">Meridian Analytics Rebrand</h3>
      <p class="card-14__desc">Redesigned the analytics dashboard for 12k+ enterprise users — 41% faster time-to-insight.</p>
      <ul class="card-14__tags">
        <li>Figma</li>
        <li>Design System</li>
        <li>Data Viz</li>
      </ul>
      <div class="card-14__foot">
        <span class="card-14__client">Meridian Labs</span>
        <a class="card-14__link" href="#project">View project <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
.card-14 {
  width: 100%;
  min-height: 100vh;
  display: block;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: #f8f7f4;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #b8613b;
}

.card-14 *,
.card-14 *::before,
.card-14 *::after {
  box-sizing: border-box;
}

.card-14__card {
  width: 100%;
  max-width: 340px;
  margin-left: auto;
  margin-right: auto;
  background: #fff;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid rgba(0,0,0,0.06);
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
  transition: transform 0.25s, box-shadow 0.25s;
}

.card-14__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 14px 32px rgba(184,97,59,0.14);
}

.card-14__thumb {
  position: relative;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg, #f7edd6, #e8c9a0);
  overflow: hidden;
}

.card-14__mock {
  position: absolute;
  inset: 14px;
  background: #fff;
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(60,30,10,0.15);
  transition: transform 0.35s ease;
}

.card-14__card:hover .card-14__mock {
  transform: scale(1.04);
}

.card-14__mock-top {
  height: 12px;
  background: #f0eae1;
  border-bottom: 1px solid rgba(0,0,0,0.06);
}

.card-14__mock-body {
  display: grid;
  grid-template-columns: 40px 1fr;
  height: calc(100% - 12px);
}

.card-14__mock-side {
  background: #faf7f2;
  padding: 8px 6px;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.card-14__mock-side span {
  display: block;
  height: 5px;
  border-radius: 2px;
  background: #e0d5c4;
}

.card-14__mock-side span:first-child {
  background: #b8613b;
}

.card-14__mock-main {
  padding: 8px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.card-14__mock-kpi {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 4px;
}

.card-14__mock-kpi span {
  height: 20px;
  background: #f0eae1;
  border-radius: 3px;
}

.card-14__mock-chart {
  flex: 1;
  display: flex;
  align-items: flex-end;
  gap: 3px;
  padding-top: 4px;
}

.card-14__mock-chart span {
  flex: 1;
  background: linear-gradient(180deg, #d97e4a, #b8451f);
  border-radius: 2px 2px 0 0;
}

.card-14__overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 60%, rgba(0,0,0,0.05));
  transition: opacity 0.3s;
}

.card-14__card:hover .card-14__overlay {
  opacity: 0;
}

.card-14__body {
  padding: 16px 18px 18px;
}

.card-14__chip {
  display: inline-block;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: #b8613b;
  background: rgba(184,97,59,0.1);
  padding: 4px 9px;
  border-radius: 999px;
  margin-bottom: 10px;
}

.card-14__title {
  font-size: 16px;
  font-weight: 700;
  margin: 0 0 6px;
  color: #1a1a1a;
  letter-spacing: -0.01em;
}

.card-14__desc {
  font-size: 12.5px;
  color: #6b6459;
  margin: 0 0 12px;
  line-height: 1.55;
}

.card-14__tags {
  list-style: none;
  padding: 0;
  margin: 0 0 14px;
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.card-14__tags li {
  font-size: 11px;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 4px;
  background: #f5f2ec;
  color: #6b6459;
}

.card-14__foot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 12px;
  border-top: 1px solid rgba(0,0,0,0.06);
}

.card-14__client {
  font-size: 12px;
  color: #6b6459;
  font-weight: 600;
}

.card-14__link {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  min-height: 44px;
  font-size: 12.5px;
  font-weight: 600;
  color: #b8613b;
  text-decoration: none;
}

.card-14__link:hover span {
  transform: translateX(3px);
}

.card-14__link span {
  display: inline-block;
  transition: transform 0.2s;
}

.card-14__link:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
  border-radius: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .card-14__card,
    .card-14__mock,
    .card-14__overlay,
    .card-14__link span {
    transition: none;
  }

  .card-14__card:hover {
    transform: none;
  }

  .card-14__card:hover .card-14__mock {
    transform: none;
  }

  .card-14__link:hover span {
    transform: none;
  }
}
```
