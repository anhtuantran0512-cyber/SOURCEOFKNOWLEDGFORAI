---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/ember-pulse/"
title: "Ember Pulse Dark Mode Alert Card"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "The card that has to be read: a billing failure notice on a dark surface with a warm ember accent, a slow pulse on the status node and a retry action that…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ember Pulse Dark Mode Alert Card
Source: https://codefronts.com/design-styles/css-dark-mode-ui/ember-pulse/

The card that has to be read: a billing failure notice on a dark surface with a warm ember accent, a slow pulse on the status node and a retry action that looks like the primary path. Severity is carried by an icon, a labelled chip and the copy itself — never by the colour alone — and the pulse stops entirely for visitors who ask for reduced motion.
## HTML
```html
<div class="dmu-22">
  <div class="dmu-22__stage">
    <section class="dmu-22__card" role="alert" aria-labelledby="dmu-22-t">
      <header class="dmu-22__head">
        <span class="dmu-22__node" aria-hidden="true">
          <span class="dmu-22__ring dmu-22__ring--a"></span>
          <span class="dmu-22__ring dmu-22__ring--b"></span>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4.4 21 19.6H3Z"/><path d="M12 9.8v4.2M12 16.4v.1"/></svg>
        </span>
        <div class="dmu-22__headText">
          <span class="dmu-22__chip">Action required</span>
          <h1 class="dmu-22__title" id="dmu-22-t">Payment for invoice INV-4821 failed</h1>
          <p class="dmu-22__body">Your card ending 4242 was declined on 14 August. Production stays online for 5 more days, then deployments pause automatically.</p>
        </div>
      </header>

      <dl class="dmu-22__facts">
        <div><dt>Amount due</dt><dd>&#36;1,480.00</dd></div>
        <div><dt>Attempted</dt><dd>3&times; &middot; 06:12 UTC</dd></div>
        <div><dt>Grace ends</dt><dd>19 Aug, 23:59 UTC</dd></div>
      </dl>

      <ul class="dmu-22__services">
        <li><span class="dmu-22__sdot dmu-22__sdot--ok" aria-hidden="true"></span>Edge runtime<em>Online</em></li>
        <li><span class="dmu-22__sdot dmu-22__sdot--warn" aria-hidden="true"></span>Preview deployments<em>Paused in 5 days</em></li>
        <li><span class="dmu-22__sdot dmu-22__sdot--warn" aria-hidden="true"></span>Log retention<em>Reduced to 24h</em></li>
      </ul>

      <footer class="dmu-22__foot">
        <p class="dmu-22__contact">Billing owner: Sam Rivera</p>
        <div class="dmu-22__acts">
          <button class="dmu-22__btn" type="button">View invoice</button>
          <button class="dmu-22__btn dmu-22__btn--primary" type="button">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="2.8" y="5.4" width="18.4" height="13.2" rx="2.2"/><path d="M2.8 10h18.4"/></svg>
            Update payment method
          </button>
        </div>
      </footer>
    </section>
  </div>
</div>
```
## CSS
```css
.dmu-22 {
  --bg: #0a0806;
  --surface: #15110e;
  --raised: #1e1813;
  --ink: #f7f1ea;
  --muted: #b0a196;
  --line: #302620;
  --ember: #ff8b3d;
  --ember-ink: #2b0e02;
  --ok: #6ee7a8;
  --focus: #ffc48a;
  --shadow: rgba(0,0,0,.8);
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(110% 70% at 50% 0%,#1a1109,var(--bg) 64%),var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-22,
.dmu-22 *,
.dmu-22 *::before,
.dmu-22 *::after {
  box-sizing: border-box;
}

.dmu-22__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-22__card {
  width: min(42rem,100%);
  display: grid;
  gap: 1rem;
  padding: clamp(1.3rem,3.5vw,2rem);
  border-radius: 1.2rem;
  color: var(--ink);
  background: linear-gradient(180deg,#20150d,var(--surface) 62%);
  border: 1px solid color-mix(in oklab,var(--ember) 28%,var(--line));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.05), 0 0 60px -30px rgba(255,139,61,.35), 0 44px 80px -55px var(--shadow);
}

@supports (background: color-mix(in oklab, white 10%, black)) {
  .dmu-22__card {
    background: linear-gradient(180deg,color-mix(in oklab,var(--ember) 9%,var(--surface)),var(--surface) 62%);
  }
}

.dmu-22__head {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 1rem;
  align-items: start;
}

.dmu-22__node {
  position: relative;
  display: grid;
  place-items: center;
  width: 2.9rem;
  height: 2.9rem;
  border-radius: 50%;
  background: color-mix(in oklab,var(--ember) 18%,transparent);
  color: var(--ember);
  flex: none;
}

.dmu-22__node svg {
  width: 1.4rem;
  height: 1.4rem;
  position: relative;
  z-index: 1;
}

.dmu-22__ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 1px solid var(--ember);
  animation: dmu-22-ring 2.6s ease-out infinite;
}

.dmu-22__ring--b {
  animation-delay: 1.15s;
}

@keyframes dmu-22-ring {
  0% {
    scale: .72;
    opacity: .55;
  }

  70% {
    scale: 2;
    opacity: 0;
  }

  100% {
    scale: 2;
    opacity: 0;
  }
}

.dmu-22__headText {
  display: grid;
  gap: .4rem;
}

.dmu-22__chip {
  width: max-content;
  display: inline-flex;
  align-items: center;
  font-family: var(--mono);
  font-size: .67rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  padding: .26rem .5rem;
  border-radius: .35rem;
  color: var(--ember);
  border: 1px solid color-mix(in oklab,var(--ember) 45%,transparent);
  background: color-mix(in oklab,var(--ember) 12%,transparent);
}

.dmu-22__title {
  margin: 0;
  font-size: clamp(1.15rem,2.8vw,1.5rem);
  font-weight: 640;
  letter-spacing: -.03em;
  line-height: 1.25;
  text-wrap: balance;
}

.dmu-22__body {
  margin: 0;
  font-size: .9rem;
  line-height: 1.65;
  color: var(--muted);
  max-width: 52ch;
  text-wrap: pretty;
}

.dmu-22__facts {
  margin: 0;
  display: grid;
  gap: .5rem;
  grid-template-columns: repeat(auto-fit,minmax(9rem,1fr));
  padding: .9rem 1rem;
  border-radius: .85rem;
  background: var(--raised);
  border: 1px solid var(--line);
}

.dmu-22__facts div {
  display: grid;
  gap: .15rem;
}

.dmu-22__facts dt {
  font-size: .72rem;
  letter-spacing: .04em;
  color: var(--muted);
}

.dmu-22__facts dd {
  margin: 0;
  font-family: var(--mono);
  font-variant-numeric: tabular-nums;
  font-size: .9rem;
}

.dmu-22__services {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .3rem;
}

.dmu-22__services li {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .6rem .75rem;
  border-radius: .6rem;
  background: var(--raised);
  font-size: .84rem;
}

.dmu-22__services em {
  margin-left: auto;
  font-style: normal;
  font-family: var(--mono);
  font-size: .74rem;
  color: var(--muted);
}

.dmu-22__sdot {
  width: .55rem;
  height: .55rem;
  border-radius: 50%;
  flex: none;
}

.dmu-22__sdot--ok {
  background: var(--ok);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--ok) 20%,transparent);
}

.dmu-22__sdot--warn {
  background: var(--ember);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--ember) 20%,transparent);
}

.dmu-22__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  padding-top: .9rem;
  border-top: 1px solid var(--line);
}

.dmu-22__contact {
  margin: 0;
  font-size: .78rem;
  color: var(--muted);
}

.dmu-22__acts {
  display: flex;
  gap: .5rem;
  flex-wrap: wrap;
}

.dmu-22__btn {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-height: 2.85rem;
  padding: 0 1.1rem;
  border-radius: .7rem;
  cursor: pointer;
  font: inherit;
  font-size: .86rem;
  font-weight: 560;
  background: var(--raised);
  color: var(--ink);
  border: 1px solid var(--line);
  transition: translate .18s ease, filter .18s ease;
}

.dmu-22__btn svg {
  width: 1.05rem;
  height: 1.05rem;
}

.dmu-22__btn:hover {
  translate: 0 -1px;
}

.dmu-22__btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

.dmu-22__btn--primary {
  background: var(--ember);
  color: var(--ember-ink);
  border-color: transparent;
  font-weight: 620;
  box-shadow: 0 0 28px -8px rgba(255,139,61,.5);
}

.dmu-22__btn--primary:hover {
  filter: brightness(1.06);
}

@media (prefers-reduced-motion: reduce) {
  .dmu-22__ring {
    animation: none;
    opacity: 0;
  }

  .dmu-22__btn {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-22__card,
    .dmu-22__facts,
    .dmu-22__services li {
    border: 1px solid CanvasText;
    box-shadow: none;
    background: Canvas;
  }

  .dmu-22__ring {
    display: none;
  }

  .dmu-22__btn--primary {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }
}
```
