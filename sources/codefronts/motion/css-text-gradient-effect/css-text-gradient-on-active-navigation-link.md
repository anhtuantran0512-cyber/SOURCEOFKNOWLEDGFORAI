---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/css-text-gradient-on-active-navigation-link/"
title: "CSS Text Gradient on Active Navigation Link"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A full-page header with a clickable nav where the active page link renders a gradient colour with an animated underline indicator."
has_js: "true"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Gradient on Active Navigation Link
Source: https://codefronts.com/motion/css-text-gradient-effect/css-text-gradient-on-active-navigation-link/

A full-page header with a clickable nav where the active page link renders a gradient colour with an animated underline indicator.
## HTML
```html
<div class="tg-07">
  <div class="tg-07__wrapper">
    <header class="tg-07__header">
      <div class="tg-07__logo">⬡ Nexus</div>
      <nav class="tg-07__nav" role="navigation">
        <a href="#" class="tg-07__link">Dashboard</a>
        <a href="#" class="tg-07__link tg-07__link--active" aria-current="page">Analytics</a>
        <a href="#" class="tg-07__link">Projects</a>
        <a href="#" class="tg-07__link">Settings</a>
      </nav>
      <div class="tg-07__avatar">AK</div>
    </header>
    <main class="tg-07__content">
      <div class="tg-07__page-title">
        <h1>Analytics <span class="tg-07__grad">Overview</span></h1>
        <p>Your performance at a glance for the last 30 days.</p>
      </div>
      <div class="tg-07__kpis">
        <div class="tg-07__kpi"><span class="tg-07__kpi-val">$124K</span><span class="tg-07__kpi-lbl">Revenue</span></div>
        <div class="tg-07__kpi"><span class="tg-07__kpi-val">8,432</span><span class="tg-07__kpi-lbl">Sessions</span></div>
        <div class="tg-07__kpi"><span class="tg-07__kpi-val">3.4%</span><span class="tg-07__kpi-lbl">Conversion</span></div>
      </div>
      <p class="tg-07__hint">Click any nav item to see gradient active state</p>
    </main>
  </div>
</div>
```
## CSS
```css
.tg-07,
.tg-07 *,
.tg-07 *::before,
.tg-07 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-07 ::selection {
  background: #2563eb;
  color: #fff;
}

.tg-07 {
  --g-a: #3b82f6;
  --g-b: #8b5cf6;
  --bg: #f8fafc;
  --header-bg: #ffffff;
  --text: #0f172a;
  --muted: #64748b;
  --border: #e2e8f0;
  --active-bg: rgba(59,130,246,.08);
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
}

.tg-07__wrapper {
  overflow: hidden;
}

.tg-07__header {
  background: var(--header-bg);
  border-bottom: 1px solid var(--border);
  padding: 0 28px;
  height: 58px;
  display: flex;
  align-items: center;
  gap: 32px;
}

.tg-07__logo {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--text);
  letter-spacing: -.02em;
  flex-shrink: 0;
}

.tg-07__nav {
  display: flex;
  gap: 2px;
  flex: 1;
}

.tg-07__link {
  text-decoration: none;
  font-size: .875rem;
  font-weight: 500;
  color: var(--muted);
  padding: 6px 14px;
  border-radius: 7px;
  transition: color .2s, background .2s;
  position: relative;
}

.tg-07__link:hover {
  color: var(--text);
  background: rgba(0,0,0,.04);
}
/* Active state: gradient text + subtle bg tint + bottom indicator */

.tg-07__link--active {
  background: var(--active-bg);
  font-weight: 700;
}

.tg-07__link--active {
  background: linear-gradient(90deg, var(--g-a), var(--g-b));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  /* Re-apply bg separately — background-clip:text consumes background */
}
/* We need two backgrounds: tint + gradient for clip. Use ::after for the tint */

.tg-07__link--active::after {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--active-bg);
  border-radius: 7px;
  z-index: -1;
}
/* Underline indicator */

.tg-07__link--active::before {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 14px;
  right: 14px;
  height: 2px;
  background: linear-gradient(90deg, var(--g-a), var(--g-b));
  border-radius: 2px 2px 0 0;
}

.tg-07__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--g-a), var(--g-b));
  color: #fff;
  font-size: .75rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.tg-07__content {
  padding: 36px 28px;
}

.tg-07__page-title h1 {
  font-size: 1.75rem;
  font-weight: 800;
  color: var(--text);
  letter-spacing: -.03em;
  margin-bottom: 6px;
}

.tg-07__page-title p {
  color: var(--muted);
  font-size: .9rem;
  margin-bottom: 32px;
}

.tg-07__grad {
  background: linear-gradient(90deg, var(--g-a), var(--g-b));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.tg-07__kpis {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  margin-bottom: 28px;
}

.tg-07__kpi {
  background: #fff;
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px 24px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 120px;
}

.tg-07__kpi-val {
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--text);
}

.tg-07__kpi-lbl {
  font-size: .8rem;
  color: var(--muted);
}

.tg-07__hint {
  font-size: .8rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .tg-07__link {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const links = document.querySelectorAll('.tg-07__link');
  links.forEach(l => {
    l.addEventListener('click', function(e){
      e.preventDefault();
      links.forEach(x => x.classList.remove('tg-07__link--active'));
      this.classList.add('tg-07__link--active');
    });
  });
})();
```
