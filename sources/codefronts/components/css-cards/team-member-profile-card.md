---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/team-member-profile-card/"
title: "Team Member Profile Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Centered team-profile tile with 72px gradient avatar, name, role, one-line bio, and a row of 44×44 social icon links (GitHub, LinkedIn, X)."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Team Member Profile Card
Source: https://codefronts.com/components/css-cards/team-member-profile-card/

Centered team-profile tile with 72px gradient avatar, name, role, one-line bio, and a row of 44×44 social icon links (GitHub, LinkedIn, X).
## HTML
```html
<section class="card-11">
  <article class="card-11__card">
    <div class="card-11__cover" aria-hidden="true">
      <div class="card-11__cover-mesh"></div>
      <div class="card-11__cover-grid"></div>
    </div>
    <button type="button" class="card-11__more" aria-label="More options">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/></svg>
    </button>
    <div class="card-11__avatar-wrap">
      <div class="card-11__avatar" aria-hidden="true">
        <span class="card-11__avatar-inner">AC</span>
      </div>
      <span class="card-11__status" aria-label="Available for work">
        <span class="card-11__status-dot" aria-hidden="true"></span>
      </span>
    </div>
    <div class="card-11__body">
      <div class="card-11__name-row">
        <h3 class="card-11__name">Alex Chen</h3>
        <svg class="card-11__verified" aria-label="Verified" role="img" width="15" height="15" viewBox="0 0 24 24" fill="none">
          <path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#6366f1"/>
          <path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      <p class="card-11__role">
        Founding Engineer at <span class="card-11__company">Anthropic</span>
      </p>
      <p class="card-11__bio">Building the tools I wish I had. Ex-Vercel, ex-Stripe.</p>
      <ul class="card-11__meta" aria-label="Profile info">
        <li>
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          San Francisco
        </li>
        <li>
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          GMT−8
        </li>
      </ul>
      <dl class="card-11__stats">
        <div class="card-11__stat">
          <dt>Following</dt>
          <dd>1,284</dd>
        </div>
        <div class="card-11__stat">
          <dt>Followers</dt>
          <dd>12.4k</dd>
        </div>
        <div class="card-11__stat">
          <dt>Repos</dt>
          <dd>47</dd>
        </div>
      </dl>
    </div>
    <footer class="card-11__foot">
      <button type="button" class="card-11__cta">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 8v8M8 12h8"/></svg>
        Follow
      </button>
      <div class="card-11__social" aria-label="Social links">
        <a class="card-11__icon" href="#github" aria-label="GitHub">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .3a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.4-4-1.4-.6-1.4-1.4-1.8-1.4-1.8-1.1-.7.1-.7.1-.7 1.2 0 1.9 1.2 1.9 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-6 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.6.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.6.2 2.9.1 3.2.7.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .3"/></svg>
        </a>
        <a class="card-11__icon" href="#linkedin" aria-label="LinkedIn">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.5 2h-17A1.5 1.5 0 0 0 2 3.5v17A1.5 1.5 0 0 0 3.5 22h17a1.5 1.5 0 0 0 1.5-1.5v-17A1.5 1.5 0 0 0 20.5 2zM8 19H5v-9h3v9zM6.5 8.25A1.75 1.75 0 1 1 8.3 6.5a1.78 1.78 0 0 1-1.8 1.75zM19 19h-3v-4.7c0-1.1 0-2.5-1.6-2.5s-1.8 1.2-1.8 2.4V19h-3v-9h2.9v1.2a3.1 3.1 0 0 1 2.8-1.5c3 0 3.6 2 3.6 4.5V19z"/></svg>
        </a>
        <a class="card-11__icon" href="#x" aria-label="X">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2H21l-6.52 7.45L22 22h-6.828l-4.79-6.213L4.83 22H2.07l6.97-7.965L1.5 2h6.99l4.33 5.688L18.244 2zm-2.395 18.4h1.888L7.29 3.6H5.264l10.585 16.8z"/></svg>
        </a>
      </div>
    </footer>
  </article>
</section>
```
## CSS
```css
.card-11 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 20%, rgba(139, 92, 246, 0.06) 0%, transparent 50%), radial-gradient(ellipse at 80% 80%, rgba(236, 72, 153, 0.04) 0%, transparent 50%), #f5f4f0;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #6366f1;
  --accent: #6366f1;
  --accent-2: #ec4899;
}

.card-11 *,
.card-11 *::before,
.card-11 *::after {
  box-sizing: border-box;
}

.card-11__card {
  position: relative;
  width: 100%;
  max-width: 340px;
  margin: 0 auto;
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 22px;
  overflow: hidden;
  box-shadow: 0 30px 60px -30px rgba(60, 40, 100, 0.18), 0 0 0 1px rgba(255, 255, 255, 0.5) inset, 0 -1px 0 rgba(0, 0, 0, 0.02) inset;
  transition: transform 0.35s ease, box-shadow 0.35s;
}

.card-11__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 40px 80px -30px rgba(60, 40, 100, 0.28), 0 0 0 1px rgba(255, 255, 255, 0.5) inset, 0 -1px 0 rgba(0, 0, 0, 0.02) inset;
}
/* ── cover strip with mesh gradient + grid pattern ── */

.card-11__cover {
  position: relative;
  height: 92px;
  background: linear-gradient(160deg, #a5b4fc 0%, #6366f1 45%, #ec4899 100%);
  overflow: hidden;
}

.card-11__cover-mesh {
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 20% 30%, rgba(255, 255, 255, 0.35) 0%, transparent 40%), radial-gradient(ellipse at 80% 70%, rgba(244, 114, 182, 0.4) 0%, transparent 45%), radial-gradient(circle at 55% 40%, rgba(139, 92, 246, 0.3) 0%, transparent 40%);
}

.card-11__cover-grid {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(255, 255, 255, 0.06) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 0.06) 1px, transparent 1px);
  background-size: 20px 20px;
  mask-image: linear-gradient(180deg, transparent 0%, black 40%, black 80%, transparent 100%);
  -webkit-mask-image: linear-gradient(180deg, transparent 0%, black 40%, black 80%, transparent 100%);
}
/* ── more button top-right ── */

.card-11__more {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 30px;
  height: 30px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.14);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 8px;
  color: #fff;
  cursor: pointer;
  z-index: 3;
  transition: background 0.18s, border-color 0.18s;
}

.card-11__more:hover {
  background: rgba(255, 255, 255, 0.24);
  border-color: rgba(255, 255, 255, 0.4);
}

.card-11__more:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* ── avatar overlapping the cover ── */

.card-11__avatar-wrap {
  position: relative;
  margin: -34px auto 0;
  width: 68px;
  height: 68px;
  z-index: 2;
}

.card-11__avatar {
  position: relative;
  width: 68px;
  height: 68px;
  border-radius: 50%;
  background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
  padding: 3px;
  box-shadow: 0 6px 18px rgba(99, 102, 241, 0.35);
}

.card-11__avatar-inner {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: linear-gradient(180deg, #f5f4fb 0%, #e4e4f0 100%);
  color: #4338ca;
  font-family: 'Inter', system-ui, sans-serif;
  font-size: 20px;
  font-weight: 800;
  letter-spacing: -0.01em;
  border: 3px solid #fff;
}

.card-11__status {
  position: absolute;
  bottom: 2px;
  right: 2px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
}

.card-11__status-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #34d399;
  box-shadow: 0 0 0 2px rgba(52, 211, 153, 0.32);
  animation: card-11-pulse 2.4s ease-in-out infinite;
}
/* ── body content ── */

.card-11__body {
  padding: 12px 22px 16px;
  text-align: center;
}

.card-11__name-row {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  margin-bottom: 4px;
}

.card-11__name {
  font-size: 19px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: -0.02em;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-11__verified {
  flex-shrink: 0;
}

.card-11__role {
  font-size: 12.5px;
  font-weight: 500;
  color: #4b5563;
  margin: 0 0 6px;
}

.card-11__company {
  color: #4338ca;
  font-weight: 700;
}

.card-11__bio {
  font-size: 12.5px;
  color: #6b6b7c;
  margin: 0 0 12px;
  line-height: 1.5;
}

.card-11__meta {
  display: inline-flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 6px 12px;
  list-style: none;
  padding: 0;
  margin: 0 0 14px;
}

.card-11__meta li {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 11px;
  font-weight: 500;
  color: #6b6b7c;
}

.card-11__meta svg {
  color: #9ca3af;
  flex-shrink: 0;
}
/* ── stat row ── */

.card-11__stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  margin: 0;
  padding: 12px 0;
  background: linear-gradient(180deg, #fafafd 0%, #f4f4fa 100%);
  border-top: 1px solid rgba(0, 0, 0, 0.05);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 12px;
  border: 1px solid rgba(0, 0, 0, 0.04);
  position: relative;
}

.card-11__stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  position: relative;
}

.card-11__stat + .card-11__stat::before {
  content: '';
  position: absolute;
  left: 0;
  top: 15%;
  bottom: 15%;
  width: 1px;
  background: rgba(0, 0, 0, 0.06);
}

.card-11__stat dt {
  font-size: 9.5px;
  font-weight: 600;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: #9ca3af;
  margin: 0;
}

.card-11__stat dd {
  font-size: 14px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: -0.01em;
  font-variant-numeric: tabular-nums;
}
/* ── footer with primary CTA + social row ── */

.card-11__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 14px 22px 18px;
}

.card-11__cta {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  min-height: 36px;
  padding: 8px 16px;
  border: 0;
  border-radius: 999px;
  background: linear-gradient(180deg, #1e1e2c 0%, #06070c 100%);
  color: #fff;
  font: inherit;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  letter-spacing: -0.01em;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2), 0 0 0 1px rgba(255, 255, 255, 0.12) inset, 0 -1px 0 rgba(255, 255, 255, 0.06) inset;
  transition: transform 0.18s, box-shadow 0.18s;
}

.card-11__cta:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.28), 0 0 0 1px rgba(255, 255, 255, 0.18) inset, 0 -1px 0 rgba(255, 255, 255, 0.08) inset;
}

.card-11__cta:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-11__social {
  display: flex;
  gap: 4px;
}

.card-11__icon {
  width: 34px;
  height: 34px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  background: transparent;
  border: 1px solid rgba(0, 0, 0, 0.06);
  color: #6b6b7c;
  text-decoration: none;
  transition: color 0.18s, background 0.18s, border-color 0.18s, transform 0.18s;
}

.card-11__icon:hover {
  color: var(--accent);
  background: rgba(99, 102, 241, 0.06);
  border-color: rgba(99, 102, 241, 0.24);
  transform: translateY(-1px);
}

.card-11__icon:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

@keyframes card-11-pulse {
  0%,
    100% {
    transform: scale(1);
    box-shadow: 0 0 0 2px rgba(52, 211, 153, 0.32);
  }

  50% {
    transform: scale(1.15);
    box-shadow: 0 0 0 4px rgba(52, 211, 153, 0.16);
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-11__card,
    .card-11__more,
    .card-11__cta,
    .card-11__icon {
    transition: none;
  }

  .card-11__card:hover {
    transform: none;
  }

  .card-11__cta:hover,
    .card-11__icon:hover {
    transform: none;
  }

  .card-11__status-dot {
    animation: none;
  }
}
```
