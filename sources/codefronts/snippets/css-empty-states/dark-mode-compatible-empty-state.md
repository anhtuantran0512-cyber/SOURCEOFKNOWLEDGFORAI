---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/dark-mode-compatible-empty-state/"
title: "Dark Mode Compatible Empty State"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "One empty state that survives three appearance modes in pure CSS: a three-way System / Light / Dark control built from radios, read by :has(), that repaints…"
has_js: "false"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Compatible Empty State
Source: https://codefronts.com/snippets/css-empty-states/dark-mode-compatible-empty-state/

One empty state that survives three appearance modes in pure CSS: a three-way System / Light / Dark control built from radios, read by :has(), that repaints an entire settings surface by swapping nine tokens. System defers to prefers-color-scheme, so the same markup follows the OS until the user overrides it.
## HTML
```html
<div class="est-19">
  <input class="est-19__sr" type="radio" name="est-19-theme" id="est-19-sys" checked>
  <input class="est-19__sr" type="radio" name="est-19-theme" id="est-19-light">
  <input class="est-19__sr" type="radio" name="est-19-theme" id="est-19-dark">

  <div class="est-19__shell">
    <aside class="est-19__side">
      <span class="est-19__logo">Beacon</span>
      <nav class="est-19__nav">
        <a class="est-19__nl" href="#est-19">General</a>
        <a class="est-19__nl" href="#est-19">Members</a>
        <a class="est-19__nl est-19__nl--on" href="#est-19" aria-current="page">Integrations</a>
        <a class="est-19__nl" href="#est-19">Billing</a>
        <a class="est-19__nl" href="#est-19">Audit log</a>
      </nav>
    </aside>

    <main class="est-19__main">
      <header class="est-19__top">
        <h1 class="est-19__h1">Integrations</h1>
        <div class="est-19__themes" role="group" aria-label="Appearance">
          <label class="est-19__tl" for="est-19-sys">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="3.5" y="5" width="17" height="11.5" rx="2" stroke="currentColor" stroke-width="1.6"/><path d="M9 19.5h6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
            System
          </label>
          <label class="est-19__tl" for="est-19-light">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5v2M12 18.5v2M3.5 12h2M18.5 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
            Light
          </label>
          <label class="est-19__tl" for="est-19-dark">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
            Dark
          </label>
        </div>
      </header>

      <section class="est-19__panel">
        <div class="est-19__ptop">
          <span class="est-19__ptitle">Connected services</span>
          <span class="est-19__ptag">none</span>
        </div>

        <div class="est-19__empty">
          <span class="est-19__plug" aria-hidden="true">
            <span class="est-19__socket"></span>
            <span class="est-19__prongs"><i></i><i></i></span>
          </span>
          <h2 class="est-19__eh">No services connected</h2>
          <p class="est-19__ep">Connect the tools your team already pays for and Beacon starts reading events from them within a minute.</p>
          <div class="est-19__eacts">
            <button class="est-19__pri" type="button">Browse the directory</button>
            <button class="est-19__ghost" type="button">Create an API key</button>
          </div>
        </div>

        <ul class="est-19__avail">
          <li><span class="est-19__ai" data-i="1" aria-hidden="true"></span>Slack<span class="est-19__ac">Alerts and digests</span></li>
          <li><span class="est-19__ai" data-i="2" aria-hidden="true"></span>Linear<span class="est-19__ac">Issue sync</span></li>
          <li><span class="est-19__ai" data-i="3" aria-hidden="true"></span>Snowflake<span class="est-19__ac">Warehouse export</span></li>
        </ul>
      </section>
    </main>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-19 {
  --bg: #f7f7f8;
  --surface: #ffffff;
  --sunk: #eff0f2;
  --line: #e4e5e8;
  --line-2: #d2d4d8;
  --ink: #15161a;
  --muted: #5a5d65;
  --faint: #8a8d95;
  --accent: #4256c8;
  --on-accent: #ffffff;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
  transition: background .3s ease, color .3s ease;
}

.est-19 *,
.est-19 *::before,
.est-19 *::after {
  box-sizing: border-box;
}

.est-19 [hidden] {
  display: none !important;
}

.est-19__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-19 {
    --bg: oklch(0.974 0.002 285);
    --surface: oklch(1 0 0);
    --sunk: oklch(0.955 0.003 285);
    --line: oklch(0.918 0.004 285);
    --line-2: oklch(0.862 0.006 285);
    --ink: oklch(0.175 0.009 280);
    --muted: oklch(0.465 0.011 280);
    --faint: oklch(0.625 0.012 280);
    --accent: oklch(0.52 0.17 272);
  }
}

.est-19:has(#est-19-dark:checked) {
  --bg: #0b0c10;
  --surface: #14161c;
  --sunk: #1b1e26;
  --line: #242833;
  --line-2: #313643;
  --ink: #eef0f5;
  --muted: #9ea3b0;
  --faint: #6d7280;
  --accent: #8ea2ff;
  --on-accent: #0b1030;
  color-scheme: dark;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-19:has(#est-19-dark:checked) {
    --bg: oklch(0.165 0.012 275);
    --surface: oklch(0.205 0.014 275);
    --sunk: oklch(0.245 0.016 275);
    --line: oklch(0.295 0.017 275);
    --line-2: oklch(0.36 0.02 275);
    --ink: oklch(0.965 0.004 275);
    --muted: oklch(0.745 0.018 275);
    --faint: oklch(0.585 0.019 275);
    --accent: oklch(0.79 0.115 272);
    --on-accent: oklch(0.2 0.06 272);
  }
}

@media (prefers-color-scheme: dark) {
  .est-19:has(#est-19-sys:checked) {
    --bg: #0b0c10;
    --surface: #14161c;
    --sunk: #1b1e26;
    --line: #242833;
    --line-2: #313643;
    --ink: #eef0f5;
    --muted: #9ea3b0;
    --faint: #6d7280;
    --accent: #8ea2ff;
    --on-accent: #0b1030;
    color-scheme: dark;
  }

  @supports (color: oklch(0.7 0.1 300)) {
    .est-19:has(#est-19-sys:checked) {
      --bg: oklch(0.165 0.012 275);
      --surface: oklch(0.205 0.014 275);
      --sunk: oklch(0.245 0.016 275);
      --line: oklch(0.295 0.017 275);
      --line-2: oklch(0.36 0.02 275);
      --ink: oklch(0.965 0.004 275);
      --muted: oklch(0.745 0.018 275);
      --faint: oklch(0.585 0.019 275);
      --accent: oklch(0.79 0.115 272);
      --on-accent: oklch(0.2 0.06 272);
    }
  }
}

.est-19__shell {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-columns: min(14rem,22vw) minmax(0,1fr);
}

.est-19__side {
  display: grid;
  gap: 1.25rem;
  align-content: start;
  padding: 1.15rem .85rem;
  border-inline-end: 1px solid var(--line);
  background: var(--surface);
  transition: background .3s ease, border-color .3s ease;
}

.est-19__logo {
  padding-inline: .4rem;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.025em;
}

.est-19__nav {
  display: grid;
  gap: .1rem;
}

.est-19__nl {
  padding: .45rem .6rem;
  border-radius: 8px;
  text-decoration: none;
  font-size: .86rem;
  color: var(--muted);
  transition: color .16s, background .16s;
}

.est-19__nl:hover {
  color: var(--ink);
  background: var(--sunk);
}

.est-19__nl--on {
  color: var(--ink);
  background: var(--sunk);
  box-shadow: inset 0 0 0 1px var(--line);
}

.est-19__main {
  min-inline-size: 0;
  padding: clamp(1.25rem,3.5vw,2.5rem) clamp(1rem,3vw,2rem);
  display: grid;
  gap: 1.25rem;
  align-content: start;
}

.est-19__top {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: center;
  justify-content: space-between;
}

.est-19__h1 {
  margin: 0;
  font-size: clamp(1.35rem,3vw,1.85rem);
  font-weight: 600;
  letter-spacing: -.032em;
}

.est-19__themes {
  display: flex;
  gap: .15rem;
  padding: .2rem;
  background: var(--sunk);
  border: 1px solid var(--line);
  border-radius: 11px;
}

.est-19__tl {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  padding: .45rem .7rem;
  cursor: pointer;
  font-size: .8rem;
  font-weight: 500;
  color: var(--muted);
  border-radius: 8px;
  transition: color .16s, background .16s;
}

.est-19__tl svg {
  inline-size: .95rem;
  block-size: .95rem;
}

.est-19__tl:hover {
  color: var(--ink);
}

.est-19:has(#est-19-sys:checked) .est-19__tl[for="est-19-sys"],
.est-19:has(#est-19-light:checked) .est-19__tl[for="est-19-light"],
.est-19:has(#est-19-dark:checked) .est-19__tl[for="est-19-dark"] {
  color: var(--ink);
  background: var(--surface);
  box-shadow: 0 1px 2px rgba(0,0,0,.12);
}

#est-19-sys:focus-visible ~ .est-19__shell .est-19__tl[for="est-19-sys"],
#est-19-light:focus-visible ~ .est-19__shell .est-19__tl[for="est-19-light"],
#est-19-dark:focus-visible ~ .est-19__shell .est-19__tl[for="est-19-dark"] {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.est-19__panel {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  overflow: hidden;
  transition: background .3s ease, border-color .3s ease;
}

.est-19__ptop {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .75rem;
  padding: .85rem 1.1rem;
  border-block-end: 1px solid var(--line);
  background: var(--sunk);
}

.est-19__ptitle {
  font-size: .88rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.est-19__ptag {
  padding: .18rem .45rem;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .66rem;
  color: var(--faint);
  border: 1px solid var(--line-2);
  border-radius: 5px;
}

.est-19__empty {
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .5rem;
  padding: clamp(2rem,6vh,3.25rem) 1.5rem;
}

.est-19__plug {
  position: relative;
  inline-size: 3.6rem;
  block-size: 3.6rem;
  display: grid;
  place-items: center;
  margin-block-end: .5rem;
}

.est-19__socket {
  position: absolute;
  inset: 0;
  border-radius: 14px;
  background: color-mix(in oklab, var(--accent) 9%, var(--surface));
  box-shadow: 0 0 0 1px color-mix(in oklab, var(--accent) 20%, transparent);
}

.est-19__socket::before,
.est-19__socket::after {
  content: '';
  position: absolute;
  inset-block-start: 35%;
  inline-size: .34rem;
  block-size: .85rem;
  border-radius: 2px;
  background: color-mix(in oklab, var(--accent) 60%, transparent);
}

.est-19__socket::before {
  inset-inline-start: 32%;
}

.est-19__socket::after {
  inset-inline-end: 32%;
}

.est-19__prongs {
  position: absolute;
  inset-block-start: -.85rem;
  inline-size: 1.5rem;
  block-size: .85rem;
  display: flex;
  justify-content: space-between;
  animation: est-19-hover 5s ease-in-out infinite;
}

.est-19__prongs i {
  inline-size: .3rem;
  block-size: 100%;
  border-radius: 2px 2px 0 0;
  background: var(--accent);
}

@keyframes est-19-hover {
  0%,
    100% {
    translate: 0 0;
    opacity: .85;
  }

  50% {
    translate: 0 .3rem;
    opacity: 1;
  }
}

.est-19__eh {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: -.024em;
}

.est-19__ep {
  margin: 0;
  max-inline-size: 46ch;
  font-size: .9rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.est-19__eacts {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: center;
  margin-block-start: .9rem;
}

.est-19__pri {
  min-block-size: 2.75rem;
  padding: .65rem 1.1rem;
  font: inherit;
  font-size: .87rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--on-accent);
  background: var(--accent);
  border: 1px solid transparent;
  border-radius: 10px;
  transition: translate .16s, filter .16s;
}

.est-19__pri:hover {
  translate: 0 -1px;
  filter: brightness(1.06);
}

.est-19__ghost {
  min-block-size: 2.75rem;
  padding: .65rem 1.05rem;
  font: inherit;
  font-size: .87rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--ink);
  background: var(--sunk);
  border: 1px solid var(--line-2);
  border-radius: 10px;
  transition: background .16s;
}

.est-19__ghost:hover {
  background: var(--line);
}

.est-19__pri:focus-visible,
.est-19__ghost:focus-visible,
.est-19__nl:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.est-19__avail {
  margin: 0;
  padding: .6rem .7rem 1rem;
  list-style: none;
  display: grid;
  gap: .1rem;
  border-block-start: 1px solid var(--line);
}

.est-19__avail li {
  display: flex;
  align-items: center;
  gap: .65rem;
  padding: .6rem .65rem;
  border-radius: 9px;
  font-size: .86rem;
  transition: background .16s;
}

.est-19__avail li:hover {
  background: var(--sunk);
}

.est-19__ai {
  inline-size: 1.6rem;
  block-size: 1.6rem;
  flex: none;
  border-radius: 6px;
  background: var(--sunk);
  box-shadow: inset 0 0 0 1px var(--line-2);
  position: relative;
}

.est-19__ai[data-i="1"]::after,
.est-19__ai[data-i="2"]::after,
.est-19__ai[data-i="3"]::after {
  content: '';
  position: absolute;
  inset: .4rem;
  border-radius: 3px;
  background: color-mix(in oklab, var(--accent) 55%, transparent);
}

.est-19__ai[data-i="2"]::after {
  border-radius: 50%;
}

.est-19__ai[data-i="3"]::after {
  clip-path: polygon(50% 0, 100% 100%, 0 100%);
}

.est-19__ac {
  margin-inline-start: auto;
  font-size: .78rem;
  color: var(--faint);
}

@media (max-width: 820px) {
  .est-19__shell {
    grid-template-columns: 1fr;
  }

  .est-19__side {
    grid-template-columns: auto minmax(0,1fr);
    align-items: center;
    border-inline-end: 0;
    border-block-end: 1px solid var(--line);
  }

  .est-19__nav {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .est-19 *,
    .est-19 *::before,
    .est-19 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-19__panel,
    .est-19__pri,
    .est-19__socket {
    border-color: CanvasText;
  }
}
```
