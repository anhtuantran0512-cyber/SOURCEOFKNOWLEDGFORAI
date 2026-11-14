---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-particle-constellation-login-canvas/"
title: "Tailwind Particle Constellation Login over Canvas"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "A creative-agency login floating over an interactive particle field: drifting stars link into a constellation and lean away from the pointer, while the form…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Particle Constellation Login over Canvas
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-particle-constellation-login-canvas/

A creative-agency login floating over an interactive particle field: drifting stars link into a constellation and lean away from the pointer, while the form sits cleanly above without swallowing clicks. The port's load-bearing utility is pointer-events-none on the canvas &mdash; two words that are the difference between a beautiful background and an unusable form.
## HTML
```html
<section class="tlf-29 relative w-full min-h-svh grid place-items-center overflow-hidden font-tlf29-sans p-6 bg-[radial-gradient(circle_at_50%_40%,oklch(0.25_0.06_265),oklch(0.12_0.02_265))]">
  <canvas aria-hidden="true" class="tlf-29-canvas absolute inset-0 z-1 w-full h-full pointer-events-none"></canvas>
  <form novalidate class="relative z-10 w-[min(380px,100%)] flex flex-col gap-3.5 p-8 rounded-[20px] bg-tlf29-card backdrop-blur-[8px] border border-tlf29-edge text-tlf29-ink shadow-[0_30px_80px_-40px_black]">
    <h1 class="text-2xl font-bold tracking-tight">Enter the network</h1>
    <p class="-mt-2 mb-1 text-[13.5px] text-tlf29-mut">Sign in to your workspace.</p>
    <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf29-label">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf29-ink bg-tlf29-field border-[1.5px] border-tlf29-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf29-ph focus-visible:outline-none focus-visible:border-tlf29-acc focus-visible:ring-4 focus-visible:ring-tlf29-halo"></label>
    <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf29-label">Password</span>
      <input type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf29-ink bg-tlf29-field border-[1.5px] border-tlf29-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf29-ph focus-visible:outline-none focus-visible:border-tlf29-acc focus-visible:ring-4 focus-visible:ring-tlf29-halo"></label>
    <button type="submit" class="mt-1 h-12 rounded-xl border-0 cursor-pointer text-tlf29-btnink text-[15px] font-bold bg-[linear-gradient(90deg,oklch(0.82_0.13_200),oklch(0.79_0.14_230))] transition-[filter,scale] duration-150 hover:brightness-105 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tlf29-ring motion-reduce:transition-none motion-reduce:active:scale-100">Connect</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf29-card: #0e162a;
  --color-tlf29-card: oklch(0.2 0.03 265 / 0.76);
  --color-tlf29-edge: #78a0dc;
  --color-tlf29-edge: oklch(0.6 0.05 255 / 0.3);
  --color-tlf29-field: #0a1020;
  --color-tlf29-field: oklch(0.16 0.025 265 / 0.6);
  --color-tlf29-ink: #eaf0fa;
  --color-tlf29-ink: oklch(0.95 0.01 255);
  --color-tlf29-label: #c3cee2;
  --color-tlf29-label: oklch(0.85 0.02 255);
  --color-tlf29-mut: #adbbd4;
  --color-tlf29-mut: oklch(0.78 0.025 255);
  --color-tlf29-ph: #8492ad;
  --color-tlf29-ph: oklch(0.63 0.03 255);
  --color-tlf29-acc: #6fc9e8;
  --color-tlf29-acc: oklch(0.78 0.12 210);
  --color-tlf29-halo: #a9dff2;
  --color-tlf29-halo: oklch(0.78 0.12 210 / 0.25);
  --color-tlf29-ring: #96d6ee;
  --color-tlf29-ring: oklch(0.78 0.12 210 / 0.6);
  --color-tlf29-btnink: #04121a;
  --color-tlf29-btnink: oklch(0.16 0.02 230);
  --font-tlf29-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tlf-29 {
  width: 100%;
  min-height: 100svh;
  color-scheme: dark;
}
/* Safari < 16.4 backdrop-filter prefix. */

.tlf-29 form {
  -webkit-backdrop-filter: blur(8px);
}
```

## JavaScript
```js
const section = document.querySelector('.tlf-29');
const canvas = section.querySelector('.tlf-29-canvas');
const ctx = canvas.getContext('2d');
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const COUNT = 60, LINK = 130;
const mouse = { x: -999, y: -999 };
let w, h, dpr, parts = [];

function resize() {
  dpr = Math.min(devicePixelRatio || 1, 2);
  w = canvas.clientWidth; h = canvas.clientHeight;
  canvas.width = w * dpr; canvas.height = h * dpr;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}

function init() {
  resize();
  parts = Array.from({ length: COUNT }, () => ({
    x: Math.random() * w,
    y: Math.random() * h,
    vx: (Math.random() - 0.5) * 0.4,
    vy: (Math.random() - 0.5) * 0.4
  }));
}

function draw(step) {
  ctx.clearRect(0, 0, w, h);
  for (const p of parts) {
    if (step) {
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0 || p.x > w) p.vx *= -1;
      if (p.y < 0 || p.y > h) p.vy *= -1;
      const dx = p.x - mouse.x, dy = p.y - mouse.y, d = Math.hypot(dx, dy);
      if (d < 100) { p.x += dx / d * 1.2; p.y += dy / d * 1.2; }
    }
    ctx.beginPath();
    ctx.arc(p.x, p.y, 1.6, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(160,210,255,0.85)';
    ctx.fill();
  }
  for (let i = 0; i < parts.length; i++) {
    for (let j = i + 1; j < parts.length; j++) {
      const a = parts[i], b = parts[j];
      const dist = Math.hypot(a.x - b.x, a.y - b.y);
      if (dist < LINK) {
        ctx.strokeStyle = 'rgba(130,190,255,' + (1 - dist / LINK) * 0.35 + ')';
        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
      }
    }
  }
  if (step) requestAnimationFrame(() => draw(true));
}

section.addEventListener('pointermove', (e) => {
  const r = canvas.getBoundingClientRect();
  mouse.x = e.clientX - r.left;
  mouse.y = e.clientY - r.top;
});
section.addEventListener('pointerleave', () => { mouse.x = mouse.y = -999; });
addEventListener('resize', () => { resize(); if (reduce) draw(false); });

init();
draw(!reduce);
```
