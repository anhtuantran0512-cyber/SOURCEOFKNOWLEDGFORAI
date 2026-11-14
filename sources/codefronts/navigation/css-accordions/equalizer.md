---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/equalizer/"
title: "Equalizer Accordion — Animated Level Bars for Playlists & Audio"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "A dark playlist where the open track 'plays': its header grows a five-bar equalizer bouncing on staggered loops, the track title tints neon green, and the…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Equalizer Accordion — Animated Level Bars for Playlists & Audio
Source: https://codefronts.com/navigation/css-accordions/equalizer/

A dark playlist where the open track 'plays': its header grows a five-bar equalizer bouncing on staggered loops, the track title tints neon green, and the body reveals liner notes with a duration readout. The now-playing metaphor everyone recognizes, driving accordion state — for music, podcasts and anything with a queue.
## HTML
```html
<section class="acc-29" aria-label="Equalizer playlist accordion demo">
  <div class="acc-29__wrap">
    <p class="acc-29__kicker">Side A · 24 min</p>
    <h3 class="acc-29__title">Basement Tapes, Vol. 3</h3>
    <details class="acc-29__item" open>
      <summary class="acc-29__sum"><span class="acc-29__idx">01</span><span class="acc-29__name">Copper Wire</span><span class="acc-29__eq"><i></i><i></i><i></i><i></i><i></i></span><span class="acc-29__len">4:12</span></summary>
      <div class="acc-29__body"><p>Recorded in one take after the amp blew and got replaced with a borrowed practice rig — which is the fuzz you hear on the second verse. We kept it.</p></div>
    </details>
    <details class="acc-29__item">
      <summary class="acc-29__sum"><span class="acc-29__idx">02</span><span class="acc-29__name">Night Bus North</span><span class="acc-29__eq"><i></i><i></i><i></i><i></i><i></i></span><span class="acc-29__len">3:48</span></summary>
      <div class="acc-29__body"><p>The field recording under the intro is the actual 2am route 6 — phone in a coat pocket, driver humming. He's credited.</p></div>
    </details>
    <details class="acc-29__item">
      <summary class="acc-29__sum"><span class="acc-29__idx">03</span><span class="acc-29__name">Salt &amp; Static</span><span class="acc-29__eq"><i></i><i></i><i></i><i></i><i></i></span><span class="acc-29__len">5:03</span></summary>
      <div class="acc-29__body"><p>Two drum kits panned hard left and right, playing almost the same part. The 'almost' is the song.</p></div>
    </details>
    <details class="acc-29__item">
      <summary class="acc-29__sum"><span class="acc-29__idx">04</span><span class="acc-29__name">Last Light on the Pier</span><span class="acc-29__eq"><i></i><i></i><i></i><i></i><i></i></span><span class="acc-29__len">6:40</span></summary>
      <div class="acc-29__body"><p>Closes the side with the string quartet from upstairs — they rehearse Thursdays and finally said yes.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-29,
.acc-29 *,
.acc-29 *::before,
.acc-29 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-29 {
  --signal: oklch(0.85 0.23 150);
  --dim: #8890a4;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #12141c;
  padding: 44px 24px;
}

.acc-29__wrap {
  width: min(540px,100%);
  background: #181b26;
  border: 1px solid #262a3a;
  border-radius: 18px;
  padding: 30px 26px;
  box-shadow: 0 30px 70px -35px rgba(0,0,0,.9);
}

.acc-29__kicker {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--dim);
}

.acc-29__title {
  font-size: 23px;
  font-weight: 800;
  color: #eef0f8;
  letter-spacing: -.01em;
  margin: 6px 0 16px;
}

.acc-29__item {
  border-top: 1px solid #232738;
}

.acc-29__sum {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 56px;
  padding: 6px 4px;
  cursor: pointer;
  transition: background .15s;
  border-radius: 8px;
}

.acc-29__sum::-webkit-details-marker {
  display: none;
}

.acc-29__sum::marker {
  content: "";
}

.acc-29__sum:hover {
  background: #1d2130;
}

.acc-29__idx {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: var(--dim);
  width: 22px;
  flex: none;
}

.acc-29__item[open] .acc-29__idx {
  color: var(--signal);
}

.acc-29__item[open] .acc-29__idx::before {
  content: "▶ ";
}

.acc-29__item[open] .acc-29__idx {
  font-size: 10px;
  letter-spacing: 0;
}

.acc-29__name {
  font-size: 15.5px;
  font-weight: 650;
  color: #dfe3f0;
}

.acc-29__item[open] .acc-29__name {
  color: var(--signal);
}

.acc-29__eq {
  margin-left: auto;
  display: flex;
  align-items: flex-end;
  gap: 2.5px;
  height: 18px;
  flex: none;
}

.acc-29__eq i {
  width: 3px;
  height: 100%;
  background: var(--dim);
  border-radius: 2px;
  transform: scaleY(.2);
  transform-origin: bottom;
  transition: background .2s;
}

.acc-29__item[open] .acc-29__eq i {
  background: var(--signal);
  animation: acc-29-bounce .62s ease-in-out infinite alternate;
}

.acc-29__item[open] .acc-29__eq i:nth-child(2) {
  animation-duration: .44s;
  animation-delay: .1s;
}

.acc-29__item[open] .acc-29__eq i:nth-child(3) {
  animation-duration: .78s;
  animation-delay: .05s;
}

.acc-29__item[open] .acc-29__eq i:nth-child(4) {
  animation-duration: .52s;
  animation-delay: .18s;
}

.acc-29__item[open] .acc-29__eq i:nth-child(5) {
  animation-duration: .7s;
  animation-delay: .12s;
}

@keyframes acc-29-bounce {
  from {
    transform: scaleY(.15);
  }

  to {
    transform: scaleY(.9);
  }
}

.acc-29__len {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: var(--dim);
  flex: none;
}

.acc-29__body {
  padding: 2px 4px 18px 36px;
  font-size: 14px;
  line-height: 1.65;
  color: #a6adc4;
}

.acc-29__item[open] .acc-29__body {
  animation: acc-29-in .3s ease-out;
}

@keyframes acc-29-in {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

.acc-29__sum:focus-visible {
  outline: 3px solid var(--signal);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-29__item[open] .acc-29__eq i {
    animation: none;
  }

  .acc-29__item[open] .acc-29__eq i:nth-child(1) {
    transform: scaleY(.4);
  }

  .acc-29__item[open] .acc-29__eq i:nth-child(2) {
    transform: scaleY(.7);
  }

  .acc-29__item[open] .acc-29__eq i:nth-child(3) {
    transform: scaleY(.5);
  }

  .acc-29__item[open] .acc-29__eq i:nth-child(4) {
    transform: scaleY(.85);
  }

  .acc-29__item[open] .acc-29__eq i:nth-child(5) {
    transform: scaleY(.6);
  }

  .acc-29__item[open] .acc-29__body {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — five bars share one scaleY bounce keyframe at non-ratio durations/delays so the meter never visibly syncs; bars run only while details[open], and reduced-motion freezes them into a static staircase. */
```
