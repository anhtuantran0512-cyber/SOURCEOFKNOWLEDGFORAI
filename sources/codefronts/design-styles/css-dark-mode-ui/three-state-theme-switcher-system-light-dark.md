---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/three-state-theme-switcher-system-light-dark/"
title: "Three State Theme Switcher (System / Light / Dark)"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "The control users actually expect in 2027: three states, not two."
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Three State Theme Switcher (System / Light / Dark)
Source: https://codefronts.com/design-styles/css-dark-mode-ui/three-state-theme-switcher-system-light-dark/

The control users actually expect in 2027: three states, not two. System ships no override at all and lets prefers-color-scheme through; Light and Dark pin explicit token sets that win over the media query. Three radios, three labels, one sliding thumb, zero JavaScript — plus a live badge that reports what the OS is currently asking for, so the difference between "System" and "Dark" is visible rather than theoretical.
## HTML
```html
<div class="dmu-09">
  <div class="dmu-09__stage">
    <div class="dmu-09__app">
      <header class="dmu-09__bar">
        <div class="dmu-09__left">
          <span class="dmu-09__logo" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 16.5 12 4l7 12.5"/><path d="M8.4 16.5h7.2"/></svg>
          </span>
          <span class="dmu-09__appName">Cadence</span>
          <span class="dmu-09__osBadge">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><rect x="2.6" y="4.4" width="18.8" height="12.4" rx="2"/><path d="M8.6 20.4h6.8"/></svg>
            OS says <strong class="dmu-09__osDark">dark</strong><strong class="dmu-09__osLight">light</strong>
          </span>
        </div>

        <fieldset class="dmu-09__seg">
          <legend class="dmu-09__sr">Theme</legend>
          <span class="dmu-09__thumb" aria-hidden="true"></span>
          <input class="dmu-09__sr" type="radio" name="dmu-09-theme" id="dmu-09-system" checked>
          <label class="dmu-09__opt" for="dmu-09-system">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="2.6" y="4.4" width="18.8" height="12.4" rx="2"/><path d="M8.6 20.4h6.8"/></svg>
            System</label>
          <input class="dmu-09__sr" type="radio" name="dmu-09-theme" id="dmu-09-light">
          <label class="dmu-09__opt" for="dmu-09-light">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.8v2M12 19.2v2M2.8 12h2M19.2 12h2M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
            Light</label>
          <input class="dmu-09__sr" type="radio" name="dmu-09-theme" id="dmu-09-dark">
          <label class="dmu-09__opt" for="dmu-09-dark">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4Z"/></svg>
            Dark</label>
        </fieldset>
      </header>

      <div class="dmu-09__body">
        <section class="dmu-09__panel">
          <p class="dmu-09__kicker">Appearance</p>
          <h1 class="dmu-09__h1">Three states, one radio group</h1>
          <p class="dmu-09__lede">System defers to the operating system. Light and Dark pin the theme and survive an OS change mid-session &mdash; including on machines whose preference already matches your default.</p>

          <div class="dmu-09__matrix">
            <div class="dmu-09__cell"><span>OS light</span><em>System</em><b>light</b></div>
            <div class="dmu-09__cell"><span>OS light</span><em>Dark</em><b>dark</b></div>
            <div class="dmu-09__cell"><span>OS dark</span><em>System</em><b>dark</b></div>
            <div class="dmu-09__cell"><span>OS dark</span><em>Light</em><b>light</b></div>
          </div>
        </section>

        <aside class="dmu-09__side">
          <div class="dmu-09__row"><span class="dmu-09__dot" aria-hidden="true"></span>Sync across devices</div>
          <div class="dmu-09__row"><span class="dmu-09__dot dmu-09__dot--muted" aria-hidden="true"></span>Dim images in dark mode</div>
          <div class="dmu-09__row"><span class="dmu-09__dot dmu-09__dot--muted" aria-hidden="true"></span>Reduce transparency</div>
          <p class="dmu-09__sideNote">Preference stored per workspace. Rendering stays pure CSS.</p>
        </aside>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.dmu-09 {
  --bg: #0b0b10;
  --surface: #12131a;
  --elevated: #191b24;
  --ink: #f4f4f7;
  --muted: #969ba9;
  --line: #262935;
  --track: rgba(255,255,255,.05);
  --accent: #a3e635;
  --accent-ink: #131c05;
  --wash: rgba(163,230,53,.14);
  --focus: #bef264;
  --shadow: rgba(0,0,0,.7);
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-09[data-theme="light"],
.dmu-09:has(#dmu-09-light:checked) {
  --bg: #f4f5f8;
  --surface: #ffffff;
  --elevated: #ffffff;
  --ink: #0b0b12;
  --muted: #5a6070;
  --line: #e3e5ec;
  --track: rgba(11,11,18,.05);
  --accent: #3f6212;
  --accent-ink: #ffffff;
  --wash: rgba(63,98,18,.10);
  --focus: #3f6212;
  --shadow: rgba(11,11,18,.16);
  color-scheme: light;
}

@media (prefers-color-scheme: light) {
  .dmu-09:not([data-theme="dark"]):has(#dmu-09-system:checked) {
    --bg: #f4f5f8;
    --surface: #ffffff;
    --elevated: #ffffff;
    --ink: #0b0b12;
    --muted: #5a6070;
    --line: #e3e5ec;
    --track: rgba(11,11,18,.05);
    --accent: #3f6212;
    --accent-ink: #ffffff;
    --wash: rgba(63,98,18,.10);
    --focus: #3f6212;
    --shadow: rgba(11,11,18,.16);
    color-scheme: light;
  }
  /* flip-back: explicit dark still wins on a light OS */

  .dmu-09:has(#dmu-09-dark:checked) {
    --bg: #0b0b10;
    --surface: #12131a;
    --elevated: #191b24;
    --ink: #f4f4f7;
    --muted: #969ba9;
    --line: #262935;
    --track: rgba(255,255,255,.05);
    --accent: #a3e635;
    --accent-ink: #131c05;
    --wash: rgba(163,230,53,.14);
    --focus: #bef264;
    --shadow: rgba(0,0,0,.7);
    color-scheme: dark;
  }
}

.dmu-09,
.dmu-09 *,
.dmu-09 *::before,
.dmu-09 *::after {
  box-sizing: border-box;
}

.dmu-09__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-09__app {
  width: min(64rem,100%);
  border-radius: 1.2rem;
  overflow: hidden;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 36px 70px -48px var(--shadow);
}

.dmu-09__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  padding: .85rem 1.1rem;
  border-bottom: 1px solid var(--line);
}

.dmu-09__left {
  display: flex;
  align-items: center;
  gap: .6rem;
  flex-wrap: wrap;
}

.dmu-09__logo {
  display: grid;
  place-items: center;
  width: 2rem;
  height: 2rem;
  border-radius: .6rem;
  background: var(--wash);
  color: var(--accent);
}

.dmu-09__logo svg {
  width: 1.1rem;
  height: 1.1rem;
}

.dmu-09__appName {
  font-weight: 600;
  letter-spacing: -.02em;
}

.dmu-09__osBadge {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  font-family: var(--mono);
  font-size: .7rem;
  padding: .3rem .5rem;
  border-radius: .4rem;
  color: var(--muted);
  background: var(--track);
  border: 1px solid var(--line);
}

.dmu-09__osBadge svg {
  width: .9rem;
  height: .9rem;
}

.dmu-09__osBadge strong {
  color: var(--ink);
  font-weight: 600;
}

.dmu-09__osLight {
  display: none;
}

.dmu-09__osDark {
  display: inline;
}

@media (prefers-color-scheme: light) {
  .dmu-09__osLight {
    display: inline;
  }

  .dmu-09__osDark {
    display: none;
  }
}

.dmu-09__seg {
  position: relative;
  margin: 0;
  padding: .25rem;
  border: 1px solid var(--line);
  border-radius: .75rem;
  display: grid;
  grid-template-columns: repeat(3,minmax(4.75rem,1fr));
  background: var(--track);
}

.dmu-09__thumb {
  position: absolute;
  top: .25rem;
  bottom: .25rem;
  left: .25rem;
  width: calc((100% - .5rem) / 3);
  border-radius: .55rem;
  background: var(--elevated);
  border: 1px solid var(--line);
  box-shadow: 0 2px 6px var(--shadow);
  transition: translate .28s cubic-bezier(.16,1,.3,1);
}

.dmu-09__seg:has(#dmu-09-light:checked) .dmu-09__thumb {
  translate: 100% 0;
}

.dmu-09__seg:has(#dmu-09-dark:checked) .dmu-09__thumb {
  translate: 200% 0;
}

.dmu-09__opt {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .35rem;
  min-height: 2.35rem;
  border-radius: .55rem;
  cursor: pointer;
  font-size: .78rem;
  font-weight: 550;
  color: var(--muted);
  transition: color .18s ease;
}

.dmu-09__opt svg {
  width: .95rem;
  height: .95rem;
}

.dmu-09__opt:hover {
  color: var(--ink);
}

.dmu-09__seg input:checked + .dmu-09__opt {
  color: var(--ink);
}

.dmu-09__seg input:focus-visible + .dmu-09__opt {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-09__body {
  display: grid;
}

@media (min-width: 56rem) {
  .dmu-09__body {
    grid-template-columns: 1.5fr 1fr;
  }
}

.dmu-09__panel {
  padding: clamp(1.25rem,3vw,2rem);
  display: grid;
  gap: .55rem;
  align-content: start;
}

.dmu-09__kicker {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent);
}

.dmu-09__h1 {
  margin: 0;
  font-size: clamp(1.4rem,3.2vw,2rem);
  font-weight: 650;
  letter-spacing: -.03em;
}

.dmu-09__lede {
  margin: 0 0 .55rem;
  color: var(--muted);
  font-size: .93rem;
  line-height: 1.65;
  max-width: 48ch;
  text-wrap: pretty;
}

.dmu-09__matrix {
  display: grid;
  gap: .5rem;
  grid-template-columns: repeat(auto-fit,minmax(10rem,1fr));
}

.dmu-09__cell {
  display: grid;
  gap: .15rem;
  padding: .7rem .8rem;
  border-radius: .65rem;
  background: var(--elevated);
  border: 1px solid var(--line);
}

.dmu-09__cell span {
  font-family: var(--mono);
  font-size: .68rem;
  color: var(--muted);
}

.dmu-09__cell em {
  font-style: normal;
  font-size: .8rem;
  font-weight: 550;
}

.dmu-09__cell b {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--accent);
}

.dmu-09__side {
  padding: clamp(1.25rem,3vw,2rem);
  display: grid;
  gap: .5rem;
  align-content: start;
  background: var(--bg);
  border-top: 1px solid var(--line);
}

@media (min-width: 56rem) {
  .dmu-09__side {
    border-top: 0;
    border-left: 1px solid var(--line);
  }
}

.dmu-09__row {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .7rem .8rem;
  border-radius: .6rem;
  background: var(--surface);
  border: 1px solid var(--line);
  font-size: .83rem;
}

.dmu-09__dot {
  width: .6rem;
  height: .6rem;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 0 3px var(--wash);
}

.dmu-09__dot--muted {
  background: var(--muted);
  box-shadow: none;
}

.dmu-09__sideNote {
  margin: .25rem 0 0;
  font-size: .76rem;
  line-height: 1.6;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .dmu-09__thumb,
    .dmu-09__opt {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-09__app,
    .dmu-09__cell,
    .dmu-09__row,
    .dmu-09__seg {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-09__thumb {
    background: Highlight;
  }

  .dmu-09__seg input:checked + .dmu-09__opt {
    color: HighlightText;
  }
}
```
