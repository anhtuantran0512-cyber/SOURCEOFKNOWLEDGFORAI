---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/scroll-down-arrow-bounce/"
title: "Scroll Down Arrow Bounce"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "A landing-page scroll-down indicator — a chevron arrow bouncing gently downward in an infinite loop, signaling \"there's more content below.\" Deep purple →…"
has_js: "false"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll Down Arrow Bounce
Source: https://codefronts.com/motion/css-bounce-animation/scroll-down-arrow-bounce/

A landing-page scroll-down indicator — a chevron arrow bouncing gently downward in an infinite loop, signaling "there's more content below." Deep purple → magenta gradient surface with the arrow as the visual anchor. The canonical Apple / Vercel / Linear landing-page pattern users search for when building marketing pages. Uses translateY with a multi-stop bounce keyframe — never margin-top or padding-top which would trigger layout on every frame.
## HTML
```html
<div class="bn-01">
  <p class="bn-01__hint">You're at the top</p>
  <button class="bn-01__scroll" type="button" aria-label="Scroll to next section">
    <span class="bn-01__label">Scroll</span>
    <span class="bn-01__arrow" aria-hidden="true">
      <svg viewBox="0 0 40 40" width="40" height="40" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="10 15 20 25 30 15"/>
      </svg>
    </span>
  </button>
</div>
```
## CSS
```css
.bn-01 {
  --ink: #f5f0ff;
  --sub: rgba(245,240,255,.6);
  --accent: #f9a8d4;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 80px;
  padding: 64px 32px;
  background: radial-gradient(60% 60% at 50% 50%, rgba(249,168,212,.18) 0%, transparent 65%), linear-gradient(135deg,#3b0764 0%,#5b21b6 45%,#831843 100%);
  color: var(--ink);
  text-align: center;
}

.bn-01 *,
.bn-01 *::before,
.bn-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-01 ::selection {
  background: var(--accent);
  color: #3b0764;
}

.bn-01__hint {
  font-size: .9rem;
  color: var(--sub);
  letter-spacing: .06em;
  font-weight: 500;
}

.bn-01__scroll {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  min-width: 88px;
  padding: 14px 24px;
  background: transparent;
  border: none;
  color: var(--ink);
  cursor: pointer;
  font-family: inherit;
  transition: opacity .18s ease;
}

.bn-01__scroll:hover {
  opacity: .75;
}

.bn-01__scroll:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 8px;
  border-radius: 8px;
}

.bn-01__label {
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
}

.bn-01__arrow {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--ink);
  animation: bn-01-bounce 2.4s cubic-bezier(.55,0,.45,1) infinite;
}

@keyframes bn-01-bounce {
  0% {
    transform: translateY(0);
  }

  30% {
    transform: translateY(-14px);
  }

  50% {
    transform: translateY(-4px);
  }

  70% {
    transform: translateY(-10px);
  }

  100% {
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bn-01__arrow {
    animation: bn-01-pulse 3s ease-in-out infinite;
  }

  @keyframes bn-01-pulse {
    0%,
        100% {
      opacity: 1;
    }

    50% {
      opacity: .55;
    }
  }
}
```
