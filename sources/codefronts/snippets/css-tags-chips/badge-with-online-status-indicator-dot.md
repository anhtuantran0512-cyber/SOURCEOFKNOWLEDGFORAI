---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/badge-with-online-status-indicator-dot/"
title: "Badge with Online Status Indicator Dot"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "The status language every chat and SaaS product speaks — online, away, busy, offline — rendered the way the big messengers render it: a dot cut into the…"
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Badge with Online Status Indicator Dot
Source: https://codefronts.com/snippets/css-tags-chips/badge-with-online-status-indicator-dot/

The status language every chat and SaaS product speaks — online, away, busy, offline — rendered the way the big messengers render it: a dot cut into the avatar's corner with a ring that matches the surface behind it, so it reads as punched-through, not stuck-on. Online pulses a soft sonar ring, away is a true crescent cut with a CSS mask, busy carries the do-not-disturb dash, offline hollows out — and a bonus three-dot typing chip bounces. One data-status attribute drives everything.
## HTML
```html
<section class="ctc-03" aria-label="Online status indicator dot demo">
  <div class="ctc-03__stage">
    <div class="ctc-03__wrap">
      <header class="ctc-03__head">
        <p class="ctc-03__kicker">Status dots · one attribute, five states</p>
        <h1>Presence you can read at 15px</h1>
      </header>
      <ul class="ctc-03__hero" aria-label="Status dot states at hero size">
        <li data-status="online"><span class="ctc-03__avatar ctc-03__avatar--xl" style="--img:url(https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=160&q=60);--h:250"><i data-dot></i></span><b>Online</b><small>sonar ping ::after</small></li>
        <li data-status="away"><span class="ctc-03__avatar ctc-03__avatar--xl" style="--img:url(https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=160&q=60);--h:20"><i data-dot></i></span><b>Away</b><small>crescent via <code>mask</code></small></li>
        <li data-status="busy"><span class="ctc-03__avatar ctc-03__avatar--xl" style="--img:url(https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=160&q=60);--h:140"><i data-dot></i></span><b>Busy · DND</b><small>gradient dash</small></li>
        <li data-status="offline"><span class="ctc-03__avatar ctc-03__avatar--xl" data-fallback="KL" style="--h:300"><i data-dot></i></span><b>Offline</b><small>inset box-shadow ring</small></li>
        <li data-status="typing"><span class="ctc-03__avatar ctc-03__avatar--xl" style="--img:url(https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=160&q=60);--h:330"><i data-dot></i></span><b>Typing</b><small>staggered bounce</small></li>
      </ul>
      <div class="ctc-03__roster" role="group" aria-label="The same dots in a roster at 40px">
        <p class="ctc-03__label">In context — 40px roster, same CSS</p>
        <ul class="ctc-03__list">
          <li data-status="online"><span class="ctc-03__avatar" style="--img:url(https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=120&q=60);--h:250"><i data-dot></i></span><b>Jonas Reid</b><span class="ctc-03__state">Active now</span></li>
          <li data-status="typing"><span class="ctc-03__avatar" style="--img:url(https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=120&q=60);--h:330"><i data-dot></i></span><b>Mara Voss</b><span class="ctc-03__typing" aria-label="typing"><i></i><i></i><i></i></span></li>
          <li data-status="away"><span class="ctc-03__avatar" style="--img:url(https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=120&q=60);--h:20"><i data-dot></i></span><b>Priya Anand</b><span class="ctc-03__state">Back at 2:30</span></li>
          <li data-status="busy"><span class="ctc-03__avatar" data-fallback="KL" style="--h:300"><i data-dot></i></span><b>Kai Lindgren</b><span class="ctc-03__state">In a call</span></li>
          <li data-status="offline"><span class="ctc-03__avatar" style="--img:url(https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=120&q=60);--h:80"><i data-dot></i></span><b>Ana Duarte</b><span class="ctc-03__state">Last seen 1d</span></li>
        </ul>
      </div>
      <p class="ctc-03__note">Every row is just <code>&lt;li data-status="away"&gt;</code> — dot color, dot shape and the trailing label all key off that one attribute. Shape + text back up every color, so the system survives color-blindness and grayscale.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-03,
.ctc-03 *,
.ctc-03 *::before,
.ctc-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-03 {
  --bg: oklch(0.2 0.02 275);
  --panel: oklch(0.25 0.022 275);
  --ink: oklch(0.95 0.008 275);
  --mut: oklch(0.66 0.02 275);
  --line: oklch(0.33 0.025 275);
  --on: oklch(0.75 0.19 148);
  --away: oklch(0.8 0.15 80);
  --busy: oklch(0.62 0.21 22);
  --off: oklch(0.55 0.015 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-03__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 85% -10%,oklch(0.3 0.06 148/.45),transparent 62%),var(--bg);
  container: ctc03/inline-size;
}

.ctc-03__wrap {
  width: min(760px,100%);
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.ctc-03__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--on);
}

.ctc-03__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin-top: 8px;
}

.ctc-03__hero {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: clamp(14px,3cqi,30px);
  justify-content: space-between;
}

.ctc-03__hero li {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  text-align: center;
}

.ctc-03__hero b {
  font-size: 13px;
  font-weight: 750;
  margin-top: 8px;
}

.ctc-03__hero small {
  font-size: 11px;
  color: var(--mut);
}

.ctc-03__hero code,
.ctc-03__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(1 0 0/.09);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

.ctc-03__avatar {
  position: relative;
  flex: none;
  width: 40px;
  height: 40px;
  border-radius: 13px;
  background-image: var(--img,none),linear-gradient(140deg,oklch(0.65 0.13 var(--h,275)),oklch(0.45 0.12 calc(var(--h,275) + 50)));
  background-size: cover;
  background-position: center;
}

.ctc-03__avatar--xl {
  width: clamp(56px,7cqi,72px);
  height: clamp(56px,7cqi,72px);
  border-radius: 22px;
}

.ctc-03__avatar[data-fallback]::before {
  content: attr(data-fallback);
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font-size: .42em;
  font-weight: 800;
  color: oklch(0.98 0 0/.92);
  font-size: 14px;
}

.ctc-03 [data-dot] {
  position: absolute;
  right: -3px;
  bottom: -3px;
  width: 15px;
  height: 15px;
  border-radius: 50%;
  border: 3px solid var(--bg);
  background: var(--off);
  z-index: 1;
}

.ctc-03__avatar--xl [data-dot] {
  width: 24%;
  aspect-ratio: 1;
  height: auto;
  right: -2px;
  bottom: -2px;
  border-width: 4px;
}

.ctc-03__list [data-dot] {
  border-color: var(--panel);
}

[data-status="online"] [data-dot],
[data-status="typing"] [data-dot] {
  background: var(--on);
}

[data-status="online"] [data-dot]::after {
  content: "";
  position: absolute;
  inset: -3px;
  border-radius: 50%;
  border: 2px solid var(--on);
  animation: ctc03-ping 2.2s ease-out infinite;
}

@keyframes ctc03-ping {
  0% {
    scale: .6;
    opacity: .9;
  }

  70%,
    100% {
    scale: 1.9;
    opacity: 0;
  }
}

[data-status="away"] [data-dot] {
  background: var(--away);
  -webkit-mask: radial-gradient(circle at 30% 28%,transparent 45%,#000 47%);
  mask: radial-gradient(circle at 30% 28%,transparent 45%,#000 47%);
}

[data-status="busy"] [data-dot] {
  background: linear-gradient(0deg,var(--busy) 32%,oklch(0.99 0 0) 33% 67%,var(--busy) 68%) no-repeat center/64% 100%,var(--busy);
}

[data-status="offline"] [data-dot] {
  background: transparent;
  box-shadow: inset 0 0 0 2.5px var(--off);
}

.ctc-03__roster {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 14px;
}

.ctc-03__label {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
  padding: 4px 10px 10px;
}

.ctc-03__list {
  list-style: none;
  display: flex;
  flex-direction: column;
}

.ctc-03__list li {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 9px 10px;
  border-radius: 12px;
  transition: background .18s;
}

.ctc-03__list li:hover {
  background: oklch(1 0 0/.06);
}

.ctc-03__list b {
  font-size: 14px;
  font-weight: 700;
  flex: 1;
}

.ctc-03__list li[data-status="offline"] {
  opacity: .6;
}

.ctc-03__state {
  font-size: 11.5px;
  font-weight: 700;
  color: var(--mut);
  background: oklch(1 0 0/.07);
  border: 1px solid var(--line);
  padding: 5px 11px;
  border-radius: 99px;
}

[data-status="online"] .ctc-03__state {
  color: var(--on);
  border-color: color-mix(in oklch,var(--on) 35%,transparent);
  background: color-mix(in oklch,var(--on) 12%,transparent);
}

[data-status="away"] .ctc-03__state {
  color: var(--away);
  border-color: color-mix(in oklch,var(--away) 35%,transparent);
  background: color-mix(in oklch,var(--away) 12%,transparent);
}

[data-status="busy"] .ctc-03__state {
  color: oklch(0.78 0.14 22);
  border-color: color-mix(in oklch,var(--busy) 45%,transparent);
  background: color-mix(in oklch,var(--busy) 15%,transparent);
}

.ctc-03__typing {
  display: inline-flex;
  gap: 3px;
  align-items: center;
  min-height: 26px;
  padding: 0 12px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--on) 12%,transparent);
  border: 1px solid color-mix(in oklch,var(--on) 35%,transparent);
}

.ctc-03__typing i {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--on);
  animation: ctc03-bounce 1.1s ease-in-out infinite;
}

.ctc-03__typing i:nth-child(2) {
  animation-delay: .15s;
}

.ctc-03__typing i:nth-child(3) {
  animation-delay: .3s;
}

@keyframes ctc03-bounce {
  30% {
    translate: 0 -4px;
  }

  60% {
    translate: 0 0;
  }
}

.ctc-03__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid var(--on);
  padding-left: 12px;
  max-width: 60ch;
}

@container ctc03 (width < 560px) {
  .ctc-03__hero {
    justify-content: flex-start;
    gap: 18px;
  }

  .ctc-03__state {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ctc-03 [data-dot]::after {
    animation: none;
    opacity: 0;
  }

  .ctc-03__typing i {
    animation: none;
  }
}
```
