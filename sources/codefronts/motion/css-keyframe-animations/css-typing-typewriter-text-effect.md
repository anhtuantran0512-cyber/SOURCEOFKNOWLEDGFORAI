---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-typing-typewriter-text-effect/"
title: "CSS Typing Typewriter Text Effect"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Classic typewriter cursor, multi-word loop, code-line reveal and glitch-reveal text animations using CSS width + border-right keyframes only, zero JS."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typing Typewriter Text Effect
Source: https://codefronts.com/motion/css-keyframe-animations/css-typing-typewriter-text-effect/

Classic typewriter cursor, multi-word loop, code-line reveal and glitch-reveal text animations using CSS width + border-right keyframes only, zero JS.
## HTML
```html
<div class="kf-02">
  <div class="kf-02__classic">Hello, world! — pure CSS typing.</div>

  <div class="kf-02__multi">
    <b>I build</b>
    <div class="kf-02__loop">
      <span>
        <div>websites.</div>
        <div>animations.</div>
        <div>experiences.</div>
      </span>
    </div>
  </div>

  <div class="kf-02__code">
    <div class="kf-02__code-line">const animate = (el, props) => {</div>
    <div class="kf-02__code-line">&nbsp;&nbsp;el.style.transform = 'translateY(0)';</div>
    <div class="kf-02__code-line">&nbsp;&nbsp;el.style.opacity = '1';</div>
    <div class="kf-02__code-line">&nbsp;&nbsp;return Promise.resolve(true);</div>
    <div class="kf-02__code-line">};</div>
  </div>

  <div class="kf-02__glitch" data-text="TYPOGRAPHIC">TYPOGRAPHIC</div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');

.kf-02,
.kf-02 *,
.kf-02 *::before,
.kf-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-02 ::selection {
  background: #e8ff45;
  color: #111;
}

.kf-02 {
  --bg: #111014;
  --lime: #e8ff45;
  --orange: #ff6b35;
  --blue: #4cc9f0;
  --white: #f0eee8;
  --dim: #555;
  font-family: 'JetBrains Mono',monospace;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  gap: 56px;
  color: var(--white);
}
/* 1 — Classic typewriter */

.kf-02__classic {
  font-size: clamp(1.4rem,4vw,2.2rem);
  font-weight: 700;
  color: var(--lime);
  overflow: hidden;
  white-space: nowrap;
  border-right: 3px solid var(--lime);
  width: 0;
  animation: kf-02-type1 3s steps(28) 0.5s forwards, kf-02-cur 0.7s steps(2) infinite;
}

@keyframes kf-02-type1 {
  to {
    width: 28ch;
  }
}

@keyframes kf-02-cur {
  50% {
    border-color: transparent;
  }
}
/* 2 — Multi-line loop */

.kf-02__multi {
  font-size: clamp(1rem,3vw,1.5rem);
  color: var(--white);
  position: relative;
  height: 2em;
  display: flex;
  align-items: center;
  gap: 8px;
}

.kf-02__multi b {
  color: var(--orange);
}

.kf-02__loop {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  vertical-align: bottom;
  border-right: 2px solid var(--orange);
  animation: kf-02-loop 9s steps(1) infinite;
}

.kf-02__loop span {
  display: block;
  animation: kf-02-slide 9s steps(1) infinite;
}

@keyframes kf-02-loop {
  0%,
    30% {
    width: 14ch;
  }

  31%,
    35% {
    width: 0;
  }

  36%,
    65% {
    width: 12ch;
  }

  66%,
    70% {
    width: 0;
  }

  71%,
    99% {
    width: 16ch;
  }
}

@keyframes kf-02-slide {
  0%,
    32% {
    transform: translateY(0);
  }

  33%,
    65% {
    transform: translateY(-2.1em);
  }

  66%,
    99% {
    transform: translateY(-4.2em);
  }
}
/* 3 — Code reveal */

.kf-02__code {
  background: #1a1a1f;
  border: 1px solid rgba(255,255,255,.1);
  border-left: 3px solid var(--blue);
  border-radius: 8px;
  padding: 28px 32px;
  width: min(600px,100%);
}

.kf-02__code-line {
  overflow: hidden;
  white-space: nowrap;
  color: #8ecae6;
  font-size: .95rem;
  line-height: 1.8;
}

.kf-02__code-line:nth-child(1) {
  width: 0;
  animation: kf-02-codeline 14s steps(22) 0.2s infinite;
}

.kf-02__code-line:nth-child(2) {
  width: 0;
  color: #a8dadc;
  animation: kf-02-codeline2 14s steps(28) 0.7s infinite;
}

.kf-02__code-line:nth-child(3) {
  width: 0;
  color: var(--lime);
  animation: kf-02-codeline3 14s steps(32) 1.2s infinite;
}

.kf-02__code-line:nth-child(4) {
  width: 0;
  color: #ff6b35;
  animation: kf-02-codeline4 14s steps(24) 1.7s infinite;
}

.kf-02__code-line:nth-child(5) {
  width: 0;
  color: #8ecae6;
  animation: kf-02-codeline5 14s steps(18) 2.2s infinite;
}

@keyframes kf-02-codeline {
  0%,
    6% {
    width: 0;
  }

  18%,
    90% {
    width: 22ch;
  }

  96%,
    100% {
    width: 0;
  }
}

@keyframes kf-02-codeline2 {
  0%,
    8% {
    width: 0;
  }

  22%,
    90% {
    width: 28ch;
  }

  96%,
    100% {
    width: 0;
  }
}

@keyframes kf-02-codeline3 {
  0%,
    10% {
    width: 0;
  }

  26%,
    90% {
    width: 32ch;
  }

  96%,
    100% {
    width: 0;
  }
}

@keyframes kf-02-codeline4 {
  0%,
    12% {
    width: 0;
  }

  30%,
    90% {
    width: 24ch;
  }

  96%,
    100% {
    width: 0;
  }
}

@keyframes kf-02-codeline5 {
  0%,
    14% {
    width: 0;
  }

  34%,
    90% {
    width: 18ch;
  }

  96%,
    100% {
    width: 0;
  }
}
/* 4 — Big headline glitch-type */

.kf-02__glitch {
  font-family: 'Playfair Display',serif;
  font-size: clamp(2.5rem,10vw,5rem);
  font-weight: 700;
  color: var(--white);
  position: relative;
  overflow: hidden;
  white-space: nowrap;
  width: 0;
  animation: kf-02-reveal 2s cubic-bezier(.2,.6,.4,1) 0.3s forwards;
}

.kf-02__glitch::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  color: var(--blue);
  clip-path: inset(0 0 60% 0);
  transform: translateX(-3px);
  animation: kf-02-glitch 4s steps(1) 2.5s infinite;
}

@keyframes kf-02-reveal {
  to {
    width: 100%;
  }
}

@keyframes kf-02-glitch {
  0%,
    90%,
    100% {
    clip-path: inset(0 0 100% 0);
    transform: translateX(0);
  }

  92% {
    clip-path: inset(20% 0 50% 0);
    transform: translateX(-4px);
  }

  94% {
    clip-path: inset(55% 0 10% 0);
    transform: translateX(3px);
  }

  96% {
    clip-path: inset(0 0 100% 0);
  }
}

@keyframes kf-02-blinkOrange {
  50% {
    border-color: transparent;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-02 * {
    animation: none!important;
    width: auto!important;
  }
}
```
