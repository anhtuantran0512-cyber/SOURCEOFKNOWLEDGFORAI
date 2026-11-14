---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/editorial-spine/"
title: "Editorial History Timeline — Sticky Era Headers in Serif"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "The museum-catalog treatment: decades of history grouped under enormous serif year headings that STICK to the top while their era's events scroll past, then…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Editorial History Timeline — Sticky Era Headers in Serif
Source: https://codefronts.com/layouts/css-timelines/editorial-spine/

The museum-catalog treatment: decades of history grouped under enormous serif year headings that STICK to the top while their era's events scroll past, then hand off to the next era with a gentle push — position:sticky choreography that makes long histories navigable without a single script, styled like a broadsheet retrospective.
## HTML
```html
<section class="tls-28" aria-label="Editorial history timeline demo">
  <div class="tls-28__paper">
    <header class="tls-28__masthead">
      <p class="tls-28__kicker">A brief history of</p>
      <h3 class="tls-28__title">The Personal Computer</h3>
    </header>
    <ol class="tls-28__eras" role="list">
      <li>
        <section class="tls-28__era" id="tls20-1970s">
          <header class="tls-28__stick"><h4 class="tls-28__year">1970s</h4><p class="tls-28__tag">The hobbyists</p></header>
          <ul class="tls-28__events" role="list">
            <li class="tls-28__ev"><time datetime="1975-01">Jan 1975</time><p>The Altair 8800 appears on a magazine cover and sells thousands to people who must assemble it themselves — and love it.</p></li>
            <li class="tls-28__ev"><time datetime="1977-06">Jun 1977</time><p>The Apple II, PET 2001 and TRS-80 arrive within months of each other. The 'trinity' makes computers appliances.</p></li>
          </ul>
        </section>
      </li>
      <li>
        <section class="tls-28__era" id="tls20-1980s">
          <header class="tls-28__stick"><h4 class="tls-28__year">1980s</h4><p class="tls-28__tag">The office lands</p></header>
          <ul class="tls-28__events" role="list">
            <li class="tls-28__ev"><time datetime="1981-08">Aug 1981</time><p>IBM ships the 5150 PC. 'Nobody ever got fired for buying IBM' becomes a purchasing department proverb.</p></li>
            <li class="tls-28__ev"><time datetime="1984-01">Jan 1984</time><p>The Macintosh introduces the mouse and the metaphor of the desktop to a Super Bowl audience.</p></li>
            <li class="tls-28__ev"><time datetime="1985-11">Nov 1985</time><p>Windows 1.0 ships — tiled windows only, because overlapping ones were considered confusing.</p></li>
          </ul>
        </section>
      </li>
      <li>
        <section class="tls-28__era" id="tls20-1990s">
          <header class="tls-28__stick"><h4 class="tls-28__year">1990s</h4><p class="tls-28__tag">The network arrives</p></header>
          <ul class="tls-28__events" role="list">
            <li class="tls-28__ev"><time datetime="1991-08">Aug 1991</time><p>The first website goes live at CERN, explaining what a website is.</p></li>
            <li class="tls-28__ev"><time datetime="1995-08">Aug 1995</time><p>Windows 95 launches with a Rolling Stones soundtrack and midnight store queues.</p></li>
            <li class="tls-28__ev"><time datetime="1998-09">Sep 1998</time><p>Google incorporates in a Menlo Park garage, indexing 25 million pages.</p></li>
          </ul>
        </section>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
.tls-28,
.tls-28 *,
.tls-28 *::before,
.tls-28 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-28 {
  min-height: 100vh;
  width: 100%;
  --tl-paper: #f7f4ee;
  --tl-ink: #211d16;
  --tl-mut: #75705f;
  --tl-rule: #dcd6c8;
  --tl-accent: #8c2f1b;
  font-family: Georgia,'Times New Roman',serif;
  background: var(--tl-paper);
  padding: 64px 24px;
  display: grid;
  place-items: center;
}

.tls-28__paper {
  width: min(640px,100%);
}

.tls-28__masthead {
  text-align: center;
  border-block: 3px double var(--tl-ink);
  padding: 22px 0;
  margin-bottom: 8px;
}

.tls-28__kicker {
  font-size: 12px;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: var(--tl-mut);
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-weight: 600;
}

.tls-28__title {
  font-size: clamp(26px,4.5vw,38px);
  font-weight: 700;
  color: var(--tl-ink);
  letter-spacing: -.01em;
  margin-top: 6px;
}

.tls-28__eras {
  list-style: none;
}

.tls-28__stick {
  position: sticky;
  top: 0;
  z-index: 2;
  background: var(--tl-paper);
  display: flex;
  align-items: baseline;
  gap: 16px;
  padding: 18px 0 12px;
  border-bottom: 1px solid var(--tl-rule);
}

.tls-28__year {
  font-size: clamp(48px,9vw,84px);
  font-weight: 700;
  line-height: .9;
  color: var(--tl-ink);
  letter-spacing: -.04em;
}

.tls-28__tag {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--tl-accent);
}

.tls-28__events {
  list-style: none;
  padding: 26px 0 56px;
}

.tls-28__ev {
  display: grid;
  grid-template-columns: 96px 1fr;
  gap: 18px;
  padding: 16px 0;
  border-bottom: 1px dotted var(--tl-rule);
}

.tls-28__ev:last-child {
  border-bottom: none;
}

.tls-28__ev time {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--tl-mut);
  padding-top: 4px;
}

.tls-28__ev p {
  font-size: 16px;
  line-height: 1.65;
  color: var(--tl-ink);
  text-wrap: pretty;
}

@media (max-width: 520px) {
  .tls-28__ev {
    grid-template-columns: 1fr;
    gap: 4px;
  }
}
```

## JavaScript
```js
/* No JavaScript — era headers are position:sticky; each section's boundary pushes the previous header off naturally. The opaque sticky background prevents text ghosting. */
```
