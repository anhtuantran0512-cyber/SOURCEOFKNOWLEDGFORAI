---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-avatar-list-with-name-and-role/"
title: "CSS Avatar List with Name and Role"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "The member directory every settings page, admin panel and team page needs: avatar, name, role, presence and a row action, aligned on a real grid so long…"
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Avatar List with Name and Role
Source: https://codefronts.com/components/css-avatars/css-avatar-list-with-name-and-role/

The member directory every settings page, admin panel and team page needs: avatar, name, role, presence and a row action, aligned on a real grid so long names and short names produce identical columns. Two densities are switchable in CSS, the whole row is one hit target with a single focusable control, and every status carries text as well as colour.
## HTML
```html
<div class="av-13">
  <input class="av-13__sr" type="checkbox" id="av-13-dark">
  <label class="av-13__theme" for="av-13-dark">
    <svg class="av-13__i av-13__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-13__i av-13__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-13__vh">Dark theme</span>
  </label>

  <div class="av-13__stage">
    <section class="av-13__wrap" aria-labelledby="av-13-h">
      <header class="av-13__head">
        <div class="av-13__headtext">
          <p class="av-13__eyebrow">Settings · Members</p>
          <h2 class="av-13__h" id="av-13-h">Workspace members</h2>
          <p class="av-13__sub">Four of 17 people. Roles align because every row shares one grid.</p>
        </div>
        <fieldset class="av-13__seg">
          <legend class="av-13__vh">Row density</legend>
          <label class="av-13__segbtn"><input type="radio" name="av-13-d" id="av-13-comfy" checked><span>Comfortable</span></label>
          <label class="av-13__segbtn"><input type="radio" name="av-13-d" id="av-13-compact"><span>Compact</span></label>
        </fieldset>
      </header>

      <ul class="av-13__list">
        <li class="av-13__row">
          <span class="av-13__fig">
            <img class="av-13__img" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Alex Chen" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-13__dot av-13__dot--online" aria-hidden="true"></span>
          </span>
          <span class="av-13__who">
            <a class="av-13__name" href="#av-13-h">Alex Chen</a>
            <span class="av-13__mail">[email protected]</span>
          </span>
          <span class="av-13__role">Staff engineer<span class="av-13__team">Platform</span></span>
          <span class="av-13__state"><span class="av-13__pill av-13__pill--online">Online</span><span class="av-13__vh">, active now</span></span>
          <button class="av-13__act" type="button" aria-label="Manage Alex Chen's access">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="5" cy="12" r="1.7" fill="currentColor"/><circle cx="12" cy="12" r="1.7" fill="currentColor"/><circle cx="19" cy="12" r="1.7" fill="currentColor"/></svg>
          </button>
        </li>

        <li class="av-13__row">
          <span class="av-13__fig">
            <img class="av-13__img" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=facearea&facepad=2.5" alt="Priya Sharma" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-13__dot av-13__dot--busy" aria-hidden="true"></span>
          </span>
          <span class="av-13__who">
            <a class="av-13__name" href="#av-13-h">Priya Sharma</a>
            <span class="av-13__mail">[email protected]</span>
          </span>
          <span class="av-13__role">Engineering manager<span class="av-13__team">Platform</span></span>
          <span class="av-13__state"><span class="av-13__pill av-13__pill--busy">Busy</span><span class="av-13__vh">, in a meeting until 16:00</span></span>
          <button class="av-13__act" type="button" aria-label="Manage Priya Sharma's access">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="5" cy="12" r="1.7" fill="currentColor"/><circle cx="12" cy="12" r="1.7" fill="currentColor"/><circle cx="19" cy="12" r="1.7" fill="currentColor"/></svg>
          </button>
        </li>

        <li class="av-13__row">
          <span class="av-13__fig">
            <img class="av-13__img" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Jordan Lee" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-13__dot av-13__dot--away" aria-hidden="true"></span>
          </span>
          <span class="av-13__who">
            <a class="av-13__name" href="#av-13-h">Jordan Lee</a>
            <span class="av-13__mail">[email protected]</span>
          </span>
          <span class="av-13__role">Site reliability<span class="av-13__team">Infrastructure</span></span>
          <span class="av-13__state"><span class="av-13__pill av-13__pill--away">Away</span><span class="av-13__vh">, idle 25 minutes</span></span>
          <button class="av-13__act" type="button" aria-label="Manage Jordan Lee's access">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="5" cy="12" r="1.7" fill="currentColor"/><circle cx="12" cy="12" r="1.7" fill="currentColor"/><circle cx="19" cy="12" r="1.7" fill="currentColor"/></svg>
          </button>
        </li>

        <li class="av-13__row">
          <span class="av-13__fig">
            <img class="av-13__img" src="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=200&auto=format&fit=facearea&facepad=2.5" alt="Sam Rivera" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-13__dot av-13__dot--offline" aria-hidden="true"></span>
          </span>
          <span class="av-13__who">
            <a class="av-13__name" href="#av-13-h">Sam Rivera</a>
            <span class="av-13__mail">[email protected]</span>
          </span>
          <span class="av-13__role">Data engineer<span class="av-13__team">Analytics</span></span>
          <span class="av-13__state"><span class="av-13__pill av-13__pill--offline">Offline</span><span class="av-13__vh">, last seen 2 hours ago</span></span>
          <button class="av-13__act" type="button" aria-label="Manage Sam Rivera's access">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="5" cy="12" r="1.7" fill="currentColor"/><circle cx="12" cy="12" r="1.7" fill="currentColor"/><circle cx="19" cy="12" r="1.7" fill="currentColor"/></svg>
          </button>
        </li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-13 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
    --online: oklch(62% .17 150);
    --away: oklch(70% .15 80);
    --busy: oklch(56% .21 22);
    --offline: oklch(68% .02 265);
  }
}

.av-13 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #4f46e5;
  --glass: rgba(255,255,255,.68);
  --online: #15803d;
  --away: #b45309;
  --busy: #b91c1c;
  --offline: #8a919e;
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
  --size: 2.75rem;
  --row-pad: .85rem;
  width: 100%;
  inline-size: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}

.av-13 *,
.av-13 *::before,
.av-13 *::after {
  box-sizing: border-box;
}

.av-13__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.av-13__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-13__theme {
  position: absolute;
  inset-block-start: clamp(.85rem,2.2vw,1.5rem);
  inset-inline-end: clamp(.85rem,2.2vw,1.5rem);
  z-index: 20;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--glass);
  color: var(--ink);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.av-13__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-13__theme:hover {
  translate: 0 -1px;
}

.av-13__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-13__i--sun {
  display: none;
}

.av-13__sr:focus-visible + .av-13__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-13__wrap {
  inline-size: min(58rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1rem,2.5vw,1.5rem);
}

.av-13__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 1rem;
  padding-inline-end: 3.5rem;
}

.av-13__headtext {
  display: flex;
  flex-direction: column;
  gap: .35rem;
}

.av-13__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-13__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.3rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-13__sub {
  margin: 0;
  max-inline-size: 34rem;
  font-size: .92rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-13__seg {
  display: inline-flex;
  gap: .15rem;
  margin: 0;
  padding: .25rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--panel);
}

.av-13__segbtn {
  position: relative;
}

.av-13__segbtn input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
}

.av-13__segbtn span {
  display: grid;
  place-items: center;
  min-inline-size: 5.5rem;
  min-block-size: 2.25rem;
  padding: 0 .8rem;
  border-radius: 999px;
  font-size: .8rem;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.av-13__segbtn:hover span {
  background: var(--panel-2);
}

.av-13__segbtn input:checked + span {
  background: var(--ink);
  color: var(--panel);
}

.av-13__segbtn input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-13__list {
  list-style: none;
  margin: 0;
  padding: .4rem;
  display: grid;
  gap: .15rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-13__row {
  display: grid;
  align-items: center;
  gap: .5rem clamp(.75rem,2vw,1.25rem);
  grid-template-columns: auto minmax(0,1fr) auto;
  grid-template-areas: "fig who act" "fig role state";
  padding: var(--row-pad) .9rem;
  border-radius: 12px;
  transition: background .18s ease;
}

@media (min-width: 48rem) {
  .av-13__row {
    grid-template-columns: auto minmax(0,1.5fr) minmax(0,1.2fr) auto auto;
    grid-template-areas: "fig who role state act";
  }
}

.av-13__row:hover,
.av-13__row:focus-within {
  background: var(--panel-2);
}

.av-13__fig {
  grid-area: fig;
  position: relative;
  display: block;
  inline-size: var(--size);
  aspect-ratio: 1;
  transition: inline-size .2s ease;
}

.av-13__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
  box-shadow: 0 0 0 1px rgba(16,19,26,.06);
}

.av-13__dot {
  position: absolute;
  inset-block-end: 0;
  inset-inline-end: 0;
  inline-size: 30%;
  aspect-ratio: 1;
  border-radius: 50%;
  box-shadow: 0 0 0 2.5px var(--panel);
}

.av-13__dot--online {
  background: var(--online);
}

.av-13__dot--away {
  background: var(--away);
  box-shadow: 0 0 0 2.5px var(--panel), inset -.14rem 0 0 var(--panel);
}

.av-13__dot--busy {
  background: var(--busy) linear-gradient(var(--panel), var(--panel)) center/62% 20% no-repeat;
}

.av-13__dot--offline {
  background: var(--panel);
  box-shadow: 0 0 0 2.5px var(--panel), inset 0 0 0 2px var(--offline);
}

.av-13__who {
  grid-area: who;
  display: flex;
  flex-direction: column;
  min-inline-size: 0;
}

.av-13__name {
  font-size: .95rem;
  font-weight: 650;
  letter-spacing: -.015em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  border-radius: 4px;
}

.av-13__name:hover {
  text-decoration: underline;
  text-underline-offset: 2px;
}

.av-13__name:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-13__mail {
  font-size: .78rem;
  color: var(--muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.av-13__role {
  grid-area: role;
  display: flex;
  flex-direction: column;
  min-inline-size: 0;
  font-size: .88rem;
  font-weight: 550;
}

.av-13__team {
  font-size: .76rem;
  font-weight: 400;
  color: var(--muted);
}

.av-13__state {
  grid-area: state;
  display: flex;
  align-items: center;
}

.av-13__pill {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  padding: .2rem .55rem;
  border-radius: 999px;
  font-size: .74rem;
  font-weight: 600;
  background: var(--panel-2);
  color: var(--muted);
}

.av-13__pill::before {
  content: "";
  inline-size: .45rem;
  block-size: .45rem;
  border-radius: 50%;
  background: currentColor;
}

.av-13__pill--online {
  color: var(--online);
}

.av-13__pill--busy {
  color: var(--busy);
}

.av-13__pill--away {
  color: var(--away);
}

.av-13__pill--offline {
  color: var(--muted);
}

.av-13__act {
  grid-area: act;
  appearance: none;
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 10px;
  border: 1px solid transparent;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.av-13__act svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-13__act:hover {
  background: var(--panel);
  color: var(--ink);
  border-color: var(--line);
}

.av-13__act:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-13:has(#av-13-compact:checked) {
  --size: 2.15rem;
  --row-pad: .42rem;
}

.av-13:has(#av-13-compact:checked) .av-13__mail {
  display: none;
}

.av-13:has(#av-13-dark:checked) {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #262a33;
  --accent: #8b8cf9;
  --glass: rgba(255,255,255,.07);
  --online: #4ade80;
  --away: #fbbf24;
  --busy: #f87171;
  --offline: #6b7280;
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

.av-13:has(#av-13-dark:checked) .av-13__img {
  box-shadow: 0 0 0 1px rgba(255,255,255,.08);
}

.av-13:has(#av-13-dark:checked) .av-13__i--moon {
  display: none;
}

.av-13:has(#av-13-dark:checked) .av-13__i--sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .av-13:not(:has(#av-13-dark:checked)) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #262a33;
    --accent: #8b8cf9;
    --glass: rgba(255,255,255,.07);
    --online: #4ade80;
    --away: #fbbf24;
    --busy: #f87171;
    --offline: #6b7280;
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-13:not(:has(#av-13-dark:checked)) .av-13__img {
    box-shadow: 0 0 0 1px rgba(255,255,255,.08);
  }

  .av-13:not(:has(#av-13-dark:checked)) .av-13__i--moon {
    display: none;
  }

  .av-13:not(:has(#av-13-dark:checked)) .av-13__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-13 *,
    .av-13 *::before,
    .av-13 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-13__dot {
    box-shadow: 0 0 0 2px Canvas;
    background: CanvasText;
  }

  .av-13__segbtn input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .av-13__list,
    .av-13__seg,
    .av-13__theme {
    border-color: CanvasText;
  }
}
```
