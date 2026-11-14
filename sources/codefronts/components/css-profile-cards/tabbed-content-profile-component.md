---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/tabbed-content-profile-component/"
title: "Tabbed Content Profile Component"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "An app-style profile card with About, Skills and Contact tabs switched by pure-CSS radio inputs, complete with a sliding active-tab indicator."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tabbed Content Profile Component
Source: https://codefronts.com/components/css-profile-cards/tabbed-content-profile-component/

An app-style profile card with About, Skills and Contact tabs switched by pure-CSS radio inputs, complete with a sliding active-tab indicator.
## HTML
```html
<div class="pc-15">
  <div class="pc-15__card">
    <input type="radio" name="pc-15-tab" id="pc-15-t1" checked>
    <input type="radio" name="pc-15-tab" id="pc-15-t2">
    <input type="radio" name="pc-15-tab" id="pc-15-t3">
    <div class="pc-15__head">
      <div class="pc-15__pfp">MA</div>
      <div>
        <h3>Mateo Alvarez</h3>
        <p>Full-Stack Engineer</p>
      </div>
    </div>
    <div class="pc-15__tabs">
      <label for="pc-15-t1">About</label>
      <label for="pc-15-t2">Skills</label>
      <label for="pc-15-t3">Contact</label>
      <span class="pc-15__ink"></span>
    </div>
    <div class="pc-15__panes">
      <div class="pc-15__pane pc-15__p1">
        <p>Building resilient systems for 8 years. I care about clean APIs, observability, and mentoring juniors.</p>
      </div>
      <div class="pc-15__pane pc-15__p2">
        <div class="pc-15__skill"><span>TypeScript</span><i style="--v:92%"></i></div>
        <div class="pc-15__skill"><span>Go</span><i style="--v:78%"></i></div>
        <div class="pc-15__skill"><span>Postgres</span><i style="--v:85%"></i></div>
      </div>
      <div class="pc-15__pane pc-15__p3">
        <a>&#9993; [email protected]</a>
        <a>&#128241; +1 (555) 018-2277</a>
        <a>&#127760; mateo.dev</a>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-15,
.pc-15 *,
.pc-15 *::before,
.pc-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-15 ::selection {
  background: #7c5cff;
  color: #fff;
}

.pc-15 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #0c0b12;
  color: #eceaf5;
}

.pc-15__card {
  width: 320px;
  border-radius: 22px;
  padding: 24px;
  background: #15131f;
  border: 1px solid #241f38;
  box-shadow: 0 24px 60px -26px rgba(0,0,0,.85);
}

.pc-15__card input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.pc-15__head {
  display: flex;
  align-items: center;
  gap: 14px;
}

.pc-15__pfp {
  width: 60px;
  height: 60px;
  border-radius: 18px;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.25rem;
  color: #fff;
  background: linear-gradient(145deg,#7c5cff,#c15cff);
}

.pc-15__head h3 {
  font-size: 1.2rem;
  font-weight: 800;
}

.pc-15__head p {
  color: #948dae;
  font-size: .82rem;
  margin-top: 2px;
}

.pc-15__tabs {
  position: relative;
  display: flex;
  margin-top: 20px;
  background: #0f0d18;
  border-radius: 12px;
  padding: 5px;
}

.pc-15__tabs label {
  flex: 1;
  text-align: center;
  padding: 9px 0;
  font-size: .82rem;
  font-weight: 600;
  color: #948dae;
  cursor: pointer;
  position: relative;
  z-index: 1;
  transition: color .3s;
}

.pc-15__ink {
  position: absolute;
  top: 5px;
  bottom: 5px;
  left: 5px;
  width: calc((100% - 10px)/3);
  border-radius: 9px;
  background: linear-gradient(145deg,#7c5cff,#c15cff);
  transition: transform .35s cubic-bezier(.4,1.2,.5,1);
  z-index: 0;
}

#pc-15-t1:checked ~ .pc-15__tabs .pc-15__ink {
  transform: translateX(0);
}

#pc-15-t2:checked ~ .pc-15__tabs .pc-15__ink {
  transform: translateX(100%);
}

#pc-15-t3:checked ~ .pc-15__tabs .pc-15__ink {
  transform: translateX(200%);
}

#pc-15-t1:checked ~ .pc-15__tabs label[for=pc-15-t1],
#pc-15-t2:checked ~ .pc-15__tabs label[for=pc-15-t2],
#pc-15-t3:checked ~ .pc-15__tabs label[for=pc-15-t3] {
  color: #fff;
}

.pc-15__panes {
  position: relative;
  margin-top: 18px;
  min-height: 120px;
}

.pc-15__pane {
  position: absolute;
  inset: 0;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity .35s,transform .35s;
  pointer-events: none;
}

#pc-15-t1:checked ~ .pc-15__panes .pc-15__p1,
#pc-15-t2:checked ~ .pc-15__panes .pc-15__p2,
#pc-15-t3:checked ~ .pc-15__panes .pc-15__p3 {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.pc-15__pane p {
  font-size: .86rem;
  line-height: 1.55;
  color: #c5c0d8;
  text-wrap: balance;
}

.pc-15__skill {
  margin-bottom: 12px;
}

.pc-15__skill span {
  font-size: .78rem;
  color: #c5c0d8;
  display: block;
  margin-bottom: 5px;
}

.pc-15__skill i {
  display: block;
  height: 7px;
  border-radius: 4px;
  background: #241f38;
  position: relative;
  overflow: hidden;
}

.pc-15__skill i::after {
  content: '';
  position: absolute;
  inset: 0;
  width: var(--v);
  border-radius: 4px;
  background: linear-gradient(90deg,#7c5cff,#c15cff);
}

.pc-15__p3 a {
  display: block;
  padding: 10px 12px;
  border-radius: 10px;
  background: #0f0d18;
  font-size: .82rem;
  margin-bottom: 8px;
  color: #c5c0d8;
  cursor: pointer;
  transition: background .25s;
}

.pc-15__p3 a:hover {
  background: #1b1830;
}

@media (prefers-reduced-motion: reduce) {
  .pc-15 * {
    transition: none!important;
  }
}
```
