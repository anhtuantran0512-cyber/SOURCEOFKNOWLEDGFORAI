---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/creator-link-in-bio-mobile-profile-card/"
title: "Creator Link-in-Bio Mobile Profile Card"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A mobile-first Linktree-style card with a centred avatar, short bio, vertically stacked link buttons that stagger in, and a row of social icons."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Creator Link-in-Bio Mobile Profile Card
Source: https://codefronts.com/components/css-profile-cards/creator-link-in-bio-mobile-profile-card/

A mobile-first Linktree-style card with a centred avatar, short bio, vertically stacked link buttons that stagger in, and a row of social icons.
## HTML
```html
<div class="pc-18">
  <div class="pc-18__phone">
    <div class="pc-18__card">
      <div class="pc-18__pfp">ZW</div>
      <h3>Zoe Winters</h3>
      <p class="pc-18__handle">@zoemakes</p>
      <p class="pc-18__bio">Illustrator &#183; Zine maker &#183; Coffee &#9749;</p>
      <div class="pc-18__links">
        <a class="pc-18__link" style="--i:0"><span>&#127912;</span>My Portfolio</a>
        <a class="pc-18__link" style="--i:1"><span>&#128214;</span>Latest Zine Drop</a>
        <a class="pc-18__link" style="--i:2"><span>&#127909;</span>YouTube Process</a>
        <a class="pc-18__link" style="--i:3"><span>&#9749;</span>Buy me a coffee</a>
      </div>
      <div class="pc-18__socials">
        <a aria-label="Instagram">&#9673;</a>
        <a aria-label="Twitter">&#120143;</a>
        <a aria-label="TikTok">&#9834;</a>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-18,
.pc-18 *,
.pc-18 *::before,
.pc-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-18 ::selection {
  background: #ff5da2;
  color: #fff;
}

.pc-18 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  background: #120a14;
  color: #fff;
}

.pc-18__phone {
  width: 300px;
  border-radius: 34px;
  padding: 26px 20px 30px;
  text-align: center;
  background: radial-gradient(400px 200px at 50% 0%,rgba(255,93,162,.35),transparent 60%), linear-gradient(180deg,#1e1122,#160c18);
  border: 1px solid rgba(255,255,255,.08);
  box-shadow: 0 30px 70px -26px rgba(0,0,0,.85);
}

.pc-18__pfp {
  width: 82px;
  height: 82px;
  border-radius: 50%;
  margin: 6px auto 14px;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.5rem;
  color: #fff;
  background: linear-gradient(145deg,#ff5da2,#a855f7);
  box-shadow: 0 0 0 4px rgba(255,255,255,.06),0 12px 30px -10px #ff5da2;
}

.pc-18__phone h3 {
  font-size: 1.3rem;
  font-weight: 800;
}

.pc-18__handle {
  color: #c79fd6;
  font-size: .85rem;
  margin-top: 2px;
}

.pc-18__bio {
  font-size: .82rem;
  color: rgba(255,255,255,.7);
  margin-top: 10px;
}

.pc-18__links {
  display: flex;
  flex-direction: column;
  gap: 11px;
  margin-top: 22px;
}

.pc-18__link {
  display: flex;
  align-items: center;
  gap: 12px;
  justify-content: center;
  padding: 14px;
  border-radius: 16px;
  cursor: pointer;
  font-weight: 600;
  font-size: .9rem;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.12);
  animation: pc-18-in .5s ease both;
  animation-delay: calc(var(--i) * .1s + .1s);
  transition: transform .2s,background .25s,border-color .25s;
}

@keyframes pc-18-in {
  from {
    opacity: 0;
    transform: translateY(14px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.pc-18__link span {
  font-size: 1.05rem;
}

.pc-18__link:hover {
  transform: scale(1.03);
  background: rgba(255,93,162,.16);
  border-color: rgba(255,93,162,.5);
}

.pc-18__socials {
  display: flex;
  justify-content: center;
  gap: 16px;
  margin-top: 22px;
}

.pc-18__socials a {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  cursor: pointer;
  font-size: 1.05rem;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.1);
  transition: background .25s;
}

.pc-18__socials a:hover {
  background: rgba(255,255,255,.16);
}

@media (prefers-reduced-motion: reduce) {
  .pc-18 * {
    animation: none!important;
  }

  .pc-18__link {
    opacity: 1;
  }
}
```
