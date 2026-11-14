---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/tailwind-neon-text-glow-utility/"
title: "Tailwind Neon Text-Glow Utility"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "The Tailwind answer: a reusable neon-glow utility built with arbitrary text-shadow values and a tokenised drop-shadow scale, shown as the exact class string…"
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Text-Glow Utility
Source: https://codefronts.com/motion/css-neon-text-effect/tailwind-neon-text-glow-utility/

The Tailwind answer: a reusable neon-glow utility built with arbitrary text-shadow values and a tokenised drop-shadow scale, shown as the exact class string devs paste into a utility-first project — no custom CSS file needed.
## HTML
```html
<div class="cnt-16">
  <div class="cnt-16__card">
    <h2 class="cnt-16__h">text-neon</h2>
    <code class="cnt-16__code">&lt;h2 class="text-cyan-400
  <span class="cnt-16__hl">[text-shadow:_0_0_6px_#fff,0_0_18px_theme(colors.cyan.400),0_0_44px_theme(colors.cyan.500)]</span>
  hover:[text-shadow:_0_0_8px_#fff,0_0_28px_#22d3ee,0_0_70px_#0891b2]"&gt;</code>
  </div>
</div>
```
## CSS
```css
.cnt-16,
.cnt-16 *,
.cnt-16 *::before,
.cnt-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-16 ::selection {
  background: oklch(0.85 0.14 200);
  color: #03131a;
}

.cnt-16 {
  --accent: oklch(0.85 0.14 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 20px;
  background: radial-gradient(120% 120% at 50% 20%,#0a0f12,#050708);
}

.cnt-16__card {
  width: min(600px,94vw);
  padding: 44px;
  border-radius: 16px;
  text-align: center;
  background: #0a0e11;
  border: 1px solid #16232a;
}

.cnt-16__h {
  font-size: clamp(44px,10vw,84px);
  font-weight: 900;
  letter-spacing: .02em;
  color: #eafcff;
  cursor: default;
  text-shadow: 0 0 6px #fff,0 0 18px var(--accent),0 0 44px var(--accent);
  transition: text-shadow .3s;
}

.cnt-16__h:hover {
  text-shadow: 0 0 8px #fff,0 0 28px var(--accent),0 0 70px color-mix(in oklch,var(--accent) 70%,transparent);
}

.cnt-16__code {
  display: block;
  margin-top: 30px;
  padding: 18px 20px;
  border-radius: 10px;
  text-align: left;
  font: 12.5px/1.7 ui-monospace,Menlo,monospace;
  color: #7f93a0;
  background: #060a0c;
  border: 1px solid #142027;
  white-space: pre-wrap;
  word-break: break-word;
}

.cnt-16__hl {
  color: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .cnt-16__h {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — rendered Tailwind output; the annotation shows the source class. */
```
