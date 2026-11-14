---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/chatgpt-response-bubble-css/"
title: "ChatGPT Response Bubble CSS"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "The layout every AI product converges on: the user prompt is a bubble, the assistant answer is not."
has_js: "true"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: ChatGPT Response Bubble CSS
Source: https://codefronts.com/snippets/css-chat-bubbles/chatgpt-response-bubble-css/

The layout every AI product converges on: the user prompt is a bubble, the assistant answer is not. Prompts sit right-aligned in a tinted capsule; the response flows full-width as real Markdown — headings, lists, inline code, a syntax-tinted code block with a copy button — under a small model badge. Streaming is animated with a blinking block caret, there is a Stop control mid-stream, and the feedback row only appears once the answer is complete.
## HTML
```html
<div class="cb-03">
  <button class="cb-03__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cb-03__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="cb-03__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>

  <section class="cb-03__shell" aria-label="Assistant conversation">
    <ol class="cb-03__thread" id="cb-03-thread" aria-label="Transcript">
      <li class="cb-03__turn cb-03__turn--user">
        <div class="cb-03__body"><p>Give me a CSS-only way to truncate text to three lines.</p></div>
      </li>
      <li class="cb-03__turn cb-03__turn--ai">
        <div class="cb-03__meta">
          <span class="cb-03__mark" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 3.5 20 8v8l-8 4.5L4 16V8z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="12" cy="12" r="2.4" fill="currentColor"/></svg>
          </span>
          <b class="cb-03__model">Atlas 4.2</b>
        </div>
        <div class="cb-03__body">
          <p>Use the line-clamp shorthand — it is now unprefixed and works with any <code>display</code> value:</p>
          <figure class="cb-03__code">
            <figcaption class="cb-03__code-bar">
              <span class="cb-03__lang">css</span>
              <button class="cb-03__copy" type="button" data-code=".excerpt{&#10;  line-clamp: 3;&#10;  overflow: hidden;&#10;  text-overflow: ellipsis;&#10;}">
                <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.5" stroke="currentColor" stroke-width="1.7"/><path d="M15 6.5A2.5 2.5 0 0 0 12.5 4H6.5A2.5 2.5 0 0 0 4 6.5v6A2.5 2.5 0 0 0 6.5 15" stroke="currentColor" stroke-width="1.7"/></svg>
                <span class="cb-03__copy-text">Copy</span>
              </button>
            </figcaption>
            <pre class="cb-03__pre" tabindex="0"><code><span class="cb-03__sel">.excerpt</span>{
  <span class="cb-03__prop">line-clamp</span>: <span class="cb-03__val">3</span>;
  <span class="cb-03__prop">overflow</span>: <span class="cb-03__val">hidden</span>;
  <span class="cb-03__prop">text-overflow</span>: <span class="cb-03__val">ellipsis</span>;
}</code></pre>
          </figure>
          <p>Three caveats worth knowing:</p>
          <ol class="cb-03__list">
            <li>The element still needs <code>overflow: hidden</code> — clamping does not clip on its own.</li>
            <li>Older engines want the <code>-webkit-box</code> trio; keep it as a fallback below the shorthand.</li>
            <li>Clamped text is still fully present in the accessibility tree, so never clamp something a user must read.</li>
          </ol>
        </div>
        <div class="cb-03__acts">
          <button class="cb-03__act" type="button" aria-label="Copy response"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.5" stroke="currentColor" stroke-width="1.7"/><path d="M15 6.5A2.5 2.5 0 0 0 12.5 4H6.5A2.5 2.5 0 0 0 4 6.5v6A2.5 2.5 0 0 0 6.5 15" stroke="currentColor" stroke-width="1.7"/></svg></button>
          <button class="cb-03__act" type="button" aria-pressed="false" aria-label="Good response"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 20V10.5l4.2-6.1a1.7 1.7 0 0 1 3 1.4L13.3 10H18a2 2 0 0 1 2 2.3l-1 5.4A2.6 2.6 0 0 1 16.4 20z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M7 20H5.4A1.4 1.4 0 0 1 4 18.6v-6.7a1.4 1.4 0 0 1 1.4-1.4H7" stroke="currentColor" stroke-width="1.6"/></svg></button>
          <button class="cb-03__act" type="button" aria-pressed="false" aria-label="Bad response"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M17 4v9.5l-4.2 6.1a1.7 1.7 0 0 1-3-1.4L10.7 14H6a2 2 0 0 1-2-2.3l1-5.4A2.6 2.6 0 0 1 7.6 4z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M17 4h1.6A1.4 1.4 0 0 1 20 5.4v6.7a1.4 1.4 0 0 1-1.4 1.4H17" stroke="currentColor" stroke-width="1.6"/></svg></button>
        </div>
      </li>
    </ol>

    <div class="cb-03__dock">
      <div class="cb-03__chips" role="group" aria-label="Suggested prompts">
        <button class="cb-03__chip" type="button" data-q="scroll">Scroll-driven animation in 6 lines</button>
        <button class="cb-03__chip" type="button" data-q="has">What can <code>:has()</code> replace?</button>
        <button class="cb-03__chip" type="button" data-q="oklch">Why oklch over hsl?</button>
      </div>
      <div class="cb-03__field">
        <textarea class="cb-03__input" id="cb-03-input" rows="1" placeholder="Ask anything about modern CSS…" aria-label="Message the assistant"></textarea>
        <button class="cb-03__send" id="cb-03-send" type="button" aria-label="Send prompt" disabled>
          <svg class="cb-03__arrow" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 19V6m0 0-5.4 5.4M12 6l5.4 5.4" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <svg class="cb-03__stop" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="7.5" y="7.5" width="9" height="9" rx="2" fill="currentColor"/></svg>
        </button>
      </div>
    </div>
    <p class="cb-03__status" id="cb-03-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

@property --cb-03-x {
  syntax: '<percentage>';
  inherits: false;
  initial-value: -40%;
}

.cb-03 {
  --bg: #f7f7f9;
  --surface: #ffffff;
  --ink: #101319;
  --muted: #646e7e;
  --line: #e5e8ef;
  --u-bg: #eceef4;
  --u-ink: #101319;
  --acc: #10a37f;
  --acc-ink: #ffffff;
  --ring: #10a37f;
  --code-bg: #0e1116;
  --code-ink: #d7dee9;
  --shadow: rgba(16,19,25,.14);
  --measure: 44rem;
  --sans: "Plus Jakarta Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
  background: radial-gradient(90% 60% at 80% 0%, color-mix(in oklab,var(--acc) 12%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-03,
.cb-03 *,
.cb-03 *::before,
.cb-03 *::after {
  box-sizing: border-box;
}

.cb-03 ::selection {
  background: color-mix(in oklab,var(--acc) 30%,transparent);
}

@supports (color: oklch(0 0 0)) {
  .cb-03 {
    --bg: oklch(97% .004 265);
    --surface: oklch(100% 0 0);
    --ink: oklch(18% .015 265);
    --muted: oklch(55% .02 265);
    --line: oklch(92% .006 265);
    --u-bg: oklch(94.5% .006 265);
    --acc: oklch(62% .13 165);
  }
}

.cb-03__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,3vw,1.6rem);
  inset-inline-end: clamp(.9rem,3vw,1.6rem);
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  z-index: 5;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  box-shadow: 0 2px 10px -6px var(--shadow);
  transition: transform .25s cubic-bezier(.16,1,.3,1);
}

.cb-03__theme:hover {
  transform: translateY(-2px);
}

.cb-03__theme svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-03__sun {
  display: none;
}

.cb-03 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.cb-03__shell {
  inline-size: min(100%,calc(var(--measure) + 6rem));
  max-block-size: min(90svh,50rem);
  display: grid;
  grid-template-rows: 1fr auto auto;
  gap: 0;
  border-radius: clamp(1.25rem,3vw,1.9rem);
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 40px 90px -60px var(--shadow);
  overflow: hidden;
  container-type: inline-size;
}

.cb-03__thread {
  list-style: none;
  margin: 0;
  padding: clamp(1.1rem,3cqi,2rem);
  display: grid;
  gap: clamp(1.4rem,3cqi,2.1rem);
  overflow-y: auto;
  overflow-anchor: auto;
  scrollbar-width: thin;
}

.cb-03__turn {
  display: grid;
  gap: .6rem;
  max-inline-size: var(--measure);
  inline-size: 100%;
  margin-inline: auto;
}

.cb-03__body {
  font-size: clamp(.95rem,.35cqi + .9rem,1.03rem);
  line-height: 1.62;
  letter-spacing: -.008em;
  text-wrap: pretty;
}

.cb-03__body > * + * {
  margin-block-start: .9em;
}

.cb-03__body p {
  margin: 0;
}
/* prompt = bubble */

.cb-03__turn--user .cb-03__body {
  justify-self: end;
  max-inline-size: min(34rem,80cqi);
  padding: .75rem 1.05rem;
  background: var(--u-bg);
  color: var(--u-ink);
  border-radius: 1.35rem 1.35rem .5rem 1.35rem;
  animation: cb-03-pop .45s cubic-bezier(.16,1,.3,1) backwards;
}

@keyframes cb-03-pop {
  from {
    opacity: 0;
    transform: translateY(8px) scale(.97);
  }

  to {
    opacity: 1;
    transform: none;
  }
}
/* answer = prose */

.cb-03__meta {
  display: flex;
  align-items: center;
  gap: .5rem;
}

.cb-03__mark {
  inline-size: 26px;
  block-size: 26px;
  display: grid;
  place-items: center;
  border-radius: 9px;
  background: color-mix(in oklab,var(--acc) 14%,transparent);
  color: var(--acc);
}

.cb-03__mark svg {
  inline-size: 16px;
  block-size: 16px;
}

.cb-03__model {
  font-size: .78rem;
  font-weight: 600;
  letter-spacing: .01em;
  color: var(--muted);
}

.cb-03__list {
  margin: 0;
  padding-inline-start: 1.35rem;
  display: grid;
  gap: .45rem;
}

.cb-03__body code {
  font-family: var(--mono);
  font-size: .86em;
  padding: .12em .38em;
  border-radius: .4em;
  background: color-mix(in oklab,var(--ink) 7%,transparent);
}
/* code block */

.cb-03__code {
  margin: 0;
  border-radius: .95rem;
  overflow: hidden;
  background: var(--code-bg);
  border: 1px solid color-mix(in oklab,var(--code-bg) 70%,var(--line));
}

.cb-03__code-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .5rem;
  padding: .35rem .4rem .35rem .9rem;
  border-block-end: 1px solid rgba(255,255,255,.07);
}

.cb-03__lang {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #8b95a6;
}

.cb-03__copy {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  min-block-size: 36px;
  padding: .3rem .6rem;
  border: 0;
  border-radius: .55rem;
  background: transparent;
  color: #aab4c4;
  cursor: pointer;
  font: inherit;
  font-size: .76rem;
  font-weight: 500;
  transition: background .2s, color .2s;
}

.cb-03__copy svg {
  inline-size: 15px;
  block-size: 15px;
}

.cb-03__copy:hover {
  background: rgba(255,255,255,.08);
  color: #fff;
}

.cb-03__copy[data-done] {
  color: #4ade80;
}

.cb-03__pre {
  margin: 0;
  padding: .95rem 1rem 1.1rem;
  overflow-x: auto;
  color: var(--code-ink);
  font-family: var(--mono);
  font-size: .83rem;
  line-height: 1.65;
  tab-size: 2;
}

.cb-03__sel {
  color: #7dd3fc;
}

.cb-03__prop {
  color: #c4b5fd;
}

.cb-03__val {
  color: #86efac;
}
/* actions */

.cb-03__acts {
  display: flex;
  gap: .15rem;
}

.cb-03__act {
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 0;
  border-radius: .7rem;
  background: transparent;
  color: var(--muted);
  transition: background .2s, color .2s, transform .2s cubic-bezier(.16,1,.3,1);
}

.cb-03__act svg {
  inline-size: 19px;
  block-size: 19px;
}

.cb-03__act:hover {
  background: var(--u-bg);
  color: var(--ink);
  transform: translateY(-1px);
}

.cb-03__act[aria-pressed="true"] {
  color: var(--acc);
  background: color-mix(in oklab,var(--acc) 12%,transparent);
}
/* thinking + caret */

.cb-03__think {
  font-size: .95rem;
  font-weight: 500;
  background: linear-gradient(90deg,var(--muted) 0 20%,var(--acc) var(--cb-03-x),var(--muted) 80% 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: cb-03-shimmer 1.7s linear infinite;
}

@keyframes cb-03-shimmer {
  from {
    --cb-03-x: -20%;
  }

  to {
    --cb-03-x: 120%;
  }
}

.cb-03__body[data-streaming] > :last-child::after {
  content: '';
  display: inline-block;
  inline-size: .48em;
  block-size: 1.02em;
  vertical-align: -.14em;
  margin-inline-start: .14em;
  background: currentColor;
  border-radius: 1px;
  animation: cb-03-caret 1s steps(2,jump-none) infinite;
}

@keyframes cb-03-caret {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}
/* dock */

.cb-03__dock {
  padding: clamp(.75rem,2cqi,1.1rem);
  border-block-start: 1px solid var(--line);
  background: color-mix(in oklab,var(--surface) 80%,var(--bg));
  display: grid;
  gap: .65rem;
}

.cb-03__chips {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  justify-content: center;
}

.cb-03__chip {
  min-block-size: 38px;
  padding: .4rem .8rem;
  border-radius: 999px;
  cursor: pointer;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--muted);
  font: inherit;
  font-size: .8rem;
  font-weight: 500;
  letter-spacing: -.005em;
  transition: transform .22s cubic-bezier(.16,1,.3,1), color .2s, border-color .2s;
}

.cb-03__chip code {
  font-family: var(--mono);
  font-size: .9em;
}

.cb-03__chip:hover {
  transform: translateY(-2px);
  color: var(--ink);
  border-color: color-mix(in oklab,var(--acc) 45%,var(--line));
}

.cb-03__field {
  display: flex;
  align-items: flex-end;
  gap: .4rem;
  padding: .35rem .35rem .35rem 1rem;
  border: 1px solid var(--line);
  border-radius: 1.4rem;
  background: var(--surface);
  box-shadow: 0 12px 30px -26px var(--shadow);
  transition: border-color .25s;
}

.cb-03__field:focus-within {
  border-color: color-mix(in oklab,var(--acc) 55%,var(--line));
}

.cb-03__input {
  flex: 1;
  border: 0;
  outline: 0;
  resize: none;
  background: transparent;
  color: var(--ink);
  font: inherit;
  font-size: 1rem;
  line-height: 1.5;
  padding-block: .65rem;
  max-block-size: 8rem;
}

@supports (field-sizing: content) {
  .cb-03__input {
    field-sizing: content;
  }
}

.cb-03__input::placeholder {
  color: var(--muted);
}

.cb-03__send {
  inline-size: 40px;
  block-size: 40px;
  flex: 0 0 auto;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 50%;
  background: var(--ink);
  color: var(--surface);
  cursor: pointer;
  transition: transform .25s cubic-bezier(.16,1,.3,1), opacity .2s, background .2s;
}

.cb-03__send svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-03__stop {
  display: none;
}

.cb-03__send:disabled {
  opacity: .28;
  cursor: not-allowed;
}

.cb-03__send:not(:disabled):hover {
  transform: scale(1.07);
}

.cb-03__send[data-busy] {
  background: var(--acc);
  color: var(--acc-ink);
  opacity: 1;
  cursor: pointer;
}

.cb-03__send[data-busy] .cb-03__arrow {
  display: none;
}

.cb-03__send[data-busy] .cb-03__stop {
  display: block;
}

.cb-03__status {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@container (max-width: 34rem) {
  .cb-03__chips {
    flex-wrap: nowrap;
    overflow-x: auto;
    justify-content: flex-start;
    scrollbar-width: none;
  }

  .cb-03__chip {
    white-space: nowrap;
  }
}
/* dark */

.cb-03[data-theme="dark"] {
  --bg: #0b0d11;
  --surface: #14171d;
  --ink: #eceff5;
  --muted: #909aab;
  --line: #232830;
  --u-bg: #22262f;
  --u-ink: #eceff5;
  --code-bg: #0a0c10;
  --shadow: rgba(0,0,0,.7);
}

.cb-03[data-theme="dark"] .cb-03__moon {
  display: none;
}

.cb-03[data-theme="dark"] .cb-03__sun {
  display: block;
}

.cb-03[data-theme="dark"] .cb-03__send {
  background: var(--ink);
  color: #0b0d11;
}

@media (prefers-color-scheme: dark) {
  .cb-03:not([data-theme="light"]) {
    --bg: #0b0d11;
    --surface: #14171d;
    --ink: #eceff5;
    --muted: #909aab;
    --line: #232830;
    --u-bg: #22262f;
    --u-ink: #eceff5;
    --code-bg: #0a0c10;
    --shadow: rgba(0,0,0,.7);
  }

  .cb-03:not([data-theme="light"]) .cb-03__moon {
    display: none;
  }

  .cb-03:not([data-theme="light"]) .cb-03__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-03 *,
    .cb-03 *::before,
    .cb-03 *::after {
    animation: none !important;
    transition: none !important;
  }

  .cb-03__think {
    background: none;
    color: var(--muted);
  }
}

@media (forced-colors: active) {
  .cb-03__turn--user .cb-03__body,
    .cb-03__code,
    .cb-03__field {
    border: 1px solid CanvasText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.cb-03');
  if (!root) return;
  const thread = root.querySelector('#cb-03-thread');
  const input = root.querySelector('#cb-03-input');
  const send = root.querySelector('#cb-03-send');
  const status = root.querySelector('#cb-03-status');

  const ANSWERS = {
    scroll: ['Scroll-driven animations need no JavaScript at all — you name a timeline and hand it to an animation.', 'Attach animation-timeline: scroll() for progress through a scroller, or view() for progress of the element through the viewport. Everything else is ordinary @keyframes.', 'Because it runs off the compositor, it stays smooth on long documents where a scroll listener would jank.'],
    has: [':has() lets a parent react to its descendants, which removes an entire class of wrapper divs and state classes.', 'The common wins: styling a card that contains an image, marking a form row invalid from the input inside it, collapsing a layout when a panel is present, and building radio-driven switches with no script.', 'Treat it as a query, not a loop — it is fast, but keep the selector inside it cheap.'],
    oklch: ['oklch() is perceptually uniform, so equal numeric steps look like equal visual steps — hsl() does not give you that.', 'Two practical consequences: a lightness ramp built in oklch reads evenly across every hue, and color-mix() in oklab never drifts through grey the way sRGB interpolation does.', 'It also reaches colours outside sRGB on wide-gamut displays, with automatic clamping elsewhere.'],
    default: ['Here is the short version.', 'Modern CSS solves most of this at the layout level: container queries for component-level responsiveness, :has() for parent state, and logical properties so the same rules work in right-to-left languages.', 'If you tell me the exact browser floor you support, I can narrow that down to the two or three properties you actually need.']
  };
  const pick = (q) => ANSWERS[q] || ANSWERS.default;
  let busy = false, timer = null;

  const addUser = (text) => {
    const li = document.createElement('li');
    li.className = 'cb-03__turn cb-03__turn--user';
    const body = document.createElement('div');
    body.className = 'cb-03__body';
    const p = document.createElement('p');
    p.textContent = text; body.append(p); li.append(body); thread.append(li);
    thread.scrollTop = thread.scrollHeight;
  };

  const addAI = () => {
    const li = document.createElement('li');
    li.className = 'cb-03__turn cb-03__turn--ai';
    li.innerHTML = '<div class="cb-03__meta"><span class="cb-03__mark" aria-hidden="true">'
      + '<svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 3.5 20 8v8l-8 4.5L4 16V8z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="12" cy="12" r="2.4" fill="currentColor"/></svg>'
      + '</span><b class="cb-03__model">Atlas 4.2</b></div>'
      + '<div class="cb-03__body"><p class="cb-03__think">Thinking…</p></div>';
    thread.append(li);
    thread.scrollTop = thread.scrollHeight;
    return li.querySelector('.cb-03__body');
  };

  /* word-by-word stream — swap this for a ReadableStream reader against a real API */
  const stream = (body, paras) => {
    busy = true; send.dataset.busy = ''; send.disabled = false;
    body.dataset.streaming = '';
    let pi = 0, wi = 0, para = null;
    const words = paras.map((t) => t.split(' '));
    setTimeout(() => {
      body.textContent = '';
      timer = setInterval(() => {
        if (pi >= words.length) return finish();
        if (wi === 0) { para = document.createElement('p'); body.append(para); }
        para.textContent += (wi ? ' ' : '') + words[pi][wi];
        wi += 1;
        if (wi >= words[pi].length) { pi += 1; wi = 0; }
        thread.scrollTop = thread.scrollHeight;
      }, 38);
    }, 620);

    const finish = () => {
      clearInterval(timer); timer = null; busy = false;
      delete body.dataset.streaming; delete send.dataset.busy;
      send.disabled = !input.value.trim();
      body.insertAdjacentHTML('afterend',
        '<div class="cb-03__acts">'
        + '<button class="cb-03__act" type="button" aria-label="Copy response"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.5" stroke="currentColor" stroke-width="1.7"/><path d="M15 6.5A2.5 2.5 0 0 0 12.5 4H6.5A2.5 2.5 0 0 0 4 6.5v6A2.5 2.5 0 0 0 6.5 15" stroke="currentColor" stroke-width="1.7"/></svg></button>'
        + '<button class="cb-03__act" type="button" aria-pressed="false" aria-label="Good response"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 20V10.5l4.2-6.1a1.7 1.7 0 0 1 3 1.4L13.3 10H18a2 2 0 0 1 2 2.3l-1 5.4A2.6 2.6 0 0 1 16.4 20z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></button>'
        + '<button class="cb-03__act" type="button" aria-pressed="false" aria-label="Bad response"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M17 4v9.5l-4.2 6.1a1.7 1.7 0 0 1-3-1.4L10.7 14H6a2 2 0 0 1-2-2.3l1-5.4A2.6 2.6 0 0 1 7.6 4z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></button>'
        + '</div>');
      status.textContent = 'Response complete.';   /* announce once, not per chunk */
    };
    body.__finish = finish;
  };

  const ask = (text, key) => {
    if (busy) return;
    addUser(text);
    stream(addAI(), pick(key));
  };

  input.addEventListener('input', () => { if (!busy) send.disabled = !input.value.trim(); });
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send.click(); } });
  send.addEventListener('click', () => {
    if (busy) {                                  /* Stop */
      const body = thread.querySelector('.cb-03__body[data-streaming]');
      if (body && body.__finish) body.__finish();
      status.textContent = 'Generation stopped.';
      return;
    }
    const text = input.value.trim();
    if (!text) return;
    input.value = ''; send.disabled = true;
    ask(text, 'default');
  });
  root.querySelectorAll('.cb-03__chip').forEach((c) => {
    c.addEventListener('click', () => ask(c.textContent.trim(), c.dataset.q));
  });

  /* copy — clipboard API with a textarea fallback for sandboxed frames */
  const copy = async (text) => {
    try { await navigator.clipboard.writeText(text); return true; }
    catch {
      const ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;top:-1000px;opacity:0';
      document.body.append(ta); ta.select();
      const ok = document.execCommand('copy'); ta.remove(); return ok;
    }
  };
  thread.addEventListener('click', async (e) => {
    const btn = e.target.closest('.cb-03__copy');
    if (btn) {
      const ok = await copy(btn.dataset.code || '');
      btn.dataset.done = '';
      btn.querySelector('.cb-03__copy-text').textContent = ok ? 'Copied' : 'Press Ctrl+C';
      status.textContent = ok ? 'Code copied to clipboard' : 'Copy blocked by the browser';
      setTimeout(() => { delete btn.dataset.done; btn.querySelector('.cb-03__copy-text').textContent = 'Copy'; }, 2200);
      return;
    }
    const act = e.target.closest('.cb-03__act');
    if (!act) return;
    if (act.getAttribute('aria-label') === 'Copy response') {
      const ok = await copy(act.closest('.cb-03__turn').querySelector('.cb-03__body').innerText.trim());
      status.textContent = ok ? 'Response copied' : 'Copy blocked by the browser';
      return;
    }
    const on = act.getAttribute('aria-pressed') === 'true';
    act.closest('.cb-03__acts').querySelectorAll('[aria-pressed]').forEach((b) => b.setAttribute('aria-pressed', 'false'));
    act.setAttribute('aria-pressed', String(!on));
    status.textContent = on ? 'Feedback cleared' : act.getAttribute('aria-label') + ' recorded';
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.cb-03');
  const btn = root && root.querySelector('.cb-03__theme');
  if (!btn) return;
  const isDark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    btn.setAttribute('aria-pressed', String(isDark()));
    btn.setAttribute('aria-label', isDark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  sync();
})();
```
