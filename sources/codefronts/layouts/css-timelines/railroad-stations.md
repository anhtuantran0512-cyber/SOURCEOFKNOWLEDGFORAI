---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/railroad-stations/"
title: "Metro Map Timeline — Transit Lines with Interchange Stations"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "A career or product history drawn as a subway map: two colored lines running in parallel, stations as ring dots with flag labels, and an interchange station…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Metro Map Timeline — Transit Lines with Interchange Stations
Source: https://codefronts.com/layouts/css-timelines/railroad-stations/

A career or product history drawn as a subway map: two colored lines running in parallel, stations as ring dots with flag labels, and an interchange station where the lines meet — the visual grammar everyone on Earth already knows how to read, built from borders and radial dots with zero SVG.
## HTML
```html
<section class="tls-30" aria-label="Metro map timeline demo">
  <div class="tls-30__inner">
    <h3 class="tls-30__title">Ten years, two tracks</h3>
    <div class="tls-30__legend"><span class="tls-30__key" style="--k:#dc2626">Engineering line</span><span class="tls-30__key" style="--k:#2563eb">Design line</span></div>
    <div class="tls-30__map">
      <ol class="tls-30__line" style="--l:#dc2626" role="list" aria-label="Engineering line">
        <li class="tls-30__st" style="--x:4%"><span class="tls-30__dot" aria-hidden="true"></span><p class="tls-30__flag"><time datetime="2016">2016</time>Junior dev</p></li>
        <li class="tls-30__st" style="--x:30%"><span class="tls-30__dot" aria-hidden="true"></span><p class="tls-30__flag"><time datetime="2018">2018</time>Senior engineer</p></li>
        <li class="tls-30__st" style="--x:56%"><span class="tls-30__dot" aria-hidden="true"></span><p class="tls-30__flag"><time datetime="2020">2020</time>Tech lead</p></li>
        <li class="tls-30__st tls-30__st--xchg" style="--x:82%"><span class="tls-30__dot" aria-hidden="true"></span><p class="tls-30__flag"><time datetime="2023">2023</time><b>Design systems lead</b></p></li>
      </ol>
      <ol class="tls-30__line tls-30__line--2" style="--l:#2563eb" role="list" aria-label="Design line">
        <li class="tls-30__st" style="--x:17%"><span class="tls-30__dot" aria-hidden="true"></span><p class="tls-30__flag"><time datetime="2017">2017</time>Night-school Figma</p></li>
        <li class="tls-30__st" style="--x:43%"><span class="tls-30__dot" aria-hidden="true"></span><p class="tls-30__flag"><time datetime="2019">2019</time>First shipped UI</p></li>
        <li class="tls-30__st" style="--x:69%"><span class="tls-30__dot" aria-hidden="true"></span><p class="tls-30__flag"><time datetime="2022">2022</time>Token architecture</p></li>
        <li class="tls-30__st tls-30__st--xchg" style="--x:82%"><span class="tls-30__dot" aria-hidden="true"></span><p class="tls-30__flag tls-30__flag--hidden"><time datetime="2023">2023</time>Interchange</p></li>
      </ol>
    </div>
  </div>
</section>
```
## CSS
```css
.tls-30,
.tls-30 *,
.tls-30 *::before,
.tls-30 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-30 {
  min-height: 100vh;
  width: 100%;
  --tl-ink: #1c1917;
  --tl-mut: #78716c;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #fbfaf8;
  padding: 64px 24px;
  display: grid;
  place-items: center;
}

.tls-30__inner {
  width: min(760px,100%);
}

.tls-30__title {
  font-size: clamp(22px,3.5vw,28px);
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.02em;
  margin-bottom: 14px;
}

.tls-30__legend {
  display: flex;
  gap: 18px;
  margin-bottom: 44px;
}

.tls-30__key {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--tl-mut);
}

.tls-30__key::before {
  content: '';
  width: 22px;
  height: 6px;
  border-radius: 3px;
  background: var(--k);
}

.tls-30__map {
  position: relative;
  padding: 30px 0 20px;
}

.tls-30__line {
  list-style: none;
  position: relative;
  height: 110px;
  border-top: 7px solid var(--l);
  border-radius: 4px;
  margin: 0 12px;
}

.tls-30__line--2 {
  margin-top: -48px;
}

.tls-30__st {
  position: absolute;
  left: var(--x);
  top: 0;
}

.tls-30__dot {
  position: absolute;
  top: -14px;
  left: -10px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #fff;
  border: 5px solid var(--l);
  box-shadow: 0 0 0 3px #fff;
}

.tls-30__st--xchg .tls-30__dot {
  top: -17px;
  left: -13px;
  width: 26px;
  height: 26px;
  border-width: 6px;
  border-color: var(--tl-ink);
  z-index: 2;
}

.tls-30__flag {
  position: absolute;
  top: 16px;
  left: -8px;
  width: 120px;
  font-size: 11.5px;
  line-height: 1.35;
  color: var(--tl-mut);
}

.tls-30__st:nth-child(even) .tls-30__flag {
  top: auto;
  bottom: 26px;
}

.tls-30__flag time {
  display: block;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .08em;
  color: var(--tl-ink);
}

.tls-30__flag b {
  color: var(--tl-ink);
}

.tls-30__flag--hidden {
  visibility: hidden;
}

@media (max-width: 600px) {
  .tls-30__map {
    padding: 0;
  }

  .tls-30__line {
    height: auto;
    border-top: none;
    border-left: 7px solid var(--l);
    margin: 0 0 30px 12px;
    padding: 6px 0 6px 26px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .tls-30__line--2 {
    margin-top: 0;
  }

  .tls-30__st {
    position: static;
  }

  .tls-30__dot {
    top: auto;
    left: -42px;
    margin-top: 2px;
    position: relative;
    display: inline-block;
  }

  .tls-30__flag {
    position: static;
    width: auto;
    margin-top: -22px;
    padding-left: 0;
  }

  .tls-30__st:nth-child(even) .tls-30__flag {
    position: static;
  }

  .tls-30__flag--hidden {
    visibility: visible;
  }
}
```

## JavaScript
```js
/* No JavaScript — rails are thick borders, stations are ring dots positioned by a --x token per stop, and the interchange is one shared station drawn larger in ink. */
```
