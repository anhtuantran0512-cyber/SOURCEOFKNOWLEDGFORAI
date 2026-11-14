---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/resume-work-experience-timeline-with-subgrid-alignment/"
title: "Resume / Work Experience Timeline with Subgrid Alignment"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "The classic career timeline done properly: a two-column grid where every date column, marker and description stays perfectly aligned across entries via CSS…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Resume / Work Experience Timeline with Subgrid Alignment
Source: https://codefronts.com/layouts/css-timelines/resume-work-experience-timeline-with-subgrid-alignment/

The classic career timeline done properly: a two-column grid where every date column, marker and description stays perfectly aligned across entries via CSS subgrid — even when one role has three bullet points and another has one — with duration chips computed into real <time> ranges.
## HTML
```html
<section class="tls-03" aria-label="Work experience timeline demo">
  <div class="tls-03__sheet">
    <h3 class="tls-03__h">Experience</h3>
    <ol class="tls-03__list" role="list">
      <li class="tls-03__item" aria-current="true">
        <div class="tls-03__when"><time datetime="2024-03">Mar 2024</time><span class="tls-03__to">— Present</span><span class="tls-03__chip">2 yr 4 mo</span></div>
        <div class="tls-03__rail" aria-hidden="true"><span class="tls-03__dot"></span></div>
        <div class="tls-03__body">
          <p class="tls-03__role">Staff Product Designer</p>
          <p class="tls-03__org">Harbourly · Full-time · Remote (US)</p>
          <ul class="tls-03__pts"><li>Own the design system used by 9 product squads</li><li>Led the container-query migration of 40+ shared components</li></ul>
        </div>
      </li>
      <li class="tls-03__item">
        <div class="tls-03__when"><time datetime="2021-09">Sep 2021</time><span class="tls-03__to">— Mar 2024</span><span class="tls-03__chip">2 yr 7 mo</span></div>
        <div class="tls-03__rail" aria-hidden="true"><span class="tls-03__dot"></span></div>
        <div class="tls-03__body">
          <p class="tls-03__role">Senior UX Designer</p>
          <p class="tls-03__org">Fernwork · Full-time · Toronto, CA</p>
          <ul class="tls-03__pts"><li>Shipped the onboarding redesign: +18% week-one retention</li></ul>
        </div>
      </li>
      <li class="tls-03__item">
        <div class="tls-03__when"><time datetime="2019-06">Jun 2019</time><span class="tls-03__to">— Sep 2021</span><span class="tls-03__chip">2 yr 3 mo</span></div>
        <div class="tls-03__rail" aria-hidden="true"><span class="tls-03__dot"></span></div>
        <div class="tls-03__body">
          <p class="tls-03__role">Product Designer</p>
          <p class="tls-03__org">Quill &amp; Co · Full-time · London, UK</p>
          <ul class="tls-03__pts"><li>First design hire; built the research practice from zero</li></ul>
        </div>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
.tls-03,
.tls-03 *,
.tls-03 *::before,
.tls-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-03 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #0a66c2;
  --tl-line: #d6dce4;
  --tl-ink: #1d2226;
  --tl-mut: #5f6b76;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #eef3f8;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-03__sheet {
  width: min(720px,100%);
  container-type: inline-size;
  background: #fff;
  border: 1px solid var(--tl-line);
  border-radius: 14px;
  padding: 28px 32px;
}

.tls-03__h {
  font-size: 18px;
  font-weight: 700;
  color: var(--tl-ink);
  margin-bottom: 20px;
  letter-spacing: -.01em;
}

.tls-03__list {
  list-style: none;
  display: grid;
  grid-template-columns: 13ch 24px 1fr;
  row-gap: 0;
}

.tls-03__item {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: subgrid;
  column-gap: 16px;
  padding-block: 16px;
  border-radius: 10px;
  transition: background .15s;
}

.tls-03__item:hover {
  background: #f4f8fc;
}

.tls-03__when {
  display: flex;
  flex-direction: column;
  gap: 2px;
  font-size: 12.5px;
  color: var(--tl-mut);
  padding-top: 2px;
}

.tls-03__when time {
  font-weight: 700;
  color: var(--tl-ink);
}

.tls-03__chip {
  align-self: flex-start;
  font-size: 10.5px;
  font-weight: 600;
  color: var(--tl-accent);
  background: #e8f1fa;
  border-radius: 999px;
  padding: 2px 8px;
  margin-top: 4px;
}

.tls-03__rail {
  position: relative;
  display: grid;
  justify-items: center;
}

.tls-03__rail::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: -16px;
  width: 2px;
  background: var(--tl-line);
}

.tls-03__item:last-child .tls-03__rail::before {
  bottom: auto;
  height: 8px;
}

.tls-03__dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid var(--tl-mut);
  margin-top: 5px;
  position: relative;
  z-index: 1;
}

.tls-03__item[aria-current="true"] .tls-03__dot {
  border-color: var(--tl-accent);
  box-shadow: 0 0 0 4px #e8f1fa;
}

.tls-03__role {
  font-size: 15.5px;
  font-weight: 700;
  color: var(--tl-ink);
}

.tls-03__org {
  font-size: 13px;
  color: var(--tl-mut);
  margin-top: 2px;
}

.tls-03__pts {
  margin: 8px 0 0 18px;
  display: grid;
  gap: 4px;
}

.tls-03__pts li {
  font-size: 13.5px;
  line-height: 1.5;
  color: #3a444d;
  text-wrap: pretty;
}

@container (max-width: 520px) {
  .tls-03__list {
    grid-template-columns: 24px 1fr;
  }

  .tls-03__when {
    grid-column: 2;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: baseline;
    gap: 6px;
    order: -1;
    margin-bottom: 6px;
  }

  .tls-03__item {
    grid-template-columns: subgrid;
    grid-template-rows: auto auto;
  }

  .tls-03__rail {
    grid-row: 1 / 3;
  }

  .tls-03__body {
    grid-column: 2;
  }
}

@supports not (grid-template-columns: subgrid) {
  .tls-03__item {
    grid-template-columns: 13ch 24px 1fr;
  }
}
```

## JavaScript
```js
/* No JavaScript — subgrid snaps every entry's date, rail and content to three shared tracks; a container query collapses to one column inside narrow parents. */
```
