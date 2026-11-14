---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/profile-card/"
title: "Profile Card"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A rich hover-card for mentions, comments, and team rosters."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Profile Card
Source: https://codefronts.com/snippets/css-tooltips/profile-card/

A rich hover-card for mentions, comments, and team rosters. Internal elements stagger in: hero glow, then portrait, then name and tagline, then stats — so the card unfolds rather than flicking on. Hover any avatar in the roster below.
## HTML
```html
<div class="tp-05">
  <div class="tp-05__roster">
    <div class="tp-05__head">
      <span>Editorial Team · Vol XII</span>
      <span>3 active</span>
    </div>
    <div class="tp-05__row">
      <div class="tp-05__avatar-trigger">
        <svg class="tp-05__avatar-svg" viewBox="0 0 100 100" aria-hidden="true">
          <defs><linearGradient id="tp-05__av1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c1422c"/><stop offset="1" stop-color="#7a2415"/></linearGradient></defs>
          <rect width="100" height="100" fill="url(#tp-05__av1)"/>
          <text x="50" y="62" text-anchor="middle" font-family="Fraunces" font-size="38" font-style="italic" fill="#f7d18e">M</text>
        </svg>
      </div>
      <div class="tp-05__id">
        <div class="tp-05__name-row">Mira <em>Vance</em></div>
        <div class="tp-05__handle">@miravance</div>
      </div>
      <div class="tp-05__role">Editor-in-Chief</div>
      <div class="tp-05__status"></div>
      <div class="tp-05__card">
        <div class="tp-05__stagger">
          <div class="tp-05__hero"></div>
          <div class="tp-05__body">
            <div class="tp-05__photo">
              <svg viewBox="0 0 100 100" width="100%" height="100%"><rect width="100" height="100" fill="url(#tp-05__av1)"/><text x="50" y="62" text-anchor="middle" font-family="Fraunces" font-size="40" font-style="italic" fill="#f7d18e">M</text></svg>
            </div>
            <div class="tp-05__display-name">Mira <em>Vance</em></div>
            <div class="tp-05__tagline">"Words first; everything else negotiated after."</div>
            <div class="tp-05__stats">
              <div><div class="tp-05__stat-num">142</div><div class="tp-05__stat-label">essays</div></div>
              <div><div class="tp-05__stat-num">8.4k</div><div class="tp-05__stat-label">readers</div></div>
              <div><div class="tp-05__stat-num">VII</div><div class="tp-05__stat-label">volumes</div></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="tp-05__row">
      <div class="tp-05__avatar-trigger">
        <svg class="tp-05__avatar-svg" viewBox="0 0 100 100" aria-hidden="true">
          <defs><linearGradient id="tp-05__av2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2d4a3e"/><stop offset="1" stop-color="#0d1f17"/></linearGradient></defs>
          <rect width="100" height="100" fill="url(#tp-05__av2)"/>
          <text x="50" y="62" text-anchor="middle" font-family="Fraunces" font-size="38" font-style="italic" fill="#f7d18e">A</text>
        </svg>
      </div>
      <div class="tp-05__id">
        <div class="tp-05__name-row">Adesh <em>Kothari</em></div>
        <div class="tp-05__handle">@adesh.k</div>
      </div>
      <div class="tp-05__role">Design Director</div>
      <div class="tp-05__status tp-05__status-away"></div>
      <div class="tp-05__card">
        <div class="tp-05__stagger">
          <div class="tp-05__hero tp-05__hero-green"></div>
          <div class="tp-05__body">
            <div class="tp-05__photo">
              <svg viewBox="0 0 100 100" width="100%" height="100%"><rect width="100" height="100" fill="url(#tp-05__av2)"/><text x="50" y="62" text-anchor="middle" font-family="Fraunces" font-size="40" font-style="italic" fill="#f7d18e">A</text></svg>
            </div>
            <div class="tp-05__display-name">Adesh <em>Kothari</em></div>
            <div class="tp-05__tagline">"Restraint is also a flourish, if you commit to it."</div>
            <div class="tp-05__stats">
              <div><div class="tp-05__stat-num">96</div><div class="tp-05__stat-label">covers</div></div>
              <div><div class="tp-05__stat-num">12</div><div class="tp-05__stat-label">awards</div></div>
              <div><div class="tp-05__stat-num">04</div><div class="tp-05__stat-label">books</div></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="tp-05__row">
      <div class="tp-05__avatar-trigger">
        <svg class="tp-05__avatar-svg" viewBox="0 0 100 100" aria-hidden="true">
          <defs><linearGradient id="tp-05__av3" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6b4226"/><stop offset="1" stop-color="#2a1810"/></linearGradient></defs>
          <rect width="100" height="100" fill="url(#tp-05__av3)"/>
          <text x="50" y="62" text-anchor="middle" font-family="Fraunces" font-size="38" font-style="italic" fill="#f7d18e">J</text>
        </svg>
      </div>
      <div class="tp-05__id">
        <div class="tp-05__name-row">June <em>Lacroix</em></div>
        <div class="tp-05__handle">@junelacroix</div>
      </div>
      <div class="tp-05__role">Photo Editor</div>
      <div class="tp-05__status"></div>
      <div class="tp-05__card">
        <div class="tp-05__stagger">
          <div class="tp-05__hero tp-05__hero-amber"></div>
          <div class="tp-05__body">
            <div class="tp-05__photo">
              <svg viewBox="0 0 100 100" width="100%" height="100%"><rect width="100" height="100" fill="url(#tp-05__av3)"/><text x="50" y="62" text-anchor="middle" font-family="Fraunces" font-size="40" font-style="italic" fill="#f7d18e">J</text></svg>
            </div>
            <div class="tp-05__display-name">June <em>Lacroix</em></div>
            <div class="tp-05__tagline">"A photograph is the slowest sentence a magazine can run."</div>
            <div class="tp-05__stats">
              <div><div class="tp-05__stat-num">311</div><div class="tp-05__stat-label">shoots</div></div>
              <div><div class="tp-05__stat-num">28</div><div class="tp-05__stat-label">cities</div></div>
              <div><div class="tp-05__stat-num">VI</div><div class="tp-05__stat-label">years</div></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-05 {
  width: 100%;
  min-height: 100vh;
  background: #14110d;
  /* Generous bottom room — profile cards drop down from roster rows
       and are ~360px tall, so the gallery card needs room below the
       visible roster for them to render in full. */
  padding: 36px 28px 400px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  font-family: 'Inter', system-ui, sans-serif;
}

.tp-05__roster {
  width: 100%;
  max-width: 560px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 2px;
}

.tp-05__head {
  padding: 12px 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 9.5px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: rgba(239, 236, 230, 0.5);
}

.tp-05__row {
  padding: 14px 20px;
  display: grid;
  grid-template-columns: 40px 1fr auto auto;
  align-items: center;
  gap: 14px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  position: relative;
  color: #efece6;
}

.tp-05__row:last-child {
  border-bottom: none;
}

.tp-05__row:hover {
  background: rgba(255, 255, 255, 0.025);
}

.tp-05__avatar-trigger {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  position: relative;
  cursor: pointer;
  flex-shrink: 0;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1);
}

.tp-05__avatar-trigger:hover {
  transform: scale(1.08);
}

.tp-05__avatar-svg {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  display: block;
}

.tp-05__name-row {
  font-family: Georgia, serif;
  font-size: 17px;
  font-weight: 400;
}

.tp-05__name-row em {
  font-style: italic;
  color: #f7d18e;
  font-weight: 300;
}

.tp-05__handle {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  color: rgba(239, 236, 230, 0.4);
  margin-top: 2px;
}

.tp-05__role {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 9.5px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: rgba(239, 236, 230, 0.5);
}

.tp-05__status {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #6fcf97;
  box-shadow: 0 0 8px rgba(111, 207, 151, 0.6);
}

.tp-05__status-away {
  background: #f7d18e;
  box-shadow: 0 0 8px rgba(247, 209, 142, 0.6);
}

.tp-05__card {
  position: absolute;
  top: calc(100% + 12px);
  left: 20px;
  width: 320px;
  background: linear-gradient(180deg, #1f1a14 0%, #14110d 100%);
  border: 1px solid rgba(247, 209, 142, 0.15);
  border-radius: 2px;
  box-shadow: 0 25px 60px -16px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(247, 209, 142, 0.05), inset 0 1px 0 rgba(247, 209, 142, 0.08);
  opacity: 0;
  visibility: hidden;
  transform: translateY(8px);
  transition: opacity 0.3s, transform 0.4s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear 0.3s;
  z-index: 30;
  pointer-events: none;
  overflow: hidden;
}

.tp-05__row:hover .tp-05__card,
.tp-05__avatar-trigger:hover .tp-05__card {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
  transition-delay: 0s;
}

.tp-05__card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, #f7d18e, transparent);
  opacity: 0.5;
}

.tp-05__hero {
  height: 76px;
  background: radial-gradient(circle at 30% 60%, rgba(193, 66, 44, 0.4), transparent 50%), radial-gradient(circle at 80% 40%, rgba(247, 209, 142, 0.3), transparent 50%), linear-gradient(135deg, #2a201a 0%, #14110d 100%);
  position: relative;
  overflow: hidden;
}

.tp-05__hero-green {
  background: radial-gradient(circle at 30% 60%, rgba(45, 74, 62, 0.5), transparent 50%), radial-gradient(circle at 80% 40%, rgba(247, 209, 142, 0.3), transparent 50%), linear-gradient(135deg, #1a2a23 0%, #14110d 100%);
}

.tp-05__hero-amber {
  background: radial-gradient(circle at 30% 60%, rgba(107, 66, 38, 0.5), transparent 50%), radial-gradient(circle at 80% 40%, rgba(247, 209, 142, 0.25), transparent 50%), linear-gradient(135deg, #2a201a 0%, #14110d 100%);
}

.tp-05__hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: repeating-linear-gradient(45deg, transparent 0, transparent 6px, rgba(247, 209, 142, 0.04) 6px, rgba(247, 209, 142, 0.04) 7px);
}

.tp-05__body {
  padding: 0 18px 16px;
  position: relative;
}

.tp-05__photo {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin-top: -28px;
  border: 2px solid #14110d;
  box-shadow: 0 0 0 1px rgba(247, 209, 142, 0.3);
  position: relative;
  overflow: hidden;
  background: #2a201a;
}

.tp-05__display-name {
  margin-top: 12px;
  font-family: Georgia, serif;
  font-size: 22px;
  font-weight: 400;
  line-height: 1.15;
  color: #efece6;
}

.tp-05__display-name em {
  font-style: italic;
  color: #f7d18e;
  font-weight: 300;
}

.tp-05__tagline {
  margin-top: 6px;
  font-family: Georgia, serif;
  font-size: 13px;
  font-style: italic;
  color: rgba(239, 236, 230, 0.65);
  line-height: 1.4;
}

.tp-05__stats {
  margin-top: 14px;
  padding-top: 12px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.tp-05__stat-num {
  font-family: Georgia, serif;
  font-size: 18px;
  font-weight: 500;
  color: #f7d18e;
}

.tp-05__stat-label {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 8.5px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: rgba(239, 236, 230, 0.4);
  margin-top: 2px;
}

.tp-05__stagger > * {
  opacity: 0;
  transform: translateY(6px);
  transition: opacity 0.4s, transform 0.5s cubic-bezier(0.22, 1, 0.36, 1);
}

.tp-05__row:hover .tp-05__stagger > *,
.tp-05__avatar-trigger:hover .tp-05__stagger > * {
  opacity: 1;
  transform: translateY(0);
}

.tp-05__row:hover .tp-05__stagger > *:nth-child(1) {
  transition-delay: 0.05s;
}

.tp-05__row:hover .tp-05__stagger > *:nth-child(2) {
  transition-delay: 0.18s;
}
```
