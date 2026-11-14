---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-typewriter-delete-animation-loop/"
title: "CSS Typewriter Delete Animation Loop"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Six typewriter-and-delete loop patterns: word cycler, terminal prompt, search input placeholder, big display, multiline build-and-erase and code editor typing."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter Delete Animation Loop
Source: https://codefronts.com/motion/css-keyframe-animations/css-typewriter-delete-animation-loop/

Six typewriter-and-delete loop patterns: word cycler, terminal prompt, search input placeholder, big display, multiline build-and-erase and code editor typing.
## HTML
```html
<div class="kf-25">
  <h2>CSS Typewriter Delete Loop Animations</h2>
  <div class="grid">

    <!-- Hero word cycler -->
    <div class="card">
      <div class="hero-type">
        <span class="static">I build</span>
        <span class="dynamic">websites.</span>
      </div>
      <label>Word Cycler</label>
    </div>

    <!-- Terminal -->
    <div class="card">
      <div class="terminal">
        <div class="terminal-line">
          <span class="prompt">❯</span>
          <span class="cmd">npm run dev</span>
        </div>
        <div class="output">✓ Server running on :3000</div>
      </div>
      <label>Terminal Typing</label>
    </div>

    <!-- Input field -->
    <div class="card">
      <div class="input-demo focused">
        <span class="placeholder">Search anything...</span>
        <span class="input-cursor"></span>
      </div>
      <label>Search Input</label>
    </div>

    <!-- Big display -->
    <div class="card" style="align-items:center; justify-content:center; min-height:120px;">
      <div class="big-type">DESIGN.</div>
      <label style="text-align:center">Big Display</label>
    </div>

    <!-- Multiline stagger -->
    <div class="card">
      <div class="multiline">
        <div class="type-line">→ Installing dependencies...</div>
        <div class="type-line">→ Compiling source files...</div>
        <div class="type-line">→ Build complete! ✓</div>
      </div>
      <label>Multiline Stagger</label>
    </div>

    <!-- Code editor -->
    <div class="card">
      <div class="code-editor">
        <div class="code-line"><span class="ln">1</span><span class="code-text">const hero = 'World';</span></div>
        <div class="code-line"><span class="ln">2</span><span class="code-text">function greet(name) {</span></div>
        <div class="code-line"><span class="ln">3</span><span class="code-text">  return `Hello, ${name}`;</span></div>
        <div class="code-line"><span class="ln">4</span><span class="code-text">}</span></div>
      </div>
      <label>Code Editor</label>
    </div>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@400;700;900&display=swap');

.kf-25 *,
.kf-25 *::before,
.kf-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-25 {
  font-family: 'Inter', sans-serif;
  background: #09090f;
  color: #fff;
  padding: 48px 24px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 48px;
}

.kf-25 h2 {
  font-size: 1rem;
  color: #444;
  letter-spacing: 3px;
  text-transform: uppercase;
}

.kf-25 .grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  width: 100%;
  max-width: 960px;
}

.kf-25 .card {
  background: #0f0f1a;
  border: 1px solid #1e1e30;
  border-radius: 16px;
  padding: 36px 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.kf-25 .card label {
  font-size: 0.72rem;
  color: #444;
  letter-spacing: 2px;
  text-transform: uppercase;
}
/* Cursor blink */

@keyframes kf-25-blink {
  0%,
    100% {
    border-color: currentColor;
  }

  50% {
    border-color: transparent;
  }
}
/* 1: Hero headline typewriter with word cycling */

.kf-25 .hero-type {
  font-size: 1.6rem;
  font-weight: 900;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 0;
  flex-wrap: wrap;
}

.kf-25 .hero-type .static {
  color: #888;
  margin-right: 8px;
  font-weight: 400;
  font-size: 1.3rem;
}

.kf-25 .hero-type .dynamic {
  color: #7c6af7;
  border-right: 3px solid #7c6af7;
  overflow: hidden;
  white-space: nowrap;
  animation: kf-25-type1 2s steps(9, end) 0s 1 normal forwards, kf-25-del1 1s steps(9, end) 2.5s 1 normal forwards, kf-25-type2 2s steps(10, end) 4s 1 normal forwards, kf-25-del2 1s steps(10, end) 6.5s 1 normal forwards, kf-25-type3 2s steps(8, end) 8s 1 normal forwards, kf-25-del3 1s steps(8, end) 10.5s 1 normal forwards, kf-25-type1 2s steps(9, end) 12s infinite;
  animation-fill-mode: forwards;
}
/* Simplified: cycle through width */

.kf-25 .dynamic {
  animation: kf-25-wordcycle 12s steps(1) infinite !important;
}

@keyframes kf-25-wordcycle {
  0% {
    width: 0;
  }

  4% {
    width: 9ch;
  }

  25% {
    width: 9ch;
  }

  30% {
    width: 0;
  }

  35% {
    width: 0;
  }

  38% {
    width: 10ch;
    color: #e91e8c;
    border-color: #e91e8c;
  }

  58% {
    width: 10ch;
  }

  63% {
    width: 0;
  }

  68% {
    width: 0;
  }

  71% {
    width: 8ch;
    color: #00d4ff;
    border-color: #00d4ff;
  }

  91% {
    width: 8ch;
  }

  96% {
    width: 0;
  }

  100% {
    width: 0;
    color: #7c6af7;
    border-color: #7c6af7;
  }
}
/* But width alone looks bad — use a more robust approach with multiple spans */
/* 2: Terminal prompt */

.kf-25 .terminal {
  background: #050508;
  border-radius: 10px;
  padding: 20px 16px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
}

.kf-25 .terminal-line {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.kf-25 .prompt {
  color: #00d46a;
}

.kf-25 .cmd {
  color: #fff;
  overflow: hidden;
  white-space: nowrap;
  border-right: 2px solid #fff;
  animation: kf-25-termtype 6s steps(1) infinite;
}

@keyframes kf-25-termtype {
  0% {
    width: 0;
    border-color: #fff;
  }

  5% {
    width: 18ch;
  }

  40% {
    width: 18ch;
  }

  45% {
    width: 10ch;
  }

  50% {
    width: 0;
  }

  55% {
    width: 14ch;
  }

  90% {
    width: 14ch;
  }

  95% {
    width: 0;
  }

  100% {
    width: 0;
  }
}

.kf-25 .output {
  color: #7c6af7;
  font-size: 0.78rem;
  opacity: 0;
  animation: kf-25-termout 6s ease infinite;
}

@keyframes kf-25-termout {
  0%,
    40% {
    opacity: 0;
  }

  50%,
    90% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}
/* 3: Input field typewriter */

.kf-25 .input-demo {
  position: relative;
  background: #0a0a16;
  border: 2px solid #2a2a4a;
  border-radius: 10px;
  padding: 14px 16px;
  font-size: 0.95rem;
  color: #ccc;
  display: flex;
  align-items: center;
  gap: 0;
}

.kf-25 .input-demo .placeholder {
  color: #333;
  overflow: hidden;
  white-space: nowrap;
  animation: kf-25-inputtype 8s steps(1) infinite;
}

@keyframes kf-25-inputtype {
  0% {
    width: 0;
  }

  6% {
    width: 20ch;
    color: #ccc;
  }

  40% {
    width: 20ch;
    color: #ccc;
  }

  50% {
    width: 12ch;
    color: #888;
  }

  56% {
    width: 0;
  }

  60% {
    width: 0;
  }

  65% {
    width: 18ch;
    color: #ccc;
  }

  92% {
    width: 18ch;
  }

  98% {
    width: 0;
  }

  100% {
    width: 0;
  }
}

.kf-25 .input-cursor {
  width: 2px;
  height: 1.1em;
  background: #7c6af7;
  animation: kf-25-blink 0.8s step-end infinite;
  flex-shrink: 0;
}

.kf-25 .input-demo.focused {
  border-color: #7c6af7;
}
/* 4: Big display typewriter  */

.kf-25 .big-type {
  font-size: 2.2rem;
  font-weight: 900;
  color: #fff;
  overflow: hidden;
  white-space: nowrap;
  border-right: 4px solid #f7c948;
  width: fit-content;
  animation: kf-25-bigtype 8s cubic-bezier(0.4,0,0.6,1) infinite, kf-25-blink 0.8s step-end infinite;
}

@keyframes kf-25-bigtype {
  0% {
    width: 0;
  }

  30% {
    width: 7ch;
  }

  60% {
    width: 7ch;
  }

  90% {
    width: 0;
  }

  100% {
    width: 0;
  }
}
/* 5: Multiline stagger */

.kf-25 .multiline {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.kf-25 .type-line {
  font-size: 0.9rem;
  color: #888;
  overflow: hidden;
  white-space: nowrap;
  border-right: 2px solid transparent;
  animation: kf-25-multitype 9s steps(1) infinite;
}

.kf-25 .type-line:nth-child(1) {
  animation-delay: 0s;
}

.kf-25 .type-line:nth-child(2) {
  animation-delay: 0.8s;
}

.kf-25 .type-line:nth-child(3) {
  animation-delay: 1.6s;
}

@keyframes kf-25-multitype {
  0% {
    width: 0;
    border-color: #7c6af7;
    color: #7c6af7;
  }

  20% {
    width: 28ch;
    border-color: #7c6af7;
    color: #fff;
  }

  70% {
    width: 28ch;
    border-color: transparent;
    color: #888;
  }

  80% {
    width: 0;
  }

  100% {
    width: 0;
  }
}
/* 6: Code editor typing */

.kf-25 .code-editor {
  background: #050508;
  border-radius: 10px;
  padding: 20px 16px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
  line-height: 1.8;
}

.kf-25 .code-line {
  display: flex;
  align-items: center;
  gap: 16px;
}

.kf-25 .ln {
  color: #333;
  user-select: none;
  min-width: 16px;
}

.kf-25 .code-text {
  overflow: hidden;
  white-space: nowrap;
  animation: kf-25-codetype 10s steps(1) infinite;
}

.kf-25 .code-line:nth-child(1) .code-text {
  color: #e91e8c;
  animation-delay: 0s;
}

.kf-25 .code-line:nth-child(2) .code-text {
  color: #7c6af7;
  animation-delay: 1.2s;
}

.kf-25 .code-line:nth-child(3) .code-text {
  color: #00d4ff;
  animation-delay: 2.4s;
}

.kf-25 .code-line:nth-child(4) .code-text {
  color: #00d46a;
  animation-delay: 3.6s;
}

@keyframes kf-25-codetype {
  0% {
    width: 0;
  }

  15% {
    width: 30ch;
  }

  75% {
    width: 30ch;
  }

  90% {
    width: 0;
  }

  100% {
    width: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-25 .dynamic,
    .kf-25 .cmd,
    .kf-25 .output,
    .kf-25 .input-demo .placeholder,
    .kf-25 .input-cursor,
    .kf-25 .big-type,
    .kf-25 .type-line,
    .kf-25 .code-text {
    animation: none;
    width: auto;
    opacity: 1;
    border-color: transparent;
  }
}
```
