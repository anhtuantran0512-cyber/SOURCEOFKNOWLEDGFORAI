---
source: "codefronts"
url: "https://codefronts.com/layouts/css-full-page-sections/css-accessible-scroll-snap-with-keyboard-navigation/"
title: "CSS Accessible Scroll Snap with Keyboard Navigation"
section: "layouts"
category: "css-full-page-sections"
category_name: "CSS Full Page Sections"
description: "The panel that makes the pattern shippable: proximity snapping so nothing traps a keyboard user, arrow / Page&nbsp;Up / Page&nbsp;Down / Home / End…"
has_js: "true"
---

Here's a working CSS Full Page Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Accessible Scroll Snap with Keyboard Navigation
Source: https://codefronts.com/layouts/css-full-page-sections/css-accessible-scroll-snap-with-keyboard-navigation/

The panel that makes the pattern shippable: proximity snapping so nothing traps a keyboard user, arrow / Page&nbsp;Up / Page&nbsp;Down / Home / End navigation that also moves focus, a skip link past the whole scroller, one labelled <section> per panel, a polite live region announcing position, and prefers-reduced-motion turning snapping and smooth scrolling off entirely.
## HTML
```html
<div class="fps-12">
  <input class="fps-12__sr" type="checkbox" id="fps-12-dark">
  <label class="fps-12__theme" for="fps-12-dark" title="Switch light or dark theme">
    <svg class="fps-12__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="fps-12__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="fps-12__vh">Switch light or dark theme</span>
  </label>

  <a class="fps-12__skip" href="#fps-12-end">Skip the panel sequence</a>
  <p class="fps-12__live" role="status" aria-live="polite"></p>

  <div class="fps-12__scroller" tabindex="0" role="group" aria-label="Accessible panel sequence, five panels. Use arrow keys, Page Up and Page Down.">

    <section class="fps-12__panel" tabindex="-1" data-label="Proximity by default" id="fps-12-s1" aria-labelledby="fps-12-h1">
      <div class="fps-12__stage">
        <p class="fps-12__eyebrow"><span class="fps-12__num">01 / 05</span><span class="fps-12__mono">scroll-snap-type: y proximity</span></p>
        <h2 class="fps-12__title" id="fps-12-h1">Snapping that never traps anyone</h2>
        <p class="fps-12__lead">Arrow keys, Page&nbsp;Up, Page&nbsp;Down, Home and End all move between panels and carry focus with them. The scrollport is focusable, so the keys work before a single line of script runs.</p>
        <ul class="fps-12__keys">
          <li><kbd>&darr;</kbd><kbd>&uarr;</kbd><span>next / previous panel</span></li>
          <li><kbd>PgDn</kbd><kbd>PgUp</kbd><span>same, one screen at a time</span></li>
          <li><kbd>Home</kbd><kbd>End</kbd><span>first / last panel</span></li>
          <li><kbd>Tab</kbd><span>next control &mdash; never trapped</span></li>
        </ul>
      </div>
    </section>

    <section class="fps-12__panel" tabindex="-1" data-label="Why mandatory can trap" id="fps-12-s2" aria-labelledby="fps-12-h2">
      <div class="fps-12__stage">
        <p class="fps-12__eyebrow"><span class="fps-12__num">02 / 05</span><span class="fps-12__mono">the WCAG failure</span></p>
        <h2 class="fps-12__title fps-12__title--sm" id="fps-12-h2">How mandatory snapping hides focused content</h2>
        <p class="fps-12__lead">With <code>mandatory</code>, the scrollport must always rest on a snap point. If a panel is taller than the screen &mdash; or a control sits below its fold &mdash; the browser can pull the scroll back to the panel edge, leaving the focused element off screen with no way to reach it.</p>
        <div class="fps-12__pair">
          <div class="fps-12__box fps-12__box--no"><p class="fps-12__bh">mandatory</p><p>Rests only on snap points. Content between them can become unreachable.</p></div>
          <div class="fps-12__box fps-12__box--yes"><p class="fps-12__bh">proximity</p><p>Snaps when the reader stops near an edge. Everything in between stays reachable.</p></div>
        </div>
      </div>
    </section>

    <section class="fps-12__panel" tabindex="-1" data-label="Focus follows the scroll" id="fps-12-s3" aria-labelledby="fps-12-h3">
      <div class="fps-12__stage">
        <p class="fps-12__eyebrow"><span class="fps-12__num">03 / 05</span><span class="fps-12__mono">focus, preventScroll</span></p>
        <h2 class="fps-12__title fps-12__title--sm" id="fps-12-h3">Move the scroll and the focus together</h2>
        <pre class="fps-12__code"><code>scroller.scrollTo({ top:panels[n].offsetTop, behavior });
panels[n].focus({ <mark>preventScroll:true</mark> });</code></pre>
        <p class="fps-12__lead">Without <code>preventScroll</code> the browser performs its own scroll to the focused element, which fights the animated one and shows as a double jump. With it, focus lands silently and the next <kbd>Tab</kbd> continues from where the reader is actually looking.</p>
      </div>
    </section>

    <section class="fps-12__panel" tabindex="-1" data-label="Announcing position" id="fps-12-s4" aria-labelledby="fps-12-h4">
      <div class="fps-12__stage">
        <p class="fps-12__eyebrow"><span class="fps-12__num">04 / 05</span><span class="fps-12__mono">aria-live: polite</span></p>
        <h2 class="fps-12__title fps-12__title--sm" id="fps-12-h4">Tell the reader where they are, quietly</h2>
        <p class="fps-12__lead">Each panel is a real <code>&lt;section&gt;</code> labelled by its own heading, so it is announced as a named region and shows up in the landmark rotor. Position (&ldquo;Panel 4 of 5&rdquo;) goes to a polite live region &mdash; announced without interrupting, and without focus ever jumping to a status element.</p>
        <ul class="fps-12__marks">
          <li><strong>polite</strong><span>queued behind whatever is being read</span></li>
          <li><strong>assertive</strong><span>interrupts &mdash; wrong for a scroll position</span></li>
          <li><strong>tabindex -1</strong><span>programmatic target, not a tab stop</span></li>
        </ul>
      </div>
    </section>

    <section class="fps-12__panel" tabindex="-1" data-label="Reduced motion" id="fps-12-s5" aria-labelledby="fps-12-h5">
      <div class="fps-12__stage">
        <p class="fps-12__eyebrow"><span class="fps-12__num">05 / 05</span><span class="fps-12__mono">prefers-reduced-motion</span></p>
        <h2 class="fps-12__title fps-12__title--sm" id="fps-12-h5">Reduced motion switches the whole pattern off</h2>
        <p class="fps-12__lead">Snapping off, smooth scrolling off, transitions off, and programmatic scrolls switched to <code>auto</code> &mdash; the script reads the same media query the CSS does. What is left is an ordinary document with tall sections, which is precisely what the setting asks for.</p>
        <p id="fps-12-end" class="fps-12__end" tabindex="-1">End of the sequence &mdash; the skip link lands here.</p>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fps-12 {
  --bg: #f5faf6;
  --panel: #ffffff;
  --panel2: #edf5ef;
  --ink: #071109;
  --muted: rgba(7,17,9,.62);
  --line: rgba(7,17,9,.11);
  --accent: #166534;
  --yes: #166534;
  --no: #9f1239;
  --sans: 'Geist',system-ui,-apple-system,'Segoe UI',sans-serif;
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  isolation: isolate;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% .1 250)) {
  .fps-12 {
    --accent: oklch(45% .13 150);
    --yes: oklch(45% .13 150);
    --no: oklch(48% .16 12);
    --ink: oklch(12% .02 150);
    --bg: oklch(97.6% .01 150);
    --panel2: oklch(95% .015 150);
  }
}

.fps-12 * {
  box-sizing: border-box;
}

.fps-12 h2,
.fps-12 p,
.fps-12 ul,
.fps-12 pre {
  margin: 0;
}

.fps-12 code {
  font-family: var(--mono);
  font-size: .92em;
}

.fps-12__sr,
.fps-12__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-12__live {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-12__theme {
  position: fixed;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 80;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  cursor: pointer;
  color: var(--ink);
  background: rgba(255,255,255,.66);
  border: 1px solid var(--line);
  -webkit-backdrop-filter: blur(10px) saturate(150%);
  backdrop-filter: blur(10px) saturate(150%);
  box-shadow: 0 8px 24px -12px rgba(7,17,9,.35);
}

.fps-12__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.fps-12__theme svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fps-12__moon {
  display: none;
}

.fps-12__sr:focus-visible + .fps-12__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-12__skip {
  position: fixed;
  inset-block-start: 1.15rem;
  inset-inline-start: 1.15rem;
  z-index: 90;
  min-block-size: 2.75rem;
  display: inline-flex;
  align-items: center;
  padding: .7rem 1.1rem;
  border-radius: 999px;
  font-size: .85rem;
  text-decoration: none;
  color: var(--accent);
  background: var(--panel);
  border: 1px solid color-mix(in srgb,var(--accent) 35%,transparent);
  translate: 0 -150%;
  opacity: 0;
  transition: translate .2s ease, opacity .2s ease;
}

.fps-12__skip:focus-visible {
  translate: 0 0;
  opacity: 1;
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-12__scroller {
  position: relative;
  block-size: 100dvh;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-snap-type: y proximity;
  scroll-behavior: smooth;
  overscroll-behavior-y: contain;
  scrollbar-width: none;
}

.fps-12__scroller::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.fps-12__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.fps-12__panel {
  position: relative;
  min-block-size: 100dvh;
  scroll-snap-align: start;
  background: var(--panel);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(4.5rem,10vh,6rem) clamp(1.25rem,5vw,4.5rem) calc(clamp(2rem,5vh,3.5rem) + 4rem);
}

.fps-12__panel:nth-child(even) {
  background: var(--panel2);
}

.fps-12__panel + .fps-12__panel {
  margin-block-start: -4rem;
  border-start-start-radius: 1.75rem;
  border-start-end-radius: 1.75rem;
  border-block-start: 1px solid var(--line);
  box-shadow: 0 -30px 64px -34px rgba(7,17,9,.2);
}

.fps-12__panel:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -4px;
}

@supports not (height: 100dvh) {
  .fps-12__scroller {
    block-size: 100vh;
  }

  .fps-12__panel {
    min-block-size: 100vh;
  }
}

.fps-12__stage {
  inline-size: min(58rem,100%);
  display: grid;
  gap: clamp(.9rem,2.2vh,1.4rem);
  justify-items: start;
}

.fps-12__eyebrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
}

.fps-12__num {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.fps-12__mono {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
  padding: .22rem .5rem;
  border: 1px solid var(--line);
  border-radius: .45rem;
}

.fps-12__title {
  font-size: clamp(2rem,5.4vw,3.9rem);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 600;
  max-inline-size: 20ch;
  text-wrap: balance;
}

.fps-12__title--sm {
  font-size: clamp(1.65rem,3.6vw,2.55rem);
  letter-spacing: -.03em;
  max-inline-size: 27ch;
}

.fps-12__lead {
  font-size: clamp(.98rem,1.35vw,1.14rem);
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 60ch;
  text-wrap: pretty;
}

.fps-12__keys {
  list-style: none;
  padding: 0;
  display: grid;
  gap: .35rem;
  inline-size: 100%;
}

.fps-12__keys li {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .45rem;
  padding: .6rem 0;
  border-block-start: 1px solid var(--line);
}

.fps-12__keys kbd {
  font-family: var(--mono);
  font-size: .74rem;
  min-inline-size: 2.1rem;
  text-align: center;
  padding: .28rem .45rem;
  border-radius: .45rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
  box-shadow: 0 1px 0 var(--line);
}

.fps-12__keys span {
  margin-inline-start: .4rem;
  font-size: .94rem;
  color: var(--muted);
}

.fps-12__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(14rem,1fr));
  gap: clamp(.8rem,2vw,1.4rem);
  inline-size: 100%;
}

.fps-12__box {
  padding: clamp(1rem,2.2vw,1.35rem);
  border-radius: 1.15rem;
  border: 1px solid var(--line);
  display: grid;
  gap: .5rem;
  background: color-mix(in srgb,var(--ink) 3%,transparent);
}

.fps-12__box p {
  font-size: .94rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.fps-12__bh {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .1em;
  text-transform: uppercase;
}

.fps-12__box--yes .fps-12__bh {
  color: var(--yes);
}

.fps-12__box--no .fps-12__bh {
  color: var(--no);
}

.fps-12__code {
  padding: 1rem 1.1rem;
  border-radius: 1rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
  overflow-x: auto;
}

.fps-12__code code {
  font-size: clamp(.76rem,1vw,.87rem);
  line-height: 1.75;
  color: var(--muted);
  white-space: pre;
}

.fps-12__code mark {
  background: color-mix(in srgb,var(--accent) 14%,transparent);
  color: var(--accent);
  border-radius: .25rem;
  padding: .05rem .2rem;
}

.fps-12__marks {
  list-style: none;
  padding: 0;
  display: grid;
  gap: .3rem;
  inline-size: 100%;
}

.fps-12__marks li {
  display: grid;
  grid-template-columns: 7rem 1fr;
  gap: 1rem;
  padding: .65rem 0;
  border-block-start: 1px solid var(--line);
  align-items: baseline;
}

.fps-12__marks strong {
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--accent);
}

.fps-12__marks span {
  font-size: .93rem;
  color: var(--muted);
}

.fps-12__end {
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--accent);
  padding: .55rem .8rem;
  border-radius: .6rem;
  border: 1px dashed color-mix(in srgb,var(--accent) 40%,transparent);
}

.fps-12__end:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-12[data-theme="dark"],
.fps-12:has(#fps-12-dark:checked) {
  --bg: #050a06;
  --panel: #080f0a;
  --panel2: #0d1710;
  --ink: #eff7f1;
  --muted: rgba(239,247,241,.62);
  --line: rgba(239,247,241,.13);
  --accent: #86efac;
  --yes: #86efac;
  --no: #fda4af;
}

.fps-12:has(#fps-12-dark:checked) .fps-12__theme {
  background: rgba(255,255,255,.07);
}

.fps-12:has(#fps-12-dark:checked) .fps-12__sun {
  display: none;
}

.fps-12:has(#fps-12-dark:checked) .fps-12__moon {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .fps-12:not([data-theme="light"]):not(:has(#fps-12-dark:checked)) {
    --bg: #050a06;
    --panel: #080f0a;
    --panel2: #0d1710;
    --ink: #eff7f1;
    --muted: rgba(239,247,241,.62);
    --line: rgba(239,247,241,.13);
    --accent: #86efac;
    --yes: #86efac;
    --no: #fda4af;
  }

  .fps-12:not([data-theme="light"]):not(:has(#fps-12-dark:checked)) .fps-12__theme {
    background: rgba(255,255,255,.07);
  }

  .fps-12:not([data-theme="light"]):not(:has(#fps-12-dark:checked)) .fps-12__sun {
    display: none;
  }

  .fps-12:not([data-theme="light"]):not(:has(#fps-12-dark:checked)) .fps-12__moon {
    display: block;
  }
}

@supports not selector(:has(*)) {
  .fps-12__theme {
    display: none;
  }
}

@media (max-height: 40rem) {
  .fps-12__panel {
    padding-block: 3.25rem 3rem;
  }

  .fps-12__stage {
    gap: .7rem;
  }

  .fps-12__keys li {
    padding-block: .4rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fps-12__scroller {
    scroll-snap-type: none;
    scroll-behavior: auto;
  }

  .fps-12 *,
    .fps-12 *::before,
    .fps-12 *::after {
    animation: none !important;
    transition: none !important;
  }

  .fps-12__skip {
    translate: 0 0;
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .fps-12__panel,
    .fps-12__box,
    .fps-12__code,
    .fps-12__theme,
    .fps-12__skip,
    .fps-12__keys kbd {
    border-color: CanvasText;
    box-shadow: none;
    background: Canvas;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }
}
```

