---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/glassmorphism-toast-notification-css/"
title: "Glassmorphism Toast Notification CSS"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Real glass, not grey rectangles: a frosted toast floating over animated gradient orbs — backdrop-filter blur + saturate, a 1px light-catching border and an…"
has_js: "false"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Toast Notification CSS
Source: https://codefronts.com/snippets/css-notifications/glassmorphism-toast-notification-css/

Real glass, not grey rectangles: a frosted toast floating over animated gradient orbs — backdrop-filter blur + saturate, a 1px light-catching border and an inner top highlight — plus a dark smoked-glass stack over a photograph that shows how to keep text legible on unpredictable backgrounds, with an @supports fallback for both.
## HTML
```html
<div class="ntf-06-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-06a" aria-label="Frosted glass toast over animated gradient orbs">
  <div class="ntf-06a__orb ntf-06a__orb--1" aria-hidden="true"></div>
  <div class="ntf-06a__orb ntf-06a__orb--2" aria-hidden="true"></div>
  <div class="ntf-06a__orb ntf-06a__orb--3" aria-hidden="true"></div>
  <div class="ntf-06a__stack">
    <div class="ntf-06a__toast" role="status">
      <span class="ntf-06a__chip" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span>
      <span class="ntf-06a__tx"><b>Focus session done</b><small>52 minutes · nice streak</small></span>
      <span class="ntf-06a__time">now</span>
    </div>
    <div class="ntf-06a__toast" role="status">
      <span class="ntf-06a__chip ntf-06a__chip--v" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v13m0 0l-4-4m4 4l4-4M4 21h16"/></svg></span>
      <span class="ntf-06a__tx"><b>Export ready</b><small>portfolio-2027.pdf · 8.4 MB</small></span>
      <span class="ntf-06a__time">1m</span>
    </div>
    <p class="ntf-06a__cap">blur(18px) saturate(1.7) · 1px light edge · inset top highlight</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-06b" aria-label="Dark glass notifications over a photograph">
  <img class="ntf-06b__photo" src="https://picsum.photos/id/1018/1600/1000" alt="" loading="lazy">
  <div class="ntf-06b__stack">
    <p class="ntf-06b__hour" aria-hidden="true">21:47</p>
    <div class="ntf-06b__toast" role="status">
      <span class="ntf-06b__app" style="--a:oklch(0.75 0.14 250)" aria-hidden="true">M</span>
      <span class="ntf-06b__tx"><b>Trail conditions update</b><small>Ridge route clear · wind 12 km/h</small></span>
    </div>
    <div class="ntf-06b__toast" role="status">
      <span class="ntf-06b__app" style="--a:oklch(0.78 0.15 60)" aria-hidden="true">S</span>
      <span class="ntf-06b__tx"><b>Sunrise in 7 hours</b><small>Golden hour starts 06:12</small></span>
    </div>
    <p class="ntf-06b__cap">dark glass: black at 42% + blur(20px) + gradient scrim = white text stays AA over any photo</p>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-06-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-06-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-06a,
.ntf-06a *,
.ntf-06a *::before,
.ntf-06a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-06a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(160deg,#141327,#1b1030 55%,#0e1626);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-06a__orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(10px);
  opacity: .85;
}

.ntf-06a__orb--1 {
  width: 340px;
  height: 340px;
  left: 12%;
  top: 14%;
  background: radial-gradient(circle at 35% 35%,oklch(0.72 0.19 320),transparent 70%);
  animation: ntf-06a-drift 13s ease-in-out infinite alternate;
}

.ntf-06a__orb--2 {
  width: 300px;
  height: 300px;
  right: 8%;
  top: 38%;
  background: radial-gradient(circle at 40% 40%,oklch(0.75 0.15 220),transparent 70%);
  animation: ntf-06a-drift 17s ease-in-out infinite alternate-reverse;
}

.ntf-06a__orb--3 {
  width: 260px;
  height: 260px;
  left: 34%;
  bottom: 6%;
  background: radial-gradient(circle at 40% 40%,oklch(0.8 0.14 60),transparent 70%);
  animation: ntf-06a-drift 15s ease-in-out 2s infinite alternate;
}

@keyframes ntf-06a-drift {
  from {
    translate: -40px -20px;
  }

  to {
    translate: 50px 30px;
  }
}

.ntf-06a__stack {
  position: relative;
  width: min(360px,100%);
  display: grid;
  gap: 14px;
}

.ntf-06a__toast {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 15px 16px;
  border-radius: 18px;
  background: rgb(255 255 255 / .13);
  -webkit-backdrop-filter: blur(18px) saturate(1.7);
  backdrop-filter: blur(18px) saturate(1.7);
  border: 1px solid rgb(255 255 255 / .32);
  box-shadow: inset 0 1px 0 rgb(255 255 255 / .28),0 24px 50px -20px rgb(0 0 0 / .6);
  animation: ntf-06a-in .55s cubic-bezier(.22,1.2,.36,1) both;
}

.ntf-06a__toast:nth-child(2) {
  animation-delay: .1s;
}

@supports not (backdrop-filter: blur(1px)) {
  .ntf-06a__toast {
    background: rgb(30 28 52 / .92);
  }
}

.ntf-06a__chip {
  flex: none;
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  color: #141327;
  background: oklch(0.85 0.12 160);
}

.ntf-06a__chip--v {
  background: oklch(0.85 0.1 250);
}

.ntf-06a__chip svg {
  width: 18px;
  height: 18px;
}

.ntf-06a__tx {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.ntf-06a__tx b {
  font-size: 14px;
  font-weight: 600;
  color: #fff;
}

.ntf-06a__tx small {
  font-size: 11.5px;
  color: rgb(255 255 255 / .72);
}

.ntf-06a__time {
  margin-left: auto;
  flex: none;
  font-size: 11px;
  font-weight: 600;
  color: rgb(255 255 255 / .6);
}

.ntf-06a__cap {
  font-size: 11.5px;
  text-align: center;
  color: rgb(255 255 255 / .5);
  letter-spacing: .02em;
}

@keyframes ntf-06a-in {
  from {
    opacity: 0;
    translate: 0 18px;
    scale: .96;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-06a__orb {
    animation: none;
  }

  .ntf-06a__toast {
    animation: ntf-06a-rm .2s ease both;
  }

  @keyframes ntf-06a-rm {
    from {
      opacity: 0;
    }
  }
}

.ntf-06b,
.ntf-06b *,
.ntf-06b *::before,
.ntf-06b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-06b {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #20242e;
  font-family: 'Sora','Segoe UI',system-ui,sans-serif;
}

.ntf-06b__photo {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.ntf-06b__stack {
  position: relative;
  width: min(350px,100%);
  display: grid;
  gap: 12px;
}

.ntf-06b__hour {
  font-size: clamp(44px,7vw,60px);
  font-weight: 300;
  letter-spacing: .02em;
  color: #fff;
  text-align: center;
  text-shadow: 0 2px 24px rgb(0 0 0 / .45);
  margin-bottom: 6px;
}

.ntf-06b__toast {
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  border-radius: 18px;
  background: linear-gradient(180deg,rgb(10 12 18 / .34),rgb(10 12 18 / .52));
  -webkit-backdrop-filter: blur(20px) saturate(1.4);
  backdrop-filter: blur(20px) saturate(1.4);
  border: 1px solid rgb(255 255 255 / .18);
  box-shadow: inset 0 1px 0 rgb(255 255 255 / .14),0 20px 44px -20px rgb(0 0 0 / .65);
  animation: ntf-06b-in .55s cubic-bezier(.22,1.2,.36,1) both;
}

.ntf-06b__toast:nth-of-type(2) {
  animation-delay: .1s;
}

@supports not (backdrop-filter: blur(1px)) {
  .ntf-06b__toast {
    background: rgb(14 16 24 / .9);
  }
}

.ntf-06b__app {
  flex: none;
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  border-radius: 11px;
  font-size: 15px;
  font-weight: 700;
  color: #10131c;
  background: var(--a);
}

.ntf-06b__tx {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.ntf-06b__tx b {
  font-size: 13.5px;
  font-weight: 600;
  color: #fff;
  text-shadow: 0 1px 2px rgb(0 0 0 / .3);
}

.ntf-06b__tx small {
  font-size: 11.5px;
  color: rgb(255 255 255 / .78);
}

.ntf-06b__cap {
  margin-top: 4px;
  font-size: 11px;
  line-height: 1.6;
  text-align: center;
  color: rgb(255 255 255 / .85);
  text-shadow: 0 1px 3px rgb(0 0 0 / .6);
  text-wrap: pretty;
}

@keyframes ntf-06b-in {
  from {
    opacity: 0;
    translate: 0 16px;
    scale: .97;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-06b__toast {
    animation: ntf-06b-rm .2s ease both;
  }

  @keyframes ntf-06b-rm {
    from {
      opacity: 0;
    }
  }
}
```

## JavaScript
```js
/* No JavaScript — the orbs drift on infinite alternate keyframes so the glass always has something to refract; backdrop-filter does the rest. */

/* No JavaScript — dark glass (black 34–52% gradient scrim inside the panel) plus blur(20px) keeps white text ≥ AA over any photograph; the image is decorative (empty alt). */
```
