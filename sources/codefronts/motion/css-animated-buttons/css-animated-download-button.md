---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-animated-download-button/"
title: "CSS Animated Download Button"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "A download CTA button where clicking triggers a bouncing arrow animation, a progress bar fill, and a completion state — all using CSS transitions and…"
has_js: "true"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Download Button
Source: https://codefronts.com/motion/css-animated-buttons/css-animated-download-button/

A download CTA button where clicking triggers a bouncing arrow animation, a progress bar fill, and a completion state — all using CSS transitions and keyframes toggled by JS class changes.
## HTML
```html
<div class="ab-13">
  <p class="ab-13__label">Click the button to download</p>
  <button class="ab-13__btn" id="ab-13-btn">
    <svg class="ab-13__icon" id="ab-13-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
      <polyline points="7 10 12 15 17 10"/>
      <line x1="12" y1="15" x2="12" y2="3"/>
    </svg>
    <span class="ab-13__text" id="ab-13-text">Download v2.4.1</span>
  </button>
  <p class="ab-13__size">macOS · 48.2 MB</p>
</div>
```
## CSS
```css
.ab-13,
.ab-13 *,
.ab-13 *::before,
.ab-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-13 ::selection {
  background: #2563eb;
  color: #fff;
}

.ab-13 {
  font-family: system-ui,sans-serif;
  background: #f0f4ff;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1.25rem;
  padding: 2rem;
}

.ab-13__label,
.ab-13__size {
  font-size: .78rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: #64748b;
}

.ab-13__btn {
  position: relative;
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  gap: .65rem;
  padding: .9rem 2.4rem;
  font-size: 1rem;
  font-weight: 700;
  color: #fff;
  background: #2563eb;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  outline: none;
  transition: background .3s,box-shadow .3s,transform .15s;
  box-shadow: 0 4px 16px rgba(37,99,235,.4);
}

.ab-13__btn:hover:not(.is-downloading):not(.is-done) {
  filter: brightness(1.08);
  transform: translateY(-2px);
}

.ab-13__btn:active {
  transform: translateY(0);
}

.ab-13__btn::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 3px;
  background: rgba(255,255,255,.55);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 2s linear;
  pointer-events: none;
}

.ab-13__btn.is-downloading {
  background: #1d4ed8;
  cursor: not-allowed;
}

.ab-13__btn.is-downloading::after {
  transform: scaleX(1);
}

.ab-13__btn.is-done {
  background: #059669;
  box-shadow: 0 4px 16px rgba(5,150,105,.4);
}

.ab-13__icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
  transition: transform .2s;
}

.ab-13__btn.is-downloading .ab-13__icon {
  animation: ab-13-bounce .6s ease-in-out infinite;
}

.ab-13__btn.is-done .ab-13__icon {
  animation: none;
  transform: rotate(0);
}

@keyframes ab-13-bounce {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(4px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ab-13__btn.is-downloading .ab-13__icon {
    animation: none;
  }

  .ab-13__btn::after {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var btn=document.getElementById('ab-13-btn');
  var txt=document.getElementById('ab-13-text');
  var icon=document.getElementById('ab-13-icon');
  if(!btn||!txt)return;
  var CHECK='<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/>';
  var DONE_ICON='<polyline points="20 6 9 17 4 12"/>';
  var orig=icon.innerHTML;
  var downloading=false;
  btn.addEventListener('click',function(){
    if(downloading||btn.classList.contains('is-done'))return;
    downloading=true;
    btn.classList.add('is-downloading');
    txt.textContent='Downloading…';
    setTimeout(function(){
      btn.classList.remove('is-downloading');
      btn.classList.add('is-done');
      icon.innerHTML=DONE_ICON;
      txt.textContent='Downloaded!';
      setTimeout(function(){
        btn.classList.remove('is-done');
        icon.innerHTML=orig;
        txt.textContent='Download v2.4.1';
        downloading=false;
      },2000);
    },2200);
  });
})();
```
