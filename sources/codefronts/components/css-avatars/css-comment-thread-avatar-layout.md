---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-comment-thread-avatar-layout/"
title: "CSS Comment Thread Avatar Layout"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "The avatar doing its real job: a threaded discussion where every reply aligns to its parent's text column, indent rails make depth legible without guessing,…"
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Comment Thread Avatar Layout
Source: https://codefronts.com/components/css-avatars/css-comment-thread-avatar-layout/

The avatar doing its real job: a threaded discussion where every reply aligns to its parent's text column, indent rails make depth legible without guessing, and avatars shrink one step per level so the hierarchy reads at a glance. Built on nested lists with a grid template per comment — so the layout survives long names, missing photos and three levels of nesting without a single absolute position.
## HTML
```html
<div class="av-22">
  <input class="av-22__sr" type="checkbox" id="av-22-dark">
  <label class="av-22__theme" for="av-22-dark">
    <svg class="av-22__i av-22__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-22__i av-22__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-22__vh">Dark theme</span>
  </label>

  <div class="av-22__stage">
    <section class="av-22__wrap" aria-labelledby="av-22-h">
      <header class="av-22__head">
        <p class="av-22__eyebrow">Discussion · 7 comments</p>
        <h2 class="av-22__h" id="av-22-h">Presence service rollout</h2>
        <p class="av-22__sub">Replies align to their parent's text column; the rail sits under the parent avatar's centre.</p>
      </header>

      <ul class="av-22__thread">
        <li>
          <article class="av-22__c" id="av-22-c1">
            <span class="av-22__fig">
              <img class="av-22__img" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=facearea&facepad=2.5" alt="Priya Sharma" width="200" height="200" loading="lazy" decoding="async">
            </span>
            <p class="av-22__chead"><strong>Priya Sharma</strong><span class="av-22__tag">Author</span><time datetime="2027-03-04T09:12">09:12</time></p>
            <p class="av-22__body">Rolling presence out to 5% of workspaces this morning. Reconnect storms were the whole risk here, so we are watching socket churn rather than error rate.</p>
            <p class="av-22__acts"><button class="av-22__act" type="button">Reply</button><button class="av-22__act" type="button">Resolve</button></p>
          </article>

          <ul class="av-22__replies">
            <li>
              <article class="av-22__c" id="av-22-c2">
                <span class="av-22__fig">
                  <img class="av-22__img" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Alex Chen" width="200" height="200" loading="lazy" decoding="async">
                </span>
                <p class="av-22__chead"><strong>Alex Chen</strong><time datetime="2027-03-04T09:31">09:31</time></p>
                <p class="av-22__body">Churn is flat at 5%. The backoff jitter we added last week is doing more work than I expected.</p>
                <p class="av-22__acts"><button class="av-22__act" type="button">Reply</button></p>
              </article>

              <ul class="av-22__replies">
                <li>
                  <article class="av-22__c" id="av-22-c3">
                    <span class="av-22__fig">
                      <img class="av-22__img" src="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=200&auto=format&fit=facearea&facepad=2.5" alt="Sam Rivera" width="200" height="200" loading="lazy" decoding="async">
                    </span>
                    <p class="av-22__chead"><strong>Sam Rivera</strong><time datetime="2027-03-04T09:44">09:44</time></p>
                    <p class="av-22__body">Confirmed on the dashboards — p95 reconnect is 380ms, down from 2.1s.</p>
                    <p class="av-22__acts"><button class="av-22__act" type="button">Reply</button></p>
                  </article>
                </li>
                <li>
                  <article class="av-22__c" id="av-22-c4">
                    <span class="av-22__fig">
                      <span class="av-22__mono" style="--h:96" aria-hidden="true">MO</span>
                      <span class="av-22__vh">Maya Okonkwo</span>
                    </span>
                    <p class="av-22__chead"><strong>Maya Okonkwo</strong><time datetime="2027-03-04T10:02">10:02</time></p>
                    <p class="av-22__body">Design note: the typing pulse reads as a loading spinner at the smaller avatar size. I would drop it below 32px.</p>
                    <p class="av-22__acts"><button class="av-22__act" type="button">Reply</button></p>
                  </article>
                </li>
              </ul>
            </li>

            <li>
              <article class="av-22__c" id="av-22-c5">
                <span class="av-22__fig">
                  <img class="av-22__img" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200&auto=format&fit=facearea&facepad=2.5" alt="Grace Tan" width="200" height="200" loading="lazy" decoding="async">
                </span>
                <p class="av-22__chead"><strong>Grace Tan</strong><span class="av-22__tag av-22__tag--staff">Staff</span><time datetime="2027-03-04T10:20">10:20</time></p>
                <p class="av-22__body">Agreed on 32px. I will add the threshold to the avatar size spec so it is not a per-surface decision.</p>
                <p class="av-22__acts"><button class="av-22__act" type="button">Reply</button></p>
              </article>
            </li>
          </ul>
        </li>

        <li>
          <article class="av-22__c" id="av-22-c6">
            <span class="av-22__fig">
              <img class="av-22__img" src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=200&auto=format&fit=facearea&facepad=2.5" alt="Ethan Brooks" width="200" height="200" loading="lazy" decoding="async">
            </span>
            <p class="av-22__chead"><strong>Ethan Brooks</strong><time datetime="2027-03-04T11:05">11:05</time></p>
            <p class="av-22__body">Moving to 25% after lunch if churn holds. I will post the graph in this thread rather than a new one.</p>
            <p class="av-22__acts"><button class="av-22__act" type="button">Reply</button><button class="av-22__act" type="button">Resolve</button></p>
          </article>
        </li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-22 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(91% .008 265);
    --accent: oklch(58% .196 272);
  }

  .av-22__mono {
    background: oklch(93% .055 var(--h));
    color: oklch(44% .13 var(--h));
  }
}

.av-22 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e2e5ec;
  --accent: #4f46e5;
  --glass: rgba(255,255,255,.68);
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
  --size: 2.5rem;
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

.av-22 *,
.av-22 *::before,
.av-22 *::after {
  box-sizing: border-box;
}

.av-22__vh {
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

.av-22__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-22__theme {
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

.av-22__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-22__theme:hover {
  translate: 0 -1px;
}

.av-22__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-22__i--sun {
  display: none;
}

.av-22__sr:focus-visible + .av-22__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-22__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-22__wrap {
  inline-size: min(50rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.1rem,2.6vw,1.6rem);
}

.av-22__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-22__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-22__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-22__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-22__thread {
  list-style: none;
  margin: 0;
  padding: clamp(1.1rem,3vw,1.75rem);
  display: flex;
  flex-direction: column;
  gap: clamp(1rem,2.5vw,1.5rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-22__replies {
  list-style: none;
  margin: .85rem 0 0;
  display: flex;
  flex-direction: column;
  gap: .9rem;
  margin-inline-start: calc(var(--size) / 2);
  padding-inline-start: calc(var(--size) / 2 + .8rem);
  border-inline-start: 2px solid var(--line);
  --size: 2.1rem;
}

.av-22__replies .av-22__replies {
  --size: 1.85rem;
}

.av-22__c {
  display: grid;
  gap: .15rem .8rem;
  padding: .5rem .6rem;
  margin-inline-start: -.6rem;
  border-radius: 12px;
  grid-template-columns: auto minmax(0,1fr);
  grid-template-areas: "fig head" "fig body" "fig acts";
  transition: background .2s ease;
}

.av-22__c:hover {
  background: var(--panel-2);
}

.av-22__c:target {
  background: var(--panel-2);
  box-shadow: inset 0 0 0 1px var(--line);
}

.av-22__fig {
  grid-area: fig;
  display: grid;
  place-items: center;
  inline-size: var(--size);
  aspect-ratio: 1;
  border-radius: 50%;
  overflow: hidden;
  background: var(--panel-2);
  margin-block-start: .15rem;
}

.av-22__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  object-position: center top;
}

.av-22__mono {
  display: grid;
  place-items: center;
  inline-size: 100%;
  block-size: 100%;
  background: hsl(var(--h) 72% 92%);
  color: hsl(var(--h) 55% 30%);
  font-size: calc(var(--size) * .34);
  font-weight: 700;
}

.av-22__chead {
  grid-area: head;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: .5rem;
  font-size: .9rem;
}

.av-22__chead strong {
  font-weight: 650;
  letter-spacing: -.015em;
}

.av-22__chead time {
  font-size: .76rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.av-22__tag {
  padding: .1rem .4rem;
  border-radius: 6px;
  background: var(--panel-2);
  color: var(--muted);
  font-size: .66rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.av-22__tag--staff {
  background: var(--accent);
  color: #fff;
}

.av-22__body {
  grid-area: body;
  margin: .1rem 0 0;
  font-size: .92rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
  max-inline-size: 44ch;
}

.av-22__acts {
  grid-area: acts;
  margin: .3rem 0 0;
  display: flex;
  flex-wrap: wrap;
  gap: .3rem;
}

.av-22__act {
  appearance: none;
  min-block-size: 2.25rem;
  padding: 0 .6rem;
  border-radius: 8px;
  border: 1px solid transparent;
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: .78rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .16s ease, color .16s ease;
}

.av-22__act:hover {
  background: var(--panel);
  color: var(--ink);
  border-color: var(--line);
}

.av-22__act:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-22:has(#av-22-dark:checked) {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #282d38;
  --accent: #6d6df5;
  --glass: rgba(255,255,255,.07);
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

.av-22:has(#av-22-dark:checked) .av-22__mono {
  background: hsl(var(--h) 42% 22%);
  color: hsl(var(--h) 78% 82%);
}

.av-22:has(#av-22-dark:checked) .av-22__i--moon {
  display: none;
}

.av-22:has(#av-22-dark:checked) .av-22__i--sun {
  display: block;
}

@supports (color: oklch(50% .1 250)) {
  .av-22:has(#av-22-dark:checked) .av-22__mono {
    background: oklch(30% .07 var(--h));
    color: oklch(88% .12 var(--h));
  }
}

@media (prefers-color-scheme: dark) {
  .av-22:not(:has(#av-22-dark:checked)) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #282d38;
    --accent: #6d6df5;
    --glass: rgba(255,255,255,.07);
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-22:not(:has(#av-22-dark:checked)) .av-22__mono {
    background: hsl(var(--h) 42% 22%);
    color: hsl(var(--h) 78% 82%);
  }

  .av-22:not(:has(#av-22-dark:checked)) .av-22__i--moon {
    display: none;
  }

  .av-22:not(:has(#av-22-dark:checked)) .av-22__i--sun {
    display: block;
  }

  @supports (color: oklch(50% .1 250)) {
    .av-22:not(:has(#av-22-dark:checked)) .av-22__mono {
      background: oklch(30% .07 var(--h));
      color: oklch(88% .12 var(--h));
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-22 *,
    .av-22 *::before,
    .av-22 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-22__replies {
    border-color: CanvasText;
  }

  .av-22__tag--staff {
    background: Highlight;
    color: HighlightText;
  }

  .av-22__thread,
    .av-22__theme {
    border-color: CanvasText;
  }
}
```
