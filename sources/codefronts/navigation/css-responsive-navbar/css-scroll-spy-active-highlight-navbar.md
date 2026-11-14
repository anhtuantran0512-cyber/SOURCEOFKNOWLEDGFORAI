---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-scroll-spy-active-highlight-navbar/"
title: "CSS Scroll Spy Active Highlight Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "IntersectionObserver scroll spy that moves a springy pill indicator to the active section link with a reading progress bar."
has_js: "true"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Scroll Spy Active Highlight Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-scroll-spy-active-highlight-navbar/

IntersectionObserver scroll spy that moves a springy pill indicator to the active section link with a reading progress bar.
## HTML
```html
<div class="nav-20" id="nav20">
  <input type="checkbox" class="nav-20__toggle" id="nav-20-toggle">
  <div class="nav-20__bar">
    <a href="#" class="nav-20__logo">
      <div class="nav-20__logo-mark">✦</div>
      Prism
    </a>
    <ul class="nav-20__links" id="nav20Links">
      <div class="nav-20__indicator" id="nav20Indicator"></div>
      <li><a href="#sec-about" class="is-active"><span class="nav-20__dot"></span>About</a></li>
      <li><a href="#sec-work"><span class="nav-20__dot"></span>Work</a></li>
      <li><a href="#sec-services"><span class="nav-20__dot"></span>Services</a></li>
      <li><a href="#sec-team"><span class="nav-20__dot"></span>Team</a></li>
      <li><a href="#sec-contact"><span class="nav-20__dot"></span>Contact</a></li>
    </ul>
    <div class="nav-20__actions">
      <button class="nav-20__ghost">Log in</button>
      <button class="nav-20__cta">Get started →</button>
    </div>
    <label for="nav-20-toggle" class="nav-20__hamburger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </label>
  </div>
  <div class="nav-20__progress"><div class="nav-20__progress-fill" id="nav20Progress"></div></div>
  <div class="nav-20__mobile" id="nav20Mobile">
    <a href="#sec-about" class="is-active">About</a>
    <a href="#sec-work">Work</a>
    <a href="#sec-services">Services</a>
    <a href="#sec-team">Team</a>
    <a href="#sec-contact">Contact</a>
    <div class="nav-20__mobile-actions">
      <button class="m-ghost">Log in</button>
      <button class="m-cta">Get started →</button>
    </div>
  </div>
</div>

<!-- Page sections for scroll spy demo -->
<div style="max-width:720px; margin:0 auto; padding:2rem 2rem 6rem;">
  <section id="sec-about" style="padding:3.5rem 0 3rem; border-bottom:1px solid #e5e0d8;">
    <p style="font-size:0.75rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#b09050; margin-bottom:0.75rem;">About</p>
    <h2 style="font-size:2.4rem; font-weight:800; letter-spacing:-0.04em; color:#0d0d0d; margin-bottom:1rem; line-height:1.15;">Scroll down to watch<br>the navbar update</h2>
    <p style="color:#6b6560; font-size:1.05rem; line-height:1.75; max-width:560px;">As you scroll through sections below, the active link shifts with a springy pill indicator. A reading progress bar also tracks how far through the page you are.</p>
  </section>
  <section id="sec-work" style="padding:3.5rem 0 3rem; border-bottom:1px solid #e5e0d8;">
    <p style="font-size:0.75rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#b09050; margin-bottom:0.75rem;">Work</p>
    <h2 style="font-size:2rem; font-weight:800; letter-spacing:-0.04em; color:#0d0d0d; margin-bottom:1rem;">Selected projects</h2>
    <p style="color:#6b6560; font-size:1.05rem; line-height:1.75; max-width:560px;">The scroll spy uses IntersectionObserver to watch each section. When a section crosses the 25% threshold from the top, its matching nav link becomes active.</p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-top:2rem;">
      <div style="background:#0d0d0d; border-radius:12px; height:140px; display:grid; place-items:center; color:#f0c14b; font-weight:700; font-size:1.1rem;">Project A</div>
      <div style="background:#1a1a2e; border-radius:12px; height:140px; display:grid; place-items:center; color:#a78bfa; font-weight:700; font-size:1.1rem;">Project B</div>
    </div>
  </section>
  <section id="sec-services" style="padding:3.5rem 0 3rem; border-bottom:1px solid #e5e0d8;">
    <p style="font-size:0.75rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#b09050; margin-bottom:0.75rem;">Services</p>
    <h2 style="font-size:2rem; font-weight:800; letter-spacing:-0.04em; color:#0d0d0d; margin-bottom:1rem;">What we do</h2>
    <p style="color:#6b6560; font-size:1.05rem; line-height:1.75; max-width:560px;">The pill indicator moves with a springy CSS cubic-bezier bounce, giving it a physical feel without any animation libraries. Width transitions smoothly between links of different text lengths.</p>
    <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:0.75rem; margin-top:2rem;">
      <div style="background:#f0c14b18; border:1px solid #f0c14b40; border-radius:10px; padding:1.25rem; font-weight:600; color:#0d0d0d; font-size:0.9rem;">Strategy</div>
      <div style="background:#f0c14b18; border:1px solid #f0c14b40; border-radius:10px; padding:1.25rem; font-weight:600; color:#0d0d0d; font-size:0.9rem;">Design</div>
      <div style="background:#f0c14b18; border:1px solid #f0c14b40; border-radius:10px; padding:1.25rem; font-weight:600; color:#0d0d0d; font-size:0.9rem;">Build</div>
    </div>
  </section>
  <section id="sec-team" style="padding:3.5rem 0 3rem; border-bottom:1px solid #e5e0d8;">
    <p style="font-size:0.75rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#b09050; margin-bottom:0.75rem;">Team</p>
    <h2 style="font-size:2rem; font-weight:800; letter-spacing:-0.04em; color:#0d0d0d; margin-bottom:1rem;">Meet the crew</h2>
    <p style="color:#6b6560; font-size:1.05rem; line-height:1.75; max-width:560px;">Four people, one shared obsession: making software feel inevitable. We're small by design — it keeps us fast, honest, and close to the work.</p>
    <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:0.75rem; margin-top:2rem;">
      <div style="background:#f8f6f2; border:1px solid #e5e0d8; border-radius:10px; padding:1rem; text-align:center;">
        <div style="width:40px;height:40px;border-radius:50%;background:#0d0d0d;margin:0 auto 0.5rem;display:grid;place-items:center;color:#f0c14b;font-weight:800;">A</div>
        <div style="font-weight:600;font-size:0.8rem;color:#0d0d0d;">Alex</div>
        <div style="font-size:0.72rem;color:#9e9890;">Design</div>
      </div>
      <div style="background:#f8f6f2; border:1px solid #e5e0d8; border-radius:10px; padding:1rem; text-align:center;">
        <div style="width:40px;height:40px;border-radius:50%;background:#0d0d0d;margin:0 auto 0.5rem;display:grid;place-items:center;color:#f0c14b;font-weight:800;">J</div>
        <div style="font-weight:600;font-size:0.8rem;color:#0d0d0d;">Jamie</div>
        <div style="font-size:0.72rem;color:#9e9890;">Dev</div>
      </div>
      <div style="background:#f8f6f2; border:1px solid #e5e0d8; border-radius:10px; padding:1rem; text-align:center;">
        <div style="width:40px;height:40px;border-radius:50%;background:#0d0d0d;margin:0 auto 0.5rem;display:grid;place-items:center;color:#f0c14b;font-weight:800;">S</div>
        <div style="font-weight:600;font-size:0.8rem;color:#0d0d0d;">Sam</div>
        <div style="font-size:0.72rem;color:#9e9890;">Strategy</div>
      </div>
      <div style="background:#f8f6f2; border:1px solid #e5e0d8; border-radius:10px; padding:1rem; text-align:center;">
        <div style="width:40px;height:40px;border-radius:50%;background:#0d0d0d;margin:0 auto 0.5rem;display:grid;place-items:center;color:#f0c14b;font-weight:800;">R</div>
        <div style="font-weight:600;font-size:0.8rem;color:#0d0d0d;">Riley</div>
        <div style="font-size:0.72rem;color:#9e9890;">Growth</div>
      </div>
    </div>
  </section>
  <section id="sec-contact" style="padding:3.5rem 0 3rem;">
    <p style="font-size:0.75rem; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#b09050; margin-bottom:0.75rem;">Contact</p>
    <h2 style="font-size:2rem; font-weight:800; letter-spacing:-0.04em; color:#0d0d0d; margin-bottom:1rem;">Let's talk</h2>
    <p style="color:#6b6560; font-size:1.05rem; line-height:1.75; max-width:560px;">Scroll all the way here and the progress bar is full. The scroll spy updates both the desktop pill and mobile link states simultaneously from one observer loop.</p>
    <button style="margin-top:1.5rem; background:#0d0d0d; color:#f0c14b; border:none; border-radius:999px; padding:0 28px; height:46px; font-family:'Bricolage Grotesque',sans-serif; font-size:0.95rem; font-weight:700; cursor:pointer; letter-spacing:-0.01em;">Start a project →</button>
  </section>
</div>
```
## CSS
```css
.nav-20,
.nav-20 *,
.nav-20 *::before,
.nav-20 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-20 {
  --bg: #0d0d0d;
  --text: #e8e4dc;
  --text-muted: rgba(232,228,220,0.5);
  --accent: #f0c14b;
  --accent-bg: rgba(240,193,75,0.12);
  --pill-h: 38px;
  font-family: 'Bricolage Grotesque', sans-serif;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-20__bar {
  background: var(--bg);
  padding: 0 2rem;
  height: 62px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.nav-20__logo {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--text);
  font-weight: 800;
  font-size: 1.15rem;
  letter-spacing: -0.03em;
  flex-shrink: 0;
}

.nav-20__logo-mark {
  width: 30px;
  height: 30px;
  background: var(--accent);
  border-radius: 6px;
  display: grid;
  place-items: center;
  font-size: 14px;
  color: #0d0d0d;
}

.nav-20__links {
  display: flex;
  align-items: center;
  list-style: none;
  position: relative;
  gap: 2px;
}
/* The sliding highlight pill */

.nav-20__indicator {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  height: var(--pill-h);
  background: var(--accent-bg);
  border: 1px solid rgba(240,193,75,0.25);
  border-radius: 999px;
  transition: left 0.35s cubic-bezier(0.34,1.56,0.64,1), width 0.35s cubic-bezier(0.34,1.56,0.64,1);
  pointer-events: none;
  z-index: 0;
}

.nav-20__links li {
  position: relative;
  z-index: 1;
}

.nav-20__links a {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 500;
  padding: 0 14px;
  height: var(--pill-h);
  border-radius: 999px;
  transition: color 0.2s;
  white-space: nowrap;
  letter-spacing: -0.01em;
}

.nav-20__links a .nav-20__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent);
  opacity: 0;
  transform: scale(0);
  transition: opacity 0.25s, transform 0.25s;
}

.nav-20__links a.is-active {
  color: var(--accent);
}

.nav-20__links a.is-active .nav-20__dot {
  opacity: 1;
  transform: scale(1);
}

.nav-20__links a:hover:not(.is-active) {
  color: var(--text);
}

.nav-20__actions {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}

.nav-20__cta {
  background: var(--accent);
  color: #0d0d0d;
  border: none;
  border-radius: 999px;
  padding: 0 18px;
  height: 36px;
  font-family: inherit;
  font-size: 0.83rem;
  font-weight: 700;
  cursor: pointer;
  transition: opacity 0.2s, transform 0.15s;
  letter-spacing: -0.01em;
}

.nav-20__cta:hover {
  opacity: 0.88;
  transform: scale(1.03);
}

.nav-20__ghost {
  background: transparent;
  color: var(--text-muted);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 999px;
  padding: 0 16px;
  height: 36px;
  font-family: inherit;
  font-size: 0.83rem;
  font-weight: 500;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s;
  letter-spacing: -0.01em;
}

.nav-20__ghost:hover {
  border-color: rgba(255,255,255,0.3);
  color: var(--text);
}
/* Progress bar */

.nav-20__progress {
  height: 2px;
  background: rgba(255,255,255,0.05);
  position: relative;
  overflow: hidden;
}

.nav-20__progress-fill {
  height: 100%;
  width: 0%;
  background: var(--accent);
  transition: width 0.1s linear;
}
/* Mobile toggle */

.nav-20__toggle {
  display: none;
}

.nav-20__hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 6px;
}

.nav-20__hamburger span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s, width 0.3s;
  transform-origin: center;
}

.nav-20__toggle:checked ~ .nav-20__bar .nav-20__hamburger span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.nav-20__toggle:checked ~ .nav-20__bar .nav-20__hamburger span:nth-child(2) {
  opacity: 0;
  width: 0;
}

.nav-20__toggle:checked ~ .nav-20__bar .nav-20__hamburger span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

.nav-20__mobile {
  display: none;
  flex-direction: column;
  background: var(--bg);
  border-top: 1px solid rgba(255,255,255,0.06);
  padding: 0.75rem 1rem 1rem;
}

.nav-20__mobile a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.65rem 0.75rem;
  border-radius: 8px;
  transition: background 0.2s, color 0.2s;
}

.nav-20__mobile a:hover {
  background: rgba(255,255,255,0.05);
  color: var(--text);
}

.nav-20__mobile a.is-active {
  color: var(--accent);
}

.nav-20__mobile a.is-active::after {
  content: '●';
  font-size: 0.5rem;
}

.nav-20__mobile-actions {
  display: flex;
  gap: 8px;
  padding: 0.75rem 0.75rem 0;
  border-top: 1px solid rgba(255,255,255,0.06);
  margin-top: 0.5rem;
}

.nav-20__mobile-actions button {
  flex: 1;
  height: 38px;
  border-radius: 8px;
  font-family: inherit;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
}

.nav-20__mobile-actions .m-cta {
  background: var(--accent);
  color: #0d0d0d;
  border: none;
}

.nav-20__mobile-actions .m-ghost {
  background: transparent;
  color: var(--text-muted);
  border: 1px solid rgba(255,255,255,0.12);
}

.nav-20__toggle:checked ~ .nav-20__mobile {
  display: flex;
}

@media (max-width: 680px) {
  .nav-20__links,
    .nav-20__actions {
    display: none !important;
  }

  .nav-20__hamburger {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-20__indicator {
    transition: none;
  }

  .nav-20__links a,
    .nav-20__links a .nav-20__dot,
    .nav-20__cta,
    .nav-20__ghost,
    .nav-20__hamburger span,
    .nav-20__progress-fill {
    transition: none;
  }
}
```

