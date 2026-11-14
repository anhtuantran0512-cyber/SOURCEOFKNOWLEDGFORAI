---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/gaming-discord-style-profile-overlay/"
title: "Gaming / Discord Style Profile Overlay"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A dark gaming-style profile with an animated banner, an avatar that overlaps the banner edge, a live presence dot and coloured role chips."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gaming / Discord Style Profile Overlay
Source: https://codefronts.com/components/css-profile-cards/gaming-discord-style-profile-overlay/

A dark gaming-style profile with an animated banner, an avatar that overlaps the banner edge, a live presence dot and coloured role chips.
## HTML
```html
<div class="pc-09">
  <div class="pc-09__card">
    <div class="pc-09__banner"></div>
    <div class="pc-09__avatar">KV<span class="pc-09__presence"></span></div>
    <div class="pc-09__body">
      <div class="pc-09__namerow">
        <h3>kai_void</h3>
        <span class="pc-09__badges"><i title="Boost">&#9889;</i><i title="Verified">&#10004;</i></span>
      </div>
      <p class="pc-09__handle">Kai Voronov</p>
      <div class="pc-09__panel">
        <span class="pc-09__k">Playing</span>
        <p>Cyberpunk 2099 — Night City</p>
      </div>
      <div class="pc-09__roles">
        <span style="--c:#5865f2">Developer</span>
        <span style="--c:#eb459e">Artist</span>
        <span style="--c:#57f287">Moderator</span>
      </div>
      <button class="pc-09__msg">Send Message</button>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-09,
.pc-09 *,
.pc-09 *::before,
.pc-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-09 ::selection {
  background: #5865f2;
  color: #fff;
}

.pc-09 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #1e1f22;
  color: #f2f3f5;
}

.pc-09__card {
  width: 320px;
  border-radius: 18px;
  overflow: hidden;
  background: #111214;
  border: 1px solid #000;
  box-shadow: 0 20px 50px -18px rgba(0,0,0,.9);
}

.pc-09__banner {
  height: 96px;
  background: radial-gradient(circle at 20% 30%,#5865f2,transparent 60%), radial-gradient(circle at 80% 60%,#eb459e,transparent 60%), linear-gradient(120deg,#2b1b52,#3a1140);
  background-size: 200% 200%;
  animation: pc-09-drift 10s ease-in-out infinite;
}

@keyframes pc-09-drift {
  0%,
    100% {
    background-position: 0% 0%;
  }

  50% {
    background-position: 100% 100%;
  }
}

.pc-09__avatar {
  position: relative;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin: -40px 0 0 20px;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.5rem;
  background: linear-gradient(145deg,#5865f2,#eb459e);
  border: 6px solid #111214;
}

.pc-09__presence {
  position: absolute;
  bottom: 2px;
  right: 2px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #57f287;
  border: 4px solid #111214;
}

.pc-09__body {
  padding: 14px 20px 22px;
}

.pc-09__namerow {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.pc-09__namerow h3 {
  font-size: 1.25rem;
  font-weight: 800;
}

.pc-09__badges i {
  font-style: normal;
  font-size: .8rem;
  margin-left: 4px;
  opacity: .8;
}

.pc-09__handle {
  color: #b5bac1;
  font-size: .85rem;
  margin-top: 1px;
}

.pc-09__panel {
  background: #1e1f22;
  border-radius: 10px;
  padding: 12px;
  margin-top: 14px;
}

.pc-09__k {
  font-size: .66rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #949ba4;
  display: block;
  margin-bottom: 5px;
}

.pc-09__panel p {
  font-size: .85rem;
  color: #dbdee1;
}

.pc-09__roles {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin-top: 14px;
}

.pc-09__roles span {
  font-size: .72rem;
  padding: 5px 10px;
  border-radius: 7px;
  color: var(--c);
  background: color-mix(in srgb,var(--c) 14%,transparent);
  border: 1px solid color-mix(in srgb,var(--c) 40%,transparent);
}

.pc-09__msg {
  width: 100%;
  margin-top: 18px;
  padding: 11px;
  border: none;
  border-radius: 9px;
  cursor: pointer;
  font-weight: 700;
  font-size: .86rem;
  color: #fff;
  background: #5865f2;
  transition: background .25s,transform .2s;
}

.pc-09__msg:hover {
  background: #4752c4;
}

.pc-09__msg:active {
  transform: scale(.98);
}

@media (prefers-reduced-motion: reduce) {
  .pc-09 * {
    animation: none!important;
  }
}
```
