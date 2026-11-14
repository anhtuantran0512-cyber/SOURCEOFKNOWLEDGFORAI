---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/bento-grid-profile-card/"
title: "Bento Grid Profile Card"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "An asymmetric bento-box profile layout where avatar, bio, skill tags, local time and stats each live in their own modular quadrant with layered ambient shadows."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bento Grid Profile Card
Source: https://codefronts.com/components/css-profile-cards/bento-grid-profile-card/

An asymmetric bento-box profile layout where avatar, bio, skill tags, local time and stats each live in their own modular quadrant with layered ambient shadows.
## HTML
```html
<div class="pc-01">
  <div class="pc-01__card">
    <div class="pc-01__tile pc-01__hero">
      <div class="pc-01__avatar"><span>AR</span></div>
      <div class="pc-01__id">
        <h3>Ava Reyes</h3>
        <p>Product Designer</p>
      </div>
      <span class="pc-01__status"><i></i>Available</span>
    </div>
    <div class="pc-01__tile pc-01__bio">
      <span class="pc-01__k">About</span>
      <p>Designing calm interfaces for complex data. Ex-Figma, now building tools for makers.</p>
    </div>
    <div class="pc-01__tile pc-01__stat">
      <strong>128</strong><span>Projects</span>
    </div>
    <div class="pc-01__tile pc-01__stat pc-01__stat--b">
      <strong>4.9</strong><span>Rating</span>
    </div>
    <div class="pc-01__tile pc-01__skills">
      <span class="pc-01__k">Stack</span>
      <div class="pc-01__chips">
        <em>Figma</em><em>OKLCH</em><em>Motion</em><em>Rust</em>
      </div>
    </div>
    <div class="pc-01__tile pc-01__time">
      <span class="pc-01__k">Local</span>
      <strong>09:41</strong><span>Lisbon · GMT</span>
    </div>
    <div class="pc-01__tile pc-01__cta">
      <button>Follow</button>
      <button class="pc-01__ghost">Message</button>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-01,
.pc-01 *,
.pc-01 *::before,
.pc-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-01 ::selection {
  background: oklch(0.7 0.2 275);
  color: #fff;
}

.pc-01 {
  --base: oklch(0.62 0.2 275);
  --bg: #0a0a0f;
  --surface: color-mix(in oklch, var(--base) 10%, #14141c);
  --surface2: color-mix(in oklch, var(--base) 18%, #16161f);
  --line: color-mix(in oklch, var(--base) 24%, transparent);
  --ink: #f4f3f8;
  --dim: color-mix(in oklch, var(--ink) 55%, transparent);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  color: var(--ink);
}

.pc-01__card {
  container-type: inline-size;
  width: 100%;
  max-width: 520px;
  display: grid;
  grid-template-columns: repeat(4,1fr);
  grid-auto-rows: minmax(64px,auto);
  gap: 12px;
}

.pc-01__tile {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 18px;
  box-shadow: 0 1px 2px rgba(0,0,0,.4),0 12px 30px -12px rgba(0,0,0,.6);
  transition: transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s;
}

.pc-01__tile:hover {
  transform: translateY(-4px);
  box-shadow: 0 2px 4px rgba(0,0,0,.5),0 22px 44px -14px color-mix(in oklch,var(--base) 40%,black);
}

.pc-01__k {
  font-size: 10px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--dim);
  display: block;
  margin-bottom: 8px;
}

.pc-01__hero {
  grid-column: span 2;
  grid-row: span 2;
  background: var(--surface2);
  display: flex;
  flex-direction: column;
  gap: 14px;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.pc-01__hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(120px 120px at 80% 0%,color-mix(in oklch,var(--base) 40%,transparent),transparent 70%);
  pointer-events: none;
}

.pc-01__avatar {
  width: 76px;
  height: 76px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  position: relative;
  background: var(--surface);
  font-weight: 800;
  font-size: 1.4rem;
  letter-spacing: .04em;
}

.pc-01__avatar::before {
  content: '';
  position: absolute;
  inset: -3px;
  border-radius: 50%;
  z-index: -1;
  background: conic-gradient(from 180deg,var(--base),oklch(0.7 0.2 200),oklch(0.75 0.2 330),var(--base));
}

.pc-01__id h3 {
  font-size: 1.25rem;
  font-weight: 800;
  letter-spacing: -.01em;
}

.pc-01__id p {
  color: var(--dim);
  font-size: .9rem;
  margin-top: 2px;
}

.pc-01__status {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: .8rem;
  color: var(--dim);
  width: fit-content;
}

.pc-01__status i {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: oklch(0.78 0.19 150);
  box-shadow: 0 0 10px oklch(0.78 0.19 150);
  animation: pc-01-blink 2.4s ease-in-out infinite;
}

@keyframes pc-01-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .35;
  }
}

.pc-01__bio {
  grid-column: span 2;
}

.pc-01__bio p {
  font-size: .86rem;
  line-height: 1.5;
  color: color-mix(in oklch,var(--ink) 82%,transparent);
  text-wrap: balance;
}

.pc-01__stat {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  gap: 2px;
}

.pc-01__stat strong {
  font-size: 1.6rem;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.pc-01__stat span {
  font-size: .72rem;
  color: var(--dim);
  letter-spacing: .04em;
}

.pc-01__stat--b strong {
  background: linear-gradient(90deg,var(--base),oklch(0.8 0.18 330));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.pc-01__skills {
  grid-column: span 2;
}

.pc-01__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.pc-01__chips em {
  font-style: normal;
  font-size: .74rem;
  padding: 5px 10px;
  border-radius: 9px;
  background: color-mix(in oklch,var(--base) 16%,transparent);
  border: 1px solid var(--line);
  color: color-mix(in oklch,var(--ink) 88%,transparent);
}

.pc-01__time {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.pc-01__time strong {
  font-size: 1.35rem;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.pc-01__time span:last-child {
  font-size: .68rem;
  color: var(--dim);
  margin-top: 2px;
}

.pc-01__cta {
  grid-column: span 2;
  display: flex;
  gap: 8px;
  align-items: center;
}

.pc-01__cta button {
  flex: 1;
  padding: 11px;
  border: none;
  border-radius: 12px;
  font-weight: 700;
  font-size: .85rem;
  cursor: pointer;
  background: var(--base);
  color: #0a0a0f;
  transition: filter .25s,transform .2s;
}

.pc-01__cta button:hover {
  filter: brightness(1.12);
}

.pc-01__cta button:active {
  transform: scale(.97);
}

.pc-01__ghost {
  background: transparent!important;
  color: var(--ink)!important;
  border: 1px solid var(--line)!important;
}

@container (max-width: 420px) {
  .pc-01__card {
    grid-template-columns: repeat(2,1fr);
  }

  .pc-01__hero {
    grid-column: span 2;
    grid-row: auto;
  }

  .pc-01__bio,
    .pc-01__skills,
    .pc-01__cta {
    grid-column: span 2;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pc-01 * {
    animation: none!important;
    transition: none!important;
  }
}
```
