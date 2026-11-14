---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/floating-fab/"
title: "Floating Action Button (FAB) Media Player"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "A floating action button that expands into a mini player: press play and the 64px circle stretches into a pill containing artwork, title and a progress line…"
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Action Button (FAB) Media Player
Source: https://codefronts.com/components/css-play-pause-buttons/floating-fab/

A floating action button that expands into a mini player: press play and the 64px circle stretches into a pill containing artwork, title and a progress line — one element, one transition, no layout thrash. This is the pattern mobile apps use for a persistent 'now playing' affordance, and it is achievable with a single width/border-radius transition plus staggered child reveals.
## HTML
```html
<section class="pp-19" aria-label="Floating action button media player demo">
  <div class="pp-19__stage">
    <div class="pp-19__sheet" aria-hidden="true">
      <span class="pp-19__ghost"></span><span class="pp-19__ghost pp-19__ghost--s"></span><span class="pp-19__ghost"></span><span class="pp-19__ghost pp-19__ghost--s"></span>
    </div>
    <div class="pp-19__dock">
      <input class="pp-19-chk" type="checkbox" id="pp-19-toggle" aria-label="Play or pause Weightless Cities">
      <label class="pp-19__fab" for="pp-19-toggle">
        <span class="pp-19__icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="24" height="24">
            <path class="pp-19__p" d="M9 5.6v12.8L18.8 12z" fill="currentColor"/>
            <path class="pp-19__q" d="M8.6 5.6h3.1v12.8H8.6zM12.9 5.6H16v12.8h-3.1z" fill="currentColor"/>
          </svg>
        </span>
        <span class="pp-19__detail">
          <img class="pp-19__art" src="https://images.unsplash.com/photo-1459749411175-04bf5292ceea?q=80&w=200&auto=format&fit=crop" alt="" width="44" height="44" loading="lazy">
          <span class="pp-19__text">
            <b>Weightless Cities</b>
            <em>Hollow Coast · playing now</em>
            <span class="pp-19__line"><i></i></span>
          </span>
        </span>
      </label>
    </div>
    <p class="pp-19__chip" aria-hidden="true">width + border-radius morph · asymmetric transition-delay · pure CSS state</p>
  </div>
</section>
```
## CSS
```css
.pp-19,
.pp-19 *,
.pp-19 *::before,
.pp-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-19-bg);
  --pp-19-bg: oklch(0.96 0.008 285);
  --pp-19-ink: oklch(0.24 0.02 285);
  --pp-19-mut: oklch(0.56 0.02 285);
  --pp-19-fab: oklch(0.55 0.19 285);
  --pp-19-on: oklch(0.99 0 0);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-19-ink);
}

.pp-19__stage {
  position: relative;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 30px;
  padding: clamp(20px,5vw,56px);
}

.pp-19__sheet {
  display: grid;
  gap: 14px;
  width: min(100%,360px);
  opacity: .5;
}

.pp-19__ghost {
  display: block;
  height: 14px;
  border-radius: 99px;
  background: oklch(0.86 0.012 285);
}

.pp-19__ghost--s {
  width: 62%;
}

.pp-19__dock {
  display: grid;
  justify-items: center;
  min-height: 76px;
  align-content: center;
}

.pp-19-chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-19__fab {
  display: flex;
  align-items: center;
  gap: 0;
  width: 68px;
  height: 68px;
  padding: 10px;
  border-radius: 50%;
  background: var(--pp-19-fab);
  color: var(--pp-19-on);
  cursor: pointer;
  overflow: hidden;
  white-space: nowrap;
  box-shadow: 0 10px 26px color-mix(in oklch,var(--pp-19-fab) 42%,transparent);
  transition: width .5s cubic-bezier(.5,0,.15,1),border-radius .5s cubic-bezier(.5,0,.15,1),gap .5s,box-shadow .3s;
}

.pp-19__fab:hover {
  box-shadow: 0 14px 34px color-mix(in oklch,var(--pp-19-fab) 52%,transparent);
}

.pp-19-chk:focus-visible+.pp-19__fab {
  outline: 3px solid var(--pp-19-ink);
  outline-offset: 4px;
}

.pp-19__icon {
  display: grid;
  place-items: center;
  width: 48px;
  height: 48px;
  flex: none;
}

.pp-19__q {
  display: none;
}

.pp-19__detail {
  display: flex;
  align-items: center;
  gap: 12px;
  opacity: 0;
  translate: -10px 0;
  transition: opacity .22s,translate .22s;
}

.pp-19__art {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  object-fit: cover;
  flex: none;
  background: oklch(0.7 0.12 300);
}

.pp-19__text {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.pp-19__text b {
  font-size: 14px;
  font-weight: 660;
  letter-spacing: -.01em;
}

.pp-19__text em {
  font-size: 11.5px;
  font-style: normal;
  opacity: .8;
}

.pp-19__line {
  display: block;
  width: 150px;
  height: 3px;
  margin-top: 5px;
  border-radius: 99px;
  background: oklch(1 0 0/.3);
  overflow: hidden;
}

.pp-19__line i {
  display: block;
  height: 100%;
  width: 0;
  background: var(--pp-19-on);
  animation: pp-19-fill 24s linear infinite;
  animation-play-state: paused;
}

.pp-19-chk:checked+.pp-19__fab {
  width: min(92vw,344px);
  border-radius: 34px;
  gap: 6px;
}

.pp-19-chk:checked+.pp-19__fab .pp-19__detail {
  opacity: 1;
  translate: 0;
  transition-delay: .22s;
}

.pp-19-chk:checked+.pp-19__fab .pp-19__p {
  display: none;
}

.pp-19-chk:checked+.pp-19__fab .pp-19__q {
  display: block;
}

.pp-19-chk:checked+.pp-19__fab .pp-19__line i {
  animation-play-state: running;
}

@keyframes pp-19-fill {
  from {
    width: 0;
  }

  to {
    width: 100%;
  }
}

.pp-19__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-19-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0.24 0.02 285/.15);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-19 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
