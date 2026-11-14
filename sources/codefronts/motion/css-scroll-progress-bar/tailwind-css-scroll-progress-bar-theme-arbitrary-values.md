---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/tailwind-css-scroll-progress-bar-theme-arbitrary-values/"
title: "Tailwind CSS Scroll Progress Bar (@theme + arbitrary values)"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "Tailwind has no built-in utility for scroll-driven animations, which sends most people back to a <style> tag."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Scroll Progress Bar (@theme + arbitrary values)
Source: https://codefronts.com/motion/css-scroll-progress-bar/tailwind-css-scroll-progress-bar-theme-arbitrary-values/

Tailwind has no built-in utility for scroll-driven animations, which sends most people back to a <style> tag. It does not have to: v4's @theme and @utility directives express the whole pattern as first-class tokens, and arbitrary properties cover the rest inline. This demo ships both — the token-based utility and the pure-inline version — with the exact underscore syntax that trips everyone up.
## HTML
```html
<section class="sp-14" aria-label="Tailwind CSS scroll progress bar demo">
  <div class="sp-14__prog" role="progressbar" aria-label="Reading progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" id="sp-14-prog"><i class="sp-14__fill"></i></div>
  <header class="sp-14__bar">
    <a class="sp-14__brand" href="#sp-14-s1"><span class="sp-14__logo" aria-hidden="true"></span>tw<span class="sp-14__brandthin">/progress</span></a>
    <p class="sp-14__meta">v4 · @theme + @utility</p>
  </header>
  <div class="sp-14__intro">
    <p class="sp-14__intro-eyebrow">utility-first, not stylesheet-first</p>
    <h2 class="sp-14__intro-title">Scroll progress without leaving Tailwind</h2>
    <p class="sp-14__intro-sub">Two routes: an arbitrary property for a one-off, and a themed <code>@utility</code> for anything you ship twice.</p>
  </div>
  <main class="sp-14__main">
    <section class="sp-14__sec" id="sp-14-s1">
      <p class="sp-14__kicker">Route A</p>
      <h3 class="sp-14__h">The inline one-liner</h3>
      <p class="sp-14__p sp-14__p--lede">Arbitrary properties take any declaration in brackets — with underscores standing in for spaces.</p>
      <pre class="sp-14__code"><code>&lt;div class="fixed inset-x-0 top-0 h-1 origin-left
     bg-indigo-500
     [animation:sp-fill_linear_both]
     [animation-timeline:scroll(root_block)]"&gt;
&lt;/div&gt;</code></pre>
      <p class="sp-14__p">It works, it ships nothing extra, and it is unreadable the second time you meet it.</p>
    </section>
    <section class="sp-14__sec" id="sp-14-s2">
      <p class="sp-14__kicker">Route B</p>
      <h3 class="sp-14__h">Tokens, then a utility</h3>
      <p class="sp-14__p">In v4 the config is CSS. <code>@theme</code> publishes tokens as utilities; <code>@utility</code> registers a class that composes with every variant.</p>
      <pre class="sp-14__code"><code>@import "tailwindcss";

@theme {
  --color-progress: oklch(0.62 0.21 265);
  --animate-scroll-fill: sp-fill linear both;
}
@keyframes sp-fill {
  from { transform: scaleX(0) }
  to   { transform: scaleX(1) }
}

@utility scroll-progress {
  transform-origin: left center;
  animation: var(--animate-scroll-fill);
  animation-timeline: scroll(root block);
}</code></pre>
      <p class="sp-14__p">The markup becomes <code>class="scroll-progress bg-progress fixed inset-x-0 top-0 h-1"</code>.</p>
    </section>
    <section class="sp-14__sec" id="sp-14-s3">
      <p class="sp-14__kicker">Variants</p>
      <h3 class="sp-14__h">Feature queries as a variant</h3>
      <p class="sp-14__p">Register <code>@custom-variant supports-scroll-timeline</code> once and progressive enhancement becomes a prefix like any other, sitting beside <code>md:</code> and <code>motion-reduce:</code>.</p>
    </section>
    <section class="sp-14__sec" id="sp-14-s4">
      <p class="sp-14__kicker">Traps</p>
      <h3 class="sp-14__h">Underscores and the scanner</h3>
      <p class="sp-14__p">A space inside brackets produces no class at all, and a class name built at runtime is never generated — the JIT reads your source as text, not as a program.</p>
      <p class="sp-14__chip">0 stylesheet escapes · 1 utility · every variant</p>
    </section>
  </main>
  <footer class="sp-14__pagefoot"><p class="sp-14__pagefootin">Scroll progress pattern 14 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-14-bg);
  --sp-14-bg: oklch(0.145 0.02 265);
  --sp-14-surface: oklch(0.2 0.025 265);
  --sp-14-ink: oklch(0.97 0.005 265);
  --sp-14-mut: oklch(0.72 0.02 265);
  --sp-14-acc: oklch(0.72 0.15 210);
  --sp-14-acc2: oklch(0.62 0.21 265);
  --sp-14-line: oklch(1 0 0/.12);
  --sp-14-p: 0;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-14-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-14 *,
.sp-14 *::before,
.sp-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-14__prog {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: 4px;
  z-index: 60;
  background: oklch(1 0 0/.08);
  pointer-events: none;
}

.sp-14__fill {
  display: block;
  block-size: 100%;
  transform-origin: left center;
  transform: scaleX(var(--sp-14-p));
  background: linear-gradient(90deg,var(--sp-14-acc),var(--sp-14-acc2));
}

@supports (animation-timeline: scroll()) {
  .sp-14__fill {
    transform: scaleX(0);
    animation: sp-14-fill linear both;
    animation-timeline: scroll(root block);
  }
}

@keyframes sp-14-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

.sp-14__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 58px;
  padding-block-start: 4px;
  background: color-mix(in oklch,var(--sp-14-bg) 76%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-block-end: 1px solid var(--sp-14-line);
}

.sp-14__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: inherit;
  text-decoration: none;
}

.sp-14__brandthin {
  color: var(--sp-14-mut);
  font-weight: 400;
}

.sp-14__brand:focus-visible {
  outline: 2px solid var(--sp-14-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.sp-14__logo {
  inline-size: 18px;
  block-size: 18px;
  border-radius: 5px;
  background: linear-gradient(140deg,var(--sp-14-acc),var(--sp-14-acc2));
}

.sp-14__meta {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  color: var(--sp-14-mut);
}

.sp-14__intro {
  display: grid;
  gap: 14px;
  padding-block: clamp(46px,10vh,116px) clamp(24px,5vh,52px);
  background: radial-gradient(80% 50% at 30% 0%,oklch(0.26 0.09 250),transparent);
}

.sp-14__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sp-14-acc);
}

.sp-14__intro-title {
  font-size: clamp(32px,5.8vw,68px);
  line-height: .99;
  letter-spacing: -.04em;
  font-weight: 730;
  max-inline-size: 17ch;
  text-wrap: balance;
}

.sp-14__intro-sub {
  font-size: clamp(14.5px,1.6vw,18px);
  line-height: 1.55;
  color: var(--sp-14-mut);
  max-inline-size: 54ch;
  text-wrap: pretty;
}

.sp-14__intro-sub code,
.sp-14__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.1);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-14__sec {
  scroll-margin-top: 74px;
  display: grid;
  gap: 13px;
  align-content: center;
  min-block-size: 74svh;
  padding-block: clamp(26px,5vw,52px);
  border-block-end: 1px solid var(--sp-14-line);
}

.sp-14__sec:last-child {
  border-block-end: 0;
}

.sp-14__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sp-14-acc);
}

.sp-14__h {
  font-size: clamp(22px,3.1vw,33px);
  line-height: 1.1;
  letter-spacing: -.032em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-14__p {
  max-inline-size: 60ch;
  font-size: 15.6px;
  line-height: 1.7;
  color: var(--sp-14-mut);
  text-wrap: pretty;
}

.sp-14__p--lede {
  font-size: 17.6px;
  color: var(--sp-14-ink);
}

.sp-14__code {
  max-inline-size: 64ch;
  padding: 16px 18px;
  border: 1px solid var(--sp-14-line);
  border-radius: 14px;
  background: oklch(0.18 0.022 265);
  overflow-x: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12.8px;
  line-height: 1.62;
  color: oklch(0.86 0.04 200);
  white-space: pre;
  -webkit-overflow-scrolling: touch;
}

.sp-14__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-14-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-14-acc) 14%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-14-acc) 30%,transparent);
}

.sp-14__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(40px,8vh,100px) 24px;
  border-block-start: 1px solid var(--sp-14-line);
}

.sp-14__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-14-mut);
  text-align: center;
}

.sp-14__bar,
.sp-14__intro,
.sp-14__sec {
  padding-inline: max(clamp(18px,4vw,36px),calc((100% - 920px)/2));
}

:root:has(.sp-14) {
  scroll-behavior: smooth;
  scroll-padding-top: 74px;
}

@media (max-width: 640px) {
  .sp-14__sec {
    min-block-size: auto;
  }

  .sp-14__code {
    font-size: 11.6px;
  }
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sp-14) {
    scroll-behavior: auto;
  }

  .sp-14 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-14');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const prog = root.querySelector('#sp-14-prog');
  const native = CSS.supports('animation-timeline', 'scroll()');
  let ticking = false;
  const paint = () => {
    ticking = false;
    const d = document.documentElement;
    const max = d.scrollHeight - d.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, d.scrollTop / max)) : 0;
    if (!native) root.style.setProperty('--sp-14-p', p.toFixed(4));
    prog.setAttribute('aria-valuenow', String(Math.round(p * 100)));
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  paint();
})();
```
