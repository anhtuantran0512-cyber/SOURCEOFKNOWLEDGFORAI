---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/web3-glowing-gradient-text-css/"
title: "Web3 Glowing Gradient Text CSS"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A cyberpunk-inspired Web3 card where a blurred duplicate element creates a neon glow bloom effect behind the gradient text."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Web3 Glowing Gradient Text CSS
Source: https://codefronts.com/motion/css-text-gradient-effect/web3-glowing-gradient-text-css/

A cyberpunk-inspired Web3 card where a blurred duplicate element creates a neon glow bloom effect behind the gradient text.
## HTML
```html
<div class="tg-02">
  <div class="tg-02__card">
    <div class="tg-02__eyebrow">⬡ Decentralized Protocol</div>
    <h2 class="tg-02__title">Own Your<br><span class="tg-02__glow-wrap"><span class="tg-02__glow-text">Digital Future</span><span class="tg-02__glow-bloom" aria-hidden="true">Digital Future</span></span></h2>
    <p class="tg-02__desc">Stake, earn, and govern—powered by transparent on-chain contracts.</p>
    <div class="tg-02__pill-row">
      <span class="tg-02__pill">Polygon</span>
      <span class="tg-02__pill">Solana</span>
      <span class="tg-02__pill">Ethereum</span>
    </div>
  </div>
</div>
```
## CSS
```css
.tg-02,
.tg-02 *,
.tg-02 *::before,
.tg-02 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-02 ::selection {
  background: #0ff2;
  color: #fff;
}

.tg-02 {
  --neon-a: #00f0ff;
  --neon-b: #a855f7;
  --neon-c: #ff2d78;
  --bg: #040714;
  --card-bg: rgba(255,255,255,.03);
  --border: rgba(0,240,255,.12);
  --text: #e2e8f0;
  --muted: #7dd3fc;
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.tg-02__card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 48px 40px;
  max-width: 560px;
  text-align: center;
  backdrop-filter: blur(12px);
}

.tg-02__eyebrow {
  font-size: .8125rem;
  font-weight: 600;
  letter-spacing: .1em;
  color: var(--neon-a);
  margin-bottom: 20px;
}

.tg-02__title {
  font-size: clamp(2rem, 6vw, 3.5rem);
  font-weight: 900;
  line-height: 1.1;
  color: var(--text);
  letter-spacing: -.03em;
  margin-bottom: 20px;
}
/* Glow technique: gradient text + absolute blurred copy for bloom */

.tg-02__glow-wrap {
  position: relative;
  display: inline-block;
}

.tg-02__glow-text {
  background: linear-gradient(90deg, var(--neon-a) 0%, var(--neon-b) 55%, var(--neon-c) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  position: relative;
  z-index: 1;
}
/* Blurred duplicate creates the neon glow bloom */

.tg-02__glow-bloom {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, var(--neon-a) 0%, var(--neon-b) 55%, var(--neon-c) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  filter: blur(18px);
  opacity: .55;
  z-index: 0;
  animation: tg-02-pulse 3s ease-in-out infinite;
}

@keyframes tg-02-pulse {
  0%,
    100% {
    opacity: .4;
    filter: blur(18px);
  }

  50% {
    opacity: .75;
    filter: blur(22px);
  }
}

.tg-02__desc {
  color: var(--muted);
  font-size: .9375rem;
  line-height: 1.7;
  margin-bottom: 28px;
}

.tg-02__pill-row {
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
}

.tg-02__pill {
  font-size: .8125rem;
  font-weight: 600;
  padding: 5px 14px;
  border-radius: 99px;
  border: 1px solid rgba(0,240,255,.25);
  color: var(--neon-a);
  background: rgba(0,240,255,.06);
}

@media (prefers-reduced-motion: reduce) {
  .tg-02__glow-bloom {
    animation: none;
    opacity: .5;
  }
}
```
