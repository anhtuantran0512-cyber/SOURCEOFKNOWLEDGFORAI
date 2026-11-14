---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/css-speech-bubble-with-avatar/"
title: "CSS Speech Bubble With Avatar"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "Three avatar layouts for the same thread, switched with a pure-CSS radio group: beside (the classic 40 px circle next to the bubble), overlap (avatar notched…"
has_js: "false"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Speech Bubble With Avatar
Source: https://codefronts.com/snippets/css-chat-bubbles/css-speech-bubble-with-avatar/

Three avatar layouts for the same thread, switched with a pure-CSS radio group: beside (the classic 40 px circle next to the bubble), overlap (avatar notched into the bubble corner), and stacked (avatar and name above the message, the layout Slack-style products use). Repeated avatars inside a run are hidden but keep their space, presence is a ring rather than a dot on top of the face, and timestamps reveal on hover and focus.
## HTML
```html
<div class="cb-06">
  <input class="cb-06__sr" type="checkbox" id="cb-06-dark">
  <label class="cb-06__theme" for="cb-06-dark">
    <svg class="cb-06__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="cb-06__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="cb-06__sr-text">Dark theme</span>
  </label>

  <input class="cb-06__sr" type="radio" name="cb-06-layout" id="cb-06-beside" checked>
  <input class="cb-06__sr" type="radio" name="cb-06-layout" id="cb-06-overlap">
  <input class="cb-06__sr" type="radio" name="cb-06-layout" id="cb-06-stacked">

  <div class="cb-06__stage">
    <ol class="cb-06__thread" aria-label="Conversation with the design guild">
      <li class="cb-06__turn cb-06__turn--in">
        <img class="cb-06__avatar" data-online src="https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=facearea&facepad=2.8&w=160&h=160&q=70" width="44" height="44" alt="Elise Marchetti" loading="lazy" decoding="async">
        <div class="cb-06__block">
          <p class="cb-06__name">Elise Marchetti <span class="cb-06__role">Design lead</span></p>
          <p class="cb-06__msg">The avatar and the bubble are siblings in a flex row — that is the whole layout.</p>
        </div>
        <time class="cb-06__time" datetime="2027-03-04T10:12">10:12</time>
      </li>
      <li class="cb-06__turn cb-06__turn--in">
        <img class="cb-06__avatar" data-online src="https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=facearea&facepad=2.8&w=160&h=160&q=70" width="44" height="44" alt="Elise Marchetti" loading="lazy" decoding="async">
        <div class="cb-06__block">
          <p class="cb-06__name">Elise Marchetti <span class="cb-06__role">Design lead</span></p>
          <p class="cb-06__msg">In a run, the repeated avatar is hidden but still occupies its box.</p>
        </div>
        <time class="cb-06__time" datetime="2027-03-04T10:12">10:12</time>
      </li>
      <li class="cb-06__turn cb-06__turn--out">
        <img class="cb-06__avatar" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=facearea&facepad=2.8&w=160&h=160&q=70" width="44" height="44" alt="Jonah Reyes" loading="lazy" decoding="async">
        <div class="cb-06__block">
          <p class="cb-06__name">Jonah Reyes</p>
          <p class="cb-06__msg">So the indent never collapses. Neat.</p>
        </div>
        <time class="cb-06__time" datetime="2027-03-04T10:14">10:14</time>
      </li>
      <li class="cb-06__turn cb-06__turn--in">
        <img class="cb-06__avatar" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=facearea&facepad=2.8&w=160&h=160&q=70" width="44" height="44" alt="Sana Iqbal" loading="lazy" decoding="async">
        <div class="cb-06__block">
          <p class="cb-06__name">Sana Iqbal <span class="cb-06__role">Research</span></p>
          <p class="cb-06__msg">Pulled six sessions into the board — worth a read before Thursday.</p>
        </div>
        <time class="cb-06__time" datetime="2027-03-04T10:19">10:19</time>
      </li>
      <li class="cb-06__seen">
        <span class="cb-06__stack" aria-hidden="true">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=facearea&facepad=2.8&w=80&h=80&q=70" width="24" height="24" alt="" loading="lazy" decoding="async">
          <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=facearea&facepad=2.8&w=80&h=80&q=70" width="24" height="24" alt="" loading="lazy" decoding="async">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=facearea&facepad=2.8&w=80&h=80&q=70" width="24" height="24" alt="" loading="lazy" decoding="async">
          <b class="cb-06__more">+4</b>
        </span>
        <span class="cb-06__seen-text">Seen by 7</span>
      </li>
    </ol>

    <div class="cb-06__switch" role="radiogroup" aria-label="Avatar layout">
      <label class="cb-06__chip" for="cb-06-beside">Beside</label>
      <label class="cb-06__chip" for="cb-06-overlap">Overlap</label>
      <label class="cb-06__chip" for="cb-06-stacked">Stacked</label>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap');

.cb-06 {
  --bg: #f4f4f2;
  --surface: #ffffff;
  --ink: #12140f;
  --muted: #61665c;
  --line: #e4e5e0;
  --in: #ffffff;
  --in-ink: #12140f;
  --out: #1d3b2a;
  --out-ink: #f2f5ef;
  --live: #37b26c;
  --ring: #1d3b2a;
  --shadow: rgba(18,20,15,.15);
  --av: 2.75rem;
  --radius: 1.25rem;
  --sans: "Manrope",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(100% 60% at 20% 0%, color-mix(in oklab,var(--out) 10%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-06,
.cb-06 *,
.cb-06 *::before,
.cb-06 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .cb-06 {
    --bg: oklch(96.5% .006 110);
    --surface: oklch(100% 0 0);
    --ink: oklch(17% .02 120);
    --muted: oklch(50% .015 120);
    --line: oklch(91% .008 110);
    --out: oklch(33% .06 155);
    --live: oklch(70% .16 155);
  }
}

.cb-06__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  opacity: 0;
}

.cb-06__sr-text {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cb-06__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,3vw,1.6rem);
  inset-inline-end: clamp(.9rem,3vw,1.6rem);
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  transition: transform .25s cubic-bezier(.16,1,.3,1);
}

.cb-06__theme:hover {
  transform: translateY(-2px);
}

.cb-06__theme svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-06__sun {
  display: none;
}

.cb-06__sr:focus-visible + .cb-06__theme {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.cb-06__stage {
  inline-size: min(100%,40rem);
  display: grid;
  gap: clamp(1.1rem,3vw,1.75rem);
}

.cb-06__thread {
  list-style: none;
  margin: 0;
  padding: clamp(1rem,3vw,1.75rem);
  display: grid;
  gap: .55rem;
  border-radius: 1.75rem;
  background: color-mix(in oklab,var(--surface) 60%,transparent);
  border: 1px solid var(--line);
  box-shadow: 0 30px 70px -55px var(--shadow);
}
/* ── row ── */

.cb-06__turn {
  display: flex;
  align-items: flex-end;
  gap: .7rem;
}

.cb-06__turn--out {
  flex-direction: row-reverse;
}

.cb-06__avatar {
  flex: 0 0 auto;
  inline-size: var(--av);
  block-size: var(--av);
  aspect-ratio: 1;
  border-radius: 50%;
  object-fit: cover;
  object-position: 50% 30%;
  background: var(--line);
}

.cb-06__avatar[data-online] {
  box-shadow: 0 0 0 2px var(--surface), 0 0 0 4px var(--live);
}
/* repeated avatar in a run: hidden, but the box stays */

.cb-06__turn--in:has(+ .cb-06__turn--in) .cb-06__avatar,
.cb-06__turn--out:has(+ .cb-06__turn--out) .cb-06__avatar {
  visibility: hidden;
}

.cb-06__block {
  min-inline-size: 0;
  display: grid;
  gap: .2rem;
}

.cb-06__name {
  display: none;
}

.cb-06__msg {
  margin: 0;
  max-inline-size: min(26rem,72vw);
  padding: .7rem 1.05rem;
  font-size: clamp(.95rem,.3vw + .9rem,1.02rem);
  line-height: 1.5;
  letter-spacing: -.008em;
  text-wrap: pretty;
  border-radius: var(--radius);
  background: var(--in);
  color: var(--in-ink);
  box-shadow: 0 1px 2px color-mix(in oklab,var(--shadow) 60%,transparent);
  animation: cb-06-in .5s cubic-bezier(.16,1,.3,1) backwards;
}

.cb-06__turn--in .cb-06__msg {
  border-end-start-radius: .35rem;
}

.cb-06__turn--out .cb-06__msg {
  background: var(--out);
  color: var(--out-ink);
  border-end-end-radius: .35rem;
}

.cb-06__turn--in:has(+ .cb-06__turn--in) .cb-06__msg {
  border-end-start-radius: var(--radius);
}

@keyframes cb-06-in {
  from {
    opacity: 0;
    translate: 0 8px;
    scale: .97;
  }

  to {
    opacity: 1;
    translate: 0;
    scale: 1;
  }
}

.cb-06__time {
  flex: 0 0 auto;
  padding-block-end: .35rem;
  font-size: .68rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  color: var(--muted);
  opacity: 0;
  translate: 0 4px;
  transition: opacity .25s, translate .25s cubic-bezier(.16,1,.3,1);
}

.cb-06__turn:hover .cb-06__time,
.cb-06__turn:focus-within .cb-06__time {
  opacity: 1;
  translate: 0 0;
}
/* ── seen-by stack ── */

.cb-06__seen {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: .5rem;
  margin-block-start: .35rem;
}

.cb-06__stack {
  display: flex;
  align-items: center;
}

.cb-06__stack img {
  inline-size: 1.5rem;
  block-size: 1.5rem;
  border-radius: 50%;
  object-fit: cover;
  outline: 2px solid var(--surface);
  background: var(--line);
}

.cb-06__stack img + img,
.cb-06__more {
  margin-inline-start: -.45rem;
}

.cb-06__more {
  display: grid;
  place-items: center;
  inline-size: 1.5rem;
  block-size: 1.5rem;
  border-radius: 50%;
  background: var(--out);
  color: var(--out-ink);
  font-size: .6rem;
  font-weight: 700;
  outline: 2px solid var(--surface);
}

.cb-06__seen-text {
  font-size: .7rem;
  font-weight: 600;
  color: var(--muted);
}
/* ═══ OVERLAP ═══ */

.cb-06:has(#cb-06-overlap:checked) .cb-06__avatar {
  margin-inline-end: -.9rem;
  z-index: 1;
  outline: 3px solid var(--surface);
  align-self: flex-end;
}

.cb-06:has(#cb-06-overlap:checked) .cb-06__turn {
  gap: 0;
}

.cb-06:has(#cb-06-overlap:checked) .cb-06__turn--out .cb-06__avatar {
  margin-inline: -.9rem 0;
}

.cb-06:has(#cb-06-overlap:checked) .cb-06__msg {
  padding-inline-start: 1.5rem;
}

.cb-06:has(#cb-06-overlap:checked) .cb-06__turn--out .cb-06__msg {
  padding-inline: 1.05rem 1.5rem;
}

.cb-06:has(#cb-06-overlap:checked) .cb-06__turn--in .cb-06__msg {
  border-end-start-radius: var(--radius);
}

.cb-06:has(#cb-06-overlap:checked) .cb-06__turn--out .cb-06__msg {
  border-end-end-radius: var(--radius);
}
/* ═══ STACKED ═══ */

.cb-06:has(#cb-06-stacked:checked) .cb-06__thread {
  gap: 1.1rem;
}

.cb-06:has(#cb-06-stacked:checked) .cb-06__turn {
  display: grid;
  grid-template-columns: 3rem var(--av) minmax(0,1fr);
  align-items: start;
  gap: .15rem .7rem;
}

.cb-06:has(#cb-06-stacked:checked) .cb-06__time {
  grid-column: 1;
  grid-row: 1;
  justify-self: end;
  padding-block: .15rem 0;
}

.cb-06:has(#cb-06-stacked:checked) .cb-06__avatar {
  grid-column: 2;
  grid-row: 1 / span 2;
  visibility: visible !important;
  align-self: start;
}

.cb-06:has(#cb-06-stacked:checked) .cb-06__block {
  grid-column: 3;
  grid-row: 1 / span 2;
  justify-items: start;
  text-align: start;
}

.cb-06:has(#cb-06-stacked:checked) .cb-06__name {
  display: flex;
  align-items: baseline;
  gap: .45rem;
  margin: 0;
  font-size: .82rem;
  font-weight: 700;
  letter-spacing: -.01em;
}

.cb-06:has(#cb-06-stacked:checked) .cb-06__role {
  font-size: .68rem;
  font-weight: 600;
  color: var(--muted);
  letter-spacing: .01em;
}

.cb-06:has(#cb-06-stacked:checked) .cb-06__msg {
  background: none !important;
  color: var(--ink) !important;
  padding: 0;
  box-shadow: none;
  max-inline-size: 38rem;
  border-radius: 0;
}

.cb-06:has(#cb-06-stacked:checked) .cb-06__time {
  opacity: 1;
  translate: 0;
  grid-row: 1;
}

.cb-06:has(#cb-06-stacked:checked) .cb-06__turn--in:has(+ .cb-06__turn--in) .cb-06__avatar {
  visibility: hidden;
}

.cb-06:has(#cb-06-stacked:checked) .cb-06__turn--in:has(+ .cb-06__turn--in) + .cb-06__turn--in .cb-06__name {
  display: none;
}
/* ── switch ── */

.cb-06__switch {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  justify-content: center;
  padding: .4rem;
  border-radius: 1rem;
  border: 1px solid var(--line);
  background: color-mix(in oklab,var(--surface) 70%,transparent);
}

.cb-06__chip {
  min-block-size: 44px;
  display: grid;
  place-items: center;
  padding: .5rem 1.1rem;
  cursor: pointer;
  border-radius: .75rem;
  color: var(--muted);
  font-size: .86rem;
  font-weight: 600;
  letter-spacing: -.01em;
  transition: background .22s, color .22s, transform .22s cubic-bezier(.16,1,.3,1);
}

.cb-06__chip:hover {
  color: var(--ink);
  transform: translateY(-1px);
}

#cb-06-beside:checked ~ .cb-06__stage .cb-06__chip[for="cb-06-beside"],
#cb-06-overlap:checked ~ .cb-06__stage .cb-06__chip[for="cb-06-overlap"],
#cb-06-stacked:checked ~ .cb-06__stage .cb-06__chip[for="cb-06-stacked"] {
  background: var(--out);
  color: var(--out-ink);
}

#cb-06-beside:focus-visible ~ .cb-06__stage .cb-06__chip[for="cb-06-beside"],
#cb-06-overlap:focus-visible ~ .cb-06__stage .cb-06__chip[for="cb-06-overlap"],
#cb-06-stacked:focus-visible ~ .cb-06__stage .cb-06__chip[for="cb-06-stacked"] {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}
/* ── dark ── */

.cb-06:has(#cb-06-dark:checked) {
  --bg: #0c0e0c;
  --surface: #161a17;
  --ink: #eef2ec;
  --muted: #939a91;
  --line: #242a25;
  --in: #1c211d;
  --in-ink: #eef2ec;
  --out: #5fd39a;
  --out-ink: #0b1410;
  --shadow: rgba(0,0,0,.7);
}

.cb-06:has(#cb-06-dark:checked) .cb-06__moon {
  display: none;
}

.cb-06:has(#cb-06-dark:checked) .cb-06__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .cb-06:not(:has(#cb-06-dark:checked)) {
    --bg: #0c0e0c;
    --surface: #161a17;
    --ink: #eef2ec;
    --muted: #939a91;
    --line: #242a25;
    --in: #1c211d;
    --in-ink: #eef2ec;
    --out: #5fd39a;
    --out-ink: #0b1410;
    --shadow: rgba(0,0,0,.7);
  }

  .cb-06:not(:has(#cb-06-dark:checked)) .cb-06__moon {
    display: none;
  }

  .cb-06:not(:has(#cb-06-dark:checked)) .cb-06__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-06 *,
    .cb-06 *::before,
    .cb-06 *::after {
    animation: none !important;
    transition: none !important;
  }

  .cb-06__time {
    opacity: 1;
    translate: 0;
  }
}

@media (forced-colors: active) {
  .cb-06__msg {
    border: 1px solid CanvasText;
  }

  .cb-06__avatar[data-online] {
    outline: 2px solid Highlight;
  }
}
```
