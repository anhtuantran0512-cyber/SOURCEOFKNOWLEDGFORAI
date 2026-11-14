---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/sticky-shrinking-navbar-css/"
title: "Sticky Shrinking Navbar CSS"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "A header that spends its first 160px of scroll gracefully slimming down — padding tightens, the wordmark shrinks, a background and shadow fade in — driven…"
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Shrinking Navbar CSS
Source: https://codefronts.com/layouts/css-sticky-elements/sticky-shrinking-navbar-css/

A header that spends its first 160px of scroll gracefully slimming down — padding tightens, the wordmark shrinks, a background and shadow fade in — driven entirely by animation-timeline: scroll(). The scrubbing is done by the compositor, not a scroll event handler, so it stays butter-smooth on a mid-range phone, and it reverses perfectly when you scroll back up. Browsers without scroll-driven animations get the compact header from the start.
## HTML
```html
<section class="cst-03" aria-label="Sticky shrinking navbar demo">
  <div class="cst-03__stage" id="cst03-top">
    <header class="cst-03__bar">
      <a class="cst-03__logo" href="#cst03-top">Interval<span>27</span></a>
      <nav class="cst-03__nav" aria-label="Primary">
        <a href="#cst03-speakers">Speakers</a>
        <a href="#cst03-schedule">Schedule</a>
        <a href="#cst03-tickets">Tickets</a>
      </nav>
      <a class="cst-03__cta" href="#cst03-tickets">Get a seat</a>
    </header>
    <section class="cst-03__hero">
      <p class="cst-03__date">14–16 Oct 2027 · Meat Market, Melbourne</p>
      <h1>A conference<br>about interfaces<br>that behave.</h1>
      <p class="cst-03__sub">Watch the header while you scroll: over the first 160px it tightens its padding, shrinks the wordmark and grows a shadow — one CSS keyframe scrubbed by <code>animation-timeline: scroll()</code>. Zero JavaScript.</p>
      <div class="cst-03__meter" aria-hidden="true"><span>0px</span><i></i><span>160px — fully shrunk</span></div>
    </section>
    <section class="cst-03__band" id="cst03-speakers">
      <h2>Speakers</h2>
      <div class="cst-03__people">
        <a href="#cst03-s1" style="--img:url('https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=800&auto=format&fit=crop');--a:oklch(0.8 0.08 50);--b:oklch(0.55 0.12 30)"><figure></figure><h3>Ada Whitmore</h3><p>Scroll-driven UI, Google</p></a>
        <a href="#cst03-s2" style="--img:url('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=800&auto=format&fit=crop');--a:oklch(0.75 0.09 240);--b:oklch(0.5 0.1 265)"><figure></figure><h3>Dele Okafor</h3><p>Design engineering, Linear</p></a>
        <a href="#cst03-s3" style="--img:url('https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=800&auto=format&fit=crop');--a:oklch(0.82 0.07 150);--b:oklch(0.55 0.1 180)"><figure></figure><h3>June Park</h3><p>Motion systems, Stripe</p></a>
        <a href="#cst03-s4" style="--img:url('https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=800&auto=format&fit=crop');--a:oklch(0.78 0.1 320);--b:oklch(0.5 0.12 345)"><figure></figure><h3>Theo Brandt</h3><p>Accessibility, BBC</p></a>
      </div>
    </section>
    <section class="cst-03__band cst-03__band--tint" id="cst03-schedule">
      <h2>Day one</h2>
      <ol class="cst-03__sched">
        <li><time>09:30</time><div><h3>Interfaces that respect the thumb</h3><p>Opening keynote — Ada Whitmore</p></div><span>Main hall</span></li>
        <li><time>11:00</time><div><h3>The death of the scroll listener</h3><p>Scroll-state queries &amp; scroll-driven animation in production</p></div><span>Main hall</span></li>
        <li><time>13:30</time><div><h3>Sticky, snapped, stuck</h3><p>Workshop — bring a laptop, leave with a design system</p></div><span>Studio B</span></li>
        <li><time>16:00</time><div><h3>Motion budgets &amp; reduced-motion</h3><p>Panel — Park, Brandt, Okafor</p></div><span>Main hall</span></li>
      </ol>
    </section>
    <section class="cst-03__tickets" id="cst03-tickets">
      <h2>Tickets</h2>
      <div class="cst-03__tix">
        <article><h3>Online</h3><p class="cst-03__price">A$180</p><p>Live streams + recordings</p><a href="#cst03-buy-online">Buy online pass</a></article>
        <article class="cst-03__tix--feat"><h3>In person</h3><p class="cst-03__price">A$740</p><p>Three days, all workshops, dinner</p><a href="#cst03-buy-person">Buy full pass</a></article>
        <article><h3>Student</h3><p class="cst-03__price">A$95</p><p>Valid ID at the door</p><a href="#cst03-buy-student">Buy student pass</a></article>
      </div>
    </section>
    <footer class="cst-03__footer"><p><strong>Interval 27</strong> — a demo from the CodeFronts sticky-elements collection.</p><a href="#cst03-top">Back to top ↑</a></footer>
  </div>
</section>
```
## CSS
```css
.cst-03,
.cst-03 *,
.cst-03 *::before,
.cst-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-03 {
  --bg: oklch(0.97 0.012 85);
  --ink: oklch(0.25 0.03 60);
  --mut: oklch(0.5 0.025 60);
  --line: oklch(0.88 0.02 80);
  --acc: oklch(0.6 0.19 35);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-03__stage {
  width: 100%;
  container: cst03/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
  scroll-padding-top: 86px;
  scroll-behavior: smooth;
}

.cst-03__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: clamp(14px,3cqi,28px);
  padding: 20px clamp(18px,4cqi,42px);
  border-bottom: 1px solid transparent;
  animation: cst03-shrink linear both;
  animation-timeline: scroll(nearest);
  animation-range: 0 160px;
}

.cst-03__logo {
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -.04em;
  color: inherit;
  text-decoration: none;
  animation: cst03-logo linear both;
  animation-timeline: scroll(nearest);
  animation-range: 0 160px;
}

.cst-03__logo span {
  color: var(--acc);
}

@keyframes cst03-shrink {
  to {
    padding-block: 9px;
    background: color-mix(in oklch,var(--bg) 88%,transparent);
    -webkit-backdrop-filter: blur(10px);
    backdrop-filter: blur(10px);
    border-color: var(--line);
    box-shadow: 0 10px 30px oklch(0.3 0.05 50/.08);
  }
}

@keyframes cst03-logo {
  to {
    font-size: 17px;
  }
}

@supports not (animation-timeline: scroll()) {
  .cst-03__bar {
    padding-block: 9px;
    background: color-mix(in oklch,var(--bg) 88%,transparent);
    -webkit-backdrop-filter: blur(10px);
    backdrop-filter: blur(10px);
    border-color: var(--line);
  }

  .cst-03__logo {
    font-size: 19px;
  }
}

.cst-03__nav {
  display: flex;
  gap: 2px;
  margin-inline: auto;
}

.cst-03__nav a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 13px;
  border-radius: 10px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: color .2s,background .2s;
}

.cst-03__nav a:hover,
.cst-03__nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.91 0.02 80);
}

.cst-03__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cst-03__cta {
  display: grid;
  place-items: center;
  min-height: 40px;
  padding: 0 17px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  color: oklch(0.98 0.01 85);
  background: var(--ink);
  transition: background .2s,translate .2s;
}

.cst-03__cta:hover,
.cst-03__cta:focus-visible {
  background: var(--acc);
  translate: 0 -1px;
}

.cst-03__cta:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-03__hero {
  min-height: calc(100svh - 86px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 40px clamp(18px,5cqi,48px) 56px;
}

.cst-03__date {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 16px;
}

.cst-03__hero h1 {
  font-size: clamp(42px,9.5cqi,104px);
  line-height: .95;
  letter-spacing: -.045em;
  font-weight: 800;
}

.cst-03__sub {
  margin-top: 22px;
  max-width: 56ch;
  font-size: 15.5px;
  line-height: 1.65;
  color: var(--mut);
}

.cst-03__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .87em;
  background: oklch(0.9 0.02 80);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--ink);
}

.cst-03__meter {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 30px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .08em;
  color: var(--mut);
}

.cst-03__meter i {
  flex: 0 1 220px;
  height: 4px;
  border-radius: 99px;
  background: linear-gradient(to right,var(--acc),oklch(0.75 0.12 60));
}

.cst-03__band {
  padding: clamp(44px,8cqi,84px) clamp(18px,5cqi,48px);
}

.cst-03__band h2,
.cst-03__tickets h2 {
  font-size: clamp(26px,4.5cqi,40px);
  letter-spacing: -.03em;
  font-weight: 800;
  margin-bottom: 24px;
}

.cst-03__band--tint {
  background: oklch(0.93 0.02 85);
}

.cst-03__people {
  display: grid;
  gap: 16px;
  grid-template-columns: repeat(auto-fit,minmax(min(190px,100%),1fr));
}

.cst-03__people a {
  text-decoration: none;
  color: inherit;
  border-radius: 16px;
  padding: 10px 10px 14px;
  background: oklch(1 0 0/.55);
  border: 1px solid var(--line);
  transition: translate .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s;
}

.cst-03__people a:hover,
.cst-03__people a:focus-visible {
  translate: 0 -3px;
  box-shadow: 0 14px 30px oklch(0.35 0.05 50/.1);
}

.cst-03__people a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-03__people figure {
  aspect-ratio: 1;
  border-radius: 11px;
  background-image: var(--img,none),linear-gradient(150deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
  filter: saturate(.9);
}

.cst-03__people h3 {
  font-size: 15px;
  margin: 12px 4px 2px;
  letter-spacing: -.01em;
}

.cst-03__people p {
  font-size: 12px;
  color: var(--mut);
  margin: 0 4px;
}

.cst-03__sched {
  list-style: none;
  display: grid;
  gap: 2px;
}

.cst-03__sched li {
  display: flex;
  align-items: center;
  gap: clamp(12px,3cqi,26px);
  padding: 16px 14px;
  border-radius: 14px;
  transition: background .2s;
}

.cst-03__sched li:hover {
  background: oklch(1 0 0/.6);
}

.cst-03__sched time {
  flex: none;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 13px;
  font-weight: 700;
  color: var(--acc);
  width: 52px;
}

.cst-03__sched h3 {
  font-size: 15.5px;
  letter-spacing: -.01em;
}

.cst-03__sched div p {
  font-size: 12.5px;
  color: var(--mut);
  margin-top: 2px;
}

.cst-03__sched li>span {
  margin-left: auto;
  flex: none;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  padding: 4px 9px;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--mut);
}

.cst-03__tickets {
  padding: clamp(44px,8cqi,84px) clamp(18px,5cqi,48px) clamp(50px,9cqi,92px);
}

.cst-03__tix {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fit,minmax(min(210px,100%),1fr));
  align-items: stretch;
}

.cst-03__tix article {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 24px 22px;
  border-radius: 18px;
  background: oklch(1 0 0/.6);
  border: 1px solid var(--line);
}

.cst-03__tix--feat {
  background: var(--ink);
  color: oklch(0.97 0.012 85);
  border-color: var(--ink);
}

.cst-03__tix--feat p {
  color: oklch(0.8 0.02 80);
}

.cst-03__tix h3 {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
}

.cst-03__price {
  font-size: 34px;
  font-weight: 800;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.cst-03__tix article p:not(.cst-03__price) {
  font-size: 12.5px;
  color: var(--mut);
}

.cst-03__tix a {
  display: grid;
  place-items: center;
  min-height: 44px;
  margin-top: 14px;
  border-radius: 11px;
  font-size: 13.5px;
  font-weight: 700;
  text-decoration: none;
  color: var(--ink);
  border: 1.5px solid var(--line);
  transition: border-color .2s,background .2s,color .2s;
}

.cst-03__tix a:hover,
.cst-03__tix a:focus-visible {
  border-color: var(--acc);
  color: var(--acc);
}

.cst-03__tix--feat a {
  color: var(--ink);
  background: oklch(0.97 0.012 85);
  border-color: transparent;
}

.cst-03__tix--feat a:hover,
.cst-03__tix--feat a:focus-visible {
  background: var(--acc);
  color: oklch(0.98 0 0);
}

.cst-03__tix a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-03__footer {
  display: flex;
  flex-wrap: wrap;
  gap: 14px 26px;
  align-items: center;
  justify-content: space-between;
  padding: 28px clamp(18px,5cqi,48px) 38px;
  border-top: 1px solid var(--line);
}

.cst-03__footer p {
  font-size: 12.5px;
  color: var(--mut);
}

.cst-03__footer a {
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

.cst-03__footer a:hover,
.cst-03__footer a:focus-visible {
  border-color: var(--acc);
}

.cst-03__footer a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

@container cst03 (width < 560px) {
  .cst-03__nav {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-03__stage {
    scroll-behavior: auto;
  }

  .cst-03__bar,
    .cst-03__logo {
    animation: none;
    padding-block: 12px;
  }

  .cst-03__logo {
    font-size: 19px;
    padding-block: 0;
  }

  .cst-03__bar {
    background: color-mix(in oklch,var(--bg) 88%,transparent);
    border-color: var(--line);
  }

  .cst-03 * {
    transition-duration: .01ms !important;
  }
}
```
