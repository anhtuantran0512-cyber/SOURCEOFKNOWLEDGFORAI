---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/constellation/"
title: "Constellation"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "A creative-agency / AI-dashboard login floating over an interactive particle field: drifting stars link into a constellation and lean toward the pointer,…"
has_js: "true"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Constellation
Source: https://codefronts.com/components/css-login-forms/constellation/

A creative-agency / AI-dashboard login floating over an interactive particle field: drifting stars link into a constellation and lean toward the pointer, while the form card sits cleanly above without swallowing clicks.
## HTML
```html
<section class="lf-29">
  <canvas class="lf-29__canvas" aria-hidden="true"></canvas>
  <form class="lf-29__card" novalidate>
    <h1 class="lf-29__h">Enter the network</h1>
    <p class="lf-29__sub">Sign in to your workspace.</p>
    <label class="lf-29__field"><span class="lf-29__label">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required></label>
    <label class="lf-29__field"><span class="lf-29__label">Password</span>
      <input type="password" autocomplete="current-password" placeholder="••••••••" required></label>
    <button class="lf-29__submit" type="submit">Connect</button>
  </form>
</section>
```
## CSS
```css
.lf-29,
.lf-29 *,
.lf-29 *::before,
.lf-29 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-29 {
  --accent: oklch(0.7 0.15 210);
  --radius: 14px;
  --field-h: 48px;
  position: relative;
  overflow: hidden;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: radial-gradient(circle at 50% 40%,#0f1830,#070a14);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-29__canvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
}

.lf-29__card {
  position: relative;
  z-index: 10;
  width: min(360px,100%);
  border-radius: 20px;
  padding: 34px 30px;
  color: #eaf0fa;
  display: flex;
  flex-direction: column;
  gap: 14px;
  background: rgba(14,22,42,.72);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(120,160,220,.22);
  box-shadow: 0 30px 80px -40px #000;
}

.lf-29__h {
  font-size: 24px;
  font-weight: 700;
}

.lf-29__sub {
  font-size: 13.5px;
  color: #9fb0cc;
  margin-top: -8px;
  margin-bottom: 4px;
}

.lf-29__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.lf-29__label {
  font-size: 13px;
  font-weight: 600;
  color: #b7c4dc;
}

.lf-29__field input {
  height: var(--field-h);
  border: 1.5px solid rgba(120,160,220,.3);
  border-radius: 11px;
  padding: 0 14px;
  font-size: 15px;
  color: #eaf0fa;
  background: rgba(10,16,32,.6);
  transition: border-color .18s,box-shadow .18s;
}

.lf-29__field input::placeholder {
  color: #6b7a97;
}

.lf-29__field input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.7 0.15 210/.25);
}

.lf-29__submit {
  height: var(--field-h);
  margin-top: 4px;
  border: 0;
  border-radius: 11px;
  cursor: pointer;
  color: #04121a;
  font-size: 15px;
  font-weight: 700;
  background: linear-gradient(90deg,oklch(0.78 0.14 200),oklch(0.75 0.15 230));
  transition: filter .18s,transform .12s;
}

.lf-29__submit:hover {
  filter: brightness(1.08);
}

.lf-29__submit:active {
  transform: scale(.985);
}

.lf-29__submit:focus-visible {
  outline: 3px solid oklch(0.7 0.15 210/.6);
  outline-offset: 3px;
}
```

## JavaScript
```js
const sec = document.querySelector('.lf-29');
const canvas = sec.querySelector('.lf-29__canvas');
const ctx = canvas.getContext('2d');
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
let w, h, dpr, parts = [];
const mouse = { x: -999, y: -999 };
const COUNT = 60, LINK = 130;
function resize() {
  dpr = Math.min(devicePixelRatio || 1, 2);
  w = canvas.clientWidth; h = canvas.clientHeight;
  canvas.width = w * dpr; canvas.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}
function init() {
  resize();
  parts = Array.from({ length: COUNT }, () => ({
    x: Math.random() * w, y: Math.random() * h,
    vx: (Math.random() - .5) * .4, vy: (Math.random() - .5) * .4
  }));
}
function frame() {
  ctx.clearRect(0, 0, w, h);
  for (const p of parts) {
    p.x += p.vx; p.y += p.vy;
    if (p.x < 0 || p.x > w) p.vx *= -1;
    if (p.y < 0 || p.y > h) p.vy *= -1;
    const dx = p.x - mouse.x, dy = p.y - mouse.y, d = Math.hypot(dx, dy);
    if (d < 100) { p.x += dx / d * 1.2; p.y += dy / d * 1.2; }
    ctx.beginPath(); ctx.arc(p.x, p.y, 1.6, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(150,200,255,.85)'; ctx.fill();
  }
  for (let i = 0; i < parts.length; i++) for (let j = i + 1; j < parts.length; j++) {
    const a = parts[i], b = parts[j], dist = Math.hypot(a.x - b.x, a.y - b.y);
    if (dist < LINK) {
      ctx.strokeStyle = 'rgba(120,180,255,' + (1 - dist / LINK) * .35 + ')';
      ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
    }
  }
  if (!reduce) requestAnimationFrame(frame);
}
sec.addEventListener('pointermove', (e) => {
  const r = canvas.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top;
});
sec.addEventListener('pointerleave', () => { mouse.x = mouse.y = -999; });
addEventListener('resize', () => { resize(); });
init(); frame();
```
