---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/glassmorphism-audio-player-toggle/"
title: "Glassmorphism Audio Player Toggle"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "A frosted-glass music widget floating over its own album art: the card blurs and brightens whatever is behind it with backdrop-filter, a hairline gradient…"
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Audio Player Toggle
Source: https://codefronts.com/components/css-play-pause-buttons/glassmorphism-audio-player-toggle/

A frosted-glass music widget floating over its own album art: the card blurs and brightens whatever is behind it with backdrop-filter, a hairline gradient border catches the light, and the play button is a second, brighter pane of glass inside the first. The equalizer and the progress line are CSS animations that simply switch animation-play-state with the toggle — so 'playing' costs zero JavaScript.
## HTML
```html
<section class="pp-03" aria-label="Glassmorphism audio player toggle demo">
  <div class="pp-03__stage">
    <div class="pp-03__card">
      <img class="pp-03__art" src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=400&auto=format&fit=crop" alt="" width="82" height="82" loading="lazy">
      <div class="pp-03__meta">
        <p class="pp-03__title">Glass Cathedral</p>
        <p class="pp-03__sub">Nocturne Division</p>
        <span class="pp-03__line" aria-hidden="true"><b></b></span>
      </div>
      <span class="pp-03__eq" aria-hidden="true"><b></b><b></b><b></b><b></b></span>
      <input class="pp-03__chk" type="checkbox" id="pp-03-toggle" aria-label="Play or pause Glass Cathedral">
      <label class="pp-03__btn" for="pp-03-toggle">
        <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true">
          <path class="pp-03__p" d="M8.5 5.4v13.2L19 12z" fill="currentColor"/>
          <path class="pp-03__q" d="M8 5h3v14H8zM13 5h3v14h-3z" fill="currentColor"/>
        </svg>
      </label>
    </div>
    <p class="pp-03__chip" aria-hidden="true">backdrop-filter: blur() saturate() · :has() state lift · animation-play-state</p>
  </div>
</section>
```
## CSS
```css
.pp-03,
.pp-03 *,
.pp-03 *::before,
.pp-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-03-bg);
  --pp-03-bg: oklch(0.22 0.06 300);
  --pp-03-ink: oklch(0.99 0.004 300);
  --pp-03-mut: oklch(0.86 0.02 300/.8);
  --pp-03-acc: oklch(0.85 0.13 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-03-ink);
}

.pp-03__stage {
  position: relative;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(18px,5vw,56px);
  background: linear-gradient(150deg,oklch(0.38 0.14 320),oklch(0.24 0.09 265) 45%,oklch(0.32 0.11 200)),url('https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=1200&auto=format&fit=crop') center/cover;
  background-blend-mode: overlay,normal;
  overflow: hidden;
}

.pp-03__stage::before {
  content: '';
  position: absolute;
  inset: -10%;
  background: inherit;
  filter: blur(46px) saturate(140%);
  z-index: 0;
}

.pp-03__card {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 18px;
  width: min(100%,470px);
  padding: 16px 20px 16px 16px;
  border-radius: 24px;
  border: 1px solid oklch(1 0 0/.22);
  background: oklch(1 0 0/.12);
  -webkit-backdrop-filter: blur(26px) saturate(160%);
  backdrop-filter: blur(26px) saturate(160%);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.35),0 30px 60px oklch(0 0 0/.45);
}

.pp-03__art {
  width: 64px;
  height: 64px;
  border-radius: 16px;
  object-fit: cover;
  flex: none;
  background: linear-gradient(135deg,oklch(0.6 0.15 320),oklch(0.4 0.1 260));
  box-shadow: 0 8px 20px oklch(0 0 0/.4);
}

.pp-03__meta {
  flex: 1;
  min-width: 0;
}

.pp-03__title {
  font-size: 15.5px;
  font-weight: 650;
  letter-spacing: -.01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.pp-03__sub {
  font-size: 12.5px;
  color: var(--pp-03-mut);
  margin-top: 2px;
}

.pp-03__line {
  display: block;
  height: 3px;
  margin-top: 11px;
  border-radius: 99px;
  background: oklch(1 0 0/.25);
  overflow: hidden;
}

.pp-03__line b {
  display: block;
  height: 100%;
  width: 0;
  background: var(--pp-03-acc);
  animation: pp-03-fill 18s linear infinite;
  animation-play-state: paused;
}

.pp-03__eq {
  display: flex;
  align-items: flex-end;
  gap: 3px;
  height: 22px;
}

.pp-03__eq b {
  width: 3px;
  height: 30%;
  border-radius: 99px;
  background: var(--pp-03-acc);
  transform-origin: bottom;
  animation: pp-03-bounce .9s ease-in-out infinite alternate;
  animation-play-state: paused;
}

.pp-03__eq b:nth-child(2) {
  animation-delay: -.25s;
}

.pp-03__eq b:nth-child(3) {
  animation-delay: -.55s;
}

.pp-03__eq b:nth-child(4) {
  animation-delay: -.8s;
}

.pp-03__chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-03__btn {
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  flex: none;
  border-radius: 50%;
  border: 1px solid oklch(1 0 0/.4);
  background: oklch(1 0 0/.2);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  color: var(--pp-03-ink);
  cursor: pointer;
  transition: transform .25s cubic-bezier(.34,1.4,.5,1),background .25s;
}

.pp-03__btn:hover {
  background: oklch(1 0 0/.32);
  transform: scale(1.07);
}

.pp-03__chk:focus-visible+.pp-03__btn {
  outline: 3px solid var(--pp-03-acc);
  outline-offset: 3px;
}

.pp-03__q {
  display: none;
}

.pp-03__card:has(.pp-03__chk:checked) .pp-03__p {
  display: none;
}

.pp-03__card:has(.pp-03__chk:checked) .pp-03__q {
  display: block;
}

.pp-03__card:has(.pp-03__chk:checked) .pp-03__eq b,
.pp-03__card:has(.pp-03__chk:checked) .pp-03__line b {
  animation-play-state: running;
}

@keyframes pp-03-bounce {
  from {
    height: 20%;
  }

  to {
    height: 100%;
  }
}

@keyframes pp-03-fill {
  from {
    width: 0;
  }

  to {
    width: 100%;
  }
}

.pp-03__chip {
  position: relative;
  z-index: 1;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: oklch(1 0 0/.75);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.2);
  border-radius: 99px;
  background: oklch(0 0 0/.18);
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-03 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```
