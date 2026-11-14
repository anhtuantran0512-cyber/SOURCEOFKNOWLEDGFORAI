---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/fork-me-on-github-corner-ribbon/"
title: "Fork Me on GitHub Corner Ribbon"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "The developer-portfolio classic, rebuilt for 2027: no 6 KB PNG, no SVG octocat, no position: fixed that breaks in a scroll container."
has_js: "false"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fork Me on GitHub Corner Ribbon
Source: https://codefronts.com/snippets/css-ribbons/fork-me-on-github-corner-ribbon/

The developer-portfolio classic, rebuilt for 2027: no 6 KB PNG, no SVG octocat, no position: fixed that breaks in a scroll container. A single anchor, two dashed stitch lines drawn with border, an inline SVG glyph, and a hover state that pushes the whole band a couple of pixels further out of the corner. Left and right variants share one rule set — the side is a custom property.
## HTML
```html
<section class="rib-04" aria-label="GitHub style fork me corner ribbon demo">
  <div class="rib-04__stage">
    <div class="rib-04__window">
      <div class="rib-04__chrome" aria-hidden="true"><span class="rib-04__dot"></span><span class="rib-04__dot"></span><span class="rib-04__dot"></span><span class="rib-04__url">ribbonkit.dev</span></div>
      <div class="rib-04__page">
        <div class="rib-04__corner rib-04__corner--br">
          <a class="rib-04__link" href="https://github.com/" rel="noopener">
            <svg class="rib-04__glyph" viewBox="0 0 16 16" width="15" height="15" aria-hidden="true" focusable="false"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>Star on GitHub</span>
          </a>
        </div>
        <div class="rib-04__corner">
          <a class="rib-04__link" href="https://github.com/" rel="noopener">
            <span>Fork me on GitHub</span>
            <svg class="rib-04__glyph" viewBox="0 0 16 16" width="15" height="15" aria-hidden="true" focusable="false"><path fill="currentColor" d="M5 3.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Zm0 2.122a2.25 2.25 0 1 0-1.5 0v.878A2.25 2.25 0 0 0 5.75 8.5h1.5v2.128a2.251 2.251 0 1 0 1.5 0V8.5h1.5a2.25 2.25 0 0 0 2.25-2.25v-.878a2.25 2.25 0 1 0-1.5 0v.878a.75.75 0 0 1-.75.75h-4.5A.75.75 0 0 1 5 6.25v-.878ZM12.75 2.5a.75.75 0 1 1 0 1.5.75.75 0 0 1 0-1.5ZM8.75 13.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z"/></svg>
          </a>
        </div>
        <div class="rib-04__content">
          <p class="rib-04__eyebrow">Open source</p>
          <h2 class="rib-04__head">ribbon-kit</h2>
          <p class="rib-04__lede">Twenty accessible, dependency-free CSS ribbon primitives. Copy the markup, keep the semantics, ship in an afternoon.</p>
          <pre class="rib-04__code" tabindex="0" aria-label="Install command"><code><span class="rib-04__tok">npm</span> i ribbon-kit <span class="rib-04__cm"># or just copy the CSS</span></code></pre>
          <p class="rib-04__meta"><span>MIT</span><span>·</span><span>4.1 kB gzipped</span><span>·</span><span>Zero dependencies</span></p>
        </div>
      </div>
    </div>
    <p class="rib-04__chip" aria-hidden="true">pointer-events none/auto pair · negative outline-offset · dashed stitch · mirrored ±45° corners</p>
  </div>
</section>
```
## CSS
```css
.rib-04,
.rib-04 *,
.rib-04 *::before,
.rib-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-04-bg: #0c0f14;
  --rib-04-bg: oklch(0.17 0.014 255);
  --rib-04-page: #11151c;
  --rib-04-page: oklch(0.21 0.016 258);
  --rib-04-ink: #e9edf3;
  --rib-04-ink: oklch(0.94 0.008 255);
  --rib-04-mut: #8b95a4;
  --rib-04-mut: oklch(0.66 0.018 258);
  --rib-04-acc: #2f7d4f;
  --rib-04-acc: oklch(0.56 0.15 152);
  --rib-04-acc2: #6c5ce7;
  --rib-04-acc2: oklch(0.55 0.2 285);
  --rib-04-size: clamp(130px,21vw,152px);
  --rib-04-band: 34px;
  --rib-04-offset: calc(var(--rib-04-size) / 2 - var(--rib-04-band) / 2);
  --rib-04-len: calc(var(--rib-04-size) * 1.415 + var(--rib-04-band) * 2);
  background: var(--rib-04-bg);
  color: var(--rib-04-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-04__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,3vw,26px);
  padding: clamp(16px,4vw,48px);
}

.rib-04__window {
  width: min(100%,860px);
  border-radius: 18px;
  overflow: hidden;
  background: var(--rib-04-page);
  border: 1px solid oklch(1 0 0/.1);
  box-shadow: 0 40px 90px -40px oklch(0 0 0/.9);
}

.rib-04__chrome {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 12px 16px;
  background: oklch(0 0 0/.25);
  border-bottom: 1px solid oklch(1 0 0/.07);
}

.rib-04__dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: oklch(1 0 0/.18);
}

.rib-04__url {
  margin-left: 12px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-04-mut);
}

.rib-04__page {
  position: relative;
  overflow: hidden;
  min-height: clamp(380px,52vh,440px);
  padding: clamp(28px,6vw,60px);
  display: grid;
  align-content: center;
  background: radial-gradient(80% 60% at 80% 0%,color-mix(in oklch,var(--rib-04-acc2) 16%,transparent),transparent 60%);
}

.rib-04__corner {
  position: absolute;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
  z-index: 5;
  filter: drop-shadow(0 6px 14px oklch(0 0 0/.6));
}

.rib-04__link {
  pointer-events: auto;
  position: absolute;
  inset-block-start: var(--rib-04-offset);
  inset-inline-end: calc((var(--rib-04-len) - var(--rib-04-size)) / -2);
  inline-size: var(--rib-04-len);
  min-block-size: var(--rib-04-band);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  rotate: 45deg;
  background: #2f7d4f;
  background: linear-gradient(180deg,color-mix(in oklch,var(--rib-04-acc) 82%,white),var(--rib-04-acc));
  color: oklch(0.99 0 0);
  font-size: clamp(11px,2.2vw,12.5px);
  font-weight: 700;
  letter-spacing: .04em;
  text-decoration: none;
  white-space: nowrap;
  border-block: 1px dashed oklch(1 0 0/.5);
  transition: translate .28s cubic-bezier(.16,1,.3,1),filter .28s;
}

.rib-04__corner--br .rib-04__link {
  inset-block-start: auto;
  inset-block-end: var(--rib-04-offset);
  rotate: -45deg;
  background: #6c5ce7;
  background: linear-gradient(180deg,color-mix(in oklch,var(--rib-04-acc2) 84%,white),var(--rib-04-acc2));
}

.rib-04__link:hover {
  translate: 0 -3px;
  filter: brightness(1.07);
}

.rib-04__corner--br .rib-04__link:hover {
  translate: 0 3px;
}

.rib-04__link:focus-visible {
  outline: 3px solid oklch(0.99 0 0);
  outline-offset: -7px;
}

.rib-04__glyph {
  flex: none;
  display: block;
}

.rib-04__content {
  display: grid;
  gap: 12px;
  max-width: 44ch;
}

.rib-04__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--rib-04-acc2);
}

.rib-04__head {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(28px,5.4vw,44px);
  font-weight: 600;
  letter-spacing: -.04em;
}

.rib-04__lede {
  font-size: clamp(14px,2.4vw,16px);
  line-height: 1.6;
  color: var(--rib-04-mut);
  text-wrap: pretty;
}

.rib-04__code {
  margin-top: 6px;
  padding: 14px 16px;
  border-radius: 12px;
  background: oklch(0 0 0/.4);
  border: 1px solid oklch(1 0 0/.09);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13px;
  color: var(--rib-04-ink);
  overflow-x: auto;
}

.rib-04__code:focus-visible {
  outline: 2px solid var(--rib-04-acc2);
  outline-offset: 2px;
}

.rib-04__tok {
  color: var(--rib-04-acc);
}

.rib-04__cm {
  color: var(--rib-04-mut);
}

.rib-04__meta {
  display: flex;
  flex-wrap: wrap;
  gap: 9px;
  font-size: 12.5px;
  color: var(--rib-04-mut);
}

.rib-04__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-04-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (max-width: 520px) {
  .rib-04__corner--br {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rib-04 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
