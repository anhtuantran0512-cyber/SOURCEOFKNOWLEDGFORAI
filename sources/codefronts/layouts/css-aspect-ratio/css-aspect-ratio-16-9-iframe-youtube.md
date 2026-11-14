---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-16-9-iframe-youtube/"
title: "CSS Aspect Ratio 16 9 Iframe YouTube"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "The fluid YouTube embed, 2026 edition: aspect-ratio: 16/9 on a wrapper, width/height 100% on the iframe — two rules replace the entire padding-bottom: 56.25%…"
has_js: "true"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio 16 9 Iframe YouTube
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-16-9-iframe-youtube/

The fluid YouTube embed, 2026 edition: aspect-ratio: 16/9 on a wrapper, width/height 100% on the iframe — two rules replace the entire padding-bottom: 56.25% ritual. The player ships as a click-to-load facade (poster + play button in the same ratio box), so the page loads zero third-party JavaScript until a human actually asks for the video; the swapped-in iframe inherits the exact same box, so nothing shifts. A talk-library page with chapters and an up-next rail proves the same ratio maths at three sizes.
## HTML
```html
<section class="car-01" aria-label="Responsive 16:9 YouTube iframe demo">
  <div class="car-01__stage" id="car01-top">
    <a class="car-01__skip" href="#car01-main">Skip to content</a>
    <header class="car-01__bar">
      <a class="car-01__brand" href="#car01-top"><i aria-hidden="true"></i>Framewise</a>
      <nav class="car-01__nav" aria-label="Primary">
        <a href="#car01-main">Talks</a>
        <a href="#car01-next">Up next</a>
        <a href="#car01-notes">Notes</a>
      </nav>
      <span class="car-01__ratio-chip" aria-hidden="true">aspect-ratio: 16 / 9</span>
    </header>
    <main class="car-01__main" id="car01-main">
      <article class="car-01__watch">
        <figure class="car-01__player" style="--img:url('https://images.unsplash.com/photo-1540575467063-178a50c2df87?q=80&w=1600&auto=format&fit=crop')">
          <button class="car-01__facade" type="button" data-embed="https://www.youtube-nocookie.com/embed/M7lc1UVf-VE?autoplay=1&rel=0" aria-label="Play talk: Layout Without Lies — The Aspect Ratio Contract (48 min)">
            <span class="car-01__facade-badge">Click to load — 0 KB of player JS until then</span>
            <span class="car-01__play" aria-hidden="true"><svg viewBox="0 0 24 24" width="30" height="30"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg></span>
            <span class="car-01__dur" aria-hidden="true">48:12</span>
          </button>
        </figure>
        <div class="car-01__meta">
          <h1>Layout without lies: the aspect-ratio contract</h1>
          <p class="car-01__byline">Ada Okafor · RenderConf 2026 · <span>4.2k plays</span></p>
          <div class="car-01__chapters" role="list" aria-label="Chapters">
            <a role="listitem" href="#car01-main"><b>00:00</b> Why 56.25% had to die</a>
            <a role="listitem" href="#car01-main"><b>07:40</b> One box, one ratio</a>
            <a role="listitem" href="#car01-main"><b>19:05</b> Facades &amp; CLS</a>
            <a role="listitem" href="#car01-main"><b>33:50</b> Q&amp;A</a>
          </div>
          <p class="car-01__desc" id="car01-notes">The wrapper above is <code>aspect-ratio: 16 / 9</code> — resize this pane and watch the height follow the width. The play button is a facade: the real YouTube iframe (and its ~1MB of JS) is created only on click, into the exact same box, so the swap shifts nothing.</p>
        </div>
      </article>
      <aside class="car-01__rail" id="car01-next" aria-label="Up next">
        <h2>Up next</h2>
        <a class="car-01__card" href="#car01-top" style="--img:url('https://images.unsplash.com/photo-1475721027785-f74eccf877e2?q=80&w=900&auto=format&fit=crop')"><figure></figure><div><h3>Container queries in production</h3><p>Priya Nair · 32 min</p></div></a>
        <a class="car-01__card" href="#car01-top" style="--img:url('https://images.unsplash.com/photo-1505373877841-8d25f7d46678?q=80&w=900&auto=format&fit=crop')"><figure></figure><div><h3>The end of the media query?</h3><p>Tom Alder · 41 min</p></div></a>
        <a class="car-01__card" href="#car01-top" style="--img:url('https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?q=80&w=900&auto=format&fit=crop')"><figure></figure><div><h3>Scroll-driven everything</h3><p>June Park · 27 min</p></div></a>
      </aside>
    </main>
    <footer class="car-01__foot">Every thumbnail on this page is the same two rules: <code>aspect-ratio:16/9</code> + <code>object-fit:cover</code>. A demo from the CodeFronts aspect-ratio collection.</footer>
  </div>
</section>
```
## CSS
```css
.car-01,
.car-01 *,
.car-01 *::before,
.car-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-01 {
  --bg: oklch(0.16 0.015 265);
  --panel: oklch(0.21 0.018 265);
  --ink: oklch(0.95 0.008 250);
  --mut: oklch(0.68 0.015 255);
  --line: oklch(0.32 0.02 262);
  --acc: oklch(0.75 0.16 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-01__stage {
  width: 100%;
  container: car01/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
  scroll-behavior: smooth;
}

.car-01__skip {
  position: absolute;
  z-index: 20;
  left: 16px;
  top: -60px;
  padding: 10px 16px;
  border-radius: 0 0 10px 10px;
  background: var(--acc);
  color: oklch(0.2 0.03 85);
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  transition: translate .2s;
}

.car-01__skip:focus-visible {
  translate: 0 60px;
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.car-01__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: clamp(12px,3cqi,28px);
  height: 60px;
  padding: 0 clamp(16px,4cqi,40px);
  background: color-mix(in oklch,var(--bg) 82%,transparent);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line);
}

.car-01__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.car-01__brand i {
  width: 14px;
  height: 14px;
  border-radius: 4px;
  background: conic-gradient(from 210deg,var(--acc),oklch(0.6 0.19 35),var(--acc));
  clip-path: polygon(0 0,100% 0,100% 62.5%,0 62.5%);
}

.car-01__nav {
  display: flex;
  gap: 2px;
  margin-inline: auto;
}

.car-01__nav a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 13px;
  border-radius: 9px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: color .2s,background .2s;
}

.car-01__nav a:hover,
.car-01__nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.3 0.02 262/.6);
}

.car-01__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.car-01__ratio-chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  font-weight: 600;
  color: var(--acc);
  padding: 6px 10px;
  border: 1px solid color-mix(in oklch,var(--acc) 40%,transparent);
  border-radius: 99px;
  white-space: nowrap;
}

.car-01__main {
  display: grid;
  grid-template-columns: minmax(0,1fr) minmax(240px,340px);
  gap: clamp(18px,3cqi,32px);
  padding: clamp(18px,3.5cqi,36px) clamp(16px,4cqi,40px);
  align-items: start;
}

.car-01__player {
  position: relative;
  aspect-ratio: 16/9;
  width: 100%;
  border-radius: 18px;
  overflow: hidden;
  background: linear-gradient(135deg,oklch(0.3 0.05 265),oklch(0.2 0.03 300));
  box-shadow: 0 24px 60px oklch(0.05 0.02 265/.5);
}

.car-01__player iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

.car-01__facade {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
  cursor: pointer;
  display: grid;
  place-items: center;
  color: oklch(0.98 0 0);
  background-color: oklch(0.25 0.04 265);
  background-image: linear-gradient(oklch(0.15 0.02 265/.25),oklch(0.12 0.02 265/.55)),var(--img);
  background-size: cover;
  background-position: center;
  transition: background-size .5s cubic-bezier(.2,.7,.2,1);
}

.car-01__facade:hover,
.car-01__facade:focus-visible {
  background-size: 107%;
}

.car-01__facade:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: -3px;
}

.car-01__play {
  display: grid;
  place-items: center;
  width: 76px;
  height: 54px;
  border-radius: 16px;
  background: oklch(0.62 0.23 27/.94);
  box-shadow: 0 10px 30px oklch(0.1 0.05 27/.55);
  transition: scale .25s cubic-bezier(.34,1.56,.64,1);
}

.car-01__facade:hover .car-01__play,
.car-01__facade:focus-visible .car-01__play {
  scale: 1.12;
}

.car-01__facade-badge {
  position: absolute;
  left: 14px;
  top: 14px;
  font-size: 11.5px;
  font-weight: 600;
  padding: 7px 11px;
  border-radius: 99px;
  background: oklch(0.15 0.02 265/.72);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}

.car-01__dur {
  position: absolute;
  right: 14px;
  bottom: 12px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  font-weight: 700;
  padding: 5px 9px;
  border-radius: 8px;
  background: oklch(0.15 0.02 265/.78);
}

.car-01__meta h1 {
  font-size: clamp(20px,3cqi,28px);
  letter-spacing: -.02em;
  font-weight: 800;
  margin-top: 18px;
}

.car-01__byline {
  margin-top: 6px;
  font-size: 13px;
  color: var(--mut);
}

.car-01__byline span {
  color: var(--acc);
  font-weight: 600;
}

.car-01__chapters {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 16px;
}

.car-01__chapters a {
  display: flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 11px;
  border: 1px solid var(--line);
  background: var(--panel);
  font-size: 12.5px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: border-color .2s,color .2s,translate .2s;
}

.car-01__chapters a:hover,
.car-01__chapters a:focus-visible {
  border-color: var(--acc);
  color: var(--ink);
  translate: 0 -1px;
}

.car-01__chapters a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.car-01__chapters b {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  color: var(--acc);
}

.car-01__desc {
  margin-top: 16px;
  font-size: 14px;
  line-height: 1.65;
  color: var(--mut);
  max-width: 64ch;
}

.car-01__desc code,
.car-01__foot code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .88em;
  background: oklch(0.28 0.02 262);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.car-01__rail h2 {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 12px;
}

.car-01__rail {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.car-01__card {
  display: flex;
  flex-direction: column;
  gap: 0;
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid var(--line);
  background: var(--panel);
  text-decoration: none;
  color: inherit;
  margin-bottom: 12px;
  transition: translate .25s cubic-bezier(.2,.7,.2,1),border-color .25s;
}

.car-01__card:hover,
.car-01__card:focus-visible {
  translate: 0 -3px;
  border-color: color-mix(in oklch,var(--acc) 55%,var(--line));
}

.car-01__card:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.car-01__card figure {
  aspect-ratio: 16/9;
  background: linear-gradient(120deg,oklch(0.33 0.05 265),oklch(0.24 0.04 320)),var(--img);
  background-image: var(--img),linear-gradient(120deg,oklch(0.33 0.05 265),oklch(0.24 0.04 320));
  background-size: cover;
  background-position: center;
}

.car-01__card div {
  padding: 12px 14px 14px;
}

.car-01__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.car-01__card p {
  font-size: 12px;
  color: var(--mut);
  margin-top: 4px;
}

.car-01__foot {
  padding: 22px clamp(16px,4cqi,40px) 34px;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-top: 1px solid var(--line);
}

@container car01 (width < 760px) {
  .car-01__main {
    grid-template-columns: 1fr;
  }

  .car-01__nav {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-01__stage {
    scroll-behavior: auto;
  }

  .car-01 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.car-01__facade').forEach((btn) => {
    if (btn.dataset.wired) return;
    btn.dataset.wired = '1';
    btn.addEventListener('click', () => {
      const f = document.createElement('iframe');
      f.src = btn.dataset.embed;
      f.title = btn.getAttribute('aria-label') || 'Video player';
      f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
      btn.replaceWith(f);
      f.focus();
    });
  });
})();
```
