---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/accordion-timeline/"
title: "Accordion Timeline — Expandable Milestones with Exclusive Open"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "The space-saver: a vertical milestone rail where each date row is a <details> disclosure — one click expands the story, and the name attribute makes the set…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accordion Timeline — Expandable Milestones with Exclusive Open
Source: https://codefronts.com/layouts/css-timelines/accordion-timeline/

The space-saver: a vertical milestone rail where each date row is a <details> disclosure — one click expands the story, and the name attribute makes the set EXCLUSIVE (opening one closes the others) with zero JavaScript — the mobile-first pattern for company histories, FAQs-over-time and product changelogs.
## HTML
```html
<section class="tls-16" aria-label="Accordion timeline demo">
  <div class="tls-16__wrap">
    <h3 class="tls-16__h">Twelve years, four turns</h3>
    <ol class="tls-16__list" role="list">
      <li class="tls-16__item">
        <details class="tls-16__d" name="tls-16">
          <summary class="tls-16__sum"><time class="tls-16__yr" datetime="2014">2014</time><span class="tls-16__ti">Founded in a garage that was actually a garage</span><span class="tls-16__pm" aria-hidden="true"></span></summary>
          <div class="tls-16__reveal"><div class="tls-16__panel"><p>Two founders, one contract, a space heater. The first product was a spreadsheet plugin nobody remembers — but the customer list from it became everything.</p></div></div>
        </details>
      </li>
      <li class="tls-16__item">
        <details class="tls-16__d" name="tls-16" open>
          <summary class="tls-16__sum"><time class="tls-16__yr" datetime="2019">2019</time><span class="tls-16__ti">The pivot: we deleted 80% of the product</span><span class="tls-16__pm" aria-hidden="true"></span></summary>
          <div class="tls-16__reveal"><div class="tls-16__panel"><p>Usage data said one feature carried the company. We cut the rest in a single release, halved onboarding time, and revenue doubled inside a year. The hardest board meeting we ever had.</p></div></div>
        </details>
      </li>
      <li class="tls-16__item">
        <details class="tls-16__d" name="tls-16">
          <summary class="tls-16__sum"><time class="tls-16__yr" datetime="2023">2023</time><span class="tls-16__ti">First profitable year · team of 40</span><span class="tls-16__pm" aria-hidden="true"></span></summary>
          <div class="tls-16__reveal"><div class="tls-16__panel"><p>Profitability changed the conversations: no runway math, just product. We opened the Toronto office and shipped the platform rewrite.</p></div></div>
        </details>
      </li>
      <li class="tls-16__item">
        <details class="tls-16__d" name="tls-16">
          <summary class="tls-16__sum"><time class="tls-16__yr" datetime="2026">2026</time><span class="tls-16__ti">10,000 teams · the second act begins</span><span class="tls-16__pm" aria-hidden="true"></span></summary>
          <div class="tls-16__reveal"><div class="tls-16__panel"><p>The roadmap for the next decade is the one we wrote in 2014 and couldn't afford. Now we can.</p></div></div>
        </details>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
.tls-16,
.tls-16 *,
.tls-16 *::before,
.tls-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-16 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #9333ea;
  --tl-line: #e5e0eb;
  --tl-ink: #241b2e;
  --tl-mut: #8a7f96;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #faf8fc;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-16__wrap {
  width: min(600px,100%);
}

.tls-16__h {
  font-size: clamp(20px,3.2vw,26px);
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.02em;
  margin-bottom: 22px;
}

.tls-16__list {
  list-style: none;
}

.tls-16__item {
  position: relative;
  padding-left: 30px;
}

.tls-16__item::before {
  content: '';
  position: absolute;
  left: 7px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: var(--tl-line);
}

.tls-16__item:first-child::before {
  top: 24px;
}

.tls-16__item:last-child::before {
  bottom: calc(100% - 24px);
}

.tls-16__item::after {
  content: '';
  position: absolute;
  left: 2px;
  top: 18px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid var(--tl-mut);
  box-shadow: 0 0 0 4px #faf8fc;
  transition: border-color .2s,scale .2s;
}

.tls-16__item:has(.tls-16__d[open])::after {
  border-color: var(--tl-accent);
  scale: 1.25;
}

.tls-16__sum {
  list-style: none;
  display: flex;
  align-items: baseline;
  gap: 14px;
  cursor: pointer;
  padding: 14px 6px;
  user-select: none;
  border-radius: 10px;
  transition: background .15s;
}

.tls-16__sum::-webkit-details-marker {
  display: none;
}

.tls-16__sum:hover {
  background: #f3eefa;
}

.tls-16__d[open] .tls-16__sum .tls-16__ti {
  color: var(--tl-accent);
}

.tls-16__yr {
  flex: none;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 13px;
  font-weight: 700;
  color: var(--tl-mut);
}

.tls-16__ti {
  flex: 1;
  font-size: 15.5px;
  font-weight: 700;
  color: var(--tl-ink);
  letter-spacing: -.01em;
  transition: color .2s;
  text-wrap: pretty;
}

.tls-16__pm {
  flex: none;
  position: relative;
  width: 14px;
  height: 14px;
  align-self: center;
}

.tls-16__pm::before,
.tls-16__pm::after {
  content: '';
  position: absolute;
  background: var(--tl-mut);
  border-radius: 1px;
  transition: transform .25s,background .2s;
}

.tls-16__pm::before {
  left: 0;
  right: 0;
  top: 6px;
  height: 2px;
}

.tls-16__pm::after {
  top: 0;
  bottom: 0;
  left: 6px;
  width: 2px;
}

.tls-16__d[open] .tls-16__pm::after {
  transform: rotate(90deg);
}

.tls-16__d[open] .tls-16__pm::before,
.tls-16__d[open] .tls-16__pm::after {
  background: var(--tl-accent);
}

.tls-16__reveal {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .35s ease;
}

.tls-16__d[open] .tls-16__reveal {
  grid-template-rows: 1fr;
}

.tls-16__panel {
  min-height: 0;
  overflow: hidden;
}

.tls-16__panel p {
  font-size: 14px;
  line-height: 1.65;
  color: #4a4055;
  padding: 2px 6px 18px calc(13px + 14px + 13ch - 13ch);
  max-width: 56ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .tls-16__reveal {
    transition: none;
  }

  .tls-16__pm::before,
    .tls-16__pm::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — details name="tls-16" gives native EXCLUSIVE accordion behavior (Baseline widely-available); the reveal animates grid-template-rows 0fr→1fr. */
```
