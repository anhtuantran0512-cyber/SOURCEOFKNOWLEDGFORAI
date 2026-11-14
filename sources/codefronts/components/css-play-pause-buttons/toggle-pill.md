---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/toggle-pill/"
title: "Sliding Pill Audio Toggle Switch"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "A pill switch built for media: the knob slides, the track colour shifts, and the play/pause glyphs cross-fade in the knob while the opposite label appears on…"
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sliding Pill Audio Toggle Switch
Source: https://codefronts.com/components/css-play-pause-buttons/toggle-pill/

A pill switch built for media: the knob slides, the track colour shifts, and the play/pause glyphs cross-fade in the knob while the opposite label appears on the empty side of the track — so both states are readable at a glance, not just inferred from position. Text labels ride along, which is what keeps this accessible where an icon-only switch fails.
## HTML
```html
<section class="pp-14" aria-label="Sliding pill audio toggle switch demo">
  <div class="pp-14__stage">
    <div class="pp-14__card">
      <div class="pp-14__row">
        <span class="pp-14__note" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="20" height="20"><path d="M9 18V6l10-2v12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="6.5" cy="18" r="2.6" fill="currentColor"/><circle cx="16.5" cy="16" r="2.6" fill="currentColor"/></svg>
        </span>
        <div>
          <p class="pp-14__title">Ambient Focus</p>
          <p class="pp-14__sub">Continuous mix · 6 h</p>
        </div>
      </div>
      <input class="pp-14-chk" type="checkbox" id="pp-14-toggle" aria-label="Play or pause Ambient Focus">
      <label class="pp-14__switch" for="pp-14-toggle">
        <span class="pp-14__word pp-14__word--play">Play</span>
        <span class="pp-14__word pp-14__word--pause">Pause</span>
        <span class="pp-14__knob" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="17" height="17">
            <path class="pp-14__p" d="M9 5.8v12.4L18.6 12z" fill="currentColor"/>
            <path class="pp-14__q" d="M8.6 5.8h3.1v12.4H8.6zM13 5.8h3.1v12.4H13z" fill="currentColor"/>
          </svg>
        </span>
      </label>
    </div>
    <p class="pp-14__chip" aria-hidden="true">translate: calc(100% + 6px) · spring easing · size-independent throw</p>
  </div>
</section>
```
## CSS
```css
.pp-14,
.pp-14 *,
.pp-14 *::before,
.pp-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-14-bg);
  --pp-14-bg: oklch(0.96 0.01 160);
  --pp-14-card: oklch(1 0 0);
  --pp-14-ink: oklch(0.25 0.02 165);
  --pp-14-mut: oklch(0.55 0.02 165);
  --pp-14-line: oklch(0.9 0.012 165);
  --pp-14-acc: oklch(0.62 0.15 158);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-14-ink);
}

.pp-14__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(80% 60% at 50% 0%,oklch(0.92 0.06 160/.65),transparent 70%);
}

.pp-14__card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 28px;
  flex-wrap: wrap;
  width: min(100%,470px);
  padding: 22px 24px;
  border: 1px solid var(--pp-14-line);
  border-radius: 22px;
  background: var(--pp-14-card);
  box-shadow: 0 20px 44px oklch(0.4 0.04 165/.14);
}

.pp-14__row {
  display: flex;
  align-items: center;
  gap: 14px;
}

.pp-14__note {
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  border-radius: 14px;
  background: color-mix(in oklch,var(--pp-14-acc) 14%,transparent);
  color: var(--pp-14-acc);
}

.pp-14__title {
  font-size: 16px;
  font-weight: 660;
  letter-spacing: -.01em;
}

.pp-14__sub {
  font-size: 12.5px;
  color: var(--pp-14-mut);
  margin-top: 3px;
}

.pp-14-chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-14__switch {
  position: relative;
  display: flex;
  align-items: center;
  width: 120px;
  height: 48px;
  padding: 5px;
  border-radius: 99px;
  background: var(--pp-14-line);
  cursor: pointer;
  transition: background .38s;
}

.pp-14__word {
  position: absolute;
  font-size: 11.5px;
  font-weight: 660;
  letter-spacing: .03em;
  transition: opacity .3s;
}

.pp-14__word--play {
  right: 16px;
  color: var(--pp-14-mut);
}

.pp-14__word--pause {
  left: 18px;
  color: oklch(0.99 0 0);
  opacity: 0;
}

.pp-14__knob {
  position: absolute;
  top: 5px;
  left: 5px;
  bottom: 5px;
  aspect-ratio: 1;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: var(--pp-14-card);
  color: var(--pp-14-acc);
  box-shadow: 0 3px 10px oklch(0.3 0.03 165/.3);
  translate: 0;
  transition: translate .38s cubic-bezier(.34,1.35,.5,1),scale .18s;
}

.pp-14__switch:active .pp-14__knob {
  scale: .93;
}

.pp-14-chk:focus-visible+.pp-14__switch {
  outline: 3px solid var(--pp-14-acc);
  outline-offset: 4px;
}

.pp-14__q {
  display: none;
}

.pp-14-chk:checked+.pp-14__switch {
  background: var(--pp-14-acc);
}

.pp-14-chk:checked+.pp-14__switch .pp-14__knob {
  translate: 72px 0;
}

.pp-14-chk:checked+.pp-14__switch .pp-14__word--play {
  opacity: 0;
}

.pp-14-chk:checked+.pp-14__switch .pp-14__word--pause {
  opacity: 1;
}

.pp-14-chk:checked+.pp-14__switch .pp-14__p {
  display: none;
}

.pp-14-chk:checked+.pp-14__switch .pp-14__q {
  display: block;
}

.pp-14__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-14-mut);
  padding: 7px 14px;
  border: 1px solid var(--pp-14-line);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-14 * {
    transition-duration: .01ms !important;
  }
}
```
