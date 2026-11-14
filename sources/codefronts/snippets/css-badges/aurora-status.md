---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/aurora-status/"
title: "Aurora Status"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Status pill that breathes."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Status
Source: https://codefronts.com/snippets/css-badges/aurora-status/

Status pill that breathes. Four pools of color drift behind a frosted lens; their hues rotate continuously through the spectrum. For loading, streaming, thinking — when text alone is not enough.
## HTML
```html
<div class="bdg-21-stage">
  <div class="bdg-21-stars"></div>
  <div class="bdg-21-badge">
    <div class="bdg-21-bg"></div>
    <span class="bdg-21-spinner">
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="12" r="9" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
        <circle cx="12" cy="12" r="9" fill="none" stroke="white" stroke-width="2" stroke-dasharray="14 42" stroke-linecap="round"/>
      </svg>
    </span>
    <div class="bdg-21-text">
      <div class="bdg-21-label">Synthesizing</div>
      <div class="bdg-21-detail">Drafting response · 73%</div>
    </div>
  </div>
  <div class="bdg-21-caption">animation runs continuously — no hover required</div>
</div>
```
## CSS
```css
.bdg-21-stage {
  background: radial-gradient(ellipse at center, #0a1438 0%, #04081e 80%);
  padding: 80px 40px;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 28px;
  position: relative;
}

.bdg-21-stars {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(1px 1px at 20% 30%, white, transparent), radial-gradient(1px 1px at 60% 70%, white, transparent), radial-gradient(1px 1px at 80% 10%, white, transparent), radial-gradient(1px 1px at 90% 60%, white, transparent), radial-gradient(1px 1px at 10% 90%, white, transparent), radial-gradient(1px 1px at 50% 20%, white, transparent), radial-gradient(1px 1px at 30% 65%, white, transparent), radial-gradient(1.5px 1.5px at 75% 40%, white, transparent), radial-gradient(1px 1px at 40% 85%, white, transparent), radial-gradient(1.5px 1.5px at 15% 50%, white, transparent), radial-gradient(1.5px 1.5px at 85% 80%, white, transparent);
  opacity: 0.65;
  pointer-events: none;
}

.bdg-21-stars::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 25% 70%, rgba(120, 200, 255, 0.08), transparent 60%), radial-gradient(circle at 75% 30%, rgba(180, 120, 255, 0.08), transparent 60%);
}

.bdg-21-badge {
  display: inline-flex;
  align-items: center;
  gap: 16px;
  padding: 18px 32px;
  border-radius: 999px;
  background: rgba(8, 12, 32, 0.55);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.16);
  position: relative;
  overflow: hidden;
  isolation: isolate;
  box-shadow: 0 20px 60px -10px rgba(0,0,0,0.65), inset 0 1px 0 rgba(255,255,255,0.12);
  z-index: 1;
}

.bdg-21-bg {
  position: absolute;
  inset: -60%;
  z-index: -1;
  background: radial-gradient(circle at 20% 50%, #00ffaa 0%, transparent 38%), radial-gradient(circle at 70% 30%, #b04dff 0%, transparent 50%), radial-gradient(circle at 50% 80%, #00aaff 0%, transparent 45%), radial-gradient(circle at 90% 70%, #ff44aa 0%, transparent 40%);
  filter: blur(38px);
  animation: bdg-21-drift 11s ease-in-out infinite, bdg-21-hue 16s linear infinite;
}

@keyframes bdg-21-drift {
  0%,
    100% {
    transform: translate(0, 0) scale(1) rotate(0deg);
  }

  25% {
    transform: translate(7%, -5%) scale(1.08) rotate(18deg);
  }

  50% {
    transform: translate(-4%, 8%) scale(0.96) rotate(-12deg);
  }

  75% {
    transform: translate(5%, 5%) scale(1.04) rotate(8deg);
  }
}

@keyframes bdg-21-hue {
  to {
    filter: blur(38px) hue-rotate(360deg);
  }
}

@keyframes bdg-21-spin {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-21-bg,
    .bdg-21-spinner {
    animation: none;
  }
}

.bdg-21-spinner {
  width: 28px;
  height: 28px;
  animation: bdg-21-spin 1.6s linear infinite;
  position: relative;
  z-index: 1;
}

.bdg-21-spinner svg {
  width: 100%;
  height: 100%;
  display: block;
}

.bdg-21-text {
  text-align: left;
  position: relative;
  z-index: 1;
}

.bdg-21-label {
  font-family: "Italiana", Georgia, serif;
  font-size: 22px;
  letter-spacing: 0.04em;
  color: #fff;
  line-height: 1;
  margin-bottom: 3px;
}

.bdg-21-detail {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 10px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.72);
}

.bdg-21-caption {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 10px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.32);
  position: relative;
  z-index: 1;
}
```
