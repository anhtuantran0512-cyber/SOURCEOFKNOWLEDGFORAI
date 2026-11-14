---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/ios-style-bottom-tab-bar/"
title: "iOS-Style Bottom Tab Bar"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "An iOS-inspired bottom navigation bar with four tab pages driven by radio inputs."
has_js: "false"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: iOS-Style Bottom Tab Bar
Source: https://codefronts.com/navigation/css-mobile-navigation/ios-style-bottom-tab-bar/

An iOS-inspired bottom navigation bar with four tab pages driven by radio inputs. Pages transition with a fade-scale effect and the tab bar uses backdrop-filter frosted glass.
## HTML
```html
<div class="mn-03">
  <input type="radio" name="mn-03-tab" id="mn-03-home" checked>
  <input type="radio" name="mn-03-tab" id="mn-03-search">
  <input type="radio" name="mn-03-tab" id="mn-03-alerts">
  <input type="radio" name="mn-03-tab" id="mn-03-profile">

  <div class="mn-03__status">
    <span class="mn-03__status-time">9:41</span>
    <div class="mn-03__status-icons">
      <span>▲</span><span>WiFi</span><span>🔋</span>
    </div>
  </div>

  <div class="mn-03__pages">
    <div class="mn-03__page" data-page="home">
      <div class="mn-03__page-header"><h2>Home</h2></div>
      <div class="mn-03__section-card">
        <div class="mn-03__row">
          <div class="mn-03__row-icon" style="background:#e8f5e9"><span>📈</span></div>
          <div class="mn-03__row-text"><h4>Portfolio Value</h4><p>+2.4% today</p></div>
          <span class="mn-03__row-chevron">›</span>
        </div>
        <div class="mn-03__row">
          <div class="mn-03__row-icon" style="background:#e3f2fd"><span>💳</span></div>
          <div class="mn-03__row-text"><h4>Spending</h4><p>$342 this week</p></div>
          <span class="mn-03__row-chevron">›</span>
        </div>
        <div class="mn-03__row">
          <div class="mn-03__row-icon" style="background:#fce4ec"><span>🎯</span></div>
          <div class="mn-03__row-text"><h4>Savings Goal</h4><p>68% complete</p></div>
          <span class="mn-03__row-chevron">›</span>
        </div>
      </div>
    </div>

    <div class="mn-03__page" data-page="search">
      <div class="mn-03__page-header"><h2>Search</h2></div>
      <div class="mn-03__search-bar">
        <span>🔍</span><p>Search transactions, people...</p>
      </div>
      <div class="mn-03__section-card">
        <div class="mn-03__row">
          <div class="mn-03__row-icon" style="background:#fff3e0"><span>🛒</span></div>
          <div class="mn-03__row-text"><h4>Groceries</h4><p>Yesterday</p></div>
          <span style="font-size:13px;color:#1c1c1e;">-$48</span>
        </div>
        <div class="mn-03__row">
          <div class="mn-03__row-icon" style="background:#e8f5e9"><span>💸</span></div>
          <div class="mn-03__row-text"><h4>Transfer received</h4><p>2 days ago</p></div>
          <span style="font-size:13px;color:#34c759;">+$200</span>
        </div>
      </div>
    </div>

    <div class="mn-03__page" data-page="alerts">
      <div class="mn-03__page-header"><h2>Notifications</h2></div>
      <div class="mn-03__section-card">
        <div class="mn-03__row">
          <div class="mn-03__row-icon" style="background:#fff3e0"><span>⚠️</span></div>
          <div class="mn-03__row-text"><h4>Unusual spend detected</h4><p>$340 at Electronics Hub</p></div>
        </div>
        <div class="mn-03__row">
          <div class="mn-03__row-icon" style="background:#e8f5e9"><span>✅</span></div>
          <div class="mn-03__row-text"><h4>Payment cleared</h4><p>Rent payment confirmed</p></div>
        </div>
      </div>
    </div>

    <div class="mn-03__page" data-page="profile">
      <div class="mn-03__profile-header">
        <div class="mn-03__profile-avatar">👤</div>
        <h3>Jordan Blake</h3>
        <p>Premium Member</p>
      </div>
      <div class="mn-03__section-card">
        <div class="mn-03__row">
          <div class="mn-03__row-icon" style="background:#f3e5f5"><span>🔒</span></div>
          <div class="mn-03__row-text"><h4>Security</h4></div>
          <span class="mn-03__row-chevron">›</span>
        </div>
        <div class="mn-03__row">
          <div class="mn-03__row-icon" style="background:#e3f2fd"><span>🔔</span></div>
          <div class="mn-03__row-text"><h4>Notifications</h4></div>
          <span class="mn-03__row-chevron">›</span>
        </div>
      </div>
    </div>
  </div>

  <div class="mn-03__tabbar">
    <label for="mn-03-home" class="mn-03__tab">
      <div class="mn-03__tab-icon">🏠</div>
      <span class="mn-03__tab-label">Home</span>
    </label>
    <label for="mn-03-search" class="mn-03__tab">
      <div class="mn-03__tab-icon">🔍</div>
      <span class="mn-03__tab-label">Search</span>
    </label>
    <label for="mn-03-alerts" class="mn-03__tab" style="position:relative">
      <div class="mn-03__tab-icon">🔔</div>
      <span class="mn-03__tab-label">Alerts</span>
    </label>
    <label for="mn-03-profile" class="mn-03__tab">
      <div class="mn-03__tab-icon">👤</div>
      <span class="mn-03__tab-label">Profile</span>
    </label>
  </div>
</div>
```
## CSS
```css
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: #0f0f13;
  font-family: -apple-system, 'SF Pro Display', 'Segoe UI', sans-serif;
}

.mn-03 {
  --bg: #f2f2f7;
  --card: #ffffff;
  --accent: #007aff;
  --accent2: #34c759;
  --accent3: #ff9500;
  --accent4: #af52de;
  --accent5: #ff2d55;
  --text: #1c1c1e;
  --muted: #8e8e93;
  --tab-bg: #ffffff;
  --tab-border: rgba(0,0,0,0.1);
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.5);
}

.mn-03 input[type="radio"] {
  display: none;
}
/* Status bar */

.mn-03__status {
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  background: var(--card);
}

.mn-03__status-time {
  font-size: 15px;
  font-weight: 600;
  color: var(--text);
}

.mn-03__status-icons {
  display: flex;
  gap: 6px;
  align-items: center;
  font-size: 12px;
  color: var(--text);
}
/* Page area */

.mn-03__pages {
  position: absolute;
  top: 44px;
  left: 0;
  right: 0;
  bottom: 83px;
}

.mn-03__page {
  position: absolute;
  inset: 0;
  padding: 20px 16px;
  opacity: 0;
  pointer-events: none;
  transform: scale(0.97);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

#mn-03-home:checked ~ .mn-03__pages .mn-03__page[data-page="home"],
#mn-03-search:checked ~ .mn-03__pages .mn-03__page[data-page="search"],
#mn-03-alerts:checked ~ .mn-03__pages .mn-03__page[data-page="alerts"],
#mn-03-profile:checked ~ .mn-03__pages .mn-03__page[data-page="profile"] {
  opacity: 1;
  pointer-events: all;
  transform: scale(1);
}
/* Page header */

.mn-03__page-header {
  margin-bottom: 20px;
}

.mn-03__page-header h2 {
  font-size: 28px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.5px;
}
/* Cards */

.mn-03__section-card {
  background: var(--card);
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 12px;
}

.mn-03__row {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 16px;
  border-bottom: 1px solid rgba(0,0,0,0.05);
}

.mn-03__row:last-child {
  border-bottom: none;
}

.mn-03__row-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  flex-shrink: 0;
}

.mn-03__row-text {
  flex: 1;
}

.mn-03__row-text h4 {
  font-size: 14px;
  font-weight: 500;
  color: var(--text);
}

.mn-03__row-text p {
  font-size: 12px;
  color: var(--muted);
}

.mn-03__row-chevron {
  color: var(--muted);
  font-size: 12px;
}
/* Search page */

.mn-03__search-bar {
  background: var(--card);
  border-radius: 12px;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
}

.mn-03__search-bar span {
  color: var(--muted);
}

.mn-03__search-bar p {
  color: var(--muted);
  font-size: 15px;
}
/* Alerts badge */

.mn-03__badge {
  background: #ff3b30;
  color: #fff;
  font-size: 10px;
  font-weight: 700;
  min-width: 18px;
  height: 18px;
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 4px;
}
/* Bottom Tab Bar */

.mn-03__tabbar {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 83px;
  background: rgba(255,255,255,0.92);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-top: 1px solid var(--tab-border);
  display: flex;
  align-items: flex-start;
  padding-top: 8px;
  z-index: 10;
}

.mn-03__tab {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  padding: 4px 0;
}

.mn-03__tab-icon {
  font-size: 24px;
  line-height: 1;
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.mn-03__tab-label {
  font-size: 10px;
  font-weight: 500;
  color: var(--muted);
  transition: color 0.2s;
}

#mn-03-home:checked ~ .mn-03__tabbar label[for="mn-03-home"] .mn-03__tab-label,
#mn-03-search:checked ~ .mn-03__tabbar label[for="mn-03-search"] .mn-03__tab-label,
#mn-03-alerts:checked ~ .mn-03__tabbar label[for="mn-03-alerts"] .mn-03__tab-label,
#mn-03-profile:checked ~ .mn-03__tabbar label[for="mn-03-profile"] .mn-03__tab-label {
  color: var(--accent);
}

#mn-03-home:checked ~ .mn-03__tabbar label[for="mn-03-home"] .mn-03__tab-icon,
#mn-03-search:checked ~ .mn-03__tabbar label[for="mn-03-search"] .mn-03__tab-icon,
#mn-03-alerts:checked ~ .mn-03__tabbar label[for="mn-03-alerts"] .mn-03__tab-icon,
#mn-03-profile:checked ~ .mn-03__tabbar label[for="mn-03-profile"] .mn-03__tab-icon {
  transform: scale(1.1);
}
/* Profile page */

.mn-03__profile-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px 0 24px;
  background: var(--card);
  border-radius: 16px;
  margin-bottom: 12px;
}

.mn-03__profile-avatar {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), var(--accent4));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 30px;
  margin-bottom: 12px;
}

.mn-03__profile-header h3 {
  font-size: 18px;
  font-weight: 600;
  color: var(--text);
}

.mn-03__profile-header p {
  font-size: 13px;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .mn-03__page,
    .mn-03__tab-icon,
    .mn-03__tab-label {
    transition: none;
  }
}
```
