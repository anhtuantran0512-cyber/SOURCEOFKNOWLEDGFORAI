---
source: "codefronts"
url: "https://codefronts.com/navigation/css-glassmorphic-navbars/mobile-off-canvas-hamburger-glass-menu/"
title: "Mobile Off-Canvas / Hamburger Glass Menu"
section: "navigation"
category: "css-glassmorphic-navbars"
category_name: "CSS Glassmorphic Sticky Navbars"
description: "The glassmorphism-mobile-overlay-menu: tap the hamburger and a full-height drawer slides in over a heavily-blurred scrim, so the page shows through as soft…"
has_js: "false"
---

Here's a working CSS Glassmorphic Sticky Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile Off-Canvas / Hamburger Glass Menu
Source: https://codefronts.com/navigation/css-glassmorphic-navbars/mobile-off-canvas-hamburger-glass-menu/

The glassmorphism-mobile-overlay-menu: tap the hamburger and a full-height drawer slides in over a heavily-blurred scrim, so the page shows through as soft frosted colour. Built with the checkbox toggle so it is 100% JavaScript-free, with a proper focusable close control and reduced-motion support.
## HTML
```html
<div class="gn-06">
  <input type="checkbox" id="gn06-toggle" class="gn-06-cb">
  <div class="gn-06__stage">
    <header class="gn-06-bar">
      <a class="gn-06-brand" href="#">Meridian</a>
      <label for="gn06-toggle" class="gn-06-burger" aria-label="Open menu" tabindex="0">
        <span></span><span></span><span></span>
      </label>
    </header>
    <div class="gn-06-body">
      <h2>Tap the hamburger &sect; scroll to feel the sticky bar</h2>
      <p>The top bar stays pinned as the page moves. Tap the burger and a full-height drawer slides in over a heavily-blurred scrim, so the page shows through as soft frosted colour.</p>
      <p>The scrim is the star. Instead of dimming to grey, it covers the viewport with <code>backdrop-filter:blur(16px)</code> and a faint dark tint &mdash; the page behind melts into frosted colour rather than getting hidden.</p>
      <p>Toggle is the CSS checkbox hack: a visually-hidden checkbox whose label is the hamburger. When <code>:checked</code>, a general-sibling selector reveals the scrim and slides the drawer in. Zero JavaScript for the whole open/close mechanic.</p>
      <p>The drawer itself is a second glass surface sliding in with <code>transform:translateX</code>. Transform-based motion runs on the compositor, so the slide stays smooth even during heavy scroll.</p>
      <h3>The full production upgrade path</h3>
      <p>The checkbox-hack is honest about its trade-offs. It has no focus trap, no Esc-to-close, and screen readers announce the toggle as a checkbox rather than a disclosure button. Fine for a demo, wrong for a real product.</p>
      <p>For production, upgrade the checkbox to a <code>&lt;button aria-expanded&gt;</code> plus ~20 lines of vanilla JS. Focus-trap on the drawer while it's open. Esc key closes and returns focus to the trigger. Scrim click closes.</p>
      <p>Body scroll lock when the drawer is open. <code>document.documentElement.style.overflow = 'hidden'</code> when opening, restore on close. This prevents the background from scrolling behind the drawer on iOS Safari.</p>
      <p>The visual layer stays byte-for-byte identical &mdash; the CSS never changes. Only the accessibility infrastructure gets upgraded. The user sees the same glass drawer with the same slide animation and the same scrim.</p>
      <h3>Slide direction and anchor variants</h3>
      <p>Slide from the right instead by starting the drawer at <code>translateX(100%)</code> and anchoring it <code>right:0</code>. Same structure, mirrored anchor. Right-slide is more common on Arabic/Hebrew locale sites (RTL matches natural reading direction).</p>
      <p>Slide from the bottom for a mobile-web-app feel: start at <code>translateY(100%)</code>, anchor <code>bottom:0</code>, make the drawer full-width and short-height. This mimics native iOS action sheets and Android bottom sheets.</p>
      <p>Slide from the top for a full-screen menu overlay: start at <code>translateY(-100%)</code>, anchor <code>top:0</code>, full width AND full height. Reads as an app-shell menu take-over, not a side drawer.</p>
      <p>Stagger the drawer link entrances with <code>transition-delay</code> steps (say 40ms per link) for a cascading reveal that feels premium. Keep the total stagger under 200ms so the drawer feels responsive.</p>
      <h3>Common failure modes</h3>
      <p><code>position:fixed</code> inside a transformed or filtered ancestor is positioned relative to that ancestor, not the viewport. If your drawer is inside a component tree with transforms, promote it to a portal / top-layer container.</p>
      <p>Give the drawer a solid-enough fill (55-65% opacity or higher). Pure blur with a low-opacity fill makes link text hard to read when the drawer sits over a busy background page.</p>
      <p>Blur the scrim, not the drawer's parent. Blurring an ancestor of the drawer will blur the drawer's text too &mdash; the drawer needs to be either a sibling of the scrim or promoted to the top layer.</p>
      <p>Focus trap needs to move focus back to the trigger button on close, not fling it to <code>document.body</code>. Screen reader users lose their place otherwise.</p>
      <h3>When to use the checkbox-hack anyway</h3>
      <p>Prototyping. Storybook demos. Marketing sites without accessibility requirements. Personal portfolio sites where you're the only user. Educational examples that focus on the CSS technique, not the compliance.</p>
      <p>Never for a shipping product. The audit will catch it, and the audit is right.</p>
      <p>Keep scrolling &mdash; the sticky bar demonstrates its pin as the page content flows beneath it.</p>
    </div>
  </div>
  <label for="gn06-toggle" class="gn-06-scrim" aria-hidden="true"></label>
  <aside class="gn-06-drawer" aria-label="Mobile">
    <label for="gn06-toggle" class="gn-06-close" aria-label="Close menu" tabindex="0">&times;</label>
    <nav aria-label="Mobile primary">
      <a href="#" aria-current="page">Home</a>
      <a href="#">Collections</a>
      <a href="#">Journal</a>
      <a href="#">About</a>
      <a href="#">Contact</a>
    </nav>
  </aside>
</div>
```
## CSS
```css
.gn-06 {
  position: relative;
  font-family: system-ui,'Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: stretch;
  border-radius: 16px;
  overflow: hidden;
  background: radial-gradient(100% 100% at 80% 0%,oklch(0.78 0.15 60),oklch(0.6 0.18 20) 45%,oklch(0.4 0.16 330) 100%);
}

.gn-06 * {
  box-sizing: border-box;
}

.gn-06__stage {
  position: relative;
  height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-behavior: smooth;
}

.gn-06-cb {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.gn-06-bar {
  position: sticky;
  top: 16px;
  z-index: 6;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 16px;
  padding: 0 12px 0 18px;
  height: 56px;
  border-radius: 14px;
  background: rgba(255,255,255,.42);
  border: 1px solid rgba(255,255,255,.55);
  -webkit-backdrop-filter: blur(14px) saturate(170%);
  backdrop-filter: blur(14px) saturate(170%);
}

.gn-06-brand {
  font-weight: 800;
  font-size: 17px;
  color: #fff;
  text-decoration: none;
  text-shadow: 0 1px 6px rgba(80,20,10,.35);
}

.gn-06-burger {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  width: 44px;
  height: 44px;
  padding: 0 10px;
  cursor: pointer;
  border-radius: 10px;
}

.gn-06-burger span {
  height: 2.5px;
  border-radius: 2px;
  background: #fff;
  transition: transform .25s ease,opacity .2s ease;
}

.gn-06-scrim {
  position: absolute;
  inset: 0;
  z-index: 7;
  opacity: 0;
  visibility: hidden;
  background: rgba(30,8,8,.28);
  -webkit-backdrop-filter: blur(16px);
  backdrop-filter: blur(16px);
  transition: opacity .3s ease,visibility .3s;
}

.gn-06-drawer {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 8;
  width: min(78%,300px);
  height: 100%;
  padding: 22px;
  transform: translateX(-100%);
  background: rgba(255,255,255,.6);
  border-right: 1px solid rgba(255,255,255,.6);
  box-shadow: 8px 0 40px rgba(40,10,10,.3);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
  backdrop-filter: blur(22px) saturate(180%);
  transition: transform .32s cubic-bezier(.4,0,.2,1);
}

.gn-06-close {
  position: absolute;
  top: 12px;
  right: 16px;
  font-size: 30px;
  line-height: 1;
  color: oklch(0.4 0.08 20);
  cursor: pointer;
}

.gn-06-drawer nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
  margin-top: 44px;
}

.gn-06-drawer nav a {
  display: flex;
  align-items: center;
  height: 48px;
  padding: 0 14px;
  border-radius: 10px;
  font: 600 16px/1 system-ui,sans-serif;
  color: oklch(0.32 0.04 20);
  text-decoration: none;
  transition: background-color .15s ease;
}

.gn-06-drawer nav a:hover {
  background: rgba(255,255,255,.6);
}

.gn-06-drawer nav a[aria-current="page"] {
  color: oklch(0.5 0.2 20);
  background: rgba(255,255,255,.55);
}

.gn-06-body {
  padding: 32px 24px 80px;
  max-width: 640px;
  margin: 0 auto;
  color: rgba(255,255,255,.94);
  text-shadow: 0 1px 6px rgba(60,10,10,.4);
}

.gn-06-body h2 {
  margin: 20px 0 14px;
  font: 800 22px/1.2 system-ui,sans-serif;
  letter-spacing: -.01em;
  color: #fff;
}

.gn-06-body h3 {
  margin: 28px 0 12px;
  font: 700 18px/1.25 system-ui,sans-serif;
  letter-spacing: -.01em;
  color: #fff;
}

.gn-06-body p {
  margin: 0 0 14px;
  font: 500 15px/1.65 system-ui,sans-serif;
}

.gn-06-body code {
  background: rgba(255,255,255,.24);
  border: 1px solid rgba(255,255,255,.35);
  padding: 2px 6px;
  border-radius: 5px;
  font-size: 13px;
  color: #fff;
  text-shadow: none;
  -webkit-backdrop-filter: blur(4px);
  backdrop-filter: blur(4px);
}

.gn-06-cb:checked~.gn-06-scrim {
  opacity: 1;
  visibility: visible;
}

.gn-06-cb:checked~.gn-06-drawer {
  transform: translateX(0);
}

.gn-06-burger:focus-visible,
.gn-06-close:focus-visible,
.gn-06-drawer a:focus-visible {
  outline: 2.5px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .gn-06-drawer {
    transition: opacity .2s ease;
    transform: translateX(0);
    opacity: 0;
    visibility: hidden;
  }

  .gn-06-cb:checked~.gn-06-drawer {
    opacity: 1;
    visibility: visible;
  }
}
```
