---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/equaliser-bars/"
title: "Equalizer Soundwave Animated Toggle"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "The 'now playing' equalizer, generated entirely in CSS: 28 bars driven by one keyframe, each offset by a negative animation-delay so the wave never marches…"
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Equalizer Soundwave Animated Toggle
Source: https://codefronts.com/components/css-play-pause-buttons/equaliser-bars/

The 'now playing' equalizer, generated entirely in CSS: 28 bars driven by one keyframe, each offset by a negative animation-delay so the wave never marches in lockstep. Press play and the bars come alive; press pause and they settle to a flat line. Because the stagger is computed from a per-bar custom property, adding bars is a copy-paste — no extra CSS.
## HTML
```html
<section class="pp-10" aria-label="Equalizer soundwave animated toggle demo">
  <div class="pp-10__stage">
    <div class="pp-10__rig">
      <div class="pp-10__head">
        <p class="pp-10__station">FREQUENCY 108.4</p>
        <p class="pp-10__now">Deep Field — Live Session</p>
      </div>
      <div class="pp-10__wave" aria-hidden="true">
        <span style="--pp-10-i:0"></span><span style="--pp-10-i:1"></span><span style="--pp-10-i:2"></span><span style="--pp-10-i:3"></span><span style="--pp-10-i:4"></span><span style="--pp-10-i:5"></span><span style="--pp-10-i:6"></span><span style="--pp-10-i:7"></span><span style="--pp-10-i:8"></span><span style="--pp-10-i:9"></span><span style="--pp-10-i:10"></span><span style="--pp-10-i:11"></span><span style="--pp-10-i:12"></span><span style="--pp-10-i:13"></span><span style="--pp-10-i:14"></span><span style="--pp-10-i:15"></span><span style="--pp-10-i:16"></span><span style="--pp-10-i:17"></span><span style="--pp-10-i:18"></span><span style="--pp-10-i:19"></span><span style="--pp-10-i:20"></span><span style="--pp-10-i:21"></span><span style="--pp-10-i:22"></span><span style="--pp-10-i:23"></span><span style="--pp-10-i:24"></span><span style="--pp-10-i:25"></span><span style="--pp-10-i:26"></span><span style="--pp-10-i:27"></span>
      </div>
      <input class="pp-10-chk" type="checkbox" id="pp-10-toggle" aria-label="Play or pause the live session">
      <label class="pp-10__btn" for="pp-10-toggle">
        <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">
          <path class="pp-10__p" d="M8.8 5.6v12.8L18.6 12z" fill="currentColor"/>
          <path class="pp-10__q" d="M8.4 5.6h3.1v12.8H8.4zM12.9 5.6H16v12.8h-3.1z" fill="currentColor"/>
        </svg>
      </label>
    </div>
    <p class="pp-10__chip" aria-hidden="true">negative animation-delay stagger · scaleY on the compositor · one keyframe</p>
  </div>
</section>
```
## CSS
```css
.pp-10,
.pp-10 *,
.pp-10 *::before,
.pp-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-10-bg);
  --pp-10-bg: oklch(0.15 0.025 275);
  --pp-10-card: oklch(0.2 0.03 275);
  --pp-10-ink: oklch(0.97 0.006 270);
  --pp-10-mut: oklch(0.68 0.03 275);
  --pp-10-acc: oklch(0.78 0.17 330);
  --pp-10-acc2: oklch(0.82 0.15 195);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-10-ink);
}

.pp-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(75% 55% at 50% 100%,oklch(0.3 0.1 330/.45),transparent 70%);
}

.pp-10__rig {
  display: grid;
  gap: 22px;
  width: min(100%,540px);
  padding: 28px 30px;
  border-radius: 24px;
  background: var(--pp-10-card);
  box-shadow: 0 0 0 1px oklch(1 0 0/.07),0 28px 64px oklch(0 0 0/.5);
}

.pp-10__station {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .2em;
  color: var(--pp-10-acc);
}

.pp-10__now {
  font-size: 18px;
  font-weight: 650;
  letter-spacing: -.015em;
  margin-top: 7px;
}

.pp-10__wave {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 3px;
  height: 92px;
  padding: 0 2px;
}

.pp-10__wave span {
  flex: 1;
  height: 70%;
  min-width: 3px;
  border-radius: 99px;
  background: linear-gradient(to top,var(--pp-10-acc),var(--pp-10-acc2));
  scale: 1 .12;
  transform-origin: center;
  transition: scale .5s cubic-bezier(.3,0,.2,1);
  animation: pp-10-wave 1.1s ease-in-out infinite alternate;
  animation-delay: calc(var(--pp-10-i) * -80ms);
  animation-play-state: paused;
}

.pp-10-chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-10__btn {
  justify-self: start;
  display: grid;
  place-items: center;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(140deg,var(--pp-10-acc),var(--pp-10-acc2));
  color: oklch(0.16 0.03 300);
  cursor: pointer;
  box-shadow: 0 10px 30px oklch(0.5 0.2 330/.35);
  transition: transform .24s cubic-bezier(.34,1.4,.5,1),box-shadow .3s;
}

.pp-10__btn:hover {
  transform: scale(1.07);
}

.pp-10-chk:focus-visible+.pp-10__btn {
  outline: 3px solid var(--pp-10-acc2);
  outline-offset: 4px;
}

.pp-10__q {
  display: none;
}

.pp-10__rig:has(.pp-10-chk:checked) .pp-10__wave span {
  animation-play-state: running;
}

.pp-10__rig:has(.pp-10-chk:checked) .pp-10__p {
  display: none;
}

.pp-10__rig:has(.pp-10-chk:checked) .pp-10__q {
  display: block;
}

@keyframes pp-10-wave {
  from {
    scale: 1 .18;
  }

  to {
    scale: 1 1;
  }
}

.pp-10__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-10-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.12);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-10__wave span {
    animation: none !important;
    scale: 1 .35;
  }

  .pp-10 * {
    transition-duration: .01ms !important;
  }
}
```
