---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/progress-ring/"
title: "Podcast Play Button with SVG Progress Ring CSS"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "The episode card every podcast app ships: a circular progress ring wrapped around the play button, showing how far into the episode you are."
has_js: "true"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Podcast Play Button with SVG Progress Ring CSS
Source: https://codefronts.com/components/css-play-pause-buttons/progress-ring/

The episode card every podcast app ships: a circular progress ring wrapped around the play button, showing how far into the episode you are. Built with SVG stroke-dashoffset (crisper caps and better control than a conic-gradient ring), driven by one custom property, with a resume-from-position state and a remaining-time readout that updates as it plays.
## HTML
```html
<section class="pp-20" aria-label="Podcast play button with SVG progress ring demo">
  <div class="pp-20__stage">
    <article class="pp-20__card" style="--pp-20-progress:.38">
      <img class="pp-20__cover" src="https://images.unsplash.com/photo-1487215078519-e21cc028cb29?q=80&w=400&auto=format&fit=crop" alt="" width="72" height="72" loading="lazy">
      <div class="pp-20__meta">
        <p class="pp-20__show">The Build Log · Ep. 214</p>
        <h3 class="pp-20__title">Shipping design systems that survive contact with users</h3>
        <p class="pp-20__left"><span class="pp-20__remain">38 min left</span> · <span class="pp-20__state">Paused</span></p>
      </div>
      <button class="pp-20__btn" type="button" aria-pressed="false">
        <svg class="pp-20__ring" viewBox="0 0 120 120" width="72" height="72" aria-hidden="true">
          <circle cx="60" cy="60" r="54" fill="none" stroke="currentColor" stroke-width="6" opacity=".18"/>
          <circle class="pp-20__arc" cx="60" cy="60" r="54" pathLength="1" fill="none" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>
        </svg>
        <svg class="pp-20__glyph" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">
          <path class="pp-20__p" d="M9.2 5.8v12.4L18.6 12z" fill="currentColor"/>
          <path class="pp-20__q" d="M8.8 5.8h3.1v12.4H8.8zM13 5.8h3.1v12.4H13z" fill="currentColor"/>
        </svg>
        <span class="pp-20__sr">Play episode 214</span>
      </button>
    </article>
    <p class="pp-20__chip" aria-hidden="true">pathLength=&quot;1&quot; · stroke-dashoffset: calc(1 - progress) · one property tick</p>
  </div>
</section>
```
## CSS
```css
.pp-20,
.pp-20 *,
.pp-20 *::before,
.pp-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-20-bg);
  --pp-20-bg: oklch(0.17 0.02 300);
  --pp-20-card: oklch(0.23 0.025 300);
  --pp-20-ink: oklch(0.97 0.006 300);
  --pp-20-mut: oklch(0.69 0.02 300);
  --pp-20-acc: oklch(0.8 0.15 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-20-ink);
}

.pp-20__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(70% 55% at 50% 6%,oklch(0.3 0.07 320/.5),transparent 72%);
}

.pp-20__card {
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
  width: min(100%,560px);
  padding: 24px;
  border-radius: 22px;
  background: var(--pp-20-card);
  box-shadow: 0 0 0 1px oklch(1 0 0/.07),0 26px 60px oklch(0 0 0/.5);
}

.pp-20__cover {
  width: 76px;
  height: 76px;
  border-radius: 16px;
  object-fit: cover;
  flex: none;
  background: linear-gradient(140deg,var(--pp-20-acc),oklch(0.5 0.14 30));
}

.pp-20__meta {
  flex: 1;
  min-width: 180px;
}

.pp-20__show {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .14em;
  color: var(--pp-20-acc);
  text-transform: uppercase;
}

.pp-20__title {
  font-size: 16.5px;
  font-weight: 640;
  line-height: 1.35;
  letter-spacing: -.012em;
  margin-top: 8px;
  text-wrap: pretty;
}

.pp-20__left {
  font-size: 12.5px;
  color: var(--pp-20-mut);
  margin-top: 9px;
  font-variant-numeric: tabular-nums;
}

.pp-20__btn {
  position: relative;
  display: grid;
  place-items: center;
  width: 72px;
  height: 72px;
  flex: none;
  border: 0;
  border-radius: 50%;
  background: transparent;
  color: var(--pp-20-acc);
  cursor: pointer;
  transition: transform .22s cubic-bezier(.34,1.4,.5,1);
}

.pp-20__btn:hover {
  transform: scale(1.06);
}

.pp-20__btn:focus-visible {
  outline: 3px solid var(--pp-20-acc);
  outline-offset: 4px;
  border-radius: 50%;
}

.pp-20__ring {
  position: absolute;
  inset: 0;
}

.pp-20__arc {
  stroke-dasharray: 1;
  stroke-dashoffset: calc(1 - var(--pp-20-progress));
  rotate: -90deg;
  transform-origin: center;
  transition: stroke-dashoffset .2s linear;
}

.pp-20__glyph {
  position: relative;
  color: var(--pp-20-ink);
}

.pp-20__q {
  display: none;
}

.pp-20__card[data-state="playing"] .pp-20__p {
  display: none;
}

.pp-20__card[data-state="playing"] .pp-20__q {
  display: block;
}

.pp-20__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pp-20__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-20-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-20 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.pp-20__card').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const btn = card.querySelector('.pp-20__btn');
    const remain = card.querySelector('.pp-20__remain');
    const state = card.querySelector('.pp-20__state');
    const sr = card.querySelector('.pp-20__sr');
    const total = 61;
    let p = 0.38, id = 0;
    const paint = () => {
      card.style.setProperty('--pp-20-progress', p.toFixed(4));
      remain.textContent = Math.max(0, Math.round(total * (1 - p))) + ' min left';
    };
    const stop = () => { clearInterval(id); id = 0; card.dataset.state = 'paused'; btn.setAttribute('aria-pressed', 'false'); state.textContent = 'Paused'; sr.textContent = 'Play episode 214'; };
    btn.addEventListener('click', () => {
      if (id) return stop();
      card.dataset.state = 'playing'; btn.setAttribute('aria-pressed', 'true');
      state.textContent = 'Playing'; sr.textContent = 'Pause episode 214';
      id = setInterval(() => { p = p >= 1 ? 0 : p + 0.004; paint(); }, 250);
    });
    paint();
  });
})();
```
