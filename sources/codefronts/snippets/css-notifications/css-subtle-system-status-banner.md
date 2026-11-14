---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-subtle-system-status-banner/"
title: "CSS Subtle System Status Banner"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Two volumes of quiet: a maintenance ticker that scrolls its message on a seamless CSS marquee (duplicated track, masked edge fades, pauses on hover — the…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Subtle System Status Banner
Source: https://codefronts.com/snippets/css-notifications/css-subtle-system-status-banner/

Two volumes of quiet: a maintenance ticker that scrolls its message on a seamless CSS marquee (duplicated track, masked edge fades, pauses on hover — the accessible rebuild of the <marquee> tag), and a status-page strip that cycles operational → degraded → maintenance with a breathing dot, cross-fading copy and a live 'checked Ns ago' counter.
## HTML
```html
<div class="ntf-19-group">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-19a" aria-label="Scrolling maintenance ticker banner">
  <div class="ntf-19a__stage">
    <div class="ntf-19a__ticker" role="region" aria-label="System maintenance notice">
      <p class="ntf-19a__sr">Scheduled maintenance: API and dashboard read-only on Sunday 02:00–02:20 UTC. Status page: status.codefronts.com.</p>
      <div class="ntf-19a__track" aria-hidden="true">
        <span class="ntf-19a__msg"><b>SCHEDULED MAINTENANCE</b> — API &amp; dashboard read-only · Sun 02:00–02:20 UTC · follow along at status.codefronts.com <i>&#9679;</i></span>
        <span class="ntf-19a__msg"><b>SCHEDULED MAINTENANCE</b> — API &amp; dashboard read-only · Sun 02:00–02:20 UTC · follow along at status.codefronts.com <i>&#9679;</i></span>
      </div>
    </div>
    <p class="ntf-19a__cap">Two copies of the message, translated −50%, masked at the edges. Hover to pause. Screen readers get one static sentence — never the moving one.</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<section class="ntf-19b" aria-label="Status page strip cycling through states">
  <div class="ntf-19b__stage">
    <div class="ntf-19b__strip" id="ntf-19b-strip" data-state="ok">
      <span class="ntf-19b__dot" aria-hidden="true"></span>
      <span class="ntf-19b__labels">
        <b class="ntf-19b__lbl" data-for="ok">All systems operational</b>
        <b class="ntf-19b__lbl" data-for="deg">Elevated API latency — investigating</b>
        <b class="ntf-19b__lbl" data-for="mnt">Planned maintenance in progress</b>
      </span>
      <code class="ntf-19b__ago" id="ntf-19b-ago">checked 0s ago</code>
    </div>
    <div class="ntf-19b__row" role="group" aria-label="Simulate state">
      <button class="ntf-19b__btn" data-ntf-19b="ok" type="button">Operational</button>
      <button class="ntf-19b__btn" data-ntf-19b="deg" type="button">Degraded</button>
      <button class="ntf-19b__btn" data-ntf-19b="mnt" type="button">Maintenance</button>
    </div>
    <p class="ntf-19b__note" id="ntf-19b-note" role="status" aria-live="polite"></p>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-19-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.ntf-19-group > section {
  width: 100%;
}

.ntf-19a,
.ntf-19a *,
.ntf-19a *::before,
.ntf-19a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-19a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#14181f,#0b0d11);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-19a__stage {
  width: min(680px,100%);
  display: grid;
  gap: 20px;
}

.ntf-19a__ticker {
  overflow: hidden;
  border-radius: 12px;
  background: oklch(0.82 0.13 85 / .08);
  border: 1px solid oklch(0.82 0.13 85 / .3);
  padding: 12px 0;
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);
  mask-image: linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);
}

.ntf-19a__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.ntf-19a__track {
  display: flex;
  gap: 56px;
  width: max-content;
  animation: ntf-19a-roll 16s linear infinite;
}

.ntf-19a__ticker:hover .ntf-19a__track,
.ntf-19a__ticker:focus-within .ntf-19a__track {
  animation-play-state: paused;
}

@keyframes ntf-19a-roll {
  to {
    translate: calc(-50% - 28px) 0;
  }
}

.ntf-19a__msg {
  flex: none;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 12.5px;
  letter-spacing: .02em;
  color: oklch(0.88 0.09 85 / .85);
  white-space: nowrap;
}

.ntf-19a__msg b {
  color: oklch(0.88 0.12 85);
  font-weight: 600;
}

.ntf-19a__msg i {
  font-style: normal;
  color: oklch(0.82 0.13 85 / .5);
  margin-inline-start: 40px;
}

.ntf-19a__cap {
  font-size: 12px;
  line-height: 1.65;
  color: rgba(215,222,235,.45);
  text-align: center;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-19a__track {
    animation: none;
    width: auto;
  }

  .ntf-19a__msg:nth-child(2) {
    display: none;
  }

  .ntf-19a__msg {
    white-space: normal;
    padding-inline: 16px;
  }
}

.ntf-19b,
.ntf-19b *,
.ntf-19b *::before,
.ntf-19b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-19b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f5f6f8,#eaecf0);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-19b__stage {
  width: min(560px,100%);
  display: grid;
  gap: 18px;
  justify-items: center;
}

.ntf-19b__strip {
  --acc: oklch(0.62 0.15 155);
  --tempo: 3.2s;
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 13px 18px;
  border-radius: 12px;
  background: #fff;
  border: 1px solid rgba(29,33,43,.1);
  box-shadow: 0 14px 34px -22px rgba(29,33,43,.4);
  transition: border-color .4s;
}

.ntf-19b__strip[data-state=deg] {
  --acc: oklch(0.68 0.15 65);
  --tempo: 1.1s;
}

.ntf-19b__strip[data-state=mnt] {
  --acc: oklch(0.6 0.12 250);
  --tempo: 0s;
}

.ntf-19b__dot {
  flex: none;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: var(--acc);
  transition: background .4s;
  animation: ntf-19b-breathe var(--tempo) ease-in-out infinite;
}

.ntf-19b__strip[data-state=mnt] .ntf-19b__dot {
  animation: none;
}

@keyframes ntf-19b-breathe {
  0%,
    100% {
    scale: 1;
    opacity: 1;
  }

  50% {
    scale: .82;
    opacity: .72;
  }
}

.ntf-19b__labels {
  position: relative;
  display: block;
  min-width: 0;
  flex: 1;
  height: 1.25em;
}

.ntf-19b__lbl {
  position: absolute;
  inset: 0;
  font-size: 14px;
  font-weight: 600;
  color: #1d212b;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  opacity: 0;
  translate: 0 5px;
  transition: opacity .35s,translate .35s;
}

.ntf-19b__strip[data-state=ok] .ntf-19b__lbl[data-for=ok],
.ntf-19b__strip[data-state=deg] .ntf-19b__lbl[data-for=deg],
.ntf-19b__strip[data-state=mnt] .ntf-19b__lbl[data-for=mnt] {
  opacity: 1;
  translate: 0 0;
}

.ntf-19b__ago {
  flex: none;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 10.5px;
  color: rgba(29,33,43,.45);
}

.ntf-19b__row {
  display: flex;
  gap: 8px;
}

.ntf-19b__btn {
  padding: 9px 16px;
  font: inherit;
  font-size: 12.5px;
  font-weight: 600;
  color: #1d212b;
  background: #fff;
  border: 1px solid rgba(29,33,43,.16);
  border-radius: 9px;
  cursor: pointer;
  transition: background .15s,scale .12s;
}

.ntf-19b__btn:hover {
  background: #f2f4f8;
}

.ntf-19b__btn:active {
  scale: .95;
}

.ntf-19b__note {
  font-size: 12px;
  color: rgba(29,33,43,.5);
  min-height: 18px;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-19b__dot {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the -50% translate loop is seamless because the track holds the message twice (the extra -28px is half the 56px gap). Reduced-motion swaps the ticker for a static, wrapped sentence. */

(function(){
  var strip=document.getElementById('ntf-19b-strip'); if(!strip) return;
  var ago=document.getElementById('ntf-19b-ago'),note=document.getElementById('ntf-19b-note'),
      NAMES={ok:'All systems operational',deg:'Elevated API latency',mnt:'Planned maintenance'},t=0;
  setInterval(function(){ t++; ago.textContent='checked '+t+'s ago'; },1000);
  document.querySelectorAll('[data-ntf-19b]').forEach(function(btn){
    btn.addEventListener('click',function(){
      var s=btn.getAttribute('data-ntf-19b');
      if(strip.getAttribute('data-state')===s) return;
      strip.setAttribute('data-state',s); t=0;
      note.textContent='Status changed: '+NAMES[s];   /* announce CHANGES, not every tick */
    });
  });
})();
```
