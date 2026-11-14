---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/spotify-inspired-circular-play-button/"
title: "Spotify-Inspired Circular Play Button"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "The streaming-app interaction pattern, rebuilt from scratch: an album card whose circular accent button lifts and fades in on hover or keyboard focus, scales…"
has_js: "true"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Spotify-Inspired Circular Play Button
Source: https://codefronts.com/components/css-play-pause-buttons/spotify-inspired-circular-play-button/

The streaming-app interaction pattern, rebuilt from scratch: an album card whose circular accent button lifts and fades in on hover or keyboard focus, scales up on press, and stays permanently visible once the track is playing. It's the small choreography — translateY + opacity on the card, scale on the button, a color shift on the title — that makes catalog grids feel alive, and it's all four CSS rules.
## HTML
```html
<section class="pp-05" aria-label="Streaming style circular play button demo">
  <div class="pp-05__stage">
    <article class="pp-05__card" data-state="paused">
      <div class="pp-05__artwrap">
        <img class="pp-05__art" src="https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?q=80&w=600&auto=format&fit=crop" alt="" width="240" height="240" loading="lazy">
        <button class="pp-05__btn" type="button" aria-pressed="false">
          <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">
            <path class="pp-05__p" d="M8.6 5.4v13.2L19 12z" fill="currentColor"/>
            <path class="pp-05__q" d="M8 5h3.1v14H8zM12.9 5H16v14h-3.1z" fill="currentColor"/>
          </svg>
          <span class="pp-05__sr">Play Neon Harbour by Static Bloom</span>
        </button>
        <span class="pp-05__eq" aria-hidden="true"><b></b><b></b><b></b><b></b></span>
      </div>
      <h3 class="pp-05__title">Neon Harbour</h3>
      <p class="pp-05__sub">Static Bloom · 2026</p>
    </article>
    <p class="pp-05__chip" aria-hidden="true">:focus-within reveal · sticky data-state · independent translate + scale</p>
  </div>
</section>
```
## CSS
```css
.pp-05,
.pp-05 *,
.pp-05 *::before,
.pp-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-05-bg);
  --pp-05-bg: oklch(0.16 0.008 260);
  --pp-05-card: oklch(0.22 0.01 260);
  --pp-05-ink: oklch(0.97 0.004 250);
  --pp-05-mut: oklch(0.66 0.012 260);
  --pp-05-acc: oklch(0.79 0.19 148);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-05-ink);
}

.pp-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
}

.pp-05__card {
  width: min(100%,260px);
  padding: 16px;
  border-radius: 16px;
  background: var(--pp-05-card);
  transition: background .3s;
}

.pp-05__card:hover,
.pp-05__card:focus-within {
  background: oklch(0.27 0.012 260);
}

.pp-05__artwrap {
  position: relative;
  margin-bottom: 16px;
}

.pp-05__art {
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
  border-radius: 10px;
  display: block;
  background: linear-gradient(140deg,oklch(0.55 0.14 165),oklch(0.3 0.08 230));
  box-shadow: 0 10px 26px oklch(0 0 0/.5);
}

.pp-05__btn {
  position: absolute;
  right: 10px;
  bottom: 10px;
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  border: 0;
  border-radius: 50%;
  background: var(--pp-05-acc);
  color: oklch(0.18 0.03 150);
  cursor: pointer;
  opacity: 0;
  translate: 0 12px;
  box-shadow: 0 8px 20px oklch(0 0 0/.5);
  transition: opacity .28s,translate .28s cubic-bezier(.34,1.4,.5,1),scale .18s;
}

.pp-05__card:hover .pp-05__btn,
.pp-05__card:focus-within .pp-05__btn,
.pp-05__card[data-state="playing"] .pp-05__btn {
  opacity: 1;
  translate: 0 0;
}

.pp-05__btn:hover {
  scale: 1.08;
}

.pp-05__btn:active {
  scale: .94;
}

.pp-05__btn:focus-visible {
  outline: 3px solid var(--pp-05-ink);
  outline-offset: 3px;
}

.pp-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pp-05__q {
  display: none;
}

.pp-05__card[data-state="playing"] .pp-05__p {
  display: none;
}

.pp-05__card[data-state="playing"] .pp-05__q {
  display: block;
}

.pp-05__eq {
  position: absolute;
  left: 10px;
  bottom: 14px;
  display: flex;
  align-items: flex-end;
  gap: 3px;
  height: 18px;
  opacity: 0;
  transition: opacity .3s;
}

.pp-05__eq b {
  width: 3px;
  height: 35%;
  border-radius: 2px;
  background: var(--pp-05-acc);
  animation: pp-05-eq .8s ease-in-out infinite alternate;
  animation-play-state: paused;
}

.pp-05__eq b:nth-child(2) {
  animation-delay: -.2s;
}

.pp-05__eq b:nth-child(3) {
  animation-delay: -.5s;
}

.pp-05__eq b:nth-child(4) {
  animation-delay: -.75s;
}

.pp-05__card[data-state="playing"] .pp-05__eq {
  opacity: 1;
}

.pp-05__card[data-state="playing"] .pp-05__eq b {
  animation-play-state: running;
}

@keyframes pp-05-eq {
  from {
    height: 22%;
  }

  to {
    height: 100%;
  }
}

.pp-05__title {
  font-size: 16px;
  font-weight: 650;
  letter-spacing: -.01em;
  transition: color .25s;
}

.pp-05__card:hover .pp-05__title {
  color: var(--pp-05-acc);
}

.pp-05__sub {
  font-size: 13px;
  color: var(--pp-05-mut);
  margin-top: 4px;
}

.pp-05__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-05-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.12);
  border-radius: 99px;
  text-align: center;
}

@media (hover: none) {
  .pp-05__btn {
    opacity: 1;
    translate: 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pp-05 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const cards = document.querySelectorAll('.pp-05__card');
  cards.forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const btn = card.querySelector('.pp-05__btn');
    const sr = card.querySelector('.pp-05__sr');
    const name = card.querySelector('.pp-05__title').textContent;
    btn.addEventListener('click', () => {
      const next = card.dataset.state !== 'playing';
      cards.forEach((c) => { if (c !== card) { c.dataset.state = 'paused'; c.querySelector('.pp-05__btn').setAttribute('aria-pressed', 'false'); } });
      card.dataset.state = next ? 'playing' : 'paused';
      btn.setAttribute('aria-pressed', String(next));
      sr.textContent = (next ? 'Pause ' : 'Play ') + name;
    });
  });
})();
```
