---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-step-progress-wizard-navbar/"
title: "CSS Step Progress Wizard Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Multi-step wizard header showing step numbers, titles, connector lines, and completion state in a horizontal flow."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Step Progress Wizard Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-step-progress-wizard-navbar/

Multi-step wizard header showing step numbers, titles, connector lines, and completion state in a horizontal flow.
## HTML
```html
<div class="nav-17">
  <div class="nav-17__top">
    <a href="#" class="nav-17__logo">Form<span>Flow</span></a>
    <a href="#" class="nav-17__help">💬 Need help?</a>
  </div>
  <div class="nav-17__steps">
    <div class="nav-17__step is-done">
      <div class="nav-17__step-content">
        <div class="nav-17__step-circle">✓</div>
        <div class="nav-17__step-info">
          <div class="nav-17__step-label">Step 1</div>
          <div class="nav-17__step-title">Account</div>
        </div>
      </div>
    </div>
    <div class="nav-17__connector"></div>
    <div class="nav-17__step is-done">
      <div class="nav-17__step-content">
        <div class="nav-17__step-circle">✓</div>
        <div class="nav-17__step-info">
          <div class="nav-17__step-label">Step 2</div>
          <div class="nav-17__step-title">Profile</div>
        </div>
      </div>
    </div>
    <div class="nav-17__connector"></div>
    <div class="nav-17__step is-active">
      <div class="nav-17__step-content">
        <div class="nav-17__step-circle">3</div>
        <div class="nav-17__step-info">
          <div class="nav-17__step-label">Step 3</div>
          <div class="nav-17__step-title">Payment</div>
        </div>
      </div>
    </div>
    <div class="nav-17__connector"></div>
    <div class="nav-17__step">
      <div class="nav-17__step-content">
        <div class="nav-17__step-circle">4</div>
        <div class="nav-17__step-info">
          <div class="nav-17__step-label">Step 4</div>
          <div class="nav-17__step-title">Review</div>
        </div>
      </div>
    </div>
    <div class="nav-17__connector"></div>
    <div class="nav-17__step">
      <div class="nav-17__step-content">
        <div class="nav-17__step-circle">5</div>
        <div class="nav-17__step-info">
          <div class="nav-17__step-label">Step 5</div>
          <div class="nav-17__step-title">Confirm</div>
        </div>
      </div>
    </div>
  </div>
  <div class="nav-17__summary">
    <span class="nav-17__summary-text">Step 3 of 5 — Payment details</span>
    <div class="nav-17__progress-bar-wrap">
      <div class="nav-17__progress-bar"></div>
    </div>
    <button class="nav-17__save">Save & exit</button>
  </div>
</div>
<div style="padding:3rem 2rem; max-width:600px; margin:0 auto;">
  <h1 style="font-size:2.2rem; font-weight:800; letter-spacing:-0.03em; margin-bottom:1rem; color:#1e2337;">Step Progress Wizard Navbar</h1>
  <p style="color:#8891a8; font-size:1.05rem; line-height:1.75;">Used for multi-step forms and checkout flows. Completed steps show a green checkmark, the active step is purple-filled, and connector lines animate to filled when the previous step is done. Built entirely with CSS.</p>
</div>
```
## CSS
```css
.nav-17,
.nav-17 *,
.nav-17 *::before,
.nav-17 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-17 {
  --bg: #fff;
  --border: #e5e8f0;
  --text: #1e2337;
  --muted: #8891a8;
  --accent: #5b4ef8;
  --done: #22c55e;
  --done-light: #f0fdf4;
  --accent-light: #f0eeff;
  font-family: 'Nunito Sans', sans-serif;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  box-shadow: 0 1px 4px rgba(0,0,0,0.05);
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-17__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 2rem;
  border-bottom: 1px solid var(--border);
}

.nav-17__logo {
  font-weight: 800;
  font-size: 1.1rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: -0.02em;
}

.nav-17__logo span {
  color: var(--accent);
}

.nav-17__help {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--muted);
  font-size: 0.875rem;
  font-weight: 600;
  text-decoration: none;
  transition: color 0.2s;
}

.nav-17__help:hover {
  color: var(--text);
}
/* Steps */

.nav-17__steps {
  display: flex;
  align-items: center;
  padding: 1rem 2rem;
  overflow-x: auto;
  scrollbar-width: none;
}

.nav-17__steps::-webkit-scrollbar {
  display: none;
}

.nav-17__step {
  display: flex;
  align-items: center;
  flex-shrink: 0;
}

.nav-17__step-content {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.4rem 0.75rem;
  border-radius: 10px;
  cursor: pointer;
  transition: background 0.15s;
}

.nav-17__step-content:hover {
  background: #f5f6fa;
}

.nav-17__step-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 800;
  flex-shrink: 0;
  transition: background 0.3s, border-color 0.3s;
  border: 2px solid var(--border);
  color: var(--muted);
  background: var(--bg);
}

.nav-17__step.is-done .nav-17__step-circle {
  background: var(--done);
  border-color: var(--done);
  color: #fff;
  font-size: 0.9rem;
}

.nav-17__step.is-active .nav-17__step-circle {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.nav-17__step-info {
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.nav-17__step-label {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--muted);
}

.nav-17__step.is-done .nav-17__step-label {
  color: var(--done);
}

.nav-17__step.is-active .nav-17__step-label {
  color: var(--accent);
}

.nav-17__step-title {
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--muted);
}

.nav-17__step.is-done .nav-17__step-title,
.nav-17__step.is-active .nav-17__step-title {
  color: var(--text);
}
/* Connector line */

.nav-17__connector {
  flex: 1;
  min-width: 2rem;
  max-width: 5rem;
  height: 2px;
  margin: 0 0.25rem;
  background: var(--border);
  position: relative;
  border-radius: 2px;
}

.nav-17__connector::after {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--done);
  border-radius: 2px;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.5s;
}

.nav-17__step.is-done + .nav-17__connector::after {
  transform: scaleX(1);
}
/* Progress summary */

.nav-17__summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.6rem 2rem;
  background: var(--accent-light);
  border-top: 1px solid rgba(91,78,248,0.1);
}

.nav-17__summary-text {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--accent);
}

.nav-17__progress-bar-wrap {
  flex: 1;
  max-width: 200px;
  height: 6px;
  background: rgba(91,78,248,0.15);
  border-radius: 3px;
  margin: 0 1rem;
}

.nav-17__progress-bar {
  height: 100%;
  border-radius: 3px;
  background: var(--accent);
  width: 40%;
  transition: width 0.5s;
}

.nav-17__save {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--muted);
  text-decoration: none;
  cursor: pointer;
  background: none;
  border: none;
  font-family: inherit;
  transition: color 0.2s;
}

.nav-17__save:hover {
  color: var(--text);
}

@media (max-width: 640px) {
  .nav-17__step-info {
    display: none;
  }

  .nav-17__connector {
    min-width: 1rem;
    max-width: 2rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-17__connector::after,
    .nav-17__progress-bar,
    .nav-17__step-circle {
    transition: none;
  }
}
```
