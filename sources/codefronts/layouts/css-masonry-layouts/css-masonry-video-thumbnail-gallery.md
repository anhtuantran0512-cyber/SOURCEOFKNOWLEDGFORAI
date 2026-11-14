---
source: "codefronts"
url: "https://codefronts.com/layouts/css-masonry-layouts/css-masonry-video-thumbnail-gallery/"
title: "CSS Masonry Video Thumbnail Gallery"
section: "layouts"
category: "css-masonry-layouts"
category_name: "CSS Masonry Layouts"
description: "A video library where landscape uploads, vertical Shorts and square clips pack into one wall — the mixed-ratio case that breaks uniform grids and justifies…"
has_js: "false"
---

Here's a working CSS Masonry Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Masonry Video Thumbnail Gallery
Source: https://codefronts.com/layouts/css-masonry-layouts/css-masonry-video-thumbnail-gallery/

A video library where landscape uploads, vertical Shorts and square clips pack into one wall — the mixed-ratio case that breaks uniform grids and justifies masonry. Duration badges, a pulsing LIVE tag, watch-progress bars, and a play glyph drawn entirely with clip-path (no icon font, no SVG sprite) that scales in on hover and focus. Ratios are declared per tile, so the layout is settled before a single poster frame loads.
## HTML
```html
<section class="msn-09" aria-label="CSS masonry video thumbnail gallery demo">
  <div class="msn-09__stage" tabindex="0">
    <header class="msn-09__head">
      <div><h2>Library</h2><p>Design engineering channel · 214 videos</p></div>
      <nav class="msn-09__chips" aria-label="Filter videos"><a href="#all" aria-current="true">All</a><a href="#uploads">Uploads</a><a href="#shorts">Shorts</a><a href="#live">Live</a></nav>
    </header>
    <div class="msn-09__wall">
      <article class="msn-09__tile"><a class="msn-09__thumb" href="#v1" data-len="18:42" style="--ar:16/9;--seen:64%;--img:url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=900&auto=format&fit=crop');--a:oklch(0.5 0.09 260);--b:oklch(0.3 0.08 280)"><span class="msn-09__play" aria-hidden="true"></span><i class="msn-09__seen" aria-hidden="true"></i></a><div class="msn-09__meta"><i style="--a:oklch(0.75 0.11 300);--b:oklch(0.5 0.13 330)"></i><div><h3><a href="#v1">Native CSS masonry in production — full migration</a></h3><a class="msn-09__ch" href="#ch1">Grid & Glory</a><span>128k views · 3 days ago</span></div></div></article>
      <article class="msn-09__tile msn-09__tile--short"><a class="msn-09__thumb" href="#v2" data-len="0:58" style="--ar:9/16;--img:url('https://images.unsplash.com/photo-1529139574466-a303027c1d8b?q=80&w=700&auto=format&fit=crop');--a:oklch(0.7 0.08 340);--b:oklch(0.45 0.1 320)"><span class="msn-09__flag">Short</span><span class="msn-09__play" aria-hidden="true"></span></a><div class="msn-09__meta msn-09__meta--bare"><div><h3><a href="#v2">break-inside: avoid in 60 seconds</a></h3><span>412k views</span></div></div></article>
      <article class="msn-09__tile"><a class="msn-09__thumb" href="#v3" data-len="42:10" style="--ar:16/9;--seen:12%;--img:url('https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=900&auto=format&fit=crop');--a:oklch(0.45 0.06 30);--b:oklch(0.28 0.06 10)"><span class="msn-09__play" aria-hidden="true"></span><i class="msn-09__seen" aria-hidden="true"></i></a><div class="msn-09__meta"><i style="--a:oklch(0.78 0.1 40);--b:oklch(0.55 0.13 20)"></i><div><h3><a href="#v3">Film study: why editors love the 12-column cut</a></h3><a class="msn-09__ch" href="#ch2">Cutting Room</a><span>96k views · 1 week ago</span></div></div></article>
      <article class="msn-09__tile"><a class="msn-09__thumb msn-09__thumb--live" href="#v4" data-len="LIVE" style="--ar:16/9;--img:url('https://images.unsplash.com/photo-1478737270239-2f02b77fc618?q=80&w=900&auto=format&fit=crop');--a:oklch(0.55 0.12 20);--b:oklch(0.35 0.1 0)"><span class="msn-09__flag msn-09__flag--live">● LIVE</span><span class="msn-09__play" aria-hidden="true"></span></a><div class="msn-09__meta"><i style="--a:oklch(0.72 0.09 220);--b:oklch(0.48 0.11 240)"></i><div><h3><a href="#v4">Office hours: bring your broken layouts</a></h3><a class="msn-09__ch" href="#ch3">Grid & Glory</a><span>1.4k watching now</span></div></div></article>
      <article class="msn-09__tile msn-09__tile--short"><a class="msn-09__thumb" href="#v5" data-len="0:41" style="--ar:9/16;--img:url('https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=700&auto=format&fit=crop');--a:oklch(0.6 0.05 250);--b:oklch(0.38 0.06 270)"><span class="msn-09__flag">Short</span><span class="msn-09__play" aria-hidden="true"></span></a><div class="msn-09__meta msn-09__meta--bare"><div><h3><a href="#v5">The :has() spotlight trick</a></h3><span>289k views</span></div></div></article>
      <article class="msn-09__tile"><a class="msn-09__thumb" href="#v6" data-len="12:05" style="--ar:1/1;--seen:100%;--img:url('https://images.unsplash.com/photo-1511512578047-dfb367046420?q=80&w=800&auto=format&fit=crop');--a:oklch(0.5 0.13 300);--b:oklch(0.3 0.11 320)"><span class="msn-09__play" aria-hidden="true"></span><i class="msn-09__seen" aria-hidden="true"></i></a><div class="msn-09__meta"><i style="--a:oklch(0.8 0.1 150);--b:oklch(0.55 0.12 170)"></i><div><h3><a href="#v6">I rebuilt a 2004 Flash site in CSS</a></h3><a class="msn-09__ch" href="#ch4">Pixel Archaeology</a><span>1.2M views · 2 weeks ago</span></div></div></article>
      <article class="msn-09__tile"><a class="msn-09__thumb" href="#v7" data-len="27:33" style="--ar:16/9;--img:url('https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=900&auto=format&fit=crop');--a:oklch(0.4 0.05 280);--b:oklch(0.25 0.05 300)"><span class="msn-09__play" aria-hidden="true"></span></a><div class="msn-09__meta"><i style="--a:oklch(0.78 0.1 40);--b:oklch(0.55 0.13 20)"></i><div><h3><a href="#v7">Projection mapping a conference stage</a></h3><a class="msn-09__ch" href="#ch2">Cutting Room</a><span>54k views · 3 weeks ago</span></div></div></article>
      <article class="msn-09__tile msn-09__tile--short"><a class="msn-09__thumb" href="#v8" data-len="0:52" style="--ar:9/16;--img:url('https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=700&auto=format&fit=crop');--a:oklch(0.75 0.07 80);--b:oklch(0.52 0.09 60)"><span class="msn-09__flag">Short</span><span class="msn-09__play" aria-hidden="true"></span></a><div class="msn-09__meta msn-09__meta--bare"><div><h3><a href="#v8">Stop nesting your media queries</a></h3><span>167k views</span></div></div></article>
      <article class="msn-09__tile"><a class="msn-09__thumb" href="#v9" data-len="15:27" style="--ar:16/9;--seen:31%;--img:url('https://images.unsplash.com/photo-1516035069371-29a1b244cc32?q=80&w=900&auto=format&fit=crop');--a:oklch(0.45 0.04 280);--b:oklch(0.28 0.05 300)"><span class="msn-09__play" aria-hidden="true"></span><i class="msn-09__seen" aria-hidden="true"></i></a><div class="msn-09__meta"><i style="--a:oklch(0.76 0.1 190);--b:oklch(0.5 0.11 210)"></i><div><h3><a href="#v9">Lens review: shooting UI b-roll that doesn't bore</a></h3><a class="msn-09__ch" href="#ch5">Studio Notes</a><span>38k views · 1 month ago</span></div></div></article>
    </div>
  </div>
</section>
```
## CSS
```css
.msn-09,
.msn-09 *,
.msn-09 *::before,
.msn-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msn-09 {
  --bg: oklch(0.16 0.01 280);
  --ink: oklch(0.95 0.008 280);
  --mut: oklch(0.63 0.015 280);
  --line: oklch(0.28 0.014 280);
  --acc: oklch(0.72 0.16 20);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.msn-09__stage {
  width: 100%;
  container: msn09/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.msn-09__head {
  position: sticky;
  top: 0;
  z-index: 2;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px 16px;
  padding: 14px clamp(16px,3cqi,26px);
  background: color-mix(in oklch,var(--bg) 82%,transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.msn-09__head h2 {
  font-size: clamp(17px,2.4cqi,22px);
  letter-spacing: -.02em;
}

.msn-09__head p {
  font-size: 11.5px;
  color: var(--mut);
  margin-top: 2px;
}

.msn-09__chips {
  display: flex;
  gap: 6px;
}

.msn-09__chips a {
  display: grid;
  place-items: center;
  min-height: 36px;
  padding: 0 13px;
  border-radius: 9px;
  font-size: 12.5px;
  font-weight: 600;
  text-decoration: none;
  color: var(--ink);
  background: oklch(0.23 0.012 280);
  transition: background .2s;
}

.msn-09__chips a:hover,
.msn-09__chips a:focus-visible {
  background: oklch(0.29 0.014 280);
}

.msn-09__chips a[aria-current] {
  background: var(--ink);
  color: var(--bg);
}

.msn-09__chips a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.msn-09__wall {
  columns: 260px;
  column-gap: 14px;
  padding: clamp(14px,3cqi,26px);
}

.msn-09__tile {
  break-inside: avoid;
  margin-bottom: 20px;
}

.msn-09__thumb {
  position: relative;
  display: block;
  aspect-ratio: var(--ar,16/9);
  border-radius: 12px;
  overflow: clip;
  background-image: var(--img,none),linear-gradient(150deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
}

.msn-09__thumb::before {
  content: "";
  position: absolute;
  inset: 0;
  background: oklch(0.1 0.01 280/.0);
  transition: background .25s;
}

.msn-09__thumb:hover::before,
.msn-09__thumb:focus-visible::before {
  background: oklch(0.1 0.01 280/.28);
}

.msn-09__thumb::after {
  content: attr(data-len);
  position: absolute;
  right: 8px;
  bottom: 8px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .03em;
  padding: 3px 7px;
  border-radius: 6px;
  background: oklch(0.12 0.01 280/.85);
  color: oklch(0.97 0 0);
}

.msn-09__thumb--live::after {
  background: var(--acc);
}

.msn-09__thumb:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.msn-09__play {
  position: absolute;
  left: 50%;
  top: 50%;
  translate: -50% -50%;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: oklch(0.98 0 0/.92);
  backdrop-filter: blur(4px);
  display: grid;
  place-items: center;
  color: oklch(0.2 0.01 280);
  scale: .6;
  opacity: 0;
  transition: scale .25s cubic-bezier(.2,.7,.2,1),opacity .25s;
}

.msn-09__play::after {
  content: "";
  width: 15px;
  height: 16px;
  margin-left: 3px;
  background: currentColor;
  clip-path: polygon(8% 0%,100% 50%,8% 100%);
}

.msn-09__thumb:hover .msn-09__play,
.msn-09__thumb:focus-visible .msn-09__play {
  scale: 1;
  opacity: 1;
}

.msn-09__seen {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 4px;
  background: linear-gradient(90deg,var(--acc) var(--seen,0%),oklch(0.95 0.008 280/.28) var(--seen,0%));
}

.msn-09__flag {
  position: absolute;
  top: 8px;
  left: 8px;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: .06em;
  padding: 4px 8px;
  border-radius: 6px;
  background: oklch(0.12 0.01 280/.78);
  backdrop-filter: blur(3px);
}

.msn-09__flag--live {
  background: var(--acc);
  animation: msn09-pulse 1.6s ease-in-out infinite;
}

@keyframes msn09-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .66;
  }
}

.msn-09__meta {
  display: flex;
  gap: 10px;
  padding: 10px 2px 0;
}

.msn-09__meta>i {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  flex: none;
  background: linear-gradient(140deg,var(--a),var(--b));
}

.msn-09__meta h3 {
  font-size: 13.5px;
  line-height: 1.4;
  letter-spacing: -.01em;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-wrap: pretty;
}

.msn-09__meta h3 a {
  color: inherit;
  text-decoration: none;
}

.msn-09__meta h3 a:hover,
.msn-09__meta h3 a:focus-visible {
  color: oklch(0.85 0.05 20);
}

.msn-09__meta h3 a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 4px;
}

.msn-09__ch {
  display: inline-block;
  margin-top: 3px;
  font-size: 11.5px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  min-height: 20px;
}

.msn-09__ch:hover,
.msn-09__ch:focus-visible {
  color: var(--ink);
}

.msn-09__ch:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 4px;
}

.msn-09__meta span {
  display: block;
  font-size: 11.5px;
  color: var(--mut);
  margin-top: 1px;
}

.msn-09__meta--bare h3 {
  -webkit-line-clamp: 2;
}

@media (hover: none) {
  .msn-09__play {
    opacity: 1;
    scale: 1;
  }
}

@container msn09 (width < 480px) {
  .msn-09__wall {
    columns: 2;
    column-gap: 8px;
  }

  .msn-09__tile {
    margin-bottom: 12px;
  }

  .msn-09__meta>i {
    display: none;
  }

  .msn-09__play {
    width: 38px;
    height: 38px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .msn-09 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
