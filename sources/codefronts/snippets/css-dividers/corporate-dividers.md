---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/corporate-dividers/"
title: "Vertical Flexbox Divider Line CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Vertical rules between nav links, header stats and toolbar groups — the divider people hand-code wrong most often."
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Flexbox Divider Line CSS
Source: https://codefronts.com/snippets/css-dividers/corporate-dividers/

Vertical rules between nav links, header stats and toolbar groups — the divider people hand-code wrong most often. The correct answer is a sibling selector plus align-self:stretch, so the rule is exactly as tall as the tallest item, never a fixed pixel height. Includes the flex-wrap trap that makes stretch rules look broken, and the one-line fix.
## HTML
```html
<section class="div-25" aria-label="Vertical flexbox divider demo">
  <div class="div-25__stage">
    <nav class="div-25__nav" aria-label="Demo navigation">
      <a href="#div-25">Overview</a><a href="#div-25">Pricing</a><a href="#div-25">Docs</a><a href="#div-25">Changelog</a>
    </nav>
    <div class="div-25__stats">
      <div class="div-25__stat"><p class="div-25__v">26</p><p class="div-25__k">Dividers</p></div>
      <div class="div-25__stat"><p class="div-25__v">4</p><p class="div-25__k">With JS</p></div>
      <div class="div-25__stat"><p class="div-25__v">0</p><p class="div-25__k">Dependencies</p></div>
    </div>
    <div class="div-25__bar">
      <span class="div-25__tool">Bold</span><span class="div-25__tool">Italic</span>
      <span class="div-25__vr" role="separator" aria-orientation="vertical"></span>
      <span class="div-25__tool">Left</span><span class="div-25__tool">Center</span>
      <span class="div-25__vr" role="separator" aria-orientation="vertical"></span>
      <span class="div-25__tool">Link</span>
    </div>
    <p class="div-25__chip">* + *::before · align-self:stretch · axis flip on wrap</p>
  </div>
</section>
```
## CSS
```css
.div-25 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-25-bg);
  --div-25-bg: oklch(0.97 0.005 250);
  --div-25-card: oklch(1 0 0);
  --div-25-ink: oklch(0.23 0.018 260);
  --div-25-mut: oklch(0.55 0.018 260);
  --div-25-line: oklch(0.23 0.018 260/.18);
  --div-25-acc: oklch(0.58 0.16 262);
  --div-25-gap: 24px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-25-ink);
}

.div-25 *,
.div-25 *::before,
.div-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-25__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(20px,4vw,34px);
  padding: clamp(28px,6vw,72px) clamp(20px,5vw,56px);
}

.div-25__nav {
  display: flex;
  align-items: stretch;
  gap: var(--div-25-gap);
  background: var(--div-25-card);
  border: 1px solid var(--div-25-line);
  border-radius: 99px;
  padding: 10px 24px;
  box-shadow: 0 8px 26px oklch(0.23 0.018 260/.07);
  flex-wrap: wrap;
  justify-content: center;
}

.div-25__nav a {
  position: relative;
  display: inline-flex;
  align-items: center;
  min-height: 32px;
  font-size: 14px;
  font-weight: 600;
  color: var(--div-25-mut);
  text-decoration: none;
  transition: color .18s ease;
}

.div-25__nav a:hover,
.div-25__nav a:focus-visible {
  color: var(--div-25-acc);
}

.div-25__nav a:focus-visible {
  outline: 2px solid var(--div-25-acc);
  outline-offset: 4px;
  border-radius: 6px;
}

.div-25__nav a+a::before {
  content: '';
  position: absolute;
  left: calc(var(--div-25-gap) / -2);
  inset-block: 6px;
  width: 1px;
  background: var(--div-25-line);
}

.div-25__stats {
  display: flex;
  align-items: stretch;
  gap: var(--div-25-gap);
  flex-wrap: wrap;
  justify-content: center;
}

.div-25__stat {
  position: relative;
  padding: 6px 10px;
  text-align: center;
  min-width: 104px;
}

.div-25__stat+.div-25__stat::before {
  content: '';
  position: absolute;
  left: calc(var(--div-25-gap) / -2);
  inset-block: 2px;
  width: 1px;
  background: linear-gradient(180deg,transparent,var(--div-25-line) 22%,var(--div-25-line) 78%,transparent);
}

.div-25__v {
  font-size: clamp(28px,5vw,42px);
  font-weight: 720;
  letter-spacing: -.035em;
  line-height: 1;
  color: var(--div-25-acc);
}

.div-25__k {
  margin-top: 6px;
  font-size: 11.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--div-25-mut);
}

.div-25__bar {
  display: flex;
  align-items: stretch;
  gap: 6px;
  background: var(--div-25-card);
  border: 1px solid var(--div-25-line);
  border-radius: 12px;
  padding: 6px;
  box-shadow: 0 6px 20px oklch(0.23 0.018 260/.07);
  flex-wrap: wrap;
  justify-content: center;
}

.div-25__tool {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  padding: 0 13px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  color: var(--div-25-mut);
  cursor: default;
  transition: background .16s ease,color .16s ease;
}

.div-25__tool:hover {
  background: color-mix(in oklch,var(--div-25-acc) 10%,transparent);
  color: var(--div-25-acc);
}

.div-25__vr {
  align-self: stretch;
  width: 1px;
  flex: none;
  background: var(--div-25-line);
  margin-inline: 5px;
}

@media (max-width: 420px) {
  .div-25__stats {
    flex-direction: column;
    align-items: center;
  }

  .div-25__stat+.div-25__stat::before {
    left: 0;
    right: 0;
    width: auto;
    height: 1px;
    inset-block: auto;
    top: calc(var(--div-25-gap) / -2);
    background: linear-gradient(90deg,transparent,var(--div-25-line),transparent);
  }
}

.div-25__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-25-mut);
  padding: 8px 14px;
  border: 1px solid var(--div-25-line);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .div-25 * {
    transition-duration: .01ms !important;
  }
}
```
