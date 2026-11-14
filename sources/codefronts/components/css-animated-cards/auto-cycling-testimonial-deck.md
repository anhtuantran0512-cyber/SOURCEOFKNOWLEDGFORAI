---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/auto-cycling-testimonial-deck/"
title: "Auto-Cycling Testimonial Deck"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "Testimonials in a physical stack: the front card slides away and drops to the back while the rest step forward, on a 6-second loop that pauses on hover, on…"
has_js: "true"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Auto-Cycling Testimonial Deck
Source: https://codefronts.com/components/css-animated-cards/auto-cycling-testimonial-deck/

Testimonials in a physical stack: the front card slides away and drops to the back while the rest step forward, on a 6-second loop that pauses on hover, on focus, and whenever the tab is hidden. Depth comes from one transform per position (translateY + scale + a whisper of rotation) driven by a single --i variable, so any number of cards works with no extra CSS.
## HTML
```html
<section class="ac-19" aria-label="Auto cycling testimonial deck demo">
  <div class="ac-19__stage">
    <div class="ac-19__deck" data-deck aria-roledescription="carousel" aria-label="Customer testimonials">
      <article class="ac-19__card" data-card>
        <p class="ac-19__quote">We deleted three animation dependencies the week we moved to native CSS timelines. Bundle down 41 kB, and the scroll finally feels like the OS.</p>
        <footer class="ac-19__by"><img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="44" height="44"><span><b>Marta Vieira</b><i>Principal Engineer · Kestrel</i></span></footer>
      </article>
      <article class="ac-19__card" data-card>
        <p class="ac-19__quote">Our checkout conversion moved 3.2% after the card-to-detail morph shipped. Nobody could tell us why — it just felt faster than it was.</p>
        <footer class="ac-19__by"><img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="44" height="44"><span><b>Idris Bello</b><i>Head of Product · Northbay</i></span></footer>
      </article>
      <article class="ac-19__card" data-card>
        <p class="ac-19__quote">The accessibility review passed first time. Reduced motion, focus states and live regions were in the components from day one instead of bolted on in Q4.</p>
        <footer class="ac-19__by"><img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="44" height="44"><span><b>Sunny Ellis</b><i>Design Systems Lead · Fathom</i></span></footer>
      </article>
      <article class="ac-19__card" data-card>
        <p class="ac-19__quote">I teach front-end to career changers. This is the first card library where the students can read the CSS and explain it back to me.</p>
        <footer class="ac-19__by"><img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=120&h=120&fit=crop&auto=format" alt="" width="44" height="44"><span><b>Priya Raman</b><i>Instructor · Kanto Academy</i></span></footer>
      </article>
    </div>
    <div class="ac-19__ctl">
      <button class="ac-19__nav" type="button" data-prev aria-label="Previous testimonial">
        <svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>
      </button>
      <button class="ac-19__play" type="button" data-play aria-pressed="true">
        <span class="ac-19__pi" aria-hidden="true"></span>
        <span data-playlabel>Pause</span>
      </button>
      <button class="ac-19__nav" type="button" data-next aria-label="Next testimonial">
        <svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>
      </button>
      <span class="ac-19__dots" data-dots aria-hidden="true"></span>
    </div>
    <p class="ac-19__sr" role="status" aria-live="polite" data-status></p>
    <p class="ac-19__chip" aria-hidden="true">--i driven depth transform · deal-to-back loop · pause on hover / focus / tab-hidden · WCAG 2.2.2 control</p>
  </div>
</section>
```
## CSS
```css
.ac-19,
.ac-19 *,
.ac-19 *::before,
.ac-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-19-bg: oklch(0.96 0.012 75);
  --ac-19-card: oklch(1 0 0);
  --ac-19-ink: oklch(0.24 0.02 60);
  --ac-19-mut: oklch(0.55 0.02 60);
  --ac-19-acc: oklch(0.52 0.14 42);
  --ac-19-line: oklch(0.24 0.02 60/.12);
  background: var(--ac-19-bg);
  color: var(--ac-19-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-19__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(22px,5vw,58px);
}

.ac-19__deck {
  position: relative;
  width: min(100%,480px);
  height: 265px;
}

.ac-19__card {
  position: absolute;
  inset: 0;
  display: grid;
  align-content: space-between;
  gap: 16px;
  padding: 26px;
  border: 1px solid var(--ac-19-line);
  border-radius: 22px;
  background: var(--ac-19-card);
  box-shadow: 0 22px 44px -30px oklch(0.24 0.02 60/.8);
  transform-origin: 50% 100%;
  translate: 0 calc(var(--ac-19-i,0) * 14px);
  scale: calc(1 - var(--ac-19-i,0) * .05);
  rotate: calc(var(--ac-19-i,0) * .7deg);
  filter: brightness(calc(1 - var(--ac-19-i,0) * .04));
  z-index: calc(10 - var(--ac-19-i,0));
  opacity: 1;
  transition: translate .62s cubic-bezier(.16,1,.3,1),scale .62s cubic-bezier(.16,1,.3,1),rotate .62s cubic-bezier(.16,1,.3,1),opacity .45s ease,filter .5s;
}

.ac-19__card[data-i="3"] {
  opacity: .9;
}

.ac-19__card[data-out] {
  translate: -118% -6%;
  rotate: -9deg;
  opacity: 0;
  transition-duration: .5s;
}

.ac-19__quote {
  font-size: clamp(16px,2.2vw,19px);
  line-height: 1.5;
  font-weight: 520;
  letter-spacing: -.018em;
  text-wrap: pretty;
}

.ac-19__quote::before {
  content: '\201C';
  display: block;
  font-size: 44px;
  line-height: .6;
  color: color-mix(in oklch,var(--ac-19-acc) 40%,transparent);
  margin-bottom: 8px;
}

.ac-19__by {
  display: flex;
  align-items: center;
  gap: 12px;
}

.ac-19__by img {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  background: oklch(0.88 0.02 60);
}

.ac-19__by span {
  display: grid;
  gap: 2px;
}

.ac-19__by b {
  font-size: 14px;
  font-weight: 650;
  letter-spacing: -.015em;
}

.ac-19__by i {
  font-style: normal;
  font-size: 12px;
  color: var(--ac-19-mut);
}

.ac-19__ctl {
  display: flex;
  align-items: center;
  gap: 9px;
}

.ac-19__nav,
.ac-19__play {
  min-height: 44px;
  border: 1px solid var(--ac-19-line);
  border-radius: 99px;
  background: var(--ac-19-card);
  color: var(--ac-19-ink);
  font-family: inherit;
  cursor: pointer;
  transition: background .2s,transform .2s;
}

.ac-19__nav {
  width: 44px;
  display: grid;
  place-items: center;
}

.ac-19__play {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  padding: 0 18px;
  font-size: 13.5px;
  font-weight: 640;
}

.ac-19__nav:hover,
.ac-19__play:hover {
  background: oklch(0.24 0.02 60/.05);
  transform: translateY(-1px);
}

.ac-19__nav:focus-visible,
.ac-19__play:focus-visible {
  outline: 2px solid var(--ac-19-acc);
  outline-offset: 3px;
}

.ac-19__pi {
  width: 11px;
  height: 12px;
  background: currentColor;
  -webkit-mask: linear-gradient(#000 0 0) 0 0/3.5px 12px no-repeat,linear-gradient(#000 0 0) 100% 0/3.5px 12px no-repeat;
  mask: linear-gradient(#000 0 0) 0 0/3.5px 12px no-repeat,linear-gradient(#000 0 0) 100% 0/3.5px 12px no-repeat;
}

.ac-19__play[aria-pressed="false"] .ac-19__pi {
  -webkit-mask: none;
  mask: none;
  clip-path: polygon(0 0,100% 50%,0 100%);
  width: 10px;
}

.ac-19__dots {
  display: inline-flex;
  gap: 6px;
  margin-left: 6px;
}

.ac-19__dots i {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: oklch(0.24 0.02 60/.2);
  transition: background .3s,width .3s;
}

.ac-19__dots i[data-on] {
  width: 20px;
  border-radius: 99px;
  background: var(--ac-19-acc);
}

.ac-19__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ac-19__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-19-mut);
  padding: 8px 15px;
  border: 1px dashed var(--ac-19-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,760px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-19__card {
    transition-duration: .01ms;
  }
}
```

