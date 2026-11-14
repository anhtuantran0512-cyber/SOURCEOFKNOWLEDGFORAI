---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/morphing-profile-card-expanding-bio/"
title: "Morphing Profile Card / Expanding Bio"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A compact profile that smoothly expands to reveal bio, social handles and stats when toggled, using the CSS grid-rows 0fr-to-1fr height animation trick."
has_js: "true"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Morphing Profile Card / Expanding Bio
Source: https://codefronts.com/components/css-profile-cards/morphing-profile-card-expanding-bio/

A compact profile that smoothly expands to reveal bio, social handles and stats when toggled, using the CSS grid-rows 0fr-to-1fr height animation trick.
## HTML
```html
<div class="pc-19">
  <div class="pc-19__card" id="pc-19-card">
    <button class="pc-19__more" id="pc-19-toggle" aria-expanded="false">
      <span class="pc-19__chev">&#8250;</span>
    </button>
    <div class="pc-19__head">
      <div class="pc-19__pfp">OT</div>
      <div>
        <h3>Omar Tahir</h3>
        <p>Data Scientist</p>
      </div>
    </div>
    <div class="pc-19__reveal">
      <p class="pc-19__bio">Turning messy datasets into decisions. I work across Python, dbt, and causal inference.</p>
      <div class="pc-19__handles">
        <a>&#9670; github/omart</a>
        <a>&#9671; linkedin/omart</a>
        <a>&#9634; omar.data</a>
      </div>
      <div class="pc-19__stats">
        <div><b>47</b><span>Models</span></div>
        <div><b>9</b><span>Papers</span></div>
        <div><b>3.2k</b><span>Followers</span></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-19,
.pc-19 *,
.pc-19 *::before,
.pc-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-19 ::selection {
  background: #00c2a8;
  color: #042;
}

.pc-19 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #07110f;
  color: #e9fbf6;
}

.pc-19__card {
  position: relative;
  width: 300px;
  border-radius: 22px;
  padding: 24px;
  background: linear-gradient(160deg,#0e201c,#0a1714);
  border: 1px solid #163029;
  box-shadow: 0 24px 60px -26px rgba(0,0,0,.8);
  transition: box-shadow .35s;
}

.pc-19__more {
  position: absolute;
  top: 18px;
  right: 18px;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  cursor: pointer;
  border: 1px solid #1d3a32;
  background: #0f221d;
  color: #00c2a8;
  display: grid;
  place-items: center;
  transition: background .25s;
}

.pc-19__more:hover {
  background: #143029;
}

.pc-19__chev {
  font-size: 1.3rem;
  line-height: 1;
  transform: rotate(90deg);
  transition: transform .4s cubic-bezier(.4,1.2,.5,1);
}

.pc-19__card.is-open .pc-19__chev {
  transform: rotate(-90deg);
}

.pc-19__head {
  display: flex;
  align-items: center;
  gap: 14px;
}

.pc-19__pfp {
  width: 58px;
  height: 58px;
  border-radius: 18px;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.2rem;
  color: #042;
  background: linear-gradient(145deg,#00c2a8,#2ee6b0);
}

.pc-19__head h3 {
  font-size: 1.2rem;
  font-weight: 800;
}

.pc-19__head p {
  color: #79b3a5;
  font-size: .82rem;
  margin-top: 2px;
}

.pc-19__reveal {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .45s cubic-bezier(.4,0,.2,1);
  overflow: hidden;
}

.pc-19__card.is-open .pc-19__reveal {
  grid-template-rows: 1fr;
}

.pc-19__reveal > * {
  min-height: 0;
}

.pc-19__reveal {
  margin-top: 0;
}

.pc-19__card.is-open .pc-19__reveal {
  margin-top: 16px;
}

.pc-19__bio {
  font-size: .84rem;
  line-height: 1.5;
  color: #bfe0d7;
  text-wrap: balance;
  overflow: hidden;
}

.pc-19__handles {
  display: flex;
  flex-direction: column;
  gap: 7px;
  margin-top: 14px;
}

.pc-19__handles a {
  font-size: .8rem;
  color: #8fd4c5;
  cursor: pointer;
  transition: color .2s;
}

.pc-19__handles a:hover {
  color: #2ee6b0;
}

.pc-19__stats {
  display: flex;
  justify-content: space-between;
  margin-top: 16px;
  padding-top: 14px;
  border-top: 1px solid #163029;
}

.pc-19__stats b {
  display: block;
  font-size: 1.1rem;
  font-weight: 800;
}

.pc-19__stats span {
  font-size: .66rem;
  color: #79b3a5;
}

@media (prefers-reduced-motion: reduce) {
  .pc-19 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var card = document.getElementById('pc-19-card');
  var btn = document.getElementById('pc-19-toggle');
  if(!card || !btn) return;
  btn.addEventListener('click', function(){
    var open = card.classList.toggle('is-open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();
```
