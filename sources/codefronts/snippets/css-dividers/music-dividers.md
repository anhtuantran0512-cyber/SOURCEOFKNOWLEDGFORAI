---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/music-dividers/"
title: "Audio Waveform SVG Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "A waveform divider for podcast and music pages, built as flex bars rather than an SVG path — which means every bar is an element you can animate, colour and…"
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Audio Waveform SVG Divider CSS
Source: https://codefronts.com/snippets/css-dividers/music-dividers/

A waveform divider for podcast and music pages, built as flex bars rather than an SVG path — which means every bar is an element you can animate, colour and stagger independently. Heights come from a hand-tuned array so the shape reads as real audio (asymmetric, with quiet passages), and a played/unplayed split shows the progress-bar pattern the pattern is actually used for.
## HTML
```html
<section class="div-23" aria-label="Audio waveform divider demo">
  <div class="div-23__stage">
    <div class="div-23__card">
      <div class="div-23__row">
        <span class="div-23__art" aria-hidden="true"></span>
        <span class="div-23__meta"><b>Episode 26 — Dividing Lines</b><br>Codefronts Radio · 41 min</span>
      </div>
      <div class="div-23__wave" aria-hidden="true">
        <span class="div-23__bar" style="--div-23-h:22%;--div-23-i:0"></span><span class="div-23__bar" style="--div-23-h:44%;--div-23-i:1"></span><span class="div-23__bar" style="--div-23-h:70%;--div-23-i:2"></span><span class="div-23__bar" style="--div-23-h:96%;--div-23-i:3"></span><span class="div-23__bar" style="--div-23-h:62%;--div-23-i:4"></span><span class="div-23__bar" style="--div-23-h:36%;--div-23-i:5"></span><span class="div-23__bar" style="--div-23-h:52%;--div-23-i:6"></span><span class="div-23__bar" style="--div-23-h:84%;--div-23-i:7"></span><span class="div-23__bar" style="--div-23-h:58%;--div-23-i:8"></span><span class="div-23__bar" style="--div-23-h:28%;--div-23-i:9"></span><span class="div-23__bar" style="--div-23-h:18%;--div-23-i:10"></span><span class="div-23__bar" style="--div-23-h:40%;--div-23-i:11"></span><span class="div-23__bar" style="--div-23-h:76%;--div-23-i:12"></span><span class="div-23__bar" style="--div-23-h:100%;--div-23-i:13"></span><span class="div-23__bar" style="--div-23-h:66%;--div-23-i:14"></span><span class="div-23__bar" style="--div-23-h:34%;--div-23-i:15"></span><span class="div-23__bar" style="--div-23-h:48%;--div-23-i:16"></span><span class="div-23__bar" style="--div-23-h:80%;--div-23-i:17"></span><span class="div-23__bar" style="--div-23-h:54%;--div-23-i:18"></span><span class="div-23__bar" style="--div-23-h:24%;--div-23-i:19"></span><span class="div-23__bar" style="--div-23-h:42%;--div-23-i:20"></span><span class="div-23__bar" style="--div-23-h:88%;--div-23-i:21"></span><span class="div-23__bar" style="--div-23-h:60%;--div-23-i:22"></span><span class="div-23__bar" style="--div-23-h:30%;--div-23-i:23"></span><span class="div-23__bar" style="--div-23-h:16%;--div-23-i:24"></span><span class="div-23__bar" style="--div-23-h:46%;--div-23-i:25"></span><span class="div-23__bar" style="--div-23-h:72%;--div-23-i:26"></span><span class="div-23__bar" style="--div-23-h:92%;--div-23-i:27"></span><span class="div-23__bar" style="--div-23-h:56%;--div-23-i:28"></span><span class="div-23__bar" style="--div-23-h:26%;--div-23-i:29"></span>
      </div>
      <div class="div-23__time"><span>17:42</span><span>41:03</span></div>
    </div>
    <p class="div-23__chip">--h per bar · calc(--i × -.07s) stagger · scaleY not height</p>
  </div>
</section>
```
## CSS
```css
.div-23 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-23-bg);
  --div-23-bg: oklch(0.16 0.024 300);
  --div-23-card: oklch(0.21 0.03 300);
  --div-23-ink: oklch(0.95 0.01 300);
  --div-23-mut: oklch(0.65 0.03 300);
  --div-23-acc: oklch(0.55 0.09 300);
  --div-23-hot: oklch(0.78 0.17 340);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-23-ink);
}

.div-23 *,
.div-23 *::before,
.div-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-23__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 20px;
  padding: clamp(24px,5vw,60px) clamp(20px,5vw,56px);
  background: radial-gradient(80% 60% at 50% 100%,oklch(0.3 0.09 330/.55),transparent);
}

.div-23__card {
  width: min(94vw,640px);
  background: var(--div-23-card);
  border: 1px solid oklch(1 0 0/.09);
  border-radius: 20px;
  padding: clamp(20px,4vw,30px);
  box-shadow: 0 26px 60px oklch(0 0 0/.45);
  display: grid;
  gap: 18px;
}

.div-23__row {
  display: flex;
  align-items: center;
  gap: 14px;
}

.div-23__art {
  width: 52px;
  height: 52px;
  flex: none;
  border-radius: 12px;
  background: linear-gradient(140deg,var(--div-23-hot),oklch(0.5 0.15 285)),url("https://images.unsplash.com/photo-1478737270239-2f02b77fc618?q=80&w=400&auto=format&fit=crop") center/cover no-repeat;
  background-blend-mode: soft-light,normal;
}

.div-23__meta {
  font-size: 13px;
  line-height: 1.5;
  color: var(--div-23-mut);
}

.div-23__meta b {
  color: var(--div-23-ink);
  font-size: 14.5px;
  font-weight: 650;
}

.div-23__wave {
  display: flex;
  align-items: center;
  gap: 3px;
  height: clamp(54px,9vw,76px);
  -webkit-mask: linear-gradient(90deg,#0000,#000 4%,#000 96%,#0000);
  mask: linear-gradient(90deg,#0000,#000 4%,#000 96%,#0000);
}

.div-23__bar {
  flex: 1 1 0;
  height: var(--div-23-h);
  min-height: 4px;
  border-radius: 99px;
  background: var(--div-23-acc);
  transform-origin: 50% 50%;
  animation: div-23-eq 1.5s ease-in-out infinite;
  animation-delay: calc(var(--div-23-i) * -.07s);
}

.div-23__bar:nth-child(-n+13) {
  background: var(--div-23-hot);
  box-shadow: 0 0 12px oklch(0.78 0.17 340/.35);
}

@keyframes div-23-eq {
  0%,
    100% {
    scale: 1 .82;
  }

  50% {
    scale: 1 1.14;
  }
}

.div-23__time {
  display: flex;
  justify-content: space-between;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--div-23-mut);
  font-variant-numeric: tabular-nums;
}

.div-23__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-23-mut);
  padding: 8px 14px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
  max-width: 94vw;
}

@media (prefers-reduced-motion: reduce) {
  .div-23__bar {
    animation: none;
    scale: 1 1;
  }
}
```