## JavaScript
```js
const links = document.querySelectorAll('#nav20Links a');
  const mobileLinks = document.querySelectorAll('#nav20Mobile a:not(.m-ghost):not(.m-cta)');
  const indicator = document.getElementById('nav20Indicator');
  const linksContainer = document.getElementById('nav20Links');
  const progress = document.getElementById('nav20Progress');

  function moveIndicator(activeLink) {
    if (!activeLink || !indicator) return;
    const linkRect = activeLink.getBoundingClientRect();
    const containerRect = linksContainer.getBoundingClientRect();
    indicator.style.left = (linkRect.left - containerRect.left) + 'px';
    indicator.style.width = linkRect.width + 'px';
  }

  function setActive(sectionId) {
    links.forEach(function(a) {
      const active = a.getAttribute('href') === '#' + sectionId;
      a.classList.toggle('is-active', active);
      if (active) moveIndicator(a);
    });
    mobileLinks.forEach(function(a) {
      a.classList.toggle('is-active', a.getAttribute('href') === '#' + sectionId);
    });
  }

  // Scroll progress
  function updateProgress() {
    const scrollTop = window.scrollY;
    const docH = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docH > 0 ? Math.min(100, (scrollTop / docH) * 100) : 0;
    progress.style.width = pct + '%';
  }

  // IntersectionObserver scroll spy
  const sections = document.querySelectorAll('#sec-about, #sec-work, #sec-services, #sec-team, #sec-contact');
  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) setActive(entry.target.id);
    });
  }, { rootMargin: '-25% 0px -60% 0px', threshold: 0 });

  sections.forEach(function(s) { observer.observe(s); });
  window.addEventListener('scroll', updateProgress, { passive: true });

  // Init indicator on first active link
  const firstActive = linksContainer ? linksContainer.querySelector('a.is-active') : null;
  if (firstActive) setTimeout(function() { moveIndicator(firstActive); }, 50);
  window.addEventListener('resize', function() {
    const cur = linksContainer ? linksContainer.querySelector('a.is-active') : null;
    if (cur) moveIndicator(cur);
  });
```
