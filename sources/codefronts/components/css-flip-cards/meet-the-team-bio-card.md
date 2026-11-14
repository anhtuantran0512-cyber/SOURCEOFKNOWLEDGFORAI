---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/meet-the-team-bio-card/"
title: "Meet the Team Bio Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front shows avatar, role badge, name, and key stats; back reveals biography, social icon links, and a contact email action."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Meet the Team Bio Card
Source: https://codefronts.com/components/css-flip-cards/meet-the-team-bio-card/

Front shows avatar, role badge, name, and key stats; back reveals biography, social icon links, and a contact email action.
## HTML
```html
<div class="fc-04">
  <div class="fc-04__scene">
    <div class="fc-04__card">
      <div class="fc-04__front">
        <div class="fc-04__avatar">
          <svg width="60" height="60" viewBox="0 0 60 60"><circle cx="30" cy="22" r="14" fill="rgba(59,130,246,.6)"/><ellipse cx="30" cy="54" rx="22" ry="16" fill="rgba(59,130,246,.4)"/></svg>
        </div>
        <div class="fc-04__role-badge">Lead Designer</div>
        <div class="fc-04__member-name">Aria Chen</div>
        <div class="fc-04__dept">Product & UX</div>
        <div class="fc-04__stat-row">
          <div class="fc-04__stat"><div class="fc-04__stat-num">120+</div><div class="fc-04__stat-lbl">Projects</div></div>
          <div class="fc-04__stat"><div class="fc-04__stat-num">6 yrs</div><div class="fc-04__stat-lbl">Experience</div></div>
          <div class="fc-04__stat"><div class="fc-04__stat-num">98%</div><div class="fc-04__stat-lbl">Rating</div></div>
        </div>
        <div class="fc-04__front-hint">Hover to connect →</div>
      </div>
      <div class="fc-04__back">
        <div class="fc-04__bio-title">About Aria</div>
        <div class="fc-04__bio">Aria leads design systems and cross-platform UX at NovaTech. She specialises in accessible, data-dense interfaces that scale from mobile to enterprise dashboards.</div>
        <div class="fc-04__social">
          <a class="fc-04__social-btn" href="#">𝕏 Twitter</a>
          <a class="fc-04__social-btn" href="#">in LinkedIn</a>
          <a class="fc-04__social-btn" href="#">⌥ Dribbble</a>
        </div>
        <a class="fc-04__contact" href="mailto:[email protected]">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 7L2 7"/></svg>
          [email protected]
        </a>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-04,
.fc-04 *,
.fc-04 *::before,
.fc-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-04 ::selection {
  background: #3b82f6;
  color: #fff;
}

.fc-04 {
  --bg: #08090f;
  --blue: #3b82f6;
  --cyan: #22d3ee;
  --white: #f8fafc;
  --card-w: 300px;
  --card-h: 400px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 60% 0%,#0c1a3a,#08090f 60%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--white);
}

.fc-04__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
  cursor: pointer;
}

.fc-04__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .85s cubic-bezier(.4,0,.2,1);
}
/* Scale-and-flip — card shrinks slightly, rotates, then settles to its
   resting size with a subtle bounce. Reads as "stepping forward to
   introduce themselves" rather than a mechanical spin. */

.fc-04__scene:hover .fc-04__card {
  animation: fc-04-scale-flip .85s cubic-bezier(.34,1.4,.5,1) forwards;
}

@keyframes fc-04-scale-flip {
  0% {
    transform: rotateY(0deg) scale(1);
  }

  40% {
    transform: rotateY(90deg) scale(.85);
  }

  70% {
    transform: rotateY(160deg) scale(.92);
  }

  100% {
    transform: rotateY(180deg) scale(1.03);
  }
}

.fc-04__front,
.fc-04__back {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT */

.fc-04__front {
  background: linear-gradient(160deg,#0d1b3e,#0a1220);
  border: 1px solid rgba(59,130,246,.2);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 36px 24px;
}

.fc-04__avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid rgba(59,130,246,.4);
  box-shadow: 0 0 30px rgba(59,130,246,.25);
  margin-bottom: 18px;
  background: linear-gradient(135deg,#1e3a8a,#1e40af);
  display: flex;
  align-items: center;
  justify-content: center;
}

.fc-04__role-badge {
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--cyan);
  font-weight: 700;
  margin-bottom: 6px;
}

.fc-04__member-name {
  font-size: 22px;
  font-weight: 800;
  color: var(--white);
  text-align: center;
}

.fc-04__dept {
  margin-top: 6px;
  font-size: 12px;
  color: rgba(248,250,252,.4);
  background: rgba(59,130,246,.1);
  border: 1px solid rgba(59,130,246,.2);
  padding: 3px 12px;
  border-radius: 20px;
}

.fc-04__stat-row {
  display: flex;
  gap: 24px;
  margin-top: 24px;
}

.fc-04__stat {
  text-align: center;
}

.fc-04__stat-num {
  font-size: 22px;
  font-weight: 800;
  background: linear-gradient(135deg,var(--blue),var(--cyan));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.fc-04__stat-lbl {
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: rgba(248,250,252,.35);
  margin-top: 2px;
}

.fc-04__front-hint {
  margin-top: auto;
  font-size: 10px;
  color: rgba(248,250,252,.25);
  letter-spacing: .08em;
}
/* BACK */

.fc-04__back {
  background: linear-gradient(160deg,#0d1117,#111827);
  border: 1px solid rgba(34,211,238,.2);
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  padding: 28px;
  gap: 16px;
}

.fc-04__bio-title {
  font-size: 11px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--cyan);
  font-weight: 700;
}

.fc-04__bio {
  font-size: 13px;
  color: rgba(248,250,252,.65);
  line-height: 1.7;
}

.fc-04__social {
  display: flex;
  gap: 12px;
  margin-top: 4px;
}

.fc-04__social-btn {
  flex: 1;
  padding: 10px 6px;
  border-radius: 10px;
  border: 1px solid rgba(255,255,255,.1);
  background: rgba(255,255,255,.04);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .06em;
  color: rgba(248,250,252,.7);
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  transition: background .2s,border-color .2s;
  display: block;
}

.fc-04__social-btn:hover {
  background: rgba(59,130,246,.15);
  border-color: rgba(59,130,246,.3);
  color: var(--blue);
}

.fc-04__contact {
  margin-top: auto;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  border-radius: 12px;
  background: linear-gradient(135deg,rgba(59,130,246,.15),rgba(34,211,238,.08));
  border: 1px solid rgba(59,130,246,.2);
  font-size: 12px;
  color: rgba(248,250,252,.7);
  text-decoration: none;
}

@media (prefers-reduced-motion: reduce) {
  .fc-04__card {
    transition: none;
  }
}
```
