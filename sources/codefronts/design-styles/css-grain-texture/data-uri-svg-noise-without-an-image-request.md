---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/data-uri-svg-noise-without-an-image-request/"
title: "Data URI SVG Noise Without an Image Request"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "The shippable form of browser-generated grain: the whole <feTurbulence> document folded into a URL-encoded data URI, parked in one custom property, and…"
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Data URI SVG Noise Without an Image Request
Source: https://codefronts.com/design-styles/css-grain-texture/data-uri-svg-noise-without-an-image-request/

The shippable form of browser-generated grain: the whole <feTurbulence> document folded into a URL-encoded data URI, parked in one custom property, and reused across a hero, a pricing card, a footer and a button. About 380 bytes, one CSS declaration, zero network requests — and no SVG block in your markup at all.
## HTML
```html
<section class="grn-03" aria-labelledby="grn-03-title">
  <div class="grn-03__theme">
    <input class="grn-03__theme-input" type="checkbox" id="grn-03-theme">
    <label class="grn-03__theme-label" for="grn-03-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-03__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="grn-03__hero">
    <div class="grn-03__hero-inner">
      <p class="grn-03__badge"><span class="grn-03__dot" aria-hidden="true"></span>382 bytes · 0 requests</p>
      <h1 class="grn-03__h1" id="grn-03-title">One texture token. Six surfaces. Nothing fetched.</h1>
      <p class="grn-03__lede">Every grained surface on this page reads the same <code>--grn-03-noise</code> custom property. The texture ships inside the stylesheet as a URL-encoded SVG, so the fifth and sixth uses cost nothing at all.</p>
      <div class="grn-03__cta-row">
        <a class="grn-03__cta" href="#grn-03-title">Copy the token</a>
        <a class="grn-03__cta grn-03__cta--ghost" href="#grn-03-title">Read the encoding rules</a>
      </div>
    </div>
  </header>

  <main class="grn-03__main">
    <section class="grn-03__cards" aria-labelledby="grn-03-h-cards">
      <h2 class="grn-03__sr" id="grn-03-h-cards">Surfaces using the token</h2>

      <article class="grn-03__card">
        <h3 class="grn-03__card-h">Starter</h3>
        <p class="grn-03__price">Free<span>forever</span></p>
        <ul class="grn-03__list">
          <li>One texture token</li>
          <li>Fine, medium, coarse presets</li>
          <li>Unlimited surfaces</li>
        </ul>
        <a class="grn-03__card-cta" href="#grn-03-title">Start here</a>
      </article>

      <article class="grn-03__card grn-03__card--feature">
        <p class="grn-03__flag">Recommended</p>
        <h3 class="grn-03__card-h">Studio</h3>
        <p class="grn-03__price">$0<span>it is CSS</span></p>
        <ul class="grn-03__list">
          <li>Everything in Starter</li>
          <li>Per-surface blend modes</li>
          <li>Dark-mode grain balance</li>
        </ul>
        <a class="grn-03__card-cta" href="#grn-03-title">Use in production</a>
      </article>

      <article class="grn-03__card">
        <h3 class="grn-03__card-h">Legacy PNG</h3>
        <p class="grn-03__price">148KB<span>per tile</span></p>
        <ul class="grn-03__list grn-03__list--strike">
          <li>Extra network request</li>
          <li>Visible tiling seams</li>
          <li>Cannot be themed</li>
        </ul>
        <a class="grn-03__card-cta grn-03__card-cta--muted" href="#grn-03-title">Not this one</a>
      </article>
    </section>

    <section class="grn-03__strip" aria-labelledby="grn-03-h-strip">
      <h2 class="grn-03__h2" id="grn-03-h-strip">The four characters that break it</h2>
      <dl class="grn-03__esc">
        <div><dt>&lt;</dt><dd>%3C</dd></div>
        <div><dt>&gt;</dt><dd>%3E</dd></div>
        <div><dt>#</dt><dd>%23</dd></div>
        <div><dt>%</dt><dd>%25</dd></div>
      </dl>
      <p class="grn-03__strip-note">An unescaped <code>#</code> truncates the URI at the first filter reference. No background, no error, one lost hour.</p>
    </section>
  </main>

  <footer class="grn-03__foot">
    <p class="grn-03__foot-line">Grained footer, grained hero, grained cards, grained buttons — one declaration.</p>
  </footer>
</section>
```
## CSS
```css
.grn-03 {
  --grn-03-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='grn03n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='140' height='140' filter='url(%23grn03n)' opacity='0.6'/%3E%3C/svg%3E");
  --grn-03-bg: #101211;
  --grn-03-surf: #191d1b;
  --grn-03-line: #2c332f;
  --grn-03-ink: #eef3ef;
  --grn-03-mut: #93a29a;
  --grn-03-acc: #a3e635;
  --grn-03-acc: oklch(85% 0.2 125);
  --grn-03-on-acc: #14210a;
  --grn-03-grain: 0.5;
  --grn-03-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-03-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-03-bg);
  color: var(--grn-03-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-03 *,
.grn-03 *::before,
.grn-03 *::after {
  box-sizing: border-box;
}

.grn-03 :focus-visible {
  outline: 2px solid var(--grn-03-acc);
  outline-offset: 3px;
}

.grn-03 code {
  font-family: var(--grn-03-font-mono);
  font-size: 0.9em;
}

.grn-03__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.grn-03:has(.grn-03__theme-input:checked) {
  --grn-03-bg: #f2f5f0;
  --grn-03-surf: #ffffff;
  --grn-03-line: #d8e0d6;
  --grn-03-ink: #101211;
  --grn-03-mut: #5d6a62;
  --grn-03-acc: #4d7c0f;
  --grn-03-acc: oklch(52% 0.14 128);
  --grn-03-on-acc: #f7fee7;
  --grn-03-grain: 0.32;
}

@media (prefers-color-scheme: light) {
  .grn-03 {
    --grn-03-bg: #f2f5f0;
    --grn-03-surf: #ffffff;
    --grn-03-line: #d8e0d6;
    --grn-03-ink: #101211;
    --grn-03-mut: #5d6a62;
    --grn-03-acc: #4d7c0f;
    --grn-03-acc: oklch(52% 0.14 128);
    --grn-03-on-acc: #f7fee7;
    --grn-03-grain: 0.32;
  }

  .grn-03:has(.grn-03__theme-input:checked) {
    --grn-03-bg: #101211;
    --grn-03-surf: #191d1b;
    --grn-03-line: #2c332f;
    --grn-03-ink: #eef3ef;
    --grn-03-mut: #93a29a;
    --grn-03-acc: #a3e635;
    --grn-03-acc: oklch(85% 0.2 125);
    --grn-03-on-acc: #14210a;
    --grn-03-grain: 0.5;
  }
}

@media (prefers-color-scheme: dark) {
  .grn-03:has(.grn-03__theme-input:checked) {
    --grn-03-bg: #f2f5f0;
    --grn-03-surf: #ffffff;
    --grn-03-line: #d8e0d6;
    --grn-03-ink: #101211;
    --grn-03-mut: #5d6a62;
    --grn-03-acc: #4d7c0f;
    --grn-03-acc: oklch(52% 0.14 128);
    --grn-03-on-acc: #f7fee7;
    --grn-03-grain: 0.32;
  }
}

.grn-03__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-03__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-03__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-03-line);
  border-radius: 999px;
  background: var(--grn-03-surf);
  color: var(--grn-03-ink);
  cursor: pointer;
}

.grn-03__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-03__theme-input:focus-visible + .grn-03__theme-label {
  outline: 2px solid var(--grn-03-acc);
  outline-offset: 3px;
}

.grn-03__hero {
  position: relative;
  overflow: hidden;
  background-image: var(--grn-03-noise), radial-gradient(120% 140% at 12% 0%, color-mix(in oklab, var(--grn-03-acc) 26%, var(--grn-03-bg)) 0%, var(--grn-03-bg) 62%);
  background-blend-mode: overlay, normal;
  background-repeat: repeat, no-repeat;
}

.grn-03__hero-inner {
  inline-size: min(70rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(4rem, 11vw, 7.5rem) clamp(3rem, 8vw, 5rem);
  display: grid;
  gap: 1rem;
  max-inline-size: 58rem;
}

.grn-03__badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  justify-self: start;
  margin: 0;
  padding: 0.35rem 0.8rem;
  border: 1px solid var(--grn-03-line);
  border-radius: 999px;
  background: color-mix(in oklab, var(--grn-03-surf) 70%, transparent);
  font: 500 0.74rem/1.4 var(--grn-03-font-mono);
  letter-spacing: 0.06em;
  color: var(--grn-03-mut);
}

.grn-03__dot {
  inline-size: 7px;
  block-size: 7px;
  border-radius: 999px;
  background: var(--grn-03-acc);
}

.grn-03__h1 {
  margin: 0;
  max-inline-size: 34rem;
  font: 600 clamp(2.1rem, 6vw, 4rem)/1.02 var(--grn-03-font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.grn-03__lede {
  margin: 0;
  max-inline-size: 38rem;
  color: var(--grn-03-mut);
  font-size: clamp(0.97rem, 2vw, 1.12rem);
  text-wrap: pretty;
}

.grn-03__cta-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7rem;
  margin-block-start: 0.6rem;
}

.grn-03__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 48px;
  padding-inline: 1.35rem;
  border-radius: 10px;
  background-image: var(--grn-03-noise), linear-gradient(var(--grn-03-acc), var(--grn-03-acc));
  background-blend-mode: soft-light, normal;
  color: var(--grn-03-on-acc);
  text-decoration: none;
  font: 600 0.92rem/1 var(--grn-03-font-display);
}

.grn-03__cta--ghost {
  background-image: none;
  background: transparent;
  border: 1px solid var(--grn-03-line);
  color: var(--grn-03-ink);
}

.grn-03__cta:hover {
  filter: brightness(1.06);
}

.grn-03__cta--ghost:hover {
  border-color: var(--grn-03-acc);
  filter: none;
}

.grn-03__main {
  inline-size: min(70rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(2.5rem, 7vw, 4.5rem);
  display: grid;
  gap: clamp(2rem, 5vw, 3.2rem);
}

.grn-03__cards {
  display: grid;
  gap: clamp(1rem, 2.4vw, 1.5rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  align-items: start;
}

.grn-03__card {
  position: relative;
  display: grid;
  gap: 0.75rem;
  align-content: start;
  padding: clamp(1.2rem, 3vw, 1.8rem);
  border: 1px solid var(--grn-03-line);
  border-radius: 16px;
  background-image: var(--grn-03-noise), linear-gradient(var(--grn-03-surf), var(--grn-03-surf));
  background-blend-mode: overlay, normal;
  min-inline-size: 0;
}

.grn-03__card--feature {
  border-color: var(--grn-03-acc);
  box-shadow: 0 0 0 1px color-mix(in oklab, var(--grn-03-acc) 40%, transparent), 0 20px 50px -30px color-mix(in oklab, var(--grn-03-acc) 60%, transparent);
}

.grn-03__flag {
  margin: 0;
  justify-self: start;
  padding: 0.2rem 0.6rem;
  border-radius: 999px;
  background: var(--grn-03-acc);
  color: var(--grn-03-on-acc);
  font: 600 0.68rem/1.5 var(--grn-03-font-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.grn-03__card-h {
  margin: 0;
  font: 600 1.1rem/1.2 var(--grn-03-font-display);
}

.grn-03__price {
  margin: 0;
  font: 600 clamp(1.7rem, 4vw, 2.3rem)/1 var(--grn-03-font-display);
  letter-spacing: -0.03em;
}

.grn-03__price span {
  display: block;
  margin-block-start: 0.25rem;
  font: 400 0.78rem/1 var(--grn-03-font-mono);
  letter-spacing: 0.04em;
  color: var(--grn-03-mut);
}

.grn-03__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.4rem;
  border-block-start: 1px solid var(--grn-03-line);
  padding-block-start: 0.8rem;
  font-size: 0.9rem;
  color: var(--grn-03-mut);
}

.grn-03__list li {
  display: flex;
  gap: 0.5rem;
}

.grn-03__list li::before {
  content: "+";
  color: var(--grn-03-acc);
  font-family: var(--grn-03-font-mono);
}

.grn-03__list--strike li {
  text-decoration: line-through;
  text-decoration-thickness: 1px;
}

.grn-03__list--strike li::before {
  content: "-";
  color: var(--grn-03-mut);
}

.grn-03__card-cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 44px;
  margin-block-start: 0.3rem;
  border-radius: 10px;
  background-image: var(--grn-03-noise), linear-gradient(var(--grn-03-acc), var(--grn-03-acc));
  background-blend-mode: soft-light, normal;
  color: var(--grn-03-on-acc);
  text-decoration: none;
  font: 600 0.86rem/1 var(--grn-03-font-display);
}

.grn-03__card-cta--muted {
  background-image: none;
  background: transparent;
  border: 1px solid var(--grn-03-line);
  color: var(--grn-03-mut);
}

.grn-03__strip {
  display: grid;
  gap: 0.9rem;
  padding: clamp(1.2rem, 3vw, 1.9rem);
  border: 1px solid var(--grn-03-line);
  border-radius: 16px;
  background: var(--grn-03-surf);
}

.grn-03__h2 {
  margin: 0;
  font: 600 clamp(1.1rem, 2.6vw, 1.35rem)/1.2 var(--grn-03-font-display);
}

.grn-03__esc {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 7rem), 1fr));
  gap: 0.6rem;
  margin: 0;
}

.grn-03__esc > div {
  display: grid;
  gap: 0.15rem;
  padding: 0.7rem 0.85rem;
  border: 1px solid var(--grn-03-line);
  border-radius: 10px;
  background: color-mix(in oklab, var(--grn-03-acc) 6%, transparent);
}

.grn-03__esc dt {
  margin: 0;
  font: 600 1.15rem/1 var(--grn-03-font-mono);
}

.grn-03__esc dd {
  margin: 0;
  font: 400 0.85rem/1 var(--grn-03-font-mono);
  color: var(--grn-03-acc);
}

.grn-03__strip-note {
  margin: 0;
  color: var(--grn-03-mut);
  font-size: 0.9rem;
  text-wrap: pretty;
}

.grn-03__foot {
  border-block-start: 1px solid var(--grn-03-line);
  background-image: var(--grn-03-noise), linear-gradient(var(--grn-03-surf), var(--grn-03-surf));
  background-blend-mode: overlay, normal;
}

.grn-03__foot-line {
  inline-size: min(70rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin: 0 auto;
  padding-block: clamp(1.5rem, 4vw, 2.4rem);
  color: var(--grn-03-mut);
  font-size: 0.88rem;
}

.grn-03__card,
.grn-03__cta,
.grn-03__card-cta {
  transition: transform 280ms cubic-bezier(0.22, 1, 0.36, 1), filter 200ms ease, border-color 200ms ease;
}

@media (hover: hover) and (pointer: fine) {
  .grn-03__card:hover {
    transform: translateY(-4px);
  }

  .grn-03__card-cta:hover {
    filter: brightness(1.07);
  }
}

@media (prefers-reduced-motion: reduce) {
  .grn-03__card,
    .grn-03__cta,
    .grn-03__card-cta {
    transition-duration: 1ms;
  }

  .grn-03__card:hover {
    transform: none;
  }
}
```
