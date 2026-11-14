---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/single-featured-hero-quote-block/"
title: "Single Featured Hero Quote Block"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "One quote, full viewport, no competition."
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Single Featured Hero Quote Block
Source: https://codefronts.com/components/css-testimonials-reviews/single-featured-hero-quote-block/

One quote, full viewport, no competition. This is the founder-endorsement or marquee-client slot at the very top of a page — oversized fluid type set with clamp() and text-wrap: balance, an animated word-by-word reveal driven purely by animation-delay, and a soft mesh backdrop built from three layered radial gradients rather than an image.
## HTML
```html
<section class="tr-10" aria-label="Single featured hero quote block demo">
  <div class="tr-10__stage">
    <div class="tr-10__mesh" aria-hidden="true"></div>
    <div class="tr-10__grain" aria-hidden="true"></div>

    <figure class="tr-10__fig">
      <p class="tr-10__eyebrow">Why we backed them</p>
      <blockquote class="tr-10__q" cite="https://example.com/investors">
        <p aria-label="I have seen four hundred data platforms. This is the first one where the engineers and the finance team both asked for a second seat in the same week.">
          <span class="tr-10__w" style="--tr-10-i:0" aria-hidden="true">I</span> <span class="tr-10__w" style="--tr-10-i:1" aria-hidden="true">have</span> <span class="tr-10__w" style="--tr-10-i:2" aria-hidden="true">seen</span> <span class="tr-10__w" style="--tr-10-i:3" aria-hidden="true">four</span> <span class="tr-10__w" style="--tr-10-i:4" aria-hidden="true">hundred</span> <span class="tr-10__w" style="--tr-10-i:5" aria-hidden="true">data</span> <span class="tr-10__w" style="--tr-10-i:6" aria-hidden="true">platforms.</span> <span class="tr-10__w tr-10__w--hi" style="--tr-10-i:7" aria-hidden="true">This</span> <span class="tr-10__w tr-10__w--hi" style="--tr-10-i:8" aria-hidden="true">is</span> <span class="tr-10__w tr-10__w--hi" style="--tr-10-i:9" aria-hidden="true">the</span> <span class="tr-10__w tr-10__w--hi" style="--tr-10-i:10" aria-hidden="true">first</span> <span class="tr-10__w tr-10__w--hi" style="--tr-10-i:11" aria-hidden="true">one</span> <span class="tr-10__w" style="--tr-10-i:12" aria-hidden="true">where</span> <span class="tr-10__w" style="--tr-10-i:13" aria-hidden="true">the</span> <span class="tr-10__w" style="--tr-10-i:14" aria-hidden="true">engineers</span> <span class="tr-10__w" style="--tr-10-i:15" aria-hidden="true">and</span> <span class="tr-10__w" style="--tr-10-i:16" aria-hidden="true">the</span> <span class="tr-10__w" style="--tr-10-i:17" aria-hidden="true">finance</span> <span class="tr-10__w" style="--tr-10-i:18" aria-hidden="true">team</span> <span class="tr-10__w" style="--tr-10-i:19" aria-hidden="true">both</span> <span class="tr-10__w" style="--tr-10-i:20" aria-hidden="true">asked</span> <span class="tr-10__w" style="--tr-10-i:21" aria-hidden="true">for</span> <span class="tr-10__w" style="--tr-10-i:22" aria-hidden="true">a</span> <span class="tr-10__w" style="--tr-10-i:23" aria-hidden="true">second</span> <span class="tr-10__w" style="--tr-10-i:24" aria-hidden="true">seat</span> <span class="tr-10__w" style="--tr-10-i:25" aria-hidden="true">in</span> <span class="tr-10__w" style="--tr-10-i:26" aria-hidden="true">the</span> <span class="tr-10__w" style="--tr-10-i:27" aria-hidden="true">same</span> <span class="tr-10__w" style="--tr-10-i:28" aria-hidden="true">week.</span>
        </p>
      </blockquote>

      <figcaption class="tr-10__cap">
        <img src="https://images.unsplash.com/photo-1556157382-97eda2d62296?q=80&w=180&h=180&fit=crop&auto=format" alt="Portrait of Vivienne Adeyemi" width="66" height="66" loading="lazy" decoding="async">
        <span class="tr-10__id"><b>Vivienne Adeyemi</b>General Partner · Halyard Ventures</span>
        <span class="tr-10__rule" aria-hidden="true"></span>
        <span class="tr-10__meta">Led the Series&nbsp;B · Board observer since 2025</span>
      </figcaption>
    </figure>
    <p class="tr-10__chip" aria-hidden="true">clamp() fluid display type · text-wrap:balance · per-word stagger · layered radial mesh</p>
  </div>
</section>
```
## CSS
```css
.tr-10,
.tr-10 *,
.tr-10 *::before,
.tr-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-10-bg: oklch(0.15 0.02 280);
  --tr-10-ink: oklch(0.98 0.005 280);
  --tr-10-mut: oklch(0.72 0.02 280);
  --tr-10-acc: oklch(0.8 0.16 90);
  --tr-10-acc2: oklch(0.66 0.19 320);
  background: var(--tr-10-bg);
  color: var(--tr-10-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-10__stage {
  position: relative;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(18px,3vw,28px);
  padding: clamp(24px,6vw,80px);
  overflow: hidden;
  isolation: isolate;
}

.tr-10__mesh {
  position: absolute;
  inset: -20%;
  z-index: -2;
  background: radial-gradient(38% 44% at 22% 24%,color-mix(in oklch,var(--tr-10-acc2) 42%,transparent),transparent 70%),radial-gradient(34% 40% at 78% 22%,color-mix(in oklch,var(--tr-10-acc) 30%,transparent),transparent 70%),radial-gradient(50% 50% at 60% 92%,oklch(0.5 0.16 220/.4),transparent 72%);
  filter: blur(40px);
  animation: tr-10-drift 26s ease-in-out infinite alternate;
}

@keyframes tr-10-drift {
  to {
    translate: 2% -3%;
    scale: 1.08;
  }
}

.tr-10__grain {
  position: absolute;
  inset: 0;
  z-index: -1;
  opacity: .05;
  background-image: repeating-linear-gradient(0deg,oklch(1 0 0) 0 1px,transparent 1px 3px),repeating-linear-gradient(90deg,oklch(1 0 0) 0 1px,transparent 1px 3px);
  mix-blend-mode: overlay;
  pointer-events: none;
}

.tr-10__fig {
  position: relative;
  width: min(100%,1080px);
  display: grid;
  justify-items: center;
  gap: clamp(22px,4vw,42px);
  text-align: center;
}

.tr-10__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--tr-10-acc);
  animation: tr-10-rise .8s cubic-bezier(.16,1,.3,1) both;
}

.tr-10__q {
  position: relative;
}

.tr-10__q::before {
  content: '“';
  position: absolute;
  inset-block-start: -.34em;
  inset-inline-start: 50%;
  translate: -50% 0;
  font-family: Georgia,'Times New Roman',serif;
  font-size: clamp(120px,20vw,260px);
  line-height: 1;
  color: oklch(1 0 0/.06);
  pointer-events: none;
  z-index: -1;
}

.tr-10__q p {
  font-size: clamp(26px,6.2vw,74px);
  font-weight: 600;
  line-height: 1.06;
  letter-spacing: -.045em;
  text-wrap: balance;
  max-width: 17ch;
}

.tr-10__w {
  display: inline-block;
  animation: tr-10-rise .9s cubic-bezier(.16,1,.3,1) both;
  animation-delay: calc(var(--tr-10-i,0)*48ms + 120ms);
}

.tr-10__w--hi {
  background: linear-gradient(100deg,var(--tr-10-acc),var(--tr-10-acc2));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

@keyframes tr-10-rise {
  from {
    opacity: 0;
    translate: 0 .42em;
    filter: blur(7px);
  }

  to {
    opacity: 1;
    translate: 0 0;
    filter: blur(0);
  }
}

.tr-10__cap {
  display: grid;
  justify-items: center;
  gap: 12px;
  animation: tr-10-rise .9s cubic-bezier(.16,1,.3,1) 1.6s both;
}

.tr-10__cap img {
  width: 66px;
  height: 66px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 0 0 1px oklch(1 0 0/.2),0 0 0 7px oklch(1 0 0/.05);
  background: oklch(0.35 0.04 280);
}

.tr-10__id {
  display: grid;
  gap: 3px;
  font-size: 13px;
  color: var(--tr-10-mut);
}

.tr-10__id b {
  font-size: 17px;
  font-weight: 640;
  color: var(--tr-10-ink);
  letter-spacing: -.02em;
}

.tr-10__rule {
  inline-size: 44px;
  block-size: 1px;
  background: oklch(1 0 0/.25);
}

.tr-10__meta {
  font-size: 12px;
  color: color-mix(in oklch,var(--tr-10-mut) 88%,transparent);
  letter-spacing: .01em;
}

.tr-10__chip {
  position: relative;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-10-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
  animation: tr-10-rise .9s cubic-bezier(.16,1,.3,1) 1.9s both;
}

@media (prefers-reduced-motion: reduce) {
  .tr-10__w,
    .tr-10__cap,
    .tr-10__eyebrow,
    .tr-10__chip {
    animation: none;
    opacity: 1;
    filter: none;
    translate: none;
  }

  .tr-10__mesh {
    animation: none;
  }
}
```
