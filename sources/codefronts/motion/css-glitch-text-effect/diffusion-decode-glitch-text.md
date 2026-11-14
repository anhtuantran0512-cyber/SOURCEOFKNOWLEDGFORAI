---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/diffusion-decode-glitch-text/"
title: "Diffusion Decode Glitch Text"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "Text that materializes the way Stable Diffusion or Imagen renders words inside generated images — starts as randomized glyph noise that progressively…"
has_js: "false"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Diffusion Decode Glitch Text
Source: https://codefronts.com/motion/css-glitch-text-effect/diffusion-decode-glitch-text/

Text that materializes the way Stable Diffusion or Imagen renders words inside generated images — starts as randomized glyph noise that progressively crystallizes into the target word over ~2 seconds, with chromatic ghost letterforms visible during the decoding process and a t-step counter ticking from t=1.0 to t=0.0. Loops through a pool of AI-era keywords.
## HTML
```html
<div class="gt-16">
  <div class="gt-16__status">
    <span class="gt-16__sampler">karras · 50 steps</span>
    <span class="gt-16__t" id="gt-16-t">t=1.000</span>
  </div>
  <div class="gt-16__stage" id="gt-16-stage"></div>
  <div class="gt-16__progress">
    <div class="gt-16__progress-fill" id="gt-16-prog"></div>
  </div>
  <div class="gt-16__meta">
    <span class="gt-16__chip">diffusion · v3.2</span>
    <span class="gt-16__chip">step <span id="gt-16-step">1</span>/50</span>
    <span class="gt-16__chip gt-16__chip--mint" id="gt-16-state">decoding</span>
  </div>
</div>
```
## CSS
```css
.gt-16,
.gt-16 *,
.gt-16 *::before,
.gt-16 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-16 ::selection {
  background: rgba(168,85,247,0.4);
  color: #fff;
}

.gt-16 {
  --bg: #050008;
  --surface: rgba(255,255,255,0.02);
  --text: #f0eeff;
  --muted: #7a78a3;
  --accent: #c4b5fd;
  --red: #ff4d6d;
  --cyan: #00e5ff;
  --mint: #5eead4;
  font-family: 'JetBrains Mono', 'SF Mono', ui-monospace, monospace;
  background: radial-gradient(ellipse at 30% 20%, rgba(168,85,247,0.15) 0%, transparent 50%), radial-gradient(ellipse at 70% 80%, rgba(0,229,255,0.12) 0%, transparent 50%), var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  gap: 28px;
  color: var(--text);
  position: relative;
  overflow: hidden;
}
/* Noise overlay — fades with decode progress (controlled via CSS var) */

.gt-16::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 17% 23%, rgba(196,181,253,0.25) 0%, transparent 2%), radial-gradient(circle at 64% 87%, rgba(0,229,255,0.20) 0%, transparent 2%), radial-gradient(circle at 38% 71%, rgba(255,77,109,0.18) 0%, transparent 2%), radial-gradient(circle at 89% 41%, rgba(196,181,253,0.22) 0%, transparent 2%), radial-gradient(circle at 12% 79%, rgba(0,229,255,0.18) 0%, transparent 2%);
  opacity: 0.6;
  pointer-events: none;
  animation: gt-16-noise-pan 8s linear infinite;
  z-index: 0;
}

@keyframes gt-16-noise-pan {
  0%,
    100% {
    transform: translate(0, 0);
  }

  50% {
    transform: translate(-8px, 6px);
  }
}

.gt-16__status {
  width: 100%;
  max-width: 720px;
  display: flex;
  justify-content: space-between;
  font-size: 10px;
  letter-spacing: 0.1em;
  color: var(--muted);
  text-transform: uppercase;
  position: relative;
  z-index: 2;
}

.gt-16__t {
  color: var(--accent);
  font-variant-numeric: tabular-nums;
}

.gt-16__stage {
  display: flex;
  font-size: clamp(54px, 9vw, 96px);
  font-weight: 900;
  letter-spacing: 2px;
  text-transform: uppercase;
  line-height: 1;
  position: relative;
  z-index: 2;
  min-height: 1.2em;
}
/* Each character — a stack with chromatic ghosts via pseudo-elements */

.gt-16__char {
  position: relative;
  display: inline-block;
  width: 0.7em;
  text-align: center;
  color: var(--text);
}

.gt-16__char::before,
.gt-16__char::after {
  content: attr(data-ghost);
  position: absolute;
  inset: 0;
  pointer-events: none;
  mix-blend-mode: screen;
  transition: opacity 200ms;
}

.gt-16__char::before {
  color: var(--red);
  transform: translateX(-4px);
  opacity: var(--ghost-op, 0.85);
}

.gt-16__char::after {
  color: var(--cyan);
  transform: translateX(4px);
  opacity: var(--ghost-op, 0.85);
  content: attr(data-ghost2);
}

.gt-16__char.is-settled {
  --ghost-op: 0;
}

.gt-16__progress {
  width: 100%;
  max-width: 480px;
  height: 2px;
  background: rgba(255,255,255,0.06);
  border-radius: 1px;
  position: relative;
  z-index: 2;
  overflow: hidden;
}

.gt-16__progress-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, var(--accent), var(--cyan));
  box-shadow: 0 0 8px var(--accent);
  transition: width 80ms linear;
}

.gt-16__meta {
  display: flex;
  gap: 6px;
  position: relative;
  z-index: 2;
}

.gt-16__chip {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  padding: 4px 10px;
  border-radius: 100px;
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.04em;
  color: var(--muted);
}

.gt-16__chip--mint {
  background: rgba(94,234,212,0.08);
  border-color: rgba(94,234,212,0.2);
  color: var(--mint);
}

@media (prefers-reduced-motion: reduce) {
  .gt-16::before {
    animation: none;
  }

  .gt-16__char::before,
    .gt-16__char::after {
    opacity: 0;
  }
}
```

