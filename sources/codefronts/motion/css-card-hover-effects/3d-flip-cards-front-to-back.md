---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/3d-flip-cards-front-to-back/"
title: "3D Flip Cards (Front to Back)"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A team-member profile card that rotates a full 180° on the Y-axis using perspective and backface-visibility, flipping from a photo-and-name front to a back…"
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Flip Cards (Front to Back)
Source: https://codefronts.com/motion/css-card-hover-effects/3d-flip-cards-front-to-back/

A team-member profile card that rotates a full 180° on the Y-axis using perspective and backface-visibility, flipping from a photo-and-name front to a back face with bio and social links. Space-efficient and tactile, it suits team pages, flashcard apps, pricing tiers, and anywhere two sides of information share one footprint.
## HTML
```html
<div class="card-04">
  <article class="card-04__card">
    <div class="card-04__face card-04__front">
      <span class="card-04__ff-role">Lead Designer</span>
      <h2 class="card-04__ff-name">Mara<br>Okonkwo</h2>
      <span class="card-04__ff-hint">↻ hover to flip</span>
    </div>
    <div class="card-04__face card-04__back">
      <div>
        <span class="card-04__fb-role">Lead Designer</span>
        <h3 class="card-04__fb-name">Mara Okonkwo</h3>
        <p class="card-04__fb-bio">Twelve years shaping product systems for fintech and health. Obsessed with motion, type, and the space between clicks.</p>
      </div>
      <div class="card-04__fb-links">
        <a href="#">Email</a>
        <a href="#">Dribbble</a>
        <a href="#">LinkedIn</a>
      </div>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],600;12..96,800&family=DM+Sans:opsz,[email protected],400;9..40,500&display=swap');

.card-04,
.card-04 *,
.card-04 *::before,
.card-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-04 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #eceae3;
  background-image: radial-gradient(circle at 70% 20%, #f6f4ee, #dcd9cf);
  font-family: 'DM Sans', sans-serif;
  padding: 2rem;
  perspective: 1600px;
}

.card-04__card {
  width: 320px;
  height: 430px;
  cursor: pointer;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 0.75s cubic-bezier(0.4,0.15,0.2,1);
}

.card-04__card:hover {
  transform: rotateY(180deg);
}

.card-04__face {
  position: absolute;
  inset: 0;
  border-radius: 24px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
  box-shadow: 0 20px 45px rgba(60,55,40,0.2);
}
/* FRONT — photo + name */

.card-04__front {
  background: linear-gradient(165deg, #2f9e8f 0%, #145c52 100%);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 2.2rem;
  color: #f2fbf9;
}

.card-04__front::before {
  content: "";
  position: absolute;
  top: -10%;
  left: 50%;
  width: 200px;
  height: 200px;
  transform: translateX(-50%);
  border-radius: 50%;
  background: radial-gradient(circle at 40% 35%, #d8f5ee, #6cc4b4);
  box-shadow: 0 20px 50px rgba(0,0,0,0.2);
}

.card-04__ff-role {
  font-size: 0.7rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #aef0e3;
}

.card-04__ff-name {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: 2.2rem;
  line-height: 1;
  margin-top: 0.3rem;
}

.card-04__ff-hint {
  margin-top: 1rem;
  font-size: 0.74rem;
  color: #cdeee7;
  opacity: 0.8;
}
/* BACK — bio + links */

.card-04__back {
  background: linear-gradient(165deg, #1c1b1a, #0f0e0d);
  transform: rotateY(180deg);
  padding: 2.2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #ece9e2;
}

.card-04__fb-role {
  font-size: 0.7rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #5fd3c0;
}

.card-04__fb-name {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: 1.7rem;
  line-height: 1.05;
  margin: 0.3rem 0 0.9rem;
}

.card-04__fb-bio {
  font-size: 0.85rem;
  line-height: 1.6;
  color: #b3afa6;
}

.card-04__fb-links {
  display: flex;
  gap: 0.6rem;
}

.card-04__fb-links a {
  flex: 1;
  text-align: center;
  text-decoration: none;
  font-size: 0.78rem;
  font-weight: 500;
  color: #ece9e2;
  padding: 0.6rem;
  border-radius: 10px;
  border: 1px solid rgba(255,255,255,0.18);
  transition: background 0.3s ease;
}

.card-04__fb-links a:hover {
  background: rgba(95,211,192,0.18);
}

@media (prefers-reduced-motion: reduce) {
  .card-04__card,
    .card-04__fb-links a {
    transition: none !important;
  }
}
```
