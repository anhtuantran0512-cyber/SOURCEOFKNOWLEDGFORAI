---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/dark-mode-toggle-team-card/"
title: "Dark Mode Toggle Team Card"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A profile card with an in-card theme switch that flips every colour token between a light and dark palette using only a checkbox and CSS variables."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Toggle Team Card
Source: https://codefronts.com/components/css-profile-cards/dark-mode-toggle-team-card/

A profile card with an in-card theme switch that flips every colour token between a light and dark palette using only a checkbox and CSS variables.
## HTML
```html
<div class="pc-05">
  <label class="pc-05__wrap">
    <input type="checkbox" class="pc-05__toggle" checked>
    <div class="pc-05__card">
      <button class="pc-05__switch" aria-label="Toggle theme">
        <span class="pc-05__knob"></span>
      </button>
      <div class="pc-05__pfp">SC</div>
      <h3>Sora Chen</h3>
      <p class="pc-05__role">iOS Engineer</p>
      <p class="pc-05__bio">Ships pixel-perfect apps. Adapts to your system theme automatically.</p>
      <div class="pc-05__row">
        <div class="pc-05__stat"><b>56</b><span>Apps</span></div>
        <div class="pc-05__stat"><b>2.1M</b><span>Installs</span></div>
        <div class="pc-05__stat"><b>4.8</b><span>Stars</span></div>
      </div>
      <button class="pc-05__cta">View Profile</button>
    </div>
  </label>
</div>
```
## CSS
```css
.pc-05,
.pc-05 *,
.pc-05 *::before,
.pc-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-05 ::selection {
  background: #6c8cff;
  color: #fff;
}

.pc-05 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #1a1c22;
}

.pc-05__toggle {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.pc-05__wrap {
  cursor: default;
}

.pc-05__card {
  --bg: #f4f5f9;
  --surface: #fff;
  --ink: #141620;
  --dim: #6a7080;
  --line: #e2e5ee;
  --accent: #5a6cff;
  width: 300px;
  border-radius: 24px;
  padding: 28px;
  text-align: center;
  background: var(--surface);
  color: var(--ink);
  border: 1px solid var(--line);
  box-shadow: 0 24px 60px -24px rgba(0,0,0,.5);
  transition: background .5s,color .5s,border-color .5s;
  position: relative;
}

.pc-05__toggle:checked ~ .pc-05__card {
  --bg: #0d1117;
  --surface: #161b22;
  --ink: #e6edf3;
  --dim: #8b949e;
  --line: #232a33;
  --accent: #7c8cff;
}

.pc-05__switch {
  position: absolute;
  top: 18px;
  right: 18px;
  width: 50px;
  height: 27px;
  border-radius: 20px;
  cursor: pointer;
  border: 1px solid var(--line);
  background: var(--bg);
  transition: background .5s;
  padding: 0;
}

.pc-05__knob {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 21px;
  height: 21px;
  border-radius: 50%;
  background: var(--accent);
  transition: transform .4s cubic-bezier(.4,1.4,.5,1);
  box-shadow: 0 2px 6px rgba(0,0,0,.3);
}

.pc-05__toggle:checked ~ .pc-05__card .pc-05__knob {
  transform: translateX(23px);
}

.pc-05__pfp {
  width: 80px;
  height: 80px;
  border-radius: 24px;
  margin: 8px auto 16px;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.6rem;
  color: #fff;
  background: linear-gradient(145deg,var(--accent),#a05cff);
  box-shadow: 0 12px 28px -10px var(--accent);
}

.pc-05__card h3 {
  font-size: 1.3rem;
  font-weight: 800;
}

.pc-05__role {
  color: var(--dim);
  font-size: .86rem;
  margin-top: 2px;
}

.pc-05__bio {
  font-size: .83rem;
  line-height: 1.5;
  color: var(--dim);
  margin-top: 12px;
  text-wrap: balance;
}

.pc-05__row {
  display: flex;
  justify-content: space-between;
  margin: 20px 0;
  padding: 16px 0;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}

.pc-05__stat {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.pc-05__stat b {
  font-size: 1.05rem;
  font-weight: 800;
}

.pc-05__stat span {
  font-size: .68rem;
  color: var(--dim);
}

.pc-05__cta {
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 13px;
  cursor: pointer;
  font-weight: 700;
  font-size: .88rem;
  color: #fff;
  background: var(--accent);
  transition: filter .25s,transform .2s;
}

.pc-05__cta:hover {
  filter: brightness(1.1);
}

.pc-05__cta:active {
  transform: scale(.97);
}

@media (prefers-reduced-motion: reduce) {
  .pc-05 * {
    transition: none!important;
  }
}
```
