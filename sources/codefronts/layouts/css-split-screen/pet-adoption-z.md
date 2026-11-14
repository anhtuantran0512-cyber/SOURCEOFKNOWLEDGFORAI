---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/pet-adoption-z/"
title: "Pet Adoption Z"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Pet adoption — grass green + sky blue + sun yellow."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pet Adoption Z
Source: https://codefronts.com/layouts/css-split-screen/pet-adoption-z/

Pet adoption — grass green + sky blue + sun yellow. Z-pattern: image left → text right → image right → text left, but expressed as a 2×2 grid that creates an interlocking flow. Friendly, optimistic, full of CSS-painted dog and cat illustrations.
## HTML
```html
<section class="ss-pet" aria-label="Pet adoption page">
  <article class="ss-pet-img ss-pet-cat" aria-hidden="true">
    <span class="ss-pet-creature">
      <span class="ss-pet-eye"></span>
      <span class="ss-pet-eye2"></span>
      <span class="ss-pet-nose"></span>
    </span>
    <span class="ss-pet-tag">MEET LUNA · 2 yrs</span>
  </article>
  <article class="ss-pet-text">
    <span class="ss-pet-eye-tag">FRIDAY ADOPTIONS</span>
    <h2>A good home<br />is one <em>nap</em><br />away.</h2>
    <p>
      22 cats and 14 dogs are waiting at Bramble Lane this weekend. Walk-ins welcome, no appointment
      needed.
    </p>
  </article>
  <article class="ss-pet-text ss-pet-text-2">
    <h3>How it works</h3>
    <ol>
      <li>Visit our shelter Sat / Sun, 10am — 4pm</li>
      <li>Spend an hour with a friend</li>
      <li>Take them home the same day</li>
    </ol>
    <button type="button" class="ss-pet-cta">Plan your visit →</button>
  </article>
  <article class="ss-pet-img ss-pet-dog" aria-hidden="true">
    <span class="ss-pet-creature">
      <span class="ss-pet-eye"></span>
      <span class="ss-pet-eye2"></span>
      <span class="ss-pet-nose"></span>
      <span class="ss-pet-tongue"></span>
    </span>
    <span class="ss-pet-tag">MEET KOJI · 3 yrs</span>
  </article>
</section>
```
## CSS
```css
.ss-pet {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
  background: #fef7d4;
  border-radius: 0;
  overflow: hidden;
  gap: 0;
}

.ss-pet-img {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.ss-pet-cat {
  background: radial-gradient(80% 80% at 30% 70%, #94c4ec 0%, #2a8cc4 100%);
}

.ss-pet-dog {
  background: radial-gradient(80% 80% at 70% 30%, #84d488 0%, #2c8c34 100%);
}

.ss-pet-creature {
  position: relative;
  width: 130px;
  height: 130px;
  border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
  background: #fff;
  box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}

.ss-pet-cat .ss-pet-creature::before,
.ss-pet-cat .ss-pet-creature::after {
  content: '';
  position: absolute;
  top: -22px;
  width: 0;
  height: 0;
  border-left: 22px solid transparent;
  border-right: 22px solid transparent;
  border-bottom: 36px solid #fff;
}

.ss-pet-cat .ss-pet-creature::before {
  left: 4px;
  transform: rotate(-12deg);
}

.ss-pet-cat .ss-pet-creature::after {
  right: 4px;
  transform: rotate(12deg);
}

.ss-pet-dog .ss-pet-creature {
  background: linear-gradient(180deg, #d4a878 0%, #a87838 100%);
}

.ss-pet-dog .ss-pet-creature::before,
.ss-pet-dog .ss-pet-creature::after {
  content: '';
  position: absolute;
  top: 22px;
  width: 38px;
  height: 56px;
  background: linear-gradient(180deg, #b8884c 0%, #6e4818 100%);
  border-radius: 50%;
}

.ss-pet-dog .ss-pet-creature::before {
  left: -22px;
  transform: rotate(-22deg);
}

.ss-pet-dog .ss-pet-creature::after {
  right: -22px;
  transform: rotate(22deg);
}

.ss-pet-eye,
.ss-pet-eye2 {
  position: absolute;
  top: 36%;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #2a2a2a;
}

.ss-pet-eye {
  left: 28%;
}

.ss-pet-eye2 {
  right: 28%;
}

.ss-pet-nose {
  position: absolute;
  top: 52%;
  left: 50%;
  transform: translateX(-50%);
  width: 14px;
  height: 12px;
  border-radius: 50%;
  background: #c45a3c;
}

.ss-pet-cat .ss-pet-nose {
  background: #ec5a82;
  width: 12px;
  height: 8px;
}

.ss-pet-tongue {
  position: absolute;
  top: 64%;
  left: 50%;
  transform: translateX(-50%);
  width: 22px;
  height: 14px;
  border-radius: 0 0 12px 12px;
  background: #ec5a82;
}

.ss-pet-tag {
  position: absolute;
  bottom: 18px;
  font-family: 'Inter', sans-serif;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: 0.18em;
  padding: 5px 11px;
  background: #fff;
  color: #2a2a2a;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.18);
}

.ss-pet-text {
  padding: 36px 36px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  background: #fef7d4;
  position: relative;
}

.ss-pet-text-2 {
  background: #fff8e8;
}

.ss-pet-eye-tag {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #c45a3c;
  align-self: flex-start;
}

.ss-pet-text h2 {
  margin: 4px 0 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(34px, 5vw, 50px);
  font-weight: 500;
  line-height: 0.94;
  color: #2a3325;
  letter-spacing: -0.02em;
}

.ss-pet-text h2 em {
  font-style: italic;
  color: #2c8c34;
}

.ss-pet-text p {
  margin: 0;
  font-size: 15px;
  line-height: 1.6;
  color: #4a4030;
  max-width: 360px;
}

.ss-pet-text h3 {
  margin: 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: 22px;
  font-weight: 500;
  font-style: italic;
  color: #2a3325;
  letter-spacing: -0.01em;
}

.ss-pet-text ol {
  list-style: none;
  counter-reset: pet;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.ss-pet-text li {
  counter-increment: pet;
  padding-left: 36px;
  position: relative;
  font-size: 14.5px;
  line-height: 1.6;
  color: #4a4030;
}

.ss-pet-text li::before {
  content: counter(pet);
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #ffe89a;
  color: #c45a3c;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 0 2px #c45a3c;
}

.ss-pet-cta {
  align-self: flex-start;
  margin-top: auto;
  padding: 13px 22px;
  background: #2c8c34;
  color: #fef7d4;
  border: 0;
  border-radius: 28px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.04em;
  cursor: pointer;
  box-shadow: 0 6px 18px rgba(44,140,52,0.35);
  transition: transform 0.12s, background 0.16s;
}

.ss-pet-cta:hover {
  background: #1a6a22;
  transform: translateY(-1px);
}

@media (max-width: 720px) {
  .ss-pet {
    grid-template-columns: 1fr;
    grid-template-rows: repeat(4, auto);
  }

  .ss-pet-img {
    min-height: 240px;
  }
}
```
