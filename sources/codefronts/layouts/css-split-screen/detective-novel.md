---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/detective-novel/"
title: "Detective Novel"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Detective novel cover — burnt orange + ink black + parchment cream."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Detective Novel
Source: https://codefronts.com/layouts/css-split-screen/detective-novel/

Detective novel cover — burnt orange + ink black + parchment cream. A diagonal mask wipes between the cover image and a synopsis on hover. Mystery noir aesthetic with serif type, thin gold rules, and a deliberately distressed paper texture.
## HTML
```html
<section class="ss-det" aria-label="Detective novel feature">
  <article class="ss-det-cover">
    <div class="ss-det-image" aria-hidden="true">
      <span class="ss-det-silhouette"></span>
      <span class="ss-det-light"></span>
      <span class="ss-det-rain"></span>
    </div>
    <div class="ss-det-overlay">
      <span class="ss-det-genre">A NEW DETECTIVE NOVEL</span>
      <h2>The<br /><em>Last</em><br />Train.</h2>
      <span class="ss-det-author">by Iris Hawthorne</span>
    </div>
  </article>
  <article class="ss-det-blurb">
    <span class="ss-det-folio">PAGE I · CHAPTER ONE</span>
    <p class="ss-det-quote">
      "It rained the night Dr. Morrow disappeared, and the only witness was a stationmaster who
      hadn't slept in three days."
    </p>
    <p class="ss-det-body">
      A woman searches for her vanished mentor through the rain-soaked streets of a coastal town
      that doesn't want her there.
    </p>
    <ul class="ss-det-list">
      <li>★★★★★ <em>The Times</em></li>
      <li>★★★★★ <em>Le Monde</em></li>
      <li>★★★★☆ <em>Hawthorne Review</em></li>
    </ul>
    <button type="button" class="ss-det-cta">Read first chapter →</button>
  </article>
</section>
```
## CSS
```css
.ss-det {
  width: 100%;
  display: grid;
  grid-template-columns: 45% 55%;
  min-height: 100vh;
  font-family: 'Cormorant Garamond', 'Georgia', serif;
  background: #f0e6d0;
  color: #1a0e08;
  border-radius: 0;
  overflow: hidden;
  border: 1px solid #1a0e08;
}

.ss-det-cover {
  position: relative;
  background: radial-gradient(80% 80% at 50% 30%, #c45a1c 0%, #6e1f0c 60%, #1a0a06 100%);
  padding: 36px 32px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  overflow: hidden;
  isolation: isolate;
  border-right: 1px solid #1a0e08;
}

.ss-det-image {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.ss-det-silhouette {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 240px;
  background: radial-gradient(ellipse at 50% 14%, #1a0a06 0%, #1a0a06 8%, transparent 9%), linear-gradient(180deg, transparent 8%, #1a0a06 8%, #1a0a06 100%);
  clip-path: polygon(40% 0, 60% 0, 70% 16%, 80% 38%, 80% 100%, 20% 100%, 20% 38%, 30% 16%);
}

.ss-det-light {
  position: absolute;
  top: 0;
  right: 12%;
  width: 220px;
  height: 220px;
  background: radial-gradient(circle at 50% 0%, rgba(255,200,80,0.32), transparent 70%);
  filter: blur(8px);
}

.ss-det-rain {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(78deg, transparent 0 22px, rgba(255,255,255,0.12) 22px 23px);
  animation: ss-det-rain 0.6s linear infinite;
}

@keyframes ss-det-rain {
  from {
    background-position: 0 0;
  }

  to {
    background-position: 22px 22px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ss-det-rain {
    animation: none;
  }
}

.ss-det-overlay {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  gap: 14px;
  height: 100%;
}

.ss-det-genre {
  font-family: 'Inter', sans-serif;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: 0.32em;
  color: #f5d68a;
  align-self: flex-start;
  padding: 5px 10px;
  border: 1px solid #f5d68a;
  background: rgba(0,0,0,0.4);
}

.ss-det-cover h2 {
  margin: auto 0;
  font-size: clamp(48px, 7vw, 80px);
  font-weight: 500;
  line-height: 0.86;
  color: #f0e6d0;
  letter-spacing: -0.02em;
  text-shadow: 0 4px 30px rgba(0,0,0,0.7);
}

.ss-det-cover h2 em {
  font-style: italic;
  color: #f5d68a;
  font-family: 'Cormorant Garamond', serif;
  display: inline-block;
}

.ss-det-author {
  font-family: 'Cormorant Garamond', serif;
  font-size: 18px;
  font-style: italic;
  color: #f0e6d0;
  text-shadow: 0 1px 4px rgba(0,0,0,0.6);
  margin-top: auto;
}

.ss-det-blurb {
  padding: 36px 36px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  background: repeating-linear-gradient(0deg, transparent 0 32px, rgba(110,30,30,0.04) 32px 33px), #f0e6d0;
}

.ss-det-folio {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.24em;
  color: #6e1f0c;
}

.ss-det-quote {
  margin: 6px 0 0;
  font-size: clamp(18px, 2.6vw, 24px);
  line-height: 1.4;
  color: #1a0e08;
  font-style: italic;
  border-left: 3px solid #c45a1c;
  padding-left: 16px;
}

.ss-det-body {
  margin: 0;
  font-family: 'Inter', sans-serif;
  font-size: 14.5px;
  line-height: 1.7;
  color: #4a3825;
  max-width: 440px;
}

.ss-det-list {
  list-style: none;
  margin: auto 0 0;
  padding: 14px 0;
  border-top: 1.5px solid #c45a1c;
  border-bottom: 1.5px solid #c45a1c;
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 14px;
  color: #1a0e08;
  font-family: 'Inter', sans-serif;
}

.ss-det-list li {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
}

.ss-det-list em {
  font-style: italic;
  color: #6e1f0c;
  font-family: 'Cormorant Garamond', serif;
  font-size: 16px;
}

.ss-det-cta {
  align-self: flex-start;
  padding: 14px 24px;
  background: #1a0e08;
  color: #f5d68a;
  border: 0;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 0.16s;
}

.ss-det-cta:hover {
  background: #6e1f0c;
}

@media (max-width: 720px) {
  .ss-det {
    grid-template-columns: 1fr;
  }

  .ss-det-cover {
    border-right: 0;
    border-bottom: 1px solid #1a0e08;
    min-height: 360px;
  }
}
```
