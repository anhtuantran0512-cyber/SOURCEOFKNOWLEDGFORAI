---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/mobile-first-swipeable-card-deck/"
title: "Mobile-First Swipeable Card Deck"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "A phone-native card deck where the cards physically stack, rotate and settle as you drag — and every frame of it is driven by scroll position, not JavaScript."
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile-First Swipeable Card Deck
Source: https://codefronts.com/components/css-testimonials-reviews/mobile-first-swipeable-card-deck/

A phone-native card deck where the cards physically stack, rotate and settle as you drag — and every frame of it is driven by scroll position, not JavaScript. animation-timeline: view(inline) maps each card's own visibility to its transform, so the deck behaves identically on a trackpad, a touchscreen and a keyboard.
## HTML
```html
<section class="tr-08" aria-label="Mobile-first swipeable testimonial card deck demo">
  <div class="tr-08__stage">
    <div class="tr-08__phone">
      <div class="tr-08__bezel" aria-hidden="true"><span class="tr-08__island"></span></div>
      <div class="tr-08__screen">
        <header class="tr-08__top">
          <p class="tr-08__eyebrow">What members say</p>
          <h2 class="tr-08__title">Swipe the deck</h2>
        </header>

        <div class="tr-08__deck" tabindex="0" role="group" aria-label="Testimonials, swipe or use arrow keys">
          <figure class="tr-08__card" style="--tr-08-h:265">
            <div class="tr-08__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</div>
            <blockquote>Six weeks in and I have run further than the whole of last year. The plan just… fits around the school run.</blockquote>
            <figcaption>
              <img src="https://images.unsplash.com/photo-1541101767792-f9b2b1c4f127?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Robyn Fletcher" width="42" height="42" loading="lazy" decoding="async">
              <span><b>Robyn Fletcher</b>Leeds · Member since 2025</span>
            </figcaption>
          </figure>
          <figure class="tr-08__card" style="--tr-08-h:25">
            <div class="tr-08__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</div>
            <blockquote>The coach replies in hours, not days. I have paid four times this for less.</blockquote>
            <figcaption>
              <img src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Ethan Park" width="42" height="42" loading="lazy" decoding="async">
              <span><b>Ethan Park</b>Vancouver · Member since 2024</span>
            </figcaption>
          </figure>
          <figure class="tr-08__card" style="--tr-08-h:150">
            <div class="tr-08__stars" role="img" aria-label="Rated 4 out of 5">★★★★<span>★</span></div>
            <blockquote>Wish the watch sync was faster, but the strength block is the best I have followed anywhere.</blockquote>
            <figcaption>
              <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Erin McAllister" width="42" height="42" loading="lazy" decoding="async">
              <span><b>Erin McAllister</b>Dublin · Member since 2026</span>
            </figcaption>
          </figure>
          <figure class="tr-08__card" style="--tr-08-h:320">
            <div class="tr-08__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</div>
            <blockquote>Cancelled two other subscriptions the week I joined. Everything I actually used is in here.</blockquote>
            <figcaption>
              <img src="https://images.unsplash.com/photo-1463453091185-61582044d556?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Samuel Idris" width="42" height="42" loading="lazy" decoding="async">
              <span><b>Samuel Idris</b>Auckland · Member since 2025</span>
            </figcaption>
          </figure>
        </div>

        <p class="tr-08__hint">Drag, flick, or press <kbd>←</kbd> <kbd>→</kbd></p>
      </div>
    </div>
    <p class="tr-08__chip" aria-hidden="true">animation-timeline:view(inline) · animation-range:entry/exit · scroll-snap-stop:always</p>
  </div>
</section>
```
## CSS
```css
.tr-08,
.tr-08 *,
.tr-08 *::before,
.tr-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-08-bg: oklch(0.94 0.02 90);
  --tr-08-screen: oklch(0.99 0.006 90);
  --tr-08-ink: oklch(0.23 0.02 60);
  --tr-08-mut: oklch(0.56 0.02 60);
  --tr-08-acc: oklch(0.62 0.2 20);
  --tr-08-star: oklch(0.72 0.17 55);
  background: var(--tr-08-bg);
  color: var(--tr-08-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(16px,4vw,44px);
  background: radial-gradient(70% 50% at 50% 10%,color-mix(in oklch,var(--tr-08-acc) 14%,transparent),transparent 60%);
}

.tr-08__phone {
  position: relative;
  width: min(100%,392px);
  border-radius: 46px;
  padding: 11px;
  background: linear-gradient(160deg,oklch(0.32 0.02 60),oklch(0.16 0.01 60));
  box-shadow: 0 3px 0 oklch(1 0 0/.14) inset,0 40px 80px -40px oklch(0 0 0/.75),0 0 0 1px oklch(0 0 0/.3);
}

.tr-08__bezel {
  position: absolute;
  inset-block-start: 11px;
  inset-inline: 11px;
  height: 34px;
  display: grid;
  place-items: center;
  z-index: 3;
  pointer-events: none;
}

.tr-08__island {
  width: 96px;
  height: 26px;
  border-radius: 99px;
  background: oklch(0.1 0 0);
}

.tr-08__screen {
  border-radius: 36px;
  background: var(--tr-08-screen);
  overflow: hidden;
  padding: 52px 0 22px;
  display: grid;
  gap: 16px;
}

.tr-08__top {
  padding-inline: 24px;
  display: grid;
  gap: 5px;
}

.tr-08__eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--tr-08-acc);
}

.tr-08__title {
  font-size: 26px;
  font-weight: 680;
  letter-spacing: -.035em;
}

.tr-08__deck {
  display: flex;
  gap: 16px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding: 26px 0;
  scrollbar-width: none;
  overscroll-behavior-x: contain;
  -webkit-overflow-scrolling: touch;
}

.tr-08__deck::-webkit-scrollbar {
  display: none;
}

.tr-08__deck::before,
.tr-08__deck::after {
  content: '';
  flex: 0 0 calc(50% - 118px);
  min-width: 0;
}

.tr-08__deck:focus-visible {
  outline: 3px solid var(--tr-08-acc);
  outline-offset: -4px;
  border-radius: 20px;
}

.tr-08__card {
  flex: 0 0 236px;
  scroll-snap-align: center;
  display: grid;
  align-content: start;
  gap: 13px;
  padding: 22px 20px;
  border-radius: 22px;
  background: linear-gradient(165deg,oklch(0.99 0.01 var(--tr-08-h,20)),oklch(0.95 0.035 var(--tr-08-h,20)));
  border: 1px solid oklch(0 0 0/.07);
  box-shadow: 0 18px 36px -22px oklch(0 0 0/.5);
  transform-origin: 50% 60%;
}

@supports (animation-timeline: view()) {
  .tr-08__card {
    animation: tr-08-deck linear both;
    animation-timeline: view(inline);
    animation-range: entry 5% exit 95%;
  }

  @keyframes tr-08-deck {
    0% {
      scale: .82;
      rotate: 8deg;
      opacity: .3;
    }

    50% {
      scale: 1;
      rotate: 0deg;
      opacity: 1;
    }

    100% {
      scale: .82;
      rotate: -8deg;
      opacity: .3;
    }
  }
}

.tr-08__stars {
  font-size: 14px;
  letter-spacing: 2px;
  color: var(--tr-08-star);
}

.tr-08__stars span {
  color: oklch(0 0 0/.15);
}

.tr-08__card blockquote {
  font-size: 15px;
  line-height: 1.5;
  letter-spacing: -.015em;
  text-wrap: pretty;
}

.tr-08__card figcaption {
  display: flex;
  align-items: center;
  gap: 10px;
  padding-top: 13px;
  border-top: 1px solid oklch(0 0 0/.08);
}

.tr-08__card figcaption img {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  background: oklch(0.88 0.03 30);
}

.tr-08__card figcaption span {
  display: grid;
  font-size: 11.5px;
  line-height: 1.35;
  color: var(--tr-08-mut);
}

.tr-08__card figcaption b {
  font-size: 13.5px;
  font-weight: 650;
  color: var(--tr-08-ink);
  letter-spacing: -.012em;
}

.tr-08__hint {
  text-align: center;
  font-size: 12px;
  color: var(--tr-08-mut);
}

.tr-08__hint kbd {
  display: inline-grid;
  place-items: center;
  min-width: 22px;
  height: 22px;
  padding: 0 5px;
  border-radius: 6px;
  border: 1px solid oklch(0 0 0/.14);
  border-block-end-width: 2px;
  background: oklch(1 0 0);
  font: inherit;
  font-size: 11px;
}

.tr-08__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-08-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.13);
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.5);
}

@media (prefers-reduced-motion: reduce) {
  .tr-08__card {
    animation: none;
  }
}
```
