---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/saas-feature-highlight-card/"
title: "SaaS Feature Highlight Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Dark feature tile with 44×44 gradient icon tile, \"NEW\" chip, headline, one-line description, and a \"Learn more →\" link whose arrow slides on hover."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Feature Highlight Card
Source: https://codefronts.com/components/css-cards/saas-feature-highlight-card/

Dark feature tile with 44×44 gradient icon tile, "NEW" chip, headline, one-line description, and a "Learn more →" link whose arrow slides on hover.
## HTML
```html
<section class="card-12">
  <article class="card-12__card">
    <span class="card-12__icon" aria-hidden="true">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="7" r="4"/><path d="M3 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2"/><circle cx="17" cy="7" r="4" opacity="0.6"/><path d="M14 15h4a4 4 0 0 1 4 4v2" opacity="0.6"/></svg>
    </span>
    <span class="card-12__chip">New</span>
    <h3 class="card-12__title">Real-time collaboration</h3>
    <p class="card-12__desc">See teammates' cursors and edits as they happen — no refresh, no conflicts.</p>
    <a class="card-12__link" href="#learn">
      Learn more
      <span class="card-12__arrow" aria-hidden="true">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </span>
    </a>
  </article>
</section>
```
## CSS
```css
.card-12 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: #f8f7f4;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #6366f1;
}

.card-12 *,
.card-12 *::before,
.card-12 *::after {
  box-sizing: border-box;
}

.card-12__card {
  position: relative;
  width: 100%;
  max-width: 340px;
  margin: 0 auto;
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 18px;
  padding: 22px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
  transition: transform 0.25s, box-shadow 0.25s, border-color 0.25s;
}

.card-12__card:hover {
  transform: translateY(-2px);
  border-color: rgba(99, 102, 241, 0.2);
  box-shadow: 0 14px 32px rgba(0, 0, 0, 0.06), 0 0 0 4px rgba(99, 102, 241, 0.04);
}

.card-12__icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: linear-gradient(135deg, #818cf8 0%, #6366f1 100%);
  box-shadow: 0 6px 16px rgba(99, 102, 241, 0.28), 0 0 0 1px rgba(255, 255, 255, 0.4) inset;
  margin-bottom: 16px;
}

.card-12__chip {
  position: absolute;
  top: 22px;
  right: 22px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: #6366f1;
  padding: 3px 9px;
  background: rgba(99, 102, 241, 0.10);
  border: 1px solid rgba(99, 102, 241, 0.2);
  border-radius: 999px;
  text-transform: uppercase;
}

.card-12__title {
  font-size: 17px;
  font-weight: 700;
  margin: 0 0 6px;
  color: #1a1a1a;
  letter-spacing: -0.01em;
}

.card-12__desc {
  font-size: 13px;
  color: #6b6b7c;
  margin: 0 0 16px;
  line-height: 1.55;
}

.card-12__link {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 13px;
  font-weight: 700;
  color: #4338ca;
  text-decoration: none;
  padding: 6px 0;
  min-height: 32px;
  border-radius: 6px;
  transition: color 0.18s;
}

.card-12__arrow {
  display: inline-flex;
  align-items: center;
  transition: transform 0.2s ease;
}

.card-12__link:hover .card-12__arrow,
.card-12__card:hover .card-12__arrow {
  transform: translateX(3px);
}

.card-12__link:hover {
  color: #312e81;
}

.card-12__link:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
  border-radius: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .card-12__card,
    .card-12__link,
    .card-12__arrow {
    transition: none;
  }

  .card-12__card:hover {
    transform: none;
  }
}
```
