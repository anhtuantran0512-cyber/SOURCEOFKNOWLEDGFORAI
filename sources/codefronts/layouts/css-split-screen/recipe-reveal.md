---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/recipe-reveal/"
title: "Recipe Reveal"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Recipe book — terracotta + sage + butter yellow."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Recipe Reveal
Source: https://codefronts.com/layouts/css-split-screen/recipe-reveal/

Recipe book — terracotta + sage + butter yellow. Two halves: a recipe header on top, ingredients/method below. On smaller viewports the layout stacks; the right half "reveals" the method. Real <ul> + <ol> for ingredients and steps.
## HTML
```html
<section class="ss-rec" aria-label="Recipe split">
  <article class="ss-rec-hero">
    <span class="ss-rec-cat">— Sunday Lunch · Serves 4</span>
    <h2>Slow-roasted<br /><em>tomato</em> orzo.</h2>
    <p>One pan, four ingredients, ninety minutes. The kind of recipe that smells like home.</p>
    <div class="ss-rec-pill">
      <span><b>1h 30m</b><em>Total time</em></span>
      <span><b>Easy</b><em>Skill</em></span>
      <span><b>4 servings</b><em>Yield</em></span>
    </div>
    <button type="button" class="ss-rec-cta">Add to my book</button>
  </article>
  <aside class="ss-rec-method">
    <section class="ss-rec-ing">
      <h3>Ingredients</h3>
      <ul>
        <li><b>500g</b> Cherry tomatoes, on the vine</li>
        <li><b>250g</b> Orzo</li>
        <li><b>2 tbsp</b> Olive oil, plus more to finish</li>
        <li><b>1 tsp</b> Sea salt</li>
        <li><b>4</b> Garlic cloves, smashed</li>
      </ul>
    </section>
    <section class="ss-rec-steps">
      <h3>Method</h3>
      <ol>
        <li>Heat oven to 200°C. Spread tomatoes in a baking dish.</li>
        <li>Add olive oil, salt, garlic. Roast 60 minutes until burst.</li>
        <li>Cook orzo in salted water 8 min. Drain.</li>
        <li>Toss orzo through tomatoes. Finish with olive oil and basil.</li>
      </ol>
    </section>
  </aside>
</section>
```
## CSS
```css
.ss-rec {
  width: 100%;
  display: grid;
  grid-template-columns: 50% 50%;
  min-height: 100vh;
  font-family: 'Cormorant Garamond', 'Georgia', serif;
  background: #fff8e8;
  color: #2a1810;
  border-radius: 0;
  overflow: hidden;
  border: 1px solid #2a1810;
}

.ss-rec-hero {
  padding: 44px 40px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  background: radial-gradient(60% 60% at 30% 30%, #ffe2c8 0%, transparent 60%), #fff1d4;
  border-right: 1px dashed #c45a3c;
  position: relative;
}

.ss-rec-hero::before {
  content: '';
  position: absolute;
  top: 24px;
  right: 24px;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, #ffaa44 0%, #c45a3c 70%, #8a3818 100%);
  box-shadow: 0 6px 18px rgba(196,90,60,0.4);
}

.ss-rec-cat {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #6a8a5a;
}

.ss-rec-hero h2 {
  margin: 4px 0 0;
  font-size: clamp(36px, 5vw, 60px);
  font-weight: 500;
  line-height: 0.94;
  color: #2a1810;
  letter-spacing: -0.02em;
}

.ss-rec-hero h2 em {
  font-style: italic;
  color: #c45a3c;
}

.ss-rec-hero p {
  margin: 0;
  font-family: 'Inter', sans-serif;
  font-size: 15px;
  line-height: 1.6;
  color: #5a4a35;
  max-width: 380px;
}

.ss-rec-pill {
  display: flex;
  gap: 14px;
  padding: 16px 0;
  border-top: 1px solid #c8a878;
  border-bottom: 1px solid #c8a878;
  flex-wrap: wrap;
}

.ss-rec-pill span {
  display: flex;
  flex-direction: column;
}

.ss-rec-pill b {
  font-family: 'Cormorant Garamond', serif;
  font-size: 18px;
  font-weight: 500;
  font-style: italic;
  color: #2a1810;
}

.ss-rec-pill em {
  font-family: 'Inter', sans-serif;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  font-style: normal;
  color: #6a8a5a;
}

.ss-rec-cta {
  align-self: flex-start;
  padding: 13px 22px;
  background: #6a8a5a;
  color: #fff8e8;
  border: 0;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 0.16s;
}

.ss-rec-cta:hover {
  background: #4a6a3a;
}

.ss-rec-method {
  padding: 36px 36px;
  display: flex;
  flex-direction: column;
  gap: 22px;
  background: repeating-linear-gradient(180deg, transparent 0 30px, rgba(196,90,60,0.04) 30px 31px), #fff8e8;
  overflow-y: auto;
}

.ss-rec-method h3 {
  margin: 0 0 10px;
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.24em;
  color: #c45a3c;
  text-transform: uppercase;
  padding-bottom: 8px;
  border-bottom: 1px dashed #c8a878;
}

.ss-rec-ing ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 16.5px;
}

.ss-rec-ing li {
  display: grid;
  grid-template-columns: 80px 1fr;
  gap: 14px;
  font-style: italic;
  color: #2a1810;
}

.ss-rec-ing b {
  font-family: 'Inter', sans-serif;
  font-style: normal;
  font-size: 13px;
  font-weight: 700;
  color: #6a8a5a;
  letter-spacing: 0.04em;
  align-self: center;
}

.ss-rec-steps ol {
  list-style: none;
  counter-reset: rec;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.ss-rec-steps li {
  counter-increment: rec;
  padding-left: 38px;
  position: relative;
  font-family: 'Inter', sans-serif;
  font-size: 14.5px;
  line-height: 1.6;
  color: #4a3825;
}

.ss-rec-steps li::before {
  content: counter(rec);
  position: absolute;
  left: 0;
  top: -2px;
  font-family: 'Cormorant Garamond', serif;
  font-size: 22px;
  font-weight: 500;
  font-style: italic;
  color: #c45a3c;
  width: 28px;
  text-align: center;
  border-bottom: 1px solid #c45a3c;
}

@media (max-width: 720px) {
  .ss-rec {
    grid-template-columns: 1fr;
  }

  .ss-rec-hero {
    border-right: 0;
    border-bottom: 1px dashed #c45a3c;
  }
}
```
