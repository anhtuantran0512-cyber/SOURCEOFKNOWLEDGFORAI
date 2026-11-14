---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/editorial/"
title: "Scrollytelling Timeline — Sticky Chapter Panel with Scrolling Beats"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "The long-form journalism pattern: a chapter panel (giant year, chapter title, running progress dots) pins to the left while its story beats scroll past on…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scrollytelling Timeline — Sticky Chapter Panel with Scrolling Beats
Source: https://codefronts.com/layouts/css-timelines/editorial/

The long-form journalism pattern: a chapter panel (giant year, chapter title, running progress dots) pins to the left while its story beats scroll past on the right, then the next chapter's panel takes over — the NYT-interactive structure, built from nothing but position:sticky and grid, no scroll library, no observers.
## HTML
```html
<section class="tls-24" aria-label="Scrollytelling timeline demo">
  <div class="tls-24__inner">
    <section class="tls-24__chapter" id="tls30-c1">
      <aside class="tls-24__panel">
        <p class="tls-24__num">Chapter 1</p>
        <p class="tls-24__year" aria-hidden="true">2019</p>
        <h4 class="tls-24__ct">The problem nobody claimed</h4>
        <p class="tls-24__dots" aria-label="Chapter 1 of 3"><span class="tls-24__dot tls-24__dot--on"></span><span class="tls-24__dot"></span><span class="tls-24__dot"></span></p>
      </aside>
      <div class="tls-24__beats">
        <div class="tls-24__beat"><p>Every team had the same spreadsheet. Nobody owned it, everybody edited it, and once a quarter it broke payroll.</p></div>
        <div class="tls-24__beat"><p>Three engineers started fixing it on Friday afternoons. Their manager pretended not to notice, which was the budget.</p></div>
      </div>
    </section>
    <section class="tls-24__chapter" id="tls30-c2">
      <aside class="tls-24__panel">
        <p class="tls-24__num">Chapter 2</p>
        <p class="tls-24__year" aria-hidden="true">2022</p>
        <h4 class="tls-24__ct">Accidentally a product</h4>
        <p class="tls-24__dots" aria-label="Chapter 2 of 3"><span class="tls-24__dot"></span><span class="tls-24__dot tls-24__dot--on"></span><span class="tls-24__dot"></span></p>
      </aside>
      <div class="tls-24__beats">
        <div class="tls-24__beat"><p>A partner company asked to license 'the payroll thing'. The invoice was written before the name was.</p></div>
        <div class="tls-24__beat"><p>By December, external revenue passed the team's own cost. The Friday project got a Monday-to-Friday budget.</p></div>
      </div>
    </section>
    <section class="tls-24__chapter" id="tls30-c3">
      <aside class="tls-24__panel">
        <p class="tls-24__num">Chapter 3</p>
        <p class="tls-24__year" aria-hidden="true">2026</p>
        <h4 class="tls-24__ct">The spin-out</h4>
        <p class="tls-24__dots" aria-label="Chapter 3 of 3"><span class="tls-24__dot"></span><span class="tls-24__dot"></span><span class="tls-24__dot tls-24__dot--on"></span></p>
      </aside>
      <div class="tls-24__beats">
        <div class="tls-24__beat"><p>Forty people, four hundred customers, and the original spreadsheet framed in the lobby — cell C7 still showing #REF!.</p></div>
      </div>
    </section>
  </div>
</section>
```
## CSS
```css
.tls-24,
.tls-24 *,
.tls-24 *::before,
.tls-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-24 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #9a3412;
  --tl-line: #eadfd6;
  --tl-ink: #292018;
  --tl-mut: #8a7767;
  font-family: Georgia,'Times New Roman',serif;
  background: #faf6f2;
  padding: 64px 24px;
}

.tls-24__inner {
  width: min(820px,100%);
  margin-inline: auto;
}

.tls-24__chapter {
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 40px;
  padding-bottom: 60px;
}

.tls-24__panel {
  position: sticky;
  top: 15vh;
  align-self: start;
  padding-top: 8px;
}

.tls-24__num {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--tl-accent);
}

.tls-24__year {
  font-size: clamp(44px,7vw,72px);
  font-weight: 700;
  color: var(--tl-ink);
  letter-spacing: -.04em;
  line-height: 1;
  margin: 8px 0 10px;
}

.tls-24__ct {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 15px;
  font-weight: 750;
  color: var(--tl-ink);
  letter-spacing: -.01em;
  line-height: 1.35;
  margin-bottom: 16px;
  text-wrap: balance;
}

.tls-24__dots {
  display: flex;
  gap: 6px;
}

.tls-24__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  border: 2px solid var(--tl-mut);
  display: inline-block;
}

.tls-24__dot--on {
  background: var(--tl-accent);
  border-color: var(--tl-accent);
}

.tls-24__beats {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.tls-24__beat {
  min-height: 32vh;
  display: grid;
  align-content: center;
  background: #fff;
  border: 1px solid var(--tl-line);
  border-radius: 16px;
  padding: 34px 36px;
}

.tls-24__beat p {
  font-size: clamp(16px,2.2vw,19px);
  line-height: 1.75;
  color: #463a2f;
  text-wrap: pretty;
}

@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .tls-24__beat {
      animation: tls-24-in linear both;
      animation-timeline: view();
      animation-range: entry 0% entry 50%;
    }

    @keyframes tls-24-in {
      from {
        opacity: .2;
        transform: translateY(16px);
      }

      to {
        opacity: 1;
        transform: none;
      }
    }
  }
}

@media (max-width: 640px) {
  .tls-24__chapter {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .tls-24__panel {
    position: static;
  }
}
```

## JavaScript
```js
/* No JavaScript — chapter panels are position:sticky with align-self:start (mandatory in grid, or sticky silently fails); chapter handoff is containment physics; the beat entrance is an optional view() layer behind a double gate. */
```
