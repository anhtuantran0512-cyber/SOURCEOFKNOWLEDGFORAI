---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/ios-26-floating-tab-bar/"
title: "iOS 26 Floating Tab Bar"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "The iOS 26 bottom tab bar recreated as a floating glass capsule that hovers above your content."
has_js: "true"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: iOS 26 Floating Tab Bar
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/ios-26-floating-tab-bar/

The iOS 26 bottom tab bar recreated as a floating glass capsule that hovers above your content. It shrinks to an icon-only pill as the user scrolls down (reclaiming screen space), then springs back to full width with labels the moment scrolling stops or the pointer enters — exactly like the native OS.
## HTML
```html
<section class="nb-01" aria-label="iOS 26 floating tab bar demo">
  <div class="nb-01__scroll">
    <h2 class="nb-01__h">Scroll me ↓</h2>
    <p class="nb-01__p">The floating tab bar shrinks to icons as you scroll down and springs back on scroll-up, idle or hover — just like iOS 26.</p>
    <p class="nb-01__p">Keep scrolling to watch the glass capsule frost the content passing beneath it. The bar collapses on scroll-down, expands on scroll-up, and always expands after 600ms of idle so it stays reachable.</p>
    <p class="nb-01__p">Every tab is a real link with a 44px hit target and an aria-current active state. Labels stay in the DOM when collapsed so screen readers still announce them.</p>
    <p class="nb-01__p">Hovering the bar or focusing any tab also forces the expanded state — useful when a keyboard user tabs into the bar mid-scroll.</p>
    <p class="nb-01__p">The frosted glass effect uses <code>backdrop-filter</code> — you need translucent fill plus something scrolling under it, which this demo intentionally ships.</p>
    <p class="nb-01__p">Try scrolling up now. The bar should spring back to its full width with all four labels visible again.</p>
    <p class="nb-01__p">All motion is <code>transform</code>, <code>opacity</code> and <code>backdrop-filter</code> — no layout thrashing, INP-friendly, WCAG 2.2 compliant.</p>
    <p class="nb-01__p">Keep going to see the bar frost this line…</p>
    <p class="nb-01__p">…and this one…</p>
    <p class="nb-01__p">…and this one too. That's it — scroll up to reset, or hover the bar to force it open.</p>
  </div>
  <nav class="nb-01__bar" id="nb-01-bar" aria-label="Primary">
    <a class="nb-01__tab" href="#nb-01" aria-current="page" aria-label="Home"><span class="nb-01__ico" aria-hidden="true">⌂</span><span class="nb-01__lbl">Home</span></a>
    <a class="nb-01__tab" href="#nb-01" aria-label="Search"><span class="nb-01__ico" aria-hidden="true">⌕</span><span class="nb-01__lbl">Search</span></a>
    <a class="nb-01__tab" href="#nb-01" aria-label="Saved"><span class="nb-01__ico" aria-hidden="true">♥</span><span class="nb-01__lbl">Saved</span></a>
    <a class="nb-01__tab" href="#nb-01" aria-label="Profile"><span class="nb-01__ico" aria-hidden="true">◉</span><span class="nb-01__lbl">Profile</span></a>
  </nav>
</section>
```
## CSS
```css
.nb-01,
.nb-01 *,
.nb-01 *::before,
.nb-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-01 {
  --accent: oklch(0.64 0.2 265);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 210deg at 30% 20%,#5b8cff,#b06bff,#ff7ab0,#5b8cff);
  background-size: 200% 200%;
  animation: nb-01-bg 18s ease-in-out infinite;
}

@keyframes nb-01-bg {
  50% {
    background-position: 100% 100%;
  }
}

.nb-01__scroll {
  position: absolute;
  inset: 0;
  overflow-y: auto;
  padding: 32px 24px 140px;
  color: #fff;
}

.nb-01__h {
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -.02em;
  margin-bottom: 14px;
  text-shadow: 0 2px 12px rgba(0,0,0,.3);
}

.nb-01__p {
  font-size: 15px;
  line-height: 1.7;
  margin-bottom: 64px;
  max-width: 44ch;
  color: rgba(255,255,255,.92);
  text-shadow: 0 1px 8px rgba(0,0,0,.28);
}

.nb-01__bar {
  position: absolute;
  left: 50%;
  bottom: 22px;
  transform: translateX(-50%);
  display: flex;
  gap: 6px;
  padding: 10px 14px;
  border-radius: 999px;
  isolation: isolate;
  background: color-mix(in oklab,white 16%,transparent);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.55),0 20px 44px -20px rgba(0,0,0,.6);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  transition: padding .45s cubic-bezier(.34,1.4,.5,1),gap .45s;
}

.nb-01__tab {
  display: flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 999px;
  text-decoration: none;
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  transition: background .25s,transform .2s;
}

.nb-01__ico {
  font-size: 19px;
  line-height: 1;
}

.nb-01__lbl {
  max-width: 80px;
  overflow: hidden;
  white-space: nowrap;
  opacity: 1;
  transition: max-width .45s cubic-bezier(.34,1.4,.5,1),opacity .3s;
}

.nb-01__tab[aria-current] {
  background: var(--accent);
  box-shadow: 0 6px 16px -6px color-mix(in oklab,var(--accent) 70%,transparent);
}

.nb-01__tab:hover {
  background: rgba(255,255,255,.18);
}

.nb-01__tab[aria-current]:hover {
  background: var(--accent);
}

.nb-01__tab:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

.nb-01__bar.is-compact {
  padding: 8px;
  gap: 2px;
}

.nb-01__bar.is-compact .nb-01__lbl {
  max-width: 0;
  opacity: 0;
  margin: 0;
}

.nb-01__bar.is-compact .nb-01__tab {
  padding: 0 12px;
}

@media (prefers-reduced-motion: reduce) {
  .nb-01 {
    animation: none;
  }

  .nb-01__bar,
    .nb-01__lbl {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const scroll = document.querySelector('.nb-01__scroll');
  const bar = document.querySelector('#nb-01-bar');
  if (!scroll || !bar) return;
  const THRESHOLD = 10;
  let last = 0, idle;
  scroll.addEventListener('scroll', () => {
    const y = scroll.scrollTop;
    if (y > last + THRESHOLD && y > 40) bar.classList.add('is-compact');
    else if (y < last - THRESHOLD) bar.classList.remove('is-compact');
    last = y;
    clearTimeout(idle);
    idle = setTimeout(() => bar.classList.remove('is-compact'), 600);
  }, { passive: true });
  const expand = () => bar.classList.remove('is-compact');
  bar.addEventListener('pointerenter', expand);
  bar.addEventListener('focusin', expand);
})();
```
