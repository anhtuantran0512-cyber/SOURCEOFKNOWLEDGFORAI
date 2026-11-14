---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/modular-synth-controls/"
title: "Extruded Synth Panel with Draggable Faders"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "A mixer panel that reads as machined hardware while staying perfectly face on: depth comes from stacked translateZ plates and a shadow ladder, not rotation."
has_js: "true"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Extruded Synth Panel with Draggable Faders
Source: https://codefronts.com/design-styles/css-3d/modular-synth-controls/

A mixer panel that reads as machined hardware while staying perfectly face on: depth comes from stacked translateZ plates and a shadow ladder, not rotation. Six faders are built from data and draggable, two VU meters run a twelve-segment LED ladder, and the transport buttons and routing switches drive a shared readout &mdash; so every control is a real button with real state.
## HTML
```html
<section class="d3-17" aria-label="Modular synth control panel demo">

  <div class="d3-17__theme">
    <input class="d3-17__theme-input" type="checkbox" id="d3-17-theme">
    <label class="d3-17__theme-label" for="d3-17-theme" aria-label="Toggle light and dark theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 1 0 17z" fill="currentColor"/></svg>
    </label>
  </div>

  <div class="card">
    <div class="panel">

      <div class="readout">
        <div class="readout-item">
          <div class="readout-key">Mode</div>
          <div class="readout-val" data-d3-17-mode>STUDIO</div>
        </div>
        <div class="readout-item">
          <div class="readout-key">Master</div>
          <div class="readout-val" data-d3-17-master>87</div>
        </div>
        <div class="readout-item">
          <div class="readout-key">BPM</div>
          <div class="readout-val" data-d3-17-bpm>124</div>
        </div>
        <div class="readout-item">
          <div class="readout-key">Status</div>
          <div class="readout-val live">LIVE</div>
        </div>
      </div>

      <div class="main-layout">
        <div class="left-controls">

          <div class="section">
            <div class="section-label">Transport</div>
            <div class="btn-row">
              <button class="push-btn" type="button" data-action="play">
                <span class="push-btn-body"><span class="btn-led"></span><span class="push-btn-label">Play</span></span>
              </button>
              <button class="push-btn active" type="button" data-action="rec">
                <span class="push-btn-body"><span class="btn-led"></span><span class="push-btn-label">Rec</span></span>
              </button>
              <button class="push-btn" type="button" data-action="stop">
                <span class="push-btn-body"><span class="btn-led"></span><span class="push-btn-label">Stop</span></span>
              </button>
              <button class="push-btn active" type="button" data-action="loop">
                <span class="push-btn-body"><span class="btn-led"></span><span class="push-btn-label">Loop</span></span>
              </button>
              <button class="push-btn" type="button" data-action="fx">
                <span class="push-btn-body"><span class="btn-led"></span><span class="push-btn-label">FX</span></span>
              </button>
            </div>
          </div>

          <div class="section">
            <div class="section-label">Routing</div>
            <div class="toggle-row">
              <div class="toggle-unit">
                <button class="toggle-sw on" type="button" data-toggle="mono">
                  <span class="toggle-thumb"></span>
                  <span class="toggle-sw-led"></span>
                </button>
                <span class="toggle-label">Mono</span>
              </div>
              <div class="toggle-unit">
                <button class="toggle-sw" type="button" data-toggle="reverb">
                  <span class="toggle-thumb"></span>
                  <span class="toggle-sw-led"></span>
                </button>
                <span class="toggle-label">Reverb</span>
              </div>
              <div class="toggle-unit">
                <button class="toggle-sw on" type="button" data-toggle="eq">
                  <span class="toggle-thumb"></span>
                  <span class="toggle-sw-led"></span>
                </button>
                <span class="toggle-label">EQ</span>
              </div>
              <div class="toggle-unit">
                <button class="toggle-sw" type="button" data-toggle="comp">
                  <span class="toggle-thumb"></span>
                  <span class="toggle-sw-led"></span>
                </button>
                <span class="toggle-label">Comp</span>
              </div>
              <div class="toggle-unit">
                <button class="toggle-sw on" type="button" data-toggle="gate">
                  <span class="toggle-thumb"></span>
                  <span class="toggle-sw-led"></span>
                </button>
                <span class="toggle-label">Gate</span>
              </div>
            </div>
          </div>

          <div class="section">
            <div class="section-label">Channel Mix</div>
            <div class="fader-row" data-d3-17-faderrow></div>
          </div>

        </div>

        <div class="right-controls">
          <div class="section-label rl">Level</div>
          <div class="vu-row" data-d3-17-vurow></div>
        </div>

      </div>

    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@400;500;600;700&display=swap');

.d3-17 {
  --d3-17-bg: #11131a;
  --d3-17-panel: #1a1c22;
  --d3-17-inset: #14161b;
  --d3-17-text-dim: rgba(120,140,180,0.40);
  --d3-17-led-cyan: #00e8cc;
  --d3-17-led-amber: #ffaa00;
  --d3-17-led-red: #ff3840;
  --d3-17-led-green: #00e060;
  --d3-17-led-purple: #c060ff;
  --d3-17-led-ring: rgba(0,0,0,0);
  --d3-17-led-off: rgba(0,0,0,0.40);
  --d3-17-led-off-deep: rgba(0,0,0,0.50);
  --d3-17-ink-cyan: #00e8cc;
  --d3-17-ink-green: #00e060;
  --d3-17-glow-cyan: rgba(0,232,204,0.50);
  --d3-17-glow-green: rgba(0,224,96,0.50);
  --d3-17-edge-hi: rgba(255,255,255,0.05);
  --d3-17-edge-hi-soft: rgba(255,255,255,0.04);
  --d3-17-drop: rgba(0,0,0,0.60);
  --d3-17-drop-mid: rgba(0,0,0,0.50);
  --d3-17-inner-hi: rgba(255,255,255,0.06);
  --d3-17-inner-lo: rgba(0,0,0,0.40);
  --d3-17-scan: rgba(255,255,255,0.007);
  --d3-17-rule: rgba(255,255,255,0.06);
  --d3-17-inset-shadow: rgba(0,0,0,0.50);
  --d3-17-cap-ink: rgba(255,255,255,0.85);
  --d3-17-cap-hi: rgba(255,255,255,0.18);
  --d3-17-cap-lo: rgba(0,0,0,0.30);
  --d3-17-cap-cyan: #1a2838;
  --d3-17-cap-cyan-edge: #0e1820;
  --d3-17-cap-amber: #281a10;
  --d3-17-cap-amber-edge: #180e08;
  --d3-17-cap-red: #281818;
  --d3-17-cap-red-edge: #180808;
  --d3-17-cap-green: #182818;
  --d3-17-cap-green-edge: #081808;
  --d3-17-cap-purple: #1e1a30;
  --d3-17-cap-purple-edge: #100e20;
  --d3-17-thumb-1: #2e3248;
  --d3-17-thumb-2: #22263a;
  --d3-17-thumb-edge: #12141e;
  --d3-17-fader-thumb-1: #3a3f58;
  --d3-17-fader-thumb-2: #2a2e44;
  --d3-17-fader-thumb-edge: #141620;
  --d3-17-thumb-hi: rgba(255,255,255,0.14);
  --d3-17-tick: rgba(255,255,255,0.06);
  --d3-17-well-1: rgba(0,0,0,0.60);
  --d3-17-well-2: rgba(0,0,0,0.80);
  --d3-17-well-hi: rgba(255,255,255,0.05);
  --d3-17-ui-face: rgba(255,255,255,0.05);
  --d3-17-ui-line: rgba(255,255,255,0.14);
  --d3-17-ui-ink: #b8c6e0;
  width: 100%;
  min-height: max(100vh, 580px);
  display: block;
  position: relative;
  background: var(--d3-17-bg);
  font-family: 'Share Tech Mono', ui-monospace, monospace;
  overflow: hidden;
  box-sizing: border-box;
}

.d3-17 *,
.d3-17 *::before,
.d3-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.d3-17:has(.d3-17__theme-input:checked) {
  --d3-17-bg: #dcdee4;
  --d3-17-panel: #eceef2;
  --d3-17-inset: #d6d9e0;
  --d3-17-text-dim: rgba(24,38,64,0.92);
  --d3-17-led-cyan: #00c2ab;
  --d3-17-led-amber: #ff9d00;
  --d3-17-led-red: #e4121f;
  --d3-17-led-green: #00a844;
  --d3-17-led-purple: #9b30ff;
  --d3-17-led-ring: rgba(18,28,48,0.45);
  --d3-17-led-off: rgba(58,70,92,0.26);
  --d3-17-led-off-deep: rgba(58,70,92,0.32);
  --d3-17-ink-cyan: #045f55;
  --d3-17-ink-green: #0a6530;
  --d3-17-glow-cyan: rgba(0,120,105,0.26);
  --d3-17-glow-green: rgba(0,130,60,0.26);
  --d3-17-edge-hi: rgba(255,255,255,0.85);
  --d3-17-edge-hi-soft: rgba(255,255,255,0.70);
  --d3-17-drop: rgba(35,45,70,0.16);
  --d3-17-drop-mid: rgba(35,45,70,0.20);
  --d3-17-inner-hi: rgba(255,255,255,0.90);
  --d3-17-inner-lo: rgba(35,45,70,0.10);
  --d3-17-scan: rgba(20,30,60,0.020);
  --d3-17-rule: rgba(30,45,80,0.14);
  --d3-17-inset-shadow: rgba(35,45,70,0.20);
  --d3-17-cap-ink: rgba(18,26,44,0.88);
  --d3-17-cap-hi: rgba(255,255,255,0.90);
  --d3-17-cap-lo: rgba(40,50,70,0.18);
  --d3-17-cap-cyan: #cfe2e6;
  --d3-17-cap-cyan-edge: #a5bcc2;
  --d3-17-cap-amber: #efe0cc;
  --d3-17-cap-amber-edge: #c8b18e;
  --d3-17-cap-red: #f0d6d6;
  --d3-17-cap-red-edge: #c7a2a2;
  --d3-17-cap-green: #d4e8d6;
  --d3-17-cap-green-edge: #a5c2a7;
  --d3-17-cap-purple: #dfd8ef;
  --d3-17-cap-purple-edge: #b2a8ca;
  --d3-17-thumb-1: #f4f6fa;
  --d3-17-thumb-2: #e0e4ee;
  --d3-17-thumb-edge: #b4bac8;
  --d3-17-fader-thumb-1: #f8fafd;
  --d3-17-fader-thumb-2: #e4e8f1;
  --d3-17-fader-thumb-edge: #aeb5c5;
  --d3-17-thumb-hi: rgba(255,255,255,0.95);
  --d3-17-tick: rgba(30,45,80,0.16);
  --d3-17-well-1: rgba(35,45,70,0.16);
  --d3-17-well-2: rgba(35,45,70,0.10);
  --d3-17-well-hi: rgba(255,255,255,0.90);
  --d3-17-ui-face: rgba(255,255,255,0.85);
  --d3-17-ui-line: rgba(30,45,80,0.20);
  --d3-17-ui-ink: #1d2740;
}

@media (prefers-color-scheme: light) {
  .d3-17:has(.d3-17__theme-input:checked) {
    --d3-17-bg: #dcdee4;
    --d3-17-panel: #eceef2;
    --d3-17-inset: #d6d9e0;
    --d3-17-text-dim: rgba(24,38,64,0.92);
    --d3-17-led-cyan: #00c2ab;
    --d3-17-led-amber: #ff9d00;
    --d3-17-led-red: #e4121f;
    --d3-17-led-green: #00a844;
    --d3-17-led-purple: #9b30ff;
    --d3-17-led-ring: rgba(18,28,48,0.45);
    --d3-17-led-off: rgba(58,70,92,0.26);
    --d3-17-led-off-deep: rgba(58,70,92,0.32);
    --d3-17-ink-cyan: #045f55;
    --d3-17-ink-green: #0a6530;
    --d3-17-glow-cyan: rgba(0,120,105,0.26);
    --d3-17-glow-green: rgba(0,130,60,0.26);
    --d3-17-edge-hi: rgba(255,255,255,0.85);
    --d3-17-edge-hi-soft: rgba(255,255,255,0.70);
    --d3-17-drop: rgba(35,45,70,0.16);
    --d3-17-drop-mid: rgba(35,45,70,0.20);
    --d3-17-inner-hi: rgba(255,255,255,0.90);
    --d3-17-inner-lo: rgba(35,45,70,0.10);
    --d3-17-scan: rgba(20,30,60,0.020);
    --d3-17-rule: rgba(30,45,80,0.14);
    --d3-17-inset-shadow: rgba(35,45,70,0.20);
    --d3-17-cap-ink: rgba(18,26,44,0.88);
    --d3-17-cap-hi: rgba(255,255,255,0.90);
    --d3-17-cap-lo: rgba(40,50,70,0.18);
    --d3-17-cap-cyan: #cfe2e6;
    --d3-17-cap-cyan-edge: #a5bcc2;
    --d3-17-cap-amber: #efe0cc;
    --d3-17-cap-amber-edge: #c8b18e;
    --d3-17-cap-red: #f0d6d6;
    --d3-17-cap-red-edge: #c7a2a2;
    --d3-17-cap-green: #d4e8d6;
    --d3-17-cap-green-edge: #a5c2a7;
    --d3-17-cap-purple: #dfd8ef;
    --d3-17-cap-purple-edge: #b2a8ca;
    --d3-17-thumb-1: #f4f6fa;
    --d3-17-thumb-2: #e0e4ee;
    --d3-17-thumb-edge: #b4bac8;
    --d3-17-fader-thumb-1: #f8fafd;
    --d3-17-fader-thumb-2: #e4e8f1;
    --d3-17-fader-thumb-edge: #aeb5c5;
    --d3-17-thumb-hi: rgba(255,255,255,0.95);
    --d3-17-tick: rgba(30,45,80,0.16);
    --d3-17-well-1: rgba(35,45,70,0.16);
    --d3-17-well-2: rgba(35,45,70,0.10);
    --d3-17-well-hi: rgba(255,255,255,0.90);
    --d3-17-ui-face: rgba(255,255,255,0.85);
    --d3-17-ui-line: rgba(30,45,80,0.20);
    --d3-17-ui-ink: #1d2740;
  }
}

@media (prefers-color-scheme: dark) {
  .d3-17:has(.d3-17__theme-input:checked) {
    --d3-17-bg: #dcdee4;
    --d3-17-panel: #eceef2;
    --d3-17-inset: #d6d9e0;
    --d3-17-text-dim: rgba(24,38,64,0.92);
    --d3-17-led-cyan: #00c2ab;
    --d3-17-led-amber: #ff9d00;
    --d3-17-led-red: #e4121f;
    --d3-17-led-green: #00a844;
    --d3-17-led-purple: #9b30ff;
    --d3-17-led-ring: rgba(18,28,48,0.45);
    --d3-17-led-off: rgba(58,70,92,0.26);
    --d3-17-led-off-deep: rgba(58,70,92,0.32);
    --d3-17-ink-cyan: #045f55;
    --d3-17-ink-green: #0a6530;
    --d3-17-glow-cyan: rgba(0,120,105,0.26);
    --d3-17-glow-green: rgba(0,130,60,0.26);
    --d3-17-edge-hi: rgba(255,255,255,0.85);
    --d3-17-edge-hi-soft: rgba(255,255,255,0.70);
    --d3-17-drop: rgba(35,45,70,0.16);
    --d3-17-drop-mid: rgba(35,45,70,0.20);
    --d3-17-inner-hi: rgba(255,255,255,0.90);
    --d3-17-inner-lo: rgba(35,45,70,0.10);
    --d3-17-scan: rgba(20,30,60,0.020);
    --d3-17-rule: rgba(30,45,80,0.14);
    --d3-17-inset-shadow: rgba(35,45,70,0.20);
    --d3-17-cap-ink: rgba(18,26,44,0.88);
    --d3-17-cap-hi: rgba(255,255,255,0.90);
    --d3-17-cap-lo: rgba(40,50,70,0.18);
    --d3-17-cap-cyan: #cfe2e6;
    --d3-17-cap-cyan-edge: #a5bcc2;
    --d3-17-cap-amber: #efe0cc;
    --d3-17-cap-amber-edge: #c8b18e;
    --d3-17-cap-red: #f0d6d6;
    --d3-17-cap-red-edge: #c7a2a2;
    --d3-17-cap-green: #d4e8d6;
    --d3-17-cap-green-edge: #a5c2a7;
    --d3-17-cap-purple: #dfd8ef;
    --d3-17-cap-purple-edge: #b2a8ca;
    --d3-17-thumb-1: #f4f6fa;
    --d3-17-thumb-2: #e0e4ee;
    --d3-17-thumb-edge: #b4bac8;
    --d3-17-fader-thumb-1: #f8fafd;
    --d3-17-fader-thumb-2: #e4e8f1;
    --d3-17-fader-thumb-edge: #aeb5c5;
    --d3-17-thumb-hi: rgba(255,255,255,0.95);
    --d3-17-tick: rgba(30,45,80,0.16);
    --d3-17-well-1: rgba(35,45,70,0.16);
    --d3-17-well-2: rgba(35,45,70,0.10);
    --d3-17-well-hi: rgba(255,255,255,0.90);
    --d3-17-ui-face: rgba(255,255,255,0.85);
    --d3-17-ui-line: rgba(30,45,80,0.20);
    --d3-17-ui-ink: #1d2740;
  }
}

.d3-17 .d3-17__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 30;
}

.d3-17 .d3-17__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
  z-index: 1;
}

.d3-17 .d3-17__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-17-ui-line);
  border-radius: 8px;
  background: var(--d3-17-ui-face);
  color: var(--d3-17-ui-ink);
  pointer-events: none;
}

.d3-17 .d3-17__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-17 .d3-17__theme-input:focus-visible + .d3-17__theme-label {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.d3-17 .card {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.d3-17 .panel {
  width: 100%;
  max-width: 640px;
  background: var(--d3-17-panel);
  border-radius: 16px;
  padding: 28px;
  box-shadow: 0 0 0 1px var(--d3-17-edge-hi), 0 2px 0 var(--d3-17-edge-hi-soft), 0 4px 24px var(--d3-17-drop), 0 1px 0 var(--d3-17-inner-hi) inset, 0 -1px 0 var(--d3-17-inner-lo) inset;
  position: relative;
}

.d3-17 .panel::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 16px;
  background-image: repeating-linear-gradient(90deg, transparent 0px, transparent 2px, var(--d3-17-scan) 2px, var(--d3-17-scan) 3px);
  pointer-events: none;
}

.d3-17 .readout {
  background: var(--d3-17-inset);
  border-radius: 8px;
  padding: 11px 16px;
  box-shadow: inset 0 2px 6px var(--d3-17-inset-shadow);
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 18px;
  gap: 8px;
}

.d3-17 .readout-item {
  text-align: center;
}

.d3-17 .readout-key {
  font-size: 7px;
  letter-spacing: 3px;
  color: var(--d3-17-text-dim);
  text-transform: uppercase;
  margin-bottom: 3px;
}

.d3-17 .readout-val {
  font-family: 'Share Tech Mono', monospace;
  font-size: 13px;
  letter-spacing: 2px;
  color: var(--d3-17-ink-cyan);
  text-shadow: 0 0 10px var(--d3-17-glow-cyan);
}

.d3-17 .readout-val.live {
  color: var(--d3-17-ink-green);
  text-shadow: 0 0 10px var(--d3-17-glow-green);
}

.d3-17 .section {
  margin-bottom: 22px;
}

.d3-17 .section:last-child {
  margin-bottom: 0;
}

.d3-17 .section-label {
  font-family: 'Share Tech Mono', monospace;
  font-size: 9px;
  letter-spacing: 3px;
  color: var(--d3-17-text-dim);
  text-transform: uppercase;
  margin-bottom: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.d3-17 .section-label::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--d3-17-rule);
}

.d3-17 .section-label.rl {
  margin-bottom: 10px;
}

.d3-17 .main-layout {
  display: flex;
  gap: 22px;
  align-items: flex-start;
}

.d3-17 .left-controls {
  flex: 1;
}

.d3-17 .right-controls {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.d3-17 .btn-row {
  display: flex;
  gap: 12px;
  align-items: center;
  flex-wrap: wrap;
}

.d3-17 .push-btn {
  position: relative;
  cursor: pointer;
  border: none;
  background: none;
  padding: 0;
  outline: none;
}

.d3-17 .push-btn-body {
  width: 72px;
  height: 50px;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  position: relative;
  transition: transform 0.08s ease, box-shadow 0.08s ease;
  background: var(--d3-17-cap);
  box-shadow: 0 6px 0 var(--d3-17-cap-edge), 0 7px 12px var(--d3-17-drop-mid), inset 0 1px 0 var(--d3-17-cap-hi), inset 0 -1px 0 var(--d3-17-cap-lo);
}

.d3-17 .push-btn:active .push-btn-body,
.d3-17 .push-btn.pressed .push-btn-body {
  transform: translateY(4px);
  box-shadow: 0 2px 0 var(--d3-17-cap-edge), 0 3px 6px var(--d3-17-drop-mid), inset 0 2px 4px var(--d3-17-cap-lo), inset 0 1px 0 var(--d3-17-cap-hi);
}

.d3-17 .push-btn-label {
  font-family: 'Share Tech Mono', monospace;
  font-size: 8px;
  letter-spacing: 1.5px;
  color: var(--d3-17-cap-ink);
  text-transform: uppercase;
}

.d3-17 .btn-led {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--d3-17-led-off);
  box-shadow: inset 0 0 0 1px var(--d3-17-led-ring);
  transition: background 0.2s, box-shadow 0.2s;
}

.d3-17 .push-btn.active .btn-led {
  background: var(--d3-17-led);
  box-shadow: 0 0 6px var(--d3-17-led), 0 0 14px var(--d3-17-led), 0 0 0 1px var(--d3-17-led-ring);
}

.d3-17 .push-btn:nth-child(1) {
  --d3-17-cap: var(--d3-17-cap-cyan);
  --d3-17-cap-edge: var(--d3-17-cap-cyan-edge);
  --d3-17-led: var(--d3-17-led-cyan);
}

.d3-17 .push-btn:nth-child(2) {
  --d3-17-cap: var(--d3-17-cap-amber);
  --d3-17-cap-edge: var(--d3-17-cap-amber-edge);
  --d3-17-led: var(--d3-17-led-amber);
}

.d3-17 .push-btn:nth-child(3) {
  --d3-17-cap: var(--d3-17-cap-red);
  --d3-17-cap-edge: var(--d3-17-cap-red-edge);
  --d3-17-led: var(--d3-17-led-red);
}

.d3-17 .push-btn:nth-child(4) {
  --d3-17-cap: var(--d3-17-cap-green);
  --d3-17-cap-edge: var(--d3-17-cap-green-edge);
  --d3-17-led: var(--d3-17-led-green);
}

.d3-17 .push-btn:nth-child(5) {
  --d3-17-cap: var(--d3-17-cap-purple);
  --d3-17-cap-edge: var(--d3-17-cap-purple-edge);
  --d3-17-led: var(--d3-17-led-purple);
}

.d3-17 .toggle-row {
  display: flex;
  gap: 22px;
  align-items: center;
  flex-wrap: wrap;
}

.d3-17 .toggle-unit {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.d3-17 .toggle-label {
  font-size: 8px;
  letter-spacing: 2px;
  color: var(--d3-17-text-dim);
  text-transform: uppercase;
}

.d3-17 .toggle-sw {
  position: relative;
  width: 60px;
  height: 28px;
  cursor: pointer;
  border-radius: 6px;
  background: var(--d3-17-inset);
  border: none;
  padding: 3px;
  box-shadow: inset 0 2px 6px var(--d3-17-well-1), inset 0 1px 2px var(--d3-17-well-2), 0 1px 0 var(--d3-17-inner-hi);
}

.d3-17 .toggle-sw[data-toggle="mono"] {
  --d3-17-sw-led: var(--d3-17-led-cyan);
}

.d3-17 .toggle-sw[data-toggle="reverb"] {
  --d3-17-sw-led: var(--d3-17-led-purple);
}

.d3-17 .toggle-sw[data-toggle="eq"] {
  --d3-17-sw-led: var(--d3-17-led-amber);
}

.d3-17 .toggle-sw[data-toggle="comp"] {
  --d3-17-sw-led: var(--d3-17-led-red);
}

.d3-17 .toggle-sw[data-toggle="gate"] {
  --d3-17-sw-led: var(--d3-17-led-green);
}

.d3-17 .toggle-thumb {
  display: block;
  width: 26px;
  height: 22px;
  border-radius: 4px;
  background: linear-gradient(180deg, var(--d3-17-thumb-1) 0%, var(--d3-17-thumb-2) 100%);
  box-shadow: 0 3px 0 var(--d3-17-thumb-edge), 0 4px 8px var(--d3-17-drop-mid), inset 0 1px 0 var(--d3-17-thumb-hi);
  transition: transform 0.18s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.d3-17 .toggle-sw.on .toggle-thumb {
  transform: translateX(28px);
}

.d3-17 .toggle-sw-led {
  position: absolute;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  top: 50%;
  right: 7px;
  transform: translateY(-50%);
  background: var(--d3-17-led-off-deep);
  transition: background 0.2s, box-shadow 0.2s;
}

.d3-17 .toggle-sw.on .toggle-sw-led {
  background: var(--d3-17-sw-led);
  box-shadow: 0 0 6px var(--d3-17-sw-led), 0 0 0 1px var(--d3-17-led-ring);
}

.d3-17 .fader-row {
  display: flex;
  gap: 18px;
  align-items: flex-end;
  flex-wrap: wrap;
}

.d3-17 .fader-unit {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 7px;
}

.d3-17 .fader-track-wrap {
  width: 28px;
  height: 120px;
  background: var(--d3-17-inset);
  border-radius: 6px;
  box-shadow: inset 0 2px 6px var(--d3-17-well-1), inset 0 1px 3px var(--d3-17-well-2), 0 1px 0 var(--d3-17-well-hi);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.d3-17 .fader-track-wrap::before {
  content: '';
  position: absolute;
  left: 4px;
  right: 4px;
  top: 10px;
  bottom: 10px;
  background: repeating-linear-gradient(to bottom, var(--d3-17-tick) 0px, var(--d3-17-tick) 1px, transparent 1px, transparent 10px);
  pointer-events: none;
}

.d3-17 .fader-thumb {
  width: 24px;
  height: 20px;
  border-radius: 4px;
  background: linear-gradient(180deg, var(--d3-17-fader-thumb-1) 0%, var(--d3-17-fader-thumb-2) 100%);
  box-shadow: 0 3px 0 var(--d3-17-fader-thumb-edge), 0 4px 8px var(--d3-17-drop-mid), inset 0 1px 0 var(--d3-17-thumb-hi);
  position: absolute;
  cursor: ns-resize;
  user-select: none;
  touch-action: none;
  z-index: 2;
}

.d3-17 .fader-fill {
  position: absolute;
  bottom: 10px;
  left: 10px;
  right: 10px;
  border-radius: 2px;
  background: linear-gradient(to top, var(--d3-17-fader-color), transparent);
  opacity: 0.6;
  pointer-events: none;
}

.d3-17 .fader-label {
  font-size: 8px;
  letter-spacing: 2px;
  color: var(--d3-17-text-dim);
  text-transform: uppercase;
}

.d3-17 .fader-value {
  font-size: 10px;
  font-family: 'Share Tech Mono', monospace;
  letter-spacing: 1px;
  min-height: 16px;
  color: var(--d3-17-fader-color);
}

.d3-17 .vu-row {
  display: flex;
  gap: 9px;
  align-items: flex-end;
  margin-left: 8px;
}

.d3-17 .vu-bar-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
}

.d3-17 .vu-track {
  width: 13px;
  height: 120px;
  background: var(--d3-17-inset);
  border-radius: 4px;
  box-shadow: inset 0 2px 5px var(--d3-17-well-1);
  display: flex;
  flex-direction: column-reverse;
  overflow: hidden;
  gap: 1px;
  padding: 3px;
}

.d3-17 .vu-seg {
  width: 100%;
  height: 7px;
  border-radius: 2px;
  background: var(--d3-17-seg-color);
  opacity: 0.22;
  transition: opacity 0.08s;
  flex-shrink: 0;
}

.d3-17 .vu-seg.lit {
  opacity: 1;
  box-shadow: 0 0 6px var(--d3-17-seg-color), inset 0 0 0 1px var(--d3-17-led-ring);
}

.d3-17 .vu-label {
  font-size: 8px;
  letter-spacing: 2px;
  color: var(--d3-17-text-dim);
  text-transform: uppercase;
}

@media (max-width: 720px) {
  .d3-17 .main-layout {
    flex-direction: column;
  }

  .d3-17 .right-controls {
    width: 100%;
  }

  .d3-17 .vu-row {
    justify-content: flex-start;
    margin-left: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .d3-17 .toggle-thumb {
    transition: none !important;
  }

  .d3-17 .vu-seg {
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.d3-17');
  if (!root) return;

  const modeReadout = root.querySelector('[data-d3-17-mode]');
  root.querySelectorAll('.push-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      btn.classList.toggle('active');
      const action = btn.dataset.action;
      const modes = { play: 'PLAY', rec: 'RECORD', stop: 'STOPPED', loop: 'LOOP', fx: 'FX ON' };
      if (modes[action] && modeReadout) modeReadout.textContent = modes[action];
    });
  });

  root.querySelectorAll('.toggle-sw').forEach(sw => {
    sw.addEventListener('click', () => sw.classList.toggle('on'));
  });

  const faderRow = root.querySelector('[data-d3-17-faderrow]');
  const masterReadout = root.querySelector('[data-d3-17-master]');
  const faderData = [
    { label: 'CH.1', color: 'var(--d3-17-led-cyan)',   val: 87 },
    { label: 'CH.2', color: 'var(--d3-17-led-cyan)',   val: 62 },
    { label: 'CH.3', color: 'var(--d3-17-led-amber)',  val: 74 },
    { label: 'CH.4', color: 'var(--d3-17-led-amber)',  val: 90 },
    { label: 'SUB',  color: 'var(--d3-17-led-purple)', val: 55 },
    { label: 'MST',  color: 'var(--d3-17-led-green)',  val: 87 }
  ];
  const TRACK_H = 120, PADDING = 10, THUMB_H = 20;
  const TRAVEL = TRACK_H - PADDING * 2 - THUMB_H;

  faderData.forEach((fd, fi) => {
    const unit = document.createElement('div');
    unit.className = 'fader-unit';
    unit.innerHTML =
      '<div class="fader-value" style="--d3-17-fader-color:' + fd.color + '">' + fd.val + '</div>' +
      '<div class="fader-track-wrap">' +
      '<div class="fader-fill" style="--d3-17-fader-color:' + fd.color + '"></div>' +
      '<div class="fader-thumb"></div>' +
      '</div>' +
      '<div class="fader-label">' + fd.label + '</div>';
    faderRow.appendChild(unit);

    const thumb = unit.querySelector('.fader-thumb');
    const fill = unit.querySelector('.fader-fill');
    const valEl = unit.querySelector('.fader-value');

    function setVal(v) {
      v = Math.max(0, Math.min(100, v));
      fd.val = Math.round(v);
      const pct = v / 100;
      thumb.style.top = (PADDING + TRAVEL * (1 - pct)) + 'px';
      fill.style.height = (TRAVEL * pct + THUMB_H / 2) + 'px';
      valEl.textContent = fd.val;
      if (fi === 5 && masterReadout) masterReadout.textContent = fd.val;
    }
    setVal(fd.val);

    let dragging = false, startY = 0, startVal = 0;
    thumb.addEventListener('mousedown', e => {
      dragging = true; startY = e.clientY; startVal = fd.val; e.preventDefault();
    });
    root.addEventListener('mousemove', e => {
      if (!dragging) return;
      setVal(startVal + ((startY - e.clientY) / TRAVEL) * 100);
    });
    root.addEventListener('mouseup', () => { dragging = false; });
    root.addEventListener('mouseleave', () => { dragging = false; });
    thumb.addEventListener('touchstart', e => {
      dragging = true; startY = e.touches[0].clientY; startVal = fd.val;
    }, { passive: true });
    root.addEventListener('touchmove', e => {
      if (!dragging) return;
      setVal(startVal + ((startY - e.touches[0].clientY) / TRAVEL) * 100);
    }, { passive: true });
    root.addEventListener('touchend', () => { dragging = false; });
  });

  const vuRow = root.querySelector('[data-d3-17-vurow]');
  const vuData = [
    { label: 'L', color: 'var(--d3-17-led-cyan)' },
    { label: 'R', color: 'var(--d3-17-led-cyan)' }
  ];
  const N_SEGS = 12;
  const vuIntervals = [];

  vuData.forEach((vu, vi) => {
    const wrap = document.createElement('div');
    wrap.className = 'vu-bar-wrap';
    const track = document.createElement('div');
    track.className = 'vu-track';
    for (let s = 0; s < N_SEGS; s++) {
      const seg = document.createElement('div');
      seg.className = 'vu-seg';
      const segColor = s >= N_SEGS - 2 ? 'var(--d3-17-led-red)' : s >= N_SEGS - 4 ? 'var(--d3-17-led-amber)' : vu.color;
      seg.style.setProperty('--d3-17-seg-color', segColor);
      track.appendChild(seg);
    }
    const lbl = document.createElement('div');
    lbl.className = 'vu-label';
    lbl.textContent = vu.label;
    wrap.appendChild(track);
    wrap.appendChild(lbl);
    vuRow.appendChild(wrap);

    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReduced) return;

    function animateVU() {
      const segs = track.querySelectorAll('.vu-seg');
      const base = 6;
      const variation = Math.random() > 0.9 ? Math.floor(Math.random() * 3) : 0;
      const level = base + variation;
      segs.forEach((seg, si) => {
        seg.classList.toggle('lit', si < level);
      });
      vuIntervals[vi] = setTimeout(animateVU, 80 + Math.random() * 60);
    }
    setTimeout(animateVU, vi * 40);
  });

  const bpmReadout = root.querySelector('[data-d3-17-bpm]');
  if (bpmReadout) {
    setInterval(() => {
      bpmReadout.textContent = 124 + (Math.random() > 0.96 ? 1 : 0);
    }, 500);
  }
})();
```
