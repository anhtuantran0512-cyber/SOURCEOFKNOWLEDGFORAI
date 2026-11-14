---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/header-navbar-integrated-sticky-search-bar/"
title: "Header Navbar Integrated Sticky Search Bar"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "A marketing header where the search field collapses to an icon as the page scrolls and re-expands the moment you focus it."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Header Navbar Integrated Sticky Search Bar
Source: https://codefronts.com/components/css-search-boxes/header-navbar-integrated-sticky-search-bar/

A marketing header where the search field collapses to an icon as the page scrolls and re-expands the moment you focus it. The shrink is a real scroll-driven animation (animation-timeline: scroll()) with an IntersectionObserver fallback, so it is smooth on modern browsers and correct everywhere else.
## HTML
```html
<div class="sb-04">
  <button class="sb-04__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-04__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-04__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-04__stage">
    <div class="sb-04__frame">
      <div class="sb-04__scroll" id="sb-04-scroll">
        <header class="sb-04__nav" id="sb-04-nav" data-scrolled="false">
          <a class="sb-04__logo" href="#sb-04-scroll"><span class="sb-04__mark" aria-hidden="true"></span>Halcyon</a>
          <nav class="sb-04__links" aria-label="Primary">
            <a href="#sb-04-scroll">Product</a>
            <a href="#sb-04-scroll">Solutions</a>
            <a href="#sb-04-scroll">Docs</a>
            <a href="#sb-04-scroll">Pricing</a>
          </nav>
          <div class="sb-04__search" role="search">
            <svg class="sb-04__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <label class="sb-04__vh" for="sb-04-input">Search the site</label>
            <input class="sb-04__input" id="sb-04-input" type="search" placeholder="Search docs and guides" autocomplete="off">
          </div>
          <button class="sb-04__cta" type="button">Start free</button>
        </header>

        <div class="sb-04__page" aria-hidden="true">
          <div class="sb-04__hero">
            <span class="sb-04__sk sb-04__sk--pill"></span>
            <span class="sb-04__sk sb-04__sk--h1"></span>
            <span class="sb-04__sk sb-04__sk--h1 sb-04__sk--short"></span>
            <span class="sb-04__sk sb-04__sk--line"></span>
            <span class="sb-04__sk sb-04__sk--line sb-04__sk--short"></span>
          </div>
          <div class="sb-04__grid">
            <span class="sb-04__sk sb-04__sk--card"></span>
            <span class="sb-04__sk sb-04__sk--card"></span>
            <span class="sb-04__sk sb-04__sk--card"></span>
            <span class="sb-04__sk sb-04__sk--card"></span>
            <span class="sb-04__sk sb-04__sk--card"></span>
            <span class="sb-04__sk sb-04__sk--card"></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@property --sb-04-pad {
  syntax: '<length>';
  inherits: true;
  initial-value: 16px;
}

@property --sb-04-w {
  syntax: '<length>';
  inherits: true;
  initial-value: 240px;
}

.sb-04 {
  --bg: #f4f5f8;
  --card: #ffffff;
  --ink: #0f1219;
  --muted: #6a7180;
  --line: #e5e7ee;
  --acc: #3b5bfd;
  --wash: #eef1ff;
  --ring: #3b5bfd;
  --shadow: rgba(15,18,25,.22);
  --pad: 16px;
  --w: 240px;
  --logo: 1.05rem;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(50rem 30rem at 80% -10%, rgba(59,91,253,.10), transparent 70%), var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-04 *,
.sb-04 *::before,
.sb-04 *::after {
  box-sizing: border-box;
}

.sb-04__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-04__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-04__frame {
  inline-size: min(64rem,100%);
  block-size: min(34rem,80svh);
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: var(--card);
  box-shadow: 0 30px 70px -34px var(--shadow);
}

.sb-04__scroll {
  block-size: 100%;
  overflow: auto;
  overscroll-behavior: contain;
  scroll-behavior: smooth;
  container-type: inline-size;
}
/* nav */

.sb-04__nav {
  position: sticky;
  inset-block-start: 0;
  z-index: 4;
  display: flex;
  align-items: center;
  gap: clamp(.6rem,2cqi,1.5rem);
  padding: var(--pad) clamp(.9rem,2.5cqi,1.5rem);
  background: color-mix(in srgb, var(--card) 82%, transparent);
  -webkit-backdrop-filter: blur(14px) saturate(160%);
  backdrop-filter: blur(14px) saturate(160%);
  border-block-end: 1px solid transparent;
  transition: padding .28s cubic-bezier(.2,.9,.25,1), border-color .28s, box-shadow .28s;
}

.sb-04__logo {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  flex: none;
  color: inherit;
  text-decoration: none;
  font-size: var(--logo);
  font-weight: 700;
  letter-spacing: -.02em;
  transition: font-size .28s;
}

.sb-04__mark {
  inline-size: 1.4em;
  block-size: 1.4em;
  border-radius: 8px;
  background: conic-gradient(from 210deg, #3b5bfd, #7c6cff 40%, #16d1c9 75%, #3b5bfd);
}

.sb-04__links {
  display: flex;
  gap: clamp(.4rem,1.6cqi,1.1rem);
  flex: 1;
  min-inline-size: 0;
}

.sb-04__links a {
  padding: .45rem .55rem;
  border-radius: 8px;
  color: var(--muted);
  text-decoration: none;
  font: 500 .88rem/1 inherit;
  white-space: nowrap;
  transition: color .16s, background .16s;
}

.sb-04__links a:hover {
  color: var(--ink);
  background: var(--wash);
}

.sb-04__links a:focus-visible,
.sb-04__logo:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

@container (max-width: 52rem) {
  .sb-04__links {
    display: none;
  }
}
/* search */

.sb-04__search {
  display: flex;
  align-items: center;
  gap: .5rem;
  flex: none;
  inline-size: var(--w);
  min-block-size: 44px;
  padding-inline: .8rem;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: #fbfbfd;
  overflow: hidden;
  transition: inline-size .3s cubic-bezier(.2,.9,.25,1), border-color .2s, box-shadow .2s, background .2s;
}

.sb-04__search:hover {
  border-color: color-mix(in oklab, var(--acc) 35%, var(--line));
}

.sb-04__search:focus-within {
  --w: min(22rem,46cqi);
  border-color: var(--acc);
  background: var(--card);
  box-shadow: 0 0 0 4px rgba(59,91,253,.16);
}

.sb-04__ico {
  inline-size: 18px;
  block-size: 18px;
  flex: none;
  color: var(--muted);
}

.sb-04__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .9rem/1 inherit;
  opacity: 1;
  transition: opacity .2s;
}

.sb-04__input::placeholder {
  color: var(--muted);
}

.sb-04__input:focus {
  outline: none;
}

.sb-04__cta {
  flex: none;
  min-block-size: 44px;
  padding-inline: 1.05rem;
  border: 0;
  border-radius: 11px;
  cursor: pointer;
  background: var(--ink);
  color: var(--card);
  font: 600 .87rem/1 inherit;
  white-space: nowrap;
  transition: filter .18s, scale .12s;
}

.sb-04__cta:hover {
  filter: brightness(1.18);
}

.sb-04__cta:active {
  scale: .97;
}

.sb-04__cta:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}
/* collapsed: JS fallback baseline */

.sb-04__nav[data-scrolled="true"] {
  --pad: 9px;
  --logo: .98rem;
  border-block-end-color: var(--line);
  box-shadow: 0 10px 26px -20px var(--shadow);
}

.sb-04__nav[data-scrolled="true"] .sb-04__search {
  --w: 44px;
  padding-inline: .75rem;
}

.sb-04__nav[data-scrolled="true"] .sb-04__search:not(:focus-within) .sb-04__input {
  opacity: 0;
}
/* collapsed: scroll-driven upgrade */

@supports (animation-timeline: scroll()) {
  .sb-04__nav {
    animation: sb-04-shrink linear both;
    animation-timeline: scroll(nearest block);
    animation-range: 0 140px;
  }

  .sb-04__nav[data-scrolled] {
    --pad: 16px;
  }

  @keyframes sb-04-shrink {
    to {
      --pad: 9px;
      --logo: .98rem;
      border-block-end-color: var(--line);
      box-shadow: 0 10px 26px -20px var(--shadow);
    }
  }

  .sb-04__search {
    animation: sb-04-collapse linear both;
    animation-timeline: scroll(nearest block);
    animation-range: 0 140px;
  }

  @keyframes sb-04-collapse {
    to {
      inline-size: 44px;
    }
  }

  .sb-04__search:focus-within {
    animation: none;
    inline-size: min(22rem,46cqi);
  }

  .sb-04__input {
    animation: sb-04-fade linear both;
    animation-timeline: scroll(nearest block);
    animation-range: 40px 130px;
  }

  @keyframes sb-04-fade {
    to {
      opacity: 0;
    }
  }

  .sb-04__search:focus-within .sb-04__input {
    animation: none;
    opacity: 1;
  }
}
/* page skeleton */

.sb-04__page {
  padding: clamp(1.5rem,5cqi,3.5rem) clamp(1rem,3cqi,2rem) 3rem;
  display: grid;
  gap: 2.5rem;
}

.sb-04__hero {
  display: grid;
  gap: .85rem;
  justify-items: center;
  text-align: center;
  padding-block: clamp(1rem,6cqi,3rem);
}

.sb-04__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(13rem,1fr));
  gap: 1rem;
}

.sb-04__sk {
  display: block;
  border-radius: 10px;
  background: linear-gradient(90deg,#eceef4,#f5f6fa,#eceef4);
  background-size: 200% 100%;
  animation: sb-04-shimmer 2.4s linear infinite;
}

.sb-04__sk--pill {
  inline-size: 9rem;
  block-size: 1.6rem;
  border-radius: 999px;
}

.sb-04__sk--h1 {
  inline-size: min(30rem,86%);
  block-size: 2.4rem;
}

.sb-04__sk--line {
  inline-size: min(24rem,72%);
  block-size: .85rem;
}

.sb-04__sk--short {
  inline-size: min(16rem,52%);
}

.sb-04__sk--card {
  block-size: 8.5rem;
}

@keyframes sb-04-shimmer {
  to {
    background-position: -200% 0;
  }
}
/* dark */

.sb-04[data-theme="dark"] {
  --bg: #0a0c12;
  --card: #11141c;
  --ink: #eef0f6;
  --muted: #8a91a3;
  --line: #1f2430;
  --acc: #6f86ff;
  --wash: rgba(111,134,255,.14);
  --ring: #6f86ff;
  --shadow: rgba(0,0,0,.7);
  background: radial-gradient(50rem 30rem at 80% -10%, rgba(111,134,255,.16), transparent 70%), var(--bg);
}

.sb-04[data-theme="dark"] .sb-04__search {
  background: #0e111a;
}

.sb-04[data-theme="dark"] .sb-04__sk {
  background: linear-gradient(90deg,#171b25,#1e2230,#171b25);
  background-size: 200% 100%;
}

@media (prefers-color-scheme: dark) {
  .sb-04:not([data-theme="light"]) {
    --bg: #0a0c12;
    --card: #11141c;
    --ink: #eef0f6;
    --muted: #8a91a3;
    --line: #1f2430;
    --acc: #6f86ff;
    --wash: rgba(111,134,255,.14);
    --ring: #6f86ff;
    --shadow: rgba(0,0,0,.7);
    background: radial-gradient(50rem 30rem at 80% -10%, rgba(111,134,255,.16), transparent 70%), var(--bg);
  }

  .sb-04:not([data-theme="light"]) .sb-04__search {
    background: #0e111a;
  }

  .sb-04:not([data-theme="light"]) .sb-04__sk {
    background: linear-gradient(90deg,#171b25,#1e2230,#171b25);
    background-size: 200% 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-04 *,
    .sb-04 *::before,
    .sb-04 *::after {
    animation: none !important;
    transition: none !important;
  }

  .sb-04__scroll {
    scroll-behavior: auto;
  }
}

@media (forced-colors: active) {
  .sb-04__frame,
    .sb-04__search,
    .sb-04__cta {
    border: 1px solid CanvasText;
  }
}

.sb-04__theme {
  position: absolute;
  inset-block-start: clamp(.75rem,2vw,1.25rem);
  inset-inline-end: clamp(.75rem,2vw,1.25rem);
  z-index: 50;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid rgba(0,0,0,.12);
  color: currentColor;
  background: rgba(255,255,255,.72);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
}

.sb-04[data-theme="dark"] .sb-04__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-04:not([data-theme="light"]) .sb-04__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-04__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-04[data-theme="dark"] .sb-04__theme:hover,
.sb-04:not([data-theme="light"]) .sb-04__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-04__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-04__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-04__sun {
  display: none;
}

.sb-04__theme[aria-pressed="true"] .sb-04__sun {
  display: block;
}

.sb-04__theme[aria-pressed="true"] .sb-04__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-04__theme {
    transition: none;
  }

  .sb-04__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-04');
  if (!root) return;
  const nav = root.querySelector('#sb-04-nav');
  const scroller = root.querySelector('#sb-04-scroll');
  if (CSS.supports('animation-timeline: scroll()')) return;   /* CSS already owns it */

  const sentinel = document.createElement('span');
  sentinel.style.cssText = 'display:block;height:1px;';
  scroller.insertBefore(sentinel, nav);
  new IntersectionObserver(
    ([entry]) => { nav.dataset.scrolled = String(!entry.isIntersecting); },
    { root: scroller, threshold: 0 }
  ).observe(sentinel);
})();
(()=>{const r=document.querySelector('.sb-04');if(!r)return;const t=r.querySelector('.sb-04__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
