---
source: "codefronts"
url: "https://codefronts.com/layouts/css-full-page-sections/css-scroll-snap-stop-to-prevent-skipping-sections/"
title: "CSS Scroll Snap Stop to Prevent Skipping Sections"
section: "layouts"
category: "css-full-page-sections"
category_name: "CSS Full Page Sections"
description: "Two live scrollers side by side, identical except for one declaration."
has_js: "false"
---

Here's a working CSS Full Page Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Scroll Snap Stop to Prevent Skipping Sections
Source: https://codefronts.com/layouts/css-full-page-sections/css-scroll-snap-stop-to-prevent-skipping-sections/

Two live scrollers side by side, identical except for one declaration. Flick the left one hard and it flies past two panels; flick the right one and scroll-snap-stop: always catches it at the very next panel. Only a handful of production sites use this property &mdash; this demo shows what it fixes, and the one case where it hurts.
## HTML
```html
<div class="fps-03">
  <input class="fps-03__sr" type="checkbox" id="fps-03-dark">
  <label class="fps-03__theme" for="fps-03-dark" title="Switch light or dark theme">
    <svg class="fps-03__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="fps-03__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="fps-03__vh">Switch light or dark theme</span>
  </label>

  <div class="fps-03__scroller" tabindex="0" role="group" aria-label="Scroll snap stop demonstration, three panels">

    <section class="fps-03__panel" id="fps-03-s1" aria-labelledby="fps-03-h1">
      <div class="fps-03__stage">
        <p class="fps-03__eyebrow"><span class="fps-03__num">01 / 03</span><span class="fps-03__mono">scroll-snap-stop: always</span></p>
        <h2 class="fps-03__title" id="fps-03-h1">Stop the flick that skips your best section</h2>
        <p class="fps-03__lead">Default snapping only decides where momentum <em>ends</em>. One hard swipe can therefore fly past two panels &mdash; and past whatever argument they carried. <code>scroll-snap-stop:always</code> makes each gesture advance exactly one panel.</p>
        <div class="fps-03__ab" aria-hidden="false">
          <figure class="fps-03__mini">
            <figcaption><span class="fps-03__tag fps-03__tag--no">normal</span>Flick hard &mdash; it skips</figcaption>
            <div class="fps-03__mscroll" tabindex="0" role="group" aria-label="Scroller without snap stop, five panels">
              <div class="fps-03__mpanel" style="--h:14"><span>01</span><p>Problem</p></div>
              <div class="fps-03__mpanel" style="--h:34"><span>02</span><p>Approach</p></div>
              <div class="fps-03__mpanel" style="--h:150"><span>03</span><p>Proof</p></div>
              <div class="fps-03__mpanel" style="--h:200"><span>04</span><p>Pricing</p></div>
              <div class="fps-03__mpanel" style="--h:265"><span>05</span><p>Sign up</p></div>
            </div>
          </figure>
          <figure class="fps-03__mini">
            <figcaption><span class="fps-03__tag fps-03__tag--yes">always</span>Flick hard &mdash; it holds</figcaption>
            <div class="fps-03__mscroll fps-03__mscroll--stop" tabindex="0" role="group" aria-label="Scroller with scroll snap stop always, five panels">
              <div class="fps-03__mpanel" style="--h:14"><span>01</span><p>Problem</p></div>
              <div class="fps-03__mpanel" style="--h:34"><span>02</span><p>Approach</p></div>
              <div class="fps-03__mpanel" style="--h:150"><span>03</span><p>Proof</p></div>
              <div class="fps-03__mpanel" style="--h:200"><span>04</span><p>Pricing</p></div>
              <div class="fps-03__mpanel" style="--h:265"><span>05</span><p>Sign up</p></div>
            </div>
          </figure>
        </div>
        <p class="fps-03__note">Your browser does not support <code>scroll-snap-stop</code>, so both scrollers behave identically &mdash; the pattern degrades to <code>normal</code>, never to broken.</p>
      </div>
    </section>

    <section class="fps-03__panel" id="fps-03-s2" aria-labelledby="fps-03-h2">
      <div class="fps-03__stage">
        <p class="fps-03__eyebrow"><span class="fps-03__num">02 / 03</span><span class="fps-03__mono">where the property goes</span></p>
        <h2 class="fps-03__title fps-03__title--sm" id="fps-03-h2">On the panel. Never on the scroller.</h2>
        <div class="fps-03__pair">
          <div class="fps-03__box fps-03__box--no">
            <p class="fps-03__bh">Does nothing</p>
            <pre><code>.scroller{
  scroll-snap-type:y mandatory;
  scroll-snap-stop:always; /* ignored */
}</code></pre>
          </div>
          <div class="fps-03__box fps-03__box--yes">
            <p class="fps-03__bh">Works</p>
            <pre><code>.panel{
  scroll-snap-align:start;
  scroll-snap-stop:always; /* enforced */
}</code></pre>
          </div>
        </div>
        <p class="fps-03__lead">It also requires an active <code>scroll-snap-align</code> on the same element &mdash; a snap stop with nothing to snap to is inert. And it constrains user gestures only: <code>scrollTo()</code> and anchor jumps still travel as far as you send them.</p>
      </div>
    </section>

    <section class="fps-03__panel" id="fps-03-s3" aria-labelledby="fps-03-h3">
      <div class="fps-03__stage">
        <p class="fps-03__eyebrow"><span class="fps-03__num">03 / 03</span><span class="fps-03__mono">when not to use it</span></p>
        <h2 class="fps-03__title fps-03__title--sm" id="fps-03-h3">Short sequences yes, long pages no</h2>
        <dl class="fps-03__table">
          <div class="fps-03__row"><dt>3&ndash;6 panels</dt><dd><strong>Use it.</strong> Onboarding, a product tour, a pitch. Every panel carries a point the reader must not skip past.</dd></div>
          <div class="fps-03__row"><dt>7+ panels</dt><dd><strong>Leave it off.</strong> One gesture per panel becomes friction, and skimmers &mdash; most of your traffic &mdash; cannot skim.</dd></div>
          <div class="fps-03__row"><dt>Selective</dt><dd><strong>Best of both.</strong> Put <code>always</code> on the two panels that matter (pricing, consent) and let the rest stay <code>normal</code>.</dd></div>
          <div class="fps-03__row"><dt>Reduced motion</dt><dd><strong>Reset it.</strong> With snapping disabled, forcing one panel per gesture makes no sense &mdash; ship <code>scroll-snap-stop:normal</code> in that media query.</dd></div>
        </dl>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fps-03 {
  --bg: #fdfaf6;
  --panel: #ffffff;
  --panel2: #f6f1ea;
  --ink: #171310;
  --muted: rgba(23,19,16,.62);
  --line: rgba(23,19,16,.12);
  --accent: #c2410c;
  --yes: #15803d;
  --no: #b91c1c;
  --sans: 'Geist',system-ui,-apple-system,'Segoe UI',sans-serif;
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  --h-scroller: clamp(11rem,30vh,17rem);
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
  .fps-03 {
    --accent: oklch(56% .18 42);
    --yes: oklch(52% .14 148);
    --no: oklch(52% .19 27);
    --ink: oklch(16% .015 45);
    --bg: oklch(98% .008 75);
    --panel2: oklch(95% .014 75);
  }
}

.fps-03 * {
  box-sizing: border-box;
}

.fps-03 h2,
.fps-03 p,
.fps-03 dl,
.fps-03 dd,
.fps-03 figure,
.fps-03 figcaption,
.fps-03 pre {
  margin: 0;
}

.fps-03 code {
  font-family: var(--mono);
  font-size: .92em;
}

.fps-03__sr,
.fps-03__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-03__theme {
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
  background: rgba(255,255,255,.62);
  border: 1px solid var(--line);
  -webkit-backdrop-filter: blur(10px) saturate(150%);
  backdrop-filter: blur(10px) saturate(150%);
  box-shadow: 0 8px 24px -12px rgba(23,19,16,.35);
}

.fps-03__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.fps-03__theme svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fps-03__moon {
  display: none;
}

.fps-03__sr:focus-visible + .fps-03__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-03__scroller {
  block-size: 100dvh;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
  overscroll-behavior-y: contain;
  scrollbar-width: none;
}

.fps-03__scroller::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.fps-03__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.fps-03__panel {
  position: relative;
  min-block-size: 100dvh;
  scroll-snap-align: start;
  background: var(--panel);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(2rem,5vh,3.5rem) clamp(1.25rem,5vw,4.5rem) calc(clamp(2rem,5vh,3.5rem) + 4rem);
}

.fps-03__panel:nth-child(even) {
  background: var(--panel2);
}

.fps-03__panel + .fps-03__panel {
  margin-block-start: -4rem;
  border-start-start-radius: 1.75rem;
  border-start-end-radius: 1.75rem;
  border-block-start: 1px solid var(--line);
  box-shadow: 0 -30px 64px -34px rgba(23,19,16,.24);
}

@supports not (height: 100dvh) {
  .fps-03__scroller {
    block-size: 100vh;
  }

  .fps-03__panel {
    min-block-size: 100vh;
  }
}

.fps-03__stage {
  inline-size: min(68rem,100%);
  display: grid;
  gap: clamp(.9rem,2.2vh,1.4rem);
  justify-items: start;
}

.fps-03__eyebrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
}

.fps-03__num {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.fps-03__mono {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
  padding: .22rem .5rem;
  border: 1px solid var(--line);
  border-radius: .45rem;
}

.fps-03__title {
  font-size: clamp(1.95rem,5.2vw,3.6rem);
  line-height: 1.04;
  letter-spacing: -.04em;
  font-weight: 600;
  max-inline-size: 22ch;
  text-wrap: balance;
}

.fps-03__title--sm {
  font-size: clamp(1.7rem,3.6vw,2.6rem);
  letter-spacing: -.03em;
  max-inline-size: 28ch;
}

.fps-03__lead {
  font-size: clamp(.98rem,1.35vw,1.12rem);
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 60ch;
  text-wrap: pretty;
}

.fps-03__ab {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(14rem,1fr));
  gap: clamp(.9rem,2.5vw,1.75rem);
  inline-size: 100%;
}

.fps-03__mini {
  display: grid;
  gap: .6rem;
}

.fps-03__mini figcaption {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-size: .85rem;
  color: var(--muted);
}

.fps-03__tag {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .08em;
  padding: .2rem .45rem;
  border-radius: .4rem;
  border: 1px solid currentColor;
}

.fps-03__tag--yes {
  color: var(--yes);
}

.fps-03__tag--no {
  color: var(--no);
}

.fps-03__mscroll {
  block-size: var(--h-scroller);
  overflow-y: auto;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
  border-radius: 1.1rem;
  border: 1px solid var(--line);
  scrollbar-width: none;
  background: color-mix(in srgb,var(--ink) 4%,transparent);
}

.fps-03__mscroll::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.fps-03__mscroll:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fps-03__mpanel {
  block-size: calc(var(--h-scroller) - 1.8rem);
  scroll-snap-align: start;
  display: grid;
  align-content: center;
  gap: .15rem;
  padding-inline: clamp(.9rem,2vw,1.4rem);
  background: hsl(var(--h) 70% 96%);
  border-block-end: 1px solid var(--line);
}

@supports (background: oklch(90% .05 40)) {
  .fps-03__mpanel {
    background: oklch(95% .045 calc(var(--h) * 1deg));
  }
}

.fps-03__mpanel span {
  font-family: var(--mono);
  font-size: clamp(1.6rem,4vw,2.4rem);
  font-variant-numeric: tabular-nums;
  color: hsl(var(--h) 65% 32%);
  letter-spacing: -.03em;
}

.fps-03__mpanel p {
  font-size: .85rem;
  color: hsl(var(--h) 30% 30%);
  letter-spacing: .02em;
}

@supports (color: oklch(40% .1 40)) {
  .fps-03__mpanel span {
    color: oklch(48% .16 calc(var(--h) * 1deg));
  }

  .fps-03__mpanel p {
    color: oklch(45% .06 calc(var(--h) * 1deg));
  }
}

@supports (scroll-snap-stop: always) {
  .fps-03__mscroll--stop .fps-03__mpanel {
    scroll-snap-stop: always;
  }
}

.fps-03__note {
  display: none;
  font-size: .85rem;
  line-height: 1.5;
  color: var(--no);
  padding: .7rem .9rem;
  border-radius: .75rem;
  border: 1px dashed color-mix(in srgb,var(--no) 45%,transparent);
}

@supports not (scroll-snap-stop: always) {
  .fps-03__note {
    display: block;
  }
}

.fps-03__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(15rem,1fr));
  gap: clamp(.85rem,2vw,1.5rem);
  inline-size: 100%;
}

.fps-03__box {
  border-radius: 1.15rem;
  border: 1px solid var(--line);
  overflow: hidden;
  background: var(--bg);
}

.fps-03__bh {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: .7rem .9rem;
  border-block-end: 1px solid var(--line);
}

.fps-03__box--yes .fps-03__bh {
  color: var(--yes);
}

.fps-03__box--no .fps-03__bh {
  color: var(--no);
}

.fps-03__box pre {
  padding: .95rem .9rem 1.15rem;
  overflow-x: auto;
}

.fps-03__box code {
  font-size: clamp(.76rem,1vw,.86rem);
  line-height: 1.7;
  color: var(--muted);
  white-space: pre;
}

.fps-03__table {
  inline-size: 100%;
  display: grid;
  gap: .4rem;
}

.fps-03__row {
  display: grid;
  grid-template-columns: minmax(6.5rem,9rem) 1fr;
  gap: clamp(.75rem,2vw,1.75rem);
  padding: clamp(.75rem,1.5vh,1.05rem) 0;
  border-block-start: 1px solid var(--line);
}

.fps-03__row dt {
  font-family: var(--mono);
  font-size: .86rem;
  color: var(--accent);
}

.fps-03__row dd {
  font-size: .96rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.fps-03__row dd strong {
  color: var(--ink);
  font-weight: 550;
}

.fps-03[data-theme="dark"],
.fps-03:has(#fps-03-dark:checked) {
  --bg: #0a0806;
  --panel: #0f0c09;
  --panel2: #161210;
  --ink: #f8f4ef;
  --muted: rgba(248,244,239,.62);
  --line: rgba(248,244,239,.14);
  --accent: #fdba74;
  --yes: #86efac;
  --no: #fca5a5;
}

.fps-03:has(#fps-03-dark:checked) .fps-03__theme {
  background: rgba(255,255,255,.07);
}

.fps-03:has(#fps-03-dark:checked) .fps-03__sun {
  display: none;
}

.fps-03:has(#fps-03-dark:checked) .fps-03__moon {
  display: block;
}

.fps-03:has(#fps-03-dark:checked) .fps-03__mpanel {
  background: hsl(var(--h) 40% 12%);
}

.fps-03:has(#fps-03-dark:checked) .fps-03__mpanel span {
  color: hsl(var(--h) 80% 78%);
}

.fps-03:has(#fps-03-dark:checked) .fps-03__mpanel p {
  color: hsl(var(--h) 25% 72%);
}

@media (prefers-color-scheme: dark) {
  .fps-03:not([data-theme="light"]):not(:has(#fps-03-dark:checked)) {
    --bg: #0a0806;
    --panel: #0f0c09;
    --panel2: #161210;
    --ink: #f8f4ef;
    --muted: rgba(248,244,239,.62);
    --line: rgba(248,244,239,.14);
    --accent: #fdba74;
    --yes: #86efac;
    --no: #fca5a5;
  }

  .fps-03:not([data-theme="light"]):not(:has(#fps-03-dark:checked)) .fps-03__theme {
    background: rgba(255,255,255,.07);
  }

  .fps-03:not([data-theme="light"]):not(:has(#fps-03-dark:checked)) .fps-03__sun {
    display: none;
  }

  .fps-03:not([data-theme="light"]):not(:has(#fps-03-dark:checked)) .fps-03__moon {
    display: block;
  }

  .fps-03:not([data-theme="light"]):not(:has(#fps-03-dark:checked)) .fps-03__mpanel {
    background: hsl(var(--h) 40% 12%);
  }

  .fps-03:not([data-theme="light"]):not(:has(#fps-03-dark:checked)) .fps-03__mpanel span {
    color: hsl(var(--h) 80% 78%);
  }

  .fps-03:not([data-theme="light"]):not(:has(#fps-03-dark:checked)) .fps-03__mpanel p {
    color: hsl(var(--h) 25% 72%);
  }
}

@supports not selector(:has(*)) {
  .fps-03__theme {
    display: none;
  }
}

@media (max-height: 40rem) {
  .fps-03 {
    --h-scroller: clamp(7.5rem,24vh,17rem);
  }

  .fps-03__scroller {
    scroll-snap-type: y proximity;
  }

  .fps-03__panel {
    padding-block: 1.25rem 3rem;
  }

  .fps-03__stage {
    gap: .7rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fps-03__scroller,
    .fps-03__mscroll {
    scroll-snap-type: none;
    scroll-behavior: auto;
  }

  .fps-03__mscroll--stop .fps-03__mpanel {
    scroll-snap-stop: normal;
  }

  .fps-03 *,
    .fps-03 *::before,
    .fps-03 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fps-03__panel,
    .fps-03__box,
    .fps-03__mscroll,
    .fps-03__mpanel,
    .fps-03__theme,
    .fps-03__tag {
    border-color: CanvasText;
    box-shadow: none;
    background: Canvas;
    color: CanvasText;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }
}
```
