---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-team-member-card-design/"
title: "Glassmorphism Team Member Card Design"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Two team walls: a three-up grid of photo cards whose glass footer slides up on hover to reveal socials, and a 3D flip roster — front is the portrait, back is…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Team Member Card Design
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-team-member-card-design/

Two team walls: a three-up grid of photo cards whose glass footer slides up on hover to reveal socials, and a 3D flip roster — front is the portrait, back is a frosted bio with links, flipping on hover or keyboard focus.
## HTML
```html
<div class="glz-10-group">
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&display=swap" rel="stylesheet">
<section class="glz-10a" aria-label="Team member cards with slide-up socials">
  <div class="glz-10a__wrap">
    <h2 class="glz-10a__title">The studio</h2>
    <div class="glz-10a__grid">
      <article class="glz-10a__card"><img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=520&auto=format&fit=crop" alt="Portrait of Maya Okafor" loading="lazy"><div class="glz-10a__foot"><b>Maya Okafor</b><em>Principal Designer</em><span class="glz-10a__soc"><a href="#" onclick="return false" aria-label="Maya on X">𝕏</a><a href="#" onclick="return false" aria-label="Maya on Dribbble">◉</a><a href="#" onclick="return false" aria-label="Email Maya">✉</a></span></div></article>
      <article class="glz-10a__card"><img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=520&auto=format&fit=crop" alt="Portrait of Jonas Elm" loading="lazy"><div class="glz-10a__foot"><b>Jonas Elm</b><em>Staff Engineer</em><span class="glz-10a__soc"><a href="#" onclick="return false" aria-label="Jonas on X">𝕏</a><a href="#" onclick="return false" aria-label="Jonas on GitHub">⌥</a><a href="#" onclick="return false" aria-label="Email Jonas">✉</a></span></div></article>
      <article class="glz-10a__card"><img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=520&auto=format&fit=crop" alt="Portrait of Priya Anand" loading="lazy"><div class="glz-10a__foot"><b>Priya Anand</b><em>Design Director</em><span class="glz-10a__soc"><a href="#" onclick="return false" aria-label="Priya on X">𝕏</a><a href="#" onclick="return false" aria-label="Priya on LinkedIn">in</a><a href="#" onclick="return false" aria-label="Email Priya">✉</a></span></div></article>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&display=swap" rel="stylesheet">
<section class="glz-10b" aria-label="Flip card team roster">
  <div class="glz-10b__grid">
    <div class="glz-10b__scene">
      <div class="glz-10b__flip">
        <figure class="glz-10b__face glz-10b__front"><img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=520&auto=format&fit=crop" alt="Portrait of Elena Marsh" loading="lazy"><figcaption><b>Elena Marsh</b><em>Head of Product</em></figcaption></figure>
        <div class="glz-10b__face glz-10b__back"><p>Ex-cartographer. Believes every roadmap is a map that lies a little.</p><a href="#" onclick="return false">[email protected] →</a></div>
      </div>
    </div>
    <div class="glz-10b__scene">
      <div class="glz-10b__flip">
        <figure class="glz-10b__face glz-10b__front"><img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=520&auto=format&fit=crop" alt="Portrait of Sam Whitmore" loading="lazy"><figcaption><b>Sam Whitmore</b><em>Founding Engineer</em></figcaption></figure>
        <div class="glz-10b__face glz-10b__back"><p>Writes CSS like it's 2027 and commit messages like it's poetry night.</p><a href="#" onclick="return false">[email protected] →</a></div>
      </div>
    </div>
  </div>
  <p class="glz-10b__hint" aria-hidden="true">hover or tab to flip</p>
</section>
</div>
```
## CSS
```css
.glz-10-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.glz-10-group > section {
  width: 100%;
}

.glz-10a,
.glz-10a *,
.glz-10a *::before,
.glz-10a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-10a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  background: #0e1018;
  font-family: 'Sora',system-ui,sans-serif;
}

.glz-10a::before {
  content: "";
  position: absolute;
  width: 60vmin;
  height: 60vmin;
  border-radius: 50%;
  background: oklch(0.55 0.18 265);
  filter: blur(100px);
  opacity: .5;
  top: -16%;
  left: 10%;
}

.glz-10a::after {
  content: "";
  position: absolute;
  width: 48vmin;
  height: 48vmin;
  border-radius: 50%;
  background: oklch(0.62 0.15 20);
  filter: blur(100px);
  opacity: .4;
  bottom: -14%;
  right: 8%;
}

.glz-10a__wrap {
  position: relative;
  z-index: 1;
  width: min(920px,100%);
}

.glz-10a__title {
  text-align: center;
  color: #eef0fa;
  font-size: clamp(24px,3.2vw,34px);
  font-weight: 700;
  letter-spacing: -.02em;
  margin-bottom: 34px;
}

.glz-10a__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 20px;
}

.glz-10a__card {
  position: relative;
  aspect-ratio: 3/3.8;
  border-radius: 22px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,.18);
  box-shadow: 0 26px 54px -24px rgba(0,0,0,.75);
  transition: transform .35s ease;
}

.glz-10a__card:hover {
  transform: translateY(-6px);
}

.glz-10a__card img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: #1d2130;
  transition: transform .6s ease;
}

.glz-10a__card:hover img {
  transform: scale(1.05);
}

.glz-10a__foot {
  position: absolute;
  inset: auto 0 0;
  padding: 16px 18px 14px;
  color: #fff;
  background: linear-gradient(180deg,rgba(16,18,30,.25),rgba(16,18,30,.6));
  backdrop-filter: blur(16px) saturate(160%);
  -webkit-backdrop-filter: blur(16px) saturate(160%);
  border-top: 1px solid rgba(255,255,255,.22);
  transform: translateY(46px);
  transition: transform .4s cubic-bezier(.2,.8,.25,1);
}

.glz-10a__card:hover .glz-10a__foot,
.glz-10a__card:focus-within .glz-10a__foot {
  transform: none;
}

.glz-10a__foot b {
  display: block;
  font-size: 15.5px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.glz-10a__foot em {
  display: block;
  font-style: normal;
  font-size: 11.5px;
  color: rgba(255,255,255,.65);
  margin-top: 2px;
}

.glz-10a__soc {
  display: flex;
  gap: 8px;
  margin-top: 12px;
}

.glz-10a__soc a {
  width: 32px;
  height: 32px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  font-size: 13px;
  font-style: normal;
  color: #fff;
  text-decoration: none;
  background: rgba(255,255,255,.12);
  border: 1px solid rgba(255,255,255,.2);
  transition: background .2s ease,transform .2s ease;
}

.glz-10a__soc a:hover {
  background: rgba(255,255,255,.28);
  transform: translateY(-2px);
}

.glz-10a__soc a:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-10a__foot {
    background: rgba(16,18,30,.88);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-10a__card,
    .glz-10a__card img,
    .glz-10a__foot,
    .glz-10a__soc a {
    transition: none;
  }
}

.glz-10b,
.glz-10b *,
.glz-10b *::before,
.glz-10b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-10b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#1a1524,#0d0a14 65%);
  font-family: 'Sora',system-ui,sans-serif;
}

.glz-10b__grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 24px;
}

.glz-10b__scene {
  width: min(250px,80vw);
  aspect-ratio: 3/3.9;
  perspective: 1100px;
}

.glz-10b__flip {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.3,.7,.25,1);
}

.glz-10b__scene:hover .glz-10b__flip,
.glz-10b__scene:focus-within .glz-10b__flip {
  transform: rotateY(180deg);
}

.glz-10b__face {
  position: absolute;
  inset: 0;
  border-radius: 22px;
  overflow: hidden;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  border: 1px solid rgba(255,255,255,.2);
}

.glz-10b__front {
  display: flex;
}

.glz-10b__front img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: #241f33;
  filter: saturate(.9);
}

.glz-10b__front figcaption {
  position: relative;
  margin-top: auto;
  width: 100%;
  padding: 14px 16px;
  color: #fff;
  background: rgba(14,12,22,.45);
  backdrop-filter: blur(14px) saturate(160%);
  -webkit-backdrop-filter: blur(14px) saturate(160%);
  border-top: 1px solid rgba(255,255,255,.2);
}

.glz-10b__front b {
  display: block;
  font-size: 15px;
}

.glz-10b__front em {
  display: block;
  font-style: normal;
  font-size: 11.5px;
  color: rgba(255,255,255,.65);
  margin-top: 2px;
}

.glz-10b__back {
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 16px;
  padding: 24px;
  color: #f1ecfa;
  text-align: center;
  background: linear-gradient(165deg,oklch(0.45 0.16 310/.5),oklch(0.3 0.1 270/.4));
  backdrop-filter: blur(20px) saturate(170%);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.25);
}

.glz-10b__back p {
  font-size: 14px;
  line-height: 1.6;
  text-wrap: pretty;
}

.glz-10b__back a {
  color: oklch(0.85 0.13 310);
  font-weight: 700;
  font-size: 13px;
  text-decoration: none;
}

.glz-10b__back a:hover {
  text-decoration: underline;
}

.glz-10b__back a:focus-visible {
  outline: 2px solid oklch(0.85 0.13 310);
  outline-offset: 3px;
  border-radius: 6px;
}

.glz-10b__hint {
  font-size: 11px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: rgba(220,210,240,.4);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-10b__back {
    background: rgba(40,28,60,.94);
  }

  .glz-10b__front figcaption {
    background: rgba(14,12,22,.85);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-10b__flip {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the footer hides its social row below the card edge via translateY(46px) and slides home on :hover / :focus-within. */

/* No JavaScript — perspective + preserve-3d + backface-visibility flip, triggered by :hover AND :focus-within so the back-face link is keyboard reachable. */
```
