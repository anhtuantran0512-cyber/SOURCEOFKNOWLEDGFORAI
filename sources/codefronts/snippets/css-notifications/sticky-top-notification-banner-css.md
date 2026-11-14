---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/sticky-top-notification-banner-css/"
title: "Sticky Top Notification Banner CSS"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Two sticky-banner behaviors over real scrolling content: a dismissible announcement bar whose position:sticky anatomy is visible live (scroll and watch it…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Top Notification Banner CSS
Source: https://codefronts.com/snippets/css-notifications/sticky-top-notification-banner-css/

Two sticky-banner behaviors over real scrolling content: a dismissible announcement bar whose position:sticky anatomy is visible live (scroll and watch it hold the top edge) and whose dismissal collapses smoothly instead of yanking the page up — and a zero-JS scroll-driven banner that condenses from a tall promo into a slim strip as you scroll, powered by animation-timeline: scroll().
## HTML
```html
<div class="ntf-15-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-15a" aria-label="Sticky announcement banner over scrolling content">
  <div class="ntf-15a__page" id="ntf-15a-page">
    <div class="ntf-15a__banner" id="ntf-15a-banner" role="region" aria-label="Announcement">
      <div class="ntf-15a__clip">
        <div class="ntf-15a__inner">
          <span class="ntf-15a__tag" aria-hidden="true">NEW</span>
          <p class="ntf-15a__msg"><b>Snippets 2.0 is live</b> — 30 fresh notification patterns, all copy-paste ready.</p>
          <a class="ntf-15a__cta" href="#" onclick="return false">Browse</a>
          <button class="ntf-15a__x" id="ntf-15a-x" type="button" aria-label="Dismiss announcement">&#10005;</button>
        </div>
      </div>
    </div>
    <header class="ntf-15a__hero"><h2>The banner above is <em>sticky</em></h2><p>Scroll this panel — it holds the top edge. Dismiss it — the page glides, never jumps.</p></header>
    <article class="ntf-15a__prose"><h3>Why sticky beats fixed</h3><p>A fixed banner floats over the document, so the page needs manual padding to avoid hiding content beneath it. A sticky banner occupies real layout space and only pins once its edge reaches the viewport.</p><h3>Dismissal without the yank</h3><p>Removing a 56px banner node scrolls everything up 56 pixels instantly. Collapsing grid-template-rows from 1fr to 0fr animates the same change over 400ms, and the reading position eases instead of teleporting.</p><h3>Filler paragraph</h3><p>Keep scrolling to feel the pin. The banner belongs to this scroll container, so it pins to the panel's top rather than the page's.</p><p>Sticky elements need every ancestor to keep visible overflow — one stray overflow:hidden and the pin silently dies.</p></article>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-15b" aria-label="Banner that condenses as you scroll, no JavaScript">
  <div class="ntf-15b__page">
    <div class="ntf-15b__banner" role="region" aria-label="Promotion">
      <p class="ntf-15b__big" aria-hidden="true">EARLY ACCESS · <b>40% OFF</b> annual plans this week</p>
      <p class="ntf-15b__small">40% off — <b>claim</b></p>
    </div>
    <article class="ntf-15b__prose">
      <h2>Scroll me</h2>
      <p>The banner's padding, size and even its message are keyframes mapped onto scroll position with <b>animation-timeline: scroll()</b>. No listeners, no throttling, runs off the main thread.</p>
      <p>Scroll back up and it re-expands — the timeline plays in both directions because it IS the scrollbar.</p>
      <p>The full promo line cross-fades into a compact one at the 60% mark of the 180px range; both live in the DOM, so screen readers always get the complete message.</p>
      <p>Support: Chrome 115+, Edge 115+, Safari 26. The @supports guard keeps older browsers on the expanded banner permanently — nothing breaks, it just doesn't condense.</p>
      <p>Filler to make the panel scroll. The pattern shines on marketing sites where the promo must stay present but shouldn't keep shouting once the visitor commits to reading.</p>
    </article>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-15-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.ntf-15-group > section {
  width: 100%;
}

.ntf-15a,
.ntf-15a *,
.ntf-15a *::before,
.ntf-15a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-15a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#151a26,#0b0e15);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-15a__page {
  width: min(680px,100%);
  height: min(72vh,560px);
  overflow: auto;
  border-radius: 18px;
  background: #f5f6f9;
  border: 1px solid rgba(165,190,230,.2);
  box-shadow: 0 34px 80px -40px rgba(0,0,0,.9);
}

.ntf-15a__banner {
  position: sticky;
  top: 0;
  z-index: 5;
  display: grid;
  grid-template-rows: 1fr;
  transition: grid-template-rows .4s cubic-bezier(.4,0,.2,1),opacity .3s ease;
}

.ntf-15a__banner.is-dismissed {
  grid-template-rows: 0fr;
  opacity: 0;
}

.ntf-15a__clip {
  overflow: hidden;
}

.ntf-15a__inner {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 13px 18px;
  background: linear-gradient(90deg,oklch(0.45 0.16 280),oklch(0.5 0.17 250));
  color: #fff;
}

.ntf-15a__tag {
  flex: none;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .1em;
  padding: 4px 8px;
  border-radius: 6px;
  background: rgb(255 255 255 / .18);
  border: 1px solid rgb(255 255 255 / .3);
}

.ntf-15a__msg {
  font-size: 13.5px;
  line-height: 1.4;
  min-width: 0;
}

.ntf-15a__msg b {
  font-weight: 700;
}

.ntf-15a__cta {
  margin-left: auto;
  flex: none;
  font-size: 12.5px;
  font-weight: 700;
  color: oklch(0.35 0.12 270);
  background: #fff;
  text-decoration: none;
  padding: 7px 14px;
  border-radius: 8px;
  transition: scale .12s;
}

.ntf-15a__cta:hover {
  scale: 1.04;
}

.ntf-15a__x {
  flex: none;
  width: 28px;
  height: 28px;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 8px;
  font-size: 12px;
  color: rgb(255 255 255 / .8);
  background: transparent;
  cursor: pointer;
  transition: background .15s;
}

.ntf-15a__x:hover {
  background: rgb(255 255 255 / .15);
}

.ntf-15a__hero {
  padding: 38px 30px 10px;
  color: #1b1f2a;
}

.ntf-15a__hero h2 {
  font-size: 26px;
  font-weight: 600;
  letter-spacing: -.01em;
}

.ntf-15a__hero h2 em {
  font-style: normal;
  color: oklch(0.5 0.17 260);
}

.ntf-15a__hero p {
  margin-top: 8px;
  font-size: 14px;
  color: rgba(27,31,42,.6);
}

.ntf-15a__prose {
  padding: 10px 30px 44px;
  color: rgba(27,31,42,.75);
}

.ntf-15a__prose h3 {
  margin-top: 26px;
  font-size: 16px;
  font-weight: 600;
  color: #1b1f2a;
}

.ntf-15a__prose p {
  margin-top: 8px;
  font-size: 13.5px;
  line-height: 1.75;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-15a__banner {
    transition-duration: .01s;
  }
}

.ntf-15b,
.ntf-15b *,
.ntf-15b *::before,
.ntf-15b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-15b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f6f2e9,#ece4d2);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-15b__page {
  width: min(680px,100%);
  height: min(72vh,560px);
  overflow: auto;
  border-radius: 18px;
  background: #fffdf8;
  border: 1px solid rgba(35,31,24,.12);
  box-shadow: 0 30px 70px -38px rgba(35,31,24,.55);
}

.ntf-15b__banner {
  position: sticky;
  top: 0;
  z-index: 5;
  display: grid;
  place-items: center;
  background: #211d16;
  color: #fdfaf2;
  padding: 26px 20px;
}

.ntf-15b__big {
  font-size: clamp(16px,2.6vw,21px);
  font-weight: 500;
  letter-spacing: .01em;
}

.ntf-15b__big b {
  font-weight: 800;
  color: oklch(0.85 0.14 85);
}

.ntf-15b__small {
  position: absolute;
  font-size: 13px;
  font-weight: 600;
  opacity: 0;
}

.ntf-15b__small b {
  color: oklch(0.85 0.14 85);
}

@supports (animation-timeline: scroll()) {
  .ntf-15b__banner {
    animation: ntf-15b-shrink linear both;
    animation-timeline: scroll();
    animation-range: 0 180px;
  }

  .ntf-15b__big {
    animation: ntf-15b-hide linear both;
    animation-timeline: scroll();
    animation-range: 0 140px;
  }

  .ntf-15b__small {
    animation: ntf-15b-show linear both;
    animation-timeline: scroll();
    animation-range: 100px 180px;
  }

  @keyframes ntf-15b-shrink {
    to {
      padding: 9px 20px;
      background: #181510;
    }
  }

  @keyframes ntf-15b-hide {
    to {
      opacity: 0;
      scale: .92;
    }
  }

  @keyframes ntf-15b-show {
    from {
      opacity: 0;
      translate: 0 6px;
    }

    to {
      opacity: 1;
      translate: 0 0;
    }
  }
}

.ntf-15b__prose {
  padding: 34px 30px 46px;
  color: rgba(35,31,24,.75);
}

.ntf-15b__prose h2 {
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: #211d16;
}

.ntf-15b__prose p {
  margin-top: 14px;
  font-size: 14px;
  line-height: 1.8;
  text-wrap: pretty;
}

.ntf-15b__prose b {
  color: #211d16;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-15b__banner,
    .ntf-15b__big,
    .ntf-15b__small {
    animation: none;
  }

  .ntf-15b__small {
    position: static;
    opacity: 0;
    display: none;
  }
}
```

## JavaScript
```js
(function(){
  var banner=document.getElementById('ntf-15a-banner'); if(!banner) return;
  document.getElementById('ntf-15a-x').addEventListener('click',function(){
    banner.classList.add('is-dismissed');
    banner.addEventListener('transitionend',function(e){
      if(e.propertyName==='grid-template-rows') banner.remove();
      /* In production: localStorage.setItem('banner-snippets-2', 'dismissed') before removing. */
    });
  });
})();

/* No JavaScript — animation-timeline:scroll() binds three keyframe sets to the panel's scroll position (banner shrinks, long message fades out, short one fades in); scrolling up plays everything backwards for free. */
```
