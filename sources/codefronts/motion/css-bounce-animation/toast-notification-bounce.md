---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/toast-notification-bounce/"
title: "Toast Notification Bounce"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "A dev-tool toast notification that bounces up from the bottom of the frame — Sonner / Radix Toast / react-hot-toast aesthetic (deep-charcoal surface,…"
has_js: "true"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Toast Notification Bounce
Source: https://codefronts.com/motion/css-bounce-animation/toast-notification-bounce/

A dev-tool toast notification that bounces up from the bottom of the frame — Sonner / Radix Toast / react-hot-toast aesthetic (deep-charcoal surface, semantic icon + copy + dismiss action, mono timestamp). The bounce reads as "new event arrived" with spring-settle physics. Dark-mode-first because dev tools live in dark IDEs. JS auto-cycles through success / info / warning states so users see the pattern in action.
## HTML
```html
<div class="bn-04">
  <p class="bn-04__label">Toast notification arrives from below</p>
  <div class="bn-04__toast-slot" id="bn-04-slot" role="status" aria-live="polite" aria-atomic="true"></div>
</div>
```
## CSS
```css
.bn-04 {
  --page-bg: #0b1220;
  --surface: #111827;
  --surface-hi: #1e2a3d;
  --ink: #f1f5f9;
  --sub: #94a3b8;
  --muted: #64748b;
  --success: #10b981;
  --info: #3b82f6;
  --warn: #f59e0b;
  --line: #1f2a3d;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 80px;
  padding: 32px;
  background: radial-gradient(70% 50% at 50% 100%, rgba(16,185,129,.08) 0%, transparent 55%), var(--page-bg);
  color: var(--ink);
}

.bn-04 *,
.bn-04 *::before,
.bn-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-04 ::selection {
  background: var(--success);
  color: var(--surface);
}

.bn-04__label {
  font-size: .85rem;
  font-weight: 600;
  letter-spacing: .02em;
  color: var(--sub);
}

.bn-04__toast-slot {
  display: flex;
  justify-content: center;
  min-width: min(400px,100%);
}

.bn-04__toast {
  position: relative;
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 14px 44px 14px 16px;
  border-radius: 12px;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 20px 40px -12px rgba(0,0,0,.5),0 4px 8px -4px rgba(0,0,0,.3);
  animation: bn-04-toast-in .55s cubic-bezier(.34,1.56,.64,1) both;
  min-width: 320px;
}

.bn-04__toast.is-out {
  animation: bn-04-toast-out .25s cubic-bezier(.65,0,.35,1) forwards;
}

@keyframes bn-04-toast-in {
  0% {
    opacity: 0;
    transform: translateY(140%) scale(.9);
  }

  60% {
    opacity: 1;
    transform: translateY(-8%) scale(1.02);
  }

  80% {
    transform: translateY(2%) scale(.99);
  }

  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@keyframes bn-04-toast-out {
  0% {
    opacity: 1;
    transform: translateY(0) scale(1);
  }

  100% {
    opacity: 0;
    transform: translateY(140%) scale(.94);
  }
}

.bn-04__toast-icon {
  flex-shrink: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  margin-top: 1px;
}

.bn-04__toast--success .bn-04__toast-icon {
  background: rgba(16,185,129,.14);
  color: var(--success);
}

.bn-04__toast--info .bn-04__toast-icon {
  background: rgba(59,130,246,.14);
  color: var(--info);
}

.bn-04__toast--warn .bn-04__toast-icon {
  background: rgba(245,158,11,.14);
  color: var(--warn);
}

.bn-04__toast-body {
  flex: 1;
  min-width: 0;
}

.bn-04__toast-title {
  font-size: .9rem;
  font-weight: 700;
  color: var(--ink);
  letter-spacing: -.005em;
  margin-bottom: 2px;
}

.bn-04__toast-desc {
  font-size: .78rem;
  color: var(--sub);
  line-height: 1.45;
}

.bn-04__toast-time {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .68rem;
  font-weight: 600;
  color: var(--muted);
  margin-top: 4px;
  letter-spacing: .02em;
  font-variant-numeric: tabular-nums;
}

.bn-04__toast-x {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 26px;
  height: 26px;
  border: none;
  border-radius: 6px;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  font-family: inherit;
  font-size: 13px;
  transition: background .15s ease,color .15s ease;
}

.bn-04__toast-x:hover {
  background: var(--surface-hi);
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .bn-04__toast {
    animation: bn-04-fade .2s ease-out both!important;
  }

  .bn-04__toast.is-out {
    animation: bn-04-fade-out .2s ease-in forwards!important;
  }

  @keyframes bn-04-fade {
    from {
      opacity: 0;
    }

    to {
      opacity: 1;
    }
  }

  @keyframes bn-04-fade-out {
    from {
      opacity: 1;
    }

    to {
      opacity: 0;
    }
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.bn-04');
  if (!root) return;
  var slot = root.querySelector('#bn-04-slot');
  if (!slot) return;
  var seq = [
    { type:'success', title:'Payment confirmed', desc:'Charge succeeded · pi_3O2xLm', time:'just now',
      icon:'<svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>' },
    { type:'info', title:'Webhook received', desc:'payment_intent.succeeded → 200 OK', time:'2s ago',
      icon:'<svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>' },
    { type:'warn', title:'3D Secure required', desc:'Redirecting customer to auth challenge', time:'5s ago',
      icon:'<svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>' }
  ];
  var i = 0;
  function render(item){
    slot.innerHTML = '';
    var toast = document.createElement('div');
    toast.className = 'bn-04__toast bn-04__toast--' + item.type;
    toast.innerHTML =
      '<span class="bn-04__toast-icon">' + item.icon + '</span>' +
      '<div class="bn-04__toast-body">' +
        '<p class="bn-04__toast-title">' + item.title + '</p>' +
        '<p class="bn-04__toast-desc">' + item.desc + '</p>' +
        '<p class="bn-04__toast-time">' + item.time + '</p>' +
      '</div>' +
      '<button class="bn-04__toast-x" aria-label="Dismiss">✕</button>';
    slot.appendChild(toast);
    toast.querySelector('.bn-04__toast-x').addEventListener('click', function(){
      toast.classList.add('is-out');
      setTimeout(function(){ if (toast.parentNode) toast.parentNode.removeChild(toast); }, 250);
    });
  }
  function cycle(){ render(seq[i % seq.length]); i++; setTimeout(cycle, 3200); }
  cycle();
})();
```
