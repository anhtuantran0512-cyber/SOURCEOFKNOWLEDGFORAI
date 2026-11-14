---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/neon-sign/"
title: "Dark Mode Glowing Neon CSS Footer"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "Neon that reads like a sign, not like a blur filter: layered text-shadow at four radii for the classic tube bloom, a flicker on a steps() curve that stutters…"
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Glowing Neon CSS Footer
Source: https://codefronts.com/layouts/css-footer-designs/neon-sign/

Neon that reads like a sign, not like a blur filter: layered text-shadow at four radii for the classic tube bloom, a flicker on a steps() curve that stutters like a failing ballast, and — the part most neon demos get wrong — body copy that stays at full contrast so the footer is still legible.
## HTML
```html
<section class="ft-17" aria-label="Neon glow footer demo">
  <main class="ft-17__main">
    <p class="ft-17__eyebrow">Layered text-shadow · steps() flicker</p>
    <h1 class="ft-17__title">Neon that stays <span class="ft-17__neon">readable</span></h1>
    <p class="ft-17__sub">Glow on the display type, flat contrast on everything you actually have to read. That single rule is the difference between a neon design and a neon mistake.</p>
  </main>
  <footer class="ft-17__foot">
    <div class="ft-17__bloom" aria-hidden="true"></div>
    <div class="ft-17__sign">
      <p class="ft-17__open">Open<span class="ft-17__tube" aria-hidden="true"></span></p>
      <p class="ft-17__wordmark">Static&nbsp;Motel</p>
      <p class="ft-17__tag">Vacancy · 24h diner · Route 6, Mile 41</p>
    </div>
    <div class="ft-17__cols">
      <nav class="ft-17__col" aria-labelledby="ft-17-c1"><h2 class="ft-17__ch" id="ft-17-c1">Rooms</h2><ul class="ft-17__list"><li><a class="ft-17__link" href="#ft-17-a">Book direct</a></li><li><a class="ft-17__link" href="#ft-17-a">Suites</a></li><li><a class="ft-17__link" href="#ft-17-a">Long stays</a></li><li><a class="ft-17__link" href="#ft-17-a">Rates</a></li></ul></nav>
      <nav class="ft-17__col" aria-labelledby="ft-17-c2"><h2 class="ft-17__ch" id="ft-17-c2">Diner</h2><ul class="ft-17__list"><li><a class="ft-17__link" href="#ft-17-a">Menu</a></li><li><a class="ft-17__link" href="#ft-17-a">Late night</a></li><li><a class="ft-17__link" href="#ft-17-a">Order ahead</a></li></ul></nav>
      <nav class="ft-17__col" aria-labelledby="ft-17-c3"><h2 class="ft-17__ch" id="ft-17-c3">Find us</h2><ul class="ft-17__list"><li><a class="ft-17__link" href="#ft-17-a">Directions</a></li><li><a class="ft-17__link" href="tel:+15550142200">+1 555 014 2200</a></li><li><a class="ft-17__link" href="#ft-17-a">Accessibility</a></li></ul></nav>
      <div class="ft-17__col">
        <h2 class="ft-17__ch">Tonight</h2>
        <p class="ft-17__status"><span class="ft-17__dot" aria-hidden="true"></span>6 rooms left</p>
        <a class="ft-17__cta" href="#ft-17-a">Reserve now</a>
      </div>
    </div>
    <div class="ft-17__bar">
      <p class="ft-17__copy">© <time datetime="2026">2026</time> Static Motel Holdings</p>
      <ul class="ft-17__legal"><li><a class="ft-17__slink" href="#ft-17-a">Privacy</a></li><li><a class="ft-17__slink" href="#ft-17-a">House rules</a></li><li><a class="ft-17__slink" href="#ft-17-a">Cancellations</a></li></ul>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-17-bg);
  --ft-17-bg: oklch(0.16 0.03 300);
  --ft-17-foot: oklch(0.13 0.028 300);
  --ft-17-ink: oklch(0.96 0.01 320);
  --ft-17-mut: oklch(0.78 0.02 320);
  --ft-17-glow: oklch(0.72 0.26 340);
  --ft-17-glow2: oklch(0.82 0.19 195);
  --ft-17-line: oklch(0.96 0.01 320/.14);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-17-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-17 *,
.ft-17 *::before,
.ft-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-17 ul {
  list-style: none;
}

.ft-17__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(38px,7.5vh,86px);
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 1080px)/2));
}

.ft-17__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ft-17-glow2);
}

.ft-17__title {
  font-size: clamp(30px,5.6vw,60px);
  line-height: 1.02;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 15ch;
  text-wrap: balance;
}

.ft-17__neon {
  color: oklch(0.98 0.04 340);
  text-shadow: 0 0 4px currentColor,0 0 12px var(--ft-17-glow),0 0 30px var(--ft-17-glow),0 0 66px var(--ft-17-glow);
}

.ft-17__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-17-mut);
  max-width: 56ch;
  text-wrap: pretty;
}

.ft-17__foot {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  background: var(--ft-17-foot);
  border-top: 1px solid color-mix(in oklch,var(--ft-17-glow) 30%,transparent);
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 1080px)/2));
}

.ft-17__bloom {
  position: absolute;
  left: 50%;
  top: -30%;
  width: min(120%,900px);
  aspect-ratio: 1;
  translate: -50% 0;
  z-index: -1;
  background: radial-gradient(circle,color-mix(in oklch,var(--ft-17-glow) 40%,transparent),transparent 62%);
  mix-blend-mode: screen;
  filter: blur(30px);
  opacity: .5;
}

.ft-17__sign {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding-block: clamp(34px,5.5vw,64px) clamp(24px,3.5vw,38px);
}

.ft-17__open {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12.5px;
  letter-spacing: .32em;
  text-transform: uppercase;
  color: var(--ft-17-glow2);
  text-shadow: 0 0 4px currentColor,0 0 14px var(--ft-17-glow2),0 0 34px var(--ft-17-glow2);
}

.ft-17__tube {
  width: 34px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  box-shadow: 0 0 8px currentColor,0 0 20px currentColor;
}

.ft-17__wordmark {
  font-size: clamp(38px,9vw,104px);
  line-height: .92;
  font-weight: 800;
  letter-spacing: -.045em;
  color: oklch(0.98 0.03 340);
  text-shadow: 0 0 5px currentColor,0 0 14px var(--ft-17-glow),0 0 38px var(--ft-17-glow),0 0 80px var(--ft-17-glow);
  animation: ft-17-flicker 7.5s steps(1,end) infinite;
}

@keyframes ft-17-flicker {
  0%,
    18%,
    20.5%,
    22%,
    24%,
    57%,
    59%,
    100% {
    opacity: 1;
  }

  19%,
    21%,
    23%,
    58% {
    opacity: .42;
  }
}

.ft-17__tag {
  font-size: 13.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--ft-17-mut);
}

.ft-17__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(10rem,1fr));
  gap: clamp(22px,3vw,36px) clamp(16px,2.2vw,28px);
  padding-block: clamp(24px,3.4vw,38px);
  border-top: 1px solid var(--ft-17-line);
}

.ft-17__col {
  display: grid;
  align-content: start;
  gap: 4px;
  min-width: 0;
}

.ft-17__ch {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--ft-17-glow2);
  margin-block-end: 8px;
  text-shadow: 0 0 10px color-mix(in oklch,var(--ft-17-glow2) 60%,transparent);
}

.ft-17__list {
  display: grid;
  gap: 1px;
}

.ft-17__link {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  font-size: 14.2px;
  color: var(--ft-17-mut);
  text-decoration: none;
  width: fit-content;
  transition: color .22s ease,text-shadow .22s ease;
}

.ft-17__link:hover {
  color: oklch(0.98 0.02 340);
  text-shadow: 0 0 10px var(--ft-17-glow),0 0 24px var(--ft-17-glow);
}

.ft-17__link:focus-visible,
.ft-17__cta:focus-visible,
.ft-17__slink:focus-visible {
  outline: 2px solid var(--ft-17-glow2);
  outline-offset: 3px;
  border-radius: 4px;
}

.ft-17__status {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 13.5px;
  color: var(--ft-17-mut);
}

.ft-17__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--ft-17-glow2);
  box-shadow: 0 0 8px currentColor,0 0 16px var(--ft-17-glow2);
  animation: ft-17-pulse 2.4s ease-in-out infinite;
}

@keyframes ft-17-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .35;
  }
}

.ft-17__cta {
  display: inline-flex;
  align-items: center;
  justify-self: start;
  margin-block-start: 10px;
  min-height: 44px;
  padding: 0 20px;
  border-radius: 99px;
  border: 1.5px solid var(--ft-17-glow);
  color: oklch(0.98 0.03 340);
  font-size: 14px;
  font-weight: 660;
  text-decoration: none;
  box-shadow: 0 0 12px -2px var(--ft-17-glow),inset 0 0 12px -6px var(--ft-17-glow);
  transition: background .25s ease,box-shadow .25s ease,transform .25s ease;
}

.ft-17__cta:hover {
  background: color-mix(in oklch,var(--ft-17-glow) 22%,transparent);
  box-shadow: 0 0 26px -2px var(--ft-17-glow),inset 0 0 22px -8px var(--ft-17-glow);
  transform: translateY(-2px);
}

.ft-17__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px 22px;
  padding-block: 18px;
  padding-bottom: calc(18px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-17-line);
}

.ft-17__copy {
  font-size: 12.6px;
  color: var(--ft-17-mut);
}

.ft-17__legal {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 16px;
  margin-inline-start: auto;
}

.ft-17__slink {
  display: flex;
  align-items: center;
  min-height: 36px;
  font-size: 12.6px;
  color: var(--ft-17-mut);
  text-decoration: none;
}

.ft-17__slink:hover {
  color: var(--ft-17-ink);
}

@media (max-width: 560px) {
  .ft-17__legal {
    margin-inline-start: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-17__wordmark,
    .ft-17__dot {
    animation: none;
  }

  .ft-17 * {
    transition-duration: .01ms !important;
  }
}
```
