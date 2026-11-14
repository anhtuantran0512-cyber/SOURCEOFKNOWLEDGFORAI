---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/editorial-centered/"
title: "Centered Minimalist Blog Footer HTML CSS"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "The footer for a personal site or writing blog: everything on the centre line, a measured column that never exceeds a comfortable reading width, a small…"
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Centered Minimalist Blog Footer HTML CSS
Source: https://codefronts.com/layouts/css-footer-designs/editorial-centered/

The footer for a personal site or writing blog: everything on the centre line, a measured column that never exceeds a comfortable reading width, a small mark, and the three links a reader actually wants — RSS, archive, and a way to reply. Quiet, confident, about 40 lines of CSS.
## HTML
```html
<section class="ft-18" aria-label="Centered minimalist blog footer demo">
  <main class="ft-18__main">
    <article class="ft-18__post">
      <p class="ft-18__meta"><time datetime="2026-07-29">29 July 2026</time> · 6 min</p>
      <h1 class="ft-18__title">On writing less markup</h1>
      <p class="ft-18__lede">Every wrapper you don't add is a bug you don't ship, a rule you don't have to override, and a line a future reader doesn't have to hold in their head. The best layout code reads like a sentence.</p>
      <p class="ft-18__body">Modern CSS keeps removing reasons to nest. Gap replaced margin stacks. Grid replaced the wrapper-plus-float. Logical properties replaced the left/right pair. Container queries replaced the media-query ladder. What's left is closer to describing the design than constructing it.</p>
    </article>
  </main>
  <footer class="ft-18__foot">
    <span class="ft-18__mark" aria-hidden="true"></span>
    <p class="ft-18__name">Ines Márquez</p>
    <p class="ft-18__blurb">Notes on interfaces, typography and the slow craft of the front end. Written in Valencia, published every other Wednesday.</p>
    <nav class="ft-18__nav" aria-label="Footer">
      <a class="ft-18__link" href="#ft-18-a">Archive</a>
      <a class="ft-18__link" href="#ft-18-a">RSS</a>
      <a class="ft-18__link" href="#ft-18-a">Now</a>
      <a class="ft-18__link" href="mailto:[email protected]">Reply by email</a>
    </nav>
    <p class="ft-18__copy">© <time datetime="2026">2026</time> Ines Márquez · Words licensed <a class="ft-18__slink" href="#ft-18-a">CC BY-NC 4.0</a> · Code <a class="ft-18__slink" href="#ft-18-a">MIT</a></p>
  </footer>
</section>
```
## CSS
```css
.ft-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-18-bg);
  --ft-18-bg: oklch(0.98 0.008 90);
  --ft-18-ink: oklch(0.24 0.014 60);
  --ft-18-mut: oklch(0.52 0.014 60);
  --ft-18-acc: oklch(0.5 0.13 25);
  font-family: 'Iowan Old Style','Palatino Linotype',Palatino,Georgia,serif;
  color: var(--ft-18-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-18 *,
.ft-18 *::before,
.ft-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-18__main {
  display: grid;
  place-items: center;
  padding-block: clamp(40px,8vh,96px);
  padding-inline: clamp(20px,5vw,44px);
}

.ft-18__post {
  display: grid;
  gap: 14px;
  max-width: 60ch;
}

.ft-18__meta {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 12.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--ft-18-mut);
}

.ft-18__title {
  font-size: clamp(30px,5vw,52px);
  line-height: 1.06;
  letter-spacing: -.028em;
  font-weight: 600;
  text-wrap: balance;
}

.ft-18__lede {
  font-size: clamp(17px,1.9vw,21px);
  line-height: 1.55;
  color: var(--ft-18-ink);
  text-wrap: pretty;
}

.ft-18__body {
  font-size: clamp(15.5px,1.7vw,17.5px);
  line-height: 1.72;
  color: var(--ft-18-mut);
  text-wrap: pretty;
}

.ft-18__foot {
  position: relative;
  display: grid;
  justify-items: center;
  gap: 12px;
  text-align: center;
  padding-block: clamp(38px,6vw,64px) clamp(28px,4vw,44px);
  padding-bottom: calc(clamp(28px,4vw,44px) + env(safe-area-inset-bottom,0px));
  padding-inline: clamp(20px,5vw,44px);
}

.ft-18__foot::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  translate: -50% 0;
  width: 64px;
  height: 1px;
  background: var(--ft-18-ink);
  opacity: .22;
}

.ft-18__mark {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: radial-gradient(circle at 34% 32%,oklch(0.72 0.14 40),var(--ft-18-acc) 72%);
  box-shadow: 0 6px 16px -8px var(--ft-18-acc);
}

.ft-18__name {
  font-size: clamp(17px,2vw,20px);
  font-weight: 600;
  letter-spacing: -.02em;
}

.ft-18__blurb {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 14px;
  line-height: 1.65;
  color: var(--ft-18-mut);
  max-width: 46ch;
  text-wrap: pretty;
}

.ft-18__nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2px clamp(12px,2vw,22px);
  margin-block-start: 2px;
}

.ft-18__link {
  font-family: 'Segoe UI',system-ui,sans-serif;
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  font-size: 14.5px;
  font-weight: 600;
  color: var(--ft-18-ink);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: .24em;
  text-decoration-color: color-mix(in oklch,currentColor 26%,transparent);
  transition: color .2s ease,text-decoration-color .2s ease,text-underline-offset .2s ease;
}

.ft-18__link:hover {
  color: var(--ft-18-acc);
  text-decoration-color: currentColor;
  text-underline-offset: .32em;
}

.ft-18__link:focus-visible,
.ft-18__slink:focus-visible {
  outline: 2px solid var(--ft-18-acc);
  outline-offset: 4px;
  border-radius: 4px;
}

.ft-18__copy {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 12.6px;
  line-height: 1.6;
  color: var(--ft-18-mut);
  max-width: 48ch;
}

.ft-18__slink {
  color: inherit;
  text-decoration: underline;
  text-underline-offset: .22em;
}

.ft-18__slink:hover {
  color: var(--ft-18-acc);
}

@media (prefers-reduced-motion: reduce) {
  .ft-18 * {
    transition-duration: .01ms !important;
  }
}
```
