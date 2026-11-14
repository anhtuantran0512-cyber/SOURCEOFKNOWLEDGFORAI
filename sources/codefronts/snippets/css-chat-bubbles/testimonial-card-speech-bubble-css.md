---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/testimonial-card-speech-bubble-css/"
title: "Testimonial Card Speech Bubble CSS"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "Testimonials as speech bubbles that point down at the person who said them — semantic <blockquote> + <cite>, an accessible star rating that reads as text,…"
has_js: "true"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Testimonial Card Speech Bubble CSS
Source: https://codefronts.com/snippets/css-chat-bubbles/testimonial-card-speech-bubble-css/

Testimonials as speech bubbles that point down at the person who said them — semantic <blockquote> + <cite>, an accessible star rating that reads as text, and a scroll-snap carousel you can drive with the arrows, the dots, a swipe or the keyboard. Active state comes from an IntersectionObserver, so the dots stay honest even when you scroll the track by hand.
## HTML
```html
<div class="cb-15">
  <button class="cb-15__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cb-15__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="cb-15__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>

  <section class="cb-15__wrap" aria-label="Customer testimonials" aria-roledescription="carousel">
    <ul class="cb-15__track" id="cb-15-track" tabindex="0">
      <li class="cb-15__slide">
        <figure class="cb-15__card">
          <span class="cb-15__stars" role="img" aria-label="Rated 5 out of 5">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
          </span>
          <blockquote class="cb-15__bubble"><p>We replaced four dashboards with one and nobody has asked for the old ones back. That has never happened here.</p></blockquote>
          <figcaption class="cb-15__by">
            <img src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=facearea&facepad=2.8&w=160&h=160&q=70" width="52" height="52" alt="Nadia Rahman" loading="lazy" decoding="async">
            <span><cite>Nadia Rahman</cite><small>Head of Operations · Kestrel Freight</small></span>
          </figcaption>
        </figure>
      </li>

      <li class="cb-15__slide">
        <figure class="cb-15__card">
          <span class="cb-15__stars" role="img" aria-label="Rated 5 out of 5">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
          </span>
          <blockquote class="cb-15__bubble"><p>Onboarding took an afternoon. The part I still think about is how little we had to explain to the team afterwards.</p></blockquote>
          <figcaption class="cb-15__by">
            <img src="https://images.unsplash.com/photo-1552058544-f2b08422138a?auto=format&fit=facearea&facepad=2.8&w=160&h=160&q=70" width="52" height="52" alt="Marcus Oyelaran" loading="lazy" decoding="async">
            <span><cite>Marcus Oyelaran</cite><small>Engineering Manager · Northbound</small></span>
          </figcaption>
        </figure>
      </li>

      <li class="cb-15__slide">
        <figure class="cb-15__card">
          <span class="cb-15__stars" role="img" aria-label="Rated 4 out of 5">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
            <svg class="cb-15__star--off" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 10l6-.8z" fill="currentColor"/></svg>
          </span>
          <blockquote class="cb-15__bubble"><p>Support answered in four minutes on a Sunday. I have paid ten times as much for a great deal less than that.</p></blockquote>
          <figcaption class="cb-15__by">
            <img src="https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?auto=format&fit=facearea&facepad=2.8&w=160&h=160&q=70" width="52" height="52" alt="Hannah Weiss" loading="lazy" decoding="async">
            <span><cite>Hannah Weiss</cite><small>Founder · Studio Verta</small></span>
          </figcaption>
        </figure>
      </li>
    </ul>

    <div class="cb-15__nav">
      <button class="cb-15__arrow" id="cb-15-prev" type="button" aria-label="Previous testimonial">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M14.5 5.5 8 12l6.5 6.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <div class="cb-15__dots" id="cb-15-dots" role="tablist" aria-label="Choose testimonial">
        <button class="cb-15__dot" type="button" role="tab" aria-current="true" aria-label="Testimonial 1 of 3"></button>
        <button class="cb-15__dot" type="button" role="tab" aria-label="Testimonial 2 of 3"></button>
        <button class="cb-15__dot" type="button" role="tab" aria-label="Testimonial 3 of 3"></button>
      </div>
      <button class="cb-15__arrow" id="cb-15-next" type="button" aria-label="Next testimonial">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9.5 5.5 16 12l-6.5 6.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
    </div>
    <p class="cb-15__sr" id="cb-15-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Instrument+Sans:wght@400;500;600;700&display=swap');

.cb-15 {
  --bg: #f5f3ee;
  --card: #ffffff;
  --ink: #131310;
  --muted: #6d6b63;
  --line: #e6e3da;
  --acc: #1f4f3f;
  --star: #e0a03a;
  --shadow: rgba(19,19,16,.14);
  --serif: "Newsreader",ui-serif,Georgia,"Times New Roman",serif;
  --sans: "Instrument Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(1rem,4vw,3rem);
  /* safe centring: when the card is taller than the viewport the overflow goes DOWN,
       never up past the top edge where it would be unreachable */
  align-items: safe center;
  align-content: safe center;
  background: radial-gradient(75% 50% at 50% 0%, color-mix(in oklab,var(--acc) 9%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-15,
.cb-15 *,
.cb-15 *::before,
.cb-15 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .cb-15 {
    --bg: oklch(96.5% .008 90);
    --card: oklch(100% 0 0);
    --ink: oklch(17% .012 90);
    --muted: oklch(52% .012 90);
    --line: oklch(91% .01 88);
    --acc: oklch(38% .07 165);
    --star: oklch(76% .13 78);
  }
}

.cb-15__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cb-15 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cb-15__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,3vw,1.6rem);
  inset-inline-end: clamp(.9rem,3vw,1.6rem);
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  z-index: 3;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--ink);
  transition: transform .25s cubic-bezier(.16,1,.3,1);
}

.cb-15__theme:hover {
  transform: translateY(-2px);
}

.cb-15__theme svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-15__sun {
  display: none;
}

.cb-15__wrap {
  inline-size: min(100%,64rem);
  display: grid;
  gap: clamp(.75rem,2vw,1.5rem);
}

.cb-15__track {
  list-style: none;
  margin: 0;
  padding: .35rem clamp(.5rem,3vw,2rem) 1rem;
  display: flex;
  gap: clamp(1rem,3vw,1.75rem);
  overflow-x: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
  scroll-padding-inline: clamp(.5rem,3vw,2rem);
  scroll-behavior: smooth;
  scrollbar-width: none;
}

.cb-15__track::-webkit-scrollbar {
  display: none;
}

.cb-15__slide {
  flex: 0 0 min(26rem,84%);
  scroll-snap-align: center;
}

.cb-15__card {
  margin: 0;
  display: grid;
  gap: .8rem;
  justify-items: start;
}

.cb-15__stars {
  display: flex;
  gap: .1rem;
  color: var(--star);
}

.cb-15__stars svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cb-15__star--off {
  color: color-mix(in oklab,var(--ink) 18%,transparent);
}

.cb-15__bubble {
  position: relative;
  margin: 0;
  inline-size: 100%;
  padding: 1.35rem 1.5rem 1.45rem;
  border-radius: 1.5rem;
  background: var(--card);
  border: 1px solid var(--line);
  box-shadow: 0 30px 60px -45px var(--shadow);
  transition: transform .35s cubic-bezier(.16,1,.3,1), box-shadow .35s;
}

.cb-15__slide:hover .cb-15__bubble {
  transform: translateY(-4px);
  box-shadow: 0 40px 70px -45px var(--shadow);
}

.cb-15__bubble p {
  margin: 0;
  font-family: var(--serif);
  font-optical-sizing: auto;
  font-size: clamp(1.1rem,.9vw + .95rem,1.4rem);
  line-height: 1.38;
  letter-spacing: -.015em;
  text-wrap: pretty;
}

.cb-15__bubble::before {
  content: '';
  position: absolute;
  inset-block-start: 100%;
  inset-inline-start: 2.5rem;
  border-inline: 12px solid transparent;
  border-block-start: 18px solid var(--line);
}

.cb-15__bubble::after {
  content: '';
  position: absolute;
  inset-block-start: 100%;
  inset-inline-start: 2.6rem;
  border-inline: 11px solid transparent;
  border-block-start: 16px solid var(--card);
}

.cb-15__by {
  display: flex;
  align-items: center;
  gap: .75rem;
  padding-inline-start: .4rem;
  margin-block-start: .2rem;
}

.cb-15__by img {
  inline-size: 52px;
  block-size: 52px;
  border-radius: 50%;
  object-fit: cover;
  background: var(--line);
}

.cb-15__by span {
  display: grid;
  gap: .1rem;
}

.cb-15__by cite {
  font-style: normal;
  font-size: .98rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.cb-15__by small {
  font-size: .78rem;
  color: var(--muted);
}

.cb-15__nav {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.cb-15__arrow {
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 1px solid var(--line);
  border-radius: 50%;
  background: var(--card);
  color: var(--ink);
  transition: transform .25s cubic-bezier(.16,1,.3,1), background .2s;
}

.cb-15__arrow svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-15__arrow:hover {
  transform: translateY(-2px);
  background: color-mix(in oklab,var(--acc) 8%,var(--card));
}

.cb-15__dots {
  display: flex;
  align-items: center;
  gap: .15rem;
}

.cb-15__dot {
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 0;
  background: transparent;
  padding: 0;
}

.cb-15__dot::before {
  content: '';
  inline-size: .5rem;
  block-size: .5rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 22%,transparent);
  transition: inline-size .3s cubic-bezier(.16,1,.3,1), background .25s;
}

.cb-15__dot[aria-current="true"]::before {
  inline-size: 1.6rem;
  background: var(--acc);
}
/* dark */

.cb-15[data-theme="dark"] {
  --bg: #0c0c0a;
  --card: #161614;
  --ink: #f3f1eb;
  --muted: #9c988e;
  --line: #242320;
  --acc: #6fd7b0;
  --star: #f0b455;
  --shadow: rgba(0,0,0,.72);
}

.cb-15[data-theme="dark"] .cb-15__moon {
  display: none;
}

.cb-15[data-theme="dark"] .cb-15__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .cb-15:not([data-theme="light"]) {
    --bg: #0c0c0a;
    --card: #161614;
    --ink: #f3f1eb;
    --muted: #9c988e;
    --line: #242320;
    --acc: #6fd7b0;
    --star: #f0b455;
    --shadow: rgba(0,0,0,.72);
  }

  .cb-15:not([data-theme="light"]) .cb-15__moon {
    display: none;
  }

  .cb-15:not([data-theme="light"]) .cb-15__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-15 *,
    .cb-15 *::before,
    .cb-15 *::after {
    animation: none !important;
    transition: none !important;
  }

  .cb-15__track {
    scroll-behavior: auto;
  }
}

@media (forced-colors: active) {
  .cb-15__bubble {
    border: 1px solid CanvasText;
  }

  .cb-15__dot[aria-current="true"]::before {
    background: Highlight;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.cb-15');
  if (!root) return;
  const track = root.querySelector('#cb-15-track');
  const slides = [...root.querySelectorAll('.cb-15__slide')];
  const dots = [...root.querySelectorAll('.cb-15__dot')];
  const status = root.querySelector('#cb-15-status');
  const prev = root.querySelector('#cb-15-prev');
  const next = root.querySelector('#cb-15-next');

  const goTo = (i) => {
    const s = slides[Math.max(0, Math.min(slides.length - 1, i))];
    if (!s) return;
    track.scrollTo({ left: s.offsetLeft - track.offsetLeft - (track.clientWidth - s.clientWidth) / 2, behavior: 'smooth' });
  };
  const current = () => dots.findIndex((d) => d.getAttribute('aria-current') === 'true');

  prev.addEventListener('click', () => goTo(current() - 1));
  next.addEventListener('click', () => goTo(current() + 1));
  dots.forEach((d, i) => d.addEventListener('click', () => goTo(i)));

  /* the scroller is the source of truth — dots follow it, not the other way round */
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting || e.intersectionRatio < 0.6) return;
      const i = slides.indexOf(e.target);
      dots.forEach((d, n) => {
        d.setAttribute('aria-selected', String(n === i));
        if (n === i) d.setAttribute('aria-current', 'true'); else d.removeAttribute('aria-current');
      });
      prev.disabled = i === 0;
      next.disabled = i === slides.length - 1;
      const who = e.target.querySelector('cite').textContent;
      status.textContent = 'Testimonial ' + (i + 1) + ' of ' + slides.length + ', ' + who;
    });
  }, { root: track, threshold: [0.6] });
  slides.forEach((s) => io.observe(s));

  track.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') { e.preventDefault(); goTo(current() + 1); }
    if (e.key === 'ArrowLeft') { e.preventDefault(); goTo(current() - 1); }
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.cb-15');
  const btn = root && root.querySelector('.cb-15__theme');
  if (!btn) return;
  const isDark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    btn.setAttribute('aria-pressed', String(isDark()));
    btn.setAttribute('aria-label', isDark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  sync();
})();
```
