---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/css-cookie-consent-banner-bottom/"
title: "Cookie Consent Banner Bottom Bar"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "The utilitarian counterpart to demo 01: a bottom bar with no JavaScript whatsoever."
has_js: "false"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cookie Consent Banner Bottom Bar
Source: https://codefronts.com/snippets/css-banners-alerts/css-cookie-consent-banner-bottom/

The utilitarian counterpart to demo 01: a bottom bar with no JavaScript whatsoever. Accept, reject and a settings disclosure are all CSS state — :has(:checked) for the dismiss, <details> for the policy detail — set in a mono/system type pairing with a hard 3:1 border and env(safe-area-inset-bottom) so it clears the iOS home indicator.
## HTML
```html
<div class="ba-13">
  <input class="ba-13__vh" type="radio" name="ba-13-c" id="ba-13-accept">
  <input class="ba-13__vh" type="radio" name="ba-13-c" id="ba-13-reject">

  <main class="ba-13__page">
    <p class="ba-13__crumb">Docs / Runtime / Edge functions</p>
    <h1>Edge functions</h1>
    <p>Deploy a function to 34 regions from one command. Cold starts are typically under 12ms because the runtime is already resident at the edge.</p>
    <pre class="ba-13__code"><code>npx edge deploy ./handler.ts --regions all</code></pre>
    <p>Functions inherit the project's environment variables and secrets. Streaming responses, request coalescing and per-region caching are on by default.</p>
    <ul class="ba-13__list">
      <li>Zero-config TypeScript, ESM only</li>
      <li>Streaming and <code>ReadableStream</code> responses</li>
      <li>Per-region cache with tag invalidation</li>
      <li>Cold start p95 under 12ms</li>
    </ul>
  </main>

  <aside class="ba-13__bar" role="region" aria-labelledby="ba-13-h">
    <div class="ba-13__copy">
      <h2 class="ba-13__h" id="ba-13-h">Cookies on this site</h2>
      <p class="ba-13__text">We use essential cookies to run the docs and optional analytics cookies to see which pages get read. You can change this any time from the footer.</p>
      <details class="ba-13__more">
        <summary>What we store</summary>
        <div class="ba-13__moreInner">
          <dl>
            <dt>Essential</dt><dd>Session id, CSRF token, theme choice. Expires with the session.</dd>
            <dt>Analytics</dt><dd>Anonymised page views and search terms, aggregated daily. 90 days.</dd>
            <dt>Never used</dt><dd>Advertising, cross-site identifiers, fingerprinting, session replay.</dd>
          </dl>
        </div>
      </details>
      <nav class="ba-13__links" aria-label="Policies">
        <a href="#ba-13-h">Cookie policy</a>
        <a href="#ba-13-h">Privacy</a>
        <a href="#ba-13-h">Sub-processors</a>
      </nav>
    </div>

    <div class="ba-13__choices">
      <label class="ba-13__btn ba-13__btn--solid" for="ba-13-accept" tabindex="0" role="button">Accept analytics</label>
      <label class="ba-13__btn" for="ba-13-reject" tabindex="0" role="button">Essential only</label>
    </div>
  </aside>

  <p class="ba-13__receipt" data-receipt aria-hidden="true"></p>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');

.ba-13 {
  --bar-max: 100%;
  --edge: 1px;
  color-scheme: light dark;
  --paper: #ffffff;
  --ink: #0c0d10;
  --muted: #5d626b;
  --line: #e3e5e9;
  --bar: #0c0d10;
  --bar-ink: #f7f8fa;
  --acc: #00d47e;
  --sans: "IBM Plex Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-13 *,
.ba-13 *::before,
.ba-13 *::after {
  box-sizing: border-box;
}

@supports (color: light-dark(#fff,#000)) {
  .ba-13 {
    --paper: light-dark(#ffffff,#0a0b0d);
    --ink: light-dark(#0c0d10,#f3f5f7);
    --muted: light-dark(#5d626b,#989ea8);
    --line: light-dark(#e3e5e9,#22252a);
    --bar: light-dark(#0c0d10,#14161a);
    --bar-ink: light-dark(#f7f8fa,#f3f5f7);
    --acc: light-dark(#00a862,#00d47e);
  }
}

.ba-13__page {
  max-width: 46rem;
  margin-inline: auto;
  padding: clamp(2rem,7vh,4rem) clamp(1.25rem,5vw,2rem) clamp(18rem,40vh,26rem);
  display: grid;
  gap: 1rem;
}

.ba-13__crumb {
  margin: 0;
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--muted);
  letter-spacing: .02em;
}

.ba-13__page h1 {
  margin: 0;
  font-size: clamp(2rem,6vw,3rem);
  font-weight: 600;
  letter-spacing: -.045em;
  line-height: 1.02;
}

.ba-13__page p {
  margin: 0;
  font-size: 1.0625rem;
  line-height: 1.7;
  color: var(--muted);
  max-width: 68ch;
  text-wrap: pretty;
}

.ba-13__code {
  margin: 0;
  padding: 1rem 1.1rem;
  border-radius: .75rem;
  overflow-x: auto;
  font-family: var(--mono);
  font-size: .875rem;
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
  border: 1px solid var(--line);
}

.ba-13__list {
  margin: 0;
  padding: 0 0 0 1.1rem;
  display: grid;
  gap: .4rem;
  font-size: .9375rem;
  color: var(--muted);
}

.ba-13__list code {
  font-family: var(--mono);
  font-size: .9em;
}

.ba-13__bar {
  position: fixed;
  z-index: 10;
  inset: auto 0 0 0;
  max-inline-size: var(--bar-max);
  margin-inline: auto;
  display: grid;
  grid-template-columns: 1fr auto;
  gap: clamp(1rem,3vw,2.5rem);
  align-items: center;
  padding: 1.15rem clamp(1rem,4vw,2rem);
  padding-block-end: calc(1.15rem + env(safe-area-inset-bottom, 0px));
  background: var(--bar);
  color: var(--bar-ink);
  border-block-start: var(--edge) solid color-mix(in oklab,var(--bar-ink) 30%,transparent);
  transition: translate .4s cubic-bezier(.16,1,.3,1), opacity .3s ease, display .4s allow-discrete;
}

@starting-style {
  .ba-13__bar {
    translate: 0 100%;
    opacity: 0;
  }
}

.ba-13:has(input[name="ba-13-c"]:checked) .ba-13__bar {
  display: none;
  translate: 0 100%;
  opacity: 0;
}

.ba-13__copy {
  min-width: 0;
  display: grid;
  gap: .45rem;
}

.ba-13__h {
  margin: 0;
  font-family: var(--mono);
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--acc);
}

.ba-13__text {
  margin: 0;
  font-size: .875rem;
  line-height: 1.6;
  color: color-mix(in oklab,var(--bar-ink) 76%,transparent);
  max-width: 72ch;
  text-wrap: pretty;
}

.ba-13__more {
  margin-block-start: .15rem;
}

.ba-13__more summary {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  min-height: 2rem;
  cursor: pointer;
  list-style: none;
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: color-mix(in oklab,var(--bar-ink) 60%,transparent);
}

.ba-13__more summary::-webkit-details-marker {
  display: none;
}

.ba-13__more summary::after {
  content: "+";
  font-weight: 600;
}

.ba-13__more[open] summary::after {
  content: "−";
}

.ba-13__more summary:hover {
  color: var(--bar-ink);
}

.ba-13__moreInner {
  padding-block: .5rem 0;
}

.ba-13__moreInner dl {
  margin: 0;
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .3rem .85rem;
  font-size: .75rem;
  line-height: 1.55;
  color: color-mix(in oklab,var(--bar-ink) 70%,transparent);
}

.ba-13__moreInner dt {
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--bar-ink);
}

.ba-13__moreInner dd {
  margin: 0;
  max-width: 60ch;
}

.ba-13__links {
  display: flex;
  flex-wrap: wrap;
  gap: .85rem;
  margin-block-start: .15rem;
}

.ba-13__links a {
  font-size: .75rem;
  color: color-mix(in oklab,var(--bar-ink) 62%,transparent);
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-thickness: 1px;
}

.ba-13__links a:hover {
  color: var(--acc);
}

.ba-13__choices {
  display: flex;
  gap: .5rem;
  flex-wrap: wrap;
}

.ba-13__btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2.9rem;
  min-width: 11rem;
  padding: .8rem 1.25rem;
  cursor: pointer;
  font-family: var(--mono);
  font-size: .8125rem;
  font-weight: 500;
  letter-spacing: .04em;
  color: var(--bar-ink);
  border: 1px solid color-mix(in oklab,var(--bar-ink) 34%,transparent);
  border-radius: .5rem;
  transition: background .2s ease, color .2s ease, border-color .2s ease;
}

.ba-13__btn:hover {
  background: color-mix(in oklab,var(--bar-ink) 12%,transparent);
  border-color: var(--bar-ink);
}

.ba-13__btn--solid {
  background: var(--acc);
  color: #04150d;
  border-color: var(--acc);
}

.ba-13__btn--solid:hover {
  background: color-mix(in oklab,var(--acc) 82%,white);
  border-color: transparent;
}

.ba-13__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.ba-13__receipt {
  position: fixed;
  inset: auto 50% 1rem auto;
  translate: 50% 0;
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--muted);
  opacity: 0;
  transition: opacity .3s ease .2s;
}

.ba-13:has(input[name="ba-13-c"]:checked) .ba-13__receipt {
  opacity: 1;
}

.ba-13:has(#ba-13-accept:checked) .ba-13__receipt::after {
  content: "Preference saved · analytics on";
}

.ba-13:has(#ba-13-reject:checked) .ba-13__receipt::after {
  content: "Preference saved · essential only";
}

.ba-13__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.ba-13 a {
  color: var(--acc);
}

.ba-13 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@media (max-width: 52rem) {
  .ba-13__bar {
    grid-template-columns: 1fr;
  }

  .ba-13__btn {
    flex: 1 1 100%;
    min-width: 0;
  }
}

@media (prefers-contrast: more) {
  .ba-13__bar {
    --edge: 3px;
  }

  .ba-13__text {
    color: var(--bar-ink);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-13 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-13__bar {
    border-block-start: 2px solid CanvasText;
  }

  .ba-13__btn--solid {
    background: Highlight;
    color: HighlightText;
  }
}
```
