---
source: "codefronts"
url: "https://codefronts.com/components/css-skeleton-loaders/avatar-card/"
title: "Avatar Profile Skeleton Loader"
section: "components"
category: "css-skeleton-loaders"
category_name: "CSS Skeleton Loaders"
description: "The pattern Slack, Discord and Twitter all show while a message resolves: a 48px circle plus a name line and a subtitle line."
has_js: "false"
---

Here's a working CSS Skeleton Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Avatar Profile Skeleton Loader
Source: https://codefronts.com/components/css-skeleton-loaders/avatar-card/

The pattern Slack, Discord and Twitter all show while a message resolves: a 48px circle plus a name line and a subtitle line. It looks trivial — the craft is in the details, which is why this demo puts the skeleton immediately above the resolved rows so you can check the circle diameter, the baseline gap and the two line widths against the real thing.
## HTML
```html
<div class="sk-13">
  <div class="sk-13__stage">
    <section class="sk-13__wrap" aria-labelledby="sk-13-h">
      <header class="sk-13__head">
        <p class="sk-13__eyebrow">--av: 3rem · 48px</p>
        <h2 class="sk-13__h" id="sk-13-h">Circle, name line, subtitle line</h2>
        <p class="sk-13__sub">The skeleton is above, the resolved rows below. Same avatar token, same bar heights as the text metrics, same 0.45rem gap — so the swap moves nothing.</p>
      </header>

      <div class="sk-13__panel">
        <p class="sk-13__label sk-13__label--on">pending</p>
        <ul class="sk-13__list" role="status" aria-live="polite">
          <span class="sk-13__vh">Loading three team members…</span>
          <li class="sk-13__item" aria-hidden="true"><span class="sk-13__bar sk-13__avatar"></span><div class="sk-13__ident"><span class="sk-13__bar sk-13__bar--name" style="inline-size:8.5rem"></span><span class="sk-13__bar sk-13__bar--sub" style="inline-size:12rem"></span></div></li>
          <li class="sk-13__item" aria-hidden="true"><span class="sk-13__bar sk-13__avatar"></span><div class="sk-13__ident"><span class="sk-13__bar sk-13__bar--name" style="inline-size:6.5rem"></span><span class="sk-13__bar sk-13__bar--sub" style="inline-size:14rem"></span></div></li>
          <li class="sk-13__item" aria-hidden="true"><span class="sk-13__bar sk-13__avatar"></span><div class="sk-13__ident"><span class="sk-13__bar sk-13__bar--name" style="inline-size:9.5rem"></span><span class="sk-13__bar sk-13__bar--sub" style="inline-size:10.5rem"></span></div></li>
        </ul>

        <hr class="sk-13__rule">

        <p class="sk-13__label">resolved</p>
        <ul class="sk-13__list">
          <li class="sk-13__item">
            <img class="sk-13__pic" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&amp;fit=crop&amp;w=96&amp;h=96&amp;q=70" width="96" height="96" alt="Alex Chen" loading="lazy" decoding="async">
            <div class="sk-13__ident"><p class="sk-13__name">Alex Chen</p><p class="sk-13__role">Staff Engineer · Platform</p></div>
          </li>
          <li class="sk-13__item">
            <img class="sk-13__pic" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&amp;fit=crop&amp;w=96&amp;h=96&amp;q=70" width="96" height="96" alt="Priya Sharma" loading="lazy" decoding="async">
            <div class="sk-13__ident"><p class="sk-13__name">Priya Sharma</p><p class="sk-13__role">Design Systems · Interfaces</p></div>
          </li>
          <li class="sk-13__item">
            <img class="sk-13__pic" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&amp;fit=crop&amp;w=96&amp;h=96&amp;q=70" width="96" height="96" alt="Jordan Lee" loading="lazy" decoding="async">
            <div class="sk-13__ident"><p class="sk-13__name">Jordan Lee</p><p class="sk-13__role">Platform · Release</p></div>
          </li>
        </ul>
      </div>

      <aside class="sk-13__spec" aria-label="Recipe">
        <p class="sk-13__srow"><span class="sk-13__skey">circle</span><span class="sk-13__sval">inline-size: var(--av); aspect-ratio: 1; border-radius: 999px; flex: none</span></p>
        <p class="sk-13__srow"><span class="sk-13__skey">bars</span><span class="sk-13__sval">name .8rem tall, subtitle .7rem — matched to the resolved text metrics</span></p>
        <p class="sk-13__srow"><span class="sk-13__skey">gap</span><span class="sk-13__sval">.45rem between the two bars, identical to the resolved stack</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.sk-13 {
  --av: 3rem;
  --bg: #08070c;
  --bg2: #100e18;
  --surface: rgba(255,255,255,.032);
  --line: rgba(255,255,255,.1);
  --ink: #f5f3fb;
  --muted: rgba(245,243,251,.62);
  --faint: rgba(245,243,251,.42);
  --accent: #f0abfc;
  --sk: rgba(245,243,251,.1);
  --sheen: rgba(245,243,251,.17);
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(58% 40% at 18% -6%, rgba(240,171,252,.12) 0%, transparent 60%), linear-gradient(178deg,var(--bg2) 0%,var(--bg) 62%);
}

.sk-13 *,
.sk-13 *::before,
.sk-13 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 320)) {
  .sk-13 {
    --ink: oklch(0.97 0.008 315);
    --muted: oklch(0.97 0.008 315 / .62);
    --faint: oklch(0.97 0.008 315 / .42);
    --accent: oklch(0.83 0.13 325);
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .sk-13 {
    --sk: color-mix(in oklab, currentColor 10%, transparent);
    --sheen: color-mix(in oklab, currentColor 17%, transparent);
  }
}

.sk-13__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.sk-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.15rem,4vw,3.25rem);
}

.sk-13__wrap {
  inline-size: min(52rem,100%);
  display: grid;
  gap: clamp(1rem,2.2vw,1.6rem);
}

.sk-13__head {
  display: grid;
  gap: .6rem;
}

.sk-13__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sk-13__h {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.032em;
  line-height: 1.06;
  text-wrap: balance;
}

.sk-13__sub {
  margin: 0;
  font-size: clamp(.94rem,1.3vw,1.02rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sk-13__panel {
  display: grid;
  gap: .8rem;
  padding: clamp(1.1rem,2.2vw,1.6rem);
  border: 1px solid var(--line);
  border-radius: 1.15rem;
  background: var(--surface);
  box-shadow: 0 28px 66px -44px rgba(0,0,0,.9);
}

.sk-13__label {
  margin: 0;
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--faint);
}

.sk-13__label--on {
  color: var(--accent);
}

.sk-13__rule {
  margin: .5rem 0;
  border: 0;
  border-block-start: 1px solid var(--line);
}

.sk-13__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1rem;
}

.sk-13__item {
  display: flex;
  align-items: center;
  gap: 1rem;
  min-block-size: var(--av);
}

.sk-13__ident {
  display: grid;
  gap: .45rem;
  min-inline-size: 0;
}

.sk-13__pic {
  inline-size: var(--av);
  aspect-ratio: 1;
  border-radius: 999px;
  object-fit: cover;
  background: var(--sk);
  flex: none;
}

.sk-13__name {
  margin: 0;
  font-size: 1rem;
  font-weight: 500;
  letter-spacing: -.01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sk-13__role {
  margin: 0;
  font-size: .85rem;
  color: var(--muted);
}

.sk-13__bar {
  display: block;
  position: relative;
  overflow: hidden;
  block-size: .8rem;
  border-radius: 6px;
  background: var(--sk);
}

.sk-13__bar::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg, transparent 18%, var(--sheen) 50%, transparent 82%);
  translate: -100% 0;
  animation: sk-13-sheen 1.4s linear infinite;
}

@keyframes sk-13-sheen {
  to {
    translate: 100% 0;
  }
}

.sk-13__bar--sub {
  block-size: .7rem;
}

.sk-13__avatar {
  inline-size: var(--av);
  block-size: auto;
  aspect-ratio: 1;
  border-radius: 999px;
  flex: none;
}

.sk-13__spec {
  padding: clamp(.85rem,1.5vw,1.1rem) clamp(1rem,1.8vw,1.3rem);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  display: grid;
  gap: .45rem;
}

.sk-13__srow {
  margin: 0;
  display: flex;
  gap: .9rem;
  flex-wrap: wrap;
  font-family: var(--mono);
  font-size: .74rem;
  line-height: 1.5;
}

.sk-13__skey {
  min-inline-size: 3.4rem;
  color: var(--accent);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .66rem;
  padding-block-start: .12rem;
}

.sk-13__sval {
  color: var(--muted);
  word-break: break-word;
}

.sk-13[data-theme="light"] {
  --bg: #fbf8fc;
  --bg2: #fff;
  --surface: rgba(16,8,20,.026);
  --line: rgba(16,8,20,.11);
  --ink: #100814;
  --muted: rgba(16,8,20,.62);
  --faint: rgba(16,8,20,.44);
  --accent: #a21caf;
  background: linear-gradient(178deg,#fff 0%,#f4ecf6 100%);
}

@media (prefers-color-scheme: light) {
  .sk-13:not([data-theme="dark"]) {
    --bg: #fbf8fc;
    --bg2: #fff;
    --surface: rgba(16,8,20,.026);
    --line: rgba(16,8,20,.11);
    --ink: #100814;
    --muted: rgba(16,8,20,.62);
    --faint: rgba(16,8,20,.44);
    --accent: #a21caf;
    background: linear-gradient(178deg,#fff 0%,#f4ecf6 100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sk-13__bar::after {
    animation: none;
    background: none;
  }

  .sk-13__bar {
    background: linear-gradient(105deg, var(--sk) 0%, var(--sheen) 50%, var(--sk) 100%);
  }
}

@media (forced-colors: active) {
  .sk-13__bar {
    background: GrayText;
    forced-color-adjust: none;
  }

  .sk-13__bar::after {
    animation: none;
    background: none;
  }

  .sk-13__panel,
    .sk-13__spec {
    border-color: CanvasText;
  }
}
```
