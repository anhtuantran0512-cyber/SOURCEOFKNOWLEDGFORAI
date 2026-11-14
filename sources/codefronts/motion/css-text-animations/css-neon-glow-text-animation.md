---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-neon-glow-text-animation/"
title: "CSS Glowing Neon Sign Text Flicker Animation"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Believable neon, not just text-shadow spam: a script cocktail sign on brick where one letter buzzes with irregular dropout while the rest of the tube hums,…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glowing Neon Sign Text Flicker Animation
Source: https://codefronts.com/motion/css-text-animations/css-neon-glow-text-animation/

Believable neon, not just text-shadow spam: a script cocktail sign on brick where one letter buzzes with irregular dropout while the rest of the tube hums, and a power-on sequence where a two-tone diner sign ignites word by word and settles into a steady glow.
## HTML
```html
<div class="cat-21-group">
<link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
<section class="cat-21a" aria-label="Neon cocktail sign with flickering letter">
  <div class="cat-21a__wall">
    <h1 class="cat-21a__sign" aria-label="Open Late"><span>Open&nbsp;La</span><span class="cat-21a__dying">t</span><span>e</span></h1>
    <p class="cat-21a__tag" aria-hidden="true">COCKTAILS · VINYL · UNTIL 4AM</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500..900;1,500..900&display=swap" rel="stylesheet">
<section class="cat-21b" aria-label="Neon diner sign powering on">
  <div class="cat-21b__frame">
    <h1 class="cat-21b__sign"><span class="cat-21b__word cat-21b__word--pink" style="--i:0">NEON</span> <span class="cat-21b__word cat-21b__word--cyan" style="--i:1">DINER</span></h1>
    <p class="cat-21b__sub" aria-hidden="true">each word ignites, stutters, then holds steady</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-21-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-21-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-21a,
.cat-21a *,
.cat-21a *::before,
.cat-21a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-21a {
  --pink: #ff5fd2;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #140d10;
  background-image: repeating-linear-gradient(0deg,rgba(255,255,255,.035) 0 2px,transparent 2px 26px),repeating-linear-gradient(90deg,rgba(255,255,255,.025) 0 2px,transparent 2px 58px),radial-gradient(120% 90% at 50% 10%,#241318,#12090d 70%);
}

.cat-21a__wall {
  text-align: center;
  padding: 60px 40px;
  border-radius: 20px;
  background: radial-gradient(80% 70% at 50% 35%,rgba(255,95,210,.08),transparent 70%);
}

.cat-21a__sign {
  font-family: 'Pacifico',cursive;
  font-weight: 400;
  font-size: clamp(52px,9.5vw,120px);
  color: #ffe9fa;
  text-shadow: 0 0 4px #fff,0 0 11px var(--pink),0 0 26px var(--pink),0 0 58px color-mix(in oklab,var(--pink) 80%,transparent),0 0 110px color-mix(in oklab,var(--pink) 55%,transparent);
  animation: cat-21a-hum 3.4s ease-in-out infinite;
}

.cat-21a__dying {
  display: inline-block;
  animation: cat-21a-buzz 4.2s linear infinite;
}

.cat-21a__tag {
  margin-top: 26px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .42em;
  color: rgba(255,210,240,.5);
}

@keyframes cat-21a-hum {
  0%,
    100% {
    filter: brightness(1);
  }

  50% {
    filter: brightness(1.13);
  }
}

@keyframes cat-21a-buzz {
  0%,
    6.8%,
    7.4%,
    30%,
    31.4%,
    52%,
    53.5%,
    79%,
    82%,
    100% {
    opacity: 1;
    color: #ffe9fa;
    text-shadow: inherit;
  }

  7%,
    31%,
    52.6%,
    80%,
    81% {
    opacity: .28;
    color: rgba(255,180,225,.35);
    text-shadow: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-21a__sign,
    .cat-21a__dying {
    animation: none;
  }
}

.cat-21b,
.cat-21b *,
.cat-21b *::before,
.cat-21b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-21b {
  --pink: #ff4fa8;
  --cyan: #2ee6ff;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(110% 90% at 50% 8%,#101622,#080b12 72%);
}

.cat-21b__frame {
  text-align: center;
  padding: 56px clamp(28px,7vw,90px);
  border: 2px solid rgba(255,255,255,.07);
  border-radius: 26px;
  box-shadow: inset 0 0 60px rgb(0 0 0/.6);
}

.cat-21b__sign {
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
  font-size: clamp(46px,9vw,110px);
  font-weight: 900;
  letter-spacing: .06em;
  line-height: 1.1;
}

.cat-21b__word {
  display: inline-block;
  animation: cat-21b-on 2.6s cubic-bezier(.3,.7,.3,1) calc(var(--i)*1.1s + .3s) both;
}

.cat-21b__word--pink {
  --c: var(--pink);
  color: #ffe6f3;
}

.cat-21b__word--cyan {
  --c: var(--cyan);
  color: #e3fbff;
}

.cat-21b__sub {
  margin-top: 24px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .2em;
  color: rgba(200,220,240,.4);
}

@keyframes cat-21b-on {
  0%,
    14% {
    color: rgba(255,255,255,.16);
    text-shadow: none;
  }

  15%,
    17% {
    color: inherit;
    text-shadow: 0 0 4px #fff,0 0 14px var(--c);
  }

  18%,
    26% {
    color: rgba(255,255,255,.16);
    text-shadow: none;
  }

  27%,
    34% {
    color: inherit;
    text-shadow: 0 0 4px #fff,0 0 14px var(--c);
  }

  35%,
    39% {
    color: rgba(255,255,255,.2);
    text-shadow: none;
  }

  40%,
    100% {
    color: inherit;
    text-shadow: 0 0 5px #fff,0 0 13px var(--c),0 0 30px var(--c),0 0 64px color-mix(in oklab,var(--c) 75%,transparent);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-21b__word {
    animation: cat-21b-steady .4s ease both;
  }
}

@keyframes cat-21b-steady {
  to {
    text-shadow: 0 0 5px #fff,0 0 13px var(--c),0 0 30px var(--c);
  }
}
```

## JavaScript
```js
/* No JavaScript — a five-layer text-shadow builds the tube glow; one letter span runs an irregular-percentage dropout keyframe like a dying tube while the sign hums. */

/* No JavaScript — a single power-on keyframe (dark → stutter → steady glow) plays per word, offset 1.1s apart via --i; reduced motion jumps straight to steady. */
```
