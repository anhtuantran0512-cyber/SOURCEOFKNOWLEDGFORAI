---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/leaderboard-ranking-widget/"
title: "Leaderboard Ranking Widget"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Top-contributors leaderboard using CSS counters. Ranks 1-3 render in gold/silver/bronze gradient text; top row gets a subtle accent tint."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Leaderboard Ranking Widget
Source: https://codefronts.com/components/css-cards/leaderboard-ranking-widget/

Top-contributors leaderboard using CSS counters. Ranks 1-3 render in gold/silver/bronze gradient text; top row gets a subtle accent tint.
## HTML
```html
<section class="card-10">
  <article class="card-10__card">
    <div class="card-10__glow" aria-hidden="true"></div>
    <header class="card-10__head">
      <div class="card-10__head-left">
        <div class="card-10__title-row">
          <h3 class="card-10__title">Top contributors</h3>
          <span class="card-10__live">
            <span class="card-10__live-dot" aria-hidden="true"></span>
            LIVE
          </span>
        </div>
        <p class="card-10__eye">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          Updated 12s ago · resets Aug 1
        </p>
      </div>
      <div class="card-10__filter" role="tablist" aria-label="Timeframe">
        <button type="button" role="tab" aria-selected="false" class="card-10__filter-btn">Week</button>
        <button type="button" role="tab" aria-selected="true" class="card-10__filter-btn card-10__filter-btn--active">Month</button>
      </div>
    </header>
    <div class="card-10__podium" aria-hidden="true">
      <div class="card-10__podium-glow card-10__podium-glow--2"></div>
      <div class="card-10__podium-glow card-10__podium-glow--1"></div>
      <div class="card-10__podium-glow card-10__podium-glow--3"></div>
    </div>
    <ol class="card-10__list">
      <li class="card-10__row card-10__row--gold">
        <div class="card-10__rank-wrap">
          <span class="card-10__rank" aria-label="Rank 1">1</span>
          <span class="card-10__medal" aria-hidden="true">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1z"/></svg>
          </span>
        </div>
        <span class="card-10__avatar card-10__avatar--1">
          AK
          <span class="card-10__streak" aria-label="12-day streak">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2s-4 4-4 8a4 4 0 0 0 8 0c0-1-1-2-1-2s2 2 2 5a5 5 0 0 1-10 0c0-6 5-11 5-11z"/></svg>
            12
          </span>
        </span>
        <div class="card-10__who">
          <span class="card-10__name">Ada Karim</span>
          <span class="card-10__role">Core maintainer · <span class="card-10__delta card-10__delta--up">▲ 2</span></span>
        </div>
        <div class="card-10__score-wrap">
          <span class="card-10__score">4,820</span>
          <span class="card-10__gain">+287</span>
        </div>
      </li>
      <li class="card-10__row card-10__row--silver">
        <div class="card-10__rank-wrap">
          <span class="card-10__rank" aria-label="Rank 2">2</span>
        </div>
        <span class="card-10__avatar card-10__avatar--2">MO</span>
        <div class="card-10__who">
          <span class="card-10__name">Miguel Ortiz</span>
          <span class="card-10__role">Docs lead · <span class="card-10__delta card-10__delta--down">▼ 1</span></span>
        </div>
        <div class="card-10__score-wrap">
          <span class="card-10__score">3,915</span>
          <span class="card-10__gain">+142</span>
        </div>
      </li>
      <li class="card-10__row card-10__row--bronze">
        <div class="card-10__rank-wrap">
          <span class="card-10__rank" aria-label="Rank 3">3</span>
        </div>
        <span class="card-10__avatar card-10__avatar--3">SN</span>
        <div class="card-10__who">
          <span class="card-10__name">Sana Novak</span>
          <span class="card-10__role">Frontend · <span class="card-10__delta card-10__delta--up">▲ 4</span></span>
        </div>
        <div class="card-10__score-wrap">
          <span class="card-10__score">3,204</span>
          <span class="card-10__gain">+412</span>
        </div>
      </li>
      <li class="card-10__row">
        <div class="card-10__rank-wrap"><span class="card-10__rank" aria-label="Rank 4">4</span></div>
        <span class="card-10__avatar card-10__avatar--4">RT</span>
        <div class="card-10__who">
          <span class="card-10__name">Ren Tanaka</span>
          <span class="card-10__role">Infra · <span class="card-10__delta card-10__delta--flat">— 0</span></span>
        </div>
        <div class="card-10__score-wrap">
          <span class="card-10__score">2,671</span>
          <span class="card-10__gain">+94</span>
        </div>
      </li>
      <li class="card-10__row card-10__row--you">
        <div class="card-10__rank-wrap"><span class="card-10__rank" aria-label="Rank 5">5</span></div>
        <span class="card-10__avatar card-10__avatar--5">LF</span>
        <div class="card-10__who">
          <span class="card-10__name">Lena Fjord<span class="card-10__you">You</span></span>
          <span class="card-10__role">Design · <span class="card-10__delta card-10__delta--up">▲ 7</span></span>
        </div>
        <div class="card-10__score-wrap">
          <span class="card-10__score">2,140</span>
          <span class="card-10__gain">+521</span>
        </div>
      </li>
    </ol>
    <footer class="card-10__foot">
      <p class="card-10__foot-msg">
        <span class="card-10__foot-emoji" aria-hidden="true">🔥</span>
        You're climbing fast — <strong>682</strong> to reach rank 4
      </p>
      <a href="#full" class="card-10__foot-link">
        See all
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </footer>
  </article>
</section>
```
## CSS
```css
.card-10 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 15%, rgba(251, 191, 36, 0.05) 0%, transparent 45%), radial-gradient(ellipse at 80% 85%, rgba(236, 72, 153, 0.05) 0%, transparent 45%), #faf9f5;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #f59e0b;
  --gold: #f59e0b;
  --gold-lite: #fbbf24;
  --silver: #94a3b8;
  --bronze: #c2410c;
}

.card-10 *,
.card-10 *::before,
.card-10 *::after {
  box-sizing: border-box;
}

.card-10__card {
  position: relative;
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 24px;
  padding: 20px 20px 12px;
  overflow: hidden;
  box-shadow: 0 30px 60px -30px rgba(60, 40, 20, 0.2), 0 0 0 1px rgba(255, 255, 255, 0.5) inset, 0 -1px 0 rgba(0, 0, 0, 0.02) inset;
  isolation: isolate;
}
/* Aura glow behind everything — reads as premium container */

.card-10__glow {
  position: absolute;
  top: -80px;
  left: -80px;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(251, 191, 36, 0.14) 0%, transparent 55%), radial-gradient(circle at 60% 60%, rgba(236, 72, 153, 0.10) 0%, transparent 55%);
  filter: blur(30px);
  pointer-events: none;
  z-index: -1;
}
/* ── header ── */

.card-10__head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
  position: relative;
  z-index: 1;
}

.card-10__title-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
}

.card-10__title {
  font-size: 16px;
  font-weight: 700;
  margin: 0;
  color: #1a1a1a;
  letter-spacing: -0.02em;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-10__live {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: #dc2626;
  padding: 2px 6px;
  background: rgba(220, 38, 38, 0.08);
  border: 1px solid rgba(220, 38, 38, 0.2);
  border-radius: 4px;
}

.card-10__live-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #dc2626;
  animation: card-10-blink 1.4s ease-in-out infinite;
}

.card-10__eye {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 11px;
  color: #9ca3af;
  margin: 0;
}

.card-10__eye svg {
  flex-shrink: 0;
}

.card-10__filter {
  display: inline-flex;
  padding: 3px;
  background: #f3f2ee;
  border: 1px solid rgba(0, 0, 0, 0.04);
  border-radius: 999px;
  gap: 2px;
}

.card-10__filter-btn {
  min-height: 26px;
  padding: 4px 12px;
  border: 0;
  border-radius: 999px;
  background: transparent;
  color: #6b6b7c;
  font: 600 11px 'Inter', sans-serif;
  cursor: pointer;
  letter-spacing: -0.005em;
  transition: color 0.18s, background 0.18s;
}

.card-10__filter-btn:hover {
  color: #1a1a1a;
}

.card-10__filter-btn--active {
  background: #fff;
  color: #1a1a1a;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08), 0 0 0 1px rgba(0, 0, 0, 0.04);
}

.card-10__filter-btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* ── decorative podium glow behind top 3 ── */

.card-10__podium {
  position: absolute;
  top: 68px;
  left: 20px;
  right: 20px;
  height: 168px;
  pointer-events: none;
  z-index: 0;
}

.card-10__podium-glow {
  position: absolute;
  width: 100%;
  height: 56px;
  border-radius: 12px;
  filter: blur(20px);
}

.card-10__podium-glow--1 {
  top: 0;
  background: linear-gradient(90deg, rgba(251, 191, 36, 0.18), transparent 70%);
}

.card-10__podium-glow--2 {
  top: 56px;
  background: linear-gradient(90deg, rgba(148, 163, 184, 0.14), transparent 70%);
}

.card-10__podium-glow--3 {
  top: 112px;
  background: linear-gradient(90deg, rgba(194, 65, 12, 0.14), transparent 70%);
}
/* ── list ── */

.card-10__list {
  list-style: none;
  padding: 0;
  margin: 0 0 12px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  position: relative;
  z-index: 1;
}

.card-10__row {
  display: grid;
  grid-template-columns: 32px 40px 1fr auto;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: 14px;
  transition: background 0.18s, transform 0.18s;
  position: relative;
}

.card-10__row:hover {
  background: rgba(0, 0, 0, 0.02);
  transform: translateX(2px);
}

.card-10__row--gold {
  background: linear-gradient(90deg, rgba(251, 191, 36, 0.12), rgba(251, 191, 36, 0.03) 70%);
  border: 1px solid rgba(251, 191, 36, 0.2);
}

.card-10__row--silver {
  background: linear-gradient(90deg, rgba(148, 163, 184, 0.10), rgba(148, 163, 184, 0.02) 70%);
  border: 1px solid rgba(148, 163, 184, 0.16);
}

.card-10__row--bronze {
  background: linear-gradient(90deg, rgba(194, 65, 12, 0.10), rgba(194, 65, 12, 0.02) 70%);
  border: 1px solid rgba(194, 65, 12, 0.15);
}

.card-10__row--gold:hover {
  background: linear-gradient(90deg, rgba(251, 191, 36, 0.18), rgba(251, 191, 36, 0.05) 70%);
}

.card-10__row--silver:hover {
  background: linear-gradient(90deg, rgba(148, 163, 184, 0.14), rgba(148, 163, 184, 0.03) 70%);
}

.card-10__row--bronze:hover {
  background: linear-gradient(90deg, rgba(194, 65, 12, 0.14), rgba(194, 65, 12, 0.03) 70%);
}

.card-10__row--you {
  background: linear-gradient(90deg, rgba(99, 102, 241, 0.08), transparent 70%);
  border: 1px solid rgba(99, 102, 241, 0.16);
}

.card-10__row--you:hover {
  background: linear-gradient(90deg, rgba(99, 102, 241, 0.12), transparent 70%);
}
/* rank number */

.card-10__rank-wrap {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
}

.card-10__rank {
  font-size: 18px;
  font-weight: 800;
  color: #cbd5e1;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.03em;
}

.card-10__row--gold .card-10__rank {
  background: linear-gradient(135deg, #fde047 0%, #f59e0b 50%, #b45309 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 1px 1px rgba(180, 83, 9, 0.35));
}

.card-10__row--silver .card-10__rank {
  background: linear-gradient(135deg, #e2e8f0 0%, #94a3b8 60%, #64748b 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-10__row--bronze .card-10__rank {
  background: linear-gradient(135deg, #fdba74 0%, #ea580c 60%, #9a3412 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
/* medal star badge on rank 1 */

.card-10__medal {
  position: absolute;
  top: -6px;
  right: -4px;
  width: 15px;
  height: 15px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #fde047 0%, #f59e0b 100%);
  border: 1.5px solid #fff;
  border-radius: 50%;
  color: #fff;
  box-shadow: 0 2px 5px rgba(245, 158, 11, 0.45);
}
/* avatar */

.card-10__avatar {
  position: relative;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  color: #fff;
  font-size: 12px;
  font-weight: 700;
  border: 2px solid #fff;
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.05), 0 2px 6px rgba(0, 0, 0, 0.08);
  letter-spacing: -0.01em;
}

.card-10__avatar--1 {
  background: linear-gradient(135deg, #f472b6, #ec4899);
}

.card-10__avatar--2 {
  background: linear-gradient(135deg, #60a5fa, #3b82f6);
}

.card-10__avatar--3 {
  background: linear-gradient(135deg, #34d399, #10b981);
}

.card-10__avatar--4 {
  background: linear-gradient(135deg, #a78bfa, #7c3aed);
}

.card-10__avatar--5 {
  background: linear-gradient(135deg, #fb923c, #f97316);
}
/* streak flame on rank 1 avatar */

.card-10__streak {
  position: absolute;
  bottom: -6px;
  left: 50%;
  transform: translateX(-50%);
  display: inline-flex;
  align-items: center;
  gap: 1px;
  padding: 1px 4px 1px 2px;
  background: linear-gradient(135deg, #fb923c, #dc2626);
  color: #fff;
  font-size: 8px;
  font-weight: 800;
  border: 1.5px solid #fff;
  border-radius: 999px;
  box-shadow: 0 2px 5px rgba(220, 38, 38, 0.35);
  letter-spacing: 0.02em;
}
/* name + role stack */

.card-10__who {
  display: flex;
  flex-direction: column;
  gap: 1px;
  min-width: 0;
}

.card-10__name {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 13px;
  font-weight: 700;
  color: #1a1a1a;
  letter-spacing: -0.005em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card-10__you {
  display: inline-block;
  font-size: 8.5px;
  font-weight: 800;
  color: #4338ca;
  padding: 1px 5px;
  background: rgba(99, 102, 241, 0.14);
  border-radius: 4px;
  letter-spacing: 0.06em;
  vertical-align: middle;
}

.card-10__role {
  font-size: 11px;
  color: #6b6b7c;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card-10__delta {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10px;
  font-weight: 700;
  padding: 0 4px;
  border-radius: 3px;
  letter-spacing: -0.01em;
}

.card-10__delta--up {
  color: #059669;
  background: rgba(52, 211, 153, 0.14);
}

.card-10__delta--down {
  color: #dc2626;
  background: rgba(220, 38, 38, 0.10);
}

.card-10__delta--flat {
  color: #9ca3af;
  background: rgba(148, 163, 184, 0.14);
}
/* score */

.card-10__score-wrap {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 1px;
}

.card-10__score {
  font-size: 14px;
  font-weight: 800;
  color: #1a1a1a;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}

.card-10__gain {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 700;
  color: #059669;
  letter-spacing: 0.01em;
}
/* footer */

.card-10__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding-top: 10px;
  border-top: 1px dashed rgba(0, 0, 0, 0.06);
  position: relative;
  z-index: 1;
}

.card-10__foot-msg {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 11.5px;
  color: #4b4b57;
  margin: 0;
}

.card-10__foot-msg strong {
  color: #4338ca;
  font-weight: 700;
}

.card-10__foot-emoji {
  filter: drop-shadow(0 2px 3px rgba(220, 38, 38, 0.35));
}

.card-10__foot-link {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 11.5px;
  font-weight: 700;
  color: #4338ca;
  text-decoration: none;
  padding: 4px 6px;
  border-radius: 6px;
  transition: color 0.18s, background 0.18s;
}

.card-10__foot-link:hover {
  color: #312e81;
  background: rgba(99, 102, 241, 0.06);
}

.card-10__foot-link:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

@keyframes card-10-blink {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0.4;
    transform: scale(0.85);
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-10__live-dot {
    animation: none;
  }

  .card-10__row,
    .card-10__filter-btn,
    .card-10__foot-link {
    transition: none;
  }

  .card-10__row:hover {
    transform: none;
  }
}
```
