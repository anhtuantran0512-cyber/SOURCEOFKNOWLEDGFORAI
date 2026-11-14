---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/3d-perspective-keynote/"
title: "3D Perspective Keynote"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Tech keynote — deep navy + holographic gradient + chrome."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Perspective Keynote
Source: https://codefronts.com/layouts/css-split-screen/3d-perspective-keynote/

Tech keynote — deep navy + holographic gradient + chrome. Two halves tilted in 3D space via perspective + rotateY; left panel angles toward viewer, right panel angles away. The "Apple event slide" feel — premium, sleek, almost cinematic.
## HTML
```html
<section class="ss-key" aria-label="Tech keynote split">
  <span class="ss-key-stars" aria-hidden="true"></span>
  <article class="ss-key-left">
    <span class="ss-key-tag">v3 · MAY 2026</span>
    <h2><span class="ss-key-shine">Aurora.</span></h2>
    <p>
      The smallest, fastest, quietest dev environment we've ever shipped. Built for the way you
      actually code.
    </p>
    <ul class="ss-key-feat">
      <li><span>◉</span>0.3s cold start</li>
      <li><span>◉</span>Type-safe everywhere</li>
      <li><span>◉</span>One-click deploy</li>
    </ul>
    <button type="button" class="ss-key-cta">Watch the keynote →</button>
  </article>
  <article class="ss-key-right" aria-hidden="true">
    <div class="ss-key-card">
      <header>
        <span class="ss-key-dots"> <i></i><i></i><i></i> </span>
        <strong>~/aurora</strong>
      </header>
      <pre><code><span class="ss-key-c">// 0.3s cold start</span>
<span class="ss-key-k">import</span> { app } <span class="ss-key-k">from</span> <span class="ss-key-s">'aurora'</span>;
<span class="ss-key-k">const</span> server <span class="ss-key-o">=</span> <span class="ss-key-fn">app</span>();
<span class="ss-key-fn">server.listen</span>(<span class="ss-key-n">3000</span>);</code></pre>
      <footer>
        <span class="ss-key-stat"><b>0.3s</b><em>start</em></span>
        <span class="ss-key-stat"><b>4.2 MB</b><em>bundle</em></span>
        <span class="ss-key-stat"><b>99 ms</b><em>p99</em></span>
      </footer>
    </div>
    <span class="ss-key-glow"></span>
  </article>
</section>
```
## CSS
```css
.ss-key {
  width: 100%;
  position: relative;
  display: grid;
  grid-template-columns: 45% 55%;
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
  background: radial-gradient(60% 80% at 30% 30%, rgba(80,40,180,0.4) 0%, transparent 60%), radial-gradient(60% 80% at 80% 80%, rgba(0,180,200,0.3) 0%, transparent 60%), linear-gradient(180deg, #0a0a2a 0%, #050518 100%);
  color: #fff;
  border-radius: 0;
  overflow: hidden;
  perspective: 1400px;
  isolation: isolate;
}

.ss-key-stars {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(1.5px 1.5px at 14% 22%, #fff, transparent), radial-gradient(1px 1px at 38% 12%, rgba(255,255,255,0.7), transparent), radial-gradient(1px 1px at 52% 30%, rgba(255,255,255,0.5), transparent), radial-gradient(1.5px 1.5px at 73% 18%, #fff, transparent), radial-gradient(1px 1px at 88% 42%, rgba(255,255,255,0.7), transparent), radial-gradient(1px 1px at 22% 50%, rgba(255,255,255,0.5), transparent), radial-gradient(1.5px 1.5px at 64% 60%, #fff, transparent), radial-gradient(1px 1px at 12% 76%, rgba(255,255,255,0.5), transparent), radial-gradient(1px 1px at 84% 78%, rgba(255,255,255,0.5), transparent);
  pointer-events: none;
  z-index: 0;
}

.ss-key-left {
  padding: 44px 36px 44px 44px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  position: relative;
  transform: rotateY(8deg) translateZ(20px);
  transform-origin: right center;
  z-index: 2;
}

.ss-key-tag {
  font-family: 'JetBrains Mono', 'Courier New', monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.24em;
  color: #00d4ff;
  align-self: flex-start;
  padding: 4px 10px;
  background: rgba(0,212,255,0.1);
  border: 1px solid rgba(0,212,255,0.4);
  border-radius: 12px;
}

.ss-key-left h2 {
  margin: 4px 0 0;
  font-size: clamp(60px, 9vw, 110px);
  font-weight: 900;
  line-height: 0.85;
  letter-spacing: -0.04em;
  color: #fff;
  font-style: italic;
}

.ss-key-shine {
  background: linear-gradient(90deg, #fff 0%, #c4b5fd 30%, #00d4ff 60%, #fff 100%);
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: ss-key-sweep 4s linear infinite;
}

@keyframes ss-key-sweep {
  to {
    background-position: -200% 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ss-key-shine {
    animation: none;
  }
}

.ss-key-left p {
  margin: 0;
  font-size: 16px;
  line-height: 1.6;
  color: #c8c4e0;
  max-width: 380px;
}

.ss-key-feat {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.ss-key-feat li {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 14.5px;
  color: #fff;
}

.ss-key-feat span {
  color: #00d4ff;
  font-size: 13px;
  text-shadow: 0 0 12px rgba(0,212,255,0.6);
}

.ss-key-cta {
  align-self: flex-start;
  padding: 14px 26px;
  background: linear-gradient(135deg, #c4b5fd 0%, #00d4ff 100%);
  color: #050518;
  border: 0;
  border-radius: 28px;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 0.04em;
  cursor: pointer;
  box-shadow: 0 12px 30px rgba(0,212,255,0.4);
  transition: transform 0.16s, box-shadow 0.16s;
}

.ss-key-cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 38px rgba(0,212,255,0.55);
}

.ss-key-right {
  position: relative;
  padding: 44px 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  perspective: 1400px;
  z-index: 1;
}

.ss-key-card {
  position: relative;
  width: 100%;
  max-width: 420px;
  background: linear-gradient(160deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.02) 100%), #14143a;
  border: 1px solid rgba(196,181,253,0.3);
  border-radius: 14px;
  box-shadow: 0 24px 60px rgba(0,0,0,0.5), 0 0 0 1px rgba(0,212,255,0.18), inset 0 1px 0 rgba(255,255,255,0.18);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  transform: rotateY(-12deg) rotateX(4deg) translateZ(-20px);
  z-index: 2;
}

.ss-key-card header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}

.ss-key-dots {
  display: inline-flex;
  gap: 6px;
}

.ss-key-dots i {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

.ss-key-dots i:nth-child(1) {
  background: #ff5f57;
}

.ss-key-dots i:nth-child(2) {
  background: #febc2e;
}

.ss-key-dots i:nth-child(3) {
  background: #28c840;
}

.ss-key-card header strong {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: #8a8ab8;
  font-weight: 500;
}

.ss-key-card pre {
  margin: 0;
  padding: 18px 22px;
  font-family: 'JetBrains Mono', 'Courier New', monospace;
  font-size: 13.5px;
  line-height: 1.7;
  color: #fff;
}

.ss-key-c {
  color: #6a6e96;
  font-style: italic;
}

.ss-key-k {
  color: #c4b5fd;
  font-weight: 600;
}

.ss-key-s {
  color: #fcd34d;
}

.ss-key-o {
  color: #ff52aa;
}

.ss-key-fn {
  color: #00d4ff;
}

.ss-key-n {
  color: #a3e635;
}

.ss-key-card footer {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  border-top: 1px solid rgba(255,255,255,0.08);
}

.ss-key-stat {
  padding: 14px 12px;
  border-right: 1px solid rgba(255,255,255,0.08);
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.ss-key-stat:last-child {
  border-right: 0;
}

.ss-key-stat b {
  font-size: 18px;
  font-weight: 700;
  color: #00d4ff;
  letter-spacing: -0.02em;
}

.ss-key-stat em {
  font-family: 'JetBrains Mono', monospace;
  font-style: normal;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #6a6e96;
}

.ss-key-glow {
  position: absolute;
  width: 60%;
  height: 80%;
  background: radial-gradient(circle, rgba(0,212,255,0.4), transparent 70%);
  filter: blur(60px);
  z-index: 0;
}

@media (max-width: 720px) {
  .ss-key {
    grid-template-columns: 1fr;
    perspective: none;
  }

  .ss-key-left,
    .ss-key-card {
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ss-key-left,
    .ss-key-card {
    transform: none;
  }
}
```
