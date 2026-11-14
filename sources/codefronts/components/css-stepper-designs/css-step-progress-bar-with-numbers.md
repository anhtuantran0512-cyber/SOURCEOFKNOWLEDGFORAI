---
source: "codefronts"
url: "https://codefronts.com/components/css-stepper-designs/css-step-progress-bar-with-numbers/"
title: "CSS Step Progress Bar With Numbers"
section: "components"
category: "css-stepper-designs"
category_name: "CSS Steppers"
description: "Three synced numbered progress bar variants on one page — a pill track, a segmented block bar, and a dot-connector strip — all advancing together from a…"
has_js: "true"
---

Here's a working CSS Stepper from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Step Progress Bar With Numbers
Source: https://codefronts.com/components/css-stepper-designs/css-step-progress-bar-with-numbers/

Three synced numbered progress bar variants on one page — a pill track, a segmented block bar, and a dot-connector strip — all advancing together from a single prev/next controller.
## HTML
```html
<div class="stp-02">
  <span class="stp-02__label">CSS Step Progress Bar Components</span>

  <!-- Variant A: pill track -->
  <div class="stp-02__varA">
    <div class="stp-02__varA-title">Pill Track Style</div>
    <div class="stp-02__track" id="stp-02-pill">
      <div class="stp-02__pip done"><div class="stp-02__num">✓</div></div>
      <div class="stp-02__connector done"></div>
      <div class="stp-02__pip done"><div class="stp-02__num">✓</div></div>
      <div class="stp-02__connector done"></div>
      <div class="stp-02__pip active"><div class="stp-02__num">3</div></div>
      <div class="stp-02__connector"></div>
      <div class="stp-02__pip"><div class="stp-02__num">4</div></div>
      <div class="stp-02__connector"></div>
      <div class="stp-02__pip"><div class="stp-02__num">5</div></div>
    </div>
  </div>

  <!-- Variant B: bar with numbered markers -->
  <div class="stp-02__varB">
    <div class="stp-02__varA-title">Progress Bar With Numbered Markers</div>
    <div class="stp-02__bar-wrap">
      <div class="stp-02__bar-track"><div class="stp-02__bar-fill" id="stp-02-fill" style="width:37.5%"></div></div>
    </div>
    <div class="stp-02__markers" id="stp-02-markers">
      <div class="stp-02__marker done"><div class="stp-02__marker-dot">✓</div><span class="stp-02__marker-name">Start</span></div>
      <div class="stp-02__marker done"><div class="stp-02__marker-dot">✓</div><span class="stp-02__marker-name">Profile</span></div>
      <div class="stp-02__marker active"><div class="stp-02__marker-dot">3</div><span class="stp-02__marker-name">Payment</span></div>
      <div class="stp-02__marker"><div class="stp-02__marker-dot">4</div><span class="stp-02__marker-name">Shipping</span></div>
      <div class="stp-02__marker"><div class="stp-02__marker-dot">5</div><span class="stp-02__marker-name">Review</span></div>
      <div class="stp-02__marker"><div class="stp-02__marker-dot">6</div><span class="stp-02__marker-name">Done</span></div>
    </div>
  </div>

  <!-- Variant C: segmented blocks -->
  <div class="stp-02__varC">
    <div class="stp-02__varA-title">Segmented Block Style</div>
    <div class="stp-02__segments" id="stp-02-segs">
      <div class="stp-02__seg done"><span class="stp-02__seg-num">✓</span><span class="stp-02__seg-name">Account</span></div>
      <div class="stp-02__seg done"><span class="stp-02__seg-num">✓</span><span class="stp-02__seg-name">Address</span></div>
      <div class="stp-02__seg active"><span class="stp-02__seg-num">03</span><span class="stp-02__seg-name">Payment</span></div>
      <div class="stp-02__seg"><span class="stp-02__seg-num">04</span><span class="stp-02__seg-name">Review</span></div>
      <div class="stp-02__seg"><span class="stp-02__seg-num">05</span><span class="stp-02__seg-name">Confirm</span></div>
    </div>
  </div>

  <div class="stp-02__controls">
    <button class="stp-02__ctrl stp-02__ctrl--prev" id="stp-02-prev">← Prev</button>
    <button class="stp-02__ctrl stp-02__ctrl--next" id="stp-02-next">Next →</button>
  </div>
</div>
```
## CSS
```css
.stp-02,
.stp-02 *,
.stp-02 *::before,
.stp-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.stp-02 ::selection {
  background: #f97316;
  color: #fff;
}

.stp-02 {
  --bg: #fff8f0;
  --card: #fff;
  --orange: #f97316;
  --amber: #fb923c;
  --dark: #1a1207;
  --mid: #7a5533;
  --muted: #c4a882;
  --done: #10b981;
  --border: #ede0d4;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 48px;
}

.stp-02__label {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 600;
}
/* ── Variant A: pill track ── */

.stp-02__varA {
  width: 100%;
  max-width: 680px;
}

.stp-02__varA-title {
  font-size: 13px;
  font-weight: 600;
  color: var(--mid);
  margin-bottom: 20px;
  text-align: center;
}

.stp-02__track {
  display: flex;
  align-items: center;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 999px;
  padding: 8px 8px;
  box-shadow: 0 4px 24px rgba(249,115,22,.08);
}

.stp-02__pip {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
  position: relative;
}

.stp-02__num {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 700;
  background: var(--border);
  color: var(--muted);
  transition: all .35s ease;
}

.stp-02__pip.done .stp-02__num {
  background: var(--done);
  color: #fff;
}

.stp-02__pip.active .stp-02__num {
  background: var(--orange);
  color: #fff;
  box-shadow: 0 0 0 4px rgba(249,115,22,.2);
}

.stp-02__connector {
  flex: 1;
  height: 3px;
  background: var(--border);
  transition: background .35s;
}

.stp-02__connector.done {
  background: var(--done);
}
/* ── Variant B: numbered steps below bar ── */

.stp-02__varB {
  width: 100%;
  max-width: 680px;
}

.stp-02__bar-wrap {
  position: relative;
  margin-bottom: 24px;
}

.stp-02__bar-track {
  height: 6px;
  background: var(--border);
  border-radius: 3px;
  overflow: hidden;
}

.stp-02__bar-fill {
  height: 100%;
  width: 60%;
  background: linear-gradient(90deg,var(--orange),var(--amber));
  border-radius: 3px;
  transition: width .5s cubic-bezier(.4,0,.2,1);
}

.stp-02__markers {
  display: flex;
  justify-content: space-between;
  margin-top: 12px;
}

.stp-02__marker {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  cursor: pointer;
}

.stp-02__marker-dot {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
  background: var(--border);
  color: var(--muted);
  transition: all .3s;
  border: 2px solid var(--border);
}

.stp-02__marker.done .stp-02__marker-dot {
  background: var(--done);
  border-color: var(--done);
  color: #fff;
}

.stp-02__marker.active .stp-02__marker-dot {
  background: var(--orange);
  border-color: var(--orange);
  color: #fff;
  transform: scale(1.2);
}

.stp-02__marker-name {
  font-size: 11px;
  color: var(--muted);
  font-weight: 500;
  text-align: center;
  transition: color .3s;
}

.stp-02__marker.active .stp-02__marker-name {
  color: var(--orange);
  font-weight: 700;
}

.stp-02__marker.done .stp-02__marker-name {
  color: var(--done);
}
/* ── Variant C: segmented blocks ── */

.stp-02__varC {
  width: 100%;
  max-width: 680px;
}

.stp-02__segments {
  display: grid;
  grid-template-columns: repeat(5,1fr);
  gap: 6px;
}

.stp-02__seg {
  height: 56px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  background: var(--border);
  transition: all .3s;
  cursor: pointer;
}

.stp-02__seg-num {
  font-size: 16px;
  font-weight: 800;
  color: var(--muted);
}

.stp-02__seg-name {
  font-size: 9px;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--muted);
}

.stp-02__seg.done {
  background: linear-gradient(135deg,#d1fae5,#a7f3d0);
  border: 1px solid var(--done);
}

.stp-02__seg.done .stp-02__seg-num {
  color: var(--done);
}

.stp-02__seg.done .stp-02__seg-name {
  color: #059669;
}

.stp-02__seg.active {
  background: linear-gradient(135deg,var(--orange),var(--amber));
  box-shadow: 0 4px 20px rgba(249,115,22,.35);
}

.stp-02__seg.active .stp-02__seg-num,
.stp-02__seg.active .stp-02__seg-name {
  color: #fff;
}
/* controls */

.stp-02__controls {
  display: flex;
  gap: 12px;
}

.stp-02__ctrl {
  padding: 10px 24px;
  border-radius: 8px;
  border: none;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all .2s;
}

.stp-02__ctrl--prev {
  background: var(--border);
  color: var(--mid);
}

.stp-02__ctrl--prev:hover {
  background: var(--muted);
  color: #fff;
}

.stp-02__ctrl--next {
  background: var(--orange);
  color: #fff;
  box-shadow: 0 4px 16px rgba(249,115,22,.35);
}

.stp-02__ctrl--next:hover {
  background: #ea6a0a;
  transform: translateY(-1px);
}

@media (prefers-reduced-motion: reduce) {
  .stp-02__bar-fill,
    .stp-02__marker-dot,
    .stp-02__seg {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  let cur=3;
  const pillPips=document.querySelectorAll('.stp-02__pip');
  const pillCons=document.querySelectorAll('.stp-02__connector');
  const markers=document.querySelectorAll('.stp-02__marker');
  const fill=document.getElementById('stp-02-fill');
  const segs=document.querySelectorAll('.stp-02__seg');
  const total=6;

  function updateAll(){
    // pill (5 steps)
    pillPips.forEach((p,i)=>{
      p.classList.remove('done','active');
      if(i+1<cur) p.classList.add('done');
      else if(i+1===cur) p.classList.add('active');
      p.querySelector('.stp-02__num').textContent=i+1<cur?'✓':i+1;
    });
    pillCons.forEach((c,i)=>{c.classList.toggle('done',i+1<cur)});

    // bar markers (6)
    markers.forEach((m,i)=>{
      m.classList.remove('done','active');
      if(i+1<cur) m.classList.add('done');
      else if(i+1===cur) m.classList.add('active');
      m.querySelector('.stp-02__marker-dot').textContent=i+1<cur?'✓':i+1;
    });
    fill.style.width=((cur-1)/(total-1)*100)+'%';

    // segs (5 steps)
    segs.forEach((s,i)=>{
      s.classList.remove('done','active');
      if(i+1<cur) s.classList.add('done');
      else if(i+1===cur) s.classList.add('active');
      s.querySelector('.stp-02__seg-num').textContent=i+1<cur?'✓':String(i+1).padStart(2,'0');
    });
  }

  document.getElementById('stp-02-prev').addEventListener('click',()=>{cur=Math.max(1,cur-1);updateAll();});
  document.getElementById('stp-02-next').addEventListener('click',()=>{cur=Math.min(total,cur+1);updateAll();});
  updateAll();
})();
```
