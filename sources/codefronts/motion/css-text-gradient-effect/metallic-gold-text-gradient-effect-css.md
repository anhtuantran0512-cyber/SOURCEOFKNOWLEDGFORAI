---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/metallic-gold-text-gradient-effect-css/"
title: "Metallic Gold Text Gradient Effect CSS"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A luxury membership card with a multi-stop metallic gold gradient simulating light reflection, animated via background-position shift."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Metallic Gold Text Gradient Effect CSS
Source: https://codefronts.com/motion/css-text-gradient-effect/metallic-gold-text-gradient-effect-css/

A luxury membership card with a multi-stop metallic gold gradient simulating light reflection, animated via background-position shift.
## HTML
```html
<div class="tg-10">
  <div class="tg-10__card">
    <div class="tg-10__crown">✦</div>
    <p class="tg-10__tier">PREMIER MEMBERSHIP</p>
    <h2 class="tg-10__name"><span class="tg-10__gold">Aurum</span></h2>
    <p class="tg-10__tagline">Excellence, redefined.</p>
    <ul class="tg-10__perks">
      <li><span class="tg-10__check">✦</span> Priority concierge access</li>
      <li><span class="tg-10__check">✦</span> Curated portfolio management</li>
      <li><span class="tg-10__check">✦</span> Exclusive event invitations</li>
    </ul>
    <div class="tg-10__divider"></div>
    <div class="tg-10__price"><span class="tg-10__amount tg-10__gold">$2,500</span><span class="tg-10__cycle">/year</span></div>
    <button class="tg-10__cta">Request access</button>
  </div>
</div>
```
## CSS
```css
.tg-10,
.tg-10 *,
.tg-10 *::before,
.tg-10 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-10 ::selection {
  background: #b45309;
  color: #fef3c7;
}

.tg-10 {
  /* Multi-stop metallic gold: dark → mid-gold → highlight → dark → shimmer */
  --gold-grad: linear-gradient(
      135deg,
      #92400e 0%,
      #b45309 15%,
      #d97706 30%,
      #fbbf24 45%,
      #fef3c7 55%,
      #fbbf24 65%,
      #d97706 80%,
      #92400e 100%
    );
  --bg: #080604;
  --surface: #0e0b07;
  --border: rgba(251,191,36,.18);
  --text: #fef9ee;
  --muted: #92816a;
  font-family: Georgia, 'Times New Roman', serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.tg-10__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 44px 36px;
  max-width: 380px;
  width: 100%;
  text-align: center;
  box-shadow: 0 0 60px rgba(251,191,36,.06);
}

.tg-10__crown {
  font-size: 1.6rem;
  background: var(--gold-grad);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 2px 6px rgba(251,191,36,.35));
  margin-bottom: 12px;
}

.tg-10__tier {
  font-family: system-ui, -apple-system, sans-serif;
  font-size: .65rem;
  font-weight: 700;
  letter-spacing: .18em;
  color: var(--muted);
  margin-bottom: 16px;
}
/* The metallic effect uses many gradient stops to simulate light reflection */

.tg-10__gold {
  background: var(--gold-grad);
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  animation: tg-10-shimmer 4s ease-in-out infinite;
}

@keyframes tg-10-shimmer {
  0%,
    100% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }
}

.tg-10__name {
  font-size: 4rem;
  font-weight: 700;
  letter-spacing: -.02em;
  line-height: 1;
  margin-bottom: 8px;
}

.tg-10__tagline {
  font-style: italic;
  color: var(--muted);
  font-size: .9rem;
  margin-bottom: 28px;
}

.tg-10__perks {
  list-style: none;
  text-align: left;
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 28px;
  font-family: system-ui, sans-serif;
}

.tg-10__perks li {
  font-size: .875rem;
  color: var(--text);
  display: flex;
  align-items: center;
  gap: 10px;
}

.tg-10__check {
  background: var(--gold-grad);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: .7rem;
}

.tg-10__divider {
  height: 1px;
  background: var(--border);
  margin-bottom: 20px;
}

.tg-10__price {
  display: flex;
  align-items: baseline;
  gap: 4px;
  justify-content: center;
  margin-bottom: 22px;
}

.tg-10__amount {
  font-size: 2rem;
  font-weight: 700;
  font-family: system-ui, sans-serif;
}

.tg-10__cycle {
  font-size: .85rem;
  color: var(--muted);
  font-family: system-ui, sans-serif;
}

.tg-10__cta {
  width: 100%;
  padding: 13px;
  border-radius: 8px;
  border: 1px solid rgba(251,191,36,.4);
  background: transparent;
  font-family: system-ui, sans-serif;
  font-size: .9rem;
  font-weight: 600;
  color: #fbbf24;
  cursor: pointer;
  transition: background .2s, color .2s;
}

.tg-10__cta:hover {
  background: rgba(251,191,36,.1);
}

@media (prefers-reduced-motion: reduce) {
  .tg-10__gold {
    animation: none;
    background-position: 0% 50%;
  }
}
```
