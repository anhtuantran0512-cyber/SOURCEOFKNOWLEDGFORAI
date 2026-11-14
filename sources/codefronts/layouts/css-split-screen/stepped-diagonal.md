---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/stepped-diagonal/"
title: "Stepped Diagonal"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Streetwear brand drop — mustard yellow + asphalt black + neon pink."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stepped Diagonal
Source: https://codefronts.com/layouts/css-split-screen/stepped-diagonal/

Streetwear brand drop — mustard yellow + asphalt black + neon pink. Stepped diagonal cut between two halves, sticker-graphic typography, drop-countdown badge. The kind of split a sneaker brand uses to announce a Friday release.
## HTML
```html
<section class="ss-str" aria-label="Streetwear drop announcement">
  <div class="ss-str-yellow">
    <span class="ss-str-stamp" aria-hidden="true">DROP 047</span>
    <h2>FRIDAY<br /><span class="ss-str-pink">3PM</span></h2>
    <ul class="ss-str-info">
      <li><b>03</b> Tees</li>
      <li><b>02</b> Hoodies</li>
      <li><b>01</b> Pair of kicks</li>
    </ul>
  </div>
  <div class="ss-str-black">
    <span class="ss-str-tag">// LIMITED RUN</span>
    <p>200 pieces. Numbered. No restock. Sign up below to get the link 5 minutes early.</p>
    <form class="ss-str-form" role="search">
      <label class="ss-str-sr" for="ss-str-em">Email for early access</label>
      <input
        id="ss-str-em"
        type="email"
        name="email"
        placeholder="[email protected]"
        autocomplete="email"
        required
      />
      <button type="submit">GET LINK →</button>
    </form>
    <span class="ss-str-counter">⏱ 04 : 12 : 47 : 03</span>
  </div>
</section>
```
## CSS
```css
.ss-str {
  width: 100%;
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100vh;
  font-family: 'Helvetica Neue', sans-serif;
  border-radius: 0;
  overflow: hidden;
  isolation: isolate;
}

.ss-str-yellow {
  background: #ffd400;
  color: #0a0a0a;
  padding: 48px 44px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  position: relative;
  /* Clean vertical right edge — the dashed splitter below sits exactly
       on this seam. Previously used a diagonal clip-path but the angle
       changed with viewport height, drifting the splitter off the actual
       cut edge on tall (100vh) layouts. */
  z-index: 2;
}

.ss-str-yellow::before {
  content: '';
  /* Vertical dashed splitter sits FLUSH on the yellow's right edge
       so the visible seam and the splitter graphic agree at every
       viewport height. */
  position: absolute;
  right: -3px;
  top: 0;
  bottom: 0;
  width: 6px;
  background: repeating-linear-gradient(180deg, #0a0a0a 0 12px, transparent 12px 24px);
  z-index: 3;
}

.ss-str-stamp {
  display: inline-block;
  padding: 6px 14px;
  background: #0a0a0a;
  color: #ffd400;
  font-family: 'Courier New', monospace;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.24em;
  align-self: flex-start;
  transform: rotate(-2deg);
}

.ss-str-yellow h2 {
  margin: 0;
  font-size: clamp(56px, 9vw, 110px);
  font-weight: 900;
  line-height: 0.85;
  letter-spacing: -0.04em;
  font-style: italic;
}

.ss-str-pink {
  color: #ff0090;
  -webkit-text-stroke: 2px #0a0a0a;
}

.ss-str-info {
  list-style: none;
  margin: auto 0 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.ss-str-info li {
  display: flex;
  align-items: baseline;
  gap: 12px;
  font-size: 17px;
  font-weight: 700;
  padding: 8px 0;
  border-bottom: 2px dashed #0a0a0a;
  font-family: 'Courier New', monospace;
}

.ss-str-info b {
  font-family: 'Helvetica Neue', sans-serif;
  font-weight: 900;
  font-size: 24px;
  background: #ff0090;
  color: #ffd400;
  padding: 0 6px;
  font-style: italic;
}

.ss-str-black {
  background: #0a0a0a;
  color: #f0ece4;
  /* Standard padding; no negative margin overlap (that only made sense
       when the yellow had a diagonal cut). Panel now sits flush against
       the yellow's vertical seam. */
  padding: 48px 44px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  position: relative;
  z-index: 1;
}

.ss-str-tag {
  font-family: 'Courier New', monospace;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.22em;
  color: #ff0090;
}

.ss-str-black p {
  margin: 0;
  font-size: 17px;
  line-height: 1.55;
  color: #f0ece4;
  max-width: 360px;
  font-weight: 500;
}

.ss-str-form {
  display: flex;
  gap: 0;
  margin-top: auto;
  border: 2px solid #ffd400;
  background: #1a1a1a;
}

.ss-str-form input {
  flex: 1;
  padding: 14px 16px;
  background: transparent;
  color: #f0ece4;
  border: 0;
  outline: 0;
  font-family: 'Courier New', monospace;
  font-size: 14px;
}

.ss-str-form input::placeholder {
  color: #6a6a6a;
}

.ss-str-form button {
  padding: 0 22px;
  background: #ffd400;
  color: #0a0a0a;
  border: 0;
  font-family: 'Helvetica Neue', sans-serif;
  font-size: 13px;
  font-weight: 900;
  letter-spacing: 0.16em;
  cursor: pointer;
  transition: background 0.12s;
}

.ss-str-form button:hover {
  background: #ff0090;
  color: #ffd400;
}

.ss-str-counter {
  font-family: 'Courier New', monospace;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: #ffd400;
  padding: 10px 14px;
  background: #1a1a1a;
  border: 1px dashed #ff0090;
  align-self: flex-start;
}

.ss-str-sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

@media (max-width: 720px) {
  .ss-str {
    grid-template-columns: 1fr;
  }
  /* Stacked layout: dashed splitter becomes a horizontal rule between
       the two panels instead of a vertical splitter on the seam. */

  .ss-str-yellow::before {
    right: 0;
    left: 0;
    top: auto;
    bottom: -3px;
    width: auto;
    height: 6px;
    background: repeating-linear-gradient(90deg, #0a0a0a 0 12px, transparent 12px 24px);
  }
}
```
