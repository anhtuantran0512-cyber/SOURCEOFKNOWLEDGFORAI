---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/terminal-dev-hero/"
title: "Terminal Dev Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Vintage-CRT terminal hero — phosphor green text + amber prompt on a warm beige paper backdrop. The 1970s computing aesthetic for a modern dev tool."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Terminal Dev Hero
Source: https://codefronts.com/layouts/css-hero-sections/terminal-dev-hero/

Vintage-CRT terminal hero — phosphor green text + amber prompt on a warm beige paper backdrop. The 1970s computing aesthetic for a modern dev tool.
## HTML
```html
<section class="hs-05" aria-label="Hero">
  <div class="hs-05__copy">
    <h2>Ship from <em>your terminal.</em></h2>
    <p>
      One command. No dashboard. No yak shave. Your CI agrees with your local because they share an
      OS.
    </p>
    <a class="hs-05__cta" href="#install">Read the docs →</a>
  </div>
  <div class="hs-05__screen" aria-hidden="true">
    <div class="hs-05__line">
      <span class="hs-05__prompt">$</span> swift install <span class="hs-05__cursor"></span>
    </div>
    <div class="hs-05__line hs-05__out">→ resolving dependencies</div>
    <div class="hs-05__line hs-05__out">→ compiling 47 modules</div>
    <div class="hs-05__line hs-05__out">→ linking binary</div>
    <div class="hs-05__line hs-05__ok">✓ shipped in 2.3s</div>
    <div class="hs-05__line"><span class="hs-05__prompt">$</span> _</div>
  </div>
</section>
```
## CSS
```css
.hs-05 {
  display: grid;
  grid-template-columns: 1fr 1.05fr;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 64px) clamp(20px, 5vw, 56px);
  gap: clamp(24px, 4vw, 56px);
  align-items: center;
  background: repeating-linear-gradient(0deg, transparent 0 31px, rgba(50,30,10,0.04) 31px 32px), #f0e4cf;
  font-family: 'Inter', system-ui, sans-serif;
  color: #2a1d0a;
  box-sizing: border-box;
}

.hs-05 h2 {
  margin: 0 0 16px;
  font-family: 'JetBrains Mono', monospace;
  font-size: clamp(34px, 5vw, 54px);
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.05;
}

.hs-05 h2 em {
  color: #b8580c;
  font-style: normal;
}

.hs-05 h2 em::before {
  content: '> ';
  opacity: 0.6;
}

.hs-05 p {
  margin: 0 0 24px;
  font-size: 15.5px;
  line-height: 1.6;
  color: #5a4220;
  max-width: 440px;
}

.hs-05__cta {
  display: inline-block;
  padding: 12px 22px;
  background: #2a1d0a;
  color: #f0e4cf;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  font-size: 13.5px;
  text-decoration: none;
  border-radius: 0;
  transition: background 0.15s;
}

.hs-05__cta:hover {
  background: #b8580c;
}

.hs-05__screen {
  background: #0d1908;
  border: 2px solid #2a1d0a;
  border-radius: 8px;
  padding: 22px 24px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  line-height: 1.85;
  box-shadow: 0 0 0 8px rgba(13,25,8,0.1), 0 0 60px rgba(60,255,120,0.18) inset;
}

.hs-05__line {
  color: #5fff8c;
  text-shadow: 0 0 8px rgba(95,255,140,0.5);
}

.hs-05__prompt {
  color: #ffb348;
  text-shadow: 0 0 8px rgba(255,179,72,0.5);
  margin-right: 6px;
}

.hs-05__out {
  color: #88a890;
  opacity: 0.9;
  padding-left: 14px;
}

.hs-05__ok {
  color: #5fff8c;
  padding-left: 14px;
  font-weight: 700;
}

.hs-05__cursor {
  display: inline-block;
  width: 8px;
  height: 16px;
  background: #5fff8c;
  vertical-align: text-bottom;
  animation: hs-05-blink 1s steps(2) infinite;
}

@keyframes hs-05-blink {
  to {
    opacity: 0;
  }
}

@media (max-width: 720px) {
  .hs-05 {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hs-05__cursor {
    animation: none;
  }
}
```
