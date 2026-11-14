---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/cta-stripe/"
title: "Pre-Footer Call-to-Action Bar HTML CSS"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "The band that sits between the last content section and the footer proper, doing the single job the footer is bad at: making one clear ask."
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pre-Footer Call-to-Action Bar HTML CSS
Source: https://codefronts.com/layouts/css-footer-designs/cta-stripe/

The band that sits between the last content section and the footer proper, doing the single job the footer is bad at: making one clear ask. Big type, one primary action, one low-friction secondary, and a clipped diagonal edge that separates it from the link grid without a border.
## HTML
```html
<section class="ft-23" aria-label="Pre-footer call to action bar demo">
  <main class="ft-23__main">
    <p class="ft-23__eyebrow">clip-path · clamp() display type</p>
    <h1 class="ft-23__title">One ask, right before the links</h1>
    <p class="ft-23__sub">The pre-footer band is the last chance to convert someone who scrolled to the bottom. It gets one heading, one button, and one line that removes the objection.</p>
  </main>
  <footer class="ft-23__foot">
    <section class="ft-23__cta" aria-labelledby="ft-23-ch">
      <div class="ft-23__ctain">
        <p class="ft-23__kicker">Free for 14 days</p>
        <h2 class="ft-23__ch2" id="ft-23-ch">Ship your first pipeline before lunch</h2>
        <p class="ft-23__cp">Import a repo, pick a target, press deploy. Most teams are live in under an hour — and you can bring your existing YAML with you.</p>
        <div class="ft-23__actions">
          <a class="ft-23__primary" href="#ft-23-a">Start free<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6"/></svg></a>
          <a class="ft-23__secondary" href="#ft-23-a">or book a 20-minute walkthrough</a>
        </div>
        <p class="ft-23__trust">No card required · cancel any time · <span class="ft-23__nowrap">SOC 2 Type II</span> · <span class="ft-23__nowrap">99.98% uptime</span></p>
      </div>
    </section>
    <div class="ft-23__links">
      <div class="ft-23__brandcol">
        <div class="ft-23__brand"><span class="ft-23__mark" aria-hidden="true"></span>Wayfinder</div>
        <p class="ft-23__blurb">Deployment for teams who would rather be building.</p>
      </div>
      <nav class="ft-23__col" aria-labelledby="ft-23-c1"><h2 class="ft-23__chh" id="ft-23-c1">Product</h2><ul class="ft-23__list"><li><a class="ft-23__link" href="#ft-23-a">Pipelines</a></li><li><a class="ft-23__link" href="#ft-23-a">Preview envs</a></li><li><a class="ft-23__link" href="#ft-23-a">Pricing</a></li><li><a class="ft-23__link" href="#ft-23-a">Changelog</a></li></ul></nav>
      <nav class="ft-23__col" aria-labelledby="ft-23-c2"><h2 class="ft-23__chh" id="ft-23-c2">Learn</h2><ul class="ft-23__list"><li><a class="ft-23__link" href="#ft-23-a">Docs</a></li><li><a class="ft-23__link" href="#ft-23-a">Guides</a></li><li><a class="ft-23__link" href="#ft-23-a">Blog</a></li></ul></nav>
      <nav class="ft-23__col" aria-labelledby="ft-23-c3"><h2 class="ft-23__chh" id="ft-23-c3">Company</h2><ul class="ft-23__list"><li><a class="ft-23__link" href="#ft-23-a">About</a></li><li><a class="ft-23__link" href="#ft-23-a">Careers</a></li><li><a class="ft-23__link" href="#ft-23-a">Contact</a></li></ul></nav>
    </div>
    <div class="ft-23__bar">
      <p class="ft-23__copy">© <time datetime="2026">2026</time> Wayfinder Cloud Ltd</p>
      <ul class="ft-23__legal"><li><a class="ft-23__slink" href="#ft-23-a">Privacy</a></li><li><a class="ft-23__slink" href="#ft-23-a">Terms</a></li><li><a class="ft-23__slink" href="#ft-23-a">Status</a></li></ul>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-23 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-23-bg);
  --ft-23-bg: oklch(0.97 0.008 260);
  --ft-23-foot: oklch(0.16 0.022 265);
  --ft-23-ink: oklch(0.21 0.028 265);
  --ft-23-mut: oklch(0.53 0.02 265);
  --ft-23-fink: oklch(0.97 0.006 265);
  --ft-23-fmut: oklch(0.73 0.015 265);
  --ft-23-acc: oklch(0.72 0.18 145);
  --ft-23-line: oklch(0.97 0.006 265/.14);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-23-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-23 *,
.ft-23 *::before,
.ft-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-23 ul {
  list-style: none;
}

.ft-23__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(34px,6.5vh,74px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1120px)/2));
}

.ft-23__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: oklch(0.5 0.15 148);
}

.ft-23__title {
  font-size: clamp(28px,5vw,54px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 15ch;
  text-wrap: balance;
}

.ft-23__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-23-mut);
  max-width: 56ch;
  text-wrap: pretty;
}

.ft-23__foot {
  background: var(--ft-23-foot);
  color: var(--ft-23-fink);
}

.ft-23__cta {
  position: relative;
  background: linear-gradient(135deg,oklch(0.26 0.09 158),oklch(0.2 0.05 200) 62%,oklch(0.19 0.04 265));
  clip-path: polygon(0 0,100% 34px,100% 100%,0 100%);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1120px)/2));
}

.ft-23__ctain {
  display: grid;
  justify-items: start;
  gap: 12px;
  padding-block: calc(34px + clamp(28px,4.5vw,56px)) clamp(30px,4.5vw,58px);
}

.ft-23__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--ft-23-acc);
  padding: 6px 12px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--ft-23-acc) 14%,transparent);
}

.ft-23__ch2 {
  font-size: clamp(27px,4.6vw,52px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 750;
  max-width: 17ch;
  text-wrap: balance;
}

.ft-23__cp {
  font-size: clamp(14.5px,1.6vw,17.5px);
  line-height: 1.6;
  color: oklch(0.85 0.015 200);
  max-width: 54ch;
  text-wrap: pretty;
}

.ft-23__actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px 22px;
  margin-block-start: 6px;
}

.ft-23__primary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-height: 54px;
  padding: 0 28px;
  border-radius: 14px;
  background: var(--ft-23-acc);
  color: oklch(0.17 0.05 150);
  font-size: 16px;
  font-weight: 700;
  letter-spacing: -.01em;
  text-decoration: none;
  transition: transform .24s cubic-bezier(.34,1.56,.64,1),box-shadow .24s ease,background .24s ease;
}

.ft-23__primary:hover {
  transform: translateY(-2px);
  background: oklch(0.8 0.18 145);
  box-shadow: 0 18px 36px -18px var(--ft-23-acc);
}

.ft-23__primary:hover svg {
  translate: 4px 0;
}

.ft-23__primary svg {
  transition: translate .24s cubic-bezier(.34,1.56,.64,1);
}

.ft-23__secondary {
  display: inline-flex;
  align-items: center;
  min-height: 48px;
  font-size: 15px;
  font-weight: 600;
  color: oklch(0.88 0.015 200);
  text-decoration: underline;
  text-underline-offset: .28em;
  text-decoration-color: color-mix(in oklch,currentColor 32%,transparent);
  transition: color .2s ease,text-decoration-color .2s ease;
}

.ft-23__secondary:hover {
  color: var(--ft-23-fink);
  text-decoration-color: currentColor;
}

.ft-23__primary:focus-visible,
.ft-23__secondary:focus-visible,
.ft-23__link:focus-visible,
.ft-23__slink:focus-visible {
  outline: 2px solid var(--ft-23-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.ft-23__trust {
  font-size: 13px;
  color: oklch(0.8 0.015 200);
}

.ft-23__nowrap {
  white-space: nowrap;
}

.ft-23__links {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(10.5rem,1fr));
  gap: clamp(22px,3vw,36px) clamp(16px,2.2vw,28px);
  padding-block: clamp(30px,4vw,48px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1120px)/2));
}

.ft-23__brandcol {
  display: grid;
  align-content: start;
  gap: 10px;
  min-width: 0;
}

.ft-23__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -.025em;
}

.ft-23__mark {
  width: 24px;
  height: 24px;
  border-radius: 8px;
  background: linear-gradient(140deg,var(--ft-23-acc),oklch(0.66 0.15 200));
}

.ft-23__blurb {
  font-size: 14px;
  line-height: 1.55;
  color: var(--ft-23-fmut);
  max-width: 28ch;
}

.ft-23__col {
  display: grid;
  align-content: start;
  gap: 4px;
  min-width: 0;
}

.ft-23__chh {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  margin-block-end: 8px;
}

.ft-23__list {
  display: grid;
  gap: 1px;
}

.ft-23__link {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  font-size: 14.2px;
  color: var(--ft-23-fmut);
  text-decoration: none;
  width: fit-content;
  transition: color .18s ease,translate .18s ease;
}

.ft-23__link:hover {
  color: var(--ft-23-acc);
  translate: 3px 0;
}

.ft-23__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px 22px;
  padding-block: 18px;
  padding-bottom: calc(18px + env(safe-area-inset-bottom,0px));
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1120px)/2));
  border-top: 1px solid var(--ft-23-line);
}

.ft-23__copy {
  font-size: 12.8px;
  color: var(--ft-23-fmut);
}

.ft-23__legal {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 16px;
  margin-inline-start: auto;
}

.ft-23__slink {
  display: flex;
  align-items: center;
  min-height: 36px;
  font-size: 12.8px;
  color: var(--ft-23-fmut);
  text-decoration: none;
}

.ft-23__slink:hover {
  color: var(--ft-23-fink);
  text-decoration: underline;
  text-underline-offset: .25em;
}

@media (max-width: 560px) {
  .ft-23__legal {
    margin-inline-start: 0;
  }

  .ft-23__cta {
    clip-path: polygon(0 0,100% 18px,100% 100%,0 100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-23 * {
    transition-duration: .01ms !important;
  }
}
```
