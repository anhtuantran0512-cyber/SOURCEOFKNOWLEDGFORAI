---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-dark-mode-subtle-mesh-pulse/"
title: "CSS Dark Mode Subtle Mesh Pulse"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "A low-contrast dark-mode background built from layered radial gradients on pseudo-elements that slowly translate and rotate, replacing flat pure-black with…"
has_js: "true"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Dark Mode Subtle Mesh Pulse
Source: https://codefronts.com/motion/css-gradient-animation/css-dark-mode-subtle-mesh-pulse/

A low-contrast dark-mode background built from layered radial gradients on pseudo-elements that slowly translate and rotate, replacing flat pure-black with breathing, atmospheric depth.
## HTML
```html
<div class="ga-04">
  <div class="ga-04__bar">
    <div class="ga-04__logo">
      <div class="ga-04__logo-mark">✦</div>
      <span class="ga-04__logo-name">Axiom</span>
    </div>
    <nav class="ga-04__nav">
      <span class="ga-04__nav-item ga-04__nav-item--active">Product</span>
      <span class="ga-04__nav-item">Pricing</span>
      <span class="ga-04__nav-item">Docs</span>
      <span class="ga-04__nav-item">Blog</span>
    </nav>
  </div>

  <div class="ga-04__hero">
    <div class="ga-04__kicker">
      <span class="ga-04__kicker-ring"></span>
      Built for dark mode
    </div>
    <h1 class="ga-04__title">Your workflow,<br><em>beautifully dark</em></h1>
    <p class="ga-04__sub">Subtle ambient gradients that breathe with your UI. No harsh blacks. No eye strain. Just clean, deep dark-mode done right.</p>
    <div class="ga-04__actions">
      <button class="ga-04__btn ga-04__btn--fill">Get Started Free</button>
      <button class="ga-04__btn ga-04__btn--outline">Explore →</button>
    </div>
  </div>

  <div class="ga-04__cards">
    <div class="ga-04__card">
      <div class="ga-04__card-icon">⚡</div>
      <div class="ga-04__card-title">Zero Config</div>
      <div class="ga-04__card-body">Works out of the box. No build steps, no config files.</div>
    </div>
    <div class="ga-04__card">
      <div class="ga-04__card-icon">🔒</div>
      <div class="ga-04__card-title">Secure by Default</div>
      <div class="ga-04__card-body">End-to-end encryption on every request, every time.</div>
    </div>
    <div class="ga-04__card">
      <div class="ga-04__card-icon">🌐</div>
      <div class="ga-04__card-title">Global Edge</div>
      <div class="ga-04__card-body">190 PoPs. Sub-10ms latency worldwide.</div>
    </div>
  </div>

  <div class="ga-04__palette">
    <div class="ga-04__swatch ga-04__swatch--indigo active" data-m1="#1a1040" data-m2="#0f1f30" data-m3="#1a0e28" data-m4="#0d1e1a" data-acc="#6366f1" title="Indigo"></div>
    <div class="ga-04__swatch ga-04__swatch--teal"   data-m1="#0a2420" data-m2="#0f2030" data-m3="#082820" data-m4="#0f2418" data-acc="#10b981" title="Teal"></div>
    <div class="ga-04__swatch ga-04__swatch--rose"   data-m1="#2a0a18" data-m2="#1a0a30" data-m3="#280812" data-m4="#1a0e20" data-acc="#f43f5e" title="Rose"></div>
  </div>
</div>
```
## CSS
```css
.ga-04,
.ga-04 *,
.ga-04 *::before,
.ga-04 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-04 ::selection {
  background: rgba(99,102,241,.5);
  color: #fff;
}

.ga-04 {
  --bg: #0a0a0f;
  --m1: #1a1040;
  --m2: #0f1f30;
  --m3: #1a0e28;
  --m4: #0d1e1a;
  --accent: #6366f1;
  --dur: 14s;
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow: hidden;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 36px;
}
/* Mesh layer: overlapping soft radial gradients on one pseudo-element */

.ga-04::before {
  content: '';
  position: absolute;
  inset: -30%;
  background: radial-gradient(ellipse 60% 55% at 20% 20%, var(--m1) 0%, transparent 70%), radial-gradient(ellipse 55% 50% at 80% 75%, var(--m2) 0%, transparent 70%), radial-gradient(ellipse 50% 60% at 75% 15%, var(--m3) 0%, transparent 70%), radial-gradient(ellipse 60% 45% at 25% 80%, var(--m4) 0%, transparent 70%);
  animation: ga-04-mesh var(--dur) ease-in-out infinite alternate;
  opacity: .95;
}

@keyframes ga-04-mesh {
  0% {
    transform: translate(0, 0) rotate(0deg);
  }

  33% {
    transform: translate(5%, 4%) rotate(3deg);
  }

  66% {
    transform: translate(-4%, 6%) rotate(-2deg);
  }

  100% {
    transform: translate(3%, -3%) rotate(1.5deg);
  }
}
/* Second mesh layer offset */

.ga-04::after {
  content: '';
  position: absolute;
  inset: -30%;
  background: radial-gradient(ellipse 45% 55% at 55% 50%, rgba(99,102,241,.06) 0%, transparent 65%), radial-gradient(ellipse 35% 45% at 30% 60%, rgba(16,185,129,.05) 0%, transparent 60%);
  animation: ga-04-mesh2 calc(var(--dur) * 1.4) ease-in-out infinite alternate-reverse;
}

@keyframes ga-04-mesh2 {
  0% {
    transform: translate(0, 0);
  }

  50% {
    transform: translate(-6%, 5%);
  }

  100% {
    transform: translate(4%, -4%);
  }
}
/* Topbar */

.ga-04__bar {
  position: relative;
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.ga-04__logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.ga-04__logo-mark {
  width: 30px;
  height: 30px;
  border-radius: 8px;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
}

.ga-04__logo-name {
  font-size: .9rem;
  font-weight: 700;
  color: #fff;
  letter-spacing: -.01em;
}

.ga-04__nav {
  display: flex;
  gap: 6px;
}

.ga-04__nav-item {
  padding: 5px 12px;
  font-size: .78rem;
  color: rgba(255,255,255,.4);
  border-radius: 6px;
  cursor: pointer;
  transition: color .2s, background .2s;
}

.ga-04__nav-item:hover {
  color: rgba(255,255,255,.8);
  background: rgba(255,255,255,.06);
}

.ga-04__nav-item--active {
  color: rgba(255,255,255,.85);
  background: rgba(255,255,255,.07);
}
/* Center hero */

.ga-04__hero {
  position: relative;
  z-index: 3;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 14px;
  padding: 24px 0;
}

.ga-04__kicker {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 4px 14px;
  border-radius: 999px;
  border: 1px solid rgba(99,102,241,.25);
  background: rgba(99,102,241,.08);
  font-size: 11.5px;
  color: #818cf8;
  font-weight: 600;
  letter-spacing: .06em;
}

.ga-04__kicker-ring {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  border: 1.5px solid #818cf8;
  position: relative;
}

.ga-04__kicker-ring::after {
  content: '';
  position: absolute;
  inset: 1.5px;
  border-radius: 50%;
  background: #818cf8;
  animation: ga-04-ring-fill 2.5s ease-in-out infinite;
}

@keyframes ga-04-ring-fill {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(0);
    opacity: 0;
  }
}

.ga-04__title {
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -.03em;
  color: #f1f5f9;
  max-width: 600px;
}

.ga-04__title em {
  font-style: normal;
  background: linear-gradient(90deg, #818cf8, #a78bfa, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.ga-04__sub {
  font-size: .95rem;
  color: rgba(255,255,255,.4);
  line-height: 1.72;
  max-width: 440px;
}

.ga-04__actions {
  display: flex;
  gap: 10px;
  margin-top: 6px;
}

.ga-04__btn {
  padding: 10px 24px;
  border-radius: 8px;
  font-size: .875rem;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: all .2s;
}

.ga-04__btn--fill {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: #fff;
  box-shadow: 0 0 0 0 rgba(99,102,241,0);
}

.ga-04__btn--fill:hover {
  box-shadow: 0 0 24px rgba(99,102,241,.45);
  transform: translateY(-1px);
}

.ga-04__btn--outline {
  background: transparent;
  color: rgba(255,255,255,.5);
  border: 1px solid rgba(255,255,255,.1);
}

.ga-04__btn--outline:hover {
  border-color: rgba(255,255,255,.2);
  color: rgba(255,255,255,.75);
}
/* Bottom card row */

.ga-04__cards {
  position: relative;
  z-index: 3;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.ga-04__card {
  padding: 16px;
  border-radius: 12px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.06);
  backdrop-filter: blur(8px);
  transition: border-color .25s, background .25s;
}

.ga-04__card:hover {
  background: rgba(255,255,255,.055);
  border-color: rgba(99,102,241,.2);
}

.ga-04__card-icon {
  font-size: 1.3rem;
  margin-bottom: 8px;
}

.ga-04__card-title {
  font-size: .8rem;
  font-weight: 700;
  color: rgba(255,255,255,.75);
  margin-bottom: 4px;
}

.ga-04__card-body {
  font-size: .72rem;
  color: rgba(255,255,255,.35);
  line-height: 1.55;
}
/* Palette toggle */

.ga-04__palette {
  position: absolute;
  top: 36px;
  right: 36px;
  z-index: 10;
  display: flex;
  gap: 6px;
}

.ga-04__swatch {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  cursor: pointer;
  border: 2px solid transparent;
  transition: border-color .2s, transform .2s;
}

.ga-04__swatch:hover,
.ga-04__swatch.active {
  border-color: #fff;
  transform: scale(1.2);
}

.ga-04__swatch--indigo {
  background: linear-gradient(135deg, #1a1040, #0f1f30);
}

.ga-04__swatch--teal {
  background: linear-gradient(135deg, #0f2420, #0a2030);
}

.ga-04__swatch--rose {
  background: linear-gradient(135deg, #2a0a18, #1a0a30);
}

@media (max-width: 600px) {
  .ga-04__cards {
    grid-template-columns: 1fr;
  }

  .ga-04__nav {
    display: none;
  }

  .ga-04__palette {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ga-04::before,
    .ga-04::after {
    animation: none;
  }

  .ga-04__kicker-ring::after {
    animation: none;
    opacity: 1;
  }
}
```

## JavaScript
```js
(function() {
  const wrapper = document.querySelector('.ga-04');
  wrapper.querySelectorAll('.ga-04__swatch').forEach(sw => {
    sw.addEventListener('click', () => {
      wrapper.querySelectorAll('.ga-04__swatch').forEach(s => s.classList.remove('active'));
      sw.classList.add('active');
      ['m1','m2','m3','m4','acc'].forEach(k => {
        const val = sw.dataset[k];
        if (val) wrapper.style.setProperty('--' + k, val);
      });
    });
  });
})();
```
