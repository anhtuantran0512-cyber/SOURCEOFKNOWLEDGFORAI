---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/adaptive-dark-mode-sidebar-navigation/"
title: "Adaptive Dark Mode Sidebar Navigation"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "A production navigation rail — brand lockup, six sections with live counters, a settings row and an account footer — that stays legible under both themes…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Adaptive Dark Mode Sidebar Navigation
Source: https://codefronts.com/design-styles/css-dark-mode-ui/adaptive-dark-mode-sidebar-navigation/

A production navigation rail — brand lockup, six sections with live counters, a settings row and an account footer — that stays legible under both themes because every surface, icon stroke and hairline is a token. The active item carries a filled surface and an accent edge, so its state never depends on colour alone. A three-way System / Light / Dark segmented control sits in the footer, pure CSS, no script.
## HTML
```html
<div class="dmu-05">
  <div class="dmu-05__stage">
    <div class="dmu-05__frame">
      <nav class="dmu-05__rail" aria-label="Workspace">
        <div class="dmu-05__brand">
          <span class="dmu-05__logo" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 3.2 20 8v8l-8 4.8L4 16V8Z"/><path d="M12 12v8.8M12 12 4 8M12 12l8-4"/></svg>
          </span>
          <span class="dmu-05__brandText">
            <span class="dmu-05__brandName">Northwind</span>
            <span class="dmu-05__brandPlan">Pro workspace</span>
          </span>
          <svg class="dmu-05__chev" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m8 10 4 4 4-4"/></svg>
        </div>

        <ul class="dmu-05__nav">
          <li><a class="dmu-05__link" href="#dmu-05" aria-current="page">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="3.5" width="7" height="7" rx="1.6"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.6"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.6"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.6"/></svg>
            <span>Overview</span></a></li>
          <li><a class="dmu-05__link" href="#dmu-05">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5V9.2M9.4 19.5V4.5M14.8 19.5v-7.8M20.2 19.5v-4.2"/></svg>
            <span>Analytics</span><span class="dmu-05__count">12</span></a></li>
          <li><a class="dmu-05__link" href="#dmu-05">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6.5h16M4 12h16M4 17.5h10"/></svg>
            <span>Deployments</span></a></li>
          <li><a class="dmu-05__link" href="#dmu-05">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4.3a3.1 3.1 0 1 1 0 6.2 3.1 3.1 0 0 1 0-6.2Z"/><path d="M5 19.7c.5-3.4 3.4-5.2 7-5.2s6.5 1.8 7 5.2"/></svg>
            <span>Members</span><span class="dmu-05__count">28</span></a></li>
          <li><a class="dmu-05__link" href="#dmu-05">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 7.5 12 3 4 7.5v9L12 21l8-4.5Z"/><path d="M12 12v9M4 7.5 12 12l8-4.5"/></svg>
            <span>Storage</span></a></li>
          <li><a class="dmu-05__link" href="#dmu-05">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5.2v13.6M5.2 12h13.6"/></svg>
            <span>Integrations</span><span class="dmu-05__badge">New</span></a></li>
        </ul>

        <div class="dmu-05__foot">
          <fieldset class="dmu-05__theme">
            <legend class="dmu-05__sr">Theme</legend>
            <input class="dmu-05__sr" type="radio" name="dmu-05-theme" id="dmu-05-system" checked>
            <label class="dmu-05__seg" for="dmu-05-system">
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="2.6" y="4.4" width="18.8" height="12.4" rx="2"/><path d="M8.6 20.4h6.8"/></svg>
              System</label>
            <input class="dmu-05__sr" type="radio" name="dmu-05-theme" id="dmu-05-light">
            <label class="dmu-05__seg" for="dmu-05-light">
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.8v2M12 19.2v2M2.8 12h2M19.2 12h2M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
              Light</label>
            <input class="dmu-05__sr" type="radio" name="dmu-05-theme" id="dmu-05-dark">
            <label class="dmu-05__seg" for="dmu-05-dark">
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4Z"/></svg>
              Dark</label>
          </fieldset>

          <a class="dmu-05__link dmu-05__link--settings" href="#dmu-05">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="2.9"/><path d="M12 2.6v2.1M12 19.3v2.1M4.4 4.4l1.5 1.5M18.1 18.1l1.5 1.5M2.6 12h2.1M19.3 12h2.1M4.4 19.6l1.5-1.5M18.1 5.9l1.5-1.5"/></svg>
            <span>Settings</span></a>

          <div class="dmu-05__user">
            <span class="dmu-05__avatar" aria-hidden="true">JL</span>
            <span class="dmu-05__userText">
              <span class="dmu-05__userName">Jordan Lee</span>
              <span class="dmu-05__userMail">[email protected]</span>
            </span>
          </div>
        </div>
      </nav>

      <section class="dmu-05__canvas" aria-label="Content preview">
        <div class="dmu-05__crumbs">Overview <span aria-hidden="true">/</span> Production</div>
        <h1 class="dmu-05__h1">Readable in both themes</h1>
        <p class="dmu-05__lede">Nav surfaces, icon strokes, hairlines and counters each own a token, so the rail keeps its hierarchy when the palette flips. Try the System / Light / Dark control in the footer.</p>
        <div class="dmu-05__tiles">
          <div class="dmu-05__tile"><p>Uptime</p><strong>99.98&#37;</strong></div>
          <div class="dmu-05__tile"><p>p95 latency</p><strong>142ms</strong></div>
          <div class="dmu-05__tile"><p>Open PRs</p><strong>7</strong></div>
        </div>
      </section>
    </div>
  </div>
</div>
```
## CSS
```css
.dmu-05 {
  --bg: #08090c;
  --rail: #0d0f13;
  --canvas: #0a0b0f;
  --elevated: #141721;
  --ink: #eef1f6;
  --muted: #8f98a8;
  --icon: #a7b0c0;
  --line: #1e222c;
  --item-hover: rgba(255,255,255,.05);
  --item-active: rgba(255,255,255,.08);
  --accent: #7c9bff;
  --accent-ink: #070b1a;
  --wash: rgba(124,155,255,.14);
  --focus: #a8c0ff;
  --shadow: rgba(0,0,0,.6);
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

.dmu-05[data-theme="light"],
.dmu-05:has(#dmu-05-light:checked) {
  --bg: #eef0f4;
  --rail: #ffffff;
  --canvas: #f7f8fa;
  --elevated: #ffffff;
  --ink: #0b0d12;
  --muted: #5d6472;
  --icon: #5d6472;
  --line: #e3e6ec;
  --item-hover: rgba(10,12,20,.04);
  --item-active: rgba(10,12,20,.07);
  --accent: #3b5bdb;
  --accent-ink: #ffffff;
  --wash: rgba(59,91,219,.10);
  --focus: #3b5bdb;
  --shadow: rgba(11,13,18,.14);
  color-scheme: light;
}

@media (prefers-color-scheme: light) {
  .dmu-05:not([data-theme="dark"]):has(#dmu-05-system:checked) {
    --bg: #eef0f4;
    --rail: #ffffff;
    --canvas: #f7f8fa;
    --elevated: #ffffff;
    --ink: #0b0d12;
    --muted: #5d6472;
    --icon: #5d6472;
    --line: #e3e6ec;
    --item-hover: rgba(10,12,20,.04);
    --item-active: rgba(10,12,20,.07);
    --accent: #3b5bdb;
    --accent-ink: #ffffff;
    --wash: rgba(59,91,219,.10);
    --focus: #3b5bdb;
    --shadow: rgba(11,13,18,.14);
    color-scheme: light;
  }
  /* flip-back: light OS, dark chosen explicitly */

  .dmu-05:has(#dmu-05-dark:checked) {
    --bg: #08090c;
    --rail: #0d0f13;
    --canvas: #0a0b0f;
    --elevated: #141721;
    --ink: #eef1f6;
    --muted: #8f98a8;
    --icon: #a7b0c0;
    --line: #1e222c;
    --item-hover: rgba(255,255,255,.05);
    --item-active: rgba(255,255,255,.08);
    --accent: #7c9bff;
    --accent-ink: #070b1a;
    --wash: rgba(124,155,255,.14);
    --focus: #a8c0ff;
    --shadow: rgba(0,0,0,.6);
    color-scheme: dark;
  }
}

.dmu-05,
.dmu-05 *,
.dmu-05 *::before,
.dmu-05 *::after {
  box-sizing: border-box;
}

.dmu-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(.75rem,3vw,2.5rem);
}

.dmu-05__frame {
  width: min(72rem,100%);
  display: grid;
  grid-template-columns: 1fr;
  border-radius: 1.15rem;
  overflow: hidden;
  border: 1px solid var(--line);
  background: var(--canvas);
  box-shadow: 0 40px 80px -55px var(--shadow);
}

@media (min-width: 52rem) {
  .dmu-05__frame {
    grid-template-columns: 17.5rem 1fr;
    min-height: min(40rem,80vh);
  }
}

.dmu-05__rail {
  display: grid;
  grid-template-rows: auto 1fr auto;
  gap: .85rem;
  padding: .85rem;
  background: var(--rail);
  border-bottom: 1px solid var(--line);
}

@media (min-width: 52rem) {
  .dmu-05__rail {
    border-bottom: 0;
    border-right: 1px solid var(--line);
  }
}

.dmu-05__brand {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .5rem .55rem;
  border-radius: .7rem;
}

.dmu-05__logo {
  display: grid;
  place-items: center;
  width: 2.1rem;
  height: 2.1rem;
  flex: none;
  border-radius: .6rem;
  background: var(--wash);
  color: var(--accent);
}

.dmu-05__logo svg {
  width: 1.15rem;
  height: 1.15rem;
}

.dmu-05__brandText {
  display: grid;
  gap: .1rem;
  min-width: 0;
}

.dmu-05__brandName {
  font-size: .9rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.dmu-05__brandPlan {
  font-size: .72rem;
  color: var(--muted);
}

.dmu-05__chev {
  width: 1rem;
  height: 1rem;
  margin-left: auto;
  color: var(--muted);
}

.dmu-05__nav {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .12rem;
  align-content: start;
}

.dmu-05__link {
  position: relative;
  display: flex;
  align-items: center;
  gap: .65rem;
  min-height: 2.75rem;
  padding: 0 .7rem;
  border-radius: .6rem;
  text-decoration: none;
  color: var(--muted);
  font-size: .875rem;
  font-weight: 500;
  transition: background-color .18s ease, color .18s ease;
}

.dmu-05__link svg {
  width: 1.1rem;
  height: 1.1rem;
  flex: none;
  color: var(--icon);
  transition: color .18s ease;
}

.dmu-05__link:hover {
  background: var(--item-hover);
  color: var(--ink);
}

.dmu-05__link:hover svg {
  color: var(--ink);
}

.dmu-05__link:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
  color: var(--ink);
}

.dmu-05__link[aria-current="page"] {
  background: var(--item-active);
  color: var(--ink);
  font-weight: 560;
}

.dmu-05__link[aria-current="page"] svg {
  color: var(--accent);
}

.dmu-05__link[aria-current="page"]::before {
  content: '';
  position: absolute;
  inset-block: .5rem;
  inset-inline-start: 0;
  width: 2px;
  border-radius: 2px;
  background: var(--accent);
}

.dmu-05__count {
  margin-left: auto;
  font-family: var(--mono);
  font-variant-numeric: tabular-nums;
  font-size: .72rem;
  color: var(--muted);
}

.dmu-05__badge {
  margin-left: auto;
  font-size: .66rem;
  letter-spacing: .04em;
  text-transform: uppercase;
  padding: .18rem .4rem;
  border-radius: .3rem;
  background: var(--wash);
  color: var(--accent);
}

.dmu-05__foot {
  display: grid;
  gap: .55rem;
  padding-top: .55rem;
  border-top: 1px solid var(--line);
}

.dmu-05__theme {
  margin: 0;
  padding: .22rem;
  border: 1px solid var(--line);
  border-radius: .65rem;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .15rem;
  background: var(--item-hover);
}

.dmu-05__seg {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .3rem;
  min-height: 2.2rem;
  border-radius: .45rem;
  cursor: pointer;
  font-size: .72rem;
  font-weight: 550;
  color: var(--muted);
  transition: background-color .18s ease, color .18s ease;
}

.dmu-05__seg svg {
  width: .9rem;
  height: .9rem;
}

.dmu-05__seg:hover {
  color: var(--ink);
}

.dmu-05__theme input:checked + .dmu-05__seg {
  background: var(--elevated);
  color: var(--ink);
  box-shadow: 0 1px 2px var(--shadow);
}

.dmu-05__theme input:focus-visible + .dmu-05__seg {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-05__link--settings {
  color: var(--muted);
}

.dmu-05__user {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .5rem .55rem;
  border-radius: .6rem;
  background: var(--item-hover);
}

.dmu-05__avatar {
  display: grid;
  place-items: center;
  width: 2rem;
  height: 2rem;
  flex: none;
  border-radius: 50%;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .72rem;
  font-weight: 650;
  letter-spacing: .02em;
}

.dmu-05__userText {
  display: grid;
  gap: .08rem;
  min-width: 0;
}

.dmu-05__userName {
  font-size: .8rem;
  font-weight: 550;
}

.dmu-05__userMail {
  font-size: .7rem;
  color: var(--muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.dmu-05__canvas {
  padding: clamp(1.25rem,3.5vw,2.5rem);
  display: grid;
  gap: .7rem;
  align-content: start;
  background: var(--canvas);
}

.dmu-05__crumbs {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  display: flex;
  gap: .4rem;
}

.dmu-05__h1 {
  margin: 0;
  font-size: clamp(1.35rem,3vw,1.95rem);
  font-weight: 650;
  letter-spacing: -.03em;
}

.dmu-05__lede {
  margin: 0 0 .5rem;
  color: var(--muted);
  font-size: .92rem;
  line-height: 1.65;
  max-width: 52ch;
  text-wrap: pretty;
}

.dmu-05__tiles {
  display: grid;
  gap: .7rem;
  grid-template-columns: repeat(auto-fit,minmax(9rem,1fr));
}

.dmu-05__tile {
  padding: .95rem 1rem;
  border-radius: .8rem;
  background: var(--elevated);
  border: 1px solid var(--line);
}

.dmu-05__tile p {
  margin: 0 0 .35rem;
  font-size: .74rem;
  color: var(--muted);
  letter-spacing: .02em;
}

.dmu-05__tile strong {
  font-family: var(--mono);
  font-variant-numeric: tabular-nums;
  font-size: 1.3rem;
  font-weight: 600;
  letter-spacing: -.03em;
}

@media (prefers-reduced-motion: reduce) {
  .dmu-05__link,
    .dmu-05__seg,
    .dmu-05__link svg {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-05__frame,
    .dmu-05__tile,
    .dmu-05__theme {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-05__link[aria-current="page"] {
    background: Highlight;
    color: HighlightText;
  }

  .dmu-05__theme input:checked + .dmu-05__seg {
    background: Highlight;
    color: HighlightText;
  }
}
```
