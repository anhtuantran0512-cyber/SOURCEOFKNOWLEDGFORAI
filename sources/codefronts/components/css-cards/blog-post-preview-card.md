---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/blog-post-preview-card/"
title: "Blog Post Preview Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Blog preview tile with 16:9 cosmic thumbnail, category chip, author + date meta, and a \"Read more →\" link whose arrow slides on hover."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blog Post Preview Card
Source: https://codefronts.com/components/css-cards/blog-post-preview-card/

Blog preview tile with 16:9 cosmic thumbnail, category chip, author + date meta, and a "Read more →" link whose arrow slides on hover.
## HTML
```html
<section class="card-06">
  <div class="card-06__grid">
    <header class="card-06__head">
      <div class="card-06__title-row">
        <span class="card-06__eyebrow">
          <span class="card-06__eyebrow-dot" aria-hidden="true"></span>
          THE JOURNAL
        </span>
        <h3 class="card-06__stack-h">Latest posts</h3>
      </div>
      <a href="#archive" class="card-06__archive">
        Archive
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </header>

    <article class="card-06__card card-06__card--hero">
      <div class="card-06__thumb">
        <img class="card-06__img" src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1200&q=80&auto=format&fit=crop" alt="CSS code on editor" loading="lazy" decoding="async">
        <div class="card-06__thumb-shade" aria-hidden="true"></div>
        <span class="card-06__badge">FEATURED</span>
        <span class="card-06__reading-time">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          6 min
        </span>
      </div>
      <div class="card-06__body">
        <span class="card-06__chip">Engineering</span>
        <h3 class="card-06__title">Why Container Queries Change Everything About Responsive Design</h3>
        <p class="card-06__desc">The most-requested CSS feature is finally shipping in every browser. Here's what changes about the way we think.</p>
        <div class="card-06__meta">
          <span class="card-06__avatar" aria-hidden="true">AC</span>
          <div class="card-06__meta-text">
            <span class="card-06__author-row">
              <span class="card-06__author">Alex Chen</span>
              <svg class="card-06__verified" role="img" aria-label="Verified" width="11" height="11" viewBox="0 0 24 24" fill="none"><path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#3b82f6"/><path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <span class="card-06__meta-info">
              <time datetime="2026-07-08">Jul 8</time>
              <span class="card-06__dot" aria-hidden="true">·</span>
              42k reads
            </span>
          </div>
          <button type="button" class="card-06__save" aria-label="Save article">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
          </button>
        </div>
      </div>
    </article>

    <div class="card-06__row">
      <article class="card-06__card card-06__card--sm">
        <div class="card-06__thumb card-06__thumb--sm">
          <img class="card-06__img" src="https://images.unsplash.com/photo-1558655146-9f40138edfeb?w=600&q=80&auto=format&fit=crop" alt="Design workspace" loading="lazy" decoding="async">
          <span class="card-06__reading-time card-06__reading-time--sm">4 min</span>
        </div>
        <div class="card-06__body card-06__body--sm">
          <span class="card-06__chip">Design</span>
          <h4 class="card-06__title-sm">The Case Against Perfect Loading States</h4>
          <div class="card-06__meta-sm">
            <span class="card-06__avatar card-06__avatar--sm card-06__avatar--2" aria-hidden="true">EK</span>
            <span class="card-06__author-sm">Emil Kowalski</span>
            <span class="card-06__dot" aria-hidden="true">·</span>
            <time datetime="2026-07-05">Jul 5</time>
          </div>
        </div>
      </article>

      <article class="card-06__card card-06__card--sm">
        <div class="card-06__thumb card-06__thumb--sm">
          <img class="card-06__img" src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&q=80&auto=format&fit=crop" alt="Server infrastructure" loading="lazy" decoding="async">
          <span class="card-06__reading-time card-06__reading-time--sm">8 min</span>
          <span class="card-06__badge card-06__badge--new">NEW</span>
        </div>
        <div class="card-06__body card-06__body--sm">
          <span class="card-06__chip">Infrastructure</span>
          <h4 class="card-06__title-sm">Why Local-First is the Future of Web Apps</h4>
          <div class="card-06__meta-sm">
            <span class="card-06__avatar card-06__avatar--sm card-06__avatar--3" aria-hidden="true">RF</span>
            <span class="card-06__author-sm">Rauno Freiberg</span>
            <span class="card-06__dot" aria-hidden="true">·</span>
            <time datetime="2026-07-08">Today</time>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.card-06 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 20%, rgba(99, 102, 241, 0.05) 0%, transparent 50%), radial-gradient(ellipse at 80% 80%, rgba(236, 72, 153, 0.04) 0%, transparent 50%), #f5f4f0;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #6366f1;
}

.card-06 *,
.card-06 *::before,
.card-06 *::after {
  box-sizing: border-box;
}

.card-06__grid {
  width: 100%;
  max-width: 720px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 14px;
}
/* ── head ── */

.card-06__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 0 4px;
}

.card-06__title-row {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.card-06__eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.16em;
  color: #6366f1;
}

.card-06__eyebrow-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #ec4899;
  box-shadow: 0 0 8px rgba(236, 72, 153, 0.5);
  animation: card-06-pulse 2s ease-in-out infinite;
}

.card-06__stack-h {
  font-size: 20px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: -0.025em;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-06__archive {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  font-weight: 700;
  color: #4b4b57;
  text-decoration: none;
  padding: 6px 10px;
  border-radius: 8px;
  transition: color 0.18s, background 0.18s;
}

.card-06__archive:hover {
  color: #1a1a1a;
  background: rgba(0, 0, 0, 0.04);
}

.card-06__archive:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* ── hero card (full-width) ── */

.card-06__card {
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 12px 30px -18px rgba(80, 40, 100, 0.15), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
  transition: transform 0.35s ease, box-shadow 0.35s, border-color 0.35s;
}

.card-06__card:hover {
  transform: translateY(-3px);
  border-color: rgba(99, 102, 241, 0.2);
  box-shadow: 0 26px 44px -18px rgba(80, 40, 100, 0.22), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
}

.card-06__card--hero {
  display: grid;
  grid-template-columns: 240px 1fr;
}
/* ── thumb ── */

.card-06__thumb {
  position: relative;
  overflow: hidden;
  background: #1a1a1a;
}

.card-06__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease;
}

.card-06__card:hover .card-06__img {
  transform: scale(1.06);
}

.card-06__thumb-shade {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 0%, rgba(0, 0, 0, 0.35) 100%);
  pointer-events: none;
}

.card-06__badge {
  position: absolute;
  top: 10px;
  left: 10px;
  padding: 3px 8px;
  background: linear-gradient(180deg, #fef3c7 0%, #fde68a 100%);
  color: #78350f;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.14em;
  border-radius: 5px;
  border: 1px solid rgba(146, 64, 14, 0.2);
  box-shadow: 0 2px 5px rgba(245, 158, 11, 0.25);
}

.card-06__badge--new {
  background: rgba(220, 38, 38, 0.9);
  color: #fff;
  border-color: rgba(255, 255, 255, 0.14);
  box-shadow: 0 2px 5px rgba(220, 38, 38, 0.3);
}

.card-06__reading-time {
  position: absolute;
  bottom: 10px;
  right: 10px;
  display: inline-flex;
  align-items: center;
  gap: 3px;
  padding: 3px 7px;
  background: rgba(0, 0, 0, 0.55);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  color: #fff;
  font-size: 10px;
  font-weight: 700;
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 5px;
  letter-spacing: 0.02em;
}

.card-06__reading-time--sm {
  padding: 2px 6px;
  font-size: 9px;
}
/* ── body ── */

.card-06__body {
  padding: 20px 24px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  justify-content: center;
}

.card-06__chip {
  align-self: flex-start;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #4338ca;
  padding: 3px 9px;
  background: rgba(99, 102, 241, 0.08);
  border: 1px solid rgba(99, 102, 241, 0.16);
  border-radius: 999px;
  text-transform: uppercase;
}

.card-06__title {
  font-size: 17px;
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

.card-06__desc {
  font-size: 12.5px;
  color: #6b6b7c;
  margin: 0;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
/* ── meta ── */

.card-06__meta {
  display: grid;
  grid-template-columns: 30px 1fr auto;
  gap: 8px;
  align-items: center;
  margin-top: 6px;
  padding-top: 10px;
  border-top: 1px dashed rgba(0, 0, 0, 0.08);
}

.card-06__avatar {
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: linear-gradient(135deg, #6366f1, #ec4899);
  color: #fff;
  font-size: 10.5px;
  font-weight: 800;
  border: 1.5px solid #fff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
  letter-spacing: -0.01em;
}

.card-06__avatar--2 {
  background: linear-gradient(135deg, #67e8f9, #0891b2);
}

.card-06__avatar--3 {
  background: linear-gradient(135deg, #fdba74, #ea580c);
}

.card-06__meta-text {
  display: flex;
  flex-direction: column;
  gap: 0;
  min-width: 0;
}

.card-06__author-row {
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.card-06__author {
  font-size: 12px;
  font-weight: 700;
  color: #1a1a1a;
  letter-spacing: -0.005em;
}

.card-06__verified {
  flex-shrink: 0;
}

.card-06__meta-info {
  font-size: 10.5px;
  color: #9ca3af;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-variant-numeric: tabular-nums;
}

.card-06__dot {
  color: #cbd5e1;
}

.card-06__save {
  width: 30px;
  height: 30px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 8px;
  color: #6b6b7c;
  cursor: pointer;
  transition: color 0.18s, background 0.18s, border-color 0.18s, transform 0.18s;
}

.card-06__save:hover {
  color: #6366f1;
  background: rgba(99, 102, 241, 0.06);
  border-color: rgba(99, 102, 241, 0.24);
  transform: translateY(-1px);
}

.card-06__save:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* ── row of two small cards ── */

.card-06__row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.card-06__card--sm {
  display: flex;
  flex-direction: column;
}

.card-06__thumb--sm {
  height: 130px;
}

.card-06__body--sm {
  padding: 12px 14px;
  gap: 6px;
}

.card-06__title-sm {
  font-size: 13px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 2px 0 0;
  letter-spacing: -0.015em;
  line-height: 1.3;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-06__meta-sm {
  display: flex;
  align-items: center;
  gap: 5px;
  margin-top: 8px;
  padding-top: 8px;
  border-top: 1px dashed rgba(0, 0, 0, 0.06);
  font-size: 10.5px;
  color: #9ca3af;
}

.card-06__avatar--sm {
  width: 22px;
  height: 22px;
  font-size: 9px;
  border-width: 1.5px;
}

.card-06__author-sm {
  font-size: 11px;
  font-weight: 700;
  color: #1a1a1a;
  letter-spacing: -0.005em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
/* mobile */

@media (max-width: 600px) {
  .card-06__card--hero {
    grid-template-columns: 1fr;
  }

  .card-06__card--hero .card-06__thumb {
    min-height: 160px;
  }

  .card-06__row {
    grid-template-columns: 1fr;
  }

  .card-06__head {
    flex-direction: column;
    align-items: flex-start;
  }
}

@keyframes card-06-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.4);
    opacity: 0.7;
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-06__card,
    .card-06__img,
    .card-06__save,
    .card-06__archive {
    transition: none;
  }

  .card-06__card:hover {
    transform: none;
  }

  .card-06__card:hover .card-06__img {
    transform: none;
  }

  .card-06__eyebrow-dot {
    animation: none;
  }
}
```
