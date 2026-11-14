---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-animated-notification-bell-hover/"
title: "CSS Animated Notification Bell Hover"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Bell physics in two doses: a hover bell built from a two-part inline SVG whose body and clapper animate SEPARATELY (the clapper lags a beat behind the shell,…"
has_js: "false"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Notification Bell Hover
Source: https://codefronts.com/snippets/css-notifications/css-animated-notification-bell-hover/

Bell physics in two doses: a hover bell built from a two-part inline SVG whose body and clapper animate SEPARATELY (the clapper lags a beat behind the shell, which is what makes it read as ringing rather than wobbling), and an ambient reminder bell that rings a short burst every six seconds using the keyframe dead-time trick — silenced entirely by its do-not-disturb toggle via :has().
## HTML
```html
<div class="ntf-20-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-20a" aria-label="Bell that rings on hover with counter-swinging clapper">
  <div class="ntf-20a__wrap">
    <button class="ntf-20a__bell" type="button" aria-label="Notifications">
      <svg viewBox="0 0 48 48" fill="none" aria-hidden="true">
        <g class="ntf-20a__shell"><path d="M24 6c-7 0-11.5 5.4-11.5 12.2 0 8.8-3.1 11.4-4.6 13.1-.7.8-.2 2.2 1 2.2h30.2c1.2 0 1.7-1.4 1-2.2-1.5-1.7-4.6-4.3-4.6-13.1C35.5 11.4 31 6 24 6z" fill="currentColor"/><rect x="21.6" y="2.6" width="4.8" height="5" rx="2.4" fill="currentColor"/></g>
        <circle class="ntf-20a__clapper" cx="24" cy="37.5" r="3.4" fill="currentColor"/>
      </svg>
    </button>
    <p class="ntf-20a__hint">hover the bell — the shell swings, the clapper counter-swings 60ms behind</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-20b" aria-label="Bell ringing periodically with do-not-disturb switch">
  <div class="ntf-20b__card">
    <div class="ntf-20b__bellrow">
      <span class="ntf-20b__bell" aria-hidden="true">
        <svg viewBox="0 0 48 48" fill="none"><g class="ntf-20b__shell"><path d="M24 6c-7 0-11.5 5.4-11.5 12.2 0 8.8-3.1 11.4-4.6 13.1-.7.8-.2 2.2 1 2.2h30.2c1.2 0 1.7-1.4 1-2.2-1.5-1.7-4.6-4.3-4.6-13.1C35.5 11.4 31 6 24 6z" fill="currentColor"/><path d="M20 37a4 4 0 0 0 8 0" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></g></svg>
        <i class="ntf-20b__dot"></i>
      </span>
      <span class="ntf-20b__tx"><b>Standup in 5 minutes</b><small>rings a short burst every 6s until you respond</small></span>
    </div>
    <label class="ntf-20b__dnd"><input type="checkbox" id="ntf-20b-dnd"><span class="ntf-20b__track" aria-hidden="true"><i></i></span><span class="ntf-20b__dndtx">Do not disturb</span></label>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-20-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-20-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-20a,
.ntf-20a *,
.ntf-20a *::before,
.ntf-20a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-20a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#171b26,#0c0e15);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-20a__wrap {
  display: grid;
  gap: 24px;
  justify-items: center;
}

.ntf-20a__bell {
  width: 104px;
  height: 104px;
  display: grid;
  place-items: center;
  border: 1px solid rgba(170,195,235,.18);
  border-radius: 28px;
  color: oklch(0.85 0.12 85);
  background: linear-gradient(180deg,rgba(255,255,255,.07),rgba(255,255,255,.02));
  cursor: pointer;
  box-shadow: 0 26px 55px -28px rgba(0,0,0,.9);
  transition: translate .2s,background .2s;
}

.ntf-20a__bell:hover {
  translate: 0 -3px;
  background: linear-gradient(180deg,rgba(255,255,255,.1),rgba(255,255,255,.04));
}

.ntf-20a__bell:focus-visible {
  outline: 2px solid oklch(0.85 0.12 85);
  outline-offset: 3px;
}

.ntf-20a__bell svg {
  width: 52px;
  height: 52px;
  overflow: visible;
}

.ntf-20a__shell,
.ntf-20a__clapper {
  transform-box: fill-box;
  transform-origin: 50% 0%;
}

.ntf-20a__clapper {
  transform-origin: 50% -900%;
}

.ntf-20a__bell:hover .ntf-20a__shell,
.ntf-20a__bell:focus-visible .ntf-20a__shell {
  animation: ntf-20a-swing .9s ease-in-out;
}

.ntf-20a__bell:hover .ntf-20a__clapper,
.ntf-20a__bell:focus-visible .ntf-20a__clapper {
  animation: ntf-20a-clap .9s ease-in-out .06s;
}

@keyframes ntf-20a-swing {
  20% {
    rotate: 14deg;
  }

  45% {
    rotate: -11deg;
  }

  68% {
    rotate: 6deg;
  }

  85% {
    rotate: -3deg;
  }

  100% {
    rotate: 0deg;
  }
}

@keyframes ntf-20a-clap {
  25% {
    rotate: -16deg;
  }

  50% {
    rotate: 13deg;
  }

  72% {
    rotate: -7deg;
  }

  88% {
    rotate: 3deg;
  }

  100% {
    rotate: 0deg;
  }
}

.ntf-20a__hint {
  font-size: 12.5px;
  color: rgba(212,224,246,.45);
  text-align: center;
  max-inline-size: 34ch;
  line-height: 1.6;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-20a__bell:hover .ntf-20a__shell,
    .ntf-20a__bell:hover .ntf-20a__clapper,
    .ntf-20a__bell:focus-visible .ntf-20a__shell,
    .ntf-20a__bell:focus-visible .ntf-20a__clapper {
    animation: none;
  }

  .ntf-20a__bell:hover {
    color: #fff;
  }
}

.ntf-20b,
.ntf-20b *,
.ntf-20b *::before,
.ntf-20b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-20b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f7f3ea,#eee7d6);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-20b__card {
  width: min(400px,100%);
  padding: 26px;
  border-radius: 20px;
  background: #fffdf7;
  border: 1px solid rgba(36,31,23,.11);
  box-shadow: 0 28px 62px -34px rgba(36,31,23,.5);
  display: grid;
  gap: 20px;
}

.ntf-20b__bellrow {
  display: flex;
  align-items: center;
  gap: 16px;
}

.ntf-20b__bell {
  position: relative;
  flex: none;
  width: 58px;
  height: 58px;
  display: grid;
  place-items: center;
  border-radius: 17px;
  color: #241f17;
  background: oklch(0.85 0.14 85 / .25);
  border: 1px solid oklch(0.7 0.14 85 / .4);
}

.ntf-20b__bell svg {
  width: 32px;
  height: 32px;
  overflow: visible;
}

.ntf-20b__shell {
  transform-box: fill-box;
  transform-origin: 50% 0%;
  animation: ntf-20b-burst 6s ease-in-out infinite;
}

@keyframes ntf-20b-burst {
  2% {
    rotate: 12deg;
  }

  5% {
    rotate: -10deg;
  }

  8% {
    rotate: 6deg;
  }

  10.5% {
    rotate: -3deg;
  }

  12%,
    100% {
    rotate: 0deg;
  }
}

.ntf-20b__dot {
  position: absolute;
  top: 8px;
  inset-inline-end: 8px;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: oklch(0.63 0.21 25);
  border: 2px solid #fffdf7;
}

.ntf-20b__tx {
  display: grid;
  gap: 2px;
}

.ntf-20b__tx b {
  font-size: 15px;
  font-weight: 600;
  color: #241f17;
}

.ntf-20b__tx small {
  font-size: 12px;
  line-height: 1.5;
  color: rgba(36,31,23,.55);
}

.ntf-20b:has(#ntf-20b-dnd:checked) .ntf-20b__shell {
  animation: none;
}

.ntf-20b:has(#ntf-20b-dnd:checked) .ntf-20b__dot {
  background: rgba(36,31,23,.25);
}

.ntf-20b:has(#ntf-20b-dnd:checked) .ntf-20b__bell {
  color: rgba(36,31,23,.4);
}

.ntf-20b__dnd {
  display: flex;
  align-items: center;
  gap: 11px;
  cursor: pointer;
  user-select: none;
}

.ntf-20b__dnd input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.ntf-20b__track {
  width: 44px;
  height: 25px;
  border-radius: 999px;
  background: rgba(36,31,23,.15);
  padding: 3px;
  transition: background .25s;
}

.ntf-20b__track i {
  display: block;
  width: 19px;
  height: 19px;
  border-radius: 50%;
  background: #fffdf7;
  box-shadow: 0 1px 3px rgba(36,31,23,.35);
  transition: translate .25s cubic-bezier(.22,1.4,.36,1);
}

.ntf-20b:has(#ntf-20b-dnd:checked) .ntf-20b__track {
  background: #241f17;
}

.ntf-20b:has(#ntf-20b-dnd:checked) .ntf-20b__track i {
  translate: 19px 0;
}

.ntf-20b__dnd:has(input:focus-visible) .ntf-20b__track {
  outline: 2px solid #241f17;
  outline-offset: 2px;
}

.ntf-20b__dndtx {
  font-size: 13.5px;
  font-weight: 600;
  color: #241f17;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-20b__shell {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the bell is two SVG groups on separate keyframes: opposite rotation signs, a 60ms clapper delay for inertia, transform-box:fill-box so the pivots sit at the mount instead of the viewBox corner. */

/* No JavaScript — the ring burst lives in the first 12% of a 6s loop (dead-time trick, since animation-delay only delays the first cycle), and :has(#dnd:checked) silences bell, badge and all. */
```
