---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/draggable-glass-kanban-card/"
title: "Draggable Glass Kanban Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A Kanban board card made of Liquid Glass that you can pick up and drag — it tilts and bends toward the drag direction with inertia, casts a deeper shadow as…"
has_js: "true"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Draggable Glass Kanban Card
Source: https://codefronts.com/components/css-liquid-glass-cards/draggable-glass-kanban-card/

A Kanban board card made of Liquid Glass that you can pick up and drag — it tilts and bends toward the drag direction with inertia, casts a deeper shadow as it lifts, then springs flat when dropped. The frosted panel keeps the column behind it visible through the glass the whole time.
## HTML
```html
<section class="lg-02" aria-label="Draggable liquid glass kanban card demo">
  <div class="lg-02__col">
    <p class="lg-02__coltitle">In Progress</p>
    <article class="lg-02__card" id="lg-02-card" tabindex="0" aria-grabbed="false" aria-label="Task: Redesign onboarding. Drag or use arrow keys to move.">
      <span class="lg-02__tag">Design</span>
      <h3 class="lg-02__title">Redesign onboarding flow</h3>
      <p class="lg-02__meta">3 subtasks · Due Fri</p>
      <div class="lg-02__foot"><span class="lg-02__ava" aria-hidden="true">◍</span><span class="lg-02__grip" aria-hidden="true">⠿ drag me</span></div>
    </article>
    <p class="lg-02__live" aria-live="polite"></p>
  </div>
</section>
```
## CSS
```css
.lg-02,
.lg-02 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --dx {
  syntax: '<number>';
  inherits: false;
  initial-value: 0;
}

@property --lift {
  syntax: '<number>';
  inherits: false;
  initial-value: 0;
}

@property --px {
  syntax: '<length>';
  inherits: false;
  initial-value: 0px;
}

@property --py {
  syntax: '<length>';
  inherits: false;
  initial-value: 0px;
}

.lg-02 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 90deg at 30% 40%,#2563eb,#7c3aed,#db2777,#2563eb);
  background-size: 220% 220%;
  animation: lg-02-bg 22s ease-in-out infinite;
}

@keyframes lg-02-bg {
  50% {
    background-position: 100% 100%;
  }
}

.lg-02__col {
  width: min(300px,100%);
  padding: 14px;
  border-radius: 20px;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.2);
}

.lg-02__coltitle {
  color: #fff;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  margin-bottom: 12px;
  opacity: .85;
}

.lg-02__card {
  --dx: 0;
  --lift: 0;
  --px: 0px;
  --py: 0px;
  position: relative;
  padding: 16px;
  border-radius: 16px;
  cursor: grab;
  touch-action: none;
  isolation: isolate;
  background: color-mix(in oklab,white 14%,transparent);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.55),0 calc(10px + var(--lift)*22px) calc(20px + var(--lift)*34px) -14px rgba(0,0,0,.7);
  backdrop-filter: blur(18px) saturate(180%);
  -webkit-backdrop-filter: blur(18px) saturate(180%);
  transform: perspective(700px) translate3d(var(--px),var(--py),0) rotate(calc(var(--dx)*0.05deg)) skewX(calc(var(--dx)*0.04deg)) scale(calc(1 + var(--lift)*0.03));
  transition: --dx .5s cubic-bezier(.2,1.3,.4,1),--lift .4s ease,--px .5s cubic-bezier(.2,1.3,.4,1),--py .5s cubic-bezier(.2,1.3,.4,1),box-shadow .4s ease;
}

.lg-02__card.is-drag {
  cursor: grabbing;
  transition: none;
}

.lg-02__card:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.lg-02__tag {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  color: #fff;
  padding: 3px 9px;
  border-radius: 999px;
  background: rgba(255,255,255,.22);
}

.lg-02__title {
  color: #fff;
  font-size: 16px;
  font-weight: 700;
  margin: 10px 0 6px;
  line-height: 1.3;
}

.lg-02__meta {
  color: rgba(255,255,255,.75);
  font-size: 13px;
}

.lg-02__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 14px;
  color: rgba(255,255,255,.8);
}

.lg-02__ava {
  font-size: 20px;
}

.lg-02__grip {
  font-size: 12px;
  font-weight: 600;
}

.lg-02__live {
  color: #fff;
  font-size: 12px;
  min-height: 1.2em;
  margin-top: 10px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-02 {
    animation: none;
  }

  .lg-02__card {
    transition: box-shadow .2s;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('#lg-02-card');
  const live = document.querySelector('.lg-02__live');
  if (!card) return;
  let dragging = false, startX = 0, startY = 0, lastX = 0, raf;
  const set = (k,v) => card.style.setProperty(k, v);
  card.addEventListener('pointerdown', (e) => {
    dragging = true;
    startX = lastX = e.clientX;
    startY = e.clientY;
    card.classList.add('is-drag');
    card.setAttribute('aria-grabbed','true');
    card.setPointerCapture(e.pointerId);
    set('--lift', 1);
    live.textContent = 'Grabbed. Drag to move.';
  });
  card.addEventListener('pointermove', (e) => {
    if (!dragging) return;
    const vx = e.clientX - lastX; lastX = e.clientX;
    const px = e.clientX - startX;
    const py = e.clientY - startY;
    cancelAnimationFrame(raf);
    raf = requestAnimationFrame(() => {
      set('--px', px + 'px');
      set('--py', py + 'px');
      set('--dx', Math.max(-30, Math.min(30, vx * 3)));
    });
  });
  const end = () => {
    if (!dragging) return; dragging = false;
    card.classList.remove('is-drag');
    card.setAttribute('aria-grabbed','false');
    set('--dx', 0); set('--lift', 0);
    set('--px', '0px'); set('--py', '0px');
    live.textContent = 'Dropped.';
  };
  card.addEventListener('pointerup', end);
  card.addEventListener('pointercancel', end);
  card.addEventListener('keydown', (e) => {
    if (!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key)) return;
    e.preventDefault();
    const step = 40;
    let dxKey = 0, pxDelta = 0, pyDelta = 0;
    if (e.key === 'ArrowRight') { pxDelta = step;  dxKey = 24; }
    if (e.key === 'ArrowLeft')  { pxDelta = -step; dxKey = -24; }
    if (e.key === 'ArrowDown')  { pyDelta = step; }
    if (e.key === 'ArrowUp')    { pyDelta = -step; }
    const cur = getComputedStyle(card);
    const curPx = parseFloat(cur.getPropertyValue('--px')) || 0;
    const curPy = parseFloat(cur.getPropertyValue('--py')) || 0;
    set('--px', (curPx + pxDelta) + 'px');
    set('--py', (curPy + pyDelta) + 'px');
    if (dxKey) set('--dx', dxKey);
    live.textContent = 'Nudged.';
    setTimeout(() => set('--dx', 0), 260);
  });
})();
```
