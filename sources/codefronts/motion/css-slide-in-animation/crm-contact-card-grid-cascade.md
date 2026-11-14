---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/crm-contact-card-grid-cascade/"
title: "CRM Contact Card Grid Cascade"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "Six B2B CRM contact cards that cascade in a 3×2 grid, each showing an avatar, name, job title, company, deal stage badge, and last-contacted timestamp — the…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CRM Contact Card Grid Cascade
Source: https://codefronts.com/motion/css-slide-in-animation/crm-contact-card-grid-cascade/

Six B2B CRM contact cards that cascade in a 3×2 grid, each showing an avatar, name, job title, company, deal stage badge, and last-contacted timestamp — the layout used by Salesforce, HubSpot, Pipedrive, and Attio contact list views.
## HTML
```html
<div class="sl-13">
  <div class="sl-13__inner">
    <div class="sl-13__head">
      <p class="sl-13__kicker">Sales Pipeline · Q4 Prospects</p>
      <h2>Active contacts (6)</h2>
    </div>
    <div class="sl-13__grid">
      <div class="sl-13__contact">
        <div class="sl-13__avatar" style="--g:linear-gradient(135deg,#0176d3,#0284c7)">SC</div>
        <h3>Sarah Chen</h3>
        <p class="sl-13__role">VP Engineering · Northlight</p>
        <div class="sl-13__meta">
          <span class="sl-13__stage sl-13__stage--won">Won</span>
          <small>2 days ago</small>
        </div>
      </div>
      <div class="sl-13__contact">
        <div class="sl-13__avatar" style="--g:linear-gradient(135deg,#f59e0b,#d97706)">MR</div>
        <h3>Marcus Rivera</h3>
        <p class="sl-13__role">CTO · Brightpath Inc.</p>
        <div class="sl-13__meta">
          <span class="sl-13__stage sl-13__stage--neg">Negotiation</span>
          <small>4 hours ago</small>
        </div>
      </div>
      <div class="sl-13__contact">
        <div class="sl-13__avatar" style="--g:linear-gradient(135deg,#8b5cf6,#7c3aed)">JK</div>
        <h3>Jordan Kim</h3>
        <p class="sl-13__role">Head of Ops · Slate Systems</p>
        <div class="sl-13__meta">
          <span class="sl-13__stage sl-13__stage--prop">Proposal</span>
          <small>1 day ago</small>
        </div>
      </div>
      <div class="sl-13__contact">
        <div class="sl-13__avatar" style="--g:linear-gradient(135deg,#ec4899,#be185d)">MS</div>
        <h3>Maria Silva</h3>
        <p class="sl-13__role">CFO · Quantum Labs</p>
        <div class="sl-13__meta">
          <span class="sl-13__stage sl-13__stage--qual">Qualified</span>
          <small>3 days ago</small>
        </div>
      </div>
      <div class="sl-13__contact">
        <div class="sl-13__avatar" style="--g:linear-gradient(135deg,#10b981,#0891b2)">DL</div>
        <h3>David Lin</h3>
        <p class="sl-13__role">Director of Product · Vertex Co.</p>
        <div class="sl-13__meta">
          <span class="sl-13__stage sl-13__stage--won">Won</span>
          <small>1 week ago</small>
        </div>
      </div>
      <div class="sl-13__contact">
        <div class="sl-13__avatar" style="--g:linear-gradient(135deg,#f97316,#dc2626)">AH</div>
        <h3>Aisha Hassan</h3>
        <p class="sl-13__role">Head of Growth · Meridian AI</p>
        <div class="sl-13__meta">
          <span class="sl-13__stage sl-13__stage--neg">Negotiation</span>
          <small>6 hours ago</small>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sl-13 {
  --bg: #f8fafc;
  --card: #fff;
  --accent: #0176d3;
  --ink: #0f172a;
  --sub: #64748b;
  --line: #e2e8f0;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: var(--bg);
  color: var(--ink);
}

.sl-13 *,
.sl-13 *::before,
.sl-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-13 ::selection {
  background: var(--accent);
  color: #fff;
}

.sl-13__inner {
  width: 100%;
  max-width: 900px;
}

.sl-13__head {
  margin-bottom: 20px;
}

.sl-13__kicker {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 4px;
}

.sl-13__head h2 {
  font-size: 1.3rem;
  font-weight: 800;
  letter-spacing: -.02em;
}

.sl-13__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 14px;
}

.sl-13__contact {
  padding: 18px 18px;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 10px;
  box-shadow: 0 4px 12px -8px rgba(15,23,42,.1);
  opacity: 0;
  transform: translateY(24px);
  animation: sl-13-card .5s cubic-bezier(.22,1,.36,1) forwards;
  transition: transform .15s ease,box-shadow .18s ease,border-color .18s ease;
}

.sl-13__contact:hover {
  transform: translateY(-2px);
  border-color: var(--accent);
  box-shadow: 0 10px 20px -10px rgba(1,118,211,.2);
}

.sl-13__contact:nth-child(1) {
  animation-delay: .08s;
}

.sl-13__contact:nth-child(2) {
  animation-delay: .16s;
}

.sl-13__contact:nth-child(3) {
  animation-delay: .24s;
}

.sl-13__contact:nth-child(4) {
  animation-delay: .32s;
}

.sl-13__contact:nth-child(5) {
  animation-delay: .4s;
}

.sl-13__contact:nth-child(6) {
  animation-delay: .48s;
}

.sl-13__avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--g,#333);
  color: #fff;
  font-size: .85rem;
  font-weight: 800;
  letter-spacing: .02em;
  margin-bottom: 12px;
}

.sl-13__contact h3 {
  font-size: .92rem;
  font-weight: 700;
  letter-spacing: -.01em;
  margin-bottom: 2px;
}

.sl-13__role {
  font-size: .75rem;
  color: var(--sub);
  line-height: 1.35;
  margin-bottom: 12px;
}

.sl-13__meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 6px;
}

.sl-13__stage {
  padding: 3px 8px;
  border-radius: 5px;
  font-size: .66rem;
  font-weight: 700;
  letter-spacing: .02em;
}

.sl-13__stage--won {
  background: rgba(16,185,129,.14);
  color: #059669;
}

.sl-13__stage--neg {
  background: rgba(245,158,11,.14);
  color: #b45309;
}

.sl-13__stage--prop {
  background: rgba(139,92,246,.14);
  color: #7c3aed;
}

.sl-13__stage--qual {
  background: rgba(1,118,211,.14);
  color: var(--accent);
}

.sl-13__meta small {
  font-size: .68rem;
  color: var(--sub);
}

@keyframes sl-13-card {
  from {
    opacity: 0;
    transform: translateY(24px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-13__contact {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}

@media (max-width: 720px) {
  .sl-13__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 480px) {
  .sl-13__grid {
    grid-template-columns: 1fr;
  }
}
```
