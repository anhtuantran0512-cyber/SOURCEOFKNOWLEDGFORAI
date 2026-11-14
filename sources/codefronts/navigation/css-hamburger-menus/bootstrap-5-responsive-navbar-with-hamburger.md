---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/bootstrap-5-responsive-navbar-with-hamburger/"
title: "Bootstrap 5 Navbar Hamburger Menu Toggle Setup"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The canonical Bootstrap 5.3 navbar, assembled correctly on the first try: navbar-expand-lg picks the breakpoint, navbar-toggler + data-bs-toggle wire the…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bootstrap 5 Navbar Hamburger Menu Toggle Setup
Source: https://codefronts.com/navigation/css-hamburger-menus/bootstrap-5-responsive-navbar-with-hamburger/

The canonical Bootstrap 5.3 navbar, assembled correctly on the first try: navbar-expand-lg picks the breakpoint, navbar-toggler + data-bs-toggle wire the collapse plugin with zero custom JS, and every class in the chain is annotated so you know which ones are load-bearing. Includes the three fixes for 'bootstrap hamburger not working' (the #1 support thread for this pattern) and the CSS to replace the default toggler icon with an animated one.
## HTML
```html
<section class="chm-16" aria-label="Bootstrap 5 navbar hamburger setup demo">
  <div class="chm-16__stage">
    <div class="chm-16__frame">
      <nav class="navbar" aria-label="Main">
        <div class="container-fluid">
          <a class="navbar-brand" href="#home"><span class="brand-dot" aria-hidden="true"></span>Bootlace</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#chm16-nav" aria-controls="chm16-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="chm-16__bars" aria-hidden="true"><i></i><i></i><i></i></span>
          </button>
          <div class="collapse navbar-collapse" id="chm16-nav">
            <ul class="navbar-nav">
              <li class="nav-item"><a class="nav-link active" aria-current="page" href="#home">Home</a></li>
              <li class="nav-item"><a class="nav-link" href="#features">Features</a></li>
              <li class="nav-item"><a class="nav-link" href="#pricing">Pricing</a></li>
              <li class="nav-item"><a class="nav-link disabled" aria-disabled="true">Beta</a></li>
            </ul>
          </div>
        </div>
      </nav>
      <div class="chm-16__page" aria-hidden="true"><span style="--w:76%"></span><span style="--w:90%"></span><span style="--w:58%"></span></div>
    </div>
    <p class="chm-16__note" aria-hidden="true">card is narrower than the <code>lg</code> breakpoint, so the toggler shows. The shim stands in for <code>bootstrap.bundle.min.js</code> here — load the real bundle in your project.</p>
  </div>
</section>
```
## CSS
```css
.chm-16,
.chm-16 *,
.chm-16 *::before,
.chm-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-16 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --body: oklch(1 0 0);
  --tertiary: oklch(0.97 0.004 260);
  --border: oklch(0.9 0.007 260);
  --ink: oklch(0.28 0.02 262);
  --mut: oklch(0.5 0.016 262);
  --primary: oklch(0.55 0.19 262);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.chm-16__stage {
  border: 1px solid var(--border);
  border-radius: 18px;
  background: oklch(0.985 0.003 260);
  padding: 20px;
  display: grid;
  gap: 14px;
}

.chm-16__frame {
  container-type: inline-size;
  border: 1px solid var(--border);
  border-radius: 14px;
  overflow: hidden;
  background: var(--body);
  box-shadow: 0 14px 34px -26px oklch(0.3 0.03 262/.6);
}

.chm-16 .navbar {
  background: var(--tertiary);
  border-bottom: 1px solid var(--border);
  padding: 8px 0;
}

.chm-16 .container-fluid {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 0 16px;
}

.chm-16 .navbar-brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 16.5px;
  font-weight: 600;
  color: var(--ink);
  text-decoration: none;
  padding: 6px 0;
}

.chm-16 .brand-dot {
  width: 19px;
  height: 19px;
  border-radius: 5px;
  background: linear-gradient(140deg,var(--primary),oklch(0.65 0.2 300));
}

.chm-16 .navbar-toggler {
  display: grid;
  place-items: center;
  width: 52px;
  height: 44px;
  border: 1px solid oklch(0.82 0.012 262);
  border-radius: 8px;
  background: transparent;
  color: var(--ink);
  cursor: pointer;
  transition: box-shadow .15s;
}

.chm-16 .navbar-toggler:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--primary) 35%,transparent);
}

.chm-16__bars {
  position: relative;
  width: 20px;
  height: 14px;
  display: block;
}

.chm-16__bars i {
  position: absolute;
  left: 0;
  width: 20px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: translate .28s,rotate .28s .04s,opacity .2s;
}

.chm-16__bars i:nth-child(1) {
  top: 0;
}

.chm-16__bars i:nth-child(2) {
  top: 6px;
}

.chm-16__bars i:nth-child(3) {
  top: 12px;
}

.chm-16 .navbar-toggler[aria-expanded="true"] .chm-16__bars i:nth-child(1) {
  translate: 0 6px;
  rotate: 45deg;
}

.chm-16 .navbar-toggler[aria-expanded="true"] .chm-16__bars i:nth-child(2) {
  opacity: 0;
}

.chm-16 .navbar-toggler[aria-expanded="true"] .chm-16__bars i:nth-child(3) {
  translate: 0 -6px;
  rotate: -45deg;
}

.chm-16 .navbar-collapse {
  flex-basis: 100%;
  overflow: hidden;
}

.chm-16 .navbar-collapse.collapse:not(.show) {
  display: none;
}

.chm-16 .navbar-collapse.collapsing {
  height: 0;
  transition: height .3s ease;
}

.chm-16 .navbar-nav {
  list-style: none;
  display: flex;
  flex-direction: column;
  padding: 6px 4px 10px;
}

.chm-16 .nav-link {
  display: block;
  padding: 10px 12px;
  border-radius: 8px;
  font-size: 14.5px;
  font-weight: 500;
  color: var(--mut);
  text-decoration: none;
  transition: color .15s,background .15s;
}

.chm-16 .nav-link:hover,
.chm-16 .nav-link:focus-visible {
  color: var(--ink);
  background: oklch(0.94 0.006 260);
}

.chm-16 .nav-link:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--primary) 35%,transparent);
}

.chm-16 .nav-link.active {
  color: var(--ink);
  font-weight: 600;
}

.chm-16 .nav-link.disabled {
  color: oklch(0.72 0.008 262);
  pointer-events: none;
}

@container (min-width: 768px) {
  .chm-16 .navbar-toggler {
    display: none;
  }

  .chm-16 .navbar-collapse {
    flex-basis: auto;
  }

  .chm-16 .navbar-collapse.collapse:not(.show) {
    display: flex !important;
  }

  .chm-16 .navbar-nav {
    flex-direction: row;
    gap: 2px;
    padding: 0;
    margin-left: auto;
  }
}

.chm-16__page {
  padding: 16px;
  display: grid;
  gap: 11px;
}

.chm-16__page span {
  display: block;
  height: 10px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.94 0.004 260);
}

.chm-16__note {
  font-size: 12px;
  line-height: 1.6;
  color: var(--mut);
  text-wrap: pretty;
}

.chm-16__note code {
  font: 11px ui-monospace,Menlo,Consolas,monospace;
  background: oklch(0.93 0.005 260);
  border-radius: 5px;
  padding: 1.5px 6px;
}

@media (prefers-reduced-motion: reduce) {
  .chm-16 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(function () {
  /* Stand-in for bootstrap.bundle.min.js collapse — same class dance, same timing. */
  document.querySelectorAll('.chm-16__frame').forEach(function (frame) {
    if (frame.dataset.bound) return; frame.dataset.bound = '1';
    var btn = frame.querySelector('[data-bs-toggle="collapse"]'),
        panel = frame.querySelector(btn.getAttribute('data-bs-target'));
    btn.addEventListener('click', function () {
      var opening = !panel.classList.contains('show');
      btn.setAttribute('aria-expanded', String(opening));
      panel.classList.remove('collapse');
      panel.classList.add('collapsing');
      panel.style.height = opening ? '0' : panel.scrollHeight + 'px';
      requestAnimationFrame(function () {
        panel.style.height = opening ? panel.scrollHeight + 'px' : '0';
      });
      setTimeout(function () {
        panel.classList.remove('collapsing');
        panel.classList.add('collapse');
        panel.classList.toggle('show', opening);
        panel.style.height = '';
      }, 300);
    });
  });
})();
```
