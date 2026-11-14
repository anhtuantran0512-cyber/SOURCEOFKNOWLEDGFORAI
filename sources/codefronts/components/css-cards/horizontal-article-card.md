---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/horizontal-article-card/"
title: "Horizontal Article Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Landscape article preview: cosmic thumbnail on the left, eyebrow + headline + description + meta on the right. Stacks under 640px."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Article Card
Source: https://codefronts.com/components/css-cards/horizontal-article-card/

Landscape article preview: cosmic thumbnail on the left, eyebrow + headline + description + meta on the right. Stacks under 640px.
## HTML
```html
<section class="card-07">
  <div class="card-07__stack">
    <div class="card-07__stack-head">
      <div class="card-07__stack-title">
        <span class="card-07__stack-emoji" aria-hidden="true">📚</span>
        <div>
          <h3 class="card-07__stack-h">For you · Engineering</h3>
          <p class="card-07__stack-sub">Curated by editors · updated 4h ago</p>
        </div>
      </div>
      <div class="card-07__stack-filter" role="tablist" aria-label="Filter">
        <button type="button" role="tab" aria-selected="true" class="card-07__stack-btn card-07__stack-btn--active">Trending</button>
        <button type="button" role="tab" aria-selected="false" class="card-07__stack-btn">New</button>
      </div>
    </div>

    <article class="card-07__card card-07__card--featured">
      <div class="card-07__media" aria-hidden="true">
        <div class="card-07__media-shape"></div>
        <div class="card-07__media-glow"></div>
        <span class="card-07__rank">#1</span>
        <span class="card-07__reading-time">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          4 min
        </span>
      </div>
      <div class="card-07__body">
        <div class="card-07__tags">
          <span class="card-07__eye">Product Design</span>
          <span class="card-07__editors">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            EDITOR'S PICK
          </span>
        </div>
        <h3 class="card-07__title">The Case Against Perfect Loading States</h3>
        <p class="card-07__desc">Skeleton screens promise smoothness but often teach users to distrust the interface. A quieter approach ships faster and reads more honest.</p>
        <div class="card-07__author-row">
          <span class="card-07__author-avatar" aria-hidden="true">EK</span>
          <div class="card-07__author">
            <span class="card-07__author-name">
              Emil Kowalski
              <svg class="card-07__author-verified" role="img" aria-label="Verified" width="11" height="11" viewBox="0 0 24 24" fill="none">
                <path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#3b82f6"/>
                <path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
            <time class="card-07__author-date" datetime="2026-07-05">Jul 5 · 42k reads</time>
          </div>
          <div class="card-07__actions">
            <button type="button" class="card-07__action" aria-label="Play audio version">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
            </button>
            <button type="button" class="card-07__action" aria-label="Save article">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
            </button>
          </div>
        </div>
      </div>
    </article>

    <article class="card-07__card">
      <div class="card-07__media card-07__media--2" aria-hidden="true">
        <img class="card-07__img" src="https://images.unsplash.com/photo-1558655146-9f40138edfeb?w=600&q=80&auto=format&fit=crop" alt="CSS code" loading="lazy" decoding="async">
        <div class="card-07__media-shade"></div>
        <span class="card-07__rank">#2</span>
        <span class="card-07__reading-time">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          8 min
        </span>
      </div>
      <div class="card-07__body">
        <div class="card-07__tags">
          <span class="card-07__eye">CSS</span>
          <span class="card-07__delta">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 15 12 9 18 15"/></svg>
            +12%
          </span>
        </div>
        <h3 class="card-07__title">Container Queries Are Finally Ready</h3>
        <p class="card-07__desc">The most-requested CSS feature landed everywhere. Here's what changes about the way we think about responsive design.</p>
        <div class="card-07__author-row">
          <span class="card-07__author-avatar card-07__author-avatar--2" aria-hidden="true">JC</span>
          <div class="card-07__author">
            <span class="card-07__author-name">Josh Comeau</span>
            <time class="card-07__author-date" datetime="2026-07-02">Jul 2 · 28k reads</time>
          </div>
          <div class="card-07__actions">
            <button type="button" class="card-07__action" aria-label="Save article">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
            </button>
          </div>
        </div>
      </div>
    </article>

    <article class="card-07__card">
      <div class="card-07__media card-07__media--3" aria-hidden="true">
        <img class="card-07__img" src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&q=80&auto=format&fit=crop" alt="Server infrastructure" loading="lazy" decoding="async">
        <div class="card-07__media-shade"></div>
        <span class="card-07__rank">#3</span>
        <span class="card-07__reading-time">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          6 min
        </span>
      </div>
      <div class="card-07__body">
        <div class="card-07__tags">
          <span class="card-07__eye">AI · Engineering</span>
          <span class="card-07__new">NEW</span>
        </div>
        <h3 class="card-07__title">Why Local-First is the Future of Web Apps</h3>
        <p class="card-07__desc">Sync engines, CRDTs, and the return of desktop-quality speed. A new class of tools is finally making it practical.</p>
        <div class="card-07__author-row">
          <span class="card-07__author-avatar card-07__author-avatar--3" aria-hidden="true">RF</span>
          <div class="card-07__author">
            <span class="card-07__author-name">Rauno Freiberg</span>
            <time class="card-07__author-date" datetime="2026-07-08">Today · 3.2k reads</time>
          </div>
          <div class="card-07__actions">
            <button type="button" class="card-07__action" aria-label="Save article">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
            </button>
          </div>
        </div>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
.card-07 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 20%, rgba(139, 92, 246, 0.05) 0%, transparent 50%), radial-gradient(ellipse at 80% 80%, rgba(236, 72, 153, 0.04) 0%, transparent 50%), #faf7f2;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #7c3aed;
}

.card-07 *,
.card-07 *::before,
.card-07 *::after {
  box-sizing: border-box;
}

.card-07__stack {
  width: 100%;
  max-width: 640px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
/* ── stack head ── */

.card-07__stack-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 4px;
  padding: 0 4px;
}

.card-07__stack-title {
  display: flex;
  align-items: center;
  gap: 10px;
}

.card-07__stack-emoji {
  font-size: 22px;
  filter: drop-shadow(0 2px 3px rgba(139, 92, 246, 0.25));
}

.card-07__stack-h {
  font-size: 15px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0 0 1px;
  letter-spacing: -0.02em;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-07__stack-sub {
  font-size: 10.5px;
  color: #9ca3af;
  margin: 0;
}

.card-07__stack-filter {
  display: inline-flex;
  padding: 3px;
  background: #ede8dc;
  border: 1px solid rgba(0, 0, 0, 0.04);
  border-radius: 999px;
}

.card-07__stack-btn {
  min-height: 24px;
  padding: 3px 10px;
  border: 0;
  border-radius: 999px;
  background: transparent;
  color: #6b6b7c;
  font: 700 10.5px 'Inter', sans-serif;
  cursor: pointer;
  letter-spacing: -0.005em;
  transition: color 0.18s, background 0.18s;
}

.card-07__stack-btn--active {
  background: #fff;
  color: #1a1a1a;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06), 0 0 0 1px rgba(0, 0, 0, 0.03);
}

.card-07__stack-btn:hover {
  color: #1a1a1a;
}

.card-07__stack-btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* ── article cards ── */

.card-07__card {
  display: grid;
  grid-template-columns: 132px 1fr;
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 12px 30px -18px rgba(80, 40, 80, 0.15), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
  transition: transform 0.35s ease, box-shadow 0.35s, border-color 0.35s;
}

.card-07__card:hover {
  transform: translateY(-2px);
  border-color: rgba(124, 58, 237, 0.2);
  box-shadow: 0 24px 42px -18px rgba(80, 40, 80, 0.2), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
}

.card-07__card--featured {
  border: 1px solid rgba(124, 58, 237, 0.16);
  background: linear-gradient(90deg, rgba(124, 58, 237, 0.03) 0%, transparent 40%), #fff;
}
/* ── media panel ── */

.card-07__media {
  position: relative;
  overflow: hidden;
  background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.15) 0%, transparent 45%), linear-gradient(135deg, #4c1d95 0%, #7c3aed 55%, #a855f7 100%);
}

.card-07__media--2 {
  background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.15) 0%, transparent 45%), linear-gradient(135deg, #075985 0%, #0891b2 55%, #22d3ee 100%);
}

.card-07__media--3 {
  background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.15) 0%, transparent 45%), linear-gradient(135deg, #7c2d12 0%, #dc2626 55%, #f59e0b 100%);
}

.card-07__media-shape {
  position: absolute;
  inset: 0;
  background: conic-gradient(from 130deg at 65% 40%, transparent 0deg, rgba(255, 255, 255, 0.25) 60deg, transparent 130deg), radial-gradient(circle at 75% 75%, rgba(236, 72, 153, 0.5) 0%, transparent 55%);
}

.card-07__media-shape--2 {
  background: conic-gradient(from 100deg at 40% 60%, transparent 0deg, rgba(255, 255, 255, 0.2) 60deg, transparent 130deg), radial-gradient(circle at 75% 30%, rgba(52, 211, 153, 0.4) 0%, transparent 55%);
}

.card-07__media-shape--3 {
  background: conic-gradient(from 200deg at 55% 55%, transparent 0deg, rgba(255, 255, 255, 0.2) 60deg, transparent 130deg), radial-gradient(circle at 25% 75%, rgba(251, 191, 36, 0.45) 0%, transparent 55%);
}

.card-07__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.35s;
}

.card-07__card:hover .card-07__img {
  transform: scale(1.04);
}

.card-07__media-shade {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.35) 100%);
  pointer-events: none;
}

.card-07__media-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%;
  height: 80%;
  background: radial-gradient(ellipse, rgba(255, 255, 255, 0.14), transparent 65%);
  pointer-events: none;
}
/* rank badge */

.card-07__rank {
  position: absolute;
  top: 8px;
  left: 8px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 800;
  color: #fff;
  padding: 2px 7px;
  background: rgba(0, 0, 0, 0.48);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 5px;
  letter-spacing: 0.02em;
}

.card-07__reading-time {
  position: absolute;
  bottom: 8px;
  right: 8px;
  display: inline-flex;
  align-items: center;
  gap: 3px;
  padding: 2px 6px;
  background: rgba(0, 0, 0, 0.48);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  color: #fff;
  font-size: 9.5px;
  font-weight: 700;
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 5px;
  letter-spacing: 0.01em;
}
/* ── body ── */

.card-07__body {
  padding: 14px 16px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.card-07__tags {
  display: flex;
  align-items: center;
  gap: 6px;
}

.card-07__eye {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #4338ca;
  padding: 2px 7px;
  background: rgba(124, 58, 237, 0.08);
  border: 1px solid rgba(124, 58, 237, 0.14);
  border-radius: 999px;
  text-transform: uppercase;
}

.card-07__editors {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.12em;
  color: #a16207;
  padding: 2px 7px;
  background: linear-gradient(180deg, #fef3c7 0%, #fde68a 100%);
  border: 1px solid rgba(146, 64, 14, 0.18);
  border-radius: 999px;
  box-shadow: 0 1px 3px rgba(245, 158, 11, 0.2);
  text-transform: uppercase;
}

.card-07__delta {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 800;
  color: #059669;
  padding: 2px 6px;
  background: rgba(52, 211, 153, 0.12);
  border: 1px solid rgba(52, 211, 153, 0.22);
  border-radius: 999px;
}

.card-07__new {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #dc2626;
  padding: 2px 7px;
  background: rgba(220, 38, 38, 0.08);
  border: 1px solid rgba(220, 38, 38, 0.22);
  border-radius: 999px;
}

.card-07__title {
  font-size: 15px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: -0.02em;
  line-height: 1.3;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-07__desc {
  font-size: 12px;
  color: #6b6b7c;
  margin: 0;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
/* ── author row ── */

.card-07__author-row {
  display: grid;
  grid-template-columns: 26px 1fr auto;
  gap: 8px;
  align-items: center;
  margin-top: 6px;
  padding-top: 8px;
  border-top: 1px dashed rgba(0, 0, 0, 0.08);
}

.card-07__author-avatar {
  width: 26px;
  height: 26px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: linear-gradient(135deg, #a5b4fc, #7c3aed);
  color: #fff;
  font-size: 10px;
  font-weight: 800;
  border: 1.5px solid #fff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
  letter-spacing: -0.01em;
}

.card-07__author-avatar--2 {
  background: linear-gradient(135deg, #67e8f9, #0891b2);
}

.card-07__author-avatar--3 {
  background: linear-gradient(135deg, #fdba74, #ea580c);
}

.card-07__author {
  display: flex;
  flex-direction: column;
  gap: 0;
  min-width: 0;
}

.card-07__author-name {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 11.5px;
  font-weight: 700;
  color: #1a1a1a;
  letter-spacing: -0.005em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card-07__author-verified {
  flex-shrink: 0;
}

.card-07__author-date {
  font-size: 10px;
  color: #9ca3af;
  letter-spacing: -0.005em;
}

.card-07__actions {
  display: flex;
  gap: 4px;
}

.card-07__action {
  width: 24px;
  height: 24px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 6px;
  color: #6b6b7c;
  cursor: pointer;
  transition: color 0.18s, background 0.18s, border-color 0.18s;
}

.card-07__action:hover {
  color: #7c3aed;
  background: rgba(124, 58, 237, 0.06);
  border-color: rgba(124, 58, 237, 0.2);
}

.card-07__action:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* ── mobile stack ── */

@media (max-width: 600px) {
  .card-07__card {
    grid-template-columns: 1fr;
  }

  .card-07__media {
    min-height: 120px;
  }

  .card-07__stack-head {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-07__card,
    .card-07__stack-btn,
    .card-07__action {
    transition: none;
  }

  .card-07__card:hover {
    transform: none;
  }
}
```
