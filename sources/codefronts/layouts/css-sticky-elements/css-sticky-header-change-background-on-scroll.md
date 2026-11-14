---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-sticky-header-change-background-on-scroll/"
title: "CSS Sticky Header Change Background on Scroll"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The transparent-over-the-hero header that turns solid the instant it pins — with zero JavaScript."
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Header Change Background on Scroll
Source: https://codefronts.com/layouts/css-sticky-elements/css-sticky-header-change-background-on-scroll/

The transparent-over-the-hero header that turns solid the instant it pins — with zero JavaScript. The 2026 way is a scroll-state container query: the sticky header declares container-type: scroll-state, and @container scroll-state(stuck: top) restyles its contents the exact frame the browser pins it. No scroll listeners, no thresholds to tune, no main-thread work — and a translucent-glass fallback keeps it readable in browsers that haven't shipped the query yet.
## HTML
```html
<section class="cst-02" aria-label="Sticky header changing background on scroll demo">
  <div class="cst-02__stage" id="cst02-top">
    <header class="cst-02__pin">
      <nav class="cst-02__bar" aria-label="Primary">
        <a class="cst-02__brand" href="#cst02-top"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M3 19 10 5l4 8 2.5-4L21 19Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>Alpenglow</a>
        <div class="cst-02__links">
          <a href="#cst02-trips">Trips</a>
          <a href="#cst02-ethos">Ethos</a>
          <a href="#cst02-journal">Journal</a>
        </div>
        <a class="cst-02__book" href="#cst02-trips">Book a trip</a>
      </nav>
    </header>
    <section class="cst-02__hero">
      <p class="cst-02__est">EST. 2011 · BANFF · CHAMONIX · QUEENSTOWN</p>
      <h1>Go where the road gives up.</h1>
      <p class="cst-02__sub">The nav starts transparent over this photo. Scroll one pixel: the moment it pins, <code>@container scroll-state(stuck: top)</code> turns it solid — no JavaScript, no scroll listener, no threshold to tune.</p>
      <a class="cst-02__cue" href="#cst02-trips">Find your route ↓</a>
    </section>
    <section class="cst-02__trips" id="cst02-trips">
      <header><h2>Seasons ahead</h2><p>Small groups, big weather. Six guests, two guides, no fixed itinerary.</p></header>
      <div class="cst-02__grid">
        <a href="#cst02-icefields" style="--img:url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=1200&auto=format&fit=crop');--a:oklch(0.75 0.08 240);--b:oklch(0.4 0.09 265)"><figure></figure><div><h3>Icefields Traverse</h3><p>Banff · 6 days · glacier travel</p><span>CA$3,400</span></div></a>
        <a href="#cst02-aiguilles" style="--img:url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1200&auto=format&fit=crop');--a:oklch(0.8 0.06 220);--b:oklch(0.45 0.08 250)"><figure></figure><div><h3>Aiguilles Rouges</h3><p>Chamonix · 4 days · alpine ridges</p><span>€2,150</span></div></a>
        <a href="#cst02-ridgeline" style="--img:url('https://images.unsplash.com/photo-1469474968028-56623f02e42e?q=80&w=1200&auto=format&fit=crop');--a:oklch(0.78 0.1 60);--b:oklch(0.45 0.1 35)"><figure></figure><div><h3>Remarkables Ridgeline</h3><p>Queenstown · 3 days · scrambling</p><span>NZ$1,850</span></div></a>
      </div>
    </section>
    <section class="cst-02__ethos" id="cst02-ethos">
      <blockquote>
        <p>“We pack out everything, hire local, and cap groups at six. The mountains were fine before us; the goal is that they never notice we came.”</p>
        <cite>— Mara Voss, founding guide</cite>
      </blockquote>
    </section>
    <footer class="cst-02__footer" id="cst02-journal">
      <p><strong>Alpenglow Expeditions</strong> — a demo from the CodeFronts sticky-elements collection.</p>
      <a href="#cst02-top">Back to top ↑</a>
    </footer>
  </div>
</section>
```
## CSS
```css
.cst-02,
.cst-02 *,
.cst-02 *::before,
.cst-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-02 {
  --bg: oklch(0.975 0.005 250);
  --ink: oklch(0.25 0.02 260);
  --mut: oklch(0.52 0.015 260);
  --line: oklch(0.9 0.01 250);
  --acc: oklch(0.62 0.14 230);
  --navH: 68px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-02__stage {
  width: 100%;
  container: cst02/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
  scroll-padding-top: calc(var(--navH) + 8px);
  scroll-behavior: smooth;
}

.cst-02__pin {
  position: sticky;
  top: 0;
  z-index: 10;
  container-type: scroll-state;
  margin-bottom: calc(-1 * var(--navH));
}

.cst-02__bar {
  height: var(--navH);
  display: flex;
  align-items: center;
  gap: clamp(14px,3cqi,28px);
  padding: 0 clamp(18px,4cqi,42px);
  color: oklch(0.99 0 0);
  background: color-mix(in oklch,oklch(0.2 0.02 260) 72%,transparent);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  transition: background .35s,color .35s,box-shadow .35s,backdrop-filter .35s;
}

.cst-02__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 16.5px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: inherit;
  text-decoration: none;
}

.cst-02__links {
  display: flex;
  gap: 2px;
  margin-inline: auto;
}

.cst-02__links a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 13px;
  border-radius: 9px;
  font-size: 13.5px;
  font-weight: 600;
  color: inherit;
  opacity: .82;
  text-decoration: none;
  transition: opacity .2s,background .2s;
}

.cst-02__links a:hover,
.cst-02__links a:focus-visible {
  opacity: 1;
  background: oklch(0.5 0.02 260/.18);
}

.cst-02__links a:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: -2px;
}

.cst-02__book {
  display: grid;
  place-items: center;
  min-height: 38px;
  padding: 0 16px;
  border-radius: 99px;
  border: 1.5px solid currentColor;
  font-size: 13px;
  font-weight: 700;
  color: inherit;
  text-decoration: none;
  transition: background .25s,color .25s,border-color .25s,translate .2s;
}

.cst-02__book:hover,
.cst-02__book:focus-visible {
  translate: 0 -1px;
}

.cst-02__book:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

@supports (container-type: scroll-state) {
  .cst-02__bar {
    background: linear-gradient(to bottom,oklch(0.1 0.02 260/.45),transparent);
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  @container scroll-state(stuck: top) {
    .cst-02__bar {
      background: color-mix(in oklch,var(--bg) 92%,transparent);
      color: var(--ink);
      -webkit-backdrop-filter: blur(12px);
      backdrop-filter: blur(12px);
      box-shadow: 0 1px 0 var(--line),0 12px 32px oklch(0.2 0.02 260/.08);
    }

    .cst-02__links a:hover,
        .cst-02__links a:focus-visible {
      background: oklch(0.9 0.015 250/.7);
    }

    .cst-02__book {
      background: var(--ink);
      border-color: var(--ink);
      color: oklch(0.98 0 0);
    }

    .cst-02__book:hover,
        .cst-02__book:focus-visible {
      background: var(--acc);
      border-color: var(--acc);
    }
  }
}

.cst-02__hero {
  position: relative;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: calc(var(--navH) + 30px) clamp(18px,5cqi,48px) clamp(40px,8cqi,72px);
  color: oklch(0.99 0 0);
  background-image: linear-gradient(to bottom,oklch(0.2 0.03 260/.35),transparent 34%,transparent 55%,oklch(0.15 0.03 260/.72)),var(--heroimg,none),linear-gradient(165deg,oklch(0.55 0.08 240),oklch(0.25 0.06 265));
  --heroimg: url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=1800&auto=format&fit=crop');
  background-size: cover;
  background-position: center;
}

.cst-02__est {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .2em;
  opacity: .85;
  margin-bottom: 14px;
}

.cst-02__hero h1 {
  font-size: clamp(40px,8.5cqi,84px);
  line-height: .98;
  letter-spacing: -.03em;
  font-weight: 800;
  max-width: 13ch;
  text-wrap: balance;
}

.cst-02__sub {
  margin-top: 16px;
  max-width: 52ch;
  font-size: 15px;
  line-height: 1.65;
  opacity: .92;
}

.cst-02__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .86em;
  background: oklch(1 0 0/.16);
  padding: 2px 6px;
  border-radius: 5px;
}

.cst-02__cue {
  display: inline-grid;
  place-items: center;
  width: fit-content;
  min-height: 46px;
  margin-top: 26px;
  padding: 0 20px;
  border-radius: 12px;
  background: oklch(0.99 0 0);
  color: oklch(0.25 0.03 260);
  font-size: 14px;
  font-weight: 700;
  text-decoration: none;
  transition: translate .2s,box-shadow .2s;
}

.cst-02__cue:hover,
.cst-02__cue:focus-visible {
  translate: 0 -2px;
  box-shadow: 0 10px 26px oklch(0.1 0.02 260/.35);
}

.cst-02__cue:focus-visible {
  outline: 2px solid oklch(0.99 0 0);
  outline-offset: 3px;
}

.cst-02__trips {
  padding: clamp(44px,8cqi,84px) clamp(18px,5cqi,48px);
}

.cst-02__trips header {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 8px 22px;
  margin-bottom: 26px;
}

.cst-02__trips h2 {
  font-size: clamp(26px,4.5cqi,40px);
  letter-spacing: -.025em;
  font-weight: 800;
}

.cst-02__trips header p {
  font-size: 13.5px;
  color: var(--mut);
}

.cst-02__grid {
  display: grid;
  gap: 16px;
  grid-template-columns: repeat(auto-fit,minmax(min(250px,100%),1fr));
}

.cst-02__grid a {
  border-radius: 18px;
  overflow: hidden;
  background: oklch(1 0 0);
  border: 1px solid var(--line);
  text-decoration: none;
  color: inherit;
  transition: translate .3s cubic-bezier(.2,.7,.2,1),box-shadow .3s;
}

.cst-02__grid a:hover,
.cst-02__grid a:focus-visible {
  translate: 0 -4px;
  box-shadow: 0 16px 38px oklch(0.25 0.03 260/.12);
}

.cst-02__grid a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-02__grid figure {
  aspect-ratio: 16/10;
  background-image: var(--img,none),linear-gradient(150deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
  transition: scale .5s cubic-bezier(.2,.7,.2,1);
}

.cst-02__grid a:hover figure {
  scale: 1.04;
}

.cst-02__grid div {
  display: grid;
  gap: 3px;
  padding: 16px 18px 18px;
}

.cst-02__grid h3 {
  font-size: 16.5px;
  letter-spacing: -.01em;
}

.cst-02__grid p {
  font-size: 12.5px;
  color: var(--mut);
}

.cst-02__grid span {
  margin-top: 8px;
  font-size: 13.5px;
  font-weight: 800;
  color: var(--acc);
}

.cst-02__ethos {
  padding: clamp(44px,9cqi,90px) clamp(18px,5cqi,48px);
  background: oklch(0.94 0.012 240);
}

.cst-02__ethos blockquote {
  max-width: 64ch;
  margin-inline: auto;
  text-align: center;
}

.cst-02__ethos p {
  font-size: clamp(19px,3cqi,26px);
  line-height: 1.45;
  letter-spacing: -.01em;
  font-weight: 600;
  text-wrap: balance;
}

.cst-02__ethos cite {
  display: block;
  margin-top: 16px;
  font-style: normal;
  font-size: 13px;
  color: var(--mut);
}

.cst-02__footer {
  display: flex;
  flex-wrap: wrap;
  gap: 14px 26px;
  align-items: center;
  justify-content: space-between;
  padding: 30px clamp(18px,5cqi,48px) 40px;
}

.cst-02__footer p {
  font-size: 12.5px;
  color: var(--mut);
  max-width: 52ch;
}

.cst-02__footer a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 700;
  color: var(--ink);
  text-decoration: none;
  border: 1.5px solid var(--line);
  transition: border-color .2s;
}

.cst-02__footer a:hover,
.cst-02__footer a:focus-visible {
  border-color: var(--acc);
}

.cst-02__footer a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

@container cst02 (width < 560px) {
  .cst-02__links {
    display: none;
  }

  .cst-02__bar {
    gap: 12px;
    justify-content: space-between;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-02__stage {
    scroll-behavior: auto;
  }

  .cst-02 * {
    transition-duration: .01ms !important;
    scale: none !important;
  }
}
```
