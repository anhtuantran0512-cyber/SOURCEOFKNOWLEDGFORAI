---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/react-responsive-navbar-burger/"
title: "React Responsive Navbar (Burger)"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A responsive glass navbar with a state-driven mobile menu: on wide screens the links sit inline; below the breakpoint they collapse behind an animated burger…"
has_js: "true"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: React Responsive Navbar (Burger)
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/react-responsive-navbar-burger/

A responsive glass navbar with a state-driven mobile menu: on wide screens the links sit inline; below the breakpoint they collapse behind an animated burger that toggles a frosted dropdown sheet. Written as vanilla state here, but structured exactly like a React component (an `open` boolean driving a class), so it drops straight into JSX.
## HTML
```html
<section class="nb-08" aria-label="React-style responsive glass navbar demo">
  <header class="nb-08__bar">
    <a class="nb-08__brand" href="#nb-08">⬡ Stateful</a>
    <nav class="nb-08__links" aria-label="Primary">
      <a class="nb-08__link" href="#nb-08" aria-current="page">Home</a>
      <a class="nb-08__link" href="#nb-08">Features</a>
      <a class="nb-08__link" href="#nb-08">Team</a>
      <a class="nb-08__link" href="#nb-08">Contact</a>
    </nav>
    <button class="nb-08__burger" id="nb-08-burger" type="button" aria-expanded="false" aria-controls="nb-08-sheet" aria-label="Menu"><span></span><span></span><span></span></button>
  </header>
  <div class="nb-08__sheet" id="nb-08-sheet" role="group" aria-label="Mobile menu">
    <a class="nb-08__mlink" href="#nb-08" aria-current="page">Home</a>
    <a class="nb-08__mlink" href="#nb-08">Features</a>
    <a class="nb-08__mlink" href="#nb-08">Team</a>
    <a class="nb-08__mlink" href="#nb-08">Contact</a>
  </div>
</section>
```
## CSS
```css
.nb-08,
.nb-08 *,
.nb-08 *::before,
.nb-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-08 {
  --accent: oklch(0.64 0.19 240);
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(130deg,#1fa2ff,#12d8fa 50%,#a6ffcb);
}

.nb-08__bar {
  container-type: inline-size;
  position: relative;
  z-index: 6;
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 16px auto;
  max-width: 520px;
  padding: 12px 16px;
  border-radius: 18px;
  color: #0a2540;
  background: rgba(255,255,255,.24);
  border: 1px solid rgba(255,255,255,.5);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.7),0 16px 36px -20px rgba(0,0,0,.4);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
}

.nb-08__brand {
  font-size: 17px;
  font-weight: 800;
  text-decoration: none;
  color: #0a2540;
}

.nb-08__links {
  display: flex;
  gap: 4px;
  margin-inline-start: auto;
}

.nb-08__link {
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 14px;
  border-radius: 10px;
  text-decoration: none;
  color: #0a2540;
  font-size: 14.5px;
  font-weight: 600;
  transition: background .2s;
}

.nb-08__link[aria-current] {
  background: rgba(255,255,255,.6);
}

.nb-08__link:hover {
  background: rgba(255,255,255,.45);
}

.nb-08__link:focus-visible,
.nb-08__mlink:focus-visible,
.nb-08__burger:focus-visible {
  outline: 2px solid #0a2540;
  outline-offset: 2px;
}

.nb-08__burger {
  display: none;
  width: 44px;
  height: 44px;
  margin-inline-start: auto;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  align-items: center;
  background: none;
  border: 0;
  cursor: pointer;
}

.nb-08__burger span {
  width: 22px;
  height: 2px;
  border-radius: 2px;
  background: #0a2540;
  transition: transform .3s,opacity .2s;
}

.nb-08__sheet {
  position: absolute;
  z-index: 5;
  left: 50%;
  top: 78px;
  width: calc(100% - 32px);
  max-width: 520px;
  transform: translateX(-50%) translateY(-10px);
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 10px;
  border-radius: 18px;
  background: rgba(255,255,255,.28);
  border: 1px solid rgba(255,255,255,.5);
  box-shadow: 0 24px 50px -24px rgba(0,0,0,.5);
  backdrop-filter: blur(22px) saturate(180%);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
  opacity: 0;
  pointer-events: none;
  transition: opacity .3s,transform .3s;
  visibility: hidden;
}

.nb-08.is-open .nb-08__sheet {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
  pointer-events: auto;
  visibility: visible;
}

.nb-08__mlink {
  min-height: 44px;
  display: flex;
  align-items: center;
  padding: 0 14px;
  border-radius: 12px;
  text-decoration: none;
  color: #0a2540;
  font-size: 15px;
  font-weight: 600;
}

.nb-08__mlink[aria-current] {
  background: rgba(255,255,255,.6);
}

.nb-08__mlink:hover {
  background: rgba(255,255,255,.45);
}

.nb-08.is-open .nb-08__burger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.nb-08.is-open .nb-08__burger span:nth-child(2) {
  opacity: 0;
}

.nb-08.is-open .nb-08__burger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

@container (max-width: 560px) {
  .nb-08__links {
    display: none;
  }

  .nb-08__burger {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nb-08__sheet,
    .nb-08__burger span {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.nb-08');
  const burger = document.querySelector('#nb-08-burger');
  const sheet = document.querySelector('#nb-08-sheet');
  if (!root || !burger) return;
  let open = false;                      // <- React: const [open,setOpen]=useState(false)
  function render(){
    root.classList.toggle('is-open', open);
    burger.setAttribute('aria-expanded', String(open));
    if (open) sheet.querySelector('a').focus();
  }
  burger.addEventListener('click', () => { open = !open; render(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && open){ open = false; render(); burger.focus(); } });
  root.addEventListener('click', e => { if (open && !e.target.closest('.nb-08__bar') && !e.target.closest('.nb-08__sheet')){ open = false; render(); } });
})();
```
