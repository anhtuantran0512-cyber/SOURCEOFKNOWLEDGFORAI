---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/text-marquee-speed-up-on-hover/"
title: "Text Marquee Speed-Up on Hover"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "The streetwear ticker with the acceleration everyone gets wrong: the loop is pure CSS (duplicated content, translateX to -50%, seamless forever), and…"
has_js: "true"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Text Marquee Speed-Up on Hover
Source: https://codefronts.com/motion/css-text-hover-effects/text-marquee-speed-up-on-hover/

The streetwear ticker with the acceleration everyone gets wrong: the loop is pure CSS (duplicated content, translateX to -50%, seamless forever), and hovering makes it SURGE smoothly — because 16 lines of JS grab the CSS animation through the Web Animations API and call updatePlaybackRate(4), which velocity-matches instead of teleporting. Changing animation-duration in CSS snaps the phase (the naive approach visibly jumps); updatePlaybackRate is the engine-level 'same tape, faster motor'. Includes the legally-required-by-taste pause button, wired to the same API.
## HTML
```html
<section class="cth-26" aria-label="Marquee speed up on hover demo">
  <div class="cth-26__stage">
    <div class="cth-26__scene">
      <header class="cth-26__head">
        <h1>ARCHIVE&nbsp;/&nbsp;004</h1>
        <button class="cth-26__pause" type="button" aria-pressed="false">Pause tickers</button>
      </header>
      <div class="cth-26__bar cth-26__bar--a" id="cth26-top">
        <div class="cth-26__track" data-marquee>
          <p class="cth-26__group">NEW DROP 004 &#9670; FREE SHIPPING OVER $120 &#9670; STORE OPENS FRI 10:00 &#9670; NO RESTOCKS &#9670;&nbsp;</p>
          <p class="cth-26__group" aria-hidden="true">NEW DROP 004 &#9670; FREE SHIPPING OVER $120 &#9670; STORE OPENS FRI 10:00 &#9670; NO RESTOCKS &#9670;&nbsp;</p>
        </div>
      </div>
      <div class="cth-26__bar cth-26__bar--b">
        <div class="cth-26__track cth-26__track--rev" data-marquee>
          <p class="cth-26__group">WORLDWIDE &#9671; 100% RECYCLED FLEECE &#9671; SIZE RUNS BIG &#9671; MEMBERS EARLY ACCESS THU &#9671;&nbsp;</p>
          <p class="cth-26__group" aria-hidden="true">WORLDWIDE &#9671; 100% RECYCLED FLEECE &#9671; SIZE RUNS BIG &#9671; MEMBERS EARLY ACCESS THU &#9671;&nbsp;</p>
        </div>
      </div>
      <p class="cth-26__hint">Hover a strip: <code>anim.updatePlaybackRate(4)</code> surges it with zero phase jump &mdash; the thing a CSS duration swap can't do. Counter-flow directions are the streetwear tell.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-26,
.cth-26 *,
.cth-26 *::before,
.cth-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-26 {
  --bg: oklch(0.96 0.005 90);
  --ink: oklch(0.17 0.005 90);
  --paper: oklch(0.99 0.002 90);
  --acc: oklch(0.62 0.21 30);
  --mut: oklch(0.48 0.01 90);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-26__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: var(--bg);
  padding: clamp(20px,4vw,56px) 0;
  container: cth26/inline-size;
  overflow: clip;
}

.cth-26__scene {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: clamp(22px,4cqi,36px);
}

.cth-26__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 0 clamp(20px,5cqi,64px);
}

.cth-26__head h1 {
  font-size: clamp(30px,6cqi,54px);
  font-weight: 900;
  letter-spacing: -.04em;
}

.cth-26__pause {
  min-height: 46px;
  padding: 0 20px;
  border-radius: 99px;
  border: 2px solid var(--ink);
  background: var(--paper);
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .06em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background .25s,color .25s;
}

.cth-26__pause:hover {
  background: var(--ink);
  color: var(--paper);
}

.cth-26__pause[aria-pressed="true"] {
  background: var(--acc);
  border-color: var(--acc);
  color: var(--paper);
}

.cth-26__pause:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.cth-26__bar {
  overflow: clip;
  padding: 14px 0;
  cursor: pointer;
}

.cth-26__bar--a {
  background: var(--ink);
  color: var(--paper);
  rotate: -1.6deg;
  scale: 1.02 1;
}

.cth-26__bar--b {
  background: var(--acc);
  color: var(--paper);
  rotate: 1.2deg;
  scale: 1.02 1;
  margin-top: -4px;
}

.cth-26__track {
  display: flex;
  width: max-content;
  animation: cth26-roll 16s linear infinite;
}

.cth-26__track--rev {
  animation: cth26-roll 22s linear infinite reverse;
}

@keyframes cth26-roll {
  to {
    transform: translateX(-50%);
  }
}

.cth-26__group {
  font-size: clamp(17px,3cqi,26px);
  font-weight: 850;
  letter-spacing: .04em;
  white-space: nowrap;
  padding-right: .5em;
}

.cth-26__hint {
  padding: 0 clamp(20px,5cqi,64px);
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 64ch;
}

.cth-26__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.9 0.008 90);
  padding: 1px 6px;
  border-radius: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .cth-26__track {
    animation-play-state: paused;
  }
}
```

## JavaScript
```js
(function(){
  var reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var tracks=[].slice.call(document.querySelectorAll('[data-marquee]'));
  var anims=tracks.map(function(t){
    var a=(t.getAnimations?t.getAnimations():[]).filter(function(x){return x.animationName==='cth26-roll';})[0];
    if(a&&reduced)a.pause();
    return a;
  }).filter(Boolean);
  tracks.forEach(function(t,i){
    var bar=t.parentElement,a=anims[i];
    if(!a)return;
    bar.addEventListener('pointerenter',function(){a.updatePlaybackRate(4);});
    bar.addEventListener('pointerleave',function(){a.updatePlaybackRate(1);});
  });
  var btn=document.querySelector('.cth-26__pause');
  if(btn)btn.addEventListener('click',function(){
    var pause=btn.getAttribute('aria-pressed')!=='true';
    btn.setAttribute('aria-pressed',String(pause));
    btn.textContent=pause?'Play tickers':'Pause tickers';
    anims.forEach(function(a){pause?a.pause():a.play();});
  });
})();
```
