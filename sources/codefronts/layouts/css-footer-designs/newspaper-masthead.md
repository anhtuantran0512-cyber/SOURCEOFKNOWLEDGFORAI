---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/newspaper-masthead/"
title: "Editorial Newspaper Style Multi-Column Footer"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "A masthead footer with the density and discipline of print: real CSS multi-columns with hairline rules between them, small-caps section labels, an editorial…"
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Editorial Newspaper Style Multi-Column Footer
Source: https://codefronts.com/layouts/css-footer-designs/newspaper-masthead/

A masthead footer with the density and discipline of print: real CSS multi-columns with hairline rules between them, small-caps section labels, an editorial colophon, and a rag that behaves because break-inside and text-wrap are doing their jobs. The one place columns beats Grid — flowing content, not a fixed matrix.
## HTML
```html
<section class="ft-12" aria-label="Editorial newspaper style footer demo">
  <main class="ft-12__main">
    <p class="ft-12__eyebrow">columns · column-rule · break-inside</p>
    <h1 class="ft-12__title">A masthead, not a link dump</h1>
    <p class="ft-12__sub">CSS multi-columns pour variable-length sections into an even grid and draw the hairline rules between them — the one layout job Grid still can't do without extra elements.</p>
  </main>
  <footer class="ft-12__foot">
    <div class="ft-12__folio">
      <span class="ft-12__logo">The Quarter Sheet</span>
      <span class="ft-12__folioline">Vol. XIV · No. 212 · <time datetime="2026-08-07">Friday, 7 August 2026</time> · Established 2012</span>
    </div>
    <div class="ft-12__masthead">
      <section class="ft-12__sec" aria-labelledby="ft-12-s1"><h2 class="ft-12__h" id="ft-12-s1">Sections</h2><ul class="ft-12__list"><li><a class="ft-12__link" href="#ft-12-a">World</a></li><li><a class="ft-12__link" href="#ft-12-a">Business</a></li><li><a class="ft-12__link" href="#ft-12-a">Science</a></li><li><a class="ft-12__link" href="#ft-12-a">Culture</a></li><li><a class="ft-12__link" href="#ft-12-a">Opinion</a></li><li><a class="ft-12__link" href="#ft-12-a">Long reads</a></li></ul></section>
      <section class="ft-12__sec" aria-labelledby="ft-12-s2"><h2 class="ft-12__h" id="ft-12-s2">Newsletters</h2><ul class="ft-12__list"><li><a class="ft-12__link" href="#ft-12-a">The Morning Sheet</a></li><li><a class="ft-12__link" href="#ft-12-a">Markets at Noon</a></li><li><a class="ft-12__link" href="#ft-12-a">Sunday Essay</a></li></ul></section>
      <section class="ft-12__sec" aria-labelledby="ft-12-s3"><h2 class="ft-12__h" id="ft-12-s3">Subscribe</h2><ul class="ft-12__list"><li><a class="ft-12__link" href="#ft-12-a">Digital · £6/mo</a></li><li><a class="ft-12__link" href="#ft-12-a">Print &amp; digital</a></li><li><a class="ft-12__link" href="#ft-12-a">Gift a subscription</a></li><li><a class="ft-12__link" href="#ft-12-a">Student rate</a></li><li><a class="ft-12__link" href="#ft-12-a">Manage my account</a></li></ul></section>
      <section class="ft-12__sec" aria-labelledby="ft-12-s4"><h2 class="ft-12__h" id="ft-12-s4">The paper</h2><ul class="ft-12__list"><li><a class="ft-12__link" href="#ft-12-a">Editorial code</a></li><li><a class="ft-12__link" href="#ft-12-a">Corrections</a></li><li><a class="ft-12__link" href="#ft-12-a">Contact the newsroom</a></li><li><a class="ft-12__link" href="#ft-12-a">Work with us</a></li></ul></section>
      <section class="ft-12__sec" aria-labelledby="ft-12-s5"><h2 class="ft-12__h" id="ft-12-s5">Notices</h2><ul class="ft-12__list"><li><a class="ft-12__link" href="#ft-12-a">Terms of use</a></li><li><a class="ft-12__link" href="#ft-12-a">Privacy &amp; cookies</a></li><li><a class="ft-12__link" href="#ft-12-a">Accessibility</a></li><li><a class="ft-12__link" href="#ft-12-a">Advertise</a></li></ul></section>
    </div>
    <div class="ft-12__colophon">
      <p class="ft-12__quote">&ldquo;Print the facts, then print what they cost.&rdquo;</p>
      <p class="ft-12__cred">Set in the system serif at 11 point. Published in London by Quarter Sheet Publishing Ltd, registered in England &amp; Wales no. 08114127. Registered office: 3 Bell Yard, London WC2A 2JR. All rights reserved. Reproduction in whole or in part without written permission is prohibited.</p>
    </div>
    <div class="ft-12__bar">
      <p class="ft-12__copy">© <time datetime="2026">2026</time> Quarter Sheet Publishing</p>
      <p class="ft-12__issn">ISSN 2049-3013 · Printed on 100% recycled stock</p>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-12-bg);
  --ft-12-bg: oklch(0.965 0.012 85);
  --ft-12-paper: oklch(0.985 0.008 85);
  --ft-12-ink: oklch(0.19 0.012 60);
  --ft-12-mut: oklch(0.46 0.014 60);
  --ft-12-rule: oklch(0.19 0.012 60/.22);
  --ft-12-acc: oklch(0.45 0.16 28);
  font-family: 'Iowan Old Style','Palatino Linotype',Palatino,Georgia,'Times New Roman',serif;
  color: var(--ft-12-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-12 *,
.ft-12 *::before,
.ft-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-12 ul {
  list-style: none;
}

.ft-12__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(40px,8vh,88px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1180px)/2));
}

.ft-12__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ft-12-acc);
}

.ft-12__title {
  font-size: clamp(32px,6vw,64px);
  line-height: 1.02;
  letter-spacing: -.025em;
  font-weight: 600;
  max-width: 14ch;
  text-wrap: balance;
}

.ft-12__sub {
  font-size: clamp(15.5px,1.7vw,19px);
  line-height: 1.62;
  color: var(--ft-12-mut);
  max-width: 56ch;
  text-wrap: pretty;
}

.ft-12__foot {
  background: var(--ft-12-paper);
  border-top: 3px solid var(--ft-12-ink);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1180px)/2));
}

.ft-12__folio {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 8px 20px;
  padding-block: 22px 14px;
  border-bottom: 1px solid var(--ft-12-rule);
}

.ft-12__logo {
  font-size: clamp(24px,3.4vw,38px);
  font-weight: 600;
  letter-spacing: -.02em;
  font-variant-caps: titling-caps;
}

.ft-12__folioline {
  margin-inline-start: auto;
  font-size: 12.5px;
  letter-spacing: .06em;
  color: var(--ft-12-mut);
  font-variant-caps: all-small-caps;
}

.ft-12__masthead {
  columns: 5 12rem;
  column-gap: clamp(22px,3vw,40px);
  column-rule: 1px solid var(--ft-12-rule);
  padding-block: clamp(24px,3.4vw,36px);
  border-bottom: 1px solid var(--ft-12-rule);
}

.ft-12__sec {
  break-inside: avoid;
  margin-block-end: 22px;
}

.ft-12__h {
  font-size: 12.5px;
  font-weight: 600;
  letter-spacing: .14em;
  font-variant-caps: all-small-caps;
  text-transform: lowercase;
  color: var(--ft-12-acc);
  padding-block-end: 7px;
  margin-block-end: 7px;
  border-bottom: 1px solid var(--ft-12-rule);
}

.ft-12__list {
  display: grid;
  gap: 0;
}

.ft-12__link {
  display: inline-flex;
  align-items: center;
  min-height: 32px;
  font-size: 15px;
  line-height: 1.35;
  color: var(--ft-12-ink);
  text-decoration: none;
  width: fit-content;
  border-bottom: 1px solid transparent;
  transition: border-color .2s ease,color .2s ease;
}

.ft-12__link:hover {
  color: var(--ft-12-acc);
  border-bottom-color: currentColor;
}

.ft-12__link:focus-visible {
  outline: 2px solid var(--ft-12-acc);
  outline-offset: 3px;
}

.ft-12__colophon {
  display: grid;
  gap: 12px;
  padding-block: clamp(22px,3vw,32px);
  border-bottom: 1px solid var(--ft-12-rule);
  hanging-punctuation: first;
}

.ft-12__quote {
  font-size: clamp(19px,2.4vw,26px);
  line-height: 1.3;
  font-style: italic;
  letter-spacing: -.015em;
  max-width: 26ch;
  text-wrap: balance;
}

.ft-12__cred {
  font-size: 12.6px;
  line-height: 1.62;
  color: var(--ft-12-mut);
  max-width: 78ch;
  text-align: justify;
  hyphens: auto;
  text-wrap: pretty;
}

.ft-12__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 8px 22px;
  padding-block: 18px;
  padding-bottom: calc(18px + env(safe-area-inset-bottom,0px));
}

.ft-12__copy,
.ft-12__issn {
  font-size: 12.4px;
  letter-spacing: .05em;
  color: var(--ft-12-mut);
  font-variant-caps: all-small-caps;
}

.ft-12__issn {
  margin-inline-start: auto;
}

@media (max-width: 640px) {
  .ft-12__folioline,
    .ft-12__issn {
    margin-inline-start: 0;
  }

  .ft-12__cred {
    text-align: start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-12 * {
    transition-duration: .01ms !important;
  }
}
```
