---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/text-swap-flip-up-effect/"
title: "Text Swap / Flip Up Effect"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Nav links that swap languages on hover — English slides up and out, Japanese slides in from below, in a clipped two-storey elevator built from one absolute…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Text Swap / Flip Up Effect
Source: https://codefronts.com/motion/css-text-hover-effects/text-swap-flip-up-effect/

Nav links that swap languages on hover — English slides up and out, Japanese slides in from below, in a clipped two-storey elevator built from one absolute span and translateY. Next to it, the rolodex version: the same swap performed as a real 3D flip, two faces mounted on an invisible prism rotating around rotateX. Both keep exactly one label in the accessibility tree; the decorative twin is aria-hidden, so screen readers hear 'Works', never 'Works 作品'.
## HTML
```html
<section class="cth-05" aria-label="Text swap and flip up demo">
  <div class="cth-05__stage">
    <div class="cth-05__scene">
      <header class="cth-05__head">
        <p class="cth-05__eyebrow">Atelier Kōyō &mdash; Kyoto / Melbourne</p>
        <span class="cth-05__chip">EN &harr; JA on hover</span>
      </header>
      <nav class="cth-05__nav" aria-label="Primary">
        <a class="cth-05__swap" href="#cth05-top" id="cth05-top"><span class="cth-05__top">Works</span><span class="cth-05__alt" aria-hidden="true" lang="ja">作品</span></a>
        <a class="cth-05__swap" href="#cth05-top"><span class="cth-05__top">Studio</span><span class="cth-05__alt" aria-hidden="true" lang="ja">工房</span></a>
        <a class="cth-05__swap" href="#cth05-top"><span class="cth-05__top">Journal</span><span class="cth-05__alt" aria-hidden="true" lang="ja">日誌</span></a>
        <a class="cth-05__swap" href="#cth05-top"><span class="cth-05__top">Contact</span><span class="cth-05__alt" aria-hidden="true" lang="ja">連絡</span></a>
      </nav>
      <div class="cth-05__row">
        <a class="cth-05__roll" href="#cth05-top" aria-label="Commissions, open for autumn">
          <span class="cth-05__core" aria-hidden="true">
            <span class="cth-05__face cth-05__face--front">Commissions</span>
            <span class="cth-05__face cth-05__face--alt">Open for autumn</span>
          </span>
        </a>
        <p class="cth-05__label">&larr; the rolodex: a real <code>rotateX</code> prism, not a slide</p>
      </div>
      <p class="cth-05__hint">Hover or <kbd>Tab</kbd>. The Japanese twins are <code>aria-hidden</code> &mdash; screen readers hear one language, not both.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-05,
.cth-05 *,
.cth-05 *::before,
.cth-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-05 {
  --bg: oklch(0.968 0.005 110);
  --ink: oklch(0.23 0.012 130);
  --mut: oklch(0.52 0.015 125);
  --acc: oklch(0.56 0.15 145);
  --line: oklch(0.885 0.01 115);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-05__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: var(--bg);
  padding: clamp(20px,4vw,56px);
  container: cth05/inline-size;
}

.cth-05__scene {
  width: min(100%,760px);
  display: flex;
  flex-direction: column;
  gap: clamp(20px,3.4cqi,30px);
}

.cth-05__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
  padding-bottom: 14px;
  border-bottom: 1.5px solid var(--ink);
}

.cth-05__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-05__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--acc);
  border: 1px solid color-mix(in oklch,var(--acc) 40%,transparent);
  border-radius: 99px;
  padding: 5px 11px;
}

.cth-05__nav {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(6px,1.6cqi,14px);
}

.cth-05__swap {
  position: relative;
  overflow: clip;
  display: inline-block;
  padding: .3em .45em;
  font-size: clamp(26px,5.4cqi,44px);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.15;
  color: inherit;
  text-decoration: none;
  border-radius: 8px;
}

.cth-05__swap:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cth-05__top {
  display: block;
  transition: transform .45s cubic-bezier(.76,0,.24,1);
}

.cth-05__alt {
  position: absolute;
  inset: .3em .45em;
  display: block;
  color: var(--acc);
  transform: translateY(150%);
  transition: transform .45s cubic-bezier(.76,0,.24,1);
}

.cth-05__swap:hover .cth-05__top,
.cth-05__swap:focus-visible .cth-05__top {
  transform: translateY(-150%);
}

.cth-05__swap:hover .cth-05__alt,
.cth-05__swap:focus-visible .cth-05__alt {
  transform: translateY(0);
}

.cth-05__row {
  display: flex;
  align-items: center;
  gap: clamp(14px,3cqi,24px);
  flex-wrap: wrap;
}

.cth-05__roll {
  display: inline-block;
  perspective: 900px;
  text-decoration: none;
  border-radius: 10px;
}

.cth-05__roll:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 4px;
}

.cth-05__core {
  position: relative;
  display: block;
  transform-style: preserve-3d;
  transition: transform .55s cubic-bezier(.68,-0.15,.27,1.15);
  font-size: clamp(19px,3cqi,25px);
  font-weight: 750;
  line-height: 1;
  height: 1em;
}

.cth-05__face {
  display: flex;
  align-items: center;
  height: 1em;
  white-space: nowrap;
  backface-visibility: hidden;
}

.cth-05__face--front {
  color: var(--ink);
  transform: translateZ(.52em);
}

.cth-05__face--alt {
  position: absolute;
  inset: 0;
  color: var(--acc);
  transform: rotateX(90deg) translateZ(.52em);
}

.cth-05__roll:hover .cth-05__core,
.cth-05__roll:focus-visible .cth-05__core {
  transform: rotateX(-90deg);
}

.cth-05__label {
  font-size: 13px;
  color: var(--mut);
}

.cth-05__label code,
.cth-05__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.92 0.008 115);
  padding: 1px 6px;
  border-radius: 4px;
}

.cth-05__hint {
  font-size: 12.5px;
  color: var(--mut);
}

.cth-05__hint kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  border: 1px solid var(--line);
  border-bottom-width: 2px;
  border-radius: 5px;
  padding: 2px 6px;
  background: oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cth-05 * {
    transition-duration: .01ms !important;
  }
}
```
