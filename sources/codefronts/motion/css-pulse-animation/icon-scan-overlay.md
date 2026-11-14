---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/icon-scan-overlay/"
title: "Icon Scan Overlay"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "A security-scanner HUD showing an active malware / virus scan in progress — a shield icon at the center with rapid concentric green rings firing outward,…"
has_js: "false"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Icon Scan Overlay
Source: https://codefronts.com/motion/css-pulse-animation/icon-scan-overlay/

A security-scanner HUD showing an active malware / virus scan in progress — a shield icon at the center with rapid concentric green rings firing outward, matched to a scan progress bar and file-processing terminal output. Terminal-black surface (#000000) with toxic-green scan color (#22c55e) and JetBrains Mono uppercase labels. Malwarebytes / Kaspersky / Norton / Trellix scan-in-progress aesthetic — dev-culture technical, not consumer-friendly.
## HTML
```html
<div class="pl-16">
  <header class="pl-16__head">
    <div class="pl-16__brand">
      <span class="pl-16__logo" aria-hidden="true">◉</span>
      <span>trellixguard</span>
    </div>
    <div class="pl-16__meta">
      <span class="pl-16__meta-item">MODE: <strong>DEEP</strong></span>
      <span class="pl-16__meta-divider">·</span>
      <span class="pl-16__meta-item">RUNTIME: <strong>00:04:22</strong></span>
    </div>
  </header>
  <main class="pl-16__stage">
    <div class="pl-16__scanner" role="img" aria-label="Scan in progress: 14,247 files scanned, 0 threats detected">
      <div class="pl-16__grid" aria-hidden="true"></div>
      <div class="pl-16__shield">
        <svg viewBox="0 0 24 24" width="42" height="42" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          <path d="M9 12l2 2 4-4"/>
        </svg>
      </div>
    </div>
    <div class="pl-16__stats">
      <div class="pl-16__stat">
        <span class="pl-16__stat-label">SCANNED</span>
        <span class="pl-16__stat-value">14,247</span>
      </div>
      <div class="pl-16__stat">
        <span class="pl-16__stat-label">THREATS</span>
        <span class="pl-16__stat-value pl-16__stat-value--ok">0</span>
      </div>
      <div class="pl-16__stat">
        <span class="pl-16__stat-label">STATUS</span>
        <span class="pl-16__stat-value pl-16__stat-value--ok">CLEAN</span>
      </div>
    </div>
    <div class="pl-16__terminal" role="log" aria-live="polite">
      <p>&gt; scanning /usr/local/bin/node <span class="pl-16__ok">OK</span></p>
      <p>&gt; scanning /Applications/Chrome.app/… <span class="pl-16__ok">OK</span></p>
      <p>&gt; scanning /path/to/downloads/… <span class="pl-16__ok">OK</span></p>
      <p>&gt; analyzing memory region 0x7fff5b3c… <span class="pl-16__cursor" aria-hidden="true"></span></p>
    </div>
  </main>
</div>
```
## CSS
```css
.pl-16 {
  --bg: #000000;
  --surface: #0a0a0a;
  --ink: #dcfce7;
  --sub: #4ade80;
  --muted: #166534;
  --green: #22c55e;
  --green-glow: rgba(34,197,94,.5);
  --line: rgba(34,197,94,.14);
  font-family: 'JetBrains Mono',ui-monospace,'Menlo','Consolas',monospace;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 16px;
  padding: 24px;
  background: radial-gradient(50% 70% at 50% 50%, rgba(34,197,94,.14) 0%, transparent 65%), var(--bg);
  color: var(--ink);
}

.pl-16 *,
.pl-16 *::before,
.pl-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-16 ::selection {
  background: var(--green);
  color: var(--bg);
}

.pl-16__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 16px;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: rgba(34,197,94,.04);
}

.pl-16__brand {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: .78rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.pl-16__logo {
  color: var(--green);
  font-size: .9rem;
}

.pl-16__meta {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: .7rem;
  color: var(--sub);
  letter-spacing: .06em;
}

.pl-16__meta strong {
  color: var(--ink);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  margin-left: 4px;
}

.pl-16__meta-divider {
  color: var(--muted);
}

.pl-16__stage {
  display: grid;
  grid-template-rows: 1fr auto auto;
  gap: 16px;
  padding: 20px;
  border-radius: 8px;
  background: var(--surface);
  border: 1px solid var(--line);
  min-height: 0;
}

.pl-16__scanner {
  position: relative;
  aspect-ratio: 16/6;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  border-radius: 6px;
  background: #050505;
}

.pl-16__grid {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg,transparent 0 19px,rgba(34,197,94,.06) 19px 20px), repeating-linear-gradient(90deg,transparent 0 19px,rgba(34,197,94,.06) 19px 20px);
  pointer-events: none;
}

.pl-16__shield {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 70px;
  height: 70px;
  border-radius: 50%;
  background: rgba(34,197,94,.14);
  color: var(--green);
  z-index: 1;
}
/* Concentric outward rings — rapid 3-ring scan cascade */

.pl-16__shield::before,
.pl-16__shield::after,
.pl-16__scanner::after {
  content: '';
  position: absolute;
  width: 70px;
  height: 70px;
  border-radius: 50%;
  border: 2px solid var(--green-glow);
  pointer-events: none;
  animation: pl-16-scan 1.2s ease-out infinite;
}

.pl-16__scanner::after {
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  animation-delay: .4s;
}

.pl-16__shield::before {
  animation-delay: 0s;
}

.pl-16__shield::after {
  animation-delay: .8s;
}

@keyframes pl-16-scan {
  0% {
    transform: translate(-50%,-50%) scale(1);
    opacity: .7;
  }

  70% {
    transform: translate(-50%,-50%) scale(2.5);
    opacity: 0;
  }

  100% {
    transform: translate(-50%,-50%) scale(2.6);
    opacity: 0;
  }
}
/* Fix: transform for shield's own pseudo-elements (positioned inset) */

.pl-16__shield::before,
.pl-16__shield::after {
  top: 0;
  left: 0;
  transform: scale(1);
  animation: pl-16-scan-shield 1.2s ease-out infinite;
}

.pl-16__shield::before {
  animation-delay: 0s;
}

.pl-16__shield::after {
  animation-delay: .8s;
}

@keyframes pl-16-scan-shield {
  0% {
    transform: scale(1);
    opacity: .7;
  }

  70% {
    transform: scale(2.5);
    opacity: 0;
  }

  100% {
    transform: scale(2.6);
    opacity: 0;
  }
}

.pl-16__stats {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 10px;
}

.pl-16__stat {
  padding: 10px 14px;
  border: 1px solid var(--line);
  border-radius: 5px;
  background: rgba(0,0,0,.3);
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.pl-16__stat-label {
  font-size: .6rem;
  font-weight: 700;
  letter-spacing: .14em;
  color: var(--muted);
}

.pl-16__stat-value {
  font-size: 1.05rem;
  font-weight: 800;
  letter-spacing: -.01em;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.pl-16__stat-value--ok {
  color: var(--green);
}

.pl-16__terminal {
  padding: 12px 14px;
  border-radius: 5px;
  background: rgba(0,0,0,.4);
  border: 1px solid var(--line);
  font-size: .72rem;
  line-height: 1.6;
  color: var(--sub);
  max-height: 120px;
  overflow: hidden;
}

.pl-16__terminal p {
  margin-bottom: 2px;
}

.pl-16__ok {
  color: var(--green);
  font-weight: 800;
  margin-left: 8px;
}

.pl-16__cursor {
  display: inline-block;
  width: 7px;
  height: 11px;
  background: var(--green);
  margin-left: 3px;
  vertical-align: middle;
  animation: pl-16-cursor 1s steps(2) infinite;
}

@keyframes pl-16-cursor {
  0%,
    50% {
    opacity: 1;
  }

  51%,
    100% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pl-16__shield::before,
    .pl-16__shield::after,
    .pl-16__cursor {
    animation: none!important;
  }

  .pl-16__shield::before,
    .pl-16__shield::after {
    opacity: 0!important;
  }
}
```
