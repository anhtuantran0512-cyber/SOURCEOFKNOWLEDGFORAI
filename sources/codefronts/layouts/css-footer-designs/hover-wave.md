---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/hover-wave/"
title: "CSS Animated SVG Wave Footer"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "The wave divider done so it actually loops: one SVG path drawn twice its width with a seamless repeat, translated by exactly 50% so the animation has no…"
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated SVG Wave Footer
Source: https://codefronts.com/layouts/css-footer-designs/hover-wave/

The wave divider done so it actually loops: one SVG path drawn twice its width with a seamless repeat, translated by exactly 50% so the animation has no visible seam, layered three deep at different speeds and opacities for parallax. Responsive at any width because preserveAspectRatio is set to slice.
## HTML
```html
<section class="ft-25" aria-label="Animated SVG wave footer demo">
  <main class="ft-25__main">
    <p class="ft-25__eyebrow">Seamless tiling path · translateX(-50%)</p>
    <h1 class="ft-25__title">A wave that loops without a seam</h1>
    <p class="ft-25__sub">One period drawn twice, moved by exactly half its width. Three layers at 14s, 21s and 30s give the parallax — and every one of them animates only a transform.</p>
  </main>
  <footer class="ft-25__foot">
    <div class="ft-25__waves" aria-hidden="true">
      <svg class="ft-25__wave ft-25__wave--back" viewBox="0 0 2400 180" preserveAspectRatio="none" focusable="false"><path d="M0,96 C300,150 600,30 1200,96 C1800,162 2100,42 2400,96 L2400,180 L0,180 Z"/></svg>
      <svg class="ft-25__wave ft-25__wave--mid" viewBox="0 0 2400 180" preserveAspectRatio="none" focusable="false"><path d="M0,110 C400,50 800,160 1200,110 C1600,60 2000,158 2400,110 L2400,180 L0,180 Z"/></svg>
      <svg class="ft-25__wave ft-25__wave--front" viewBox="0 0 2400 180" preserveAspectRatio="none" focusable="false"><path d="M0,132 C350,180 700,88 1200,132 C1700,176 2050,86 2400,132 L2400,180 L0,180 Z"/></svg>
    </div>
    <div class="ft-25__body">
      <div class="ft-25__lead">
        <div class="ft-25__brand"><span class="ft-25__mark" aria-hidden="true"></span>Tidal Reach</div>
        <p class="ft-25__blurb">Coastal conservation, mapped and funded by the people who swim there. 41 beaches monitored weekly.</p>
        <a class="ft-25__cta" href="#ft-25-a">Adopt a stretch of coast</a>
      </div>
      <nav class="ft-25__col" aria-labelledby="ft-25-c1"><h2 class="ft-25__ch" id="ft-25-c1">The work</h2><ul class="ft-25__list"><li><a class="ft-25__link" href="#ft-25-a">Water quality map</a></li><li><a class="ft-25__link" href="#ft-25-a">Beach reports</a></li><li><a class="ft-25__link" href="#ft-25-a">Restoration sites</a></li><li><a class="ft-25__link" href="#ft-25-a">Open data</a></li></ul></nav>
      <nav class="ft-25__col" aria-labelledby="ft-25-c2"><h2 class="ft-25__ch" id="ft-25-c2">Take part</h2><ul class="ft-25__list"><li><a class="ft-25__link" href="#ft-25-a">Volunteer</a></li><li><a class="ft-25__link" href="#ft-25-a">Report a spill</a></li><li><a class="ft-25__link" href="#ft-25-a">Fundraise</a></li></ul></nav>
      <nav class="ft-25__col" aria-labelledby="ft-25-c3"><h2 class="ft-25__ch" id="ft-25-c3">About</h2><ul class="ft-25__list"><li><a class="ft-25__link" href="#ft-25-a">Our accounts</a></li><li><a class="ft-25__link" href="#ft-25-a">Trustees</a></li><li><a class="ft-25__link" href="#ft-25-a">Contact</a></li></ul></nav>
    </div>
    <div class="ft-25__bar">
      <p class="ft-25__copy">© <time datetime="2026">2026</time> Tidal Reach · Registered charity 1188422</p>
      <ul class="ft-25__legal"><li><a class="ft-25__slink" href="#ft-25-a">Privacy</a></li><li><a class="ft-25__slink" href="#ft-25-a">Safeguarding</a></li><li><a class="ft-25__slink" href="#ft-25-a">Accessibility</a></li></ul>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-25 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-25-bg);
  --ft-25-bg: oklch(0.97 0.014 210);
  --ft-25-deep: oklch(0.28 0.09 235);
  --ft-25-mid: oklch(0.36 0.1 225);
  --ft-25-fink: oklch(0.97 0.01 210);
  --ft-25-fmut: oklch(0.8 0.03 210);
  --ft-25-ink: oklch(0.24 0.04 235);
  --ft-25-mut: oklch(0.52 0.03 235);
  --ft-25-acc: oklch(0.83 0.14 190);
  --ft-25-line: oklch(0.97 0.01 210/.18);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-25-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-25 *,
.ft-25 *::before,
.ft-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-25 ul {
  list-style: none;
}

.ft-25__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(34px,6.5vh,74px) clamp(20px,4vh,40px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1120px)/2));
}

.ft-25__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: oklch(0.5 0.12 220);
}

.ft-25__title {
  font-size: clamp(28px,5.2vw,56px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 15ch;
  text-wrap: balance;
}

.ft-25__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-25-mut);
  max-width: 56ch;
  text-wrap: pretty;
}

.ft-25__foot {
  position: relative;
  background: linear-gradient(180deg,var(--ft-25-mid),var(--ft-25-deep));
  color: var(--ft-25-fink);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1120px)/2));
}

.ft-25__waves {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  height: clamp(70px,10vw,124px);
  translate: 0 -99%;
  overflow: hidden;
  pointer-events: none;
}

.ft-25__wave {
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 200%;
  height: 100%;
  display: block;
}

.ft-25__wave path {
  fill: currentColor;
}

.ft-25__wave--back {
  color: color-mix(in oklch,var(--ft-25-mid) 42%,transparent);
  animation: ft-25-drift 30s linear infinite;
}

.ft-25__wave--mid {
  color: color-mix(in oklch,var(--ft-25-mid) 70%,transparent);
  animation: ft-25-drift 21s linear infinite;
}

.ft-25__wave--front {
  color: var(--ft-25-mid);
  animation: ft-25-drift 14s linear infinite;
}

@keyframes ft-25-drift {
  to {
    transform: translateX(-50%);
  }
}

.ft-25__body {
  position: relative;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(10.5rem,1fr));
  gap: clamp(24px,3.2vw,40px) clamp(16px,2.2vw,30px);
  padding-block: clamp(28px,4vw,48px);
}

.ft-25__lead {
  display: grid;
  align-content: start;
  gap: 12px;
  min-width: 0;
  grid-column: span 2;
}

.ft-25__brand {
  display: flex;
  align-items: center;
  gap: 11px;
  font-size: 19px;
  font-weight: 700;
  letter-spacing: -.03em;
}

.ft-25__mark {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 30%,var(--ft-25-acc),oklch(0.5 0.14 220) 72%);
  box-shadow: 0 0 22px -6px var(--ft-25-acc);
}

.ft-25__blurb {
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--ft-25-fmut);
  max-width: 34ch;
  text-wrap: pretty;
}

.ft-25__cta {
  display: inline-flex;
  align-items: center;
  justify-self: start;
  min-height: 46px;
  padding: 0 22px;
  border-radius: 99px;
  background: var(--ft-25-acc);
  color: oklch(0.2 0.06 230);
  font-size: 14.5px;
  font-weight: 680;
  text-decoration: none;
  transition: transform .24s cubic-bezier(.34,1.56,.64,1),box-shadow .24s ease;
}

.ft-25__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 32px -16px var(--ft-25-acc);
}

.ft-25__col {
  display: grid;
  align-content: start;
  gap: 4px;
  min-width: 0;
}

.ft-25__ch {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  margin-block-end: 8px;
}

.ft-25__list {
  display: grid;
  gap: 1px;
}

.ft-25__link {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  font-size: 14.2px;
  color: var(--ft-25-fmut);
  text-decoration: none;
  width: fit-content;
  transition: color .18s ease,translate .18s ease;
}

.ft-25__link:hover {
  color: var(--ft-25-acc);
  translate: 3px 0;
}

.ft-25__link:focus-visible,
.ft-25__cta:focus-visible,
.ft-25__slink:focus-visible {
  outline: 2px solid var(--ft-25-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.ft-25__bar {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px 22px;
  padding-block: 18px;
  padding-bottom: calc(18px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-25-line);
}

.ft-25__copy {
  font-size: 12.6px;
  color: var(--ft-25-fmut);
}

.ft-25__legal {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 16px;
  margin-inline-start: auto;
}

.ft-25__slink {
  display: flex;
  align-items: center;
  min-height: 36px;
  font-size: 12.6px;
  color: var(--ft-25-fmut);
  text-decoration: none;
}

.ft-25__slink:hover {
  color: var(--ft-25-fink);
  text-decoration: underline;
  text-underline-offset: .25em;
}

@media (max-width: 700px) {
  .ft-25__lead {
    grid-column: auto;
  }

  .ft-25__legal {
    margin-inline-start: 0;
  }
}

@media (max-width: 640px) {
  .ft-25__waves {
    height: 60px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-25__wave {
    animation: none;
    transform: translateX(-12%);
  }

  .ft-25 * {
    transition-duration: .01ms !important;
  }
}
```
