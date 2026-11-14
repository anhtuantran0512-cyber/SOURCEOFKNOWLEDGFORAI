---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/notification-bell-badge-pulse/"
title: "Notification Bell Badge Pulse"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "A business SaaS app header with a bell icon and an unread-count badge that pulses to draw the eye — Notion/Linear/Superhuman header convention."
has_js: "false"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Notification Bell Badge Pulse
Source: https://codefronts.com/motion/css-pulse-animation/notification-bell-badge-pulse/

A business SaaS app header with a bell icon and an unread-count badge that pulses to draw the eye — Notion/Linear/Superhuman header convention. Clean white surface (#ffffff) with slate ink (#0f172a) and a red badge (#ef4444). Only the badge itself pulses (subtle scale + box-shadow ring), the bell stays still. The pattern signals "new alert" without being distracting because the pulse animates the smallest UI element on the page — an 18px circle — not the entire header.
## HTML
```html
<div class="pl-05">
  <div class="pl-05__page">
    <header class="pl-05__header">
      <div class="pl-05__brand">
        <span class="pl-05__logo" aria-hidden="true">◆</span>
        <span class="pl-05__workspace">Northlight</span>
        <span class="pl-05__divider" aria-hidden="true">/</span>
        <span class="pl-05__location">Design system</span>
      </div>
      <nav class="pl-05__nav" aria-label="Primary">
        <a href="#" class="pl-05__link">Docs</a>
        <a href="#" class="pl-05__link pl-05__link--sel">Projects</a>
        <a href="#" class="pl-05__link">Team</a>
      </nav>
      <div class="pl-05__actions">
        <button class="pl-05__icon" aria-label="Search">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <circle cx="11" cy="11" r="8"/>
            <path d="M21 21l-4.35-4.35"/>
          </svg>
        </button>
        <button class="pl-05__icon pl-05__bell" aria-label="3 unread notifications">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/>
            <path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>
          </svg>
          <span class="pl-05__badge" aria-hidden="true">3</span>
        </button>
        <button class="pl-05__avatar" aria-label="Account">A</button>
      </div>
    </header>
    <section class="pl-05__content">
      <p class="pl-05__eyebrow">Recent</p>
      <h2 class="pl-05__title">Component library</h2>
      <div class="pl-05__cards">
        <div class="pl-05__card"><span>Buttons</span><em>42</em></div>
        <div class="pl-05__card"><span>Cards</span><em>28</em></div>
        <div class="pl-05__card"><span>Forms</span><em>16</em></div>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
.pl-05 {
  --page-bg: #f8fafc;
  --surface: #ffffff;
  --ink: #0f172a;
  --sub: #64748b;
  --brand: #7c3aed;
  --accent: #ef4444;
  --line: #e2e8f0;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: grid;
  place-items: start center;
  padding: 32px;
  background: var(--page-bg);
  color: var(--ink);
}

.pl-05 *,
.pl-05 *::before,
.pl-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-05 ::selection {
  background: var(--brand);
  color: #fff;
}

.pl-05__page {
  width: min(760px,100%);
  border-radius: 14px;
  overflow: hidden;
  background: var(--surface);
  box-shadow: 0 20px 40px -20px rgba(15,23,42,.15),0 4px 12px -6px rgba(15,23,42,.08);
}

.pl-05__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 14px 20px;
  border-bottom: 1px solid var(--line);
}

.pl-05__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: .85rem;
  font-weight: 600;
}

.pl-05__logo {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  border-radius: 6px;
  background: linear-gradient(135deg,var(--brand),#a78bfa);
  color: #fff;
  font-size: .7rem;
}

.pl-05__workspace {
  color: var(--ink);
}

.pl-05__divider {
  color: var(--sub);
  font-weight: 400;
}

.pl-05__location {
  color: var(--sub);
  font-weight: 500;
}

.pl-05__nav {
  display: flex;
  gap: 6px;
}

.pl-05__link {
  padding: 6px 12px;
  border-radius: 6px;
  color: var(--sub);
  text-decoration: none;
  font-size: .82rem;
  font-weight: 600;
  transition: background .15s ease,color .15s ease;
}

.pl-05__link:hover {
  background: #f1f5f9;
  color: var(--ink);
}

.pl-05__link--sel {
  background: #f1f5f9;
  color: var(--ink);
}

.pl-05__actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.pl-05__icon {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: var(--sub);
  cursor: pointer;
  transition: background .15s ease,color .15s ease,transform .15s ease;
}

.pl-05__icon:hover {
  background: #f1f5f9;
  color: var(--ink);
  transform: translateY(-1px);
}

.pl-05__icon:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 2px;
}
/* Bell badge — dual animation: badge scale + box-shadow ring */

.pl-05__badge {
  position: absolute;
  top: -4px;
  right: -4px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 18px;
  height: 18px;
  padding: 0 5px;
  border-radius: 9px;
  background: var(--accent);
  color: #fff;
  font-size: .65rem;
  font-weight: 800;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  border: 2px solid var(--surface);
  animation: pl-05-badge 2s ease-in-out infinite;
  transform-origin: center;
}

.pl-05__badge::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: 9px;
  pointer-events: none;
  animation: pl-05-ring 2s ease-out infinite;
}

@keyframes pl-05-badge {
  0%,
    100% {
    transform: scale(1);
  }

  15% {
    transform: scale(1.15);
  }

  30% {
    transform: scale(1);
  }
}

@keyframes pl-05-ring {
  0% {
    box-shadow: 0 0 0 0 rgba(239,68,68,.55);
  }

  50% {
    box-shadow: 0 0 0 8px rgba(239,68,68,0);
  }

  100% {
    box-shadow: 0 0 0 8px rgba(239,68,68,0);
  }
}

.pl-05__avatar {
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 50%;
  background: linear-gradient(135deg,#f472b6,#ec4899);
  color: #fff;
  font-family: inherit;
  font-size: .82rem;
  font-weight: 700;
  cursor: pointer;
  transition: transform .15s ease;
}

.pl-05__avatar:hover {
  transform: translateY(-1px);
}

.pl-05__avatar:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 2px;
}

.pl-05__content {
  padding: 24px 20px 22px;
}

.pl-05__eyebrow {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sub);
  margin-bottom: 4px;
}

.pl-05__title {
  font-size: 1.35rem;
  font-weight: 800;
  letter-spacing: -.02em;
  margin-bottom: 14px;
}

.pl-05__cards {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 10px;
}

.pl-05__card {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 12px 14px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: #fafbfc;
  font-size: .82rem;
  font-weight: 600;
}

.pl-05__card em {
  color: var(--brand);
  font-style: normal;
  font-weight: 800;
}

@media (prefers-reduced-motion: reduce) {
  .pl-05__badge,
    .pl-05__badge::after {
    animation: none!important;
  }

  .pl-05__badge {
    transform: none!important;
  }
}
```
