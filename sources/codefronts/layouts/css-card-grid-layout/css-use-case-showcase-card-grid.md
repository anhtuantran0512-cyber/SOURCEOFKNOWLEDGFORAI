---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-use-case-showcase-card-grid/"
title: "CSS Use-Case Showcase Card Grid"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "A 2x2 showcase grid where each card is a real, fully-rendered page archetype inside a browser-chrome frame — a Photo Gallery with rated photos and a…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Use-Case Showcase Card Grid
Source: https://codefronts.com/layouts/css-card-grid-layout/css-use-case-showcase-card-grid/

A 2x2 showcase grid where each card is a real, fully-rendered page archetype inside a browser-chrome frame — a Photo Gallery with rated photos and a carousel, a Contact Page with labelled form fields and a map, a 5-column Product Grid with prices, and a 4-column Team Grid with avatars and roles — drawn entirely with CSS divs and inline SVG so users can copy-paste any archetype directly into their project.
## HTML
```html
<div class="cg-09">
  <div class="cg-09__grid">

    <article class="cg-09__card">
      <div class="cg-09__win">
        <div class="cg-09__chrome">
          <span class="cg-09__dot"></span><span class="cg-09__dot"></span><span class="cg-09__dot"></span>
          <span class="cg-09__urlbar">photos.app / albums</span>
          <span class="cg-09__menu">⋯</span>
        </div>
        <div class="cg-09__body cg-09__body--gallery">
          <div class="cg-09__galleryhead">
            <span class="cg-09__pagetitle">Albums</span>
            <span class="cg-09__filter">All ▾</span>
          </div>
          <div class="cg-09__carousel">
            <span class="cg-09__arrow">‹</span>
            <div class="cg-09__photo cg-09__photo--main"><span class="cg-09__caption">Iceland · 2026</span></div>
            <span class="cg-09__arrow">›</span>
          </div>
          <div class="cg-09__thumbs">
            <span class="cg-09__thumb cg-09__thumb--1"></span>
            <span class="cg-09__thumb cg-09__thumb--2"></span>
            <span class="cg-09__thumb cg-09__thumb--3 is-active"></span>
            <span class="cg-09__thumb cg-09__thumb--4"></span>
            <span class="cg-09__thumb cg-09__thumb--5"></span>
          </div>
        </div>
      </div>
      <p class="cg-09__label">Gallery</p>
    </article>

    <article class="cg-09__card">
      <div class="cg-09__win">
        <div class="cg-09__chrome">
          <span class="cg-09__dot"></span><span class="cg-09__dot"></span><span class="cg-09__dot"></span>
          <span class="cg-09__urlbar">acme.co / contact</span>
          <span class="cg-09__menu">⋯</span>
        </div>
        <div class="cg-09__body cg-09__body--contact">
          <span class="cg-09__pagetitle">Get in touch</span>
          <div class="cg-09__contactrow">
            <div class="cg-09__form">
              <label class="cg-09__field"><span>Name</span><b>Sarah Patel</b></label>
              <label class="cg-09__field"><span>Email</span><b>[email protected]</b></label>
              <label class="cg-09__field cg-09__field--ta"><span>Message</span><b>Hi team, I'd love a demo…</b></label>
              <span class="cg-09__sendbtn">Send →</span>
            </div>
            <div class="cg-09__map">
              <svg viewBox="0 0 60 60" width="100%" height="100%" preserveAspectRatio="none">
                <rect width="60" height="60" fill="#dde6ef"/>
                <path d="M0 20 L60 16" stroke="#fff" stroke-width="2" fill="none"/>
                <path d="M0 36 L60 32" stroke="#fff" stroke-width="2" fill="none"/>
                <path d="M14 0 L18 60" stroke="#fff" stroke-width="2" fill="none"/>
                <path d="M42 0 L46 60" stroke="#fff" stroke-width="2" fill="none"/>
                <rect x="20" y="22" width="14" height="10" fill="#c0cbd8"/>
                <circle cx="34" cy="34" r="6" fill="#ef4444"/>
                <circle cx="34" cy="34" r="2" fill="#fff"/>
              </svg>
            </div>
          </div>
        </div>
      </div>
      <p class="cg-09__label">Contact Page</p>
    </article>

    <article class="cg-09__card">
      <div class="cg-09__win">
        <div class="cg-09__chrome">
          <span class="cg-09__dot"></span><span class="cg-09__dot"></span><span class="cg-09__dot"></span>
          <span class="cg-09__urlbar">shop.co / products</span>
          <span class="cg-09__menu">⋯</span>
        </div>
        <div class="cg-09__body cg-09__body--cols">
          <span class="cg-09__pagetitle">Shop · 247 items</span>
          <div class="cg-09__cols cg-09__cols--5">
            <span class="cg-09__prod cg-09__prod--1"><b>$32</b></span>
            <span class="cg-09__prod cg-09__prod--2"><b>$48</b></span>
            <span class="cg-09__prod cg-09__prod--3"><b>$19</b></span>
            <span class="cg-09__prod cg-09__prod--4"><b>$74</b></span>
            <span class="cg-09__prod cg-09__prod--5"><b>$58</b></span>
            <span class="cg-09__prod cg-09__prod--6"><b>$24</b></span>
            <span class="cg-09__prod cg-09__prod--7"><b>$96</b></span>
            <span class="cg-09__prod cg-09__prod--8"><b>$12</b></span>
            <span class="cg-09__prod cg-09__prod--9"><b>$45</b></span>
            <span class="cg-09__prod cg-09__prod--10"><b>$67</b></span>
          </div>
        </div>
      </div>
      <p class="cg-09__label">5 Column Grid</p>
    </article>

    <article class="cg-09__card">
      <div class="cg-09__win">
        <div class="cg-09__chrome">
          <span class="cg-09__dot"></span><span class="cg-09__dot"></span><span class="cg-09__dot"></span>
          <span class="cg-09__urlbar">acme.co / team</span>
          <span class="cg-09__menu">⋯</span>
        </div>
        <div class="cg-09__body cg-09__body--cols">
          <span class="cg-09__pagetitle">Meet the team</span>
          <div class="cg-09__cols cg-09__cols--4">
            <span class="cg-09__person cg-09__person--1"><i></i><em>Maya · CEO</em></span>
            <span class="cg-09__person cg-09__person--2"><i></i><em>Liam · CTO</em></span>
            <span class="cg-09__person cg-09__person--3"><i></i><em>Aria · Design</em></span>
            <span class="cg-09__person cg-09__person--4"><i></i><em>Noah · Eng</em></span>
            <span class="cg-09__person cg-09__person--5"><i></i><em>Zoe · Ops</em></span>
            <span class="cg-09__person cg-09__person--6"><i></i><em>Sam · Sales</em></span>
            <span class="cg-09__person cg-09__person--7"><i></i><em>Ivy · CS</em></span>
            <span class="cg-09__person cg-09__person--8"><i></i><em>Kai · Eng</em></span>
          </div>
        </div>
      </div>
      <p class="cg-09__label">4 Column Grid</p>
    </article>

  </div>
</div>
```
## CSS
```css
.cg-09,
.cg-09 *,
.cg-09 *::before,
.cg-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-09 ::selection {
  background: #3b82f6;
  color: #fff;
}

.cg-09 {
  --bg: #2a3450;
  --chrome: #3b9bd9;
  --tile: #f4f6fa;
  --line: #dde1ea;
  --ink: #1f2942;
  min-height: 100vh;
  background: var(--bg);
  padding: 24px 36px;
  font-family: "Inter",-apple-system,sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cg-09__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 18px 36px;
  width: 100%;
  max-width: 760px;
}

.cg-09__card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  transition: transform .35s cubic-bezier(.4,.2,.2,1);
}

.cg-09__card:hover {
  transform: translateY(-6px);
}

.cg-09__win {
  width: 100%;
  aspect-ratio: 16/10;
  background: #f4f6fa;
  border-radius: 6px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  box-shadow: 0 8px 22px rgba(0,0,0,.25);
}

.cg-09__chrome {
  height: 28px;
  flex-shrink: 0;
  background: var(--chrome);
  display: flex;
  align-items: center;
  padding: 0 10px;
  gap: 5px;
  position: relative;
}

.cg-09__dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: rgba(255,255,255,.55);
  transition: background .3s;
}

.cg-09__card:hover .cg-09__dot {
  background: rgba(255,255,255,.95);
}

.cg-09__urlbar {
  background: rgba(255,255,255,.92);
  color: #5b6478;
  font-size: .52rem;
  padding: 3px 10px;
  border-radius: 10px;
  margin-left: 8px;
  flex: 1;
  max-width: 60%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-weight: 600;
}

.cg-09__menu {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  color: rgba(255,255,255,.9);
  font-size: .85rem;
  font-weight: 700;
  line-height: 1;
}

.cg-09__body {
  flex: 1;
  padding: 10px 12px;
  display: flex;
  flex-direction: column;
  gap: 7px;
  background: #fff;
  min-height: 0;
}

.cg-09__pagetitle {
  font-size: .62rem;
  font-weight: 700;
  color: var(--ink);
}

.cg-09__label {
  color: #e6e8ef;
  font-size: .92rem;
  font-weight: 500;
  letter-spacing: .01em;
}
/* Gallery body */

.cg-09__galleryhead {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cg-09__filter {
  font-size: .5rem;
  color: #5b6478;
  font-weight: 600;
}

.cg-09__carousel {
  flex: 1;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  min-height: 0;
}

.cg-09__photo {
  flex: 1;
  height: 100%;
  border-radius: 4px;
  position: relative;
  display: flex;
  align-items: flex-end;
  padding: 6px 8px;
}

.cg-09__photo--main {
  background: linear-gradient(180deg,rgba(0,0,0,0) 60%,rgba(0,0,0,.42)), linear-gradient(135deg,#5b8fd9 0%,#3c5f9a 50%,#1f3866 100%);
}

.cg-09__caption {
  color: #fff;
  font-size: .5rem;
  font-weight: 700;
  letter-spacing: .04em;
  text-shadow: 0 1px 2px rgba(0,0,0,.4);
}

.cg-09__arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  color: #fff;
  font-size: 1rem;
  font-weight: 300;
  padding: 0 6px;
  line-height: 1;
  background: rgba(0,0,0,.28);
  width: 16px;
  height: 16px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1;
}

.cg-09__arrow:first-of-type {
  left: 6px;
}

.cg-09__arrow:last-of-type {
  right: 6px;
}

.cg-09__thumbs {
  display: flex;
  gap: 4px;
  height: 18%;
  flex-shrink: 0;
}

.cg-09__thumb {
  flex: 1;
  border-radius: 2px;
  border: 1.5px solid transparent;
  transition: border-color .25s;
}

.cg-09__thumb.is-active {
  border-color: #5b8fd9;
}

.cg-09__thumb--1 {
  background: linear-gradient(135deg,#86b58a,#3d7a4a);
}

.cg-09__thumb--2 {
  background: linear-gradient(135deg,#e8b08a,#a85d3d);
}

.cg-09__thumb--3 {
  background: linear-gradient(135deg,#5b8fd9,#1f3866);
}

.cg-09__thumb--4 {
  background: linear-gradient(135deg,#d987a8,#7a3855);
}

.cg-09__thumb--5 {
  background: linear-gradient(135deg,#c4b88a,#7a6a3d);
}
/* Contact body */

.cg-09__body--contact {
  padding: 10px 12px;
}

.cg-09__contactrow {
  flex: 1;
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 8px;
  min-height: 0;
}

.cg-09__form {
  display: flex;
  flex-direction: column;
  gap: 5px;
  font-size: .45rem;
}

.cg-09__field {
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.cg-09__field span {
  color: #8a92a3;
  font-size: .42rem;
  font-weight: 600;
  letter-spacing: .04em;
}

.cg-09__field b {
  display: block;
  background: #eef1f6;
  border: 1px solid #dde1ea;
  border-radius: 2px;
  padding: 3px 5px;
  color: var(--ink);
  font-size: .46rem;
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cg-09__field--ta b {
  padding-bottom: 8px;
}

.cg-09__sendbtn {
  align-self: flex-start;
  background: var(--ink);
  color: #fff;
  font-size: .46rem;
  font-weight: 700;
  padding: 4px 8px;
  border-radius: 3px;
  margin-top: 2px;
}

.cg-09__map {
  border-radius: 3px;
  overflow: hidden;
}

.cg-09__map svg {
  display: block;
  width: 100%;
  height: 100%;
}
/* Cols bodies */

.cg-09__body--cols {
  padding: 10px 12px;
}

.cg-09__body--cols .cg-09__cols {
  flex: 1;
  display: grid;
  gap: 5px;
  min-height: 0;
}

.cg-09__cols--5 {
  grid-template-columns: repeat(5,1fr);
  grid-template-rows: repeat(2,1fr);
}

.cg-09__cols--4 {
  grid-template-columns: repeat(4,1fr);
  grid-template-rows: repeat(2,1fr);
}
/* Product tiles (5-col) */

.cg-09__prod {
  background: #eef1f6;
  border-radius: 3px;
  position: relative;
  display: flex;
  align-items: flex-end;
  justify-content: flex-end;
  padding: 3px 4px;
  overflow: hidden;
}

.cg-09__prod b {
  font-size: .42rem;
  font-weight: 800;
  color: #fff;
  background: rgba(0,0,0,.55);
  padding: 1px 3px;
  border-radius: 2px;
}

.cg-09__prod--1 {
  background: linear-gradient(135deg,#f7b88a,#d97f4f);
}

.cg-09__prod--2 {
  background: linear-gradient(135deg,#a7c8e7,#5b8fd9);
}

.cg-09__prod--3 {
  background: linear-gradient(135deg,#c5da9c,#7aa852);
}

.cg-09__prod--4 {
  background: linear-gradient(135deg,#f9c1cf,#d97a99);
}

.cg-09__prod--5 {
  background: linear-gradient(135deg,#c4b5fd,#9b87e5);
}

.cg-09__prod--6 {
  background: linear-gradient(135deg,#fef0a3,#e6c54a);
}

.cg-09__prod--7 {
  background: linear-gradient(135deg,#86b58a,#3d7a4a);
}

.cg-09__prod--8 {
  background: linear-gradient(135deg,#e8b08a,#a85d3d);
}

.cg-09__prod--9 {
  background: linear-gradient(135deg,#5b8fd9,#1f3866);
}

.cg-09__prod--10 {
  background: linear-gradient(135deg,#d987a8,#7a3855);
}
/* Person tiles (4-col) */

.cg-09__person {
  background: #fff;
  border: 1px solid #dde1ea;
  border-radius: 3px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
  padding: 4px 2px;
  overflow: hidden;
}

.cg-09__person i {
  display: block;
  width: 54%;
  aspect-ratio: 1;
  border-radius: 50%;
}

.cg-09__person em {
  font-size: .4rem;
  font-weight: 600;
  color: var(--ink);
  font-style: normal;
  text-align: center;
  line-height: 1.1;
}

.cg-09__person--1 i {
  background: linear-gradient(135deg,#f9c1cf,#d97a99);
}

.cg-09__person--2 i {
  background: linear-gradient(135deg,#a7c8e7,#5b8fd9);
}

.cg-09__person--3 i {
  background: linear-gradient(135deg,#c5da9c,#7aa852);
}

.cg-09__person--4 i {
  background: linear-gradient(135deg,#f7b88a,#d97f4f);
}

.cg-09__person--5 i {
  background: linear-gradient(135deg,#c4b5fd,#9b87e5);
}

.cg-09__person--6 i {
  background: linear-gradient(135deg,#86b58a,#3d7a4a);
}

.cg-09__person--7 i {
  background: linear-gradient(135deg,#fef0a3,#e6c54a);
}

.cg-09__person--8 i {
  background: linear-gradient(135deg,#e8b08a,#a85d3d);
}

@media (max-width: 640px) {
  .cg-09__grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }

  .cg-09 {
    padding: 32px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cg-09__card,
    .cg-09__dot,
    .cg-09__thumb {
    transition: none;
  }
}
```
