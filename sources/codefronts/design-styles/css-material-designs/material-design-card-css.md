---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-card-css/"
title: "Material Design Card CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Elevated, outlined, tonal, horizontal, social-media, stats, and profile cards showcasing Material Design 3 shape tokens, elevation shadows, and colour roles."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Card CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-card-css/

Elevated, outlined, tonal, horizontal, social-media, stats, and profile cards showcasing Material Design 3 shape tokens, elevation shadows, and colour roles.
## HTML
```html
<div class="md-02">
  <div class="md-02__page-title">Material Design 3 Cards</div>
  <div class="md-02__page-sub">Elevated, outlined, tonal and horizontal card patterns — pure CSS Material Design components</div>

  <div class="md-02__grid">

    <!-- Media + actions card -->
    <div class="md-02__card md-02__card--elev2">
      <div class="md-02__media-bg" style="background:linear-gradient(135deg,#1565c0,#42a5f5)">🌊</div>
      <div class="md-02__card-body">
        <div class="md-02__card-overline" style="color:var(--c1)">Ocean Series</div>
        <div class="md-02__card-title">Deep Blue UI Components</div>
        <div class="md-02__card-sub">A comprehensive set of Material Design 3 components crafted for modern web applications.</div>
        <span class="md-02__tag" style="background:#e3f2fd;color:#1565c0">CSS</span>
        <span class="md-02__tag" style="background:#e8eaf6;color:#3949ab">Design</span>
      </div>
      <div class="md-02__card-actions">
        <button class="md-02__card-btn md-02__card-btn--p">Share</button>
        <button class="md-02__card-btn md-02__card-btn--s">Explore</button>
      </div>
    </div>

    <!-- Social / header card -->
    <div class="md-02__card md-02__card--elev1">
      <div class="md-02__card-header">
        <div class="md-02__avatar" style="background:#e91e63">M</div>
        <div class="md-02__card-header-text">
          <div class="md-02__card-title">Maria Chen</div>
          <div class="md-02__card-sub">Lead UI Designer · 2h ago</div>
        </div>
        <span class="md-02__card-menu">⋮</span>
      </div>
      <div class="md-02__media-bg" style="background:linear-gradient(135deg,#e91e63,#ff80ab);height:140px">🎨</div>
      <div class="md-02__card-body">
        <div class="md-02__card-sub">Just shipped the new icon system for our design tokens library. 340 icons, fully optimised SVGs!</div>
      </div>
      <div class="md-02__card-actions">
        <button class="md-02__card-btn" style="color:#e91e63">♥ Like</button>
        <button class="md-02__card-btn" style="color:var(--ink2)">💬 Comment</button>
        <button class="md-02__card-btn" style="color:var(--ink2)">↗ Share</button>
      </div>
    </div>

    <!-- Stats card -->
    <div class="md-02__card md-02__card--elev3">
      <div class="md-02__card-body">
        <div class="md-02__card-overline" style="color:var(--c3)">Revenue · June 2025</div>
        <div class="md-02__stat" style="color:var(--c3)">$84,240</div>
        <span class="md-02__stat-change md-02__stat-change--up">↑ 12.4% vs last month</span>
        <div class="md-02__card-progress">
          <div style="display:flex;justify-content:space-between;font-size:.75rem;color:var(--ink3);margin-bottom:6px"><span>Goal progress</span><span>84%</span></div>
          <div class="md-02__card-progress-track"><div class="md-02__card-progress-fill" style="width:84%;background:var(--c3)"></div></div>
        </div>
        <div style="margin-top:12px;display:grid;grid-template-columns:1fr 1fr;gap:12px">
          <div><div style="font-size:1.2rem;font-weight:700;color:var(--ink)">2,840</div><div style="font-size:.78rem;color:var(--ink2)">New customers</div></div>
          <div><div style="font-size:1.2rem;font-weight:700;color:var(--ink)">94.2%</div><div style="font-size:.78rem;color:var(--ink2)">Satisfaction</div></div>
        </div>
      </div>
    </div>

    <!-- Horizontal card -->
    <div class="md-02__card md-02__card--elev2 md-02__card--horizontal">
      <div class="md-02__media-bg" style="background:linear-gradient(180deg,#7b1fa2,#ce93d8);font-size:2.5rem">🎵</div>
      <div style="display:flex;flex-direction:column;flex:1">
        <div class="md-02__card-body" style="flex:1">
          <div class="md-02__card-overline" style="color:var(--c5)">Now Playing</div>
          <div class="md-02__card-title">Midnight Motion</div>
          <div class="md-02__card-sub">Aurora Collective · 3:24</div>
        </div>
        <div class="md-02__card-actions">
          <button class="md-02__card-btn" style="color:var(--c5)">⏮</button>
          <button class="md-02__card-btn" style="color:var(--c5)">⏸</button>
          <button class="md-02__card-btn" style="color:var(--c5)">⏭</button>
        </div>
      </div>
    </div>

    <!-- Outlined card -->
    <div class="md-02__card md-02__card--outlined">
      <div class="md-02__card-body">
        <div class="md-02__card-overline" style="color:var(--c4)">Product · Limited Edition</div>
        <div class="md-02__card-title">Sunset Ceramic Mug</div>
        <div class="md-02__card-sub">Handcrafted from high-fire stoneware with a reactive glaze finish. Each piece is uniquely patterned.</div>
        <div style="font-size:1.5rem;font-weight:700;color:var(--c4);margin-top:12px">$42.00</div>
        <div style="font-size:.8rem;color:var(--ink3);text-decoration:line-through">$58.00</div>
      </div>
      <div class="md-02__card-actions">
        <button class="md-02__card-btn" style="color:var(--c4)">♡ Wishlist</button>
        <button class="md-02__card-btn" style="color:var(--c4)">🛒 Add to Cart</button>
      </div>
    </div>

    <!-- Tonal filled card -->
    <div class="md-02__card md-02__card--tonal-blue md-02__card--elev1">
      <div class="md-02__card-body">
        <div style="font-size:2rem;margin-bottom:12px">📅</div>
        <div class="md-02__card-title" style="color:#0d47a1">Team Standup</div>
        <div class="md-02__card-sub" style="color:#1565c0">Today · 10:00 AM – 10:30 AM</div>
        <div style="margin-top:14px;display:flex;flex-direction:column;gap:6px">
          <div style="font-size:.85rem;color:#1565c0">📍 Google Meet · <a style="color:inherit">join.meet.com/abc-xyz</a></div>
          <div style="font-size:.85rem;color:#1565c0">👥 Priya, Alex, Sam +3</div>
        </div>
      </div>
      <div class="md-02__card-actions" style="border-top:1px solid rgba(21,101,192,.2)">
        <button class="md-02__card-btn" style="color:#1565c0">Decline</button>
        <button class="md-02__card-btn" style="color:#1565c0">Join Call</button>
      </div>
    </div>

    <!-- Tonal green -->
    <div class="md-02__card md-02__card--tonal-green md-02__card--elev1">
      <div class="md-02__card-body">
        <div style="font-size:2rem;margin-bottom:12px">✅</div>
        <div class="md-02__card-title" style="color:#1b5e20">Sprint Goal Achieved</div>
        <div class="md-02__card-sub" style="color:#2e7d32;margin-bottom:14px">All 24 story points completed ahead of schedule.</div>
        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;text-align:center">
          <div><div style="font-size:1.3rem;font-weight:700;color:#1b5e20">24</div><div style="font-size:.72rem;color:#388e3c">Points</div></div>
          <div><div style="font-size:1.3rem;font-weight:700;color:#1b5e20">8</div><div style="font-size:.72rem;color:#388e3c">Stories</div></div>
          <div><div style="font-size:1.3rem;font-weight:700;color:#1b5e20">0</div><div style="font-size:.72rem;color:#388e3c">Bugs</div></div>
        </div>
      </div>
    </div>

    <!-- Profile / contact card -->
    <div class="md-02__card md-02__card--elev2">
      <div style="background:linear-gradient(135deg,#00897b,#80cbc4);height:80px"></div>
      <div style="padding:0 16px 16px;margin-top:-28px">
        <div class="md-02__avatar" style="background:#00897b;width:56px;height:56px;font-size:1.3rem;border:3px solid #fff">JK</div>
        <div style="margin-top:8px">
          <div class="md-02__card-title">Jordan Kim</div>
          <div class="md-02__card-sub">Senior Product Designer at Nexus Co.</div>
        </div>
        <div style="display:flex;gap:8px;margin-top:14px;flex-wrap:wrap">
          <span class="md-02__tag" style="background:#e0f2f1;color:#00695c">🎨 Figma</span>
          <span class="md-02__tag" style="background:#e0f2f1;color:#00695c">✦ Framer</span>
          <span class="md-02__tag" style="background:#e0f2f1;color:#00695c">⚡ CSS</span>
        </div>
      </div>
      <div class="md-02__card-actions">
        <button class="md-02__card-btn" style="color:#00897b">Message</button>
        <button class="md-02__card-btn" style="color:#00897b">Follow</button>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.md-02,
.md-02 *,
.md-02 *::before,
.md-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-02 ::selection {
  background: #1565c0;
  color: #fff;
}

.md-02 {
  --c1: #1565c0;
  --c2: #e91e63;
  --c3: #00897b;
  --c4: #f57c00;
  --c5: #7b1fa2;
  --bg: #eceff1;
  --surface: #fff;
  --ink: #212121;
  --ink2: #616161;
  --ink3: #9e9e9e;
  --divider: #e0e0e0;
  font-family: 'Roboto',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 48px 24px 80px;
  color: var(--ink);
}

.md-02__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(300px,1fr));
  gap: 24px;
  max-width: 1200px;
  margin: 0 auto;
}

.md-02__page-title {
  font-size: clamp(1.4rem,4vw,2rem);
  font-weight: 700;
  margin-bottom: 4px;
  max-width: 1200px;
  margin: 0 auto 8px;
}

.md-02__page-sub {
  font-size: .9rem;
  color: var(--ink2);
  max-width: 1200px;
  margin: 0 auto 40px;
}
/* Base card */

.md-02__card {
  background: var(--surface);
  border-radius: 12px;
  overflow: hidden;
  position: relative;
  transition: box-shadow .25s cubic-bezier(.4,0,.2,1),transform .25s cubic-bezier(.4,0,.2,1);
  cursor: pointer;
}

.md-02__card--elev1 {
  box-shadow: 0 1px 3px rgba(0,0,0,.12),0 1px 2px rgba(0,0,0,.24);
}

.md-02__card--elev2 {
  box-shadow: 0 3px 6px rgba(0,0,0,.15),0 2px 4px rgba(0,0,0,.12);
}

.md-02__card--elev3 {
  box-shadow: 0 10px 20px rgba(0,0,0,.12),0 3px 6px rgba(0,0,0,.08);
}

.md-02__card:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,.15),0 10px 10px rgba(0,0,0,.1);
  transform: translateY(-3px);
}
/* Media card */

.md-02__media {
  width: 100%;
  height: 180px;
  object-fit: cover;
  display: block;
}

.md-02__media-bg {
  width: 100%;
  height: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
}

.md-02__card-body {
  padding: 16px;
}

.md-02__card-overline {
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  font-weight: 500;
  margin-bottom: 4px;
}

.md-02__card-title {
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.3;
  margin-bottom: 6px;
}

.md-02__card-sub {
  font-size: .85rem;
  color: var(--ink2);
  margin-bottom: 12px;
  line-height: 1.5;
}

.md-02__card-actions {
  display: flex;
  gap: 8px;
  padding: 8px 8px 8px;
  border-top: 1px solid var(--divider);
  margin-top: 4px;
}

.md-02__card-btn {
  background: transparent;
  border: none;
  cursor: pointer;
  font-family: 'Roboto';
  font-size: .8rem;
  font-weight: 500;
  letter-spacing: .089em;
  text-transform: uppercase;
  padding: 6px 12px;
  border-radius: 4px;
  transition: background .15s;
}

.md-02__card-btn--p {
  color: var(--c1);
}

.md-02__card-btn--p:hover {
  background: rgba(21,101,192,.08);
}

.md-02__card-btn--s {
  color: var(--c2);
}

.md-02__card-btn--s:hover {
  background: rgba(233,30,99,.08);
}
/* Horizontal card */

.md-02__card--horizontal {
  display: flex;
  align-items: stretch;
}

.md-02__card--horizontal .md-02__media-bg {
  width: 120px;
  flex-shrink: 0;
  height: auto;
  border-radius: 0;
}

.md-02__card--horizontal .md-02__card-body {
  flex: 1;
}
/* Outlined card */

.md-02__card--outlined {
  box-shadow: none;
  border: 1px solid var(--divider);
}

.md-02__card--outlined:hover {
  box-shadow: 0 3px 6px rgba(0,0,0,.1);
  border-color: transparent;
}
/* Tonal/filled card */

.md-02__card--tonal-blue {
  background: #e3f2fd;
  box-shadow: none;
}

.md-02__card--tonal-green {
  background: #e8f5e9;
  box-shadow: none;
}

.md-02__card--tonal-pink {
  background: #fce4ec;
  box-shadow: none;
}

.md-02__card--tonal-amber {
  background: #fff8e1;
  box-shadow: none;
}
/* Avatar row */

.md-02__card-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 16px 0;
}

.md-02__avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  font-weight: 700;
  color: #fff;
  flex-shrink: 0;
}

.md-02__card-header-text .md-02__card-title {
  font-size: .95rem;
  margin-bottom: 2px;
}

.md-02__card-header-text .md-02__card-sub {
  font-size: .8rem;
  margin-bottom: 0;
}

.md-02__card-menu {
  margin-left: auto;
  font-size: 1.2rem;
  cursor: pointer;
  color: var(--ink3);
  padding: 4px;
}
/* Stat card */

.md-02__stat {
  font-size: 2rem;
  font-weight: 700;
  line-height: 1;
  margin-bottom: 4px;
}

.md-02__stat-change {
  font-size: .8rem;
  font-weight: 500;
  padding: 2px 8px;
  border-radius: 12px;
  display: inline-block;
  margin-bottom: 8px;
}

.md-02__stat-change--up {
  background: #e8f5e9;
  color: #2e7d32;
}

.md-02__stat-change--down {
  background: #fce4ec;
  color: #c62828;
}
/* Progress in card */

.md-02__card-progress {
  margin: 8px 0 4px;
}

.md-02__card-progress-track {
  height: 4px;
  background: #e0e0e0;
  border-radius: 2px;
  overflow: hidden;
}

.md-02__card-progress-fill {
  height: 100%;
  border-radius: 2px;
  transition: width .4s ease;
}
/* Tag chip */

.md-02__tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: .75rem;
  font-weight: 500;
  margin-right: 6px;
  margin-bottom: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .md-02 * {
    transition: none!important;
  }
}
```
