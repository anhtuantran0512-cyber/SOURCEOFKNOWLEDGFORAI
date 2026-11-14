---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-square-grid-items/"
title: "CSS Aspect Ratio Square Grid Items"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "The Instagram-shaped grid: auto-fill columns from CSS Grid, aspect-ratio: 1 on every tile, object-fit: cover on every photo."
has_js: "false"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio Square Grid Items
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-square-grid-items/

The Instagram-shaped grid: auto-fill columns from CSS Grid, aspect-ratio: 1 on every tile, object-fit: cover on every photo. No fixed heights, no JavaScript measuring, no cropping scripts — squares at 2 columns, squares at 8. A photographer profile with a 2×2 featured tile (still a perfect square, because the unit cells are), hover overlays that also fire on keyboard focus, and a scroll-driven reveal that browsers without view() timelines simply skip.
## HTML
```html
<section class="car-03" aria-label="Square grid items demo">
  <div class="car-03__stage" id="car03-top">
    <header class="car-03__profile">
      <img class="car-03__avatar" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=200&h=200&auto=format&fit=crop" width="200" height="200" alt="Profile photo of Lena Marsh">
      <div class="car-03__who">
        <h1>lena.marsh</h1>
        <p class="car-03__tag">Landscape photographer — every tile below is <code>aspect-ratio: 1</code></p>
        <dl class="car-03__stats">
          <div><dt>214</dt><dd>posts</dd></div>
          <div><dt>18.3k</dt><dd>followers</dd></div>
          <div><dt>402</dt><dd>following</dd></div>
        </dl>
      </div>
      <a class="car-03__follow" href="#car03-top">Follow</a>
    </header>
    <nav class="car-03__tabs" aria-label="Profile sections">
      <a href="#car03-grid" aria-current="page"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M4 4h7v7H4zm9 0h7v7h-7zM4 13h7v7H4zm9 0h7v7h-7z" fill="currentColor"/></svg>Grid</a>
      <a href="#car03-grid"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M5 4h14v16H5zM9 4v16M15 4v16" fill="none" stroke="currentColor" stroke-width="2"/></svg>Reels</a>
      <a href="#car03-grid"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><circle cx="12" cy="9" r="3.4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M5 20a7 7 0 0 1 14 0" fill="none" stroke="currentColor" stroke-width="2"/></svg>Tagged</a>
    </nav>
    <div class="car-03__grid" id="car03-grid">
      <a class="car-03__tile car-03__tile--feature" href="#car03-top"><img src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=900&h=900&auto=format&fit=crop" width="900" height="900" loading="lazy" alt="Snowy ridgeline at dawn"><span class="car-03__hud"><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20.5C5 15 3 11.5 3 8.6 3 6 5 4 7.5 4c1.8 0 3.4 1 4.5 2.6C13.1 5 14.7 4 16.5 4 19 4 21 6 21 8.6c0 2.9-2 6.4-9 11.9z" fill="currentColor"/></svg>2,418</b><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2-3a8 8 0 1 1 15-5z" fill="currentColor"/></svg>96</b></span></a>
      <a class="car-03__tile" href="#car03-top"><img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=600&h=600&auto=format&fit=crop" width="600" height="600" loading="lazy" alt="Sunlit forest road"><span class="car-03__hud"><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20.5C5 15 3 11.5 3 8.6 3 6 5 4 7.5 4c1.8 0 3.4 1 4.5 2.6C13.1 5 14.7 4 16.5 4 19 4 21 6 21 8.6c0 2.9-2 6.4-9 11.9z" fill="currentColor"/></svg>931</b><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2-3a8 8 0 1 1 15-5z" fill="currentColor"/></svg>41</b></span></a>
      <a class="car-03__tile" href="#car03-top"><img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=600&h=600&auto=format&fit=crop" width="600" height="600" loading="lazy" alt="Fog over foothills"><span class="car-03__hud"><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20.5C5 15 3 11.5 3 8.6 3 6 5 4 7.5 4c1.8 0 3.4 1 4.5 2.6C13.1 5 14.7 4 16.5 4 19 4 21 6 21 8.6c0 2.9-2 6.4-9 11.9z" fill="currentColor"/></svg>1,204</b><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2-3a8 8 0 1 1 15-5z" fill="currentColor"/></svg>67</b></span></a>
      <a class="car-03__tile" href="#car03-top"><img src="https://images.unsplash.com/photo-1433086966358-54859d0ed716?q=80&w=600&h=600&auto=format&fit=crop" width="600" height="600" loading="lazy" alt="Waterfall in a green gorge"><span class="car-03__hud"><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20.5C5 15 3 11.5 3 8.6 3 6 5 4 7.5 4c1.8 0 3.4 1 4.5 2.6C13.1 5 14.7 4 16.5 4 19 4 21 6 21 8.6c0 2.9-2 6.4-9 11.9z" fill="currentColor"/></svg>856</b><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2-3a8 8 0 1 1 15-5z" fill="currentColor"/></svg>23</b></span></a>
      <a class="car-03__tile" href="#car03-top"><img src="https://images.unsplash.com/photo-1501785888041-af3ef285b470?q=80&w=600&h=600&auto=format&fit=crop" width="600" height="600" loading="lazy" alt="Lake at golden hour"><span class="car-03__hud"><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20.5C5 15 3 11.5 3 8.6 3 6 5 4 7.5 4c1.8 0 3.4 1 4.5 2.6C13.1 5 14.7 4 16.5 4 19 4 21 6 21 8.6c0 2.9-2 6.4-9 11.9z" fill="currentColor"/></svg>2,010</b><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2-3a8 8 0 1 1 15-5z" fill="currentColor"/></svg>88</b></span></a>
      <a class="car-03__tile" href="#car03-top"><img src="https://images.unsplash.com/photo-1472214103451-9374bd1c798e?q=80&w=600&h=600&auto=format&fit=crop" width="600" height="600" loading="lazy" alt="Field under big sky"><span class="car-03__hud"><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20.5C5 15 3 11.5 3 8.6 3 6 5 4 7.5 4c1.8 0 3.4 1 4.5 2.6C13.1 5 14.7 4 16.5 4 19 4 21 6 21 8.6c0 2.9-2 6.4-9 11.9z" fill="currentColor"/></svg>644</b><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2-3a8 8 0 1 1 15-5z" fill="currentColor"/></svg>19</b></span></a>
      <a class="car-03__tile" href="#car03-top"><img src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=600&h=600&auto=format&fit=crop" width="600" height="600" loading="lazy" alt="Empty beach and surf"><span class="car-03__hud"><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20.5C5 15 3 11.5 3 8.6 3 6 5 4 7.5 4c1.8 0 3.4 1 4.5 2.6C13.1 5 14.7 4 16.5 4 19 4 21 6 21 8.6c0 2.9-2 6.4-9 11.9z" fill="currentColor"/></svg>1,377</b><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2-3a8 8 0 1 1 15-5z" fill="currentColor"/></svg>52</b></span></a>
      <a class="car-03__tile" href="#car03-top"><img src="https://images.unsplash.com/photo-1507608616759-54f48f0af0ee?q=80&w=600&h=600&auto=format&fit=crop" width="600" height="600" loading="lazy" alt="Milky Way over silhouettes"><span class="car-03__hud"><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20.5C5 15 3 11.5 3 8.6 3 6 5 4 7.5 4c1.8 0 3.4 1 4.5 2.6C13.1 5 14.7 4 16.5 4 19 4 21 6 21 8.6c0 2.9-2 6.4-9 11.9z" fill="currentColor"/></svg>3,591</b><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2-3a8 8 0 1 1 15-5z" fill="currentColor"/></svg>140</b></span></a>
      <a class="car-03__tile" href="#car03-top"><img src="https://images.unsplash.com/photo-1418065460487-3e41a6c84dc5?q=80&w=600&h=600&auto=format&fit=crop" width="600" height="600" loading="lazy" alt="Snow dusted evergreens"><span class="car-03__hud"><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20.5C5 15 3 11.5 3 8.6 3 6 5 4 7.5 4c1.8 0 3.4 1 4.5 2.6C13.1 5 14.7 4 16.5 4 19 4 21 6 21 8.6c0 2.9-2 6.4-9 11.9z" fill="currentColor"/></svg>722</b><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2-3a8 8 0 1 1 15-5z" fill="currentColor"/></svg>31</b></span></a>
      <a class="car-03__tile" href="#car03-top"><img src="https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&w=600&h=600&auto=format&fit=crop" width="600" height="600" loading="lazy" alt="Sunbeams through canopy"><span class="car-03__hud"><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20.5C5 15 3 11.5 3 8.6 3 6 5 4 7.5 4c1.8 0 3.4 1 4.5 2.6C13.1 5 14.7 4 16.5 4 19 4 21 6 21 8.6c0 2.9-2 6.4-9 11.9z" fill="currentColor"/></svg>1,845</b><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2-3a8 8 0 1 1 15-5z" fill="currentColor"/></svg>74</b></span></a>
      <a class="car-03__tile" href="#car03-top"><img src="https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?q=80&w=600&h=600&auto=format&fit=crop" width="600" height="600" loading="lazy" alt="Mossy forest path"><span class="car-03__hud"><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20.5C5 15 3 11.5 3 8.6 3 6 5 4 7.5 4c1.8 0 3.4 1 4.5 2.6C13.1 5 14.7 4 16.5 4 19 4 21 6 21 8.6c0 2.9-2 6.4-9 11.9z" fill="currentColor"/></svg>598</b><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2-3a8 8 0 1 1 15-5z" fill="currentColor"/></svg>17</b></span></a>
      <a class="car-03__tile" href="#car03-top"><img src="https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=600&h=600&auto=format&fit=crop" width="600" height="600" loading="lazy" alt="Violet nebula"><span class="car-03__hud"><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20.5C5 15 3 11.5 3 8.6 3 6 5 4 7.5 4c1.8 0 3.4 1 4.5 2.6C13.1 5 14.7 4 16.5 4 19 4 21 6 21 8.6c0 2.9-2 6.4-9 11.9z" fill="currentColor"/></svg>2,933</b><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2-3a8 8 0 1 1 15-5z" fill="currentColor"/></svg>112</b></span></a>
      <a class="car-03__tile" href="#car03-top"><img src="https://images.unsplash.com/photo-1519046904884-53103b34b206?q=80&w=600&h=600&auto=format&fit=crop" width="600" height="600" loading="lazy" alt="Umbrella on a bright beach"><span class="car-03__hud"><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20.5C5 15 3 11.5 3 8.6 3 6 5 4 7.5 4c1.8 0 3.4 1 4.5 2.6C13.1 5 14.7 4 16.5 4 19 4 21 6 21 8.6c0 2.9-2 6.4-9 11.9z" fill="currentColor"/></svg>1,066</b><b><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M21 12a8 8 0 0 1-8 8H4l2-3a8 8 0 1 1 15-5z" fill="currentColor"/></svg>45</b></span></a>
    </div>
    <footer class="car-03__foot">Grid: <code>repeat(auto-fill, minmax(min(150px,100%), 1fr))</code> · tiles: <code>aspect-ratio:1</code> · photos: <code>object-fit:cover</code>. The 2×2 feature stays square because the unit cells are. A demo from the CodeFronts aspect-ratio collection.</footer>
  </div>
</section>
```
## CSS
```css
.car-03,
.car-03 *,
.car-03 *::before,
.car-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-03 {
  --bg: oklch(0.985 0.003 250);
  --ink: oklch(0.22 0.02 260);
  --mut: oklch(0.52 0.015 260);
  --line: oklch(0.91 0.008 255);
  --acc: oklch(0.55 0.19 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-03__stage {
  width: 100%;
  container: car03/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.car-03__profile {
  display: flex;
  align-items: center;
  gap: clamp(16px,3.5cqi,32px);
  padding: clamp(20px,4cqi,36px) clamp(16px,4cqi,40px) 18px;
  max-width: 1080px;
  margin-inline: auto;
}

.car-03__avatar {
  width: clamp(72px,11cqi,104px);
  height: auto;
  aspect-ratio: 1;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid var(--bg);
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.car-03__who {
  min-width: 0;
  flex: 1;
}

.car-03__who h1 {
  font-size: clamp(19px,3cqi,24px);
  letter-spacing: -.02em;
  font-weight: 800;
}

.car-03__tag {
  font-size: 12.5px;
  color: var(--mut);
  margin-top: 3px;
}

.car-03__tag code,
.car-03__foot code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.93 0.01 300);
  padding: 1px 5px;
  border-radius: 5px;
  color: oklch(0.42 0.16 300);
}

.car-03__stats {
  display: flex;
  gap: clamp(14px,3cqi,28px);
  margin-top: 10px;
}

.car-03__stats dt {
  font-size: 15px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  display: inline;
}

.car-03__stats dd {
  display: inline;
  font-size: 12.5px;
  color: var(--mut);
  margin-left: 4px;
}

.car-03__follow {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 22px;
  border-radius: 12px;
  background: var(--acc);
  color: oklch(0.99 0 0);
  font-size: 13.5px;
  font-weight: 700;
  text-decoration: none;
  transition: background .2s,translate .2s;
}

.car-03__follow:hover,
.car-03__follow:focus-visible {
  background: color-mix(in oklch,var(--acc) 85%,black);
  translate: 0 -1px;
}

.car-03__follow:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.car-03__tabs {
  display: flex;
  gap: 2px;
  justify-content: center;
  border-top: 1px solid var(--line);
  max-width: 1080px;
  margin-inline: auto;
  padding: 0 clamp(8px,2cqi,16px);
}

.car-03__tabs a {
  display: flex;
  align-items: center;
  gap: 7px;
  min-height: 46px;
  padding: 0 16px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--mut);
  text-decoration: none;
  border-top: 2px solid transparent;
  margin-top: -1px;
  transition: color .2s;
}

.car-03__tabs a:hover,
.car-03__tabs a:focus-visible {
  color: var(--ink);
}

.car-03__tabs a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.car-03__tabs a[aria-current] {
  color: var(--ink);
  border-top-color: var(--ink);
}

.car-03__grid {
  display: grid;
  gap: 4px;
  grid-template-columns: repeat(auto-fill,minmax(min(150px,100%),1fr));
  max-width: 1080px;
  margin-inline: auto;
  padding: 4px clamp(4px,1cqi,12px);
}

.car-03__tile {
  position: relative;
  display: block;
  aspect-ratio: 1;
  overflow: hidden;
  border-radius: 4px;
  background: linear-gradient(140deg,oklch(0.88 0.03 300),oklch(0.82 0.04 250));
}

.car-03__tile--feature {
  grid-column: span 2;
  grid-row: span 2;
}

.car-03__tile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: scale .5s cubic-bezier(.2,.7,.2,1);
}

.car-03__tile:hover img,
.car-03__tile:focus-visible img {
  scale: 1.06;
}

.car-03__tile:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: -3px;
}

.car-03__hud {
  position: absolute;
  inset: 0;
  display: flex;
  gap: 18px;
  align-items: center;
  justify-content: center;
  background: oklch(0.2 0.03 300/.45);
  color: oklch(0.99 0 0);
  opacity: 0;
  transition: opacity .25s;
}

.car-03__hud b {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.car-03__tile:hover .car-03__hud,
.car-03__tile:focus-visible .car-03__hud {
  opacity: 1;
}

.car-03__foot {
  max-width: 1080px;
  margin-inline: auto;
  padding: 20px clamp(16px,4cqi,40px) 36px;
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
}

@supports (animation-timeline: view()) {
  .car-03__tile {
    animation: car03-rise linear both;
    animation-timeline: view();
    animation-range: entry 0% entry 45%;
  }

  @keyframes car03-rise {
    from {
      opacity: .15;
      scale: .92;
    }

    to {
      opacity: 1;
      scale: 1;
    }
  }
}

@container car03 (width < 620px) {
  .car-03__profile {
    flex-wrap: wrap;
  }

  .car-03__follow {
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-03__tile {
    animation: none;
  }

  .car-03 * {
    transition-duration: .01ms !important;
  }
}
```
