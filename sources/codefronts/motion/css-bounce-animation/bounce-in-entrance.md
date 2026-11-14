---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/bounce-in-entrance/"
title: "Bounce-In Entrance"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "The canonical bounceIn entrance every animate.css user has copy-pasted at some point, rewritten as vanilla CSS with a modern cubic-bezier + 5-stop keyframe.…"
has_js: "true"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bounce-In Entrance
Source: https://codefronts.com/motion/css-bounce-animation/bounce-in-entrance/

The canonical bounceIn entrance every animate.css user has copy-pasted at some point, rewritten as vanilla CSS with a modern cubic-bezier + 5-stop keyframe. A single centered card scales in from 0 with elastic overshoot then settles. Perfect drop-in replacement for the animate__bounceIn class most tutorials still teach — no 20KB library import needed. Click the trigger to replay the entrance.
## HTML
```html
<div class="bn-02">
  <button class="bn-02__trigger" id="bn-02-open" type="button">Replay bounce-in</button>
  <div class="bn-02__backdrop" id="bn-02-stage">
    <div class="bn-02__card">
      <span class="bn-02__badge" aria-hidden="true">✨</span>
      <h2 class="bn-02__title">bounceIn</h2>
      <p class="bn-02__sub">Vanilla CSS replica of the animate.css <code>bounceIn</code> class — 5-stop keyframe, 750ms, cubic-bezier(.34,1.56,.64,1).</p>
    </div>
  </div>
</div>
```
## CSS
```css
.bn-02 {
  --page-bg: #f8fafc;
  --card: #ffffff;
  --ink: #0f172a;
  --sub: #64748b;
  --brand: #635bff;
  --brand-dark: #4f46e5;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(60% 60% at 20% 20%, rgba(99,91,255,.08) 0%, transparent 55%), var(--page-bg);
  color: var(--ink);
}

.bn-02 *,
.bn-02 *::before,
.bn-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-02 ::selection {
  background: var(--brand);
  color: #fff;
}

.bn-02__trigger {
  position: absolute;
  top: 32px;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: .85rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 8px 18px -6px rgba(99,91,255,.4);
  transition: background .18s ease;
  z-index: 2;
}

.bn-02__trigger:hover {
  background: var(--brand-dark);
}

.bn-02__backdrop {
  display: flex;
  align-items: center;
  justify-content: center;
  width: min(520px,100%);
  padding: 60px 40px;
  border-radius: 18px;
  background: rgba(99,91,255,.06);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
}

.bn-02__card {
  padding: 36px 32px;
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 20px 40px -12px rgba(15,23,42,.16);
  text-align: center;
  max-width: 340px;
  opacity: 0;
  transform: scale(.3);
  animation: bn-02-bounce-in .75s cubic-bezier(.34,1.56,.64,1) both;
}

.bn-02__backdrop.is-replay .bn-02__card {
  animation: none;
  animation: bn-02-bounce-in .75s cubic-bezier(.34,1.56,.64,1) both;
}

@keyframes bn-02-bounce-in {
  0% {
    opacity: 0;
    transform: scale(.3);
  }

  20% {
    transform: scale(1.1);
  }

  40% {
    transform: scale(.9);
  }

  60% {
    opacity: 1;
    transform: scale(1.03);
  }

  80% {
    transform: scale(.97);
  }

  100% {
    opacity: 1;
    transform: scale(1);
  }
}

.bn-02__badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: linear-gradient(135deg,#a78bfa,#635bff);
  color: #fff;
  font-size: 22px;
  margin-bottom: 16px;
}

.bn-02__title {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.1;
  margin-bottom: 8px;
}

.bn-02__sub {
  font-size: .85rem;
  color: var(--sub);
  line-height: 1.5;
}

.bn-02__sub code {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .78rem;
  padding: 1px 5px;
  border-radius: 4px;
  background: #f1f5f9;
  color: var(--brand);
}

@media (prefers-reduced-motion: reduce) {
  .bn-02__card,
    .bn-02__backdrop.is-replay .bn-02__card {
    animation: bn-02-fade .3s ease-out both!important;
  }

  @keyframes bn-02-fade {
    from {
      opacity: 0;
    }

    to {
      opacity: 1;
      transform: scale(1);
    }
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.bn-02');
  if (!root) return;
  var btn = root.querySelector('#bn-02-open');
  var stage = root.querySelector('#bn-02-stage');
  if (!btn || !stage) return;
  btn.addEventListener('click', function(){
    stage.classList.remove('is-replay');
    void stage.offsetWidth;
    stage.classList.add('is-replay');
  });
})();
```
