---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/ios-style-compose-floating-button/"
title: "iOS-Style Compose Floating Button"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "What a compose button looks like on iOS: translucent rather than opaque, sitting on a blurred plate that picks up the colour of the content scrolling…"
has_js: "false"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: iOS-Style Compose Floating Button
Source: https://codefronts.com/components/css-floating-buttons/ios-style-compose-floating-button/

What a compose button looks like on iOS: translucent rather than opaque, sitting on a blurred plate that picks up the colour of the content scrolling underneath, with a spring-loaded press that overshoots on release. Also handles the two things web clones forget — env(safe-area-inset-bottom) so the button clears the home indicator, and a specular top highlight that makes the glass read as a physical lens.
## HTML
```html
<section class="fb-02" aria-label="iOS style floating compose button demo">
  <div class="fb-02__stage">
    <div class="fb-02__phone">
      <div class="fb-02__screen">
        <div class="fb-02__status"><span>9:41</span><span class="fb-02__statusR"><i class="fb-02__sig"></i><i class="fb-02__bat"></i></span></div>
        <div class="fb-02__nav"><span class="fb-02__navTitle">Notes</span><span class="fb-02__navSub">iCloud · 24 notes</span></div>
        <div class="fb-02__scroll">
          <article class="fb-02__note"><b>Type scale for 2027</b><span>Variable weight axis on the display face, 3 optical sizes…</span><time>Yesterday</time></article>
          <article class="fb-02__note"><b>FAB motion spec</b><span>Press 90ms in, 380ms spring out, overshoot 1.04 max…</span><time>Tuesday</time></article>
          <article class="fb-02__note fb-02__note--img"><b>Studio moodboard</b><span>Warm concrete, brushed steel, one hot accent.</span><time>Mon</time></article>
          <article class="fb-02__note"><b>Glass tokens</b><span>blur 22, saturate 180, tint 78% — anything more is soup.</span><time>Mon</time></article>
        </div>
        <button class="fb-02__compose" type="button" aria-label="Compose a new note">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 20h4l10.5-10.5-4-4L4 16v4z" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round"/><path d="M14.5 5.5l4 4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
        </button>
        <div class="fb-02__home" aria-hidden="true"></div>
      </div>
    </div>
    <div class="fb-02__copy">
      <p class="fb-02__eyebrow">backdrop-filter · spring easing</p>
      <h2 class="fb-02__title">Glass that samples the scroll</h2>
      <p class="fb-02__sub">Press it. Fast in at 90ms, springy out at 380ms with a 4% overshoot — the asymmetry is the whole trick.</p>
      <p class="fb-02__chip">blur(22px) saturate(180%) · env(safe-area-inset-bottom)</p>
    </div>
  </div>
</section>
```
## CSS
```css
.fb-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-02-bg);
  --fb-02-bg: radial-gradient(120% 90% at 15% 0%,oklch(0.34 0.09 265),oklch(0.19 0.04 265) 62%);
  --fb-02-tint: oklch(0.63 0.19 258);
  --fb-02-ink: oklch(0.97 0.01 265);
  --fb-02-mut: oklch(0.78 0.02 265);
  font-family: -apple-system,'SF Pro Text','Segoe UI',system-ui,sans-serif;
  color: var(--fb-02-ink);
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,52px);
}

.fb-02 *,
.fb-02 *::before,
.fb-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-02__stage {
  width: min(100%,880px);
  display: grid;
  gap: clamp(24px,4vw,46px);
  justify-items: center;
  align-items: center;
}

.fb-02__phone {
  width: min(92vw,320px);
  aspect-ratio: 9/19;
  padding: 11px;
  border-radius: 52px;
  background: linear-gradient(160deg,oklch(0.42 0.01 265),oklch(0.2 0.01 265));
  box-shadow: 0 40px 90px -30px oklch(0.1 0.03 265/.85),inset 0 1px 0 oklch(1 0 0/.28);
}

.fb-02__screen {
  position: relative;
  height: 100%;
  border-radius: 42px;
  overflow: hidden;
  background: oklch(0.99 0.004 265);
  color: oklch(0.2 0.01 265);
  display: flex;
  flex-direction: column;
  isolation: isolate;
}

.fb-02__status {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 22px 2px;
  font-size: 12.5px;
  font-weight: 650;
}

.fb-02__statusR {
  display: flex;
  align-items: center;
  gap: 5px;
}

.fb-02__sig {
  width: 15px;
  height: 10px;
  background: currentColor;
  clip-path: polygon(0 70%,22% 70%,22% 100%,0 100%,0 70%,33% 45%,55% 45%,55% 100%,33% 100%,33% 45%,66% 22%,88% 22%,88% 100%,66% 100%);
}

.fb-02__bat {
  width: 22px;
  height: 11px;
  border: 1.4px solid currentColor;
  border-radius: 3px;
  position: relative;
}

.fb-02__bat::after {
  content: "";
  position: absolute;
  inset: 1.6px;
  width: 62%;
  background: currentColor;
  border-radius: 1px;
}

.fb-02__nav {
  padding: 6px 20px 10px;
  display: grid;
  gap: 1px;
}

.fb-02__navTitle {
  font-size: 27px;
  font-weight: 750;
  letter-spacing: -.03em;
}

.fb-02__navSub {
  font-size: 11.5px;
  color: oklch(0.58 0.01 265);
}

.fb-02__scroll {
  flex: 1;
  overflow: auto;
  padding: 0 14px 96px;
  display: grid;
  gap: 9px;
  align-content: start;
  scrollbar-width: none;
}

.fb-02__scroll::-webkit-scrollbar {
  display: none;
}

.fb-02__note {
  display: grid;
  gap: 3px;
  padding: 13px 15px;
  border-radius: 15px;
  background: oklch(0.96 0.006 265);
}

.fb-02__note b {
  font-size: 14px;
  font-weight: 640;
  letter-spacing: -.01em;
}

.fb-02__note span {
  font-size: 12px;
  line-height: 1.45;
  color: oklch(0.55 0.01 265);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.fb-02__note time {
  font-size: 10.5px;
  color: oklch(0.65 0.01 265);
  font-variant-numeric: tabular-nums;
}

.fb-02__note--img {
  background: linear-gradient(180deg,oklch(0.35 0.06 40/.72),oklch(0.22 0.05 40/.9)),url("https://images.unsplash.com/photo-1487958449943-2429e8be8625?q=80&w=900&auto=format&fit=crop") center/cover;
  color: oklch(0.98 0.01 40);
}

.fb-02__note--img span,
.fb-02__note--img time {
  color: oklch(0.9 0.02 40);
}

.fb-02__compose {
  position: absolute;
  right: 18px;
  bottom: calc(30px + env(safe-area-inset-bottom));
  z-index: 3;
  inline-size: 58px;
  block-size: 58px;
  border: 0;
  border-radius: 22px;
  display: grid;
  place-items: center;
  cursor: pointer;
  color: oklch(0.99 0.01 258);
  background: color-mix(in oklch,var(--fb-02-tint) 78%,transparent);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
  backdrop-filter: blur(22px) saturate(180%);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.55),inset 0 -1px 0 oklch(0 0 0/.1),0 10px 30px -8px oklch(0.2 0.06 258/.5);
  transition: transform .38s cubic-bezier(.2,1.5,.4,1),box-shadow .3s ease;
}

.fb-02__compose svg {
  width: 25px;
  height: 25px;
}

.fb-02__compose:hover {
  box-shadow: inset 0 1px 0 oklch(1 0 0/.6),0 14px 34px -8px oklch(0.2 0.06 258/.62);
}

.fb-02__compose:active {
  transform: scale(.9);
  transition-duration: .09s;
}

.fb-02__compose:focus-visible {
  outline: 3px solid oklch(0.99 0.01 258);
  outline-offset: 3px;
}

.fb-02__home {
  position: absolute;
  left: 50%;
  bottom: 8px;
  translate: -50% 0;
  width: 118px;
  height: 5px;
  border-radius: 99px;
  background: oklch(0.2 0.01 265/.35);
}

.fb-02__copy {
  display: grid;
  gap: 11px;
  justify-items: center;
  text-align: center;
  max-width: 52ch;
}

.fb-02__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.8 0.12 258);
}

.fb-02__title {
  font-size: clamp(25px,4.2vw,40px);
  line-height: 1.07;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-02__sub {
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.6;
  color: var(--fb-02-mut);
  text-wrap: pretty;
}

.fb-02__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-02-mut);
  padding: 8px 14px;
  border: 1px solid oklch(1 0 0/.16);
  border-radius: 99px;
}

@media (min-width: 800px) {
  .fb-02__stage {
    grid-template-columns: auto 1fr;
  }

  .fb-02__copy {
    text-align: left;
    justify-items: start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fb-02__compose {
    transition: none;
  }
}
```
