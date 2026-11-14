---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/glassmorphism-profile-info-card/"
title: "Glassmorphism Profile Info Card"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "A social profile card with an animated gradient banner, overlapping avatar, live online indicator, stat grid, skill tags, and a Follow / Message action row —…"
has_js: "true"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Profile Info Card
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/glassmorphism-profile-info-card/

A social profile card with an animated gradient banner, overlapping avatar, live online indicator, stat grid, skill tags, and a Follow / Message action row — all composited on a three-orb animated background.
## HTML
```html
<div class="fg-08">
  <div class="fg-03__bg" aria-hidden="true">
    <div class="fg-03__orb fg-03__orb--1"></div>
    <div class="fg-03__orb fg-03__orb--2"></div>
    <div class="fg-03__orb fg-03__orb--3"></div>
  </div>
  <div class="fg-03__card">
    <div class="fg-03__banner">
      <div class="fg-03__banner-grid"></div>
    </div>
    <div class="fg-03__avatar-wrap">
      <div class="fg-03__avatar" aria-label="Alex Chen">
        <svg width="52" height="60" viewBox="0 0 52 60" fill="none" aria-hidden="true">
          <circle cx="26" cy="20" r="15" fill="rgba(255,255,255,.45)"/>
          <ellipse cx="26" cy="54" rx="24" ry="16" fill="rgba(255,255,255,.35)"/>
        </svg>
      </div>
      <span class="fg-03__online" aria-label="Online"></span>
    </div>
    <div class="fg-03__body">
      <h2 class="fg-03__name">Alex Chen</h2>
      <p class="fg-03__role">Senior UI Designer &amp; Creative Dev</p>
      <p class="fg-03__loc">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
        San Francisco, CA &middot; Joined 2019
      </p>
      <div class="fg-03__stats" role="list">
        <div class="fg-03__stat" role="listitem"><span class="fg-03__stat-n">12.4K</span><span class="fg-03__stat-l">Followers</span></div>
        <div class="fg-03__stat-div" aria-hidden="true"></div>
        <div class="fg-03__stat" role="listitem"><span class="fg-03__stat-n">847</span><span class="fg-03__stat-l">Following</span></div>
        <div class="fg-03__stat-div" aria-hidden="true"></div>
        <div class="fg-03__stat" role="listitem"><span class="fg-03__stat-n">234</span><span class="fg-03__stat-l">Posts</span></div>
      </div>
      <p class="fg-03__bio">Crafting beautiful interfaces &amp; experiences. Obsessed with motion design and pixel perfection. &#127912;</p>
      <div class="fg-03__tags" aria-label="Skills">
        <span>#UI/UX</span><span>#Motion</span><span>#Figma</span><span>#CSS Art</span>
      </div>
      <div class="fg-03__actions">
        <button class="fg-03__btn-follow" id="fg-08-follow">Follow</button>
        <button class="fg-03__btn-msg">Message</button>
        <button class="fg-03__btn-more" aria-label="More options">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="5" cy="12" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="19" cy="12" r="2"/></svg>
        </button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fg-08,
.fg-08 *,
.fg-08 *::before,
.fg-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-08 ::selection {
  background: rgba(147,51,234,.5);
  color: #fff;
}

.fg-08 {
  --c-bg: #0b0b1e;
  --c-o1: #9333ea;
  --c-o2: #db2777;
  --c-o3: #f59e0b;
  --c-glass: rgba(255,255,255,.07);
  --c-border: rgba(255,255,255,.12);
  --c-text: #f0f0ff;
  --c-muted: rgba(240,240,255,.55);
  --t: .25s ease;
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--c-bg);
  position: relative;
  overflow: hidden;
  padding: 40px 20px;
}

.fg-03__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.fg-03__orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
}

.fg-03__orb--1 {
  width: 360px;
  height: 360px;
  background: var(--c-o1);
  opacity: .28;
  top: -80px;
  right: -60px;
  animation: fg-08-o1 22s ease-in-out infinite alternate;
}

.fg-03__orb--2 {
  width: 300px;
  height: 300px;
  background: var(--c-o2);
  opacity: .22;
  bottom: -60px;
  left: -50px;
  animation: fg-08-o2 18s ease-in-out infinite alternate;
}

.fg-03__orb--3 {
  width: 220px;
  height: 220px;
  background: var(--c-o3);
  opacity: .18;
  top: 50%;
  left: 55%;
  animation: fg-08-o3 15s ease-in-out infinite alternate;
}

@keyframes fg-08-o1 {
  to {
    transform: translate(-50px,70px) scale(1.1);
  }
}

@keyframes fg-08-o2 {
  to {
    transform: translate(60px,-60px) scale(1.12);
  }
}

@keyframes fg-08-o3 {
  to {
    transform: translate(-60px,40px) scale(.9);
  }
}

.fg-03__card {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 360px;
  background: var(--c-glass);
  backdrop-filter: blur(24px) saturate(160%);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
  border: 1px solid var(--c-border);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 8px 48px rgba(0,0,0,.5),0 1px 0 rgba(255,255,255,.1) inset;
}

.fg-03__banner {
  height: 110px;
  position: relative;
  background: linear-gradient(135deg,#4f46e5 0%,#9333ea 30%,#db2777 65%,#f59e0b 100%);
  overflow: hidden;
}

.fg-03__banner::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom,transparent 50%,rgba(0,0,0,.35));
  z-index: 1;
}

.fg-03__banner-grid {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(255,255,255,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.07) 1px,transparent 1px);
  background-size: 20px 20px;
}

.fg-03__avatar-wrap {
  position: relative;
  width: -webkit-fit-content;
  width: fit-content;
  margin: -46px 0 0 22px;
  z-index: 2;
}

.fg-03__avatar {
  width: 88px;
  height: 88px;
  border-radius: 50%;
  background: linear-gradient(135deg,#6d28d9,#9333ea,#db2777);
  border: 3px solid rgba(255,255,255,.2);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  box-shadow: 0 0 32px rgba(147,51,234,.45);
}

.fg-03__online {
  position: absolute;
  bottom: 5px;
  right: 3px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #22c55e;
  border: 2.5px solid #0b0b1e;
  animation: fg-08-ping 2s ease infinite;
}

@keyframes fg-08-ping {
  0%,
    100% {
    box-shadow: 0 0 0 0 rgba(34,197,94,.6);
  }

  50% {
    box-shadow: 0 0 0 6px rgba(34,197,94,0);
  }
}

.fg-03__body {
  padding: 12px 22px 22px;
}

.fg-03__name {
  font-size: 20px;
  font-weight: 800;
  color: var(--c-text);
  letter-spacing: -.3px;
  margin-bottom: 2px;
}

.fg-03__role {
  font-size: 12px;
  color: #c084fc;
  font-weight: 600;
  margin-bottom: 6px;
}

.fg-03__loc {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 12px;
  color: var(--c-muted);
  margin-bottom: 14px;
}

.fg-03__stats {
  display: flex;
  align-items: center;
  background: rgba(255,255,255,.05);
  border: 1px solid var(--c-border);
  border-radius: 12px;
  padding: 12px;
  margin-bottom: 12px;
}

.fg-03__stat {
  flex: 1;
  text-align: center;
}

.fg-03__stat-n {
  display: block;
  font-size: 17px;
  font-weight: 800;
  color: var(--c-text);
}

.fg-03__stat-l {
  display: block;
  font-size: 10px;
  color: var(--c-muted);
  letter-spacing: .3px;
  margin-top: 1px;
}

.fg-03__stat-div {
  width: 1px;
  height: 32px;
  background: var(--c-border);
  flex-shrink: 0;
}

.fg-03__bio {
  font-size: 13px;
  color: rgba(240,240,255,.72);
  line-height: 1.6;
  margin-bottom: 12px;
}

.fg-03__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 16px;
}

.fg-03__tags span {
  font-size: 11px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 20px;
  background: rgba(147,51,234,.15);
  border: 1px solid rgba(147,51,234,.3);
  color: #c084fc;
}

.fg-03__actions {
  display: flex;
  gap: 8px;
}

.fg-03__btn-follow {
  flex: 1;
  padding: 11px;
  border: 1px solid transparent;
  border-radius: 10px;
  background: linear-gradient(135deg,var(--c-o1),#6d28d9);
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  transition: transform .15s,box-shadow .2s,background .3s,color .2s,border-color .2s;
  box-shadow: 0 4px 18px rgba(147,51,234,.4);
}

.fg-03__btn-follow:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 24px rgba(147,51,234,.55);
}

.fg-03__btn-follow.is-following {
  background: rgba(255,255,255,.08);
  border-color: var(--c-border);
  color: var(--c-text);
  box-shadow: none;
}

.fg-03__btn-msg {
  flex: 1;
  padding: 11px;
  border: 1px solid var(--c-border);
  border-radius: 10px;
  background: rgba(255,255,255,.07);
  color: var(--c-text);
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: background var(--t);
}

.fg-03__btn-msg:hover {
  background: rgba(255,255,255,.13);
}

.fg-03__btn-more {
  width: 42px;
  padding: 11px;
  border: 1px solid var(--c-border);
  border-radius: 10px;
  background: rgba(255,255,255,.07);
  color: var(--c-text);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background var(--t);
}

.fg-03__btn-more:hover {
  background: rgba(255,255,255,.13);
}

@media (prefers-reduced-motion: reduce) {
  .fg-03__orb,
    .fg-03__online {
    animation: none;
  }

  .fg-03__btn-follow,
    .fg-03__btn-msg,
    .fg-03__btn-more {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var r=document.querySelector('.fg-08');
  if(!r)return;
  var btn=r.querySelector('#fg-08-follow');
  if(!btn)return;
  btn.addEventListener('click',function(){
    var on=btn.classList.toggle('is-following');
    btn.textContent=on?'✓ Following':'Follow';
  });
})();
```
