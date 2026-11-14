---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-avatar-notification-badge/"
title: "CSS Avatar Notification Badge"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "The avatar badge without the white-ring hack: a mask-image radial cutout punches a true transparent gap between avatar and status dot (proven live over a…"
has_js: "false"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Avatar Notification Badge
Source: https://codefronts.com/snippets/css-notifications/css-avatar-notification-badge/

The avatar badge without the white-ring hack: a mask-image radial cutout punches a true transparent gap between avatar and status dot (proven live over a shifting gradient), with a radio-driven online/busy/away switcher — and a facepile where negative-margin avatars ring themselves with the same mask trick and a +3 pill absorbs the overflow.
## HTML
```html
<div class="ntf-11-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-11a" aria-label="Avatar status badge with true masked cutout">
  <div class="ntf-11a__card">
    <div class="ntf-11a__stage">
      <span class="ntf-11a__avatar">
        <img src="https://i.pravatar.cc/96?img=47" alt="Amara Okafor" width="72" height="72">
        <i class="ntf-11a__badge" aria-hidden="true"></i>
      </span>
      <span class="ntf-11a__who"><b>Amara Okafor</b><small class="ntf-11a__state"></small></span>
    </div>
    <fieldset class="ntf-11a__set">
      <legend class="ntf-11a__legend">Status</legend>
      <label class="ntf-11a__opt"><input type="radio" name="ntf-11a" value="online" checked><span>Online</span></label>
      <label class="ntf-11a__opt"><input type="radio" name="ntf-11a" value="busy"><span>Busy</span></label>
      <label class="ntf-11a__opt"><input type="radio" name="ntf-11a" value="away"><span>Away</span></label>
    </fieldset>
    <p class="ntf-11a__cap">The gap is a <b>real hole</b> — a mask-image cutout, not a painted border — so it stays perfect over this drifting gradient.</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-11b" aria-label="Overlapping avatar group with unread count">
  <div class="ntf-11b__card">
    <h2 class="ntf-11b__title">Design sync</h2>
    <p class="ntf-11b__sub">Thu 14:00 · #design-crit</p>
    <div class="ntf-11b__row">
      <div class="ntf-11b__pile">
        <img class="ntf-11b__face" src="https://i.pravatar.cc/72?img=32" alt="Priya" width="44" height="44">
        <img class="ntf-11b__face" src="https://i.pravatar.cc/72?img=12" alt="Marcus" width="44" height="44">
        <img class="ntf-11b__face" src="https://i.pravatar.cc/72?img=56" alt="Elena" width="44" height="44">
        <img class="ntf-11b__face" src="https://i.pravatar.cc/72?img=8" alt="Tom" width="44" height="44">
        <span class="ntf-11b__more" aria-label="3 more attendees">+3</span>
      </div>
      <span class="ntf-11b__unread" aria-label="5 unread messages in this thread">5<small> unread</small></span>
    </div>
    <p class="ntf-11b__cap">Each avatar masks a crescent where its neighbor overlaps — the “ring” is transparent, so it works on this card, on hover tints, anywhere.</p>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-11-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-11-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-11a,
.ntf-11a *,
.ntf-11a *::before,
.ntf-11a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-11a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #101318;
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-11a__card {
  width: min(400px,100%);
  padding: 26px;
  border-radius: 20px;
  border: 1px solid rgba(170,190,225,.16);
  background: linear-gradient(120deg,oklch(0.45 0.13 300),oklch(0.5 0.14 220),oklch(0.48 0.13 160));
  background-size: 250% 250%;
  animation: ntf-11a-bg 9s ease-in-out infinite alternate;
  box-shadow: 0 30px 70px -35px rgba(0,0,0,.9);
}

@keyframes ntf-11a-bg {
  from {
    background-position: 0% 40%;
  }

  to {
    background-position: 100% 60%;
  }
}

.ntf-11a__stage {
  display: flex;
  align-items: center;
  gap: 16px;
}

.ntf-11a__avatar {
  position: relative;
  flex: none;
  width: 72px;
  height: 72px;
}

.ntf-11a__avatar img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  display: block;
  background: #2a2f3a;
  -webkit-mask-image: radial-gradient(circle 12px at calc(100% - 9px) calc(100% - 9px),transparent 96%,#000 100%);
  mask-image: radial-gradient(circle 12px at calc(100% - 9px) calc(100% - 9px),transparent 96%,#000 100%);
}

.ntf-11a__badge {
  position: absolute;
  inset-inline-end: 0;
  bottom: 0;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: oklch(0.75 0.17 155);
  display: grid;
  place-items: center;
  transition: background .25s;
}

.ntf-11a__badge::after {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: rgba(255,255,255,.0);
  transition: all .25s;
}

.ntf-11a:has(input[value=busy]:checked) .ntf-11a__badge {
  background: oklch(0.62 0.21 25);
}

.ntf-11a:has(input[value=busy]:checked) .ntf-11a__badge::after {
  width: 8px;
  height: 2.5px;
  border-radius: 2px;
  background: #fff;
}

.ntf-11a:has(input[value=away]:checked) .ntf-11a__badge {
  background: oklch(0.82 0.14 85);
}

.ntf-11a:has(input[value=away]:checked) .ntf-11a__badge::after {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: transparent;
  box-shadow: inset 3px -2px 0 0 #fff;
}

.ntf-11a__who {
  display: grid;
  gap: 2px;
}

.ntf-11a__who b {
  font-size: 16.5px;
  font-weight: 600;
  color: #fff;
  text-shadow: 0 1px 3px rgb(0 0 0 / .3);
}

.ntf-11a__state {
  font-size: 12.5px;
  color: rgb(255 255 255 / .8);
}

.ntf-11a__state::after {
  content: "online — in a huddle";
}

.ntf-11a:has(input[value=busy]:checked) .ntf-11a__state::after {
  content: "busy — do not disturb";
}

.ntf-11a:has(input[value=away]:checked) .ntf-11a__state::after {
  content: "away — back at 14:00";
}

.ntf-11a__set {
  margin-top: 20px;
  display: flex;
  gap: 6px;
  border: 0;
  background: rgb(0 0 0 / .25);
  padding: 5px;
  border-radius: 12px;
}

.ntf-11a__legend {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.ntf-11a__opt {
  flex: 1;
}

.ntf-11a__opt input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.ntf-11a__opt span {
  display: block;
  text-align: center;
  padding: 9px 0;
  border-radius: 9px;
  font-size: 12.5px;
  font-weight: 600;
  color: rgb(255 255 255 / .75);
  cursor: pointer;
  transition: background .2s,color .2s;
}

.ntf-11a__opt:has(input:checked) span {
  background: rgb(255 255 255 / .92);
  color: #14171d;
}

.ntf-11a__opt:has(input:focus-visible) span {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.ntf-11a__cap {
  margin-top: 16px;
  font-size: 11.5px;
  line-height: 1.6;
  color: rgb(255 255 255 / .75);
  text-wrap: pretty;
}

.ntf-11a__cap b {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-11a__card {
    animation: none;
  }
}

.ntf-11b,
.ntf-11b *,
.ntf-11b *::before,
.ntf-11b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-11b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f4f5f8,#e9ebf0);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-11b__card {
  width: min(390px,100%);
  padding: 26px;
  border-radius: 20px;
  background: #fff;
  border: 1px solid rgba(29,33,43,.1);
  box-shadow: 0 26px 60px -34px rgba(29,33,43,.5);
  transition: background .2s;
}

.ntf-11b__card:hover {
  background: #fafbff;
}

.ntf-11b__title {
  font-size: 19px;
  font-weight: 600;
  letter-spacing: -.01em;
  color: #1d212b;
}

.ntf-11b__sub {
  margin-top: 2px;
  font-size: 12.5px;
  color: rgba(29,33,43,.5);
}

.ntf-11b__row {
  margin-top: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
}

.ntf-11b__pile {
  display: flex;
  align-items: center;
}

.ntf-11b__face {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  display: block;
  background: #d7dbe4;
}

.ntf-11b__face+.ntf-11b__face,
.ntf-11b__more {
  margin-inline-start: -11px;
}

.ntf-11b__face+.ntf-11b__face {
  -webkit-mask-image: radial-gradient(circle 25px at -12px 50%,transparent 96%,#000 100%);
  mask-image: radial-gradient(circle 25px at -12px 50%,transparent 96%,#000 100%);
}

.ntf-11b__more {
  position: relative;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 12.5px;
  font-weight: 700;
  color: #1d212b;
  background: #e8ebf2;
  -webkit-mask-image: radial-gradient(circle 25px at -12px 50%,transparent 96%,#000 100%);
  mask-image: radial-gradient(circle 25px at -12px 50%,transparent 96%,#000 100%);
}

.ntf-11b__unread {
  flex: none;
  display: flex;
  align-items: baseline;
  gap: 4px;
  padding: 8px 14px;
  border-radius: 999px;
  font-size: 15px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: #fff;
  background: oklch(0.63 0.21 25);
  box-shadow: 0 10px 20px -10px oklch(0.63 0.21 25 / .7);
  animation: ntf-11b-in .5s cubic-bezier(.22,1.4,.36,1) both .2s;
}

.ntf-11b__unread small {
  font-size: 11px;
  font-weight: 600;
  opacity: .85;
}

@keyframes ntf-11b-in {
  from {
    opacity: 0;
    scale: .6;
  }
}

.ntf-11b__cap {
  margin-top: 18px;
  font-size: 11.5px;
  line-height: 1.6;
  color: rgba(29,33,43,.45);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-11b__unread {
    animation: ntf-11b-rm .2s ease both;
  }

  @keyframes ntf-11b-rm {
    from {
      opacity: 0;
    }
  }
}
```

## JavaScript
```js
/* No JavaScript — the radio group is the state machine: :has(input[value=…]:checked) recolors the badge, reshapes its glyph (dash for busy, moon for away) and swaps the status line, while the mask cutout stays put. */

/* No JavaScript — the facepile is flexbox with -11px overlaps; every avatar after the first masks a crescent at its inline-start, so the separation ring is genuinely transparent rather than painted white. */
```
