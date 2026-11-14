---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-editorial-tabloid-bento-layout/"
title: "CSS Editorial Tabloid Bento Layout"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "A newsprint-inspired magazine-cover bento with a real masthead, display-poster headline, in-this-issue table of contents, pull-quote ribbon, and section…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Editorial Tabloid Bento Layout
Source: https://codefronts.com/layouts/css-card-grid-layout/css-editorial-tabloid-bento-layout/

A newsprint-inspired magazine-cover bento with a real masthead, display-poster headline, in-this-issue table of contents, pull-quote ribbon, and section pills — every tile carries a real editorial role (Editorial, Interview, Read Next) so the layout reads as an actual magazine spread, not a colorful dashboard.
## HTML
```html
<div class="cg-08">

  <div class="cg-08__bento">

    <!-- Magazine masthead strip -->
    <div class="cg-08__masthead">
      <span class="cg-08__nameplate">THE BRUTALIST</span>
      <span class="cg-08__metarow">
        <span>VOL. 07</span>
        <span class="cg-08__dot">●</span>
        <span>SUMMER 2026</span>
        <span class="cg-08__dot">●</span>
        <span>ISSUE 04</span>
        <span class="cg-08__dot">●</span>
        <span>$12</span>
      </span>
    </div>

    <!-- Display-poster headline (left) + In This Issue TOC (right) -->
    <div class="cg-08__headline">
      <span class="cg-08__kicker">The cover story</span>
      <h2 class="cg-08__display">Brutalist<br><span class="cg-08__display--accent">Web</span></h2>
      <span class="cg-08__byline">Field notes from designers building louder, slower, and on purpose.</span>
    </div>

    <div class="cg-08__toc">
      <div class="cg-08__tochead">
        <span>In this issue</span>
        <span class="cg-08__tocnum">04 / pieces</span>
      </div>
      <ol class="cg-08__toclist">
        <li><span class="cg-08__tocidx">01</span><span class="cg-08__toctitle">The Brutalist Web</span><span class="cg-08__tocpage">p.12</span></li>
        <li><span class="cg-08__tocidx">02</span><span class="cg-08__toctitle">Whitespace as protest</span><span class="cg-08__tocpage">p.24</span></li>
        <li><span class="cg-08__tocidx">03</span><span class="cg-08__toctitle">Field notes from the type foundry</span><span class="cg-08__tocpage">p.38</span></li>
        <li><span class="cg-08__tocidx">04</span><span class="cg-08__toctitle">Interview with Massimo Vignelli</span><span class="cg-08__tocpage">p.52</span></li>
      </ol>
    </div>

    <!-- Pull-quote ribbon (full width) -->
    <div class="cg-08__pullquote">
      <span class="cg-08__quote-glyph">"</span>
      <blockquote>
        Whitespace is a design choice. <em>Not a bug.</em>
      </blockquote>
      <span class="cg-08__quote-src">— Editorial, p. 24</span>
    </div>

    <!-- Bottom strip: 3 section tiles, each a different "page" -->
    <div class="cg-08__strip">
      <article class="cg-08__section cg-08__section--editorial">
        <span class="cg-08__pill">Editorial</span>
        <h3 class="cg-08__sectitle">Long Reads</h3>
        <p class="cg-08__secexc">Six essays on quiet design, by writers who'd rather you stayed.</p>
        <span class="cg-08__secpage">p.12</span>
      </article>
      <article class="cg-08__section cg-08__section--interview">
        <span class="cg-08__pill">Interview</span>
        <h3 class="cg-08__sectitle">Massimo Vignelli</h3>
        <p class="cg-08__secexc">"If you can design one thing, you can design everything." A conversation.</p>
        <span class="cg-08__secpage">p.24</span>
      </article>
      <article class="cg-08__section cg-08__section--read">
        <span class="cg-08__pill cg-08__pill--ink">Read Next</span>
        <h3 class="cg-08__sectitle">The Slow Web Manifesto</h3>
        <p class="cg-08__secexc">Why the best sites in 2026 load in 3 seconds — on purpose.</p>
        <span class="cg-08__secpage">p.38 →</span>
      </article>
    </div>

  </div>
</div>
```
## CSS
```css
.cg-08,
.cg-08 *,
.cg-08 *::before,
.cg-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-08 ::selection {
  background: #1a1410;
  color: #f1ece0;
}

.cg-08 {
  --paper: #f1ece0;
  --ink: #1a1410;
  --accent: #c93a4a;
  --rule: #1a1410;
  --serif: Georgia,"Times New Roman",serif;
  min-height: 100vh;
  padding: clamp(28px,3vw,48px);
  background: repeating-linear-gradient(0deg,rgba(26,20,16,.025) 0 1px,transparent 1px 3px), var(--paper);
  font-family: -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",sans-serif;
  color: var(--ink);
  display: flex;
  align-items: center;
  justify-content: center;
}

.cg-08__bento {
  width: 100%;
  max-width: 1100px;
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-auto-rows: auto;
  gap: 0;
  border: 2px solid var(--ink);
  border-radius: 4px;
  overflow: hidden;
  background: var(--paper);
}
/* MASTHEAD — top strip */

.cg-08__masthead {
  grid-column: 1 / -1;
  background: var(--ink);
  color: var(--paper);
  padding: clamp(12px,1.4vw,18px) clamp(18px,2.2vw,28px);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  border-bottom: 2px solid var(--ink);
}

.cg-08__nameplate {
  font-family: var(--serif);
  font-weight: 900;
  font-style: italic;
  font-size: clamp(1.1rem,1.8vw,1.6rem);
  letter-spacing: .01em;
  line-height: 1;
}

.cg-08__metarow {
  display: flex;
  align-items: center;
  gap: clamp(6px,1vw,12px);
  font-size: clamp(.62rem,.85vw,.74rem);
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  font-feature-settings: "tnum";
}

.cg-08__dot {
  opacity: .55;
  font-size: .6em;
}
/* HEADLINE — display-poster left side */

.cg-08__headline {
  grid-column: 1 / span 8;
  padding: clamp(28px,3.4vw,48px) clamp(28px,3vw,40px);
  border-right: 1px solid var(--ink);
  border-bottom: 1px solid var(--ink);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 14px;
}

.cg-08__kicker {
  font-size: clamp(.66rem,.95vw,.78rem);
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--accent);
}

.cg-08__display {
  font-family: var(--serif);
  font-weight: 900;
  font-size: clamp(2.8rem,6.6vw,6rem);
  line-height: .88;
  letter-spacing: -.035em;
  color: var(--ink);
}

.cg-08__display--accent {
  color: var(--accent);
  font-style: italic;
}

.cg-08__byline {
  font-size: clamp(.82rem,1.05vw,.96rem);
  color: rgba(26,20,16,.7);
  line-height: 1.5;
  max-width: 38ch;
  font-family: var(--serif);
  font-style: italic;
}
/* TOC — In This Issue right side */

.cg-08__toc {
  grid-column: 9 / span 4;
  padding: clamp(22px,2.4vw,32px) clamp(22px,2.4vw,28px);
  border-bottom: 1px solid var(--ink);
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: rgba(26,20,16,.025);
}

.cg-08__tochead {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  padding-bottom: 10px;
  border-bottom: 2px solid var(--ink);
}

.cg-08__tochead > span:first-child {
  font-family: var(--serif);
  font-weight: 900;
  font-style: italic;
  font-size: clamp(.95rem,1.3vw,1.15rem);
}

.cg-08__tocnum {
  font-size: .62rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  opacity: .65;
}

.cg-08__toclist {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.cg-08__toclist li {
  display: flex;
  align-items: baseline;
  gap: 8px;
  padding: 10px 0;
  border-bottom: 1px dashed rgba(26,20,16,.25);
}

.cg-08__toclist li:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.cg-08__tocidx {
  font-family: var(--serif);
  font-weight: 900;
  font-size: .88rem;
  color: var(--accent);
  min-width: 1.6em;
}

.cg-08__toctitle {
  flex: 1;
  font-size: clamp(.74rem,.92vw,.86rem);
  font-weight: 500;
  line-height: 1.3;
  color: var(--ink);
}

.cg-08__tocpage {
  font-size: .72rem;
  font-weight: 700;
  font-feature-settings: "tnum";
  letter-spacing: .04em;
  color: rgba(26,20,16,.6);
}
/* PULL-QUOTE RIBBON — full width */

.cg-08__pullquote {
  grid-column: 1 / -1;
  position: relative;
  padding: clamp(24px,3vw,40px) clamp(28px,3.4vw,56px);
  border-bottom: 1px solid var(--ink);
  background: var(--paper);
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.cg-08__quote-glyph {
  position: absolute;
  top: -10px;
  left: clamp(12px,1.6vw,24px);
  font-family: var(--serif);
  font-size: clamp(6rem,12vw,10rem);
  font-weight: 900;
  color: var(--accent);
  opacity: .16;
  line-height: 1;
  pointer-events: none;
}

.cg-08__pullquote blockquote {
  font-family: var(--serif);
  font-size: clamp(1.15rem,2.2vw,1.7rem);
  font-weight: 600;
  line-height: 1.32;
  color: var(--ink);
  letter-spacing: -.005em;
  max-width: 32ch;
  position: relative;
  z-index: 1;
}

.cg-08__pullquote blockquote em {
  font-style: italic;
  color: var(--accent);
}

.cg-08__quote-src {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: rgba(26,20,16,.55);
}
/* BOTTOM STRIP — 3 section tiles */

.cg-08__strip {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 0;
}

.cg-08__section {
  padding: clamp(20px,2.4vw,28px);
  border-right: 1px solid var(--ink);
  display: flex;
  flex-direction: column;
  gap: 10px;
  position: relative;
  min-height: clamp(180px,18vw,220px);
}

.cg-08__section:last-child {
  border-right: none;
}

.cg-08__section--read {
  background: var(--ink);
  color: var(--paper);
}

.cg-08__pill {
  align-self: flex-start;
  font-size: .62rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  background: var(--ink);
  color: var(--paper);
  padding: 5px 10px 4px;
  border-radius: 2px;
  font-feature-settings: "tnum";
}

.cg-08__pill--ink {
  background: var(--accent);
  color: var(--paper);
}

.cg-08__sectitle {
  font-family: var(--serif);
  font-size: clamp(1.05rem,1.6vw,1.35rem);
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -.015em;
}

.cg-08__section--read .cg-08__sectitle {
  color: var(--paper);
}

.cg-08__secexc {
  font-size: clamp(.76rem,.95vw,.88rem);
  line-height: 1.45;
  color: rgba(26,20,16,.72);
  max-width: 32ch;
}

.cg-08__section--read .cg-08__secexc {
  color: rgba(241,236,224,.78);
}

.cg-08__secpage {
  margin-top: auto;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: rgba(26,20,16,.5);
  padding-top: 8px;
  font-feature-settings: "tnum";
}

.cg-08__section--read .cg-08__secpage {
  color: var(--accent);
}
/* TABLET — 900px and below */

@media (max-width: 900px) {
  .cg-08__headline {
    grid-column: 1 / span 7;
  }

  .cg-08__toc {
    grid-column: 8 / span 5;
  }

  .cg-08__display {
    font-size: clamp(2.4rem,7vw,4rem);
  }
}
/* SMALL TABLET — 720px and below: stack headline + TOC, keep strip 3-col */

@media (max-width: 720px) {
  .cg-08__masthead {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }

  .cg-08__headline {
    grid-column: 1 / -1;
    border-right: none;
  }

  .cg-08__toc {
    grid-column: 1 / -1;
    border-top: 1px solid var(--ink);
  }

  .cg-08__strip {
    grid-template-columns: 1fr 1fr;
  }

  .cg-08__section {
    border-right: 1px solid var(--ink);
    border-bottom: 1px solid var(--ink);
  }

  .cg-08__section:nth-child(2) {
    border-right: none;
  }

  .cg-08__section:last-child {
    grid-column: 1 / -1;
    border-bottom: none;
  }
}
/* MOBILE — 480px and below */

@media (max-width: 480px) {
  .cg-08 {
    padding: 20px 16px;
  }

  .cg-08__masthead {
    padding: 14px 18px;
  }

  .cg-08__display {
    font-size: clamp(2rem,9vw,3rem);
  }

  .cg-08__strip {
    grid-template-columns: 1fr;
  }

  .cg-08__section {
    border-right: none !important;
    border-bottom: 1px solid var(--ink) !important;
  }

  .cg-08__section:last-child {
    border-bottom: none !important;
  }

  .cg-08__metarow {
    font-size: .58rem;
    letter-spacing: .12em;
    gap: 6px;
    flex-wrap: wrap;
  }

  .cg-08__quote-glyph {
    font-size: 5rem;
    top: -6px;
  }
}
```
