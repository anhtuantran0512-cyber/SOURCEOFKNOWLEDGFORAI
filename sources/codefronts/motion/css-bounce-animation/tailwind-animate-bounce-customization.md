---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/tailwind-animate-bounce-customization/"
title: "Tailwind animate-bounce Customization"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "The 3-tier Tailwind animate-bounce customization reference — default utility, arbitrary-value tweak, and custom keyframes registered in tailwind.config.js.…"
has_js: "false"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind animate-bounce Customization
Source: https://codefronts.com/motion/css-bounce-animation/tailwind-animate-bounce-customization/

The 3-tier Tailwind animate-bounce customization reference — default utility, arbitrary-value tweak, and custom keyframes registered in tailwind.config.js. Three side-by-side badges bouncing at different heights and durations show how each tier controls the effect. The Stack Overflow / dev.to search intent "how do I customize Tailwind's animate-bounce" solved with a copy-paste reference. Tailwind teal palette + JetBrains Mono code snippets so users see exactly what to write.
## HTML
```html
<div class="bn-16">
  <p class="bn-16__label">Tailwind <code>animate-bounce</code> — 3 customization tiers</p>
  <div class="bn-16__grid">
    <div class="bn-16__col">
      <span class="bn-16__badge bn-16__badge--t1" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
      </span>
      <p class="bn-16__tier-title">Tier 1 · Default</p>
      <code class="bn-16__code">animate-bounce</code>
      <p class="bn-16__tier-note">Built-in utility<br/><code>-25%</code> translateY, 1s cycle</p>
    </div>
    <div class="bn-16__col">
      <span class="bn-16__badge bn-16__badge--t2" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
      </span>
      <p class="bn-16__tier-title">Tier 2 · Arbitrary</p>
      <code class="bn-16__code">animate-[bounce_2s_ease-in-out_infinite]</code>
      <p class="bn-16__tier-note">Override per-instance<br/>No config edit</p>
    </div>
    <div class="bn-16__col">
      <span class="bn-16__badge bn-16__badge--t3" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2" stroke="#0f766e" stroke-width="2.5" fill="none" stroke-linecap="round"/></svg>
      </span>
      <p class="bn-16__tier-title">Tier 3 · Custom keyframes</p>
      <code class="bn-16__code">animate-customBounce</code>
      <p class="bn-16__tier-note">Full pixel control<br/>Registered in config</p>
    </div>
  </div>
</div>
```
## CSS
```css
.bn-16 {
  --page-bg: #f0fdfa;
  --surface: #ffffff;
  --ink: #134e4a;
  --sub: #0f766e;
  --teal: #14b8a6;
  --teal-hi: #5eead4;
  --line: #ccfbf1;
  --code-bg: #134e4a;
  --code-ink: #ccfbf1;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 32px;
  padding: 32px;
  background: radial-gradient(70% 60% at 50% 20%, rgba(20,184,166,.12) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
  text-align: center;
}

.bn-16 *,
.bn-16 *::before,
.bn-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-16 ::selection {
  background: var(--teal);
  color: #fff;
}

.bn-16__label {
  font-size: .95rem;
  font-weight: 700;
  color: var(--sub);
  letter-spacing: .02em;
}

.bn-16__label code {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .85rem;
  padding: 1px 6px;
  border-radius: 5px;
  background: var(--code-bg);
  color: var(--code-ink);
}

.bn-16__grid {
  display: grid;
  grid-template-columns: repeat(3,minmax(0,220px));
  gap: 20px;
  width: 100%;
  justify-content: center;
}

@media (max-width: 720px) {
  .bn-16__grid {
    grid-template-columns: 1fr;
  }
}

.bn-16__col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  padding: 22px 16px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--surface);
  box-shadow: 0 8px 20px -8px rgba(20,184,166,.14);
}

.bn-16__badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 64px;
  height: 64px;
  border-radius: 16px;
  color: #fff;
  will-change: transform;
}

.bn-16__badge--t1 {
  background: linear-gradient(135deg,#5eead4,#14b8a6);
  animation: bn-16-t1 1s ease-in-out infinite;
}

.bn-16__badge--t2 {
  background: linear-gradient(135deg,#fb923c,#ea580c);
  animation: bn-16-t2 2s ease-in-out infinite;
}

.bn-16__badge--t3 {
  background: linear-gradient(135deg,#a78bfa,#7c3aed);
  animation: bn-16-t3 1.8s ease-in-out infinite;
}
/* Tier 1 — Tailwind's default animate-bounce keyframe */

@keyframes bn-16-t1 {
  0%,
    100% {
    transform: translateY(-25%);
    animation-timing-function: cubic-bezier(.8,0,1,1);
  }

  50% {
    transform: translateY(0);
    animation-timing-function: cubic-bezier(0,0,.2,1);
  }
}
/* Tier 2 — same keyframe, slower duration + ease-in-out */

@keyframes bn-16-t2 {
  0%,
    100% {
    transform: translateY(-25%);
  }

  50% {
    transform: translateY(0);
  }
}
/* Tier 3 — custom pixel-based keyframes for exact control */

@keyframes bn-16-t3 {
  0%,
    100% {
    transform: translateY(0);
  }

  30% {
    transform: translateY(-30px);
  }

  60% {
    transform: translateY(-10px);
  }
}

.bn-16__tier-title {
  font-size: .85rem;
  font-weight: 800;
  letter-spacing: -.005em;
  color: var(--ink);
  margin-top: 2px;
}

.bn-16__code {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .72rem;
  font-weight: 600;
  padding: 5px 9px;
  border-radius: 6px;
  background: var(--code-bg);
  color: var(--code-ink);
  word-break: break-all;
  max-width: 100%;
}

.bn-16__tier-note {
  font-size: .72rem;
  color: var(--sub);
  line-height: 1.5;
}

.bn-16__tier-note code {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .68rem;
  padding: 1px 4px;
  border-radius: 3px;
  background: var(--line);
  color: var(--sub);
}

@media (prefers-reduced-motion: reduce) {
  .bn-16__badge {
    animation: none!important;
    transform: none!important;
  }
}
```
