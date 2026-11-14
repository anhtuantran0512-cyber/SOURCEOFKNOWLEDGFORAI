---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-event-ticket-card-html-css/"
title: "Glassmorphism Event Ticket Card HTML CSS"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Ticketcraft: a concert pass over a crowd photo with REAL punched notches (mask-composited out of the glass so the background shows through), a dashed…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Event Ticket Card HTML CSS
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-event-ticket-card-html-css/

Ticketcraft: a concert pass over a crowd photo with REAL punched notches (mask-composited out of the glass so the background shows through), a dashed perforation line and a repeating-gradient barcode — plus a tech-conf boarding pass whose stub visibly tears away on hover.
## HTML
```html
<div class="glz-19-group">
<link href="https://fonts.googleapis.com/css2?family=Unbounded:[email protected]&family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="glz-19a" aria-label="Glassmorphism concert ticket demo">
  <article class="glz-19a__ticket">
    <header class="glz-19a__head"><span class="glz-19a__fest">HELIOS FEST</span><span class="glz-19a__tier">VIP</span></header>
    <h3 class="glz-19a__act">Neon Palms<em>+ Cobalt Era · Ferry Lights</em></h3>
    <dl class="glz-19a__meta">
      <div><dt>Date</dt><dd>Sat 21 Mar 2027</dd></div>
      <div><dt>Doors</dt><dd>7:30 PM</dd></div>
      <div><dt>Gate</dt><dd>C4</dd></div>
      <div><dt>Seat</dt><dd>GA — Floor</dd></div>
    </dl>
    <div class="glz-19a__tear" aria-hidden="true"></div>
    <footer class="glz-19a__foot"><i class="glz-19a__code" aria-hidden="true"></i><span class="glz-19a__serial">Nº 004467-B</span></footer>
  </article>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="glz-19b" aria-label="Conference boarding pass with tear-off stub">
  <div class="glz-19b__pass">
    <article class="glz-19b__main">
      <header><span class="glz-19b__conf">CSSCONF · AKL</span><b>27</b></header>
      <h3>Frontend Boarding Pass</h3>
      <dl>
        <div><dt>Attendee</dt><dd>R. Okonkwo</dd></div>
        <div><dt>Track</dt><dd>Modern CSS</dd></div>
        <div><dt>Row</dt><dd>D</dd></div>
        <div><dt>Seat</dt><dd>14</dd></div>
      </dl>
      <p class="glz-19b__gate">Workshop Hall 2 · boarding 8:45 AM</p>
    </article>
    <aside class="glz-19b__stub" aria-hidden="true">
      <span class="glz-19b__conf">STUB</span>
      <b>D-14</b>
      <i class="glz-19b__qr"></i>
      <em>keep this half</em>
    </aside>
  </div>
  <p class="glz-19b__hint" aria-hidden="true">hover to tear</p>
</section>
</div>
```
## CSS
```css
.glz-19-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-19-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-19a,
.glz-19a *,
.glz-19a *::before,
.glz-19a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-19a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(rgba(30,16,50,.72),rgba(16,10,30,.85)),url('https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?q=80&w=1600&auto=format&fit=crop') center/cover;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
}

.glz-19a__ticket {
  position: relative;
  width: min(360px,100%);
  padding: 26px 26px 22px;
  border-radius: 22px;
  color: #f5efff;
  background: linear-gradient(165deg,rgba(255,255,255,.16),rgba(255,255,255,.05));
  backdrop-filter: blur(20px) saturate(170%);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
  border: 1px solid rgba(255,255,255,.28);
  box-shadow: 0 34px 70px -26px rgba(0,0,0,.85);
  -webkit-mask: radial-gradient(circle 13px at 0 67%,transparent 98%,#000) ,radial-gradient(circle 13px at 100% 67%,transparent 98%,#000);
  -webkit-mask-composite: source-in;
  mask: radial-gradient(circle 13px at 0 67%,transparent 98%,#000),radial-gradient(circle 13px at 100% 67%,transparent 98%,#000);
  mask-composite: intersect;
}

.glz-19a__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.glz-19a__fest {
  font-size: 11px;
  letter-spacing: .34em;
  color: oklch(0.85 0.14 320);
}

.glz-19a__tier {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .2em;
  padding: 5px 11px;
  border-radius: 99px;
  color: #1a0f2e;
  background: linear-gradient(120deg,oklch(0.85 0.12 320),oklch(0.85 0.14 60));
}

.glz-19a__act {
  margin-top: 18px;
  font-family: 'Unbounded',sans-serif;
  font-size: clamp(24px,5.4vw,31px);
  font-weight: 700;
  letter-spacing: -.01em;
  line-height: 1.1;
}

.glz-19a__act em {
  display: block;
  margin-top: 8px;
  font-family: 'JetBrains Mono',monospace;
  font-style: normal;
  font-size: 11px;
  letter-spacing: .1em;
  color: rgba(245,239,255,.6);
}

.glz-19a__meta {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px 18px;
  margin-top: 20px;
}

.glz-19a__meta dt {
  font-size: 9px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: rgba(245,239,255,.45);
}

.glz-19a__meta dd {
  margin-top: 3px;
  font-size: 13px;
  font-weight: 700;
}

.glz-19a__tear {
  margin: 20px -26px 0;
  border-top: 2px dashed rgba(255,255,255,.3);
}

.glz-19a__foot {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-top: 18px;
}

.glz-19a__code {
  flex: 1;
  height: 44px;
  border-radius: 6px;
  background: repeating-linear-gradient(90deg,#f5efff 0 2px,transparent 2px 5px,#f5efff 5px 8px,transparent 8px 10px,#f5efff 10px 13px,transparent 13px 18px,#f5efff 18px 20px,transparent 20px 23px);
  opacity: .92;
}

.glz-19a__serial {
  font-size: 10.5px;
  letter-spacing: .14em;
  color: rgba(245,239,255,.55);
  writing-mode: vertical-rl;
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-19a__ticket {
    background: rgba(34,22,56,.94);
  }
}

.glz-19b,
.glz-19b *,
.glz-19b *::before,
.glz-19b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-19b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: 48px 24px;
  position: relative;
  overflow: hidden;
  background: linear-gradient(190deg,#0f1626,#101d2c);
}

.glz-19b::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(44% 40% at 78% 18%,oklch(0.6 0.15 220/.4),transparent 70%),radial-gradient(40% 34% at 14% 84%,oklch(0.65 0.14 160/.35),transparent 70%);
}

.glz-19b__pass {
  position: relative;
  z-index: 1;
  display: flex;
  width: min(520px,100%);
  filter: drop-shadow(0 30px 44px rgba(0,0,0,.6));
}

.glz-19b__main {
  flex: 1;
  min-width: 0;
  padding: 24px 26px;
  border-radius: 20px 0 0 20px;
  color: #eaf3fb;
  font-family: 'Space Grotesk',system-ui,sans-serif;
  background: linear-gradient(165deg,rgba(255,255,255,.14),rgba(255,255,255,.05));
  backdrop-filter: blur(20px) saturate(170%);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
  border: 1px solid rgba(255,255,255,.25);
  border-right: 2px dashed rgba(255,255,255,.35);
}

.glz-19b__main header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.glz-19b__conf {
  font: 700 10px 'JetBrains Mono',monospace;
  letter-spacing: .3em;
  color: oklch(0.82 0.13 200);
}

.glz-19b__main header b {
  font: 700 15px 'JetBrains Mono',monospace;
  color: rgba(234,243,251,.55);
}

.glz-19b__main h3 {
  margin-top: 14px;
  font-size: 21px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.glz-19b__main dl {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(90px,1fr));
  gap: 12px;
  margin-top: 18px;
}

.glz-19b__main dt {
  font-size: 9px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(234,243,251,.45);
}

.glz-19b__main dd {
  margin-top: 3px;
  font: 700 13.5px 'JetBrains Mono',monospace;
}

.glz-19b__gate {
  margin-top: 18px;
  padding-top: 14px;
  border-top: 1px solid rgba(255,255,255,.15);
  font-size: 12px;
  color: rgba(234,243,251,.6);
}

.glz-19b__stub {
  flex: none;
  width: 128px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 22px 14px;
  border-radius: 0 20px 20px 0;
  color: #eaf3fb;
  text-align: center;
  background: linear-gradient(165deg,oklch(0.6 0.15 220/.3),rgba(255,255,255,.06));
  backdrop-filter: blur(20px) saturate(170%);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
  border: 1px solid rgba(255,255,255,.25);
  border-left: none;
  transform-origin: left center;
  transition: transform .5s cubic-bezier(.2,.8,.25,1.1);
}

.glz-19b__pass:hover .glz-19b__stub {
  transform: translateX(16px) rotate(5deg);
}

.glz-19b__stub b {
  font: 700 22px 'JetBrains Mono',monospace;
}

.glz-19b__qr {
  width: 58px;
  height: 58px;
  border-radius: 8px;
  background: conic-gradient(#eaf3fb 25%,transparent 0 50%,#eaf3fb 0 75%,transparent 0) 0 0/14px 14px,#20304a;
  opacity: .9;
}

.glz-19b__stub em {
  font: 600 9px 'JetBrains Mono',monospace;
  font-style: normal;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: rgba(234,243,251,.5);
}

.glz-19b__hint {
  position: relative;
  z-index: 1;
  font: 600 11px 'JetBrains Mono',monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(180,205,230,.4);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-19b__main,
    .glz-19b__stub {
    background: rgba(20,30,46,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-19b__stub {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the side notches are mask-composited OUT of the glass (the blurred crowd shows through the holes); the barcode is one repeating gradient. */

/* No JavaScript — the stub is a flex sibling behind a dashed rule; hovering the pass translates + rotates it from its left edge like a real tear. */
```
