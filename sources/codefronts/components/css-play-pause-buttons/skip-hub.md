---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/skip-hub/"
title: "Media Player Track Skip & Fast-Forward"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "A complete transport cluster — previous, rewind 15, play/pause, forward 30, next — with a real playlist behind it."
has_js: "true"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Media Player Track Skip & Fast-Forward
Source: https://codefronts.com/components/css-play-pause-buttons/skip-hub/

A complete transport cluster — previous, rewind 15, play/pause, forward 30, next — with a real playlist behind it. Skip buttons show their offset as text inside a circular arrow, exactly like podcast apps, and pressing next actually advances the track, updates the artwork and resets the scrubber. The layout is a five-column grid with the play button optically weighted, which is what makes a transport row feel balanced instead of arbitrary.
## HTML
```html
<section class="pp-11" aria-label="Media player skip and fast forward controls demo">
  <div class="pp-11__stage">
    <div class="pp-11__player" data-state="paused">
      <img class="pp-11__art" src="https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?q=80&w=500&auto=format&fit=crop" alt="" width="96" height="96" loading="lazy">
      <p class="pp-11__title">Signal to Noise</p>
      <p class="pp-11__sub">Episode 12 · 48 min</p>
      <div class="pp-11__scrub" aria-hidden="true"><b></b></div>
      <div class="pp-11__transport">
        <button class="pp-11__btn pp-11__btn--sm" type="button" data-act="prev" aria-label="Previous track">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M7 6v12M19 6l-9 6 9 6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/></svg>
        </button>
        <button class="pp-11__btn pp-11__btn--md" type="button" data-act="back" aria-label="Rewind 15 seconds">
          <svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path d="M12 5.5a6.5 6.5 0 1 1-6.3 8" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/><path d="M12 2.4v6.2L7.6 5.5z" fill="currentColor"/></svg>
          <span class="pp-11__num">15</span>
        </button>
        <button class="pp-11__btn pp-11__btn--lg" type="button" data-act="play" aria-pressed="false">
          <svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true">
            <path class="pp-11__p" d="M8.6 5.4v13.2L19 12z" fill="currentColor"/>
            <path class="pp-11__q" d="M8 5h3.1v14H8zM12.9 5H16v14h-3.1z" fill="currentColor"/>
          </svg>
          <span class="pp-11__sr">Play</span>
        </button>
        <button class="pp-11__btn pp-11__btn--md" type="button" data-act="fwd" aria-label="Fast forward 30 seconds">
          <svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path d="M12 5.5a6.5 6.5 0 1 0 6.3 8" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/><path d="M12 2.4v6.2l4.4-3.1z" fill="currentColor"/></svg>
          <span class="pp-11__num">30</span>
        </button>
        <button class="pp-11__btn pp-11__btn--sm" type="button" data-act="next" aria-label="Next track">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M17 6v12M5 6l9 6-9 6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/></svg>
        </button>
      </div>
      <p class="pp-11__live" role="status"></p>
    </div>
    <p class="pp-11__chip" aria-hidden="true">5-column transport grid · state → render() · labelled seek arcs</p>
  </div>
</section>
```
## CSS
```css
.pp-11,
.pp-11 *,
.pp-11 *::before,
.pp-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-11-bg);
  --pp-11-bg: oklch(0.95 0.012 250);
  --pp-11-card: oklch(1 0 0);
  --pp-11-ink: oklch(0.24 0.02 265);
  --pp-11-mut: oklch(0.55 0.02 265);
  --pp-11-line: oklch(0.9 0.01 260);
  --pp-11-acc: oklch(0.55 0.2 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-11-ink);
}

.pp-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(80% 60% at 50% 0%,oklch(0.9 0.05 300/.55),transparent 70%);
}

.pp-11__player {
  display: grid;
  justify-items: center;
  width: min(100%,420px);
  padding: 30px 28px 26px;
  border-radius: 26px;
  background: var(--pp-11-card);
  box-shadow: 0 1px 0 var(--pp-11-line),0 24px 60px oklch(0.4 0.05 290/.18);
}

.pp-11__art {
  width: 104px;
  height: 104px;
  border-radius: 20px;
  object-fit: cover;
  background: linear-gradient(140deg,var(--pp-11-acc),oklch(0.7 0.14 340));
  box-shadow: 0 14px 30px oklch(0.4 0.1 300/.35);
}

.pp-11__title {
  font-size: 20px;
  font-weight: 670;
  letter-spacing: -.02em;
  margin-top: 18px;
  text-align: center;
}

.pp-11__sub {
  font-size: 13px;
  color: var(--pp-11-mut);
  margin-top: 5px;
}

.pp-11__scrub {
  width: 100%;
  height: 5px;
  margin: 20px 0 4px;
  border-radius: 99px;
  background: var(--pp-11-line);
  overflow: hidden;
}

.pp-11__scrub b {
  display: block;
  height: 100%;
  width: 0;
  border-radius: 99px;
  background: var(--pp-11-acc);
  animation: pp-11-fill 20s linear infinite;
  animation-play-state: paused;
}

.pp-11__player[data-state="playing"] .pp-11__scrub b {
  animation-play-state: running;
}

@keyframes pp-11-fill {
  from {
    width: 0;
  }

  to {
    width: 100%;
  }
}

.pp-11__transport {
  display: grid;
  grid-template-columns: repeat(5,auto);
  align-items: center;
  justify-content: center;
  gap: clamp(8px,3.5vw,18px);
  margin-top: 20px;
}

.pp-11__btn {
  position: relative;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 50%;
  background: transparent;
  color: var(--pp-11-ink);
  cursor: pointer;
  transition: background .2s,transform .18s,color .2s;
}

.pp-11__btn:hover {
  background: color-mix(in oklch,var(--pp-11-acc) 10%,transparent);
}

.pp-11__btn:active {
  transform: scale(.92);
}

.pp-11__btn:focus-visible {
  outline: 3px solid var(--pp-11-acc);
  outline-offset: 2px;
}

.pp-11__btn--sm {
  width: 44px;
  height: 44px;
  color: var(--pp-11-mut);
}

.pp-11__btn--md {
  width: 52px;
  height: 52px;
}

.pp-11__btn--lg {
  width: 72px;
  height: 72px;
  background: var(--pp-11-acc);
  color: oklch(0.99 0 0);
  box-shadow: 0 10px 24px color-mix(in oklch,var(--pp-11-acc) 45%,transparent);
}

.pp-11__btn--lg:hover {
  background: color-mix(in oklch,var(--pp-11-acc) 88%,black);
}

.pp-11__num {
  position: absolute;
  font-size: 9.5px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  letter-spacing: .02em;
  margin-top: 2px;
}

.pp-11__sr,
.pp-11__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pp-11__q {
  display: none;
}

.pp-11__player[data-state="playing"] .pp-11__p {
  display: none;
}

.pp-11__player[data-state="playing"] .pp-11__q {
  display: block;
}

.pp-11__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-11-mut);
  padding: 7px 14px;
  border: 1px solid var(--pp-11-line);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-11 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const tracks = [
    { t: 'Signal to Noise', s: 'Episode 12 \u00b7 48 min', a: 'https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?q=80&w=500&auto=format&fit=crop' },
    { t: 'Latency Budget', s: 'Episode 13 \u00b7 41 min', a: 'https://images.unsplash.com/photo-1487215078519-e21cc028cb29?q=80&w=500&auto=format&fit=crop' },
    { t: 'Ship It Friday', s: 'Episode 14 \u00b7 55 min', a: 'https://images.unsplash.com/photo-1478737270239-2f02b77fc618?q=80&w=500&auto=format&fit=crop' }
  ];
  document.querySelectorAll('.pp-11__player').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const el = (s) => root.querySelector(s);
    let i = 0, playing = false;
    const render = (msg) => {
      el('.pp-11__title').textContent = tracks[i].t;
      el('.pp-11__sub').textContent = tracks[i].s;
      el('.pp-11__art').src = tracks[i].a;
      root.dataset.state = playing ? 'playing' : 'paused';
      el('.pp-11__btn--lg').setAttribute('aria-pressed', String(playing));
      el('.pp-11__sr').textContent = playing ? 'Pause' : 'Play';
      el('.pp-11__live').textContent = msg || (playing ? 'Playing ' : 'Paused ') + tracks[i].t;
    };
    root.addEventListener('click', (e) => {
      const act = e.target.closest('[data-act]')?.dataset.act;
      if (!act) return;
      if (act === 'play') playing = !playing;
      if (act === 'next' || act === 'prev') i = (i + (act === 'next' ? 1 : -1) + tracks.length) % tracks.length;
      render(act === 'back' ? 'Rewound 15 seconds' : act === 'fwd' ? 'Forward 30 seconds' : '');
    });
    render();
  });
})();
```