## JavaScript
```js
(function() {
  const stage = document.getElementById('gt-16-stage');
  const tEl   = document.getElementById('gt-16-t');
  const prog  = document.getElementById('gt-16-prog');
  const step  = document.getElementById('gt-16-step');
  const state = document.getElementById('gt-16-state');
  if (!stage) return;

  const WORDS = ['SYNTHESIZE', 'INFERENCE', 'EMBEDDING', 'LATENT', 'DECODE', 'TENSOR'];
  const RANDOM_CHARS = 'ABCDEFGHJKLMNPRSTUVWXYZ0123456789ΣΦΨΩαβγδλμ∇∂∞≈≠□◇△▽▢';
  const DECODE_MS = 2000;
  const HOLD_MS = 1500;
  const RENOISE_MS = 800;

  let wordIdx = 0;
  let charSpans = [];

  function rand() {
    return RANDOM_CHARS[Math.floor(Math.random() * RANDOM_CHARS.length)];
  }

  function buildWord(word) {
    stage.innerHTML = '';
    charSpans = [];
    for (let i = 0; i < word.length; i++) {
      const c = document.createElement('span');
      c.className = 'gt-16__char';
      c.textContent = rand();
      c.setAttribute('data-ghost', rand());
      c.setAttribute('data-ghost2', rand());
      stage.appendChild(c);
      charSpans.push({ el: c, target: word[i], settled: false });
    }
  }

  function tick(progress) {
    /* progress 0→1 during decode. Each char's chance of being settled
       increases with progress. Random glyphs cycle for unsettled chars. */
    let unsettledCount = 0;
    charSpans.forEach((s, i) => {
      if (!s.settled) {
        // Probability of settling this tick scales with global progress + per-char offset
        const settleProb = Math.pow(progress, 1.5) * 0.18;
        if (progress > 0.95 || Math.random() < settleProb * (1 + i * 0.05)) {
          s.settled = true;
          s.el.textContent = s.target;
          s.el.classList.add('is-settled');
          s.el.removeAttribute('data-ghost');
          s.el.removeAttribute('data-ghost2');
        } else {
          unsettledCount++;
          s.el.textContent = rand();
          s.el.setAttribute('data-ghost', rand());
          s.el.setAttribute('data-ghost2', rand());
        }
      }
    });
    return unsettledCount;
  }

  function renoise() {
    /* Reverse: settled chars become unsettled, ghosts re-appear, glyphs scramble */
    charSpans.forEach(s => {
      s.settled = false;
      s.el.classList.remove('is-settled');
      s.el.textContent = rand();
      s.el.setAttribute('data-ghost', rand());
      s.el.setAttribute('data-ghost2', rand());
    });
  }

  let rafId;
  function decodeCycle() {
    const word = WORDS[wordIdx];
    buildWord(word);
    state.textContent = 'decoding';
    const start = performance.now();
    let lastTick = start;

    function frame(now) {
      const elapsed = now - start;
      const progress = Math.min(1, elapsed / DECODE_MS);
      const t = (1 - progress).toFixed(3);
      const stepN = Math.floor(1 + progress * 49);
      // Throttle DOM updates to 50ms
      if (now - lastTick >= 50) {
        tick(progress);
        tEl.textContent = 't=' + t;
        prog.style.width = (progress * 100) + '%';
        step.textContent = stepN;
        lastTick = now;
      }
      if (progress < 1) {
        rafId = requestAnimationFrame(frame);
      } else {
        // Force final settle
        charSpans.forEach(s => {
          s.settled = true;
          s.el.textContent = s.target;
          s.el.classList.add('is-settled');
        });
        state.textContent = 'resolved';
        // Hold, then re-noise + advance
        setTimeout(() => {
          state.textContent = 're-noising';
          renoise();
          setTimeout(() => {
            wordIdx = (wordIdx + 1) % WORDS.length;
            decodeCycle();
          }, RENOISE_MS);
        }, HOLD_MS);
      }
    }
    rafId = requestAnimationFrame(frame);
  }

  decodeCycle();
})();
```
