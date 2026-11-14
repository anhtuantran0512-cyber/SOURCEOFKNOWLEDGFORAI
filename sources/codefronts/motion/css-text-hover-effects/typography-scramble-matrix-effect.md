---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/typography-scramble-matrix-effect/"
title: "Typography Scramble / Matrix Effect"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Labels that decrypt under the cursor: on hover, every character cycles through random glyphs, then resolves to the real text left-to-right like a codebreaker…"
has_js: "true"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Typography Scramble / Matrix Effect
Source: https://codefronts.com/motion/css-text-hover-effects/typography-scramble-matrix-effect/

Labels that decrypt under the cursor: on hover, every character cycles through random glyphs, then resolves to the real text left-to-right like a codebreaker locking digits. The 22-line engine is the honest minimum — original strings cached in data-text, one interval per element, resolve speed proportional to position — and the CSS does the part JS versions always botch: monospace + a min-width in ch units, so the row NEVER changes width mid-scramble. Phosphor-green security-console styling included, as the search intent demands.
## HTML
```html
<section class="cth-17" aria-label="Text scramble decrypt demo">
  <div class="cth-17__stage">
    <div class="cth-17__term">
      <header class="cth-17__bar"><i></i><i></i><i></i><span>krypta &mdash; ops console v3.1</span></header>
      <p class="cth-17__log">&gt; session verified &middot; clearance <b>ONYX</b> &middot; 3 actions armed</p>
      <nav class="cth-17__menu" aria-label="Operations">
        <a class="cth-17__op" href="#cth17-top" id="cth17-top" data-text="ACCESS THE VAULT" style="min-width:16ch">ACCESS THE VAULT</a>
        <a class="cth-17__op" href="#cth17-top" data-text="ROTATE ALL KEYS" style="min-width:15ch">ROTATE ALL KEYS</a>
        <a class="cth-17__op" href="#cth17-top" data-text="BURN THIS SESSION" style="min-width:17ch">BURN THIS SESSION</a>
      </nav>
      <p class="cth-17__hint">Hover an action &mdash; characters cycle, then lock left to right. Monospace + <code>ch</code> widths keep the row from breathing.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-17,
.cth-17 *,
.cth-17 *::before,
.cth-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-17 {
  --bg: oklch(0.14 0.01 155);
  --panel: oklch(0.18 0.015 155);
  --ink: oklch(0.87 0.12 150);
  --dim: oklch(0.55 0.06 150);
  --hot: oklch(0.92 0.16 145);
  --line: oklch(0.3 0.03 152);
  font-family: ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;
  color: var(--ink);
}

.cth-17__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(100% 80% at 50% 0%,oklch(0.17 0.014 155),var(--bg) 70%);
  padding: clamp(20px,4vw,56px);
  container: cth17/inline-size;
}

.cth-17__term {
  width: min(100%,640px);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 24px 70px oklch(0.05 0.02 155/.55),0 0 0 1px oklch(0.1 0.02 155);
  position: relative;
}

.cth-17__term::after {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(0deg,oklch(0 0 0/.14) 0 1px,transparent 1px 3px);
  mix-blend-mode: multiply;
}

.cth-17__bar {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 12px 16px;
  border-bottom: 1px solid var(--line);
  background: oklch(0.16 0.012 155);
}

.cth-17__bar i {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--line);
}

.cth-17__bar i:first-child {
  background: oklch(0.6 0.16 25);
}

.cth-17__bar span {
  margin-left: 8px;
  font-size: 11.5px;
  letter-spacing: .08em;
  color: var(--dim);
}

.cth-17__log {
  padding: 18px 20px 4px;
  font-size: 12.5px;
  line-height: 1.8;
  color: var(--dim);
}

.cth-17__log b {
  color: var(--hot);
  font-weight: 700;
}

.cth-17__menu {
  display: flex;
  flex-direction: column;
  padding: 12px 12px 8px;
}

.cth-17__op {
  display: flex;
  align-items: center;
  min-height: 52px;
  padding: 0 12px;
  font-size: clamp(15px,2.6cqi,19px);
  font-weight: 700;
  letter-spacing: .06em;
  color: var(--ink);
  text-decoration: none;
  border-radius: 8px;
  white-space: nowrap;
  transition: background .2s,color .2s,text-shadow .3s;
}

.cth-17__op::before {
  content: '> ';
  color: var(--dim);
  transition: color .2s;
}

.cth-17__op:hover,
.cth-17__op:focus-visible {
  background: oklch(0.22 0.025 152);
  color: var(--hot);
  text-shadow: 0 0 .5em color-mix(in oklch,var(--hot) 60%,transparent);
}

.cth-17__op:hover::before,
.cth-17__op:focus-visible::before {
  color: var(--hot);
}

.cth-17__op:focus-visible {
  outline: 1.5px solid var(--hot);
  outline-offset: -1px;
}

.cth-17__hint {
  padding: 10px 20px 20px;
  font-size: 11.5px;
  line-height: 1.7;
  color: var(--dim);
}

.cth-17__hint code {
  background: oklch(0.24 0.02 152);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .cth-17 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(function(){
  var CHARS='#$%&@[]{}<>/=+*^!?:;0123456789';
  var reduced=matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('.cth-17__op').forEach(function(el){
    function scramble(){
      if(reduced.matches)return;
      var txt=el.getAttribute('data-text'),tick=0;
      clearInterval(el._sc);
      el._sc=setInterval(function(){
        var out='';
        for(var i=0;i<txt.length;i++){
          out+=(tick>i*2.6||txt.charAt(i)===' ')?txt.charAt(i):CHARS.charAt((Math.random()*CHARS.length)|0);
        }
        el.textContent=out;
        if(tick++>txt.length*2.6+2){clearInterval(el._sc);el.textContent=txt;}
      },28);
    }
    el.addEventListener('pointerenter',scramble);
    el.addEventListener('focus',scramble);
  });
})();
```
