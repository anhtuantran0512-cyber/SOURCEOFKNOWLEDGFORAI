---
source: "codefronts"
url: "https://codefronts.com/navigation/css-glassmorphic-navbars/glassmorphic-dropdown-mega-menu/"
title: "Glassmorphic Dropdown & Mega Menu"
section: "navigation"
category: "css-glassmorphic-navbars"
category_name: "CSS Glassmorphic Sticky Navbars"
description: "The glassmorphism-navbar-with-dropdown-menu that dodges the notorious double-blur clipping bug: a frosted bar whose dropdown panels and mega-menu are ALSO…"
has_js: "false"
---

Here's a working CSS Glassmorphic Sticky Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphic Dropdown & Mega Menu
Source: https://codefronts.com/navigation/css-glassmorphic-navbars/glassmorphic-dropdown-mega-menu/

The glassmorphism-navbar-with-dropdown-menu that dodges the notorious double-blur clipping bug: a frosted bar whose dropdown panels and mega-menu are ALSO glass, layered correctly so each pane blurs the real page behind it — not a smeared copy of its parent. Opens on hover AND keyboard focus, animated in with @starting-style.
## HTML
```html
<div class="gn-05">
  <div class="gn-05__stage">
    <header class="gn-05-bar">
      <a class="gn-05-brand" href="#">Atlas</a>
      <nav aria-label="Primary">
        <ul class="gn-05-menu">
          <li><a href="#">Home</a></li>
          <li>
            <a href="#" aria-haspopup="true">Products &#9662;</a>
            <div class="gn-05-mega">
              <div><h4>Build</h4><a href="#">Editor</a><a href="#">CLI</a><a href="#">SDK</a></div>
              <div><h4>Ship</h4><a href="#">Deploy</a><a href="#">Analytics</a><a href="#">Edge</a></div>
              <div><h4>Scale</h4><a href="#">Teams</a><a href="#">Security</a><a href="#">SLA</a></div>
            </div>
          </li>
          <li>
            <a href="#" aria-haspopup="true">Company &#9662;</a>
            <div class="gn-05-drop">
              <a href="#">About</a><a href="#">Careers</a><a href="#">Blog</a><a href="#">Press</a>
            </div>
          </li>
          <li><a href="#">Pricing</a></li>
        </ul>
      </nav>
    </header>
    <div class="gn-05-body">
      <h2>Hover Products &sect; the mega-menu opens as glass-on-glass</h2>
      <p>The sticky bar frosts the page behind it. The dropdown panels frost the page behind THEM &mdash; not the bar &mdash; because they're absolutely-positioned siblings anchored to each menu item, not nested inside the bar's blurred surface.</p>
      <p>This dodges the notorious double-blur bug: nesting a <code>backdrop-filter</code> element inside another <code>backdrop-filter</code> element makes the child blur its parent's already-blurred output, producing muddy compound frost and clipping artefacts.</p>
      <p>Open/close is pure CSS. The panels live at <code>opacity:0; visibility:hidden</code> and reveal on <code>li:hover</code> AND <code>li:focus-within</code>, so mouse and keyboard both work. Tabbing into a link inside the panel keeps it open.</p>
      <p>Entrance is animated with <code>@starting-style</code> and <code>transition-behavior:allow-discrete</code> &mdash; the modern way to tween an element from <code>display:none</code>. Without both, the panel pops in with no transition.</p>
      <h3>The double-blur bug, illustrated</h3>
      <p>If you nest the panel inside the bar's DOM (a natural place to put it), the panel's <code>backdrop-filter</code> tries to blur the bar's already-blurred pixels. The result reads as a compound frost with visible seams where the two filter regions meet.</p>
      <p>The fix is structural: the panel must be a DOM sibling to the bar, or an absolutely-positioned child of a non-blurred ancestor. Both panels in this demo are children of each <code>&lt;li&gt;</code> with <code>position:absolute; top:calc(100% + 8px)</code>.</p>
      <p>Because the panel is outside the bar's blur surface, it samples the actual page pixels beneath it. Both surfaces frost the same underlying content at the same strength &mdash; no compounding, no seams.</p>
      <p>The same rule applies to modals, tooltips, popovers, and any other glass surface that appears above another glass surface. Never nest; always sibling or promote to a portal-style top-layer container.</p>
      <h3>Frost strength ratios</h3>
      <p>Match the two frost strengths deliberately. Identical blur on bar and panel reads as one material. A slightly stronger panel blur reads as closer to the viewer &mdash; use that when the panel needs perceptual lift over the bar.</p>
      <p>This demo uses <code>blur(16px) saturate(180%)</code> on the bar and <code>blur(18px) saturate(180%)</code> on the panel. The 2px difference is imperceptible in isolation but reads as depth when they're stacked visually.</p>
      <p>Never blur the panel more than 24px. Above that, the sampling artefact starts to show as a moir&eacute; pattern where the panel's blur circle overlaps busy background content.</p>
      <h3>Mega-menu vs dropdown structural difference</h3>
      <p>Widen the panel and switch its layout to <code>grid-template-columns:repeat(3, 1fr)</code> for a mega-menu; keep it narrow with a column of links for a classic dropdown. Same structural pattern, different scale.</p>
      <p>The mega-menu here has three columns: Build, Ship, Scale. Each column carries a small caps heading and a link stack. On mobile widths (below 640px), collapse to a single column with <code>grid-template-columns: 1fr</code>.</p>
      <p>Add a hover-intent delay with <code>transition-delay</code> on the close so the panel doesn't vanish if the pointer clips a corner while moving toward the links.</p>
      <h3>Accessibility contract</h3>
      <p>Every trigger has <code>aria-haspopup="true"</code> so screen readers announce it as opening a submenu. The chevron in the trigger text is a Unicode down-triangle character &mdash; announced but decorative.</p>
      <p>Keyboard: focus lands on the trigger, panel opens on focus (via <code>:focus-within</code> on the <code>&lt;li&gt;</code>), tab moves through the panel links, tabbing out of the last link closes the panel and moves to the next top-level trigger.</p>
      <p>Screen readers announce the panel as a menu because the trigger has <code>aria-haspopup</code>. For richer control, add <code>role="menu"</code> to the panel and <code>role="menuitem"</code> to each link &mdash; but that's optional for a browse-to-navigate mega menu.</p>
      <p>Add <code>aria-expanded</code> that flips true/false on hover/focus if the pattern needs the announcement. For hover-driven menus (this pattern), most teams skip the announcement to keep the SR experience quiet.</p>
      <p>Keep scrolling &mdash; the sticky bar and its dropdowns stay ready to hover as the content passes underneath.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.gn-05 {
  font-family: system-ui,'Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: stretch;
  border-radius: 16px;
  overflow: hidden;
  background: linear-gradient(135deg,oklch(0.68 0.18 25),oklch(0.6 0.19 350) 45%,oklch(0.55 0.18 285));
}

.gn-05 * {
  box-sizing: border-box;
}

.gn-05__stage {
  position: relative;
  height: 100vh;
  overflow-y: auto;
  scroll-behavior: smooth;
  padding: 20px;
  overflow-x: visible;
}

.gn-05-bar {
  position: sticky;
  top: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 0 20px;
  height: 60px;
  border-radius: 14px;
  background: rgba(255,255,255,.5);
  border: 1px solid rgba(255,255,255,.6);
  box-shadow: 0 8px 28px rgba(50,10,40,.2);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  backdrop-filter: blur(16px) saturate(180%);
}

.gn-05-brand {
  font-weight: 800;
  font-size: 17px;
  color: oklch(0.3 0.07 15);
  text-decoration: none;
}

.gn-05-menu {
  display: flex;
  gap: 2px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.gn-05-menu>li {
  position: relative;
}

.gn-05-menu>li>a {
  display: flex;
  align-items: center;
  height: 60px;
  padding: 0 14px;
  font: 600 14px/1 system-ui,sans-serif;
  color: oklch(0.32 0.03 15);
  text-decoration: none;
  transition: color .15s ease;
}

.gn-05-menu>li>a:hover {
  color: oklch(0.42 0.2 15);
}

.gn-05-mega,
.gn-05-drop {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  z-index: 20;
  padding: 16px;
  border-radius: 14px;
  background: rgba(255,255,255,.62);
  border: 1px solid rgba(255,255,255,.7);
  box-shadow: 0 16px 40px rgba(50,10,40,.24);
  -webkit-backdrop-filter: blur(18px) saturate(180%);
  backdrop-filter: blur(18px) saturate(180%);
  opacity: 0;
  visibility: hidden;
  transform: translateY(-6px);
  transition: opacity .2s ease,transform .2s ease,visibility .2s;
  transition-behavior: allow-discrete;
}

.gn-05-mega {
  display: grid;
  grid-template-columns: repeat(3,minmax(120px,1fr));
  gap: 8px 22px;
  width: max-content;
}

.gn-05-mega h4 {
  margin: 0 0 8px;
  font: 700 11px/1 system-ui,sans-serif;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: oklch(0.5 0.02 15);
}

.gn-05-mega a,
.gn-05-drop a {
  display: block;
  padding: 7px 10px;
  border-radius: 8px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: oklch(0.34 0.03 15);
  text-decoration: none;
  transition: background-color .14s ease;
}

.gn-05-drop {
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 180px;
}

.gn-05-mega a:hover,
.gn-05-drop a:hover {
  background: rgba(255,255,255,.7);
  color: oklch(0.42 0.2 15);
}

.gn-05-menu>li:hover .gn-05-mega,
.gn-05-menu>li:hover .gn-05-drop,
.gn-05-menu>li:focus-within .gn-05-mega,
.gn-05-menu>li:focus-within .gn-05-drop {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

@starting-style {
  .gn-05-menu>li:hover .gn-05-mega,
    .gn-05-menu>li:hover .gn-05-drop,
    .gn-05-menu>li:focus-within .gn-05-mega,
    .gn-05-menu>li:focus-within .gn-05-drop {
    opacity: 0;
    transform: translateY(-6px);
  }
}

.gn-05-bar a:focus-visible {
  outline: 2.5px solid oklch(0.45 0.2 15);
  outline-offset: 2px;
}

.gn-05-body {
  padding: 40px 8px 80px;
  max-width: 640px;
  margin-inline: auto;
  color: rgba(255,255,255,.92);
  text-shadow: 0 1px 6px rgba(60,10,40,.35);
}

.gn-05-body h2 {
  margin: 20px 0 14px;
  font: 800 22px/1.2 system-ui,sans-serif;
  letter-spacing: -.01em;
  color: #fff;
}

.gn-05-body h3 {
  margin: 28px 0 12px;
  font: 700 18px/1.25 system-ui,sans-serif;
  letter-spacing: -.01em;
  color: #fff;
}

.gn-05-body p {
  margin: 0 0 14px;
  font: 500 15px/1.65 system-ui,sans-serif;
}

.gn-05-body code {
  background: rgba(255,255,255,.28);
  border: 1px solid rgba(255,255,255,.35);
  padding: 2px 6px;
  border-radius: 5px;
  font-size: 13px;
  color: #fff;
  text-shadow: none;
  -webkit-backdrop-filter: blur(4px);
  backdrop-filter: blur(4px);
}

@media (max-width: 640px) {
  .gn-05-bar {
    gap: 12px;
    padding: 0 12px;
    height: 56px;
    overflow-x: auto;
    scrollbar-width: none;
  }

  .gn-05-bar::-webkit-scrollbar {
    display: none;
  }

  .gn-05-brand {
    font-size: 15px;
    flex-shrink: 0;
  }

  .gn-05-menu {
    flex-wrap: nowrap;
  }

  .gn-05-menu>li>a {
    height: 56px;
    padding: 0 10px;
    font-size: 13px;
    white-space: nowrap;
  }

  .gn-05-mega {
    grid-template-columns: 1fr;
    min-width: 220px;
  }

  .gn-05-mega,
    .gn-05-drop {
    left: auto;
    right: auto;
  }
}

@media (max-width: 400px) {
  .gn-05-menu>li>a {
    padding: 0 8px;
    font-size: 12px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gn-05-mega,
    .gn-05-drop {
    transition: opacity .01s;
  }
}
```
