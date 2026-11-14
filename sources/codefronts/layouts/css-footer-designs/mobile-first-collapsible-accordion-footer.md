---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/mobile-first-collapsible-accordion-footer/"
title: "Mobile-First Collapsible Accordion Footer"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "Four link categories that collapse into tappable accordion rows on a phone and expand into plain columns on a laptop — built on <details> so it works before…"
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile-First Collapsible Accordion Footer
Source: https://codefronts.com/layouts/css-footer-designs/mobile-first-collapsible-accordion-footer/

Four link categories that collapse into tappable accordion rows on a phone and expand into plain columns on a laptop — built on <details> so it works before a single byte of JavaScript loads, with a genuinely smooth height animation using the 0fr → 1fr grid technique.
## HTML
```html
<section class="ft-08" aria-label="Mobile-first collapsible accordion footer demo">
  <main class="ft-08__main">
    <p class="ft-08__eyebrow">&lt;details name&gt; · 0fr → 1fr</p>
    <h1 class="ft-08__title">Accordion on a phone, columns on a laptop</h1>
    <p class="ft-08__sub">Narrow the frame below 720px and the link groups collapse into tappable rows. Widen it and the same markup lays out as ordinary columns — no JavaScript at either size.</p>
  </main>
  <footer class="ft-08__foot">
    <div class="ft-08__top">
      <div class="ft-08__brand"><span class="ft-08__mark" aria-hidden="true"></span>Verso Mobile</div>
      <p class="ft-08__blurb">Banking that fits in a pocket. Regulated by the FCA, 04412887.</p>
    </div>
    <div class="ft-08__acc">
      <details class="ft-08__d" name="ft-08-group" open>
        <summary class="ft-08__sum">Accounts<span class="ft-08__chev" aria-hidden="true"></span></summary>
        <div class="ft-08__panel"><div class="ft-08__panelin">
          <ul class="ft-08__list"><li><a class="ft-08__link" href="#ft-08-a">Everyday account</a></li><li><a class="ft-08__link" href="#ft-08-a">Joint account</a></li><li><a class="ft-08__link" href="#ft-08-a">Savings pots</a></li><li><a class="ft-08__link" href="#ft-08-a">Under-18s</a></li><li><a class="ft-08__link" href="#ft-08-a">Business</a></li></ul>
        </div></div>
      </details>
      <details class="ft-08__d" name="ft-08-group">
        <summary class="ft-08__sum">Borrowing<span class="ft-08__chev" aria-hidden="true"></span></summary>
        <div class="ft-08__panel"><div class="ft-08__panelin">
          <ul class="ft-08__list"><li><a class="ft-08__link" href="#ft-08-a">Overdrafts</a></li><li><a class="ft-08__link" href="#ft-08-a">Personal loans</a></li><li><a class="ft-08__link" href="#ft-08-a">Credit builder</a></li><li><a class="ft-08__link" href="#ft-08-a">Rates &amp; fees</a></li></ul>
        </div></div>
      </details>
      <details class="ft-08__d" name="ft-08-group">
        <summary class="ft-08__sum">Support<span class="ft-08__chev" aria-hidden="true"></span></summary>
        <div class="ft-08__panel"><div class="ft-08__panelin">
          <ul class="ft-08__list"><li><a class="ft-08__link" href="#ft-08-a">Help centre</a></li><li><a class="ft-08__link" href="#ft-08-a">Lost or stolen card</a></li><li><a class="ft-08__link" href="#ft-08-a">Report a scam</a></li><li><a class="ft-08__link" href="#ft-08-a">Accessibility support</a></li><li><a class="ft-08__link" href="#ft-08-a">Complaints</a></li></ul>
        </div></div>
      </details>
      <details class="ft-08__d" name="ft-08-group">
        <summary class="ft-08__sum">Company<span class="ft-08__chev" aria-hidden="true"></span></summary>
        <div class="ft-08__panel"><div class="ft-08__panelin">
          <ul class="ft-08__list"><li><a class="ft-08__link" href="#ft-08-a">About Verso</a></li><li><a class="ft-08__link" href="#ft-08-a">Careers</a></li><li><a class="ft-08__link" href="#ft-08-a">Press</a></li><li><a class="ft-08__link" href="#ft-08-a">Investors</a></li></ul>
        </div></div>
      </details>
    </div>
    <div class="ft-08__bar">
      <p class="ft-08__copy">© <time datetime="2026">2026</time> Verso Mobile Ltd</p>
      <ul class="ft-08__legal"><li><a class="ft-08__slink" href="#ft-08-a">Privacy</a></li><li><a class="ft-08__slink" href="#ft-08-a">Terms</a></li><li><a class="ft-08__slink" href="#ft-08-a">Cookies</a></li></ul>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-08-bg);
  --ft-08-bg: oklch(0.97 0.01 300);
  --ft-08-foot: oklch(0.21 0.04 300);
  --ft-08-ink: oklch(0.22 0.04 300);
  --ft-08-mut: oklch(0.54 0.025 300);
  --ft-08-fink: oklch(0.97 0.008 300);
  --ft-08-fmut: oklch(0.76 0.02 300);
  --ft-08-acc: oklch(0.72 0.17 320);
  --ft-08-fline: oklch(0.97 0.008 300/.15);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-08-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-08 *,
.ft-08 *::before,
.ft-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-08 ul {
  list-style: none;
}

.ft-08__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(40px,8vh,90px);
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 1100px)/2));
}

.ft-08__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: oklch(0.5 0.18 320);
}

.ft-08__title {
  font-size: clamp(29px,5.2vw,56px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 16ch;
  text-wrap: balance;
}

.ft-08__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-08-mut);
  max-width: 56ch;
  text-wrap: pretty;
}

.ft-08__foot {
  background: var(--ft-08-foot);
  color: var(--ft-08-fink);
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 1100px)/2));
  container-type: inline-size;
  container-name: ft-08-foot;
}

.ft-08__top {
  display: grid;
  gap: 8px;
  padding-block: clamp(26px,4vw,40px) 18px;
}

.ft-08__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 18px;
  font-weight: 700;
  letter-spacing: -.025em;
}

.ft-08__mark {
  width: 24px;
  height: 24px;
  border-radius: 8px;
  background: linear-gradient(140deg,var(--ft-08-acc),oklch(0.66 0.19 275));
  box-shadow: 0 6px 18px -6px var(--ft-08-acc);
}

.ft-08__blurb {
  font-size: 14px;
  color: var(--ft-08-fmut);
  max-width: 40ch;
}

.ft-08__acc {
  display: grid;
  border-top: 1px solid var(--ft-08-fline);
}

.ft-08__d {
  border-bottom: 1px solid var(--ft-08-fline);
}

.ft-08__sum {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  min-height: 56px;
  padding-block: 8px;
  font-size: 15px;
  font-weight: 660;
  letter-spacing: -.01em;
  cursor: pointer;
  list-style: none;
  -webkit-tap-highlight-color: transparent;
}

.ft-08__sum::-webkit-details-marker {
  display: none;
}

.ft-08__sum:hover {
  color: var(--ft-08-acc);
}

.ft-08__sum:focus-visible {
  outline: 2px solid var(--ft-08-acc);
  outline-offset: -2px;
  border-radius: 6px;
}

.ft-08__chev {
  position: relative;
  width: 13px;
  height: 13px;
  flex: none;
  transition: rotate .3s cubic-bezier(.2,.8,.2,1);
}

.ft-08__chev::before,
.ft-08__chev::after {
  content: '';
  position: absolute;
  background: currentColor;
  border-radius: 2px;
}

.ft-08__chev::before {
  left: 0;
  top: 50%;
  width: 100%;
  height: 1.8px;
  translate: 0 -50%;
}

.ft-08__chev::after {
  top: 0;
  left: 50%;
  height: 100%;
  width: 1.8px;
  translate: -50% 0;
  transition: opacity .3s ease,rotate .3s ease;
}

.ft-08__d[open] .ft-08__chev::after {
  opacity: 0;
}

.ft-08__d[open] .ft-08__chev {
  rotate: 180deg;
}

.ft-08__panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .38s cubic-bezier(.2,.8,.2,1);
}

.ft-08__d[open] .ft-08__panel {
  grid-template-rows: 1fr;
}

.ft-08__panelin {
  overflow: hidden;
  min-height: 0;
}

.ft-08__list {
  display: grid;
  gap: 2px;
  padding-block: 0 14px;
}

.ft-08__link {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  font-size: 14.5px;
  color: var(--ft-08-fmut);
  text-decoration: none;
  width: fit-content;
  transition: color .18s ease,translate .18s ease;
}

.ft-08__link:hover {
  color: var(--ft-08-acc);
  translate: 3px 0;
}

.ft-08__link:focus-visible,
.ft-08__slink:focus-visible {
  outline: 2px solid var(--ft-08-acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.ft-08__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px 20px;
  padding-block: 20px;
  padding-bottom: calc(20px + env(safe-area-inset-bottom,0px));
}

.ft-08__copy {
  font-size: 13px;
  color: var(--ft-08-fmut);
}

.ft-08__legal {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 16px;
  margin-inline-start: auto;
}

.ft-08__slink {
  display: flex;
  align-items: center;
  min-height: 38px;
  font-size: 13px;
  color: var(--ft-08-fmut);
  text-decoration: none;
}

.ft-08__slink:hover {
  color: var(--ft-08-fink);
  text-decoration: underline;
  text-underline-offset: .25em;
}

@container ft-08-foot (min-width: 720px) {
  .ft-08__acc {
    grid-template-columns: repeat(4,1fr);
    gap: clamp(18px,2.4vw,32px);
    padding-block-start: clamp(22px,3vw,32px);
  }

  .ft-08__d {
    border-bottom: 0;
  }

  .ft-08__sum {
    pointer-events: none;
    min-height: auto;
    padding-block: 0 10px;
    font-size: 11.5px;
    font-weight: 700;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: var(--ft-08-fink);
    justify-content: flex-start;
  }

  .ft-08__chev {
    display: none;
  }

  .ft-08__panel {
    grid-template-rows: 1fr !important;
  }

  .ft-08__link {
    min-height: 34px;
  }
}

@supports (interpolate-size: allow-keywords) {
  .ft-08 {
    interpolate-size: allow-keywords;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-08 * {
    transition-duration: .01ms !important;
  }
}
```
