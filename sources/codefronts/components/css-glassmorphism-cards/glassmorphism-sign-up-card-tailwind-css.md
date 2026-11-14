---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-sign-up-card-tailwind-css/"
title: "Glassmorphism Sign Up Card Tailwind CSS"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "A signup card whose every style maps to a Tailwind utility (the recipe: bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl shadow-2xl), with a…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Sign Up Card Tailwind CSS
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-sign-up-card-tailwind-css/

A signup card whose every style maps to a Tailwind utility (the recipe: bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl shadow-2xl), with a pattern-driven password strength meter that fills when the password satisfies the regex — plus a compact waitlist variant with an avatar cluster for social proof.
## HTML
```html
<div class="glz-09-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="glz-09a" aria-label="Glassmorphism sign up card demo">
  <form class="glz-09a__card" onsubmit="return false">
    <span class="glz-09a__tw" aria-hidden="true">bg-white/10 backdrop-blur-xl border-white/20</span>
    <h2 class="glz-09a__title">Create your account</h2>
    <label class="glz-09a__lab" for="glz-09a-nm">Full name</label>
    <input id="glz-09a-nm" type="text" placeholder="Ada Lovelace" autocomplete="name" required>
    <label class="glz-09a__lab" for="glz-09a-em">Email</label>
    <input id="glz-09a-em" type="email" placeholder="[email protected]" autocomplete="email" required>
    <label class="glz-09a__lab" for="glz-09a-pw">Password</label>
    <input id="glz-09a-pw" type="password" placeholder="8+ chars, 1 number" autocomplete="new-password" pattern="(?=.*\d)(?=.*[a-zA-Z]).{8,}" required aria-describedby="glz-09a-hint">
    <div class="glz-09a__meter" aria-hidden="true"><i></i><i></i><i></i></div>
    <p class="glz-09a__hint" id="glz-09a-hint"><span class="glz-09a__weak">Needs 8+ characters with a number</span><span class="glz-09a__strong">✓ Strong enough</span></p>
    <button type="submit" class="glz-09a__cta">Sign up free</button>
    <p class="glz-09a__legal">By joining you agree to the <a href="#" onclick="return false">Terms</a>.</p>
  </form>
</section>
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="glz-09b" aria-label="Waitlist signup card demo">
  <form class="glz-09b__card" onsubmit="return false">
    <div class="glz-09b__cluster" aria-hidden="true">
      <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=160&auto=format&fit=crop" alt="" loading="lazy">
      <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=160&auto=format&fit=crop" alt="" loading="lazy">
      <img src="https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?q=80&w=160&auto=format&fit=crop" alt="" loading="lazy">
      <span>+2.4k</span>
    </div>
    <h2>Join the Fielda beta</h2>
    <p class="glz-09b__sub">Design reviews that run themselves. Invites roll out weekly.</p>
    <div class="glz-09b__row">
      <label class="glz-09b__sr" for="glz-09b-em">Email address</label>
      <input id="glz-09b-em" type="email" placeholder="[email protected]" autocomplete="email" required>
      <button type="submit">Get invite</button>
    </div>
    <p class="glz-09b__note">No spam. One email when it's your turn.</p>
  </form>
</section>
</div>
```
## CSS
```css
.glz-09-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-09-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-09a,
.glz-09a *,
.glz-09a *::before,
.glz-09a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-09a {
  --acc: oklch(0.85 0.19 130);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0c1210;
  font-family: 'Outfit',system-ui,sans-serif;
}

.glz-09a::before {
  content: "";
  position: absolute;
  width: 56vmin;
  height: 56vmin;
  border-radius: 50%;
  background: oklch(0.6 0.17 145);
  filter: blur(90px);
  opacity: .5;
  top: -14%;
  right: -4%;
}

.glz-09a::after {
  content: "";
  position: absolute;
  width: 44vmin;
  height: 44vmin;
  border-radius: 50%;
  background: oklch(0.6 0.14 220);
  filter: blur(90px);
  opacity: .45;
  bottom: -12%;
  left: -4%;
}

.glz-09a__card {
  position: relative;
  z-index: 1;
  width: min(380px,100%);
  padding: 32px 30px 26px;
  border-radius: 24px;
  color: #edf5ef;
  display: flex;
  flex-direction: column;
  background: rgba(255,255,255,.1);
  backdrop-filter: blur(24px) saturate(150%);
  -webkit-backdrop-filter: blur(24px) saturate(150%);
  border: 1px solid rgba(255,255,255,.2);
  box-shadow: 0 25px 50px -12px rgba(0,0,0,.6),inset 0 1px 0 rgba(255,255,255,.22);
}

.glz-09a__tw {
  align-self: flex-start;
  font: 500 10px 'JetBrains Mono',monospace;
  letter-spacing: .02em;
  padding: 5px 9px;
  border-radius: 7px;
  color: oklch(0.85 0.19 130);
  background: oklch(0.85 0.19 130/.12);
  border: 1px solid oklch(0.85 0.19 130/.3);
}

.glz-09a__title {
  margin-top: 14px;
  font-size: 23px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.glz-09a__lab {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: rgba(237,245,239,.55);
  margin: 18px 0 7px;
}

.glz-09a__card input {
  padding: 13px 15px;
  font: 500 16px 'Outfit',sans-serif;
  color: #fff;
  border-radius: 13px;
  border: 1px solid rgba(255,255,255,.18);
  background: rgba(255,255,255,.07);
  transition: border-color .2s ease,box-shadow .2s ease;
}

.glz-09a__card input::placeholder {
  color: rgba(237,245,239,.35);
}

.glz-09a__card input:focus-visible {
  outline: none;
  border-color: var(--acc);
  box-shadow: 0 0 0 4px oklch(0.85 0.19 130/.18);
}

.glz-09a__meter {
  display: flex;
  gap: 6px;
  margin-top: 12px;
}

.glz-09a__meter i {
  flex: 1;
  height: 5px;
  border-radius: 99px;
  background: rgba(255,255,255,.14);
  transition: background .35s ease;
}

.glz-09a__card:has(#glz-09a-pw:not(:placeholder-shown)) .glz-09a__meter i:first-child {
  background: oklch(0.75 0.16 70);
}

.glz-09a__card:has(#glz-09a-pw:valid) .glz-09a__meter i {
  background: var(--acc);
}

.glz-09a__hint {
  margin-top: 9px;
  font-size: 12px;
  display: grid;
}

.glz-09a__hint span {
  grid-area: 1/1;
  transition: opacity .3s ease;
}

.glz-09a__weak {
  color: rgba(237,245,239,.5);
}

.glz-09a__strong {
  color: var(--acc);
  font-weight: 700;
  opacity: 0;
}

.glz-09a__card:has(#glz-09a-pw:valid) .glz-09a__weak {
  opacity: 0;
}

.glz-09a__card:has(#glz-09a-pw:valid) .glz-09a__strong {
  opacity: 1;
}

.glz-09a__cta {
  margin-top: 22px;
  padding: 15px;
  border: none;
  border-radius: 14px;
  background: linear-gradient(120deg,oklch(0.85 0.19 130),oklch(0.8 0.15 175));
  color: #08130b;
  font: 800 15px 'Outfit',sans-serif;
  cursor: pointer;
  box-shadow: 0 16px 32px -12px oklch(0.85 0.19 130/.55);
  transition: transform .2s ease,filter .2s ease;
}

.glz-09a__cta:hover {
  transform: translateY(-2px);
  filter: brightness(1.06);
}

.glz-09a__cta:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

.glz-09a__legal {
  margin-top: 14px;
  font-size: 11.5px;
  color: rgba(237,245,239,.45);
  text-align: center;
}

.glz-09a__legal a {
  color: rgba(237,245,239,.75);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-09a__card {
    background: rgba(18,26,22,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-09a__card * {
    transition: none!important;
  }
}

.glz-09b,
.glz-09b *,
.glz-09b *::before,
.glz-09b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-09b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  position: relative;
  overflow: hidden;
  background: linear-gradient(200deg,#141022,#0e0c18);
}

.glz-09b::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(46% 40% at 24% 22%,oklch(0.6 0.23 310/.4),transparent 70%),radial-gradient(40% 36% at 80% 78%,oklch(0.72 0.16 60/.35),transparent 70%);
}

.glz-09b__card {
  position: relative;
  z-index: 1;
  width: min(420px,100%);
  padding: 34px 32px 28px;
  border-radius: 26px;
  text-align: center;
  color: #f2eefc;
  font-family: 'Outfit',system-ui,sans-serif;
  background: linear-gradient(160deg,rgba(255,255,255,.12),rgba(255,255,255,.04));
  backdrop-filter: blur(24px) saturate(170%);
  -webkit-backdrop-filter: blur(24px) saturate(170%);
  border: 1px solid rgba(255,255,255,.2);
  box-shadow: 0 34px 70px -26px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.24);
}

.glz-09b__cluster {
  display: flex;
  justify-content: center;
  align-items: center;
}

.glz-09b__cluster img {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  object-fit: cover;
  border: 2.5px solid #221d33;
  background: #3a3352;
}

.glz-09b__cluster img+img,
.glz-09b__cluster span {
  margin-left: -11px;
}

.glz-09b__cluster span {
  height: 42px;
  padding: 0 13px;
  display: grid;
  place-items: center;
  border-radius: 99px;
  font-size: 12px;
  font-weight: 800;
  color: #1a1428;
  background: linear-gradient(120deg,oklch(0.85 0.12 310),oklch(0.85 0.13 60));
  border: 2.5px solid #221d33;
}

.glz-09b__card h2 {
  margin-top: 18px;
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.glz-09b__sub {
  margin-top: 8px;
  font-size: 14px;
  line-height: 1.5;
  color: rgba(242,238,252,.6);
}

.glz-09b__row {
  display: flex;
  gap: 9px;
  margin-top: 22px;
  padding: 7px;
  border-radius: 16px;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(255,255,255,.16);
  transition: border-color .25s ease,box-shadow .25s ease;
}

.glz-09b__row:focus-within {
  border-color: oklch(0.75 0.18 310);
  box-shadow: 0 0 0 4px oklch(0.75 0.18 310/.2);
}

.glz-09b__row input {
  flex: 1;
  min-width: 0;
  border: none;
  background: transparent;
  padding: 9px 10px;
  font: 500 15px 'Outfit',sans-serif;
  color: #fff;
}

.glz-09b__row input::placeholder {
  color: rgba(242,238,252,.4);
}

.glz-09b__row input:focus-visible {
  outline: none;
}

.glz-09b__row button {
  padding: 12px 18px;
  border: none;
  border-radius: 11px;
  background: linear-gradient(120deg,oklch(0.7 0.21 310),oklch(0.75 0.17 40));
  color: #fff;
  font: 700 13.5px 'Outfit',sans-serif;
  cursor: pointer;
  transition: transform .2s ease,filter .2s ease;
}

.glz-09b__row button:hover {
  transform: translateY(-1px);
  filter: brightness(1.1);
}

.glz-09b__row button:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.glz-09b__note {
  margin-top: 13px;
  font-size: 11.5px;
  color: rgba(242,238,252,.45);
}

.glz-09b__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-09b__card {
    background: rgba(24,19,40,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-09b__row,
    .glz-09b__row button {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the strength meter reads the input's own constraint state: pattern + :valid via :has() fills the bars and swaps the hint. */

/* No JavaScript — the input+button share one glass capsule that glows via :focus-within; the avatar cluster is negative-margin overlap (Tailwind's -ml-3). */
```
