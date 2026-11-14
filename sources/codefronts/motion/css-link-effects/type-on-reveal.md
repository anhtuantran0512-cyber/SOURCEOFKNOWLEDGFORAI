---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/type-on-reveal/"
title: "CSS Typewriter / Type-On Link Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Typing without JavaScript: steps() easing plus ch units — one step per character, one ch per character, monospace makes them equal."
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter / Type-On Link Hover Effect
Source: https://codefronts.com/motion/css-link-effects/type-on-reveal/

Typing without JavaScript: steps() easing plus ch units — one step per character, one ch per character, monospace makes them equal. Hover a link and it types an extra clause after itself, caret blinking at the live edge; or watch it backspace 'Projects' and retype 'Selected work'; or decrypt a proportional-font phrase in chunky clip-path blocks. The math is the tutorial.
## HTML
```html
<section class="cle-26" aria-label="Typewriter hover demo">
  <div class="cle-26__stage">
    <div class="cle-26__var"><a href="#a" class="cle-26__type">Contact<span class="cle-26__added" aria-hidden="true"> — say hi</span></a><small class="cle-26__cap">A · types a suffix</small></div>
    <div class="cle-26__var"><a href="#b" class="cle-26__retype"><span class="cle-26__old">Projects</span><span class="cle-26__new" aria-hidden="true">Selected work</span><span class="cle-26__edge" aria-hidden="true"></span></a><small class="cle-26__cap">B · backspace, retype</small></div>
    <div class="cle-26__var"><a href="#c" class="cle-26__chunk" data-text="Decrypt the archive">Decrypt the archive</a><small class="cle-26__cap">C · chunked reveal (any font)</small></div>
  </div>
</section>
```
## CSS
```css
.cle-26,
.cle-26 *,
.cle-26 *::before,
.cle-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-26 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.3 0.02 250);
  --accent: oklch(0.52 0.17 250);
  font-family: ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;
}

.cle-26__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 46px;
  border: 1px solid oklch(0.9 0.012 250);
  background: linear-gradient(175deg,oklch(0.985 0.005 250),oklch(0.95 0.012 250));
  padding: 44px 32px;
}

.cle-26__var {
  display: grid;
  gap: 13px;
  justify-items: center;
}

.cle-26__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.03 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-26 a {
  color: var(--ink);
  text-decoration: none;
  font-size: clamp(20px,2.8vw,26px);
  font-weight: 600;
  transition: color .3s;
}

.cle-26 a:hover,
.cle-26 a:focus-visible {
  color: var(--accent);
}

.cle-26 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 6px;
  border-radius: 3px;
}

.cle-26__added {
  display: inline-block;
  overflow: hidden;
  vertical-align: bottom;
  white-space: pre;
  width: 0;
  color: var(--accent);
  border-right: 2px solid transparent;
}

.cle-26__type:hover .cle-26__added,
.cle-26__type:focus-visible .cle-26__added {
  animation: clh26-typeA .7s steps(9) forwards,clh26-caret 1s steps(1) infinite;
}

@keyframes clh26-typeA {
  to {
    width: 9ch;
  }
}

@keyframes clh26-caret {
  0%,
    49% {
    border-right-color: var(--accent);
  }

  50%,
    100% {
    border-right-color: transparent;
  }
}

.cle-26__retype .cle-26__old,
.cle-26__retype .cle-26__new {
  display: inline-block;
  overflow: hidden;
  vertical-align: bottom;
  white-space: pre;
}

.cle-26__retype .cle-26__old {
  width: 8ch;
}

.cle-26__retype .cle-26__new {
  width: 0;
  color: var(--accent);
}

.cle-26__retype .cle-26__edge {
  display: inline-block;
  vertical-align: bottom;
  width: 2px;
  height: 1.15em;
  background: transparent;
}

.cle-26__retype:hover .cle-26__old,
.cle-26__retype:focus-visible .cle-26__old {
  animation: clh26-del .35s steps(8) forwards;
}

.cle-26__retype:hover .cle-26__new,
.cle-26__retype:focus-visible .cle-26__new {
  animation: clh26-typeB .5s steps(13) .45s forwards;
}

.cle-26__retype:hover .cle-26__edge,
.cle-26__retype:focus-visible .cle-26__edge {
  animation: clh26-edge 1s steps(1) infinite;
}

@keyframes clh26-del {
  to {
    width: 0;
  }
}

@keyframes clh26-typeB {
  to {
    width: 13ch;
  }
}

@keyframes clh26-edge {
  0%,
    49% {
    background: var(--accent);
  }

  50%,
    100% {
    background: transparent;
  }
}

.cle-26__chunk {
  position: relative;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-weight: 800;
  letter-spacing: -.01em;
}

.cle-26__chunk::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  color: var(--accent);
  clip-path: inset(0 100% 0 0);
  transition: clip-path .6s steps(12,end);
}

.cle-26__chunk:hover::after,
.cle-26__chunk:focus-visible::after {
  clip-path: inset(0 0 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cle-26 * {
    animation: none !important;
    transition-duration: .01s !important;
  }

  .cle-26__type:hover .cle-26__added {
    width: 9ch;
  }

  .cle-26__retype:hover .cle-26__old {
    width: 0;
  }

  .cle-26__retype:hover .cle-26__new {
    width: 13ch;
  }
}
```
