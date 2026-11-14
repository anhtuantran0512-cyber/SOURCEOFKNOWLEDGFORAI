---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/magnetic-pull/"
title: "CSS Magnetic Cursor Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "The awwwards-site staple, in ~30 dependency-free lines: a CTA that leans toward your cursor inside its magnetic field, its label drifting a beat further for…"
has_js: "true"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Magnetic Cursor Hover Effect
Source: https://codefronts.com/motion/css-link-effects/magnetic-pull/

The awwwards-site staple, in ~30 dependency-free lines: a CTA that leans toward your cursor inside its magnetic field, its label drifting a beat further for parallax depth — then releasing with a genuine spring wobble courtesy of CSS linear() easing (no physics library; the spring curve IS the easing function). Plus an underline dot that tracks your cursor along a text link.
## HTML
```html
<section class="cle-22" aria-label="Magnetic hover demo">
  <div class="cle-22__stage">
    <div class="cle-22__var">
      <span class="cle-22__field"><a href="#a" class="cle-22__magnet"><span class="cle-22__t">Let's work together</span></a></span>
      <small class="cle-22__cap">A · magnetic pull + spring release</small>
    </div>
    <div class="cle-22__var">
      <a href="#b" class="cle-22__dotlink">[email protected]</a>
      <small class="cle-22__cap">B · dot shadows the cursor</small>
    </div>
  </div>
</section>
```
## CSS
```css
.cle-22,
.cle-22 *,
.cle-22 *::before,
.cle-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-22 {
  width: 100%;
  min-height: 100vh;
  --bg: oklch(0.18 0.02 270);
  --cream: oklch(0.95 0.015 90);
  --brand: oklch(0.75 0.16 60);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-22__stage {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 40px 70px;
  background: radial-gradient(100% 130% at 50% 0%,oklch(0.24 0.025 275),oklch(0.16 0.02 265) 65%);
  padding: 36px;
}

.cle-22__var {
  display: grid;
  gap: 6px;
  justify-items: center;
}

.cle-22__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.58 0.03 270);
}

.cle-22__field {
  display: inline-block;
  padding: 34px 40px;
}

.cle-22__magnet {
  display: inline-block;
  padding: 19px 36px;
  border-radius: 999px;
  background: var(--cream);
  color: oklch(0.2 0.02 270);
  text-decoration: none;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: .01em;
  translate: var(--tx,0px) var(--ty,0px);
  transition: translate .16s ease-out;
  box-shadow: 0 18px 44px -18px oklch(0.75 0.16 60 / .35);
}

.cle-22__magnet .cle-22__t {
  display: inline-block;
  translate: var(--lx,0px) var(--ly,0px);
  transition: translate .16s ease-out;
}

.cle-22__magnet.cle-22__spring,
.cle-22__magnet.cle-22__spring .cle-22__t {
  transition: translate .6s cubic-bezier(.2,1.6,.35,1);
  transition: translate .6s linear(0,0.218 2.1%,0.862 6.5%,1.114 8.6%,1.245 10.7%,1.279 12.4%,1.252 14.1%,1.152 16.7%,0.998 20.2%,0.917 22.9%,0.891 25.7%,0.906 28.8%,0.998 34.3%,1.036 38.1%,1.014 44.3%,0.997 51.4%,1.001 61.5%,1);
}

.cle-22__magnet:hover {
  background: oklch(0.98 0.01 90);
}

.cle-22__magnet:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 4px;
}

.cle-22__dotlink {
  position: relative;
  color: var(--cream);
  text-decoration: none;
  font-size: 20px;
  font-weight: 600;
  letter-spacing: .01em;
  padding-bottom: 12px;
  transition: color .3s;
}

.cle-22__dotlink:hover,
.cle-22__dotlink:focus-visible {
  color: var(--brand);
}

.cle-22__dotlink:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 5px;
  border-radius: 3px;
}

.cle-22__dotlink::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: var(--mx,50%);
  translate: -50% 0;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--brand);
  opacity: 0;
  scale: .4;
  transition: left .15s ease-out,opacity .25s,scale .3s cubic-bezier(.3,1.4,.4,1);
}

.cle-22__dotlink:hover::after,
.cle-22__dotlink:focus-visible::after {
  opacity: 1;
  scale: 1;
}

@media (prefers-reduced-motion: reduce) {
  .cle-22 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  if (matchMedia('(hover: none), (prefers-reduced-motion: reduce)').matches) return;
  document.querySelectorAll('.cle-22__field').forEach((field) => {
    const link = field.querySelector('.cle-22__magnet');
    const label = link.querySelector('.cle-22__t');
    let raf = 0, ev = null;
    const apply = () => {
      raf = 0;
      const r = link.getBoundingClientRect();
      const dx = ev.clientX - (r.left + r.width / 2);
      const dy = ev.clientY - (r.top + r.height / 2);
      link.style.setProperty('--tx', (dx * 0.34).toFixed(1) + 'px');
      link.style.setProperty('--ty', (dy * 0.34).toFixed(1) + 'px');
      label.style.setProperty('--lx', (dx * 0.18).toFixed(1) + 'px');
      label.style.setProperty('--ly', (dy * 0.18).toFixed(1) + 'px');
    };
    field.addEventListener('pointerenter', () => link.classList.remove('cle-22__spring'));
    field.addEventListener('pointermove', (e) => { ev = e; if (!raf) raf = requestAnimationFrame(apply); });
    field.addEventListener('pointerleave', () => {
      link.classList.add('cle-22__spring');
      ['--tx','--ty'].forEach((p) => link.style.setProperty(p, '0px'));
      ['--lx','--ly'].forEach((p) => label.style.setProperty(p, '0px'));
    });
  });
  document.querySelectorAll('.cle-22__dotlink').forEach((a) => {
    a.addEventListener('pointermove', (e) => {
      const r = a.getBoundingClientRect();
      const x = Math.max(4, Math.min(r.width - 4, e.clientX - r.left));
      a.style.setProperty('--mx', x.toFixed(0) + 'px');
    });
    a.addEventListener('pointerleave', () => a.style.setProperty('--mx', '50%'));
  });
})();
```
