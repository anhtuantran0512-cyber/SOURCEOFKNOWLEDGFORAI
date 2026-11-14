---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/responsive-full-width-mobile-notification-bar/"
title: "Responsive Full Width Mobile Notification Bar"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "The same notification markup rendered in three container widths side by side — @container queries morph it from full-width thumb-zone bottom bar (block…"
has_js: "false"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Full Width Mobile Notification Bar
Source: https://codefronts.com/snippets/css-notifications/responsive-full-width-mobile-notification-bar/

The same notification markup rendered in three container widths side by side — @container queries morph it from full-width thumb-zone bottom bar (block buttons, 48px targets) through mid-size sheet to compact corner card, no JavaScript and no viewport queries — plus a phone-frame bottom sheet with real drag physics via scroll-snap: peek, half and full snap points, honest 100dvh sizing and a safe-area spacer.
## HTML
```html
<div class="ntf-27-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<section class="ntf-27a" aria-label="Same notification in three container widths">
  <div class="ntf-27a__rig">
    <div class="ntf-27a__slot" style="width:min(320px,100%)"><code class="ntf-27a__w">container: 320px — thumb-zone sheet</code>
      <div class="ntf-27a__bar" role="status"><span class="ntf-27a__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v13m0 0l-4-4m4 4l4-4M4 21h16"/></svg></span><span class="ntf-27a__tx"><b>Update downloaded</b><small>v4.1 · 82 MB — restart to install</small></span><div class="ntf-27a__btns"><button class="ntf-27a__go" type="button">Restart now</button><button class="ntf-27a__later" type="button">Tonight</button></div></div>
    </div>
    <div class="ntf-27a__slot" style="width:min(460px,100%)"><code class="ntf-27a__w">container: 460px — inline actions</code>
      <div class="ntf-27a__bar" role="status"><span class="ntf-27a__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v13m0 0l-4-4m4 4l4-4M4 21h16"/></svg></span><span class="ntf-27a__tx"><b>Update downloaded</b><small>v4.1 · 82 MB — restart to install</small></span><div class="ntf-27a__btns"><button class="ntf-27a__go" type="button">Restart now</button><button class="ntf-27a__later" type="button">Tonight</button></div></div>
    </div>
    <div class="ntf-27a__slot" style="width:min(620px,100%)"><code class="ntf-27a__w">container: 620px — corner-card density</code>
      <div class="ntf-27a__bar" role="status"><span class="ntf-27a__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v13m0 0l-4-4m4 4l4-4M4 21h16"/></svg></span><span class="ntf-27a__tx"><b>Update downloaded</b><small>v4.1 · 82 MB — restart to install</small></span><div class="ntf-27a__btns"><button class="ntf-27a__go" type="button">Restart now</button><button class="ntf-27a__later" type="button">Tonight</button></div></div>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-27b" aria-label="Mobile bottom sheet with scroll snap states">
  <div class="ntf-27b__phone">
    <div class="ntf-27b__screen">
      <p class="ntf-27b__ghost">app content</p>
      <div class="ntf-27b__snapper">
        <div class="ntf-27b__spacer ntf-27b__spacer--full" aria-hidden="true"></div>
        <div class="ntf-27b__spacer ntf-27b__spacer--half" aria-hidden="true"></div>
        <aside class="ntf-27b__sheet" role="region" aria-label="Notifications sheet">
          <i class="ntf-27b__grab" aria-hidden="true"></i>
          <header class="ntf-27b__head"><b>Notifications</b><span>4 new</span></header>
          <div class="ntf-27b__item"><i style="--c:oklch(0.72 0.15 155)" aria-hidden="true"></i><span><b>Backup finished</b><small>212 photos secured</small></span></div>
          <div class="ntf-27b__item"><i style="--c:oklch(0.7 0.13 250)" aria-hidden="true"></i><span><b>2 new followers</b><small>@june.builds, @pxlgrid</small></span></div>
          <div class="ntf-27b__item"><i style="--c:oklch(0.78 0.13 85)" aria-hidden="true"></i><span><b>Storage 80% full</b><small>manage your library</small></span></div>
          <div class="ntf-27b__item"><i style="--c:oklch(0.66 0.18 25)" aria-hidden="true"></i><span><b>Sign-in from new device</b><small>Chrome · Melbourne AU</small></span></div>
          <div class="ntf-27b__safe" aria-hidden="true"></div>
        </aside>
      </div>
    </div>
  </div>
  <p class="ntf-27b__cap">drag the sheet — <b>peek / half / full</b> are scroll-snap stops, not JavaScript states · sized with 100dvh · safe-area padded</p>
</section>
</div>
```
## CSS
```css
.ntf-27-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.ntf-27-group > section {
  width: 100%;
}

.ntf-27a,
.ntf-27a *,
.ntf-27a *::before,
.ntf-27a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-27a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#141a26,#0b0e15);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-27a__rig {
  display: grid;
  gap: 26px;
  justify-items: center;
  width: 100%;
}

.ntf-27a__slot {
  container-type: inline-size;
  display: grid;
  gap: 8px;
}

.ntf-27a__w {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 10.5px;
  color: rgba(205,220,248,.45);
}

.ntf-27a__bar {
  display: grid;
  grid-template-columns: auto 1fr;
  align-items: center;
  gap: 12px;
  padding: 16px;
  border-radius: 18px;
  background: #161c2a;
  border: 1px solid rgba(165,190,230,.2);
  box-shadow: 0 22px 50px -28px rgba(0,0,0,.9);
}

.ntf-27a__ico {
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  color: #0d1420;
  background: oklch(0.74 0.13 250);
}

.ntf-27a__ico svg {
  width: 19px;
  height: 19px;
}

.ntf-27a__tx {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.ntf-27a__tx b {
  font-size: 14px;
  font-weight: 600;
  color: #edf2fc;
}

.ntf-27a__tx small {
  font-size: 12px;
  color: rgba(212,224,246,.55);
}

.ntf-27a__btns {
  grid-column: 1 / -1;
  display: grid;
  gap: 8px;
}

.ntf-27a__go,
.ntf-27a__later {
  font: inherit;
  font-size: 13px;
  font-weight: 700;
  border-radius: 11px;
  cursor: pointer;
  min-height: 48px;
  padding: 0 16px;
  transition: filter .15s,background .15s;
}

.ntf-27a__go {
  color: #0d1420;
  background: oklch(0.74 0.13 250);
  border: 0;
}

.ntf-27a__go:hover {
  filter: brightness(1.08);
}

.ntf-27a__later {
  color: #edf2fc;
  background: transparent;
  border: 1.5px solid rgba(165,190,230,.28);
}

.ntf-27a__later:hover {
  background: rgba(255,255,255,.06);
}

@container (min-width: 420px) {
  .ntf-27a__bar {
    grid-template-columns: auto 1fr auto;
  }

  .ntf-27a__btns {
    grid-column: auto;
    grid-auto-flow: column;
    gap: 8px;
  }

  .ntf-27a__go,
    .ntf-27a__later {
    min-height: 40px;
    font-size: 12.5px;
  }
}

@container (min-width: 560px) {
  .ntf-27a__bar {
    padding: 13px 16px;
    border-radius: 14px;
  }

  .ntf-27a__ico {
    width: 32px;
    height: 32px;
    border-radius: 9px;
  }

  .ntf-27a__ico svg {
    width: 16px;
    height: 16px;
  }

  .ntf-27a__tx b {
    font-size: 13px;
  }

  .ntf-27a__tx small {
    font-size: 11px;
  }

  .ntf-27a__go,
    .ntf-27a__later {
    min-height: 34px;
    font-size: 12px;
    border-radius: 9px;
  }
}

.ntf-27b,
.ntf-27b *,
.ntf-27b *::before,
.ntf-27b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-27b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f6f3ec,#ebe4d3);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-27b__phone {
  width: min(330px,100%);
  border-radius: 38px;
  padding: 10px;
  background: #221f19;
  box-shadow: 0 40px 80px -40px rgba(36,31,23,.7);
}

.ntf-27b__screen {
  position: relative;
  height: 560px;
  max-height: min(72vh,560px);
  border-radius: 30px;
  overflow: hidden;
  background: linear-gradient(170deg,#39342a,#262219);
}

.ntf-27b__ghost {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font-size: 13px;
  color: rgba(255,253,247,.3);
}

.ntf-27b__snapper {
  position: absolute;
  inset: 0;
  overflow-y: auto;
  scroll-snap-type: y mandatory;
  overscroll-behavior: contain;
  scrollbar-width: none;
}

.ntf-27b__snapper::-webkit-scrollbar {
  display: none;
}

.ntf-27b__spacer--full {
  height: 14%;
  scroll-snap-align: start;
}

.ntf-27b__spacer--half {
  height: 38%;
  scroll-snap-align: start;
}

.ntf-27b__sheet {
  min-height: 86%;
  scroll-snap-align: start;
  border-radius: 24px 24px 0 0;
  background: #fffdf7;
  box-shadow: 0 -18px 50px -20px rgba(0,0,0,.55);
  padding: 10px 16px 0;
}

.ntf-27b__grab {
  display: block;
  width: 40px;
  height: 4.5px;
  border-radius: 999px;
  background: rgba(36,31,23,.2);
  margin: 4px auto 10px;
}

.ntf-27b__head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 2px 4px 10px;
}

.ntf-27b__head b {
  font-size: 16px;
  font-weight: 700;
  color: #241f17;
}

.ntf-27b__head span {
  font-size: 11.5px;
  font-weight: 600;
  color: oklch(0.6 0.18 25);
}

.ntf-27b__item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 13px 6px;
  border-top: 1px solid rgba(36,31,23,.08);
}

.ntf-27b__item i {
  flex: none;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: var(--c);
}

.ntf-27b__item span {
  display: grid;
  gap: 1px;
  min-width: 0;
}

.ntf-27b__item b {
  font-size: 13.5px;
  font-weight: 600;
  color: #241f17;
}

.ntf-27b__item small {
  font-size: 11.5px;
  color: rgba(36,31,23,.5);
}

.ntf-27b__safe {
  height: calc(14px + env(safe-area-inset-bottom,0px));
}

.ntf-27b__cap {
  font-size: 12px;
  line-height: 1.6;
  color: rgba(36,31,23,.55);
  text-align: center;
  max-inline-size: 46ch;
  text-wrap: pretty;
}

.ntf-27b__cap b {
  color: #241f17;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-27b__snapper {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — three identical components in three container-typed slots; each @container block re-lays-out the bar based on the slot's own width. Copy the component anywhere and it keeps judging itself correctly. */

/* No JavaScript — the sheet sits in a y-mandatory scroll-snap container; two invisible spacers define the peek and half stops, the sheet's own top edge is the full stop. In a real app, size the screen with 100dvh so collapsing browser chrome never clips the sheet. */
```
