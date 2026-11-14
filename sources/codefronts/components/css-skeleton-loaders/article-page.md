---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/article-page/"
title: "Article Page Skeleton Loader"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "A full reading-view shell: hero block, title, byline row, then six paragraphs of bars at varying widths with a short final line in each — the Medium /…"
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Article Page Skeleton Loader
Source: https://codefronts.com/components/css-skeleton-loaders/article-page/

A full reading-view shell: hero block, title, byline row, then six paragraphs of bars at varying widths with a short final line in each — the Medium / Substack / Ghost pattern. The measure is capped in ch, so the placeholder occupies exactly the column the article will fill.
## HTML
```html
<div class="sk-17">
  <div class="sk-17__stage">
    <article class="sk-17__col" role="status" aria-live="polite" aria-labelledby="sk-17-h">
      <span class="sk-17__vh">Loading article…</span>
      <header class="sk-17__head">
        <p class="sk-17__eyebrow">reading view · 68ch measure</p>
        <h2 class="sk-17__h" id="sk-17-h">A shell for long-form, sized like type</h2>
        <p class="sk-17__sub">Three type scales, one measure, and a short last line in every paragraph. The bar gap equals the article's line-height, so six paragraphs of prose land without moving a pixel.</p>
      </header>

      <div class="sk-17__sheet" aria-hidden="true">
        <span class="sk-17__bar sk-17__bar--hero"></span>

        <div class="sk-17__titleblock">
          <span class="sk-17__bar sk-17__bar--h1"></span>
          <span class="sk-17__bar sk-17__bar--h1" style="inline-size:62%"></span>
        </div>

        <div class="sk-17__byline">
          <span class="sk-17__bar sk-17__avatar"></span>
          <div class="sk-17__bylines">
            <span class="sk-17__bar sk-17__bar--meta" style="inline-size:9rem"></span>
            <span class="sk-17__bar sk-17__bar--meta" style="inline-size:13rem"></span>
          </div>
        </div>

        <div class="sk-17__body">
          <div class="sk-17__para"><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span></div>
          <div class="sk-17__para"><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span></div>
          <div class="sk-17__quote"><span class="sk-17__bar sk-17__bar--q"></span><span class="sk-17__bar sk-17__bar--q" style="inline-size:72%"></span></div>
          <div class="sk-17__para"><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span></div>
          <div class="sk-17__para"><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span></div>
          <div class="sk-17__para"><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span></div>
          <div class="sk-17__para"><span class="sk-17__bar sk-17__bar--p"></span><span class="sk-17__bar sk-17__bar--p"></span></div>
        </div>
      </div>

      <aside class="sk-17__spec" aria-label="Recipe">
        <p class="sk-17__srow"><span class="sk-17__skey">measure</span><span class="sk-17__sval">max-inline-size: 68ch — the same column the prose will fill</span></p>
        <p class="sk-17__srow"><span class="sk-17__skey">rhythm</span><span class="sk-17__sval">line gap .62rem ≈ line-height 1.75 · paragraph gap 1.5rem</span></p>
        <p class="sk-17__srow"><span class="sk-17__skey">rag</span><span class="sk-17__sval">3-width cycle + last line clamp(30%, 26ch, 64%)</span></p>
      </aside>
    </article>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-17 {
  --bg: #08080a;
  --bg2: #101013;
  --surface: rgba(255,255,255,.03);
  --line: rgba(255,255,255,.1);
  --ink: #f6f5f4;
  --muted: rgba(246,245,244,.62);
  --faint: rgba(246,245,244,.42);
  --accent: #fca5a5;
  --sk: rgba(246,245,244,.1);
  --sheen: rgba(246,245,244,.17);
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(52% 38% at 50% -6%, rgba(252,165,165,.1) 0%, transparent 60%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-17 *,
.sk-17 *::before,
.sk-17 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 20)) {
  .sk-17 {
    --ink: oklch(0.97 0.004 60);
    --muted: oklch(0.97 0.004 60 / .62);
    --faint: oklch(0.97 0.004 60 / .42);
    --accent: oklch(0.8 0.1 20);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-17 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 17%, transparent);
  }
}

.sk-17__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-17__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: start center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-17__col {
  inline-size: min(68ch,100%);
  display: grid;
  gap: clamp(1.1rem,2.4vw,1.7rem);
}

.sk-17__head {
  display: grid;
  gap: .6rem;
}

.sk-17__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-17__h {
  margin: 0;
  font-size: clamp(1.55rem,3.4vw,2.35rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.08;
  text-wrap: balance;
}

.sk-17__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-17__sheet {
  display: grid;
  gap: 1.5rem;
  padding: clamp(1.1rem,2.4vw,1.9rem);
  border: 1px solid var(--line);
  border-radius: 1.15rem;
  background: var(--surface);
  box-shadow: 0 30px 70px -46px rgba(0,0,0,.9);
}

.sk-17__titleblock {
  display: grid;
  gap: .6rem;
}

.sk-17__byline {
  display: flex;
  align-items: center;
  gap: .9rem;
  padding-block-end: .3rem;
  border-block-end: 1px solid var(--line);
}

.sk-17__bylines {
  display: grid;
  gap: .45rem;
  min-inline-size: 0;
}

.sk-17__body {
  display: grid;
  gap: 1.5rem;
}

.sk-17__para {
  display: grid;
  gap: .62rem;
}

.sk-17__quote {
  display: grid;
  gap: .62rem;
  padding-inline-start: 1.1rem;
  border-inline-start: 2px solid var(--accent);
  opacity: .9;
}

.sk-17__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .78rem;
  inline-size: 100%;
  border-radius: 6px;
  background: var(--sk);
}

.sk-17__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-17-sheen 1.5s linear infinite;
}

@keyframes sk-17-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-17__bar--hero {
  block-size: auto;
  aspect-ratio: 16/8;
  border-radius: 12px;
}

.sk-17__bar--h1 {
  block-size: 2.1rem;
  border-radius: 9px;
}

.sk-17__bar--meta {
  block-size: .7rem;
}

.sk-17__bar--q {
  block-size: .95rem;
  border-radius: 7px;
}

.sk-17__avatar {
  inline-size: 2.5rem;
  block-size: auto;
  aspect-ratio: 1;
  border-radius: 999px;
  flex: none;
}

.sk-17__para > .sk-17__bar--p:nth-child(3n+1) {
  inline-size: 100%;
}

.sk-17__para > .sk-17__bar--p:nth-child(3n+2) {
  inline-size: 96%;
}

.sk-17__para > .sk-17__bar--p:nth-child(3n+3) {
  inline-size: 92%;
}

.sk-17__para > .sk-17__bar--p:last-child {
  inline-size: clamp(30%,26ch,64%);
}

.sk-17__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-17__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-17__skey {
  min-inline-size: 4.6rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-17__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-17[data-theme="light"] {
  --bg: #fdfcfb;
  --bg2: #fff;
  --surface: #ffffff;
  --line: rgba(12,10,10,.11);
  --ink: #0c0a0a;
  --muted: rgba(12,10,10,.62);
  --faint: rgba(12,10,10,.44);
  --accent: #b91c1c;
  background: linear-gradient(178deg,#fff 0%,#f5f2f0 100%);
}

@media (prefers-color-scheme: light) {
  .sk-17:not([data-theme="dark"]) {
    --bg: #fdfcfb;
    --bg2: #fff;
    --surface: #ffffff;
    --line: rgba(12,10,10,.11);
    --ink: #0c0a0a;
    --muted: rgba(12,10,10,.62);
    --faint: rgba(12,10,10,.44);
    --accent: #b91c1c;
    background: linear-gradient(178deg,#fff 0%,#f5f2f0 100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-17__bar::after {
    animation: none;
    background: none;
  }

  .sk-17__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }
}

@media (forced-colors: active) {
  .sk-17__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-17__bar::after {
    animation: none;
    background: none;
  }

  .sk-17__sheet,
    .sk-17__spec {
    border-color: CanvasText;
  }
}
```
