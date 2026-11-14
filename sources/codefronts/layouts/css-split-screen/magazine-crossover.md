---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/magazine-crossover/"
title: "Magazine Crossover"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Editorial magazine spread — newspaper black on cream with a single spot color (cobalt blue)."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magazine Crossover
Source: https://codefronts.com/layouts/css-split-screen/magazine-crossover/

Editorial magazine spread — newspaper black on cream with a single spot color (cobalt blue). Oversized italic headline crosses the seam between two halves; pull-quote on the right intrudes into the left photo zone. The kind of layout you see on a New York Times Magazine longread.
## HTML
```html
<section class="ss-mag" aria-label="Editorial magazine spread">
  <article class="ss-mag-photo">
    <div class="ss-mag-image" aria-hidden="true">
      <span class="ss-mag-figure"></span>
      <span class="ss-mag-light"></span>
    </div>
    <span class="ss-mag-caption">Photo · Iris Hawthorne for The Quarterly</span>
  </article>
  <article class="ss-mag-text">
    <span class="ss-mag-section">SECTION 04 / ESSAY</span>
    <h2 class="ss-mag-head">
      The <em>quiet</em> art of<br />doing one thing<br />at a <em>time.</em>
    </h2>
    <span class="ss-mag-byline">By <b>Iris Hawthorne</b> · Spring 2026</span>
    <p class="ss-mag-lede">
      <span class="ss-mag-drop">A</span>fter a decade of optimizing every minute, the loneliest
      realization wasn't that I had no time. It was that I'd forgotten how to spend it. Three years
      ago I made a small commitment, and it changed everything I thought I knew about productivity.
    </p>
    <blockquote class="ss-mag-pull">
      "The thing about doing one thing at a time is that the thing finally gets your attention."
    </blockquote>
    <p class="ss-mag-out">What I learned was simpler than I expected — and harder to keep.</p>
    <ul class="ss-mag-meta">
      <li><b>12 min</b> read</li>
      <li><b>2,840</b> words</li>
      <li><b>Apr 14</b> issue</li>
    </ul>
  </article>
</section>
```
## CSS
```css
.ss-mag {
  width: 100%;
  display: grid;
  grid-template-columns: 42% 58%;
  min-height: 100vh;
  font-family: 'Cormorant Garamond', 'Georgia', serif;
  background: #f4ede0;
  color: #1a1a1a;
  border-radius: 0;
  overflow: hidden;
  border: 1px solid #1a1a1a;
}

.ss-mag-photo {
  position: relative;
  background: linear-gradient(180deg, #2a2a2a 0%, #0a0a0a 100%);
  padding: 36px 32px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  border-right: 1px solid #1a1a1a;
}

.ss-mag-image {
  position: relative;
  flex: 1;
  background: linear-gradient(180deg, #4a4a4a 0%, #1a1a1a 100%);
  overflow: hidden;
  isolation: isolate;
}

.ss-mag-figure {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 200px;
  height: 80%;
  background: radial-gradient(ellipse at 50% 12%, #c8a878 0%, #c8a878 8%, transparent 9%), linear-gradient(180deg, transparent 8%, #1a3658 8%, #1a3658 100%);
  clip-path: polygon(40% 0, 60% 0, 70% 16%, 80% 38%, 80% 100%, 20% 100%, 20% 38%, 30% 16%);
}

.ss-mag-light {
  position: absolute;
  top: -10%;
  right: -20%;
  width: 60%;
  height: 80%;
  background: radial-gradient(circle at 50% 0%, rgba(255,200,80,0.35), transparent 70%);
  filter: blur(8px);
}

.ss-mag-caption {
  font-family: 'Cormorant Garamond', serif;
  font-size: 12px;
  font-style: italic;
  color: #c8a878;
}

.ss-mag-text {
  padding: 36px 40px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  background: repeating-linear-gradient(0deg, transparent 0 32px, rgba(0,0,0,0.018) 32px 33px), #f9f3e6;
  position: relative;
}

.ss-mag-section {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.32em;
  text-transform: uppercase;
  color: #1a3658;
}

.ss-mag-head {
  margin: 4px 0 0;
  font-size: clamp(36px, 5.5vw, 60px);
  font-weight: 500;
  line-height: 0.92;
  letter-spacing: -0.02em;
  color: #1a1a1a;
}

.ss-mag-head em {
  font-style: italic;
  color: #1a3658;
}

.ss-mag-byline {
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  color: #4a4a4a;
}

.ss-mag-byline b {
  color: #1a3658;
  font-weight: 700;
}

.ss-mag-lede {
  margin: 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: 18px;
  line-height: 1.55;
  color: #1a1a1a;
  column-count: 2;
  column-gap: 24px;
  column-rule: 1px solid #c8a878;
}

.ss-mag-drop {
  font-family: 'Cormorant Garamond', serif;
  font-size: 64px;
  font-weight: 500;
  font-style: italic;
  line-height: 0.85;
  float: left;
  padding: 4px 8px 0 0;
  color: #1a3658;
}

.ss-mag-pull {
  margin: 0;
  font-size: clamp(18px, 2.4vw, 24px);
  line-height: 1.4;
  color: #1a3658;
  font-style: italic;
  border-left: 4px solid #1a3658;
  padding: 0 0 0 18px;
  font-weight: 500;
}

.ss-mag-out {
  margin: 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: 16px;
  line-height: 1.6;
  color: #2a2a2a;
}

.ss-mag-meta {
  list-style: none;
  margin: 0;
  padding: 14px 0;
  border-top: 1px solid #c8a878;
  border-bottom: 1px solid #c8a878;
  display: flex;
  gap: 22px;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  color: #4a4a4a;
}

.ss-mag-meta b {
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
  font-size: 18px;
  font-weight: 500;
  color: #1a1a1a;
  margin-right: 4px;
}

@media (max-width: 720px) {
  .ss-mag {
    grid-template-columns: 1fr;
  }

  .ss-mag-photo {
    border-right: 0;
    border-bottom: 1px solid #1a1a1a;
    min-height: 280px;
  }
  /* .ss-mag-head no longer needs a mobile reset (no desktop overflow). */

  .ss-mag-lede {
    column-count: 1;
  }
}
```
