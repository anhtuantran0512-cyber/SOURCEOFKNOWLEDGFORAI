---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/clay-bottom-tab-bar-for-mobile/"
title: "Clay Bottom Tab Bar for Mobile"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "A floating clay dock with five destinations, a sliding puffy indicator, and the two things production tab bars must get right: env(safe-area-inset-bottom) so…"
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clay Bottom Tab Bar for Mobile
Source: https://codefronts.com/design-styles/css-claymorphism/clay-bottom-tab-bar-for-mobile/

A floating clay dock with five destinations, a sliding puffy indicator, and the two things production tab bars must get right: env(safe-area-inset-bottom) so it clears the iPhone home bar, and 44px+ hit targets with labels that stay legible at the smallest text size. The indicator and label reveal are driven by radios and :has(), and the active tab is announced natively.
## HTML
```html
<section class="cl-16" aria-label="Clay bottom tab bar for mobile demo">
  <div class="cl-16__stage">
    <div class="cl-16__phone">
      <div class="cl-16__screen">
        <header class="cl-16__appbar">
          <span class="cl-16__appTitle">Library</span>
          <span class="cl-16__appAvatar" aria-hidden="true"></span>
        </header>
        <div class="cl-16__content" aria-hidden="true">
          <div class="cl-16__row"><span class="cl-16__thumb"></span><span class="cl-16__lines"><i></i><i></i></span></div>
          <div class="cl-16__row"><span class="cl-16__thumb cl-16__thumb--b"></span><span class="cl-16__lines"><i></i><i></i></span></div>
          <div class="cl-16__row"><span class="cl-16__thumb cl-16__thumb--c"></span><span class="cl-16__lines"><i></i><i></i></span></div>
          <div class="cl-16__row"><span class="cl-16__thumb cl-16__thumb--d"></span><span class="cl-16__lines"><i></i><i></i></span></div>
        </div>
        <nav class="cl-16__dock" aria-label="Main">
          <div class="cl-16__bar" role="tablist">
            <span class="cl-16__pill" aria-hidden="true"></span>
            <input class="cl-16__r" type="radio" name="cl-16-tab" id="cl-16-t1">
            <label class="cl-16__tab" for="cl-16-t1">
              <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M4 11.2 12 4l8 7.2V20a1 1 0 0 1-1 1h-4v-6H9v6H5a1 1 0 0 1-1-1z" fill="currentColor"/></svg>
              <span>Home</span>
            </label>
            <input class="cl-16__r" type="radio" name="cl-16-tab" id="cl-16-t2" checked>
            <label class="cl-16__tab" for="cl-16-t2">
              <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M5 4h9l5 5v11a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1zm8 1.8V10h4.2z" fill="currentColor"/></svg>
              <span>Library</span>
            </label>
            <input class="cl-16__r" type="radio" name="cl-16-tab" id="cl-16-t3">
            <label class="cl-16__tab" for="cl-16-t3">
              <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M12 3.5 14.6 9l6 .9-4.3 4.2 1 6-5.3-2.8-5.3 2.8 1-6L3.4 9.9 9.4 9z" fill="currentColor"/></svg>
              <span>Streaks</span>
            </label>
            <input class="cl-16__r" type="radio" name="cl-16-tab" id="cl-16-t4">
            <label class="cl-16__tab" for="cl-16-t4">
              <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zm0 2c-4 0-7 2.2-7 5v1h14v-1c0-2.8-3-5-7-5z" fill="currentColor"/></svg>
              <span>Profile</span>
            </label>
            <input class="cl-16__r" type="radio" name="cl-16-tab" id="cl-16-t5">
            <label class="cl-16__tab" for="cl-16-t5">
              <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M4 6h16v2.4H4zm0 4.8h16v2.4H4zm0 4.8h11V18H4z" fill="currentColor"/></svg>
              <span>More</span>
            </label>
          </div>
        </nav>
      </div>
    </div>
    <p class="cl-16__chip" aria-hidden="true">one translating pill · label expands on active · env(safe-area-inset-bottom)</p>
  </div>
</section>
```
## CSS
```css
.cl-16,
.cl-16 *,
.cl-16 *::before,
.cl-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-16-bg);
  --cl-16-bg: oklch(0.93 0.03 340);
  --cl-16-clay: oklch(0.91 0.045 340);
  --cl-16-accent: oklch(0.8 0.13 340);
  --cl-16-shade: oklch(0.52 0.09 340/.5);
  --cl-16-light: oklch(1 0.012 340/.95);
  --cl-16-ink: oklch(0.27 0.05 340);
  --cl-16-mut: oklch(0.5 0.04 340);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-16-ink);
}

.cl-16__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(18px,4vw,48px);
  background: radial-gradient(80% 60% at 50% 0%,oklch(0.97 0.03 350),transparent 66%);
}

.cl-16__phone {
  width: min(94vw,372px);
  padding: 14px;
  border-radius: 56px;
  background: color-mix(in oklch,var(--cl-16-bg) 90%,white);
  box-shadow: 0 40px 70px -26px var(--cl-16-shade),inset 0 -18px 30px -16px var(--cl-16-shade),inset 0 20px 30px -12px var(--cl-16-light);
}

.cl-16__screen {
  position: relative;
  display: grid;
  grid-template-rows: auto 1fr auto;
  gap: 14px;
  height: min(70svh,560px);
  padding: 18px 16px 0;
  border-radius: 44px;
  overflow: hidden;
  background: color-mix(in oklch,var(--cl-16-bg) 96%,oklch(0.72 0.05 340));
  box-shadow: inset 0 12px 22px -10px var(--cl-16-shade),inset 0 -10px 18px -12px var(--cl-16-light);
}

.cl-16__appbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 2px 6px;
}

.cl-16__appTitle {
  font-size: 21px;
  font-weight: 780;
  letter-spacing: -.02em;
}

.cl-16__appAvatar {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: oklch(0.84 0.1 340);
  box-shadow: 0 8px 14px -7px var(--cl-16-shade),inset 0 -6px 10px -7px var(--cl-16-shade),inset 0 8px 10px -6px var(--cl-16-light);
}

.cl-16__content {
  display: grid;
  gap: 10px;
  align-content: start;
  overflow: hidden;
}

.cl-16__row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  border-radius: 26px;
  background: var(--cl-16-clay);
  box-shadow: 0 12px 20px -14px var(--cl-16-shade),inset 0 -8px 14px -10px var(--cl-16-shade),inset 0 10px 14px -8px var(--cl-16-light);
}

.cl-16__thumb {
  flex: none;
  width: 46px;
  height: 46px;
  border-radius: 18px;
  background: oklch(0.84 0.1 30);
  box-shadow: inset 0 -6px 10px -7px var(--cl-16-shade),inset 0 8px 10px -6px var(--cl-16-light);
}

.cl-16__thumb--b {
  background: oklch(0.84 0.09 190);
}

.cl-16__thumb--c {
  background: oklch(0.85 0.1 290);
}

.cl-16__thumb--d {
  background: oklch(0.86 0.1 145);
}

.cl-16__lines {
  flex: 1;
  display: grid;
  gap: 8px;
}

.cl-16__lines i {
  display: block;
  height: 9px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--cl-16-shade) 26%,transparent);
}

.cl-16__lines i:last-child {
  width: 58%;
}

.cl-16__dock {
  position: sticky;
  bottom: 0;
  padding: 0 0 calc(12px + env(safe-area-inset-bottom,0px));
}

.cl-16__bar {
  position: relative;
  display: grid;
  grid-template-columns: repeat(5,1fr);
  gap: 0;
  padding: 8px;
  border-radius: 32px;
  background: var(--cl-16-clay);
  box-shadow: 0 26px 44px -18px var(--cl-16-shade),inset 0 -12px 20px -12px var(--cl-16-shade),inset 0 14px 20px -8px var(--cl-16-light);
}

.cl-16__pill {
  position: absolute;
  top: 8px;
  left: 8px;
  width: calc((100% - 16px) / 5);
  height: calc(100% - 16px);
  border-radius: 24px;
  background: var(--cl-16-accent);
  box-shadow: 0 10px 18px -8px var(--cl-16-shade),inset 0 -7px 12px -8px var(--cl-16-shade),inset 0 9px 12px -6px var(--cl-16-light);
  transition: translate .36s cubic-bezier(.34,1.45,.5,1);
}

.cl-16__bar:has(#cl-16-t2:checked) .cl-16__pill {
  translate: 100% 0;
}

.cl-16__bar:has(#cl-16-t3:checked) .cl-16__pill {
  translate: 200% 0;
}

.cl-16__bar:has(#cl-16-t4:checked) .cl-16__pill {
  translate: 300% 0;
}

.cl-16__bar:has(#cl-16-t5:checked) .cl-16__pill {
  translate: 400% 0;
}

.cl-16__r {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cl-16__tab {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  min-height: 56px;
  border-radius: 24px;
  color: var(--cl-16-mut);
  cursor: pointer;
  overflow: hidden;
  transition: color .3s,scale .3s cubic-bezier(.34,1.4,.5,1);
}

.cl-16__tab svg {
  flex: none;
  transition: scale .3s cubic-bezier(.34,1.5,.5,1),translate .3s;
}

.cl-16__tab span {
  max-height: 0;
  font-size: 10.5px;
  font-weight: 680;
  letter-spacing: -.01em;
  white-space: nowrap;
  opacity: 0;
  transition: max-height .34s cubic-bezier(.2,.8,.3,1),opacity .22s;
}

.cl-16__tab:hover {
  color: var(--cl-16-ink);
}

.cl-16__tab:active {
  scale: .94;
}

.cl-16__r:checked+.cl-16__tab {
  color: oklch(0.24 0.06 340);
}

.cl-16__r:checked+.cl-16__tab svg {
  scale: 1.08;
}

.cl-16__r:checked+.cl-16__tab span {
  max-height: 14px;
  opacity: 1;
}

.cl-16__r:focus-visible+.cl-16__tab {
  outline: 3px solid var(--cl-16-ink);
  outline-offset: -3px;
}

.cl-16__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-16-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.55);
  box-shadow: inset 0 -4px 10px -8px var(--cl-16-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-16 * {
    transition-duration: .01ms !important;
  }
}
```
