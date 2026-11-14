---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/tailwind-css-hamburger-menu/"
title: "Tailwind CSS Responsive Hamburger Menu Component"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "A copy-paste Tailwind navbar the way Tailwind authors actually write one: hidden md:flex for the desktop row, a burger button that swaps two SVGs, and a…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Responsive Hamburger Menu Component
Source: https://codefronts.com/navigation/css-hamburger-menus/tailwind-css-hamburger-menu/

A copy-paste Tailwind navbar the way Tailwind authors actually write one: hidden md:flex for the desktop row, a burger button that swaps two SVGs, and a mobile panel toggled by one class — plus the peer-checked variant for a zero-JS version, both spelled out in the docs. The demo below renders through a scoped shim that replicates exactly what the Tailwind JIT would generate, so what you see is what those utilities produce.
## HTML
```html
<section class="chm-15" aria-label="Tailwind CSS hamburger menu demo">
  <div class="chm-15__stage">
    <div class="chm-15__frame">
      <nav class="flex items-center justify-between px-4 py-3 bg-white border-b border-zinc-200" aria-label="Primary">
        <a href="#home" class="flex items-center gap-2 font-bold text-zinc-900"><span class="logo-dot" aria-hidden="true"></span>tailfleet</a>
        <div class="hidden md:flex md:items-center md:gap-1">
          <a href="#features" class="nav-link" aria-current="page">Features</a>
          <a href="#pricing" class="nav-link">Pricing</a>
          <a href="#docs" class="nav-link">Docs</a>
          <a href="#blog" class="nav-link">Blog</a>
        </div>
        <div class="flex items-center gap-2">
          <a href="#signup" class="btn-primary hidden md:inline-flex">Sign up</a>
          <button type="button" class="burger md:hidden" aria-expanded="false" aria-controls="chm15-menu" aria-label="Open menu">
            <svg class="icon-open" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
            <svg class="icon-close hidden" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg>
          </button>
        </div>
      </nav>
      <div id="chm15-menu" class="hidden md:hidden px-3 pb-3 bg-white border-b border-zinc-200">
        <a href="#features" class="menu-link" aria-current="page">Features</a>
        <a href="#pricing" class="menu-link">Pricing</a>
        <a href="#docs" class="menu-link">Docs</a>
        <a href="#blog" class="menu-link">Blog</a>
        <a href="#signup" class="btn-primary w-full justify-center mt-2">Sign up</a>
      </div>
      <div class="chm-15__page" aria-hidden="true"><span style="--w:70%"></span><span style="--w:88%"></span><span style="--w:54%"></span></div>
    </div>
    <p class="chm-15__note" aria-hidden="true">rendered by a scoped shim of the exact utilities — in your project, Tailwind generates this CSS. The card is narrower than <code>md</code>, so you see the mobile state; the docs give the peer-checked no-JS variant.</p>
  </div>
</section>
```
## CSS
```css
.chm-15,
.chm-15 *,
.chm-15 *::before,
.chm-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-15 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --zinc50: oklch(0.985 0 0);
  --zinc200: oklch(0.92 0.004 286);
  --zinc500: oklch(0.55 0.014 286);
  --zinc900: oklch(0.21 0.006 286);
  --sky: oklch(0.59 0.16 245);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--zinc900);
}

.chm-15__stage {
  border: 1px solid var(--zinc200);
  border-radius: 18px;
  background: var(--zinc50);
  padding: 20px;
  display: grid;
  gap: 14px;
}

.chm-15__frame {
  container-type: inline-size;
  border: 1px solid var(--zinc200);
  border-radius: 14px;
  overflow: hidden;
  background: oklch(1 0 0);
  box-shadow: 0 14px 34px -26px oklch(0.3 0.02 286/.6);
}

.chm-15 [class~="flex"] {
  display: flex;
}

.chm-15 [class~="items-center"] {
  align-items: center;
}

.chm-15 [class~="justify-between"] {
  justify-content: space-between;
}

.chm-15 [class~="justify-center"] {
  justify-content: center;
}

.chm-15 [class~="gap-2"] {
  gap: 8px;
}

.chm-15 [class~="px-4"] {
  padding-inline: 16px;
}

.chm-15 [class~="py-3"] {
  padding-block: 12px;
}

.chm-15 [class~="px-3"] {
  padding-inline: 12px;
}

.chm-15 [class~="pb-3"] {
  padding-bottom: 12px;
}

.chm-15 [class~="mt-2"] {
  margin-top: 8px;
}

.chm-15 [class~="w-full"] {
  width: 100%;
}

.chm-15 [class~="bg-white"] {
  background: oklch(1 0 0);
}

.chm-15 [class~="border-b"] {
  border-bottom: 1px solid var(--zinc200);
}

.chm-15 [class~="font-bold"] {
  font-weight: 700;
}

.chm-15 [class~="text-zinc-900"] {
  color: var(--zinc900);
}

.chm-15 [class~="hidden"] {
  display: none;
}

.chm-15 .logo-dot {
  width: 18px;
  height: 18px;
  border-radius: 6px;
  background: conic-gradient(from 200deg,var(--sky),oklch(0.72 0.14 190));
}

.chm-15 nav a {
  text-decoration: none;
}

.chm-15 .nav-link {
  display: inline-flex;
  align-items: center;
  min-height: 38px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--zinc500);
  transition: color .15s,background .15s;
}

.chm-15 .nav-link:hover,
.chm-15 .nav-link:focus-visible {
  color: var(--zinc900);
  background: oklch(0.96 0.002 286);
}

.chm-15 .nav-link[aria-current="page"] {
  color: var(--sky);
}

.chm-15 .btn-primary {
  display: inline-flex;
  align-items: center;
  min-height: 40px;
  padding: 0 16px;
  border-radius: 10px;
  background: var(--zinc900);
  color: oklch(0.985 0 0);
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  transition: background .2s;
}

.chm-15 .btn-primary:hover {
  background: var(--sky);
}

.chm-15 .burger {
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  border: 1px solid var(--zinc200);
  border-radius: 10px;
  background: oklch(1 0 0);
  color: var(--zinc900);
  cursor: pointer;
  transition: background .15s;
}

.chm-15 .burger:hover {
  background: oklch(0.97 0.002 286);
}

.chm-15 .burger svg {
  grid-area: 1/1;
}

.chm-15 .menu-link {
  display: flex;
  align-items: center;
  min-height: 44px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 14px;
  font-weight: 600;
  color: var(--zinc500);
  transition: background .15s,color .15s;
}

.chm-15 .menu-link:hover,
.chm-15 .menu-link:focus-visible {
  background: oklch(0.96 0.002 286);
  color: var(--zinc900);
}

.chm-15 .menu-link[aria-current="page"] {
  color: var(--sky);
}

.chm-15 .nav-link:focus-visible,
.chm-15 .menu-link:focus-visible,
.chm-15 .btn-primary:focus-visible,
.chm-15 .burger:focus-visible {
  outline: 2px solid var(--sky);
  outline-offset: 2px;
}

@container (min-width: 768px) {
  .chm-15 [class~="md:flex"] {
    display: flex;
  }

  .chm-15 [class~="md:items-center"] {
    align-items: center;
  }

  .chm-15 [class~="md:gap-1"] {
    gap: 4px;
  }

  .chm-15 [class~="md:hidden"] {
    display: none;
  }

  .chm-15 [class~="md:inline-flex"] {
    display: inline-flex;
  }
}

.chm-15__page {
  padding: 16px;
  display: grid;
  gap: 11px;
}

.chm-15__page span {
  display: block;
  height: 10px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.94 0.002 286);
}

.chm-15__note {
  font-size: 12px;
  line-height: 1.6;
  color: var(--zinc500);
  text-wrap: pretty;
}

.chm-15__note code {
  font: 11px ui-monospace,Menlo,Consolas,monospace;
  background: oklch(0.94 0.002 286);
  border-radius: 5px;
  padding: 1.5px 6px;
}

@media (prefers-reduced-motion: reduce) {
  .chm-15 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-15__frame').forEach(function (frame) {
    if (frame.dataset.bound) return; frame.dataset.bound = '1';
    var btn = frame.querySelector('.burger'),
        menu = frame.querySelector('#chm15-menu') || frame.querySelector('[id$="menu"]');
    btn.addEventListener('click', function () {
      var open = menu.classList.toggle('hidden') === false;
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      btn.querySelector('.icon-open').classList.toggle('hidden', open);
      btn.querySelector('.icon-close').classList.toggle('hidden', !open);
    });
  });
})();
```
