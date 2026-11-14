---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/recording-indicator/"
title: "Recording Indicator"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "A screen-recorder UI mockup with an active recording dot — pulsing red camera indicator + running timer + recording controls (pause / stop / mic / camera)."
has_js: "false"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Recording Indicator
Source: https://codefronts.com/motion/css-pulse-animation/recording-indicator/

A screen-recorder UI mockup with an active recording dot — pulsing red camera indicator + running timer + recording controls (pause / stop / mic / camera). Loom / Riverside / Zoom recording aesthetic with cool-gray (#f1f5f9) surface, deep slate ink (#0f172a), and red (#dc2626) recording state. The dot uses a subtle opacity pulse (not scale) because recording indicators must NEVER feel frivolous — this is a data-capture context where users need to trust the app is genuinely recording.
## HTML
```html
<div class="pl-09">
  <div class="pl-09__preview">
    <div class="pl-09__preview-frame">
      <div class="pl-09__preview-topbar">
        <span class="pl-09__preview-dot"></span>
        <span class="pl-09__preview-dot"></span>
        <span class="pl-09__preview-dot"></span>
        <span class="pl-09__preview-url">codefronts.com/motion/css-pulse-animation</span>
      </div>
      <div class="pl-09__preview-content">
        <div class="pl-09__preview-block pl-09__preview-block--wide"></div>
        <div class="pl-09__preview-block pl-09__preview-block--mid"></div>
        <div class="pl-09__preview-block pl-09__preview-block--wide"></div>
        <div class="pl-09__preview-block pl-09__preview-block--short"></div>
        <div class="pl-09__preview-row">
          <span class="pl-09__preview-card"></span>
          <span class="pl-09__preview-card"></span>
          <span class="pl-09__preview-card"></span>
        </div>
      </div>
      <div class="pl-09__preview-cursor" aria-hidden="true"></div>
    </div>
  </div>
  <div class="pl-09__toolbar">
    <div class="pl-09__rec">
      <span class="pl-09__rec-dot" aria-label="Recording in progress"></span>
      <span class="pl-09__rec-time" aria-live="polite">00:04:22</span>
      <span class="pl-09__rec-label">REC</span>
    </div>
    <div class="pl-09__divider" aria-hidden="true"></div>
    <div class="pl-09__controls">
      <button class="pl-09__ctrl" aria-label="Pause recording">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true">
          <rect x="6" y="5" width="4" height="14" rx="1"/>
          <rect x="14" y="5" width="4" height="14" rx="1"/>
        </svg>
      </button>
      <button class="pl-09__ctrl pl-09__ctrl--stop" aria-label="Stop recording">
        <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor" aria-hidden="true">
          <rect x="6" y="6" width="12" height="12" rx="1.5"/>
        </svg>
      </button>
      <button class="pl-09__ctrl pl-09__ctrl--toggle pl-09__ctrl--on" aria-label="Microphone on" aria-pressed="true">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
          <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
          <line x1="12" y1="19" x2="12" y2="23"/>
          <line x1="8" y1="23" x2="16" y2="23"/>
        </svg>
      </button>
      <button class="pl-09__ctrl pl-09__ctrl--toggle" aria-label="Camera off" aria-pressed="false">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M23 7l-7 5 7 5V7z"/>
          <rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>
        </svg>
      </button>
    </div>
  </div>
</div>
```
## CSS
```css
.pl-09 {
  --page-bg: #f1f5f9;
  --surface: #ffffff;
  --ink: #0f172a;
  --sub: #64748b;
  --red: #dc2626;
  --red-dim: rgba(220,38,38,.5);
  --line: #e2e8f0;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: grid;
  grid-template-rows: 1fr auto;
  gap: 20px;
  padding: 32px;
  background: var(--page-bg);
  color: var(--ink);
}

.pl-09 *,
.pl-09 *::before,
.pl-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-09 ::selection {
  background: var(--red);
  color: #fff;
}

.pl-09__preview {
  display: grid;
  place-items: center;
  min-height: 0;
}

.pl-09__preview-frame {
  position: relative;
  width: min(720px,100%);
  aspect-ratio: 16/9;
  border-radius: 10px;
  overflow: hidden;
  background: linear-gradient(180deg,#e2e8f0 0%,#cbd5e1 100%);
  box-shadow: 0 20px 40px -20px rgba(15,23,42,.25);
  border: 1px solid var(--line);
}

.pl-09__preview-topbar {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  background: #cbd5e1;
  border-bottom: 1px solid #94a3b8;
}

.pl-09__preview-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #94a3b8;
}

.pl-09__preview-url {
  margin-left: 14px;
  padding: 3px 12px;
  border-radius: 5px;
  background: #e2e8f0;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .68rem;
  color: #475569;
}

.pl-09__preview-content {
  padding: 22px 32px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: #f8fafc;
}

.pl-09__preview-block {
  height: 14px;
  border-radius: 4px;
  background: linear-gradient(90deg,#e2e8f0 0%,#cbd5e1 50%,#e2e8f0 100%);
}

.pl-09__preview-block--wide {
  width: 75%;
}

.pl-09__preview-block--mid {
  width: 50%;
}

.pl-09__preview-block--short {
  width: 35%;
}

.pl-09__preview-row {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 10px;
  margin-top: 6px;
}

.pl-09__preview-card {
  height: 56px;
  border-radius: 6px;
  background: linear-gradient(180deg,#e2e8f0 0%,#f8fafc 100%);
  border: 1px solid #cbd5e1;
}

.pl-09__preview-cursor {
  position: absolute;
  top: 52%;
  left: 58%;
  width: 14px;
  height: 20px;
  background: var(--ink);
  clip-path: polygon(0 0, 100% 40%, 40% 55%, 60% 90%, 40% 100%, 0 55%);
  filter: drop-shadow(0 1px 2px rgba(0,0,0,.3));
}

.pl-09__toolbar {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 12px 20px;
  border-radius: 12px;
  background: var(--surface);
  box-shadow: 0 12px 32px -12px rgba(15,23,42,.2),0 4px 12px -6px rgba(15,23,42,.08);
  border: 1px solid var(--line);
  align-self: end;
  justify-self: center;
}

.pl-09__rec {
  display: flex;
  align-items: center;
  gap: 8px;
}
/* Recording dot — DELIBERATELY MUTED opacity pulse, no scale, no glow */

.pl-09__rec-dot {
  display: inline-block;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--red);
  animation: pl-09-rec 1s ease-in-out infinite;
}

@keyframes pl-09-rec {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .35;
  }
}

.pl-09__rec-time {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .95rem;
  font-weight: 700;
  letter-spacing: .02em;
  font-variant-numeric: tabular-nums;
  color: var(--ink);
}

.pl-09__rec-label {
  padding: 3px 7px;
  border-radius: 4px;
  background: var(--red);
  color: #fff;
  font-size: .62rem;
  font-weight: 800;
  letter-spacing: .1em;
}

.pl-09__divider {
  width: 1px;
  height: 24px;
  background: var(--line);
}

.pl-09__controls {
  display: flex;
  align-items: center;
  gap: 6px;
}

.pl-09__ctrl {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: var(--sub);
  cursor: pointer;
  transition: background .15s ease,color .15s ease;
}

.pl-09__ctrl:hover {
  background: #f1f5f9;
  color: var(--ink);
}

.pl-09__ctrl:focus-visible {
  outline: 2px solid var(--red);
  outline-offset: 2px;
}

.pl-09__ctrl--stop {
  background: #fef2f2;
  color: var(--red);
}

.pl-09__ctrl--stop:hover {
  background: #fee2e2;
  color: var(--red);
}

.pl-09__ctrl--toggle {
  position: relative;
}

.pl-09__ctrl--on {
  color: var(--ink);
  background: #f1f5f9;
}

@media (prefers-reduced-motion: reduce) {
  .pl-09__rec-dot {
    animation: none!important;
    opacity: 1!important;
  }
}
```