## JavaScript
```js
(() => {
  const DELAY = 6000;
  document.querySelectorAll('.ac-19').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const deck = root.querySelector('[data-deck]');
    const cards = [...deck.querySelectorAll('[data-card]')];
    const dots = root.querySelector('[data-dots]');
    const status = root.querySelector('[data-status]');
    const play = root.querySelector('[data-play]');
    const playLabel = root.querySelector('[data-playlabel]');
    let order = cards.map((_, i) => i);   // order[position] = card index
    let timer = 0, running = true;

    dots.innerHTML = cards.map(() => '<i></i>').join('');
    const pips = [...dots.querySelectorAll('i')];

    const paint = (announce) => {
      order.forEach((cardIdx, pos) => {
        const c = cards[cardIdx];
        c.style.setProperty('--ac-19-i', pos);
        c.dataset.i = pos;
        if (pos === 0) { c.removeAttribute('inert'); c.removeAttribute('aria-hidden'); }
        else { c.setAttribute('inert', ''); c.setAttribute('aria-hidden', 'true'); }
      });
      pips.forEach((p, i) => (i === order[0] ? p.setAttribute('data-on', '') : p.removeAttribute('data-on')));
      if (announce) {
        const who = cards[order[0]].querySelector('b').textContent;
        status.textContent = 'Testimonial ' + (order[0] + 1) + ' of ' + cards.length + ', ' + who + '.';
      }
    };

    const next = (announce) => {
      const front = cards[order[0]];
      front.dataset.out = '';                       // deal the front card away
      setTimeout(() => { front.removeAttribute('data-out'); }, 480);
      order = order.slice(1).concat(order[0]);      // and wrap it to the back
      paint(announce);
    };
    const prev = () => { order = [order[order.length - 1]].concat(order.slice(0, -1)); paint(true); };

    const start = () => { clearInterval(timer); if (running) timer = setInterval(() => next(false), DELAY); };
    const stop = () => clearInterval(timer);

    play.addEventListener('click', () => {
      running = !running;
      play.setAttribute('aria-pressed', String(running));
      playLabel.textContent = running ? 'Pause' : 'Play';
      running ? start() : stop();
    });
    root.querySelector('[data-next]').addEventListener('click', () => { next(true); start(); });
    root.querySelector('[data-prev]').addEventListener('click', () => { prev(); start(); });

    deck.addEventListener('pointerenter', stop);            // WCAG: motion must be stoppable
    deck.addEventListener('pointerleave', start);
    deck.addEventListener('focusin', stop);
    deck.addEventListener('focusout', start);
    document.addEventListener('visibilitychange', () => (document.hidden ? stop() : start()));

    paint(false); start();
  });
})();
```
