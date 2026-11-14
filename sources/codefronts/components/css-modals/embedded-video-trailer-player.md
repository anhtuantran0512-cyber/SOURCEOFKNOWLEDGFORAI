---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/embedded-video-trailer-player/"
title: "Embedded Video / Trailer Player"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A responsive modal that holds an aspect-ratio-locked player for a YouTube / Vimeo / HTML5 trailer, and blanks the source on close so audio stops instantly —…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Embedded Video / Trailer Player
Source: https://codefronts.com/components/css-modals/embedded-video-trailer-player/

A responsive modal that holds an aspect-ratio-locked player for a YouTube / Vimeo / HTML5 trailer, and blanks the source on close so audio stops instantly — the click-to-play video overlay done without layout shift.
## HTML
```html
<div class="cm-10">
  <button class="cm-10__open" type="button"><span aria-hidden="true">▶</span> Watch trailer</button>

  <dialog class="cm-10__dlg" aria-labelledby="cm-10-title">
    <div class="cm-10__card">
      <div class="cm-10__bar">
        <h2 id="cm-10-title" class="cm-10__t">Official Trailer — “Nightfall”</h2>
        <button class="cm-10__x" type="button" aria-label="Close player">&times;</button>
      </div>
      <div class="cm-10__frame">
        <!-- Ship this: an aspect-ratio-locked iframe whose src you set on open / clear on close
        <iframe class="cm-10__video" title="Official Trailer — Nightfall"
          data-src="https://www.youtube-nocookie.com/embed/VIDEO_ID?rel=0"
          allow="accelerated-encoding; autoplay; encrypted-media; fullscreen"
          allowfullscreen></iframe> -->
        <div class="cm-10__poster" aria-hidden="true">
          <div class="cm-10__play"><span>▶</span></div>
          <span class="cm-10__phlabel">16:9 player · your &lt;iframe&gt; here</span>
        </div>
      </div>
    </div>
  </dialog>
</div>
```
## CSS
```css
.cm-10,
.cm-10 *,
.cm-10 *::before,
.cm-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-10 {
  --accent: oklch(0.66 0.2 15);
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#120e10,#080607);
}

.cm-10__open {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  cursor: pointer;
  padding: 13px 26px;
  border-radius: 11px;
  color: #fdeef0;
  font: 600 15px system-ui;
  border: 1px solid color-mix(in oklch,var(--accent) 45%,#33242a);
  background: color-mix(in oklch,var(--accent) 14%,#140e10);
  transition: background .2s,border-color .2s;
}

.cm-10__open:hover {
  border-color: var(--accent);
  background: color-mix(in oklch,var(--accent) 22%,#140e10);
}

.cm-10__open:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-10__dlg {
  margin: auto;
  width: min(780px,94vw);
  padding: 0;
  border: none;
  border-radius: 16px;
  overflow: hidden;
  color: #f0e9eb;
  background: #0c0809;
  box-shadow: 0 40px 90px -30px #000,0 0 0 1px #2a1e22;
  opacity: 0;
  transform: scale(.96);
  transition: opacity .28s,transform .28s,overlay .28s allow-discrete,display .28s allow-discrete;
}

.cm-10__dlg[open] {
  opacity: 1;
  transform: none;
}

@starting-style {
  .cm-10__dlg[open] {
    opacity: 0;
    transform: scale(.96);
  }
}

.cm-10__dlg::backdrop {
  background: rgba(4,3,3,0);
  backdrop-filter: blur(0);
  transition: background .3s,backdrop-filter .3s,overlay .3s allow-discrete,display .3s allow-discrete;
}

.cm-10__dlg[open]::backdrop {
  background: rgba(4,3,3,.72);
  backdrop-filter: blur(6px);
}

@starting-style {
  .cm-10__dlg[open]::backdrop {
    background: rgba(4,3,3,0);
    backdrop-filter: blur(0);
  }
}

.cm-10__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 16px;
  background: #120c0e;
}

.cm-10__t {
  font-size: 15px;
  font-weight: 600;
  color: #f4ecee;
}

.cm-10__x {
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #a98a90;
  font-size: 22px;
  cursor: pointer;
}

.cm-10__x:hover {
  background: #241a1d;
  color: #fff;
}

.cm-10__x:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-10__frame {
  aspect-ratio: 16/9;
  position: relative;
  background: #000;
}

.cm-10__video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

.cm-10__poster {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  background: radial-gradient(120% 120% at 50% 40%,#241318,#0a0608);
}

.cm-10__play {
  width: 76px;
  height: 76px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: color-mix(in oklch,var(--accent) 88%,#fff);
  color: #1a0a0d;
  font-size: 26px;
  padding-left: 5px;
  box-shadow: 0 0 50px -6px var(--accent);
  animation: cm-10-pulse 2.4s ease-in-out infinite;
}

@keyframes cm-10-pulse {
  0%,
    100% {
    transform: scale(1);
  }

  50% {
    transform: scale(1.06);
  }
}

.cm-10__phlabel {
  font: 12px ui-monospace,monospace;
  letter-spacing: .14em;
  color: #8a6b71;
}

@media (prefers-reduced-motion: reduce) {
  .cm-10__dlg,
    .cm-10__dlg::backdrop {
    transition-duration: .001s;
  }

  .cm-10__play {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-10');
  var dlg = root.querySelector('.cm-10__dlg');
  var video = root.querySelector('.cm-10__video'); // present in production markup
  root.querySelector('.cm-10__open').addEventListener('click', function(){
    if(video && video.dataset.src) video.src = video.dataset.src; // start
    dlg.showModal();
  });
  root.querySelector('.cm-10__x').addEventListener('click', function(){ dlg.close(); });
  dlg.addEventListener('close', function(){ if(video) video.src = ''; }); // stop playback
  dlg.addEventListener('click', function(e){
    var c = dlg.querySelector('.cm-10__card').getBoundingClientRect();
    if(e.clientX < c.left || e.clientX > c.right || e.clientY < c.top || e.clientY > c.bottom) dlg.close();
  });
})();
```
