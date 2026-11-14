---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/morph-triangle/"
title: "CSS Play Button Icon Morph Animation"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "True path morphing — the play triangle's vertices slide into the pause bars — using the CSS d property, which lets you transition an SVG path's geometry the…"
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Play Button Icon Morph Animation
Source: https://codefronts.com/components/css-play-pause-buttons/morph-triangle/

True path morphing — the play triangle's vertices slide into the pause bars — using the CSS d property, which lets you transition an SVG path's geometry the same way you transition a color. No GreenSock, no Flubber, no JS. Browsers without d interpolation get a tasteful rotate-and-crossfade instead, gated behind an @supports query, so the component degrades instead of breaking.
## HTML
```html
<section class="pp-08" aria-label="SVG path morph play pause icon demo">
  <div class="pp-08__stage">
    <div class="pp-08__wrap">
      <input class="pp-08-chk" type="checkbox" id="pp-08-toggle" aria-label="Play or pause">
      <label class="pp-08__btn" for="pp-08-toggle">
        <svg class="pp-08__icon" viewBox="0 0 24 24" width="46" height="46" aria-hidden="true">
          <path class="pp-08__morph" fill="currentColor"/>
          <g class="pp-08__fallback">
            <path class="pp-08__p" d="M8.5 5.5L18 12L8.5 18.5Z" fill="currentColor"/>
            <path class="pp-08__q" d="M8 5.5h3v13H8zM13 5.5h3v13h-3z" fill="currentColor"/>
          </g>
        </svg>
      </label>
      <p class="pp-08__cap">Vertices travel<span>d:path() interpolation</span></p>
    </div>
    <p class="pp-08__chip" aria-hidden="true">CSS d property · matched vertex counts · @supports fallback</p>
  </div>
</section>
```
## CSS
```css
.pp-08,
.pp-08 *,
.pp-08 *::before,
.pp-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-08-bg);
  --pp-08-bg: oklch(0.98 0.005 95);
  --pp-08-ink: oklch(0.22 0.02 95);
  --pp-08-mut: oklch(0.55 0.02 95);
  --pp-08-acc: oklch(0.63 0.19 32);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-08-ink);
}

.pp-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(70% 55% at 50% 0%,oklch(0.94 0.04 60/.7),transparent 70%);
}

.pp-08__wrap {
  display: grid;
  justify-items: center;
  gap: 22px;
}

.pp-08-chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-08__btn {
  display: grid;
  place-items: center;
  width: 132px;
  height: 132px;
  border-radius: 38px;
  background: var(--pp-08-ink);
  color: var(--pp-08-bg);
  cursor: pointer;
  box-shadow: 0 18px 44px oklch(0.3 0.05 60/.25);
  transition: border-radius .5s cubic-bezier(.65,0,.35,1),background .35s,transform .25s;
}

.pp-08__btn:hover {
  transform: translateY(-3px);
}

.pp-08-chk:checked+.pp-08__btn {
  border-radius: 50%;
  background: var(--pp-08-acc);
}

.pp-08-chk:focus-visible+.pp-08__btn {
  outline: 3px solid var(--pp-08-acc);
  outline-offset: 5px;
}

.pp-08__morph {
  d: path("M8 5.5L12 7.8L12 16.2L8 18.5Z M12 7.8L17.5 12L17.5 12L12 16.2Z");
  transition: d .45s cubic-bezier(.65,0,.35,1);
}

.pp-08-chk:checked+.pp-08__btn .pp-08__morph {
  d: path("M8 5.5L11 5.5L11 18.5L8 18.5Z M13 5.5L16 5.5L16 18.5L13 18.5Z");
}

.pp-08__fallback {
  display: none;
}

@supports not (d: path("M0 0Z")) {
  .pp-08__morph {
    display: none;
  }

  .pp-08__fallback {
    display: block;
  }

  .pp-08__p,
    .pp-08__q {
    transform-origin: 12px 12px;
    transition: opacity .32s,rotate .42s cubic-bezier(.65,0,.35,1),scale .42s;
  }

  .pp-08__q {
    opacity: 0;
    rotate: -20deg;
    scale: .8;
  }

  .pp-08-chk:checked+.pp-08__btn .pp-08__p {
    opacity: 0;
    rotate: 20deg;
    scale: .8;
  }

  .pp-08-chk:checked+.pp-08__btn .pp-08__q {
    opacity: 1;
    rotate: 0deg;
    scale: 1;
  }
}

.pp-08__cap {
  text-align: center;
  font-size: 15px;
  font-weight: 640;
}

.pp-08__cap span {
  display: block;
  margin-top: 4px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  font-weight: 400;
  color: var(--pp-08-mut);
}

.pp-08__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-08-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0.22 0.02 95/.16);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-08 * {
    transition-duration: .01ms !important;
  }
}
```
