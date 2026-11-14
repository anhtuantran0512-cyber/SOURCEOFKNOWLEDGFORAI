---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-notification-card-overlay/"
title: "Glassmorphism Notification Card Overlay"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Overlay UI where blur is functional, not decorative: a toast stack that slides in staggered over a mock app (each with icon, copy, action and a draining time…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Notification Card Overlay
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-notification-card-overlay/

Overlay UI where blur is functional, not decorative: a toast stack that slides in staggered over a mock app (each with icon, copy, action and a draining time bar), and a notification-center panel with unread pulse dots and hover-revealed archive actions.
## HTML
```html
<div class="glz-15-group">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
<section class="glz-15a" aria-label="Glass toast notifications demo">
  <div class="glz-15a__mock" aria-hidden="true">
    <div class="glz-15a__mockbar"><i></i><i></i><i></i></div>
    <div class="glz-15a__mockgrid"><b></b><b></b><b></b><b></b><b></b><b></b></div>
  </div>
  <div class="glz-15a__stack" role="log" aria-live="polite" aria-label="Notifications">
    <div class="glz-15a__toast" style="--tone:oklch(0.8 0.16 155);--d:.2s"><span class="glz-15a__ic">✓</span><div class="glz-15a__tx"><b>Deploy complete</b><em>codefronts.com is live — build #482 in 41s</em></div><button type="button">View</button></div>
    <div class="glz-15a__toast" style="--tone:oklch(0.78 0.13 230);--d:1.1s"><span class="glz-15a__ic">↓</span><div class="glz-15a__tx"><b>Export ready</b><em>glass-cards.zip · 2.4 MB</em></div><button type="button">Save</button></div>
    <div class="glz-15a__toast" style="--tone:oklch(0.8 0.14 75);--d:2s"><span class="glz-15a__ic">!</span><div class="glz-15a__tx"><b>Storage at 91%</b><em>Old previews can be cleared automatically</em></div><button type="button">Fix</button></div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
<section class="glz-15b" aria-label="Glass notification center demo">
  <article class="glz-15b__panel">
    <header class="glz-15b__head"><h3>Notifications</h3><button type="button" class="glz-15b__clear">Mark all read</button></header>
    <div class="glz-15b__day">Today</div>
    <ul class="glz-15b__list">
      <li class="glz-15b__row glz-15b__row--new"><i class="glz-15b__dot" aria-label="Unread"></i><img src="https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?q=80&w=160&auto=format&fit=crop" alt="" loading="lazy"><div><b>Noor mentioned you</b><em>“@you the glass nav is 🔥 — ship it?”</em><time>2m</time></div><span class="glz-15b__act"><button type="button" aria-label="Reply">↩</button><button type="button" aria-label="Archive">🗄</button></span></li>
      <li class="glz-15b__row glz-15b__row--new"><i class="glz-15b__dot" aria-label="Unread"></i><span class="glz-15b__sys" aria-hidden="true">▲</span><div><b>Build passed</b><em>main · 128 tests · 38s</em><time>18m</time></div><span class="glz-15b__act"><button type="button" aria-label="Open build">→</button><button type="button" aria-label="Archive">🗄</button></span></li>
      <li class="glz-15b__row"><img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=160&auto=format&fit=crop" alt="" loading="lazy"><div><b>Theo shared a file</b><em>pricing-v3.fig · 4.1 MB</em><time>1h</time></div><span class="glz-15b__act"><button type="button" aria-label="Download">↓</button><button type="button" aria-label="Archive">🗄</button></span></li>
    </ul>
  </article>
</section>
</div>
```
## CSS
```css
.glz-15-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-15-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-15a,
.glz-15a *,
.glz-15a *::before,
.glz-15a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-15a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0d1120;
  font-family: 'Instrument Sans',system-ui,sans-serif;
}

.glz-15a__mock {
  position: absolute;
  inset: 8%;
  border-radius: 22px;
  background: linear-gradient(165deg,#161d33,#101527);
  border: 1px solid rgba(140,160,220,.15);
  padding: 18px;
  opacity: .9;
}

.glz-15a__mockbar {
  display: flex;
  gap: 7px;
}

.glz-15a__mockbar i {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: #2a3352;
}

.glz-15a__mockgrid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 14px;
  margin-top: 18px;
  height: calc(100% - 40px);
}

.glz-15a__mockgrid b {
  border-radius: 14px;
  background: linear-gradient(150deg,oklch(0.45 0.12 265/.5),oklch(0.4 0.1 320/.35));
  border: 1px solid rgba(140,160,220,.12);
}

.glz-15a__stack {
  position: relative;
  z-index: 2;
  width: min(360px,88vw);
  display: grid;
  gap: 12px;
  justify-self: end;
  align-self: start;
  margin: 6% 6% 0 0;
}

.glz-15a__toast {
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 14px 16px;
  border-radius: 17px;
  color: #eef1fc;
  background: linear-gradient(160deg,rgba(255,255,255,.14),rgba(255,255,255,.05));
  backdrop-filter: blur(18px) saturate(170%);
  -webkit-backdrop-filter: blur(18px) saturate(170%);
  border: 1px solid rgba(255,255,255,.22);
  box-shadow: 0 22px 46px -18px rgba(0,0,0,.75),inset 0 1px 0 rgba(255,255,255,.25);
  opacity: 0;
  transform: translateX(40px) scale(.95);
  animation: glz-15a-in .55s cubic-bezier(.2,.9,.3,1.2) var(--d) forwards;
}

.glz-15a__toast::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  height: 3px;
  width: 100%;
  background: var(--tone);
  transform-origin: left;
  animation: glz-15a-drain 6s linear calc(var(--d) + .5s) forwards;
}

.glz-15a__toast:hover::after {
  animation-play-state: paused;
}

.glz-15a__ic {
  width: 34px;
  height: 34px;
  flex: none;
  display: grid;
  place-items: center;
  border-radius: 11px;
  font-weight: 800;
  font-size: 14px;
  color: #0c1018;
  background: var(--tone);
  box-shadow: 0 0 16px color-mix(in oklab,var(--tone) 55%,transparent);
}

.glz-15a__tx {
  flex: 1;
  min-width: 0;
}

.glz-15a__tx b {
  display: block;
  font-size: 13.5px;
  font-weight: 700;
}

.glz-15a__tx em {
  display: block;
  font-style: normal;
  font-size: 11.5px;
  color: rgba(238,241,252,.6);
  margin-top: 2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.glz-15a__toast button {
  padding: 8px 12px;
  border-radius: 9px;
  border: 1px solid rgba(255,255,255,.25);
  background: rgba(255,255,255,.1);
  color: #fff;
  font: 700 11.5px 'Instrument Sans',sans-serif;
  cursor: pointer;
  transition: background .2s ease;
}

.glz-15a__toast button:hover {
  background: rgba(255,255,255,.2);
}

.glz-15a__toast button:focus-visible {
  outline: 2px solid var(--tone);
  outline-offset: 2px;
}

@keyframes glz-15a-in {
  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes glz-15a-drain {
  to {
    transform: scaleX(0);
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-15a__toast {
    background: rgba(22,28,48,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-15a__toast {
    animation: glz-15a-in .001s var(--d) forwards;
  }

  .glz-15a__toast::after {
    animation: none;
    transform: scaleX(.4);
  }
}

.glz-15b,
.glz-15b *,
.glz-15b *::before,
.glz-15b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-15b {
  --acc: oklch(0.75 0.17 300);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  position: relative;
  overflow: hidden;
  background: linear-gradient(200deg,#151129,#0d1020);
}

.glz-15b::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(44% 40% at 80% 16%,oklch(0.55 0.2 300/.4),transparent 70%),radial-gradient(40% 34% at 12% 86%,oklch(0.55 0.15 200/.35),transparent 70%);
}

.glz-15b__panel {
  position: relative;
  z-index: 1;
  width: min(410px,100%);
  padding: 22px;
  border-radius: 24px;
  color: #f0edfb;
  font-family: 'Instrument Sans',system-ui,sans-serif;
  background: linear-gradient(165deg,rgba(255,255,255,.12),rgba(255,255,255,.04));
  backdrop-filter: blur(24px) saturate(170%);
  -webkit-backdrop-filter: blur(24px) saturate(170%);
  border: 1px solid rgba(255,255,255,.2);
  box-shadow: 0 34px 70px -26px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.24);
}

.glz-15b__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.glz-15b__head h3 {
  font-size: 17px;
  font-weight: 700;
}

.glz-15b__clear {
  border: none;
  background: transparent;
  color: var(--acc);
  font: 600 12px 'Instrument Sans',sans-serif;
  cursor: pointer;
  padding: 6px 8px;
  border-radius: 8px;
}

.glz-15b__clear:hover {
  background: oklch(0.75 0.17 300/.14);
}

.glz-15b__clear:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.glz-15b__day {
  margin-top: 14px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(240,237,251,.4);
}

.glz-15b__list {
  list-style: none;
  margin-top: 8px;
  display: grid;
  gap: 6px;
}

.glz-15b__row {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 12px 12px 20px;
  border-radius: 16px;
  border: 1px solid transparent;
  transition: background .2s ease,border-color .2s ease;
}

.glz-15b__row:hover,
.glz-15b__row:focus-within {
  background: rgba(255,255,255,.07);
  border-color: rgba(255,255,255,.14);
}

.glz-15b__row--new {
  background: rgba(255,255,255,.045);
}

.glz-15b__dot {
  position: absolute;
  left: 7px;
  top: 50%;
  translate: 0 -50%;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--acc);
  animation: glz-15b-pulse 2.4s ease-out infinite;
}

.glz-15b__row img {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  object-fit: cover;
  background: #332a4d;
}

.glz-15b__sys {
  width: 38px;
  height: 38px;
  flex: none;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-size: 13px;
  color: oklch(0.85 0.15 160);
  background: oklch(0.85 0.15 160/.12);
  border: 1px solid oklch(0.85 0.15 160/.35);
}

.glz-15b__row>div {
  flex: 1;
  min-width: 0;
  position: relative;
  padding-right: 26px;
}

.glz-15b__row b {
  display: block;
  font-size: 13.5px;
  font-weight: 700;
}

.glz-15b__row em {
  display: block;
  font-style: normal;
  font-size: 12px;
  color: rgba(240,237,251,.6);
  margin-top: 2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.glz-15b__row time {
  position: absolute;
  right: 0;
  top: 1px;
  font-size: 10.5px;
  color: rgba(240,237,251,.4);
}

.glz-15b__act {
  display: flex;
  gap: 6px;
  opacity: 0;
  translate: 6px 0;
  transition: opacity .2s ease,translate .2s ease;
}

.glz-15b__row:hover .glz-15b__act,
.glz-15b__row:focus-within .glz-15b__act {
  opacity: 1;
  translate: 0 0;
}

.glz-15b__act button {
  width: 30px;
  height: 30px;
  border-radius: 9px;
  border: 1px solid rgba(255,255,255,.2);
  background: rgba(255,255,255,.08);
  color: #f0edfb;
  font-size: 12px;
  cursor: pointer;
}

.glz-15b__act button:hover {
  background: rgba(255,255,255,.18);
}

.glz-15b__act button:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@keyframes glz-15b-pulse {
  0% {
    box-shadow: 0 0 0 0 oklch(0.75 0.17 300/.55);
  }

  70%,
    100% {
    box-shadow: 0 0 0 9px transparent;
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-15b__panel {
    background: rgba(26,21,44,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-15b__dot {
    animation: none;
  }

  .glz-15b__act {
    opacity: 1;
    translate: 0 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — toasts stagger in via per-toast --d delays; each ::after bar drains over 6s and pauses while hovered, mirroring production toast behaviour. */

/* No JavaScript — unread dots pulse via expanding transparent box-shadow; row actions reveal on hover AND :focus-within (and stay visible under reduced-motion). */
```
