---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/sticky-fixed-vertical-navigation-sidebar/"
title: "Sticky Fixed Vertical Navigation Sidebar"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A full-height sidebar that remains anchored to the viewport top while long-form main content scrolls independently alongside it using position:sticky."
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Fixed Vertical Navigation Sidebar
Source: https://codefronts.com/navigation/css-side-menu/sticky-fixed-vertical-navigation-sidebar/

A full-height sidebar that remains anchored to the viewport top while long-form main content scrolls independently alongside it using position:sticky.
## HTML
```html
<div class="sm-06">
  <nav class="sm-06__nav">
    <div class="sm-06__brand">
      <div class="sm-06__logo">N</div>
      <div>
        <span class="sm-06__brand-name">Nova</span>
        <span class="sm-06__brand-plan">Pro</span>
      </div>
    </div>
    <div class="sm-06__section">
      <div class="sm-06__section-lbl">Content</div>
      <a class="sm-06__link sm-06__link--active" href="#">
        <span class="sm-06__link-pip"></span> Articles
        <span class="sm-06__badge">24</span>
      </a>
      <a class="sm-06__link" href="#">
        <span class="sm-06__link-pip"></span> Drafts
        <span class="sm-06__badge">3</span>
      </a>
      <a class="sm-06__link" href="#"><span class="sm-06__link-pip"></span> Media</a>
      <a class="sm-06__link" href="#"><span class="sm-06__link-pip"></span> Comments</a>
      <div class="sm-06__divider"></div>
      <div class="sm-06__section-lbl">Manage</div>
      <a class="sm-06__link" href="#"><span class="sm-06__link-pip"></span> Users</a>
      <a class="sm-06__link" href="#"><span class="sm-06__link-pip"></span> Settings</a>
      <a class="sm-06__link" href="#"><span class="sm-06__link-pip"></span> Plugins</a>
    </div>
    <div class="sm-06__upgrade">
      <div class="sm-06__upgrade-title">Upgrade to Team</div>
      <div class="sm-06__upgrade-sub">Collaborate with up to 20 members and unlock analytics.</div>
      <div class="sm-06__upgrade-btn">View Plans →</div>
    </div>
  </nav>
  <div class="sm-06__main">
    <div class="sm-06__page-title">Articles</div>
    <div class="sm-06__page-sub">The sidebar stays fixed while this content area scrolls. Scroll down to verify.</div>
    <div class="sm-06__article">
      <div class="sm-06__article-title">Getting Started with CSS Grid Layout</div>
      <div class="sm-06__article-body">A comprehensive guide to modern CSS Grid including template areas, named lines, and implicit grids for professional web layouts.</div>
      <div class="sm-06__article-meta">Published · 4 min read</div>
    </div>
    <div class="sm-06__article">
      <div class="sm-06__article-title">Mastering the CSS Cascade & Specificity</div>
      <div class="sm-06__article-body">Deep dive into how browsers resolve style conflicts, the cascade algorithm, and why understanding layers beats specificity hacks.</div>
      <div class="sm-06__article-meta">Draft · 7 min read</div>
    </div>
    <div class="sm-06__article">
      <div class="sm-06__article-title">Container Queries: A New Era of Responsive UI</div>
      <div class="sm-06__article-body">Explore how container queries enable truly component-level responsiveness without relying on the viewport width at all.</div>
      <div class="sm-06__article-meta">Published · 5 min read</div>
    </div>
    <div class="sm-06__article">
      <div class="sm-06__article-title">Advanced CSS Custom Properties Techniques</div>
      <div class="sm-06__article-body">Beyond basic theming: learn how to use custom properties as data channels, calculation bridges, and runtime animation drivers.</div>
      <div class="sm-06__article-meta">Published · 6 min read</div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-06,
.sm-06 *,
.sm-06 *::before,
.sm-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-06 ::selection {
  background: #db2777;
  color: #fff;
}

.sm-06 {
  --bg: #0c0c14;
  --surface: #15151f;
  --nav-bg: #0e0e19;
  --accent: #db2777;
  --accent2: #f472b6;
  --text: #f8fafc;
  --muted: #6b7280;
  --border: rgba(219,39,119,0.15);
  --font: 'Manrope', system-ui, sans-serif;
  --nav-w: 240px;
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  display: flex;
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  border-radius: 12px;
}
/* Sticky sidebar */

.sm-06__nav {
  width: var(--nav-w);
  position: sticky;
  top: 0;
  height: 100vh;
  background: var(--nav-bg);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  padding: 20px 0;
  flex-shrink: 0;
  overflow: hidden;
}
/* Top glow */

.sm-06__nav::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 120px;
  height: 120px;
  background: radial-gradient(circle, rgba(219,39,119,0.15), transparent 70%);
  pointer-events: none;
}

.sm-06__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 0 18px 18px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 16px;
}

.sm-06__logo {
  width: 34px;
  height: 34px;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 14px;
  color: #fff;
}

.sm-06__brand-name {
  font-size: 15px;
  font-weight: 800;
}

.sm-06__brand-plan {
  font-size: 10px;
  color: var(--accent2);
  font-weight: 700;
  background: rgba(219,39,119,0.12);
  padding: 1px 6px;
  border-radius: 99px;
  margin-left: 4px;
}

.sm-06__section {
  padding: 0 18px;
  flex: 1;
}

.sm-06__section-lbl {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 6px;
  margin-top: 4px;
}

.sm-06__link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  border-radius: 9px;
  color: var(--muted);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.2s;
  margin-bottom: 1px;
  position: relative;
}

.sm-06__link:hover {
  color: var(--text);
  background: rgba(219,39,119,0.1);
}

.sm-06__link--active {
  color: var(--text);
  background: rgba(219,39,119,0.15);
}

.sm-06__link--active .sm-06__link-pip {
  background: var(--accent);
  box-shadow: 0 0 8px var(--accent);
}

.sm-06__link-pip {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--muted);
  flex-shrink: 0;
  transition: background 0.2s, box-shadow 0.2s;
}

.sm-06__link:hover .sm-06__link-pip {
  background: var(--accent2);
}

.sm-06__badge {
  margin-left: auto;
  background: rgba(219,39,119,0.2);
  color: var(--accent2);
  font-size: 10px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 99px;
}

.sm-06__divider {
  height: 1px;
  background: var(--border);
  margin: 10px 0;
}

.sm-06__upgrade {
  margin: 0 10px 16px;
  padding: 14px;
  background: linear-gradient(135deg, rgba(219,39,119,0.15), rgba(244,114,182,0.08));
  border: 1px solid rgba(219,39,119,0.25);
  border-radius: 10px;
}

.sm-06__upgrade-title {
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 4px;
}

.sm-06__upgrade-sub {
  font-size: 11px;
  color: var(--muted);
  line-height: 1.5;
}

.sm-06__upgrade-btn {
  display: inline-block;
  margin-top: 10px;
  padding: 6px 14px;
  background: var(--accent);
  color: #fff;
  font-size: 12px;
  font-weight: 700;
  border-radius: 7px;
  cursor: pointer;
}
/* Main content — scrollable */

.sm-06__main {
  flex: 1;
  min-width: 0;
  overflow-y: auto;
  padding: 24px;
}

.sm-06__main::-webkit-scrollbar {
  width: 4px;
}

.sm-06__main::-webkit-scrollbar-track {
  background: transparent;
}

.sm-06__main::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 4px;
}

.sm-06__page-title {
  font-size: 20px;
  font-weight: 800;
  margin-bottom: 4px;
}

.sm-06__page-sub {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 24px;
  line-height: 1.6;
}

.sm-06__article {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 16px;
  margin-bottom: 12px;
}

.sm-06__article-title {
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 6px;
}

.sm-06__article-body {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.7;
}

.sm-06__article-meta {
  font-size: 11px;
  color: rgba(219,39,119,0.7);
  margin-top: 8px;
  font-weight: 600;
}

@container (max-width: 720px), (max-width: 720px) {
  .sm-06 {
    --nav-w: 64px;
  }

  .sm-06__brand {
    padding: 0 12px 14px;
    justify-content: center;
  }

  .sm-06__brand > div:last-child {
    display: none;
  }

  .sm-06__section {
    padding: 0 8px;
  }

  .sm-06__link {
    padding: 10px 8px;
    justify-content: center;
    gap: 0;
    font-size: 0;
  }

  .sm-06__link-pip {
    width: 8px;
    height: 8px;
  }

  .sm-06__badge,
    .sm-06__section-lbl {
    display: none;
  }

  .sm-06__upgrade {
    display: none;
  }

  .sm-06__main {
    padding: 16px;
    min-width: 0;
  }

  .sm-06__article {
    padding: 14px;
  }

  .sm-06__article-title,
    .sm-06__article-body {
    overflow-wrap: anywhere;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sm-06__link,
    .sm-06__link-pip {
    transition: none;
  }
}
```
