---
source: "codefronts"
url: "https://codefronts.com/layouts/css-masonry-layouts/css-masonry-infinite-scroll-dynamic-loading/"
title: "CSS Masonry Infinite Scroll Dynamic Loading"
section: "layouts"
category: "css-masonry-layouts"
category_name: "CSS Masonry Layouts"
description: "Infinite scroll done the way the layout gods intended: the wall is demo 03's append-stable grid-span engine (columns would reshuffle every card on each load…"
has_js: "true"
---

Here's a working CSS Masonry Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Masonry Infinite Scroll Dynamic Loading
Source: https://codefronts.com/layouts/css-masonry-layouts/css-masonry-infinite-scroll-dynamic-loading/

Infinite scroll done the way the layout gods intended: the wall is demo 03's append-stable grid-span engine (columns would reshuffle every card on each load — the classic library bug, explained), a sentinel row of shimmering skeleton cards trips an IntersectionObserver 600px early, batches append with zero existing-card movement, an aria-live region narrates progress, and the stream ends honestly with 'all caught up' instead of a spinner that lies.
## HTML
```html
<section class="msn-11" aria-label="CSS masonry infinite scroll demo">
  <div class="msn-11__stage" tabindex="0">
    <header class="msn-11__head">
      <div><h2>Discover</h2><p>Endless-ish · stops honestly at 40</p></div>
      <span class="msn-11__status" role="status" aria-live="polite">Loaded 8 of 40</span>
    </header>
    <div class="msn-11__grid">
      <article class="msn-11__card msn-11__card--t" style="--img:url('https://images.unsplash.com/photo-1469474968028-56623f02e42e?q=80&w=700&auto=format&fit=crop');--a:oklch(0.75 0.1 130);--b:oklch(0.45 0.11 150)"><div class="msn-11__cap"><strong>Shot 1</strong><span>3.2k likes</span></div></article>
      <article class="msn-11__card msn-11__card--s" style="--img:url('https://images.unsplash.com/photo-1482938289607-e9573fc25ebb?q=80&w=700&auto=format&fit=crop');--a:oklch(0.72 0.09 230);--b:oklch(0.45 0.1 250)"><div class="msn-11__cap"><strong>Shot 2</strong><span>2.8k likes</span></div></article>
      <article class="msn-11__card msn-11__card--w" style="--img:url('https://images.unsplash.com/photo-1501594907352-04cda38ebc29?q=80&w=700&auto=format&fit=crop');--a:oklch(0.7 0.1 40);--b:oklch(0.45 0.13 20)"><div class="msn-11__cap"><strong>Shot 3</strong><span>2.1k likes</span></div></article>
      <article class="msn-11__card msn-11__card--s" style="--img:url('https://images.unsplash.com/photo-1519125323398-675f0ddb6308?q=80&w=700&auto=format&fit=crop');--a:oklch(0.8 0.07 120);--b:oklch(0.55 0.09 100)"><div class="msn-11__cap"><strong>Shot 4</strong><span>1.9k likes</span></div></article>
      <article class="msn-11__card msn-11__card--t" style="--img:url('https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?q=80&w=700&auto=format&fit=crop');--a:oklch(0.7 0.1 140);--b:oklch(0.42 0.1 160)"><div class="msn-11__cap"><strong>Shot 5</strong><span>1.7k likes</span></div></article>
      <article class="msn-11__card msn-11__card--w" style="--img:url('https://images.unsplash.com/photo-1472214103451-9374bd1c798e?q=80&w=700&auto=format&fit=crop');--a:oklch(0.8 0.09 90);--b:oklch(0.55 0.12 70)"><div class="msn-11__cap"><strong>Shot 6</strong><span>1.4k likes</span></div></article>
      <article class="msn-11__card msn-11__card--s" style="--img:url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=700&auto=format&fit=crop');--a:oklch(0.74 0.09 220);--b:oklch(0.48 0.1 240)"><div class="msn-11__cap"><strong>Shot 7</strong><span>1.2k likes</span></div></article>
      <article class="msn-11__card msn-11__card--t" style="--img:url('https://images.unsplash.com/photo-1433086966358-54859d0ed716?q=80&w=700&auto=format&fit=crop');--a:oklch(0.78 0.08 160);--b:oklch(0.5 0.09 180)"><div class="msn-11__cap"><strong>Shot 8</strong><span>980 likes</span></div></article>
      <div class="msn-11__sentinel" aria-hidden="true"><i></i><i></i><i></i></div>
    </div>
    <footer class="msn-11__foot"><p>You can always reach me — that's the point.</p><a href="#top">Back to top</a></footer>
  </div>
</section>
```
## CSS
```css
.msn-11,
.msn-11 *,
.msn-11 *::before,
.msn-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msn-11 {
  --bg: oklch(0.98 0.004 250);
  --ink: oklch(0.23 0.015 260);
  --mut: oklch(0.55 0.015 260);
  --line: oklch(0.9 0.008 250);
  --acc: oklch(0.6 0.17 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.msn-11__stage {
  width: 100%;
  container: msn11/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.msn-11__head {
  position: sticky;
  top: 0;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  padding: 15px clamp(16px,3cqi,26px);
  background: color-mix(in oklch,var(--bg) 84%,transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.msn-11__head h2 {
  font-size: clamp(17px,2.4cqi,22px);
  letter-spacing: -.02em;
}

.msn-11__head p {
  font-size: 11.5px;
  color: var(--mut);
  margin-top: 2px;
}

.msn-11__status {
  font-size: 11.5px;
  font-weight: 700;
  color: var(--acc);
  border: 1px solid color-mix(in oklch,var(--acc) 35%,var(--line));
  background: color-mix(in oklch,var(--acc) 8%,transparent);
  border-radius: 99px;
  padding: 6px 12px;
  font-variant-numeric: tabular-nums;
}

.msn-11__grid {
  display: grid;
  gap: 10px;
  grid-template-columns: repeat(auto-fill,minmax(min(190px,100%),1fr));
  grid-auto-rows: 10px;
  padding: clamp(14px,3cqi,26px);
}

.msn-11__card {
  position: relative;
  border-radius: 13px;
  overflow: clip;
  background: linear-gradient(150deg,var(--a),var(--b));
}

.msn-11__card::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: var(--img,none);
  background-size: cover;
  background-position: center;
  transition: scale .4s cubic-bezier(.2,.7,.2,1);
}

.msn-11__card:hover::before {
  scale: 1.04;
}

.msn-11__card::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,transparent 55%,oklch(0.2 0.02 260/.6));
}

.msn-11__card--t {
  grid-row: span 24;
}

.msn-11__card--s {
  grid-row: span 15;
}

.msn-11__card--w {
  grid-row: span 10;
}

.msn-11__cap {
  position: absolute;
  left: 11px;
  right: 11px;
  bottom: 9px;
  z-index: 1;
  color: oklch(0.99 0 0);
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 8px;
}

.msn-11__cap strong {
  font-size: 12.5px;
  letter-spacing: -.01em;
}

.msn-11__cap span {
  font-size: 10.5px;
  opacity: .85;
}

.msn-11__sentinel {
  grid-column: 1/-1;
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(min(190px,100%),1fr));
  gap: 10px;
  grid-row: span 12;
}

.msn-11__sentinel i {
  border-radius: 13px;
  background: linear-gradient(100deg,oklch(0.93 0.006 250) 40%,oklch(0.965 0.004 250) 50%,oklch(0.93 0.006 250) 60%) 0 0/240% 100%;
  animation: msn11-shimmer 1.3s linear infinite;
}

.msn-11__sentinel i:nth-child(3) {
  display: none;
}

@keyframes msn11-shimmer {
  to {
    background-position: -140% 0;
  }
}

.msn-11__sentinel.is-done {
  display: flex;
  align-items: center;
  justify-content: center;
  grid-row: span 5;
}

.msn-11__sentinel.is-done::after {
  content: "You're all caught up — 40 of 40";
  font-size: 13px;
  font-weight: 700;
  color: var(--mut);
}

.msn-11__sentinel.is-done i {
  display: none;
}

.msn-11__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 16px clamp(16px,3cqi,26px) 26px;
  border-top: 1px solid var(--line);
}

.msn-11__foot p {
  font-size: 12px;
  color: var(--mut);
}

.msn-11__foot a {
  font-size: 12.5px;
  font-weight: 700;
  color: var(--acc);
  text-decoration: none;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
}

.msn-11__foot a:hover,
.msn-11__foot a:focus-visible {
  text-decoration: underline;
  text-underline-offset: 3px;
}

.msn-11__foot a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 4px;
}

@container msn11 (width < 460px) {
  .msn-11__grid {
    grid-template-columns: repeat(2,1fr);
    gap: 8px;
  }

  .msn-11__sentinel {
    grid-template-columns: repeat(2,1fr);
  }

  .msn-11__sentinel i:nth-child(3) {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .msn-11 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.msn-11').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var scroller = root.querySelector('.msn-11__stage');
    var grid = root.querySelector('.msn-11__grid');
    var sent = root.querySelector('.msn-11__sentinel');
    var status = root.querySelector('.msn-11__status');
    var BATCH = 8, TOTAL = 40, loaded = 8, busy = false;
    var kinds = ['t', 's', 'w', 's', 't', 'w', 's', 's'];
    function addBatch() {
      var frag = document.createDocumentFragment();
      for (var i = 0; i < BATCH; i++) {
        var n = loaded + i + 1, hue = (n * 47) % 360;
        var el = document.createElement('article');
        el.className = 'msn-11__card msn-11__card--' + kinds[(n + i) % kinds.length];
        el.style.setProperty('--a', 'oklch(0.78 0.11 ' + hue + ')');
        el.style.setProperty('--b', 'oklch(0.5 0.14 ' + ((hue + 45) % 360) + ')');
        el.innerHTML = '<div class="msn-11__cap"><strong>Shot ' + n + '</strong><span>' + (2 + (n % 7)) + '.' + (n % 10) + 'k likes</span></div>';
        frag.appendChild(el);
      }
      grid.insertBefore(frag, sent);
      loaded += BATCH;
      status.textContent = 'Loaded ' + loaded + ' of ' + TOTAL;
      if (loaded >= TOTAL) { io.disconnect(); sent.classList.add('is-done'); }
    }
    // Watch BOTH the stage's own scroll (root: scroller) AND the outer
    // viewport (root: null) so infinite scroll fires whether the user
    // scrolls inside the fixed-height stage or the outer page/iframe.
    // Necessary because when the initial 8-card wall doesn't overflow
    // the stage, the outer scroll is the only one the user can trigger.
    function onIntersect(entries) {
      if (busy || loaded >= TOTAL) return;
      var hit = entries.some(function (e) { return e.isIntersecting; });
      if (!hit) return;
      busy = true;
      setTimeout(function () { /* swap this timeout for your fetch() */
        addBatch();
        busy = false;
        // If the sentinel is STILL in view after the batch (large
        // stage / small screens / initial full wall fits above the
        // fold), keep loading in a chain without waiting for another
        // scroll event — that would strand the user staring at the
        // shimmer skeleton forever.
        if (loaded < TOTAL) {
          var r = sent.getBoundingClientRect();
          var vh = window.innerHeight || document.documentElement.clientHeight;
          if (r.top < vh + 600) setTimeout(function () { onIntersect([{ isIntersecting: true }]); }, 50);
        }
      }, 550);
    }
    var ioStage = new IntersectionObserver(onIntersect, { root: scroller, rootMargin: '600px 0px' });
    var ioPage  = new IntersectionObserver(onIntersect, { root: null,     rootMargin: '600px 0px' });
    var io = { disconnect: function () { ioStage.disconnect(); ioPage.disconnect(); } };
    ioStage.observe(sent);
    ioPage.observe(sent);
  });
})();
```
