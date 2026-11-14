---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-avatar-with-online-status-dot/"
title: "CSS Avatar with Online Status Dot"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "Presence done to spec: a dot at the bottom-right with a ring of surface colour so it reads on any photo, in four states — online, away, busy, offline — where…"
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Avatar with Online Status Dot
Source: https://codefronts.com/components/css-avatars/css-avatar-with-online-status-dot/

Presence done to spec: a dot at the bottom-right with a ring of surface colour so it reads on any photo, in four states — online, away, busy, offline — where each state is distinguished by an inline-SVG glyph and visually-hidden text, never by hue alone. A real radio group sets your own presence and every dependent surface updates through :has(), with zero JavaScript.
## HTML
```html
<div class="av-06">
  <input class="av-06__sr" type="checkbox" id="av-06-dark">
  <label class="av-06__theme" for="av-06-dark">
    <svg class="av-06__i av-06__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-06__i av-06__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-06__vh">Dark theme</span>
  </label>

  <div class="av-06__stage">
    <section class="av-06__wrap" aria-labelledby="av-06-h">
      <header class="av-06__head">
        <p class="av-06__eyebrow">Workspace · Presence</p>
        <h2 class="av-06__h" id="av-06-h">Status dots</h2>
        <p class="av-06__sub">Shape and text carry the meaning; colour only reinforces it.</p>
      </header>

      <div class="av-06__panel">
        <div class="av-06__me">
          <span class="av-06__fig">
            <img class="av-06__img" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?w=200&auto=format&fit=facearea&facepad=2.5" alt="Elena Vasquez" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-06__dot" aria-hidden="true"><span class="av-06__glyph"></span></span>
          </span>
          <div class="av-06__meinfo">
            <p class="av-06__name">Elena Vasquez</p>
            <p class="av-06__handle">@elena · Product design</p>
            <p class="av-06__say" aria-live="polite">
              <span class="av-06__s av-06__s--online">Online — active now</span>
              <span class="av-06__s av-06__s--away">Away — back in 20 minutes</span>
              <span class="av-06__s av-06__s--busy">Busy — notifications paused</span>
              <span class="av-06__s av-06__s--offline">Offline — appear invisible</span>
            </p>
          </div>
        </div>

        <fieldset class="av-06__picker">
          <legend class="av-06__legend">Set your presence</legend>
          <label class="av-06__opt"><input type="radio" name="av-06-p" id="av-06-online" checked><span class="av-06__optbox"><span class="av-06__mini av-06__mini--online" aria-hidden="true"></span>Online</span></label>
          <label class="av-06__opt"><input type="radio" name="av-06-p" id="av-06-away"><span class="av-06__optbox"><span class="av-06__mini av-06__mini--away" aria-hidden="true"></span>Away</span></label>
          <label class="av-06__opt"><input type="radio" name="av-06-p" id="av-06-busy"><span class="av-06__optbox"><span class="av-06__mini av-06__mini--busy" aria-hidden="true"></span>Busy</span></label>
          <label class="av-06__opt"><input type="radio" name="av-06-p" id="av-06-offline"><span class="av-06__optbox"><span class="av-06__mini av-06__mini--offline" aria-hidden="true"></span>Offline</span></label>
        </fieldset>
      </div>

      <ul class="av-06__team">
        <li class="av-06__member">
          <span class="av-06__fig av-06__fig--sm">
            <img class="av-06__img" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Jordan Lee" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-06__dot av-06__dot--online" aria-hidden="true"><span class="av-06__glyph"></span></span>
          </span>
          <span class="av-06__who"><span class="av-06__mname">Jordan Lee</span><span class="av-06__mstate">Online<span class="av-06__vh"> — active now</span></span></span>
        </li>
        <li class="av-06__member">
          <span class="av-06__fig av-06__fig--sm">
            <img class="av-06__img" src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=200&auto=format&fit=facearea&facepad=2.5" alt="Hannah Wright" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-06__dot av-06__dot--away" aria-hidden="true"><span class="av-06__glyph"></span></span>
          </span>
          <span class="av-06__who"><span class="av-06__mname">Hannah Wright</span><span class="av-06__mstate">Away<span class="av-06__vh"> — idle 12 minutes</span></span></span>
        </li>
        <li class="av-06__member">
          <span class="av-06__fig av-06__fig--sm">
            <img class="av-06__img" src="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=200&auto=format&fit=facearea&facepad=2.5" alt="Sam Rivera" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-06__dot av-06__dot--busy" aria-hidden="true"><span class="av-06__glyph"></span></span>
          </span>
          <span class="av-06__who"><span class="av-06__mname">Sam Rivera</span><span class="av-06__mstate">Busy<span class="av-06__vh"> — in a meeting until 4pm</span></span></span>
        </li>
        <li class="av-06__member">
          <span class="av-06__fig av-06__fig--sm">
            <img class="av-06__img" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=200&auto=format&fit=facearea&facepad=2.5" alt="Tom Bergström" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-06__dot av-06__dot--offline" aria-hidden="true"><span class="av-06__glyph"></span></span>
          </span>
          <span class="av-06__who"><span class="av-06__mname">Tom Bergström</span><span class="av-06__mstate">Offline<span class="av-06__vh"> — last seen 2 hours ago</span></span></span>
        </li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-06 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
    --online: oklch(66% .18 150);
    --away: oklch(75% .16 80);
    --busy: oklch(58% .21 22);
    --offline: oklch(70% .02 265);
  }
}

.av-06 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #4f46e5;
  --glass: rgba(255,255,255,.68);
  --online: #16a34a;
  --away: #f59e0b;
  --busy: #dc2626;
  --offline: #9aa1ad;
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
  --c: var(--online);
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

.av-06 *,
.av-06 *::before,
.av-06 *::after {
  box-sizing: border-box;
}

.av-06__vh {
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

.av-06__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-06__theme {
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

.av-06__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-06__theme:hover {
  translate: 0 -1px;
}

.av-06__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-06__i--sun {
  display: none;
}

.av-06__sr:focus-visible + .av-06__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-06__wrap {
  inline-size: min(58rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.25rem,3vw,2rem);
}

.av-06__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-06__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-06__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-06__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-06__panel {
  display: grid;
  gap: clamp(1.25rem,3vw,2rem);
  align-items: center;
  grid-template-columns: minmax(0,1fr);
  padding: clamp(1.35rem,3.5vw,2rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

@media (min-width: 46rem) {
  .av-06__panel {
    grid-template-columns: minmax(0,1fr) auto;
  }
}

.av-06__me {
  display: flex;
  align-items: center;
  gap: clamp(.9rem,2.5vw,1.35rem);
}

.av-06__fig {
  --size: clamp(4rem,11vw,5.5rem);
  position: relative;
  display: block;
  inline-size: var(--size);
  aspect-ratio: 1;
  flex: none;
}

.av-06__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
  box-shadow: 0 0 0 1px rgba(16,19,26,.06);
}

.av-06__dot {
  position: absolute;
  inset-block-end: 4%;
  inset-inline-end: 4%;
  display: grid;
  place-items: center;
  inline-size: 28%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--c);
  box-shadow: 0 0 0 .17em var(--panel);
  transition: background .2s ease;
}

.av-06__glyph {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
}

.av-06__fig--sm {
  --size: 2.75rem;
}

.av-06__fig--sm .av-06__dot {
  box-shadow: 0 0 0 3px var(--panel);
}

.av-06__dot--online {
  --c: var(--online);
}

.av-06__dot--away {
  --c: var(--away);
}

.av-06__dot--busy {
  --c: var(--busy);
}

.av-06__dot--offline {
  --c: var(--offline);
}

.av-06__dot--away .av-06__glyph {
  background: radial-gradient(circle at 118% 50%, var(--panel) 46%, transparent 47%);
}

.av-06__dot--busy .av-06__glyph {
  background: linear-gradient(var(--panel), var(--panel)) center/64% 22% no-repeat;
}

.av-06__dot--offline .av-06__glyph {
  background: var(--panel);
  scale: .42;
}

.av-06__meinfo {
  display: flex;
  flex-direction: column;
  gap: .2rem;
  min-inline-size: 0;
}

.av-06__name {
  margin: 0;
  font-size: clamp(1.05rem,2.5vw,1.3rem);
  font-weight: 650;
  letter-spacing: -.02em;
}

.av-06__handle {
  margin: 0;
  font-size: .85rem;
  color: var(--muted);
}

.av-06__say {
  margin: .3rem 0 0;
  font-size: .85rem;
  font-weight: 600;
}

.av-06__s {
  display: none;
}

.av-06__s--online {
  color: var(--online);
}

.av-06__s--away {
  color: var(--away);
}

.av-06__s--busy {
  color: var(--busy);
}

.av-06__s--offline {
  color: var(--muted);
}

.av-06__picker {
  display: grid;
  gap: .3rem;
  margin: 0;
  padding: .35rem;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--panel-2);
}

.av-06__legend {
  padding: .15rem .5rem;
  font-size: .68rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-06__opt {
  position: relative;
  display: block;
}

.av-06__opt input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
}

.av-06__optbox {
  display: flex;
  align-items: center;
  gap: .6rem;
  min-block-size: 2.75rem;
  padding: 0 1rem 0 .75rem;
  border-radius: 10px;
  font-size: .88rem;
  font-weight: 550;
  cursor: pointer;
  color: var(--muted);
  transition: background .18s ease, color .18s ease;
}

.av-06__opt:hover .av-06__optbox {
  background: var(--panel);
}

.av-06__opt input:checked + .av-06__optbox {
  background: var(--panel);
  color: var(--ink);
  box-shadow: 0 1px 2px rgba(16,19,26,.08);
}

.av-06__opt input:focus-visible + .av-06__optbox {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-06__mini {
  inline-size: .7rem;
  block-size: .7rem;
  border-radius: 50%;
  flex: none;
}

.av-06__mini--online {
  background: var(--online);
}

.av-06__mini--away {
  background: var(--away);
  box-shadow: inset -.2rem 0 0 var(--panel-2);
}

.av-06__mini--busy {
  background: var(--busy) linear-gradient(var(--panel-2), var(--panel-2)) center/60% 20% no-repeat;
}

.av-06__mini--offline {
  background: var(--panel-2);
  box-shadow: inset 0 0 0 2px var(--offline);
}

.av-06__team {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .5rem;
  grid-template-columns: repeat(auto-fit,minmax(13rem,1fr));
}

.av-06__member {
  display: flex;
  align-items: center;
  gap: .8rem;
  padding: .6rem .8rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
}

.av-06__who {
  display: flex;
  flex-direction: column;
  min-inline-size: 0;
}

.av-06__mname {
  font-size: .9rem;
  font-weight: 600;
  letter-spacing: -.01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.av-06__mstate {
  font-size: .78rem;
  color: var(--muted);
}

.av-06:has(#av-06-online:checked) .av-06__s--online {
  display: block;
}

.av-06:has(#av-06-away:checked) .av-06__s--away {
  display: block;
}

.av-06:has(#av-06-busy:checked) .av-06__s--busy {
  display: block;
}

.av-06:has(#av-06-offline:checked) .av-06__s--offline {
  display: block;
}

.av-06:has(#av-06-away:checked) .av-06__me .av-06__dot {
  --c: var(--away);
}

.av-06:has(#av-06-away:checked) .av-06__me .av-06__glyph {
  background: radial-gradient(circle at 118% 50%, var(--panel) 46%, transparent 47%);
}

.av-06:has(#av-06-busy:checked) .av-06__me .av-06__dot {
  --c: var(--busy);
}

.av-06:has(#av-06-busy:checked) .av-06__me .av-06__glyph {
  background: linear-gradient(var(--panel), var(--panel)) center/64% 22% no-repeat;
}

.av-06:has(#av-06-offline:checked) .av-06__me .av-06__dot {
  --c: var(--offline);
}

.av-06:has(#av-06-offline:checked) .av-06__me .av-06__glyph {
  background: var(--panel);
  scale: .42;
}

.av-06:has(#av-06-dark:checked) {
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

.av-06:has(#av-06-dark:checked) .av-06__img {
  box-shadow: 0 0 0 1px rgba(255,255,255,.08);
}

.av-06:has(#av-06-dark:checked) .av-06__i--moon {
  display: none;
}

.av-06:has(#av-06-dark:checked) .av-06__i--sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .av-06:not(:has(#av-06-dark:checked)) {
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

  .av-06:not(:has(#av-06-dark:checked)) .av-06__img {
    box-shadow: 0 0 0 1px rgba(255,255,255,.08);
  }

  .av-06:not(:has(#av-06-dark:checked)) .av-06__i--moon {
    display: none;
  }

  .av-06:not(:has(#av-06-dark:checked)) .av-06__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-06 *,
    .av-06 *::before,
    .av-06 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-06__dot {
    box-shadow: 0 0 0 2px Canvas;
    background: CanvasText;
  }

  .av-06__opt input:checked + .av-06__optbox {
    background: Highlight;
    color: HighlightText;
  }

  .av-06__panel,
    .av-06__member,
    .av-06__picker,
    .av-06__theme {
    border-color: CanvasText;
  }
}
```
