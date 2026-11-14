---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-avatar-with-verified-checkmark-badge/"
title: "CSS Avatar with Verified Checkmark Badge"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "The platform verification tick, engineered rather than pasted: an inline-SVG check on a coloured disc, notched into the avatar edge with a ring of surface…"
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Avatar with Verified Checkmark Badge
Source: https://codefronts.com/components/css-avatars/css-avatar-with-verified-checkmark-badge/

The platform verification tick, engineered rather than pasted: an inline-SVG check on a coloured disc, notched into the avatar edge with a ring of surface colour so it reads as cut into the photo. Three tiers — verified, official, staff — each with its own glyph and its own visible text, because a blue disc alone means nothing to a screen reader or to anyone who cannot separate blue from grey.
## HTML
```html
<div class="av-08">
  <input class="av-08__sr" type="checkbox" id="av-08-dark">
  <label class="av-08__theme" for="av-08-dark">
    <svg class="av-08__i av-08__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-08__i av-08__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-08__vh">Dark theme</span>
  </label>

  <div class="av-08__stage">
    <section class="av-08__wrap" aria-labelledby="av-08-h">
      <header class="av-08__head">
        <p class="av-08__eyebrow">Trust · Verification</p>
        <h2 class="av-08__h" id="av-08-h">Verified badges</h2>
        <p class="av-08__sub">Each tier has its own glyph and its own words — never three colours of one tick.</p>
      </header>

      <ul class="av-08__row">
        <li class="av-08__chip">
          <a class="av-08__link" href="#av-08-h" aria-label="Priya Sharma, verified account">
            <span class="av-08__fig">
              <img class="av-08__img" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=facearea&facepad=2.5" alt="" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-08__badge av-08__badge--verified" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 12.5l3.6 3.5L18 8" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </span>
            </span>
            <span class="av-08__who"><span class="av-08__name">Priya Sharma</span><span class="av-08__role">Verified</span></span>
          </a>
          <span class="av-08__tip" role="note">Identity confirmed by document check</span>
        </li>
        <li class="av-08__chip">
          <a class="av-08__link" href="#av-08-h" aria-label="Northwind Labs, official organisation account">
            <span class="av-08__fig">
              <img class="av-08__img" src="https://images.unsplash.com/photo-1560250097-0b93528c311a?w=200&auto=format&fit=facearea&facepad=2.5" alt="" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-08__badge av-08__badge--official" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 3.2l6.8 2.6v5.6c0 4.2-2.9 6.8-6.8 8.4-3.9-1.6-6.8-4.2-6.8-8.4V5.8z" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
              </span>
            </span>
            <span class="av-08__who"><span class="av-08__name">Victor Cho</span><span class="av-08__role">Official</span></span>
          </a>
          <span class="av-08__tip" role="note">Organisation account, managed by Northwind Labs</span>
        </li>
        <li class="av-08__chip">
          <a class="av-08__link" href="#av-08-h" aria-label="Grace Tan, staff account">
            <span class="av-08__fig">
              <img class="av-08__img" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200&auto=format&fit=facearea&facepad=2.5" alt="" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-08__badge av-08__badge--staff" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 4l2.3 4.9 5.2.7-3.8 3.7.9 5.3L12 16.1 7.4 18.6l.9-5.3L4.5 9.6l5.2-.7z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>
              </span>
            </span>
            <span class="av-08__who"><span class="av-08__name">Grace Tan</span><span class="av-08__role">Staff</span></span>
          </a>
          <span class="av-08__tip" role="note">Works at Codefronts — support and moderation</span>
        </li>
      </ul>

      <div class="av-08__inline">
        <p class="av-08__inlinehead">In a timeline</p>
        <p class="av-08__post">
          <span class="av-08__fig av-08__fig--xs">
            <img class="av-08__img" src="https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=200&auto=format&fit=facearea&facepad=2.5" alt="Mia Castellano" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-08__badge av-08__badge--verified" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 12.5l3.6 3.5L18 8" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
          </span>
          <span class="av-08__postbody"><strong>Mia Castellano</strong><span class="av-08__vh">, verified account</span> shipped the new presence service · 14:02</span>
        </p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-08 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
    --verified: oklch(60% .18 250);
    --official: oklch(58% .16 155);
    --staff: oklch(64% .19 300);
  }
}

.av-08 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #4f46e5;
  --glass: rgba(255,255,255,.68);
  --verified: #1d80e2;
  --official: #0f9d58;
  --staff: #8b5cf6;
  --tier: var(--verified);
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
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

.av-08 *,
.av-08 *::before,
.av-08 *::after {
  box-sizing: border-box;
}

.av-08__vh {
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

.av-08__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-08__theme {
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

.av-08__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-08__theme:hover {
  translate: 0 -1px;
}

.av-08__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-08__i--sun {
  display: none;
}

.av-08__sr:focus-visible + .av-08__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-08__wrap {
  inline-size: min(58rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.25rem,3vw,2rem);
}

.av-08__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-08__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-08__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-08__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-08__row {
  list-style: none;
  margin: 0;
  padding: clamp(1.5rem,4vw,2.5rem) clamp(1rem,3vw,2rem);
  display: grid;
  gap: clamp(1.25rem,3vw,2rem);
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-08__chip {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .55rem;
}

.av-08__link {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .75rem;
  text-decoration: none;
  color: inherit;
  padding: .35rem .5rem;
  border-radius: 14px;
}

.av-08__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-08__fig {
  --size: clamp(4.5rem,12vw,6.5rem);
  position: relative;
  display: block;
  inline-size: var(--size);
  aspect-ratio: 1;
  transition: translate .24s cubic-bezier(.2,.7,.3,1);
}

.av-08__link:hover .av-08__fig {
  translate: 0 -4px;
}

.av-08__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
  box-shadow: 0 0 0 1px rgba(16,19,26,.06);
}

.av-08__badge {
  position: absolute;
  inset-block-end: 0%;
  inset-inline-end: 0%;
  z-index: 2;
  display: grid;
  place-items: center;
  inline-size: 34%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--tier);
  color: #fff;
  box-shadow: 0 0 0 .15em var(--panel);
}

.av-08__badge svg {
  inline-size: 64%;
  block-size: 64%;
}

.av-08__badge--verified {
  --tier: var(--verified);
}

.av-08__badge--official {
  --tier: var(--official);
}

.av-08__badge--staff {
  --tier: var(--staff);
}

.av-08__who {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .1rem;
  text-align: center;
}

.av-08__name {
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.av-08__role {
  font-size: .78rem;
  color: var(--muted);
}

.av-08__tip {
  position: absolute;
  inset-block-start: calc(100% + .35rem);
  inset-inline: 0;
  z-index: 5;
  padding: .5rem .65rem;
  border-radius: 10px;
  background: var(--ink);
  color: var(--page);
  font-size: .74rem;
  line-height: 1.4;
  text-align: center;
  text-wrap: balance;
  opacity: 0;
  translate: 0 -.35rem;
  pointer-events: none;
  transition: opacity .2s ease, translate .2s ease;
}

.av-08__chip:hover .av-08__tip,
.av-08__chip:focus-within .av-08__tip {
  opacity: 1;
  translate: 0 0;
}

.av-08__inline {
  display: flex;
  flex-direction: column;
  gap: .6rem;
  padding: 1rem 1.15rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
}

.av-08__inlinehead {
  margin: 0;
  font-size: .68rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-08__post {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .7rem;
  font-size: .9rem;
  line-height: 1.45;
}

.av-08__fig--xs {
  --size: 2.5rem;
  flex: none;
}

.av-08__fig--xs .av-08__badge {
  inline-size: 42%;
  box-shadow: 0 0 0 2px var(--panel);
}

.av-08__postbody {
  color: var(--muted);
}

.av-08__postbody strong {
  color: var(--ink);
  font-weight: 650;
}

.av-08:has(#av-08-dark:checked) {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #262a33;
  --accent: #8b8cf9;
  --glass: rgba(255,255,255,.07);
  --verified: #3b9dff;
  --official: #22c55e;
  --staff: #a78bfa;
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

.av-08:has(#av-08-dark:checked) .av-08__img {
  box-shadow: 0 0 0 1px rgba(255,255,255,.08);
}

.av-08:has(#av-08-dark:checked) .av-08__tip {
  background: var(--panel-2);
  color: var(--ink);
  box-shadow: 0 0 0 1px var(--line);
}

.av-08:has(#av-08-dark:checked) .av-08__i--moon {
  display: none;
}

.av-08:has(#av-08-dark:checked) .av-08__i--sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .av-08:not(:has(#av-08-dark:checked)) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #262a33;
    --accent: #8b8cf9;
    --glass: rgba(255,255,255,.07);
    --verified: #3b9dff;
    --official: #22c55e;
    --staff: #a78bfa;
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-08:not(:has(#av-08-dark:checked)) .av-08__img {
    box-shadow: 0 0 0 1px rgba(255,255,255,.08);
  }

  .av-08:not(:has(#av-08-dark:checked)) .av-08__tip {
    background: var(--panel-2);
    color: var(--ink);
    box-shadow: 0 0 0 1px var(--line);
  }

  .av-08:not(:has(#av-08-dark:checked)) .av-08__i--moon {
    display: none;
  }

  .av-08:not(:has(#av-08-dark:checked)) .av-08__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-08 *,
    .av-08 *::before,
    .av-08 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-08__badge {
    background: Canvas;
    color: CanvasText;
    box-shadow: 0 0 0 2px Canvas, 0 0 0 3px CanvasText;
  }

  .av-08__row,
    .av-08__inline,
    .av-08__theme {
    border-color: CanvasText;
  }
}
```
