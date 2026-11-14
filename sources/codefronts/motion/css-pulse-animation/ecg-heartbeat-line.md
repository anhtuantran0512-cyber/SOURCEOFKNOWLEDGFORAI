---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/ecg-heartbeat-line/"
title: "ECG Heartbeat Line"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "A medical vitals monitor with an animated ECG heartbeat waveform sweeping left-to-right across a grid, matched to numeric vitals (HR, SpO2, BP, Resp) in a…"
has_js: "false"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: ECG Heartbeat Line
Source: https://codefronts.com/motion/css-pulse-animation/ecg-heartbeat-line/

A medical vitals monitor with an animated ECG heartbeat waveform sweeping left-to-right across a grid, matched to numeric vitals (HR, SpO2, BP, Resp) in a telehealth dashboard layout. Medical blue (#2563eb) + mint (#10b981) trace with clinical white surface (#ffffff) and grid graph background — Epic MyChart / Teladoc / Withings clinician-facing convention. Uses a pure-SVG animated stroke-dashoffset for the trace + a running dot marker.
## HTML
```html
<div class="pl-07">
  <div class="pl-07__monitor">
    <header class="pl-07__head">
      <div class="pl-07__patient">
        <span class="pl-07__id">Bed 12 · Room 402N</span>
        <strong>Chen, Marcus · 58M</strong>
      </div>
      <div class="pl-07__status">
        <span class="pl-07__status-dot" aria-label="Actively monitoring"></span>
        <span>Live monitoring</span>
        <span class="pl-07__time">14:22:08</span>
      </div>
    </header>

    <section class="pl-07__trace">
      <svg class="pl-07__ecg" viewBox="0 0 1000 200" preserveAspectRatio="none" aria-hidden="true">
        <defs>
          <linearGradient id="pl-07-grad" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#2563eb" stop-opacity="0"/>
            <stop offset="80%" stop-color="#2563eb" stop-opacity="1"/>
            <stop offset="100%" stop-color="#60a5fa" stop-opacity="1"/>
          </linearGradient>
        </defs>
        <!-- Ghost trace (persistent, low-opacity) -->
        <path class="pl-07__ecg-ghost"
              d="M0 100 L120 100 L140 100 Q160 90 170 100 L190 100 L200 100 L205 80 L210 100 L215 30 L220 170 L225 100 L235 100 L245 100 Q265 90 275 100 L300 100 L420 100 L440 100 Q460 90 470 100 L490 100 L500 100 L505 80 L510 100 L515 30 L520 170 L525 100 L535 100 L545 100 Q565 90 575 100 L600 100 L720 100 L740 100 Q760 90 770 100 L790 100 L800 100 L805 80 L810 100 L815 30 L820 170 L825 100 L835 100 L845 100 Q865 90 875 100 L1000 100"
              fill="none" stroke="#2563eb" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" opacity="0.14"/>
        <!-- Animated draw -->
        <path class="pl-07__ecg-line"
              d="M0 100 L120 100 L140 100 Q160 90 170 100 L190 100 L200 100 L205 80 L210 100 L215 30 L220 170 L225 100 L235 100 L245 100 Q265 90 275 100 L300 100 L420 100 L440 100 Q460 90 470 100 L490 100 L500 100 L505 80 L510 100 L515 30 L520 170 L525 100 L535 100 L545 100 Q565 90 575 100 L600 100 L720 100 L740 100 Q760 90 770 100 L790 100 L800 100 L805 80 L810 100 L815 30 L820 170 L825 100 L835 100 L845 100 Q865 90 875 100 L1000 100"
              fill="none" stroke="url(#pl-07-grad)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </section>

    <section class="pl-07__vitals" aria-live="polite">
      <div class="pl-07__vital">
        <div class="pl-07__vital-label">Heart rate</div>
        <div class="pl-07__vital-value pl-07__vital-value--blue">
          72<span>bpm</span>
        </div>
        <div class="pl-07__vital-note">Normal sinus rhythm</div>
      </div>
      <div class="pl-07__vital">
        <div class="pl-07__vital-label">SpO<sub>2</sub></div>
        <div class="pl-07__vital-value pl-07__vital-value--mint">
          98<span>%</span>
        </div>
        <div class="pl-07__vital-note">Room air</div>
      </div>
      <div class="pl-07__vital">
        <div class="pl-07__vital-label">Blood pressure</div>
        <div class="pl-07__vital-value pl-07__vital-value--ink">
          118<span>/</span>72
        </div>
        <div class="pl-07__vital-note">mmHg · Stable</div>
      </div>
      <div class="pl-07__vital">
        <div class="pl-07__vital-label">Respiratory</div>
        <div class="pl-07__vital-value pl-07__vital-value--ink">
          16<span>bpm</span>
        </div>
        <div class="pl-07__vital-note">Regular</div>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
.pl-07 {
  --page-bg: #f0f7fc;
  --surface: #ffffff;
  --ink: #0f172a;
  --sub: #64748b;
  --blue: #2563eb;
  --blue-soft: #dbeafe;
  --mint: #10b981;
  --line: #e0e7ee;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  padding: 32px;
  background: var(--page-bg);
  color: var(--ink);
}

.pl-07 *,
.pl-07 *::before,
.pl-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-07 ::selection {
  background: var(--blue);
  color: #fff;
}

.pl-07__monitor {
  width: min(820px,100%);
  padding: 0;
  border-radius: 14px;
  overflow: hidden;
  background: var(--surface);
  box-shadow: 0 20px 40px -20px rgba(15,23,42,.12),0 4px 12px -6px rgba(15,23,42,.08);
  border: 1px solid var(--line);
}

.pl-07__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 14px 20px;
  border-bottom: 1px solid var(--line);
  background: linear-gradient(180deg,#f8fafc 0%,var(--surface) 100%);
}

.pl-07__patient {
  display: flex;
  flex-direction: column;
}

.pl-07__id {
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sub);
}

.pl-07__patient strong {
  font-size: .95rem;
  font-weight: 700;
  color: var(--ink);
  letter-spacing: -.01em;
  margin-top: 1px;
}

.pl-07__status {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: .75rem;
  color: var(--sub);
}

.pl-07__status-dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--mint);
  animation: pl-07-heart 1s ease-in-out infinite;
}

@keyframes pl-07-heart {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  20% {
    transform: scale(1.3);
    opacity: 1;
  }

  40% {
    transform: scale(1);
    opacity: .7;
  }
}

.pl-07__time {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-weight: 600;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
  padding-left: 8px;
  border-left: 1px solid var(--line);
  margin-left: 4px;
}

.pl-07__trace {
  position: relative;
  height: 170px;
  background: repeating-linear-gradient(0deg,transparent 0 19px,rgba(37,99,235,.05) 19px 20px), repeating-linear-gradient(90deg,transparent 0 19px,rgba(37,99,235,.05) 19px 20px), #fbfdff;
  border-bottom: 1px solid var(--line);
  overflow: hidden;
}

.pl-07__ecg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.pl-07__ecg-line {
  stroke-dasharray: 2400;
  stroke-dashoffset: 2400;
  animation: pl-07-draw 4s linear infinite;
  filter: drop-shadow(0 0 4px rgba(37,99,235,.35));
}

@keyframes pl-07-draw {
  0% {
    stroke-dashoffset: 2400;
  }

  100% {
    stroke-dashoffset: 0;
  }
}

.pl-07__vitals {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 0;
}

@media (max-width: 640px) {
  .pl-07__vitals {
    grid-template-columns: repeat(2,1fr);
  }
}

.pl-07__vital {
  padding: 14px 18px;
  border-right: 1px solid var(--line);
}

.pl-07__vital:last-child {
  border-right: none;
}

.pl-07__vital-label {
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sub);
  margin-bottom: 6px;
}

.pl-07__vital-value {
  display: flex;
  align-items: baseline;
  gap: 2px;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 1.75rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  margin-bottom: 4px;
}

.pl-07__vital-value span {
  font-family: -apple-system,BlinkMacSystemFont,'Inter',sans-serif;
  font-size: .7rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: 0;
}

.pl-07__vital-value--blue {
  color: var(--blue);
}

.pl-07__vital-value--mint {
  color: var(--mint);
}

.pl-07__vital-value--ink {
  color: var(--ink);
}

.pl-07__vital-note {
  font-size: .68rem;
  color: var(--sub);
}

@media (prefers-reduced-motion: reduce) {
  .pl-07__ecg-line {
    animation: none!important;
    stroke-dashoffset: 0!important;
  }

  .pl-07__status-dot {
    animation: none!important;
    transform: none!important;
  }
}
```
