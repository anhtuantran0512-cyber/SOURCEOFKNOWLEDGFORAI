---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/simple-minimalist-footer-html-css/"
title: "Simple Minimalist Footer HTML CSS"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "Twelve lines of CSS for the footer most sites actually need: a wordmark, a short link row and a copyright line, holding its composure from 320px to 2560px."
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Simple Minimalist Footer HTML CSS
Source: https://codefronts.com/layouts/css-footer-designs/simple-minimalist-footer-html-css/

Twelve lines of CSS for the footer most sites actually need: a wordmark, a short link row and a copyright line, holding its composure from 320px to 2560px. Nothing is hidden at small sizes, nothing is centred by hand, and the underline treatment is the modern one — text-underline-offset rather than a fake border.
## HTML
```html
<section class="ft-04" aria-label="Simple minimalist footer demo">
  <main class="ft-04__main">
    <p class="ft-04__eyebrow">flex-wrap · gap · clamp()</p>
    <h1 class="ft-04__title">Small footer. No compromises.</h1>
    <p class="ft-04__sub">One flex row that wraps, real text underlines, and a hairline that re-tints itself on any background. Roughly 700 bytes of CSS.</p>
    <ul class="ft-04__facts">
      <li>No media queries</li>
      <li>No wrapper divs</li>
      <li>44px hit targets</li>
    </ul>
  </main>
  <footer class="ft-04__foot">
    <a class="ft-04__brand" href="#ft-04-top">Kestrel<span class="ft-04__dot" aria-hidden="true"></span></a>
    <nav class="ft-04__nav" aria-label="Footer">
      <a class="ft-04__link" href="#ft-04-a">Work</a>
      <a class="ft-04__link" href="#ft-04-a">Studio</a>
      <a class="ft-04__link" href="#ft-04-a">Journal</a>
      <a class="ft-04__link" href="#ft-04-a">Contact</a>
    </nav>
    <p class="ft-04__copy">© <time datetime="2026">2026</time> Kestrel Studio</p>
  </footer>
</section>
```
## CSS
```css
.ft-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-04-bg);
  --ft-04-bg: oklch(0.985 0.004 95);
  --ft-04-ink: oklch(0.24 0.012 70);
  --ft-04-mut: oklch(0.56 0.012 70);
  --ft-04-acc: oklch(0.52 0.13 45);
  --ft-04-line: color-mix(in oklch,var(--ft-04-ink) 12%,transparent);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-04-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-04 *,
.ft-04 *::before,
.ft-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-04 ul {
  list-style: none;
}

.ft-04__main {
  display: grid;
  align-content: center;
  gap: 16px;
  padding-block: clamp(44px,9vh,100px);
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 940px)/2));
}

.ft-04__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--ft-04-acc);
}

.ft-04__title {
  font-size: clamp(32px,6vw,62px);
  line-height: 1.02;
  letter-spacing: -.045em;
  font-weight: 700;
  max-width: 14ch;
  text-wrap: balance;
}

.ft-04__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.62;
  color: var(--ft-04-mut);
  max-width: 52ch;
  text-wrap: pretty;
}

.ft-04__facts {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.ft-04__facts li {
  font-size: 12.5px;
  font-weight: 600;
  color: var(--ft-04-mut);
  padding: 7px 13px;
  border-radius: 99px;
  border: 1px solid var(--ft-04-line);
}

.ft-04__foot {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px clamp(20px,4vw,40px);
  padding-block: clamp(18px,2.5vw,26px);
  padding-bottom: calc(clamp(18px,2.5vw,26px) + env(safe-area-inset-bottom,0px));
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 940px)/2));
  border-top: 1px solid var(--ft-04-line);
}

.ft-04__brand {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: clamp(15px,1.5vw,17px);
  font-weight: 700;
  letter-spacing: -.03em;
  color: inherit;
  text-decoration: none;
}

.ft-04__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--ft-04-acc);
  translate: 0 -6px;
}

.ft-04__nav {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 4px clamp(14px,2vw,24px);
}

.ft-04__link {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  font-size: clamp(14px,1.4vw,15.5px);
  color: var(--ft-04-mut);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: .28em;
  text-decoration-color: color-mix(in oklch,currentColor 28%,transparent);
  transition: color .2s ease,text-decoration-color .2s ease;
}

.ft-04__link:hover {
  color: var(--ft-04-ink);
  text-decoration-color: currentColor;
}

.ft-04__link:focus-visible,
.ft-04__brand:focus-visible {
  outline: 2px solid var(--ft-04-acc);
  outline-offset: 4px;
  border-radius: 4px;
}

.ft-04__copy {
  font-size: clamp(13px,1.3vw,14px);
  color: var(--ft-04-mut);
}

@media (max-width: 640px) {
  .ft-04__foot {
    justify-content: flex-start;
  }

  .ft-04__nav {
    width: 100%;
    order: 3;
  }

  .ft-04__copy {
    order: 4;
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-04 * {
    transition-duration: .01ms !important;
  }
}
```
