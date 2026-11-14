---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-alert-badge-shake-animation/"
title: "CSS Alert Badge Shake Animation"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Badges that refuse to be ignored: a sidebar rail whose alert count rattles on a polite schedule (with a ping halo, while read items sit still), and a CI…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Alert Badge Shake Animation
Source: https://codefronts.com/motion/css-shake-animation/css-alert-badge-shake-animation/

Badges that refuse to be ignored: a sidebar rail whose alert count rattles on a polite schedule (with a ping halo, while read items sit still), and a CI status pill that keeps twitching until you actually click resolve — state-bound motion that stops the moment the state does.
## HTML
```html
<div class="shk-19-group">
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="shk-19a" aria-label="Sidebar with rattling alert badge">
  <nav class="shk-19a__rail" aria-label="Demo navigation">
    <a class="shk-19a__item" href="#" onclick="return false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9.5 12 3l9 6.5V21a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"></path></svg>Home</a>
    <a class="shk-19a__item is-alert" href="#" onclick="return false" aria-label="Inbox, 4 unread alerts"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 12h-6l-2 3h-4l-2-3H2"></path><path d="M5.4 5.1 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.4-6.9A2 2 0 0 0 16.8 4H7.2a2 2 0 0 0-1.8 1.1z"></path></svg>Inbox<span class="shk-19a__badge" aria-hidden="true">4<i class="shk-19a__halo"></i></span></a>
    <a class="shk-19a__item" href="#" onclick="return false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"></rect><path d="M3 10h18M9 4v16"></path></svg>Projects</a>
    <a class="shk-19a__item" href="#" onclick="return false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09a1.65 1.65 0 0 0-1-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09a1.65 1.65 0 0 0 1.51-1 1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33h0a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51h0a1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82v0a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>Settings</a>
  </nav>
  <p class="shk-19a__hint" aria-hidden="true">the badge rattles ~½s of every 3s — read items hold perfectly still</p>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<section class="shk-19b" aria-label="CI status pill that shakes until resolved">
  <div class="shk-19b__bar">
    <span class="shk-19b__repo">meridian/web · <b>main</b></span>
    <span class="shk-19b__pill" id="shk-19b-pill" data-state="failing" aria-live="polite"><i class="shk-19b__dot" aria-hidden="true"></i><span class="shk-19b__count" id="shk-19b-count">3 checks failing</span></span>
    <button class="shk-19b__fix" id="shk-19b-fix" type="button">Re-run checks</button>
  </div>
  <p class="shk-19b__hint" aria-hidden="true">the twitch is bound to data-state="failing" — resolving flips the attribute and ALL motion stops atomically</p>
</section>
</div>
```
## CSS
```css
.shk-19-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-19-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-19a,
.shk-19a *,
.shk-19a *::before,
.shk-19a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-19a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 20px;
  padding: 48px 24px;
  background: linear-gradient(180deg,#13161d,#0d0f14);
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
}

.shk-19a__rail {
  width: min(280px,86vw);
  padding: 12px;
  border-radius: 18px;
  background: rgba(255,255,255,.045);
  border: 1px solid rgba(165,185,220,.14);
  display: grid;
  gap: 4px;
  box-shadow: 0 40px 80px -45px rgba(0,0,0,.95);
}

.shk-19a__item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 13px;
  border-radius: 11px;
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  color: rgba(222,230,246,.7);
  transition: background .15s,color .15s;
}

.shk-19a__item svg {
  width: 19px;
  height: 19px;
  flex: none;
}

.shk-19a__item:hover {
  background: rgba(255,255,255,.07);
  color: #eef2fb;
}

.shk-19a__item.is-alert {
  color: #eef2fb;
}

.shk-19a__badge {
  position: relative;
  margin-left: auto;
  min-width: 22px;
  height: 22px;
  padding: 0 6px;
  display: grid;
  place-items: center;
  font-size: 11.5px;
  font-weight: 800;
  color: #fff;
  background: oklch(0.6 0.21 25);
  border-radius: 999px;
  animation: shk-19a-rattle 3s ease-in-out infinite;
}

.shk-19a__halo {
  position: absolute;
  inset: 0;
  border-radius: 999px;
  border: 2px solid oklch(0.6 0.21 25);
  animation: shk-19a-halo 3s ease-out infinite;
}

.shk-19a__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(222,230,246,.4);
}

@keyframes shk-19a-rattle {
  0%,
    4% {
    translate: 0 0;
    rotate: 0deg;
  }

  6% {
    translate: -1.5px 0;
    rotate: -6deg;
  }

  8.5% {
    translate: 1.5px 0;
    rotate: 5deg;
  }

  11% {
    translate: -1px 0;
    rotate: -3deg;
  }

  13.5% {
    translate: .5px 0;
    rotate: 1.5deg;
  }

  16%,
    100% {
    translate: 0 0;
    rotate: 0deg;
  }
}

@keyframes shk-19a-halo {
  0%,
    4% {
    opacity: .9;
    scale: 1;
  }

  22% {
    opacity: 0;
    scale: 2;
  }

  100% {
    opacity: 0;
    scale: 2;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-19a__badge,
    .shk-19a__halo {
    animation: none;
  }

  .shk-19a__halo {
    opacity: 0;
  }
}

.shk-19b,
.shk-19b *,
.shk-19b *::before,
.shk-19b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-19b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 18px;
  padding: 48px 24px;
  background: #0e1014;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-19b__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 16px;
  padding: 15px 20px;
  border-radius: 14px;
  background: #161a21;
  border: 1px solid rgba(170,190,220,.14);
}

.shk-19b__repo {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 13px;
  color: rgba(215,226,245,.6);
}

.shk-19b__repo b {
  color: #e8eefa;
  font-weight: 600;
}

.shk-19b__pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 14px;
  border-radius: 999px;
  font-size: 13px;
  font-weight: 700;
  transition: background .3s,color .3s,border-color .3s;
  border: 1px solid;
}

.shk-19b__pill[data-state="failing"] {
  color: oklch(0.82 0.13 25);
  background: oklch(0.6 0.21 25 / .13);
  border-color: oklch(0.6 0.21 25 / .45);
}

.shk-19b__pill[data-state="running"] {
  color: oklch(0.85 0.12 85);
  background: oklch(0.75 0.14 85 / .12);
  border-color: oklch(0.75 0.14 85 / .4);
}

.shk-19b__pill[data-state="passing"] {
  color: oklch(0.85 0.13 158);
  background: oklch(0.75 0.15 158 / .12);
  border-color: oklch(0.75 0.15 158 / .4);
}

.shk-19b__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: currentColor;
}

.shk-19b__pill[data-state="running"] .shk-19b__dot {
  animation: shk-19b-blink .8s ease-in-out infinite;
}

.shk-19b__pill[data-state="failing"] .shk-19b__count {
  display: inline-block;
  animation: shk-19b-twitch 2.4s ease-in-out infinite;
}

.shk-19b__pill[data-state="passing"] {
  animation: shk-19b-settle .5s cubic-bezier(.34,1.56,.64,1);
}

.shk-19b__fix {
  margin-left: auto;
  padding: 10px 18px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 700;
  color: #0e1014;
  background: #e8eefa;
  border: 0;
  border-radius: 10px;
  cursor: pointer;
  transition: filter .2s,scale .12s;
}

.shk-19b__fix:hover {
  filter: brightness(1.08);
}

.shk-19b__fix:active {
  scale: .96;
}

.shk-19b__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(215,226,245,.4);
  max-width: 480px;
  justify-self: center;
}

@keyframes shk-19b-twitch {
  0%,
    6% {
    translate: 0 0;
  }

  7.5% {
    translate: -2px 0;
  }

  9% {
    translate: 2px 0;
  }

  10.5% {
    translate: -1px 0;
  }

  12% {
    translate: 0 0;
  }

  54% {
    translate: 0 0;
  }

  55.5% {
    translate: -2px 0;
  }

  57% {
    translate: 1.5px 0;
  }

  58.5%,
    100% {
    translate: 0 0;
  }
}

@keyframes shk-19b-blink {
  50% {
    opacity: .35;
  }
}

@keyframes shk-19b-settle {
  40% {
    scale: 1.06;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-19b__pill[data-state="failing"] .shk-19b__count,
    .shk-19b__pill[data-state="passing"] {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — badge rattle and halo share one 3s loop (burst in the first 16%). Give each badge on a page a different period (2.4s / 3.1s / 3.7s) so alerts never synchronize. */

(function(){
  var pill=document.getElementById('shk-19b-pill'),fix=document.getElementById('shk-19b-fix'),
      count=document.getElementById('shk-19b-count'); if(!pill) return;
  fix.addEventListener('click',function(){
    if(pill.dataset.state!=='failing') return;
    pill.dataset.state='running'; count.textContent='Re-running 3 checks…'; fix.disabled=true; fix.style.opacity='.5';
    setTimeout(function(){
      pill.dataset.state='passing';                 // one attribute write: motion, color, copy all flip
      count.textContent='All checks passing';
      fix.textContent='Resolved'; 
    },1600);
  });
})();
```