## JavaScript
```js
const fps12 = document.querySelector('.fps-12');
if (fps12) {
  const scroller = fps12.querySelector('.fps-12__scroller');
  const live = fps12.querySelector('.fps-12__live');
  const panels = [...fps12.querySelectorAll('.fps-12__panel')];
  const steps = { ArrowDown: 1, PageDown: 1, ArrowUp: -1, PageUp: -1 };
  const go = (i) => {
    const n = Math.min(panels.length - 1, Math.max(0, i));
    const soft = matchMedia('(prefers-reduced-motion: reduce)').matches;
    scroller.scrollTo({ top: panels[n].offsetTop, behavior: soft ? 'auto' : 'smooth' });
    panels[n].focus({ preventScroll: true });
    live.textContent = 'Panel ' + (n + 1) + ' of ' + panels.length + ': ' + panels[n].dataset.label;
  };
  const current = () => Math.max(0, panels.findIndex((p) => p === document.activeElement || p.contains(document.activeElement)));
  scroller.addEventListener('keydown', (event) => {
    if (event.key in steps) { event.preventDefault(); go(current() + steps[event.key]); }
    else if (event.key === 'Home') { event.preventDefault(); go(0); }
    else if (event.key === 'End') { event.preventDefault(); go(panels.length - 1); }
  });
}
```
