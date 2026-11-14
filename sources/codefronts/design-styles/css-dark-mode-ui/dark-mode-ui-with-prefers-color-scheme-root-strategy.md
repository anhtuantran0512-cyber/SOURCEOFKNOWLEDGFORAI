---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-ui-with-prefers-color-scheme-root-strategy/"
title: "Dark Mode UI with prefers-color-scheme Root Strategy"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "The baseline pattern every other dark-mode technique builds on: declare your token block once on the component root, then let one media query re-declare the…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode UI with prefers-color-scheme Root Strategy
Source: https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-ui-with-prefers-color-scheme-root-strategy/

The baseline pattern every other dark-mode technique builds on: declare your token block once on the component root, then let one media query re-declare the same token names for dark. No toggle, no attribute, no script — the UI simply obeys the operating system. Three panels render identical markup: a forced-light reference, a forced-dark reference, and one live panel that follows your current OS preference right now.
## HTML
```html
<div class="dmu-01">
  <!-- Pair this component with, in your document head:
       <meta name="theme-color" media="(prefers-color-scheme: light)" content="#ffffff">
       <meta name="theme-color" media="(prefers-color-scheme: dark)"  content="#09090b"> -->
  <div class="dmu-01__stage">
    <header class="dmu-01__head">
      <h1 class="dmu-01__h1">Root token strategy</h1>
      <p class="dmu-01__lede">One token block, one media query. Identical markup, three renderings.</p>
    </header>

    <div class="dmu-01__grid">
      <section class="dmu-01__panel dmu-01__panel--light">
        <p class="dmu-01__badge">Forced light reference</p>
        <article class="dmu-01__card">
          <div class="dmu-01__cardTop">
            <span class="dmu-01__dot" aria-hidden="true"></span>
            <span class="dmu-01__cardKicker">Deploy</span>
          </div>
          <h2 class="dmu-01__cardTitle">edge-runtime v4.2</h2>
          <p class="dmu-01__cardBody">Promoted to production 14 minutes ago by Alex Chen.</p>
          <div class="dmu-01__cardFoot">
            <button class="dmu-01__btn" type="button">View build</button>
            <span class="dmu-01__meta">iad1</span>
          </div>
        </article>
      </section>

      <section class="dmu-01__panel dmu-01__panel--dark">
        <p class="dmu-01__badge">Forced dark reference</p>
        <article class="dmu-01__card">
          <div class="dmu-01__cardTop">
            <span class="dmu-01__dot" aria-hidden="true"></span>
            <span class="dmu-01__cardKicker">Deploy</span>
          </div>
          <h2 class="dmu-01__cardTitle">edge-runtime v4.2</h2>
          <p class="dmu-01__cardBody">Promoted to production 14 minutes ago by Alex Chen.</p>
          <div class="dmu-01__cardFoot">
            <button class="dmu-01__btn" type="button">View build</button>
            <span class="dmu-01__meta">iad1</span>
          </div>
        </article>
      </section>

      <section class="dmu-01__panel dmu-01__panel--live">
        <p class="dmu-01__badge">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8.5 20.5h7"/><path d="M12 17v3.5"/></svg>
          Live &mdash; follows your OS
        </p>
        <article class="dmu-01__card">
          <div class="dmu-01__cardTop">
            <span class="dmu-01__dot" aria-hidden="true"></span>
            <span class="dmu-01__cardKicker">Deploy</span>
          </div>
          <h2 class="dmu-01__cardTitle">edge-runtime v4.2</h2>
          <p class="dmu-01__cardBody">Promoted to production 14 minutes ago by Alex Chen.</p>
          <div class="dmu-01__cardFoot">
            <button class="dmu-01__btn" type="button">View build</button>
            <span class="dmu-01__meta">iad1</span>
          </div>
        </article>
      </section>
    </div>

    <aside class="dmu-01__notes">
      <h3 class="dmu-01__notesTitle">What the media query flips</h3>
      <dl class="dmu-01__tokens">
        <div class="dmu-01__row"><dt>--bg</dt><dd><span class="dmu-01__sw" style="background:#ffffff"></span>#ffffff<span class="dmu-01__arrow" aria-hidden="true">&rarr;</span><span class="dmu-01__sw" style="background:#09090b"></span>#09090b</dd></div>
        <div class="dmu-01__row"><dt>--surface</dt><dd><span class="dmu-01__sw" style="background:#f6f6f7"></span>#f6f6f7<span class="dmu-01__arrow" aria-hidden="true">&rarr;</span><span class="dmu-01__sw" style="background:#121216"></span>#121216</dd></div>
        <div class="dmu-01__row"><dt>--ink</dt><dd><span class="dmu-01__sw" style="background:#0a0a0b"></span>#0a0a0b<span class="dmu-01__arrow" aria-hidden="true">&rarr;</span><span class="dmu-01__sw" style="background:#f4f4f5"></span>#f4f4f5</dd></div>
        <div class="dmu-01__row"><dt>--line</dt><dd><span class="dmu-01__sw" style="background:#e3e3e7"></span>#e3e3e7<span class="dmu-01__arrow" aria-hidden="true">&rarr;</span><span class="dmu-01__sw" style="background:#26262c"></span>#26262c</dd></div>
        <div class="dmu-01__row"><dt>--accent</dt><dd><span class="dmu-01__sw" style="background:#4f46e5"></span>#4f46e5<span class="dmu-01__arrow" aria-hidden="true">&rarr;</span><span class="dmu-01__sw" style="background:#8b8bff"></span>#8b8bff</dd></div>
      </dl>
      <p class="dmu-01__notesFoot">No toggle ships here on purpose: this is the pure OS-driven baseline. Layer an override on top only when a visitor needs to disagree with their system.</p>
    </aside>
  </div>
</div>
```
## CSS
```css
.dmu-01 {
  --bg: #ffffff;
  --surface: #f6f6f7;
  --elevated: #ffffff;
  --ink: #0a0a0b;
  --muted: #5b5f66;
  --line: #e3e3e7;
  --accent: #4f46e5;
  --accent-ink: #ffffff;
  --focus: #4f46e5;
  --dot: #16a34a;
  --shadow: rgba(9,9,11,.10);
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: light dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: dark) {
  .dmu-01 {
    --bg: #09090b;
    --surface: #121216;
    --elevated: #17171c;
    --ink: #f4f4f5;
    --muted: #a1a1aa;
    --line: #26262c;
    --accent: #8b8bff;
    --accent-ink: #0a0a12;
    --focus: #a5b4fc;
    --dot: #4ade80;
    --shadow: rgba(0,0,0,.6);
  }
}

@supports (color: oklch(50% .1 250)) {
  .dmu-01 {
    --bg: oklch(100% 0 0);
    --surface: oklch(97% .003 285);
    --ink: oklch(14% .01 285);
    --accent: oklch(50% .21 275);
  }

  @media (prefers-color-scheme: dark) {
    .dmu-01 {
      --bg: oklch(14% .008 285);
      --surface: oklch(19% .012 285);
      --ink: oklch(96% .004 285);
      --accent: oklch(76% .13 280);
    }
  }
}

.dmu-01,
.dmu-01 *,
.dmu-01 *::before,
.dmu-01 *::after {
  box-sizing: border-box;
}

.dmu-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  align-content: center;
  gap: clamp(1.5rem,3vw,2.5rem);
  padding: clamp(1.25rem,5vw,3.5rem);
  max-width: 82rem;
  margin-inline: auto;
}

.dmu-01__head {
  display: grid;
  gap: .45rem;
}

.dmu-01__h1 {
  margin: 0;
  font-size: clamp(1.35rem,3vw,1.9rem);
  font-weight: 650;
  letter-spacing: -.025em;
}

.dmu-01__lede {
  margin: 0;
  color: var(--muted);
  font-size: .95rem;
}

.dmu-01__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(15rem,1fr));
}

.dmu-01__panel {
  display: grid;
  gap: .75rem;
  padding: 1rem;
  border-radius: 1rem;
  background: var(--surface);
  border: 1px solid var(--line);
  color: var(--ink);
}

.dmu-01__panel--light {
  --bg: #ffffff;
  --surface: #f6f6f7;
  --elevated: #ffffff;
  --ink: #0a0a0b;
  --muted: #5b5f66;
  --line: #e3e3e7;
  --accent: #4f46e5;
  --accent-ink: #ffffff;
  --dot: #16a34a;
  --shadow: rgba(9,9,11,.10);
}

.dmu-01__panel--dark {
  --bg: #09090b;
  --surface: #121216;
  --elevated: #17171c;
  --ink: #f4f4f5;
  --muted: #a1a1aa;
  --line: #26262c;
  --accent: #8b8bff;
  --accent-ink: #0a0a12;
  --dot: #4ade80;
  --shadow: rgba(0,0,0,.6);
}

.dmu-01__badge {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .4rem;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
}

.dmu-01__badge svg {
  width: .95rem;
  height: .95rem;
}

.dmu-01__card {
  display: grid;
  gap: .6rem;
  padding: 1.05rem;
  border-radius: .85rem;
  background: var(--elevated);
  border: 1px solid var(--line);
  box-shadow: 0 1px 2px var(--shadow), 0 12px 28px -20px var(--shadow);
}

.dmu-01__cardTop {
  display: flex;
  align-items: center;
  gap: .5rem;
}

.dmu-01__dot {
  width: .5rem;
  height: .5rem;
  border-radius: 50%;
  background: var(--dot);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--dot) 22%,transparent);
}

.dmu-01__cardKicker {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.dmu-01__cardTitle {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: -.02em;
  font-family: var(--mono);
}

.dmu-01__cardBody {
  margin: 0;
  font-size: .875rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.dmu-01__cardFoot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .75rem;
  margin-top: .15rem;
}

.dmu-01__btn {
  min-height: 2.5rem;
  padding: 0 .95rem;
  border: 1px solid transparent;
  border-radius: .55rem;
  font: inherit;
  font-size: .85rem;
  font-weight: 550;
  cursor: pointer;
  background: var(--accent);
  color: var(--accent-ink);
  transition: filter .18s ease, translate .18s ease;
}

.dmu-01__btn:hover {
  filter: brightness(1.08);
  translate: 0 -1px;
}

.dmu-01__btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-01__meta {
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--muted);
}

.dmu-01__notes {
  display: grid;
  gap: .85rem;
  padding: clamp(1rem,2.5vw,1.5rem);
  border-radius: 1rem;
  background: var(--surface);
  border: 1px solid var(--line);
}

.dmu-01__notesTitle {
  margin: 0;
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.dmu-01__tokens {
  margin: 0;
  display: grid;
  gap: .35rem;
}

.dmu-01__row {
  display: grid;
  grid-template-columns: minmax(6rem,9rem) 1fr;
  gap: .75rem;
  align-items: center;
  padding: .45rem .55rem;
  border-radius: .5rem;
  background: var(--bg);
  border: 1px solid var(--line);
}

.dmu-01__row dt {
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--accent);
}

.dmu-01__row dd {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .4rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
}

.dmu-01__sw {
  width: .85rem;
  height: .85rem;
  border-radius: .25rem;
  border: 1px solid var(--line);
}

.dmu-01__arrow {
  padding-inline: .3rem;
  color: var(--ink);
}

.dmu-01__notesFoot {
  margin: 0;
  font-size: .83rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 60ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .dmu-01__btn {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-01__card,
    .dmu-01__panel,
    .dmu-01__notes,
    .dmu-01__row {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-01__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
```
