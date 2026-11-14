---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/notification-badge-pop/"
title: "Notification Badge Pop"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "A bell icon with a red count badge that pops into view when a new notification arrives — the bell shakes briefly and the badge scales up with elastic overshoot."
has_js: "true"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Notification Badge Pop
Source: https://codefronts.com/motion/css-bounce-animation/notification-badge-pop/

A bell icon with a red count badge that pops into view when a new notification arrives — the bell shakes briefly and the badge scales up with elastic overshoot. Slack / Discord / Notion header notification pattern. The demo centers a large bell + badge as the hero — the bounce reads as "new event arrived NOW."
## HTML
```html
<div class="bn-09">
  <p class="bn-09__label">New notification arriving</p>
  <button class="bn-09__bell" id="bn-09-bell" aria-label="Notifications, 0 unread">
    <svg viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M6 8a6 6 0 0112 0c0 7 3 9 3 9H3s3-2 3-9"/>
      <path d="M10.3 21a1.94 1.94 0 003.4 0"/>
    </svg>
    <span class="bn-09__badge" id="bn-09-badge" aria-hidden="true">0</span>
  </button>
  <p class="bn-09__hint">The bell rings + badge pops each time a new event arrives.</p>
  <div class="bn-09__live" role="status" aria-live="polite" id="bn-09-live"></div>
</div>
```
## CSS
```css
.bn-09 {
  --page-bg: #faf7ff;
  --surface: #ffffff;
  --ink: #1c1917;
  --sub: #78716c;
  --slack: #4a154b;
  --red: #ef4444;
  --line: #e7e5e0;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  padding: 32px;
  background: radial-gradient(60% 60% at 50% 50%, rgba(74,21,75,.06) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
  text-align: center;
}

.bn-09 *,
.bn-09 *::before,
.bn-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-09 ::selection {
  background: var(--slack);
  color: #fff;
}

.bn-09__label {
  font-size: .9rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
}

.bn-09__bell {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 88px;
  height: 88px;
  border: none;
  border-radius: 14px;
  background: var(--surface);
  color: var(--slack);
  cursor: pointer;
  box-shadow: 0 12px 30px -8px rgba(74,21,75,.18),0 4px 8px -4px rgba(74,21,75,.08);
  transition: background .18s ease;
  will-change: transform;
}

.bn-09__bell:hover {
  background: #f9f4fa;
}

.bn-09__bell:focus-visible {
  outline: 2px solid var(--slack);
  outline-offset: 4px;
}

.bn-09__bell.is-ringing svg {
  animation: bn-09-bell-shake .7s ease-out;
  transform-origin: top center;
}

@keyframes bn-09-bell-shake {
  0% {
    transform: rotate(0);
  }

  15% {
    transform: rotate(-15deg);
  }

  30% {
    transform: rotate(12deg);
  }

  45% {
    transform: rotate(-8deg);
  }

  60% {
    transform: rotate(4deg);
  }

  75% {
    transform: rotate(-2deg);
  }

  100% {
    transform: rotate(0);
  }
}

.bn-09__badge {
  position: absolute;
  top: 8px;
  right: 4px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 24px;
  height: 24px;
  padding: 0 7px;
  border-radius: 12px;
  background: var(--red);
  color: #fff;
  font-size: .75rem;
  font-weight: 800;
  border: 3px solid var(--surface);
  font-variant-numeric: tabular-nums;
  opacity: 0;
  transform: scale(0);
  will-change: transform;
}

.bn-09__badge.is-visible {
  opacity: 1;
  transform: scale(1);
}

.bn-09__badge.is-popping {
  animation: bn-09-badge-pop .55s cubic-bezier(.34,1.56,.64,1) forwards;
}

@keyframes bn-09-badge-pop {
  0% {
    transform: scale(0);
    opacity: 0;
  }

  30% {
    transform: scale(1.3);
    opacity: 1;
  }

  50% {
    transform: scale(.9);
  }

  70% {
    transform: scale(1.08);
  }

  100% {
    transform: scale(1);
    opacity: 1;
  }
}

.bn-09__hint {
  font-size: .78rem;
  color: var(--sub);
  max-width: 320px;
  line-height: 1.5;
}

.bn-09__live {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

@media (prefers-reduced-motion: reduce) {
  .bn-09__bell.is-ringing svg {
    animation: none!important;
  }

  .bn-09__badge.is-popping {
    animation: none!important;
  }

  .bn-09__badge.is-visible {
    transform: scale(1)!important;
    opacity: 1!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.bn-09');
  if (!root) return;
  var bell = root.querySelector('#bn-09-bell');
  var badge = root.querySelector('#bn-09-badge');
  var live = root.querySelector('#bn-09-live');
  if (!bell || !badge) return;
  var count = 0;
  function ring(){
    count++;
    badge.textContent = String(count);
    bell.setAttribute('aria-label', 'Notifications, ' + count + ' unread');
    if (live) live.textContent = count + ' new notification' + (count === 1 ? '' : 's');
    badge.classList.add('is-visible');
    bell.classList.add('is-ringing');
    badge.classList.add('is-popping');
    setTimeout(function(){
      bell.classList.remove('is-ringing');
      badge.classList.remove('is-popping');
    }, 750);
  }
  function reset(){ count = 0; badge.textContent = '0'; badge.classList.remove('is-visible'); bell.setAttribute('aria-label', 'Notifications, 0 unread'); }
  setInterval(function(){ if (count >= 4) { reset(); return; } ring(); }, 2600);
})();
```
