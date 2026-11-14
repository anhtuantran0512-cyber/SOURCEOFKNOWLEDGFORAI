---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/intercom-drift-chat-bubble-floating-button/"
title: "Intercom / Drift Chat Bubble Floating Button"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "The support-launcher pattern used by every SaaS help widget: a persistent bubble in the corner that morphs into a close button when the panel opens, carries…"
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Intercom / Drift Chat Bubble Floating Button
Source: https://codefronts.com/components/css-floating-buttons/intercom-drift-chat-bubble-floating-button/

The support-launcher pattern used by every SaaS help widget: a persistent bubble in the corner that morphs into a close button when the panel opens, carries an unread count, and teases the last agent message once before settling down. Built as a proper disclosure — aria-expanded, aria-controls, Escape to close, and focus returned to the launcher on close.
## HTML
```html
<section class="fb-04" aria-label="Support chat launcher demo">
  <div class="fb-04__page">
    <p class="fb-04__eyebrow">aria-expanded drives the CSS</p>
    <h2 class="fb-04__title">Launcher, teaser, unread count</h2>
    <p class="fb-04__sub">One button, two stacked icons, zero position change. Escape closes the panel and returns focus.</p>
    <p class="fb-04__chip">disclosure pattern · @starting-style · role="status"</p>
  </div>
  <div class="fb-04__dock">
    <div class="fb-04__teaser" id="fb-04-teaser" hidden>
      <span class="fb-04__teaserAv" aria-hidden="true"></span>
      <p class="fb-04__teaserTxt"><b>Priya · Support</b>Hey! Anything I can help you ship today?</p>
      <button class="fb-04__teaserX" type="button" aria-label="Dismiss message preview">×</button>
    </div>
    <div class="fb-04__panel" id="fb-04-panel" role="dialog" aria-label="Support chat" hidden>
      <header class="fb-04__pHead">
        <span class="fb-04__pAv" aria-hidden="true"></span>
        <span class="fb-04__pWho"><b>Priya Raman</b><i>Support · online now</i></span>
      </header>
      <div class="fb-04__log">
        <p class="fb-04__bub fb-04__bub--them">Hey! Anything I can help you ship today?</p>
        <p class="fb-04__bub fb-04__bub--me">Looking for the FAB spacing tokens.</p>
        <p class="fb-04__bub fb-04__bub--them">On it — sending the sheet now <span class="fb-04__typing" aria-hidden="true"><i></i><i></i><i></i></span></p>
      </div>
      <div class="fb-04__quick">
        <button class="fb-04__qBtn" type="button">Pricing</button>
        <button class="fb-04__qBtn" type="button">Docs</button>
        <button class="fb-04__qBtn" type="button">Talk to sales</button>
      </div>
    </div>
    <button class="fb-04__launch" id="fb-04-launch" type="button" aria-expanded="false" aria-controls="fb-04-panel" aria-label="Open support chat">
      <span class="fb-04__ico fb-04__ico--bubble" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M12 3c-4.97 0-9 3.58-9 8 0 2.5 1.29 4.73 3.3 6.2L5.4 21l4.2-2.2c.77.13 1.57.2 2.4.2 4.97 0 9-3.58 9-8s-4.03-8-9-8z" fill="currentColor"/></svg></span>
      <span class="fb-04__ico fb-04__ico--close" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></span>
      <span class="fb-04__badge" id="fb-04-badge" role="status">1</span>
    </button>
  </div>
</section>
```
## CSS
```css
.fb-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-04-bg);
  --fb-04-bg: linear-gradient(180deg,oklch(0.98 0.008 255),oklch(0.93 0.02 255));
  --fb-04-brand: oklch(0.55 0.19 268);
  --fb-04-brandDeep: oklch(0.42 0.17 268);
  --fb-04-ink: oklch(0.24 0.03 265);
  --fb-04-mut: oklch(0.55 0.02 265);
  --fb-04-card: oklch(1 0 0);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-04-ink);
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
  overflow: hidden;
}

.fb-04 *,
.fb-04 *::before,
.fb-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-04__page {
  width: min(100%,54ch);
  display: grid;
  gap: 11px;
  justify-items: center;
  text-align: center;
}

.fb-04__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-04-brand);
}

.fb-04__title {
  font-size: clamp(26px,4.6vw,44px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-04__sub {
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-04-mut);
  text-wrap: pretty;
}

.fb-04__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-04-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.24 0.03 265/.14);
  border-radius: 99px;
}

.fb-04__dock {
  position: absolute;
  right: clamp(16px,3vw,30px);
  bottom: calc(clamp(16px,3vw,30px) + env(safe-area-inset-bottom));
  z-index: 6;
  display: grid;
  justify-items: end;
  gap: 12px;
}

.fb-04__launch {
  position: relative;
  justify-self: end;
  display: grid;
  place-items: center;
  inline-size: 60px;
  block-size: 60px;
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  color: oklch(0.99 0.01 268);
  background: radial-gradient(120% 120% at 30% 20%,oklch(0.66 0.19 275),var(--fb-04-brandDeep));
  box-shadow: 0 10px 28px -8px oklch(0.42 0.17 268/.75),0 2px 6px oklch(0.3 0.1 268/.3);
  transition: transform .26s cubic-bezier(.2,1.3,.4,1),box-shadow .26s ease;
}

.fb-04__launch:hover {
  transform: translateY(-2px) scale(1.04);
}

.fb-04__launch:active {
  transform: scale(.94);
}

.fb-04__launch:focus-visible {
  outline: 3px solid var(--fb-04-brandDeep);
  outline-offset: 4px;
}

.fb-04__ico {
  grid-area: 1/1;
  display: grid;
  place-items: center;
  transition: opacity .22s ease,rotate .34s cubic-bezier(.3,1.4,.4,1),scale .3s ease;
}

.fb-04__ico svg {
  width: 27px;
  height: 27px;
}

.fb-04__ico--close {
  opacity: 0;
  rotate: 90deg;
  scale: .7;
}

.fb-04__launch[aria-expanded="true"] .fb-04__ico--bubble {
  opacity: 0;
  rotate: -90deg;
  scale: .7;
}

.fb-04__launch[aria-expanded="true"] .fb-04__ico--close {
  opacity: 1;
  rotate: 0deg;
  scale: 1;
}

.fb-04__badge {
  position: absolute;
  top: -2px;
  right: -2px;
  min-width: 22px;
  height: 22px;
  padding: 0 6px;
  border-radius: 99px;
  background: oklch(0.62 0.22 25);
  color: oklch(0.99 0.01 25);
  font-size: 12px;
  font-weight: 700;
  line-height: 22px;
  box-shadow: 0 0 0 3px oklch(0.96 0.01 255);
  font-variant-numeric: tabular-nums;
}

.fb-04__launch[aria-expanded="true"] .fb-04__badge {
  opacity: 0;
  scale: .5;
  transition: opacity .18s,scale .18s;
}

.fb-04__teaser {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  width: min(78vw,282px);
  padding: 12px 13px;
  border-radius: 18px 18px 6px 18px;
  background: var(--fb-04-card);
  box-shadow: 0 14px 40px -18px oklch(0.24 0.03 265/.6),0 1px 2px oklch(0.24 0.03 265/.12);
  transition: opacity .3s ease,translate .3s cubic-bezier(.2,.9,.3,1),display .3s allow-discrete;
  opacity: 1;
  translate: 0 0;
}

.fb-04__teaser[hidden] {
  display: none;
}

@starting-style {
  .fb-04__teaser {
    opacity: 0;
    translate: 0 12px;
  }
}

.fb-04__teaserAv,
.fb-04__pAv {
  flex: none;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: linear-gradient(140deg,oklch(0.7 0.12 30),oklch(0.5 0.14 320)),url("https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=200&auto=format&fit=crop") center/cover;
}

.fb-04__teaserTxt {
  font-size: 12.8px;
  line-height: 1.45;
  color: var(--fb-04-ink);
  display: grid;
  gap: 2px;
}

.fb-04__teaserTxt b {
  font-size: 11.5px;
  color: var(--fb-04-brand);
}

.fb-04__teaserX {
  flex: none;
  width: 24px;
  height: 24px;
  border: 0;
  border-radius: 50%;
  background: transparent;
  color: var(--fb-04-mut);
  font-size: 17px;
  line-height: 1;
  cursor: pointer;
}

.fb-04__teaserX:hover {
  background: oklch(0.24 0.03 265/.07);
}

.fb-04__teaserX:focus-visible {
  outline: 2px solid var(--fb-04-brand);
  outline-offset: 2px;
}

.fb-04__panel {
  width: min(88vw,340px);
  border-radius: 20px;
  overflow: hidden;
  background: var(--fb-04-card);
  box-shadow: 0 30px 70px -24px oklch(0.24 0.03 265/.55),0 1px 3px oklch(0.24 0.03 265/.14);
  transform-origin: 100% 100%;
  transition: opacity .26s ease,scale .3s cubic-bezier(.2,1.1,.3,1),translate .3s ease,display .3s allow-discrete;
  opacity: 1;
  scale: 1;
  translate: 0 0;
}

.fb-04__panel[hidden] {
  display: none;
}

@starting-style {
  .fb-04__panel {
    opacity: 0;
    scale: .9;
    translate: 0 16px;
  }
}

.fb-04__pHead {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 15px 17px;
  background: linear-gradient(120deg,var(--fb-04-brandDeep),oklch(0.5 0.2 300));
  color: oklch(0.99 0.01 268);
}

.fb-04__pWho {
  display: grid;
  gap: 1px;
}

.fb-04__pWho b {
  font-size: 14.5px;
  font-weight: 650;
}

.fb-04__pWho i {
  font-style: normal;
  font-size: 11.5px;
  opacity: .82;
}

.fb-04__log {
  display: grid;
  gap: 9px;
  padding: 16px;
  background: oklch(0.98 0.005 265);
}

.fb-04__bub {
  max-width: 82%;
  padding: 10px 13px;
  border-radius: 16px;
  font-size: 13px;
  line-height: 1.5;
}

.fb-04__bub--them {
  justify-self: start;
  background: oklch(0.94 0.01 265);
  border-bottom-left-radius: 5px;
}

.fb-04__bub--me {
  justify-self: end;
  background: var(--fb-04-brand);
  color: oklch(0.99 0.01 268);
  border-bottom-right-radius: 5px;
}

.fb-04__typing {
  display: inline-flex;
  gap: 3px;
  margin-left: 4px;
  vertical-align: middle;
}

.fb-04__typing i {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: currentColor;
  opacity: .45;
  animation: fb-04-bounce 1.1s ease-in-out infinite;
}

.fb-04__typing i:nth-child(2) {
  animation-delay: .15s;
}

.fb-04__typing i:nth-child(3) {
  animation-delay: .3s;
}

@keyframes fb-04-bounce {
  0%,
    100% {
    transform: translateY(0);
    opacity: .35;
  }

  50% {
    transform: translateY(-4px);
    opacity: .9;
  }
}

.fb-04__quick {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  padding: 12px 16px 16px;
  background: oklch(0.98 0.005 265);
}

.fb-04__qBtn {
  min-height: 36px;
  padding: 0 14px;
  border-radius: 99px;
  border: 1px solid oklch(0.55 0.19 268/.3);
  background: transparent;
  color: var(--fb-04-brandDeep);
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease,transform .18s ease;
}

.fb-04__qBtn:hover {
  background: oklch(0.55 0.19 268/.1);
}

.fb-04__qBtn:active {
  transform: scale(.96);
}

.fb-04__qBtn:focus-visible {
  outline: 2px solid var(--fb-04-brand);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .fb-04 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const launch = document.getElementById('fb-04-launch');
  const panel = document.getElementById('fb-04-panel');
  const teaser = document.getElementById('fb-04-teaser');
  const badge = document.getElementById('fb-04-badge');
  if (!launch || !panel || launch.dataset.fbWired) return;
  launch.dataset.fbWired = '1';
  const setOpen = (open) => {
    launch.setAttribute('aria-expanded', String(open));
    launch.setAttribute('aria-label', open ? 'Close support chat' : 'Open support chat');
    panel.hidden = !open;
    if (open) { teaser.hidden = true; badge.textContent = '0'; badge.hidden = true; }
  };
  launch.addEventListener('click', () => setOpen(launch.getAttribute('aria-expanded') !== 'true'));
  teaser.querySelector('.fb-04__teaserX').addEventListener('click', () => { teaser.hidden = true; });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && launch.getAttribute('aria-expanded') === 'true') { setOpen(false); launch.focus(); }
  });
  setTimeout(() => { if (launch.getAttribute('aria-expanded') !== 'true') teaser.hidden = false; }, 2200);
  setTimeout(() => { teaser.hidden = true; }, 11000);
})();
```
