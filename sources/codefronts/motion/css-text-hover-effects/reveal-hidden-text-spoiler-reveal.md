---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/reveal-hidden-text-spoiler-reveal/"
title: "Reveal Hidden Text / Spoiler Reveal"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "The spoiler pattern done properly — three affordances layered on one blur: HOVER peeks at the answer while the cursor stays (mouse users), a real CHECKBOX…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Reveal Hidden Text / Spoiler Reveal
Source: https://codefronts.com/motion/css-text-hover-effects/reveal-hidden-text-spoiler-reveal/

The spoiler pattern done properly — three affordances layered on one blur: HOVER peeks at the answer while the cursor stays (mouse users), a real CHECKBOX pins it revealed (touch and keyboard users — hover-only spoilers are broken on phones), and a 'reveal all' master switch flips the whole card via :has() with staggered delays. While hidden, user-select:none stops copy-paste cheating and a REVEALS-ON chip tells users the row is interactive. Pure CSS; the checkbox is genuine form state you could persist.
## HTML
```html
<section class="cth-12" aria-label="Spoiler reveal demo">
  <div class="cth-12__stage">
    <article class="cth-12__card">
      <header class="cth-12__head">
        <div><p class="cth-12__eyebrow">The Thursday Quiz &mdash; round 4</p><h2>Cinema, unspoiled</h2></div>
        <label class="cth-12__all"><input class="cth-12__allbox" type="checkbox"><span>Reveal all</span></label>
      </header>
      <ol class="cth-12__list">
        <li class="cth-12__row" style="--i:0">
          <p class="cth-12__q">Which 2024 film's twist hinges on the narrator being the composer?</p>
          <div class="cth-12__a"><span class="cth-12__ans"><em>The Long Static</em> &mdash; the score was the confession all along.</span><label class="cth-12__pinlab"><input class="cth-12__pin" type="checkbox" aria-label="Reveal answer 1"><i aria-hidden="true"></i></label></div>
        </li>
        <li class="cth-12__row" style="--i:1">
          <p class="cth-12__q">Who directed it &mdash; and what was their day job until 2019?</p>
          <div class="cth-12__a"><span class="cth-12__ans">Mara Chen &mdash; she was a foley artist, which explains everything.</span><label class="cth-12__pinlab"><input class="cth-12__pin" type="checkbox" aria-label="Reveal answer 2"><i aria-hidden="true"></i></label></div>
        </li>
        <li class="cth-12__row" style="--i:2">
          <p class="cth-12__q">The final shot mirrors which 1962 classic, frame for frame?</p>
          <div class="cth-12__a"><span class="cth-12__ans"><em>La Jet&eacute;e</em> &mdash; a still photograph, finally allowed to move.</span><label class="cth-12__pinlab"><input class="cth-12__pin" type="checkbox" aria-label="Reveal answer 3"><i aria-hidden="true"></i></label></div>
        </li>
      </ol>
      <p class="cth-12__hint">Hover an answer to peek; the <b>Reveal</b> pill pins it (touch &amp; keyboard get equal rights). <code>:has(:checked)</code> does the state &mdash; no JS.</p>
    </article>
  </div>
</section>
```
## CSS
```css
.cth-12,
.cth-12 *,
.cth-12 *::before,
.cth-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-12 {
  --bg: oklch(0.965 0.008 90);
  --card: oklch(1 0 0);
  --ink: oklch(0.27 0.02 290);
  --mut: oklch(0.52 0.02 290);
  --acc: oklch(0.55 0.19 295);
  --line: oklch(0.9 0.01 290);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-12__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: var(--bg);
  padding: clamp(20px,4vw,56px);
  container: cth12/inline-size;
}

.cth-12__card {
  width: min(100%,680px);
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: clamp(20px,4cqi,34px);
  box-shadow: 0 20px 60px oklch(0.35 0.05 295/.1);
}

.cth-12__head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  padding-bottom: 16px;
  border-bottom: 1.5px solid var(--ink);
}

.cth-12__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--acc);
}

.cth-12__head h2 {
  font-size: clamp(20px,3.4cqi,27px);
  font-weight: 850;
  letter-spacing: -.02em;
  margin-top: 4px;
}

.cth-12__all {
  display: flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 16px;
  border: 1.5px solid var(--line);
  border-radius: 99px;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: border-color .25s,background .25s,color .25s;
}

.cth-12__all:hover {
  border-color: var(--acc);
}

.cth-12__all:has(:checked) {
  background: var(--acc);
  border-color: var(--acc);
  color: oklch(0.98 0.005 90);
}

.cth-12__all:has(:focus-visible) {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cth-12__allbox,
.cth-12__pin {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cth-12__list {
  list-style: none;
  counter-reset: cth12;
  display: flex;
  flex-direction: column;
}

.cth-12__row {
  counter-increment: cth12;
  padding: clamp(14px,2.6cqi,20px) 0;
  border-bottom: 1px solid var(--line);
}

.cth-12__q {
  font-size: 15.5px;
  font-weight: 700;
  line-height: 1.5;
}

.cth-12__q::before {
  content: 'Q' counter(cth12) '  ';
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  font-weight: 600;
  color: var(--acc);
  letter-spacing: .06em;
}

.cth-12__a {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-top: 10px;
}

.cth-12__ans {
  flex: 1;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
  filter: blur(9px) saturate(.7);
  user-select: none;
  -webkit-user-select: none;
  transition: filter .4s ease;
  transition-delay: calc(var(--i)*0ms);
}

.cth-12__row:hover .cth-12__ans,
.cth-12__row:has(.cth-12__pin:checked) .cth-12__ans,
.cth-12__card:has(.cth-12__allbox:checked) .cth-12__ans {
  filter: blur(0) saturate(1);
  user-select: text;
  -webkit-user-select: text;
}

.cth-12__card:has(.cth-12__allbox:checked) .cth-12__ans {
  transition-delay: calc(var(--i)*70ms);
}

.cth-12__pinlab {
  flex: none;
  display: grid;
  place-items: center;
  min-height: 44px;
  min-width: 74px;
  cursor: pointer;
}

.cth-12__pinlab i {
  font-style: normal;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--acc);
  border: 1.5px solid color-mix(in oklch,var(--acc) 45%,transparent);
  border-radius: 99px;
  padding: 8px 13px;
  transition: background .25s,color .25s,border-color .25s;
}

.cth-12__pinlab:hover i {
  border-color: var(--acc);
}

.cth-12__pinlab:has(:checked) i {
  background: var(--acc);
  border-color: var(--acc);
  color: oklch(0.98 0.005 90);
}

.cth-12__pinlab:has(:focus-visible) i {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cth-12__pinlab i::before {
  content: 'Reveal';
}

.cth-12__row:has(.cth-12__pin:checked) .cth-12__pinlab i::before {
  content: 'Hide';
}

.cth-12__hint {
  margin-top: 16px;
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
}

.cth-12__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.94 0.01 290);
  padding: 1px 6px;
  border-radius: 4px;
}

@container cth12 (width < 460px) {
  .cth-12__head {
    flex-direction: column;
  }

  .cth-12__a {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cth-12 * {
    transition-duration: .01ms !important;
    transition-delay: 0ms !important;
  }
}
```
