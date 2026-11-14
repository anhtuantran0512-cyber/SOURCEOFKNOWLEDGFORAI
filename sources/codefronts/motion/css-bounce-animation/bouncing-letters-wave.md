---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/bouncing-letters-wave/"
title: "Bouncing Letters Wave"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "Individual letters in a word bounce up in sequence, creating a wave motion — the classic 404-page / playful branding pattern."
has_js: "false"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bouncing Letters Wave
Source: https://codefronts.com/motion/css-bounce-animation/bouncing-letters-wave/

Individual letters in a word bounce up in sequence, creating a wave motion — the classic 404-page / playful branding pattern. Deep pink surface with the letters of "BOUNCE" spelled out, each letter animated with staggered animation-delay. Every letter runs the SAME translateY bounce keyframe but starts at a different point in the cycle, creating the wave illusion. Users search for this when building error pages, empty states, or playful hero moments.
## HTML
```html
<div class="bn-13">
  <p class="bn-13__label">Bouncing letters wave</p>
  <p class="bn-13__word" aria-label="Bounce">
    <span aria-hidden="true">B</span>
    <span aria-hidden="true">O</span>
    <span aria-hidden="true">U</span>
    <span aria-hidden="true">N</span>
    <span aria-hidden="true">C</span>
    <span aria-hidden="true">E</span>
  </p>
  <p class="bn-13__hint">Each letter uses the same bounce keyframe with staggered <code>animation-delay</code>.</p>
</div>
```
## CSS
```css
.bn-13 {
  --page-bg: #831843;
  --ink: #fdf2f8;
  --sub: rgba(253,242,248,.7);
  --accent: #f9a8d4;
  --accent-hi: #f0abfc;
  font-family: -apple-system,BlinkMacSystemFont,'Poppins','Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 32px;
  padding: 32px;
  background: radial-gradient(60% 60% at 50% 40%, rgba(240,171,252,.16) 0%, transparent 60%), linear-gradient(135deg,#831843 0%,#9d174d 50%,#701a75 100%);
  color: var(--ink);
  text-align: center;
}

.bn-13 *,
.bn-13 *::before,
.bn-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-13 ::selection {
  background: var(--accent);
  color: #831843;
}

.bn-13__label {
  font-size: .9rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .14em;
  text-transform: uppercase;
}

.bn-13__word {
  display: inline-flex;
  align-items: baseline;
  gap: 6px;
  font-family: 'Poppins','Inter',sans-serif;
  font-size: clamp(4rem,10vw,7rem);
  font-weight: 900;
  letter-spacing: -.03em;
  line-height: 1.2;
  color: var(--accent-hi);
}

.bn-13__word span {
  display: inline-block;
  animation: bn-13-letter 1.8s cubic-bezier(.55,0,.45,1) infinite;
  will-change: transform;
}

.bn-13__word span:nth-child(1) {
  animation-delay: 0s;
}

.bn-13__word span:nth-child(2) {
  animation-delay: .12s;
}

.bn-13__word span:nth-child(3) {
  animation-delay: .24s;
}

.bn-13__word span:nth-child(4) {
  animation-delay: .36s;
}

.bn-13__word span:nth-child(5) {
  animation-delay: .48s;
}

.bn-13__word span:nth-child(6) {
  animation-delay: .60s;
}

@keyframes bn-13-letter {
  0% {
    transform: translateY(0);
  }

  30% {
    transform: translateY(-20px);
  }

  60% {
    transform: translateY(-8px);
  }

  100% {
    transform: translateY(0);
  }
}

.bn-13__hint {
  font-size: .78rem;
  color: var(--sub);
  max-width: 420px;
  line-height: 1.5;
}

.bn-13__hint code {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .72rem;
  padding: 1px 5px;
  border-radius: 4px;
  background: rgba(253,242,248,.14);
}

@media (prefers-reduced-motion: reduce) {
  .bn-13__word span {
    animation: none!important;
    transform: none!important;
  }
}
```
