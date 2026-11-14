---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/cursor-blink-underline/"
title: "CSS Blinking Cursor Underline Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Terminal-native link affordances for dev tools, docs and portfolio sites: a block caret that starts blinking beside the link on hover, an underline that…"
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Blinking Cursor Underline Hover Effect
Source: https://codefronts.com/motion/css-link-effects/cursor-blink-underline/

Terminal-native link affordances for dev tools, docs and portfolio sites: a block caret that starts blinking beside the link on hover, an underline that types itself in discrete steps before the caret appears at its end, and a prompt chevron that slides in like a fresh shell line. Blinks use steps(1) — the authentic square-wave flicker, not a fade.
## HTML
```html
<section class="cle-12" aria-label="Blinking cursor link demo">
  <div class="cle-12__stage">
    <div class="cle-12__screen" role="presentation">
      <p class="cle-12__line"><span class="cle-12__dim">visitor@codefronts:~$</span> ls ./guides</p>
      <ul class="cle-12__list">
        <li><a href="#a" class="cle-12__caret">deploy-checklist.md</a><small class="cle-12__cap">A · block caret blinks</small></li>
        <li><a href="#b" class="cle-12__typed">shell-profiles.md</a><small class="cle-12__cap">B · underline types, then blinks</small></li>
        <li><a href="#c" class="cle-12__prompt"><span class="cle-12__chev" aria-hidden="true">›</span>ssh-hardening.md</a><small class="cle-12__cap">C · prompt slides in</small></li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
.cle-12,
.cle-12 *,
.cle-12 *::before,
.cle-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-12 {
  width: 100%;
  min-height: 100vh;
  --term: oklch(0.85 0.19 150);
  --dim: oklch(0.62 0.06 150);
  font-family: ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;
}

.cle-12__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
  background: radial-gradient(120% 130% at 50% 0%,oklch(0.23 0.03 155),oklch(0.16 0.02 160) 65%);
  padding: 44px 32px;
}

.cle-12__screen {
  width: min(560px,100%);
  border-radius: 14px;
  border: 1px solid oklch(0.4 0.05 150 / .5);
  background: oklch(0.13 0.015 160 / .85);
  padding: 28px 30px;
  box-shadow: 0 30px 60px -30px oklch(0 0 0 / .6),inset 0 1px 0 oklch(0.5 0.06 150 / .25);
}

.cle-12__line {
  color: var(--term);
  font-size: 14.5px;
  margin-bottom: 20px;
}

.cle-12__dim {
  color: var(--dim);
}

.cle-12__list {
  list-style: none;
  display: grid;
  gap: 18px;
}

.cle-12__list li {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 18px;
  flex-wrap: wrap;
}

.cle-12__cap {
  font-size: 10px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-12 a {
  color: oklch(0.9 0.06 150);
  text-decoration: none;
  font-size: 16px;
  transition: color .2s;
}

.cle-12 a:hover,
.cle-12 a:focus-visible {
  color: var(--term);
}

.cle-12 a:focus-visible {
  outline: 1.5px solid var(--term);
  outline-offset: 4px;
}

.cle-12 a::selection {
  background: oklch(0.85 0.19 150 / .35);
}

.cle-12__caret::after {
  content: "";
  display: inline-block;
  width: .55ch;
  height: 1.05em;
  margin-left: .35ch;
  vertical-align: text-bottom;
  background: var(--term);
  opacity: 0;
}

.cle-12__caret:hover::after,
.cle-12__caret:focus-visible::after {
  animation: clh12-blink 1.1s steps(1) infinite;
}

.cle-12__typed {
  padding-bottom: 5px;
  background: linear-gradient(var(--term),var(--term)) no-repeat left bottom / 0% 2px;
  transition: background-size .4s steps(10,end);
}

.cle-12__typed:hover,
.cle-12__typed:focus-visible {
  background-size: 100% 2px;
}

.cle-12__typed::after {
  content: "";
  display: inline-block;
  width: .55ch;
  height: 1.05em;
  margin-left: .35ch;
  vertical-align: text-bottom;
  background: var(--term);
  opacity: 0;
}

.cle-12__typed:hover::after,
.cle-12__typed:focus-visible::after {
  animation: clh12-blink 1.1s steps(1) .4s infinite;
}

.cle-12__prompt .cle-12__chev {
  display: inline-block;
  width: 0;
  overflow: hidden;
  color: var(--term);
  translate: -8px 0;
  opacity: 0;
  transition: width .3s,translate .3s cubic-bezier(.3,1.3,.4,1),opacity .25s;
  vertical-align: baseline;
}

.cle-12__prompt:hover .cle-12__chev,
.cle-12__prompt:focus-visible .cle-12__chev {
  width: 1.4ch;
  translate: 0 0;
  opacity: 1;
}

@keyframes clh12-blink {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cle-12 * {
    transition-duration: .01s !important;
    animation: none !important;
  }

  .cle-12__caret:hover::after,
    .cle-12__typed:hover::after {
    opacity: 1;
  }
}
```
