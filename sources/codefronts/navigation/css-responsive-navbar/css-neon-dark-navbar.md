---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-neon-dark-navbar/"
title: "CSS Neon Dark Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "High-contrast dark navbar with neon-glow text effects, glowing CTA button, and animated pulse indicator dot."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Neon Dark Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-neon-dark-navbar/

High-contrast dark navbar with neon-glow text effects, glowing CTA button, and animated pulse indicator dot.
## HTML
```html
<div class="nav-07">
  <input type="checkbox" id="nav-07-toggle">
  <div class="nav-07__inner">
    <a href="#" class="nav-07__logo">NEXUS</a>
    <ul class="nav-07__links">
      <li><a href="#" class="is-active">System</a></li>
      <li><a href="#">Networks</a></li>
      <li><a href="#">Data</a></li>
      <li><a href="#">Security</a></li>
      <li><a href="#">Console</a></li>
    </ul>
    <div class="nav-07__status">ONLINE</div>
    <button class="nav-07__btn">Connect</button>
    <label for="nav-07-toggle" class="nav-07__hamburger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </label>
  </div>
  <div class="nav-07__mobile">
    <a href="#">System</a><a href="#">Networks</a><a href="#">Data</a><a href="#">Security</a><a href="#">Console</a>
  </div>
</div>
<div style="padding:4rem 2rem; color:#e0e8ff; max-width:700px; margin:0 auto;">
  <h1 style="font-family:'Orbitron',monospace; font-size:2.5rem; font-weight:900; letter-spacing:0.05em; margin-bottom:1rem; background:linear-gradient(90deg,#00f5ff,#ff00cc); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">Neon Dark Navbar</h1>
  <p style="color:rgba(224,232,255,0.55); font-size:1rem; line-height:1.7; font-family:'DM Sans',sans-serif;">Hover the nav links to see the neon underline slide in. The glowing status dot uses a CSS keyframe. All glow effects are achieved with <code>box-shadow</code> and <code>filter: drop-shadow</code>.</p>
</div>
```
## CSS
```css
.nav-07,
.nav-07 *,
.nav-07 *::before,
.nav-07 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-07 {
  --bg: #0a0a1a;
  --border: rgba(0,245,255,0.2);
  --text: #e0e8ff;
  --muted: rgba(224,232,255,0.45);
  --cyan: #00f5ff;
  --magenta: #ff00cc;
  --green: #00ff88;
  font-family: 'Orbitron', monospace;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 0 40px rgba(0,245,255,0.05), 0 1px 0 rgba(0,245,255,0.15);
}

.nav-07__inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  height: 64px;
  gap: 2rem;
}

.nav-07__logo {
  font-weight: 900;
  font-size: 1.1rem;
  text-decoration: none;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  background: linear-gradient(90deg, var(--cyan), var(--magenta));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 8px rgba(0,245,255,0.5));
  flex-shrink: 0;
  transition: filter 0.3s;
}

.nav-07__logo:hover {
  filter: drop-shadow(0 0 16px rgba(0,245,255,0.9));
}

.nav-07__links {
  display: flex;
  list-style: none;
  gap: 0;
  flex: 1;
}

.nav-07__links a {
  display: block;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  position: relative;
  transition: color 0.25s;
}

.nav-07__links a::before {
  content: '';
  position: absolute;
  bottom: 6px;
  left: 50%;
  right: 50%;
  height: 1px;
  background: var(--cyan);
  box-shadow: 0 0 6px var(--cyan), 0 0 12px var(--cyan);
  transition: left 0.25s, right 0.25s;
}

.nav-07__links a:hover {
  color: var(--cyan);
}

.nav-07__links a:hover::before {
  left: 1rem;
  right: 1rem;
}

.nav-07__links a.is-active {
  color: var(--cyan);
}

.nav-07__links a.is-active::before {
  left: 1rem;
  right: 1rem;
}

.nav-07__status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.65rem;
  letter-spacing: 0.1em;
  color: var(--green);
  border: 1px solid rgba(0,255,136,0.3);
  padding: 0.3rem 0.75rem;
  border-radius: 4px;
  background: rgba(0,255,136,0.05);
  flex-shrink: 0;
}

.nav-07__status::before {
  content: '';
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--green);
  box-shadow: 0 0 6px var(--green), 0 0 12px var(--green);
  animation: nav-07-pulse 2s ease-in-out infinite;
}

@keyframes nav-07-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.3;
  }
}

.nav-07__btn {
  padding: 0.45rem 1.3rem;
  border: 1px solid var(--cyan);
  border-radius: 4px;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  font-family: inherit;
  background: transparent;
  color: var(--cyan);
  box-shadow: 0 0 8px rgba(0,245,255,0.2), inset 0 0 8px rgba(0,245,255,0.05);
  transition: box-shadow 0.25s, background 0.25s, color 0.25s;
  flex-shrink: 0;
}

.nav-07__btn:hover {
  background: rgba(0,245,255,0.1);
  box-shadow: 0 0 20px rgba(0,245,255,0.5), inset 0 0 20px rgba(0,245,255,0.1);
  color: #fff;
}
/* Mobile */

#nav-07-toggle {
  display: none;
}

.nav-07__hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 8px;
  border: none;
  background: transparent;
  margin-left: auto;
}

.nav-07__hamburger span {
  display: block;
  width: 22px;
  height: 1.5px;
  background: var(--cyan);
  box-shadow: 0 0 4px var(--cyan);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

#nav-07-toggle:checked ~ .nav-07__inner .nav-07__hamburger span:nth-child(1) {
  transform: translateY(6.5px) rotate(45deg);
}

#nav-07-toggle:checked ~ .nav-07__inner .nav-07__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-07-toggle:checked ~ .nav-07__inner .nav-07__hamburger span:nth-child(3) {
  transform: translateY(-6.5px) rotate(-45deg);
}

.nav-07__mobile {
  display: none;
  flex-direction: column;
  gap: 0.25rem;
  background: #0a0a1a;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid rgba(0,245,255,0.15);
}

.nav-07__mobile a {
  display: block;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0.65rem 0.5rem;
  border-bottom: 1px solid rgba(0,245,255,0.08);
  transition: color 0.2s, padding-left 0.2s;
}

.nav-07__mobile a:last-child {
  border-bottom: none;
}

.nav-07__mobile a:hover {
  color: var(--cyan);
  padding-left: 1rem;
}

#nav-07-toggle:checked ~ .nav-07__mobile {
  display: flex;
}

@media (max-width: 768px) {
  .nav-07__links,
    .nav-07__status,
    .nav-07__btn {
    display: none;
  }

  .nav-07__hamburger {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-07__status::before {
    animation: none;
  }

  .nav-07__links a::before,
    .nav-07__logo,
    .nav-07__btn {
    transition: none;
  }

  .nav-07__hamburger span {
    transition: none;
  }
}
```
