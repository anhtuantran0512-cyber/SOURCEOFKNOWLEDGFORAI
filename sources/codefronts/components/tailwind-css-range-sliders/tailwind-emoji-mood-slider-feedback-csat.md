---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-emoji-mood-slider-feedback-csat/"
title: "Tailwind CSS Emoji Mood Slider for Feedback & CSAT Surveys"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "A five-state feedback scale from miserable to elated, with a pulsing ring, a colour that shifts with the mood, and a star row that follows."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Emoji Mood Slider for Feedback & CSAT Surveys
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-emoji-mood-slider-feedback-csat/

A five-state feedback scale from miserable to elated, with a pulsing ring, a colour that shifts with the mood, and a star row that follows. The port turns a JS colour-assignment pile into one --mood property: the face tint, ring, label and stars all read it, so a new mood is one array entry and zero style writes.
## HTML
```html
<section class="trs-04 w-full min-h-svh grid place-items-center bg-trs04-bg font-trs04-sans px-5 py-10" id="trs-04-root" style="--mood:#f6d365">
  <div class="w-[min(420px,100%)] rounded-3xl bg-trs04-card border border-trs04-edge px-8 py-9 text-center">
    <h3 class="text-lg font-extrabold text-trs04-ink m-0">How do you feel today?</h3>
    <p class="text-[13px] text-trs04-mut mt-1.5 mb-8 m-0">Drag, or tap a face below</p>

    <div class="relative mx-auto size-25 mb-6 text-[var(--mood)]">
      <span class="absolute -inset-2 rounded-full border-2 border-current animate-trs04-pulse motion-reduce:animate-none" aria-hidden="true"></span>
      <div class="grid place-items-center size-25 rounded-full text-[62px] leading-none bg-[color-mix(in_oklab,var(--mood)_18%,transparent)] shadow-[0_10px_34px_-8px_oklch(0.1_0.05_300/0.6)]" id="trs-04-face" aria-hidden="true">😐</div>
    </div>

    <p class="text-xl font-extrabold tracking-tight text-(--mood) m-0" id="trs-04-label">Neutral</p>
    <p class="text-[13px] text-trs04-mut mt-1 mb-8 m-0" id="trs-04-sub">Could be better, could be worse</p>

    <div class="relative py-3.5 mb-3">
      <div class="h-2.5 rounded-full bg-gradient-to-r from-trs04-sad via-trs04-mid to-trs04-glad opacity-40" aria-hidden="true"></div>
      <input type="range" min="0" max="100" value="50" id="trs-04-inp" aria-label="Mood rating"
             class="absolute inset-0 w-full h-full appearance-none bg-transparent outline-none cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-trs04-ring rounded-full">
    </div>

    <div class="grid grid-cols-5 gap-1" id="trs-04-picks" role="group" aria-label="Pick a mood"></div>

    <div class="flex justify-center gap-1.5 mt-7" id="trs-04-stars" aria-hidden="true">
      <span class="text-xl grayscale transition-[filter,scale] duration-300 data-[on=true]:grayscale-0 data-[on=true]:scale-110 motion-reduce:transition-none">⭐</span>
      <span class="text-xl grayscale transition-[filter,scale] duration-300 data-[on=true]:grayscale-0 data-[on=true]:scale-110 motion-reduce:transition-none">⭐</span>
      <span class="text-xl grayscale transition-[filter,scale] duration-300 data-[on=true]:grayscale-0 data-[on=true]:scale-110 motion-reduce:transition-none">⭐</span>
      <span class="text-xl grayscale transition-[filter,scale] duration-300 data-[on=true]:grayscale-0 data-[on=true]:scale-110 motion-reduce:transition-none">⭐</span>
      <span class="text-xl grayscale transition-[filter,scale] duration-300 data-[on=true]:grayscale-0 data-[on=true]:scale-110 motion-reduce:transition-none">⭐</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs04-bg: #1a0a2e;
  --color-trs04-bg: oklch(0.22 0.08 300);
  --color-trs04-card: #241242;
  --color-trs04-card: oklch(0.27 0.09 300);
  --color-trs04-edge: #3d2070;
  --color-trs04-edge: oklch(0.36 0.12 300);
  --color-trs04-ink: #f0e6ff;
  --color-trs04-ink: oklch(0.94 0.03 300);
  --color-trs04-mut: #a68ed0;
  --color-trs04-mut: oklch(0.72 0.08 300);
  --color-trs04-sad: #667eea;
  --color-trs04-sad: oklch(0.62 0.16 275);
  --color-trs04-mid: #f6d365;
  --color-trs04-mid: oklch(0.87 0.13 90);
  --color-trs04-glad: #ff6b35;
  --color-trs04-glad: oklch(0.7 0.2 40);
  --color-trs04-ring: #ffffff;
  --color-trs04-ring: oklch(1 0 0);
  --font-trs04-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --animate-trs04-pulse: trs04-pulse 1.8s ease-out infinite;
}

@keyframes trs04-pulse {
  0% {
    transform: scale(0.92);
    opacity: 0.6;
  }

  100% {
    transform: scale(1.3);
    opacity: 0;
  }
}
/* Same rule as the numeric properties: a paint property that READS a var()
   freezes at first paint when it carries its own transition, because its
   declared token stream never changes. Register the colour and animate IT. */

@property --mood {
  syntax: "<color>";
  inherits: true;
  initial-value: oklch(0.87 0.13 90);
}

.trs-04 {
  width: 100%;
  min-height: 100svh;
  transition: --mood .4s ease;
}

@media (prefers-reduced-motion: reduce) {
  .trs-04 {
    transition: none;
  }
}
/* Thumb: a plain white disc, tinted by the active mood via a CSS variable. */

.trs-04 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 28px;
  height: 28px;
  border-radius: 9999px;
  background: #fff;
  border: 3px solid var(--mood, #ccc);
  box-shadow: 0 4px 16px oklch(0.1 0.05 300 / 0.5);
  cursor: grab;
  transition: border-color .3s, transform .15s;
}

.trs-04 input[type="range"]:active::-webkit-slider-thumb {
  transform: scale(1.18);
  cursor: grabbing;
}

.trs-04 input[type="range"]::-moz-range-thumb {
  width: 28px;
  height: 28px;
  border-radius: 9999px;
  background: #fff;
  border: 3px solid var(--mood, #ccc);
  cursor: grab;
}

@media (prefers-reduced-motion: reduce) {
  .trs-04 input[type="range"]::-webkit-slider-thumb {
    transition: none;
  }

  .trs-04 input[type="range"]:active::-webkit-slider-thumb {
    transform: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-04-root');
  var inp = document.getElementById('trs-04-inp');
  var face = document.getElementById('trs-04-face');
  var label = document.getElementById('trs-04-label');
  var sub = document.getElementById('trs-04-sub');
  var picks = document.getElementById('trs-04-picks');
  var stars = Array.prototype.slice.call(document.getElementById('trs-04-stars').children);
  var MOODS = [
    { emoji: '😢', text: 'Terrible', sub: 'This really is not my day', color: 'oklch(0.62 0.16 275)' },
    { emoji: '😕', text: 'Not great', sub: 'Struggling a bit today', color: 'oklch(0.68 0.15 295)' },
    { emoji: '😐', text: 'Neutral', sub: 'Could be better, could be worse', color: 'oklch(0.87 0.13 90)' },
    { emoji: '😊', text: 'Good', sub: 'Things are looking up', color: 'oklch(0.76 0.17 60)' },
    { emoji: '😎', text: 'Amazing', sub: 'Absolutely crushing it today', color: 'oklch(0.7 0.2 40)' }
  ];
  var lastIdx = -1;

  MOODS.forEach(function(m, i){
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'grid place-items-center min-h-11 rounded-xl text-xl bg-white/5 border border-transparent transition-colors duration-200 hover:bg-white/12 data-[sel=true]:border-current data-[sel=true]:text-[var(--mood)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs04-ring motion-reduce:transition-none';
    b.innerHTML = '<span aria-hidden="true">' + m.emoji + '</span><span class="sr-only">' + m.text + '</span>';
    b.addEventListener('click', function(){ inp.value = i * 25; update(); });
    picks.appendChild(b);
  });
  var buttons = Array.prototype.slice.call(picks.children);

  function update(){
    var v = +inp.value;
    var idx = Math.min(MOODS.length - 1, Math.floor(v / 100 * MOODS.length));
    var m = MOODS[idx];
    root.style.setProperty('--mood', m.color);
    face.textContent = m.emoji;
    label.textContent = m.text;
    sub.textContent = m.sub;
    inp.setAttribute('aria-valuetext', m.text + ', ' + v + ' of 100');
    buttons.forEach(function(b, i){ b.dataset.sel = i === idx ? 'true' : 'false'; });
    var on = Math.round(v / 100 * 5);
    stars.forEach(function(s, i){ s.dataset.on = i < on ? 'true' : 'false'; });
    if (idx !== lastIdx && lastIdx !== -1 && navigator.vibrate) navigator.vibrate(12);
    lastIdx = idx;
  }
  inp.addEventListener('input', update);
  update();
})();
```
