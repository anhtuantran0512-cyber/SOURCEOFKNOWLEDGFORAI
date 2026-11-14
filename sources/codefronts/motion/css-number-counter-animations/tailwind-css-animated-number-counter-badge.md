---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/tailwind-css-animated-number-counter-badge/"
title: "Tailwind CSS Animated Number Counter Badge"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "Notification, cart and inbox badges that pop when the count changes — written twice: once in plain scoped CSS you can paste anywhere, and once as the exact…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Animated Number Counter Badge
Source: https://codefronts.com/motion/css-number-counter-animations/tailwind-css-animated-number-counter-badge/

Notification, cart and inbox badges that pop when the count changes — written twice: once in plain scoped CSS you can paste anywhere, and once as the exact Tailwind v4 utility string (given in the walkthrough) for projects already on Tailwind. The badge scales, the digit rolls, and a 99+ overflow rule keeps the pill from stretching past its design width.
## HTML
```html
<section class="cnc-05" aria-label="Tailwind style animated counter badge demo">
  <div class="cnc-05__stage">
    <div class="cnc-05__bar">
      <div class="cnc-05__brand">Acme<span>Mail</span></div>
      <div class="cnc-05__icons">
        <button class="cnc-05__icon" type="button" data-kind="bell" aria-label="Notifications, 7 unread">
          <svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M18 8a6 6 0 1 0-12 0c0 7-3 8-3 8h18s-3-1-3-8"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/></svg>
          <span class="cnc-05__badge" data-count="7" aria-hidden="true">7</span>
        </button>
        <button class="cnc-05__icon" type="button" data-kind="cart" aria-label="Cart, 3 items">
          <svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="9" cy="20" r="1.4"/><circle cx="18" cy="20" r="1.4"/><path d="M2 3h2.2l2.4 12.3a2 2 0 0 0 2 1.6h8.6a2 2 0 0 0 2-1.6L21 7H5.4"/></svg>
          <span class="cnc-05__badge" data-count="3" aria-hidden="true">3</span>
        </button>
        <button class="cnc-05__icon" type="button" data-kind="inbox" aria-label="Inbox, 128 unread">
          <svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M3 12h5l1.6 3h4.8L16 12h5"/><path d="M4.6 5.5 3 12v6a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1v-6l-1.6-6.5a1 1 0 0 0-1-.5H5.6a1 1 0 0 0-1 .5z"/></svg>
          <span class="cnc-05__badge" data-count="128" aria-hidden="true">99+</span>
        </button>
        <div class="cnc-05__avatar" aria-hidden="true">JR</div>
      </div>
    </div>
    <div class="cnc-05__ctrls">
      <button class="cnc-05__btn" type="button" data-act="bell">+1 notification</button>
      <button class="cnc-05__btn" type="button" data-act="cart">+1 cart item</button>
      <button class="cnc-05__btn" type="button" data-act="reset">Mark all read</button>
    </div>
    <p class="cnc-05__sr" role="status" aria-live="polite"></p>
    <p class="cnc-05__chip" aria-hidden="true">min-w + px pill · tabular-nums · ring halo · reflow-restarted pop keyframes</p>
  </div>
</section>
```
## CSS
```css
.cnc-05,
.cnc-05 *,
.cnc-05 *::before,
.cnc-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-05-bg: oklch(0.19 0.02 265);
  --cnc-05-bar: oklch(0.25 0.022 265);
  --cnc-05-ink: oklch(0.97 0.005 260);
  --cnc-05-mut: oklch(0.68 0.02 265);
  --cnc-05-acc: oklch(0.65 0.23 20);
  background: var(--cnc-05-bg);
  color: var(--cnc-05-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: clamp(18px,4vw,48px);
}

.cnc-05__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  width: min(100%,540px);
  padding: 14px 18px;
  border-radius: 16px;
  background: var(--cnc-05-bar);
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.08),0 18px 44px oklch(0 0 0/.42);
}

.cnc-05__brand {
  font-size: 16px;
  font-weight: 720;
  letter-spacing: -.02em;
}

.cnc-05__brand span {
  color: var(--cnc-05-acc);
}

.cnc-05__icons {
  display: flex;
  align-items: center;
  gap: 6px;
}

.cnc-05__icon {
  position: relative;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border: 0;
  border-radius: 12px;
  background: transparent;
  color: var(--cnc-05-mut);
  cursor: pointer;
  transition: background .2s,color .2s;
}

.cnc-05__icon:hover {
  background: oklch(1 0 0/.08);
  color: var(--cnc-05-ink);
}

.cnc-05__icon:focus-visible {
  outline: 3px solid var(--cnc-05-acc);
  outline-offset: 2px;
}

.cnc-05__badge {
  position: absolute;
  top: 4px;
  right: 3px;
  display: grid;
  place-items: center;
  min-width: 20px;
  height: 20px;
  padding: 0 6px;
  border-radius: 99px;
  background: var(--cnc-05-acc);
  box-shadow: 0 0 0 2.5px var(--cnc-05-bar);
  color: oklch(0.99 0 0);
  font-size: 11px;
  font-weight: 750;
  line-height: 1;
  letter-spacing: -.01em;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-05__badge[hidden] {
  display: none;
}

.cnc-05__pop {
  animation: cnc-05-pop .44s cubic-bezier(.16,1,.3,1);
}

@keyframes cnc-05-pop {
  0% {
    scale: 1;
  }

  45% {
    scale: 1.32;
  }

  100% {
    scale: 1;
  }
}

.cnc-05__avatar {
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  margin-left: 8px;
  border-radius: 50%;
  background: linear-gradient(140deg,oklch(0.7 0.15 250),oklch(0.62 0.2 300));
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .02em;
}

.cnc-05__ctrls {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
}

.cnc-05__btn {
  min-height: 44px;
  padding: 0 16px;
  border: 1px solid oklch(1 0 0/.16);
  border-radius: 99px;
  background: oklch(1 0 0/.05);
  color: var(--cnc-05-ink);
  font: inherit;
  font-size: 13.5px;
  font-weight: 620;
  cursor: pointer;
  transition: background .2s,transform .2s;
}

.cnc-05__btn:hover {
  background: oklch(1 0 0/.12);
  transform: translateY(-1px);
}

.cnc-05__btn:active {
  transform: translateY(0) scale(.98);
}

.cnc-05__btn:focus-visible {
  outline: 3px solid var(--cnc-05-acc);
  outline-offset: 3px;
}

.cnc-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-05__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-05-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .cnc-05__pop {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.cnc-05').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const say = root.querySelector('.cnc-05__sr');
    const labels = { bell: 'Notifications', cart: 'Cart', inbox: 'Inbox' };

    const render = (icon) => {
      const badge = icon.querySelector('.cnc-05__badge');
      const n = +badge.dataset.count;
      badge.textContent = n > 99 ? '99+' : n;        // cap before render: bounded layout
      badge.hidden = n === 0;                        // zero leaves the a11y tree entirely
      icon.setAttribute('aria-label', labels[icon.dataset.kind] + ', ' + n + (icon.dataset.kind === 'cart' ? ' items' : ' unread'));
      badge.classList.remove('cnc-05__pop');
      void badge.offsetWidth;                        // forced reflow restarts the keyframes
      badge.classList.add('cnc-05__pop');
    };

    root.querySelectorAll('.cnc-05__btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        const act = btn.dataset.act;
        if (act === 'reset') {
          root.querySelectorAll('.cnc-05__icon').forEach((i) => { i.querySelector('.cnc-05__badge').dataset.count = 0; render(i); });
          say.textContent = 'All notifications cleared';
          return;
        }
        const icon = root.querySelector('.cnc-05__icon[data-kind="' + act + '"]');
        const badge = icon.querySelector('.cnc-05__badge');
        badge.dataset.count = +badge.dataset.count + 1;
        render(icon);
        say.textContent = labels[act] + ': ' + badge.dataset.count;
      });
    });
    root.querySelectorAll('.cnc-05__icon').forEach(render);
  });
})();
```
