---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/team-avatar-card/"
title: "Team Avatar Card"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "Initials-only avatar circles in a row that lift slightly on hover and pop out a full profile card — gradient hero band, larger avatar with shadow ring, role…"
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Team Avatar Card
Source: https://codefronts.com/snippets/css-tooltips/team-avatar-card/

Initials-only avatar circles in a row that lift slightly on hover and pop out a full profile card — gradient hero band, larger avatar with shadow ring, role + presence dot + bio + three-stat row + Message / View Profile buttons. Built for team rosters, mention popovers, comment hovers.
## HTML
```html
<div class="tp-09">
  <div class="tp-09__inner">
    <div class="tp-09__t">
      <div class="tp-09__circle" style="background:linear-gradient(135deg,#6028a0,#9060d0)">SL</div>
      <div class="tp-09__tip">
        <div class="tp-09__hero" style="background:linear-gradient(135deg,#4a1880,#8050c0)">
          <div class="tp-09__photo" style="background:linear-gradient(135deg,#6028a0,#9060d0)">SL</div>
        </div>
        <div class="tp-09__body">
          <div class="tp-09__name">Sarah Lindqvist</div>
          <div class="tp-09__role">CEO · Executive</div>
          <div class="tp-09__online"><span class="tp-09__online-dot" style="background:#22c55e"></span>Active now</div>
          <div class="tp-09__bio">Former Stripe PM. Building the next layer of financial infrastructure for SMBs.</div>
          <div class="tp-09__stats">
            <div><div class="tp-09__stat-n">214</div><div class="tp-09__stat-l">Team</div></div>
            <div><div class="tp-09__stat-n">8yr</div><div class="tp-09__stat-l">Tenure</div></div>
            <div><div class="tp-09__stat-n">$1.2B</div><div class="tp-09__stat-l">Valuation</div></div>
          </div>
        </div>
        <div class="tp-09__foot">
          <div class="tp-09__btn">Message</div>
          <div class="tp-09__btn tp-09__btn-prim">View Profile</div>
        </div>
      </div>
    </div>

    <div class="tp-09__t">
      <div class="tp-09__circle" style="background:linear-gradient(135deg,#204080,#4070c0)">MW</div>
      <div class="tp-09__tip">
        <div class="tp-09__hero" style="background:linear-gradient(135deg,#102060,#3060a0)">
          <div class="tp-09__photo" style="background:linear-gradient(135deg,#204080,#4070c0)">MW</div>
        </div>
        <div class="tp-09__body">
          <div class="tp-09__name">Marcus Webb</div>
          <div class="tp-09__role">CTO · Engineering</div>
          <div class="tp-09__online"><span class="tp-09__online-dot" style="background:#22c55e"></span>Active now</div>
          <div class="tp-09__bio">Ex-Google infra. Obsessed with distributed systems and making things fast at scale.</div>
          <div class="tp-09__stats">
            <div><div class="tp-09__stat-n">96</div><div class="tp-09__stat-l">Team</div></div>
            <div><div class="tp-09__stat-n">5yr</div><div class="tp-09__stat-l">Tenure</div></div>
            <div><div class="tp-09__stat-n">340</div><div class="tp-09__stat-l">PRs</div></div>
          </div>
        </div>
        <div class="tp-09__foot">
          <div class="tp-09__btn">Message</div>
          <div class="tp-09__btn tp-09__btn-prim">View Profile</div>
        </div>
      </div>
    </div>

    <div class="tp-09__t">
      <div class="tp-09__circle" style="background:linear-gradient(135deg,#0a6050,#1aa080)">ER</div>
      <div class="tp-09__tip">
        <div class="tp-09__hero" style="background:linear-gradient(135deg,#054030,#108060)">
          <div class="tp-09__photo" style="background:linear-gradient(135deg,#0a6050,#1aa080)">ER</div>
        </div>
        <div class="tp-09__body">
          <div class="tp-09__name">Elena Russo</div>
          <div class="tp-09__role">CMO · Marketing</div>
          <div class="tp-09__online"><span class="tp-09__online-dot" style="background:#f59e0b"></span>Away · 2h ago</div>
          <div class="tp-09__bio">Brand strategist. Grew Notion's Europe presence 3×. London-based, GMT+1.</div>
          <div class="tp-09__stats">
            <div><div class="tp-09__stat-n">68</div><div class="tp-09__stat-l">Team</div></div>
            <div><div class="tp-09__stat-n">3yr</div><div class="tp-09__stat-l">Tenure</div></div>
            <div><div class="tp-09__stat-n">+84%</div><div class="tp-09__stat-l">YoY</div></div>
          </div>
        </div>
        <div class="tp-09__foot">
          <div class="tp-09__btn">Message</div>
          <div class="tp-09__btn tp-09__btn-prim">View Profile</div>
        </div>
      </div>
    </div>

    <div class="tp-09__t">
      <div class="tp-09__circle" style="background:linear-gradient(135deg,#802050,#c04080)">AP</div>
      <div class="tp-09__tip">
        <div class="tp-09__hero" style="background:linear-gradient(135deg,#601030,#a03060)">
          <div class="tp-09__photo" style="background:linear-gradient(135deg,#802050,#c04080)">AP</div>
        </div>
        <div class="tp-09__body">
          <div class="tp-09__name">Aisha Patel</div>
          <div class="tp-09__role">Growth Lead · Marketing</div>
          <div class="tp-09__online"><span class="tp-09__online-dot" style="background:#94a3b8"></span>Offline</div>
          <div class="tp-09__bio">Data-driven growth. 0 → 100k users in 18 months. Runs the acquisition engine.</div>
          <div class="tp-09__stats">
            <div><div class="tp-09__stat-n">6</div><div class="tp-09__stat-l">Team</div></div>
            <div><div class="tp-09__stat-n">1yr</div><div class="tp-09__stat-l">Tenure</div></div>
            <div><div class="tp-09__stat-n">$1.2M</div><div class="tp-09__stat-l">Budget</div></div>
          </div>
        </div>
        <div class="tp-09__foot">
          <div class="tp-09__btn">Message</div>
          <div class="tp-09__btn tp-09__btn-prim">View Profile</div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-09 {
  width: 100%;
  min-height: 100vh;
  background: #ffffff;
  /* Top room for the profile card (~280px tall) popping up from each
       avatar circle. */
  padding: 300px 28px 40px;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  font-family: 'Inter', system-ui, sans-serif;
}

.tp-09__inner {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  justify-content: center;
}

.tp-09__t {
  position: relative;
  cursor: help;
}

.tp-09__circle {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.9);
  letter-spacing: 0.03em;
  transition: transform .15s, box-shadow .15s;
}

.tp-09__t:hover .tp-09__circle {
  transform: scale(1.1) translateY(-3px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.18);
}

.tp-09__tip {
  position: absolute;
  bottom: calc(100% + 12px);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  width: 240px;
  background: #fff;
  border-radius: 12px;
  border: 1px solid rgba(0, 0, 0, 0.07);
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.12), 0 2px 8px rgba(0, 0, 0, 0.06);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .25s, transform .25s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .25s;
  z-index: 30;
  overflow: hidden;
  text-align: left;
}

.tp-09__t:hover .tp-09__tip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
  transition-delay: 0s;
}

.tp-09__hero {
  height: 56px;
  position: relative;
}

.tp-09__photo {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: 3px solid #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.14);
  position: absolute;
  left: 14px;
  bottom: -14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.92);
}

.tp-09__body {
  padding: 20px 14px 12px;
}

.tp-09__name {
  font-size: 14px;
  font-weight: 600;
  color: #111;
}

.tp-09__role {
  font-size: 10.5px;
  color: #888;
  margin-top: 2px;
}

.tp-09__online {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 10px;
  color: #888;
  margin-top: 6px;
}

.tp-09__online-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
}

.tp-09__bio {
  font-size: 11.5px;
  color: #555;
  margin-top: 8px;
  line-height: 1.5;
}

.tp-09__stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  margin-top: 12px;
  padding-top: 11px;
  border-top: 1px solid #f0f0f0;
  text-align: center;
}

.tp-09__stat-n {
  font-size: 15px;
  font-weight: 700;
  color: #111;
}

.tp-09__stat-l {
  font-size: 8px;
  color: #bbb;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-top: 1px;
}

.tp-09__foot {
  padding: 9px 14px;
  border-top: 1px solid #f0f0f0;
  display: flex;
  gap: 6px;
}

.tp-09__btn {
  flex: 1;
  padding: 6px 0;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 500;
  text-align: center;
  border: 1px solid #e8e8e8;
  color: #444;
  background: #fafafa;
  cursor: pointer;
}

.tp-09__btn-prim {
  background: #111;
  border-color: #111;
  color: #fff;
}
```
