---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/letter-push/"
title: "CSS Staggered Letter Push Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Per-letter choreography with a 14-line accessible splitter: hover a link and its letters roll over one by one, each replaced from below by an accent copy —…"
has_js: "true"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Staggered Letter Push Hover Effect
Source: https://codefronts.com/motion/css-link-effects/letter-push/

Per-letter choreography with a 14-line accessible splitter: hover a link and its letters roll over one by one, each replaced from below by an accent copy — the effect every award-site nav uses. Plus a gentler cascade lift and a jelly wave that undulates while hovered. The stagger is one line of math: transition-delay: calc(var(--i) * 28ms).
## HTML
```html
<section class="cle-16" aria-label="Staggered letter hover demo">
  <div class="cle-16__stage">
    <nav class="cle-16__nav" aria-label="Studio">
      <div class="cle-16__var"><a href="#a" class="cle-16__roll" data-split="roll">STUDIO</a><small class="cle-16__cap">A · letter roll-over</small></div>
      <div class="cle-16__var"><a href="#b" class="cle-16__lift" data-split="lift">PROJECTS</a><small class="cle-16__cap">B · cascade lift</small></div>
      <div class="cle-16__var"><a href="#c" class="cle-16__wavey" data-split="wave">CONTACT</a><small class="cle-16__cap">C · jelly wave loop</small></div>
    </nav>
  </div>
</section>
```
## CSS
```css
.cle-16,
.cle-16 *,
.cle-16 *::before,
.cle-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-16 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.92 0.01 100);
  --accent: oklch(0.85 0.17 100);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-16__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
  background: linear-gradient(170deg,oklch(0.24 0.015 100),oklch(0.17 0.012 90));
  padding: 44px 32px;
}

.cle-16__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 44px 64px;
  justify-content: center;
}

.cle-16__var {
  display: grid;
  gap: 14px;
  justify-items: center;
}

.cle-16__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.58 0.04 95);
}

.cle-16 a {
  color: var(--ink);
  text-decoration: none;
  font-size: clamp(24px,3.6vw,34px);
  font-weight: 800;
  letter-spacing: .06em;
  white-space: nowrap;
}

.cle-16 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 6px;
  border-radius: 4px;
}

.cle-16__w {
  display: inline-block;
}

.cle-16__ch {
  position: relative;
  display: inline-block;
  transition: translate .4s cubic-bezier(.3,1,.3,1),color .3s;
  transition-delay: calc(var(--i) * 28ms);
}

.cle-16__roll {
  display: inline-block;
  overflow: hidden;
}

.cle-16__roll .cle-16__ch::after {
  content: attr(data-char);
  position: absolute;
  left: 0;
  top: 100%;
  color: var(--accent);
}

.cle-16__roll:hover .cle-16__ch,
.cle-16__roll:focus-visible .cle-16__ch {
  translate: 0 -100%;
}

.cle-16__lift:hover .cle-16__ch,
.cle-16__lift:focus-visible .cle-16__ch {
  translate: 0 -5px;
  color: var(--accent);
}

.cle-16__wavey:hover .cle-16__ch,
.cle-16__wavey:focus-visible .cle-16__ch {
  animation: clh16-wave .9s ease-in-out infinite;
  animation-delay: calc(var(--i) * 60ms);
  color: var(--accent);
}

@keyframes clh16-wave {
  0%,
    100% {
    translate: 0 0;
  }

  50% {
    translate: 0 -7px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cle-16 .cle-16__ch {
    transition: color .3s;
    transition-delay: 0s;
    animation: none !important;
  }

  .cle-16 a:hover .cle-16__ch {
    translate: 0 0;
    color: var(--accent);
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.cle-16 a[data-split]').forEach((a) => {
    const label = a.textContent.trim();
    a.setAttribute('aria-label', label);
    const wrap = document.createElement('span');
    wrap.className = 'cle-16__w';
    wrap.setAttribute('aria-hidden', 'true');
    [...label].forEach((ch, i) => {
      const s = document.createElement('span');
      s.className = 'cle-16__ch';
      s.style.setProperty('--i', i);
      s.dataset.char = ch;
      s.innerHTML = ch === ' ' ? '&nbsp;' : ch;
      wrap.append(s);
    });
    a.replaceChildren(wrap);
  });
})();
```
