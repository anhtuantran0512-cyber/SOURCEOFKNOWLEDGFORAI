---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/floating-chat-widget/"
title: "Floating Chat Widget FAB with Notification Panel"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "A launcher that opens a real inbox, not a placeholder: unread conversations with avatars, presence dots, relative timestamps, a typing indicator, and a…"
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Chat Widget FAB with Notification Panel
Source: https://codefronts.com/components/css-floating-buttons/floating-chat-widget/

A launcher that opens a real inbox, not a placeholder: unread conversations with avatars, presence dots, relative timestamps, a typing indicator, and a compose row. This is the version you build when the widget is the product — every row is a button, the unread count is a live region, and marking all read animates the badge away instead of snapping it.
## HTML
```html
<section class="fb-13" aria-label="Floating chat widget with notification panel demo">
  <div class="fb-13__page">
    <p class="fb-13__eyebrow">disclosure · live region · origin-anchored panel</p>
    <h2 class="fb-13__title">The launcher opens an actual inbox</h2>
    <p class="fb-13__sub">Rows are buttons, avatars are decorative, the count lives in one place and animates out when you clear it.</p>
    <p class="fb-13__chip">transform-origin: 100% 100% · role="status"</p>
  </div>
  <div class="fb-13__dock">
    <div class="fb-13__panel" id="fb-13-panel" role="dialog" aria-labelledby="fb-13-ptitle" hidden>
      <header class="fb-13__head">
        <div class="fb-13__headTxt">
          <h3 class="fb-13__ptitle" id="fb-13-ptitle">Messages</h3>
          <p class="fb-13__count" id="fb-13-count" role="status">3 unread conversations</p>
        </div>
        <button class="fb-13__clear" id="fb-13-clear" type="button">Mark all read</button>
      </header>
      <ul class="fb-13__list" id="fb-13-list">
        <li><button class="fb-13__row is-unread" type="button">
          <span class="fb-13__av"><img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=120&auto=format&fit=crop" alt="" loading="lazy"><i class="fb-13__on"></i></span>
          <span class="fb-13__rTxt"><b>Priya Raman</b><i>Sent the FAB spacing sheet — take a look when you can.</i></span>
          <span class="fb-13__rMeta"><time datetime="2026-08-06T14:12">4m</time><em>2</em></span>
        </button></li>
        <li><button class="fb-13__row is-unread" type="button">
          <span class="fb-13__av"><img src="https://images.unsplash.com/photo-1633332755192-727a05c4013d?q=80&w=120&auto=format&fit=crop" alt="" loading="lazy"></span>
          <span class="fb-13__rTxt"><b>Daniel Okafor</b><i><span class="fb-13__typing" aria-hidden="true"><i></i><i></i><i></i></span>typing…</i></span>
          <span class="fb-13__rMeta"><time datetime="2026-08-06T13:40">36m</time><em>1</em></span>
        </button></li>
        <li><button class="fb-13__row" type="button">
          <span class="fb-13__av"><img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=120&auto=format&fit=crop" alt="" loading="lazy"><i class="fb-13__on"></i></span>
          <span class="fb-13__rTxt"><b>Lena Fischer</b><i>Perfect, shipping the tonal palette tonight.</i></span>
          <span class="fb-13__rMeta"><time datetime="2026-08-05T18:02">Yesterday</time></span>
        </button></li>
        <li><button class="fb-13__row" type="button">
          <span class="fb-13__av fb-13__av--txt">SC</span>
          <span class="fb-13__rTxt"><b>Support channel</b><i>Weekly digest: 14 resolved, 2 open.</i></span>
          <span class="fb-13__rMeta"><time datetime="2026-08-04T09:15">Tue</time></span>
        </button></li>
      </ul>
      <div class="fb-13__compose">
        <input class="fb-13__field" id="fb-13-field" type="text" placeholder="Write a message…" aria-label="Write a message" autocomplete="off">
        <button class="fb-13__send" id="fb-13-send" type="button" aria-label="Send message"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12l16-7-6 7 6 7z" fill="currentColor"/></svg></button>
      </div>
    </div>
    <button class="fb-13__launch" id="fb-13-launch" type="button" aria-expanded="false" aria-controls="fb-13-panel" aria-label="Open messages, 3 unread">
      <span class="fb-13__lIco fb-13__lIco--chat" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M4 5h16v11H8l-4 4z" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round"/><path d="M8 9.5h8M8 12.5h5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg></span>
      <span class="fb-13__lIco fb-13__lIco--x" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></span>
      <span class="fb-13__badge" id="fb-13-badge">3</span>
    </button>
  </div>
</section>
```
## CSS
```css
.fb-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-13-bg);
  --fb-13-bg: linear-gradient(170deg,oklch(0.97 0.012 250),oklch(0.92 0.022 265));
  --fb-13-brand: oklch(0.52 0.18 275);
  --fb-13-brandDeep: oklch(0.4 0.16 275);
  --fb-13-ink: oklch(0.22 0.025 270);
  --fb-13-mut: oklch(0.54 0.02 270);
  --fb-13-card: oklch(1 0 0);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-13-ink);
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
  overflow: hidden;
}

.fb-13 *,
.fb-13 *::before,
.fb-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-13__page {
  width: min(100%,54ch);
  display: grid;
  gap: 12px;
  justify-items: center;
  text-align: center;
}

.fb-13__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--fb-13-brand);
}

.fb-13__title {
  font-size: clamp(26px,4.6vw,44px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-13__sub {
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-13-mut);
  text-wrap: pretty;
}

.fb-13__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-13-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.22 0.025 270/.14);
  border-radius: 99px;
}

.fb-13__dock {
  position: absolute;
  right: clamp(14px,3vw,32px);
  bottom: calc(clamp(14px,3vw,32px) + env(safe-area-inset-bottom));
  z-index: 6;
  display: grid;
  justify-items: end;
  gap: 14px;
}

.fb-13__panel {
  width: min(92vw,368px);
  max-block-size: min(72svh,540px);
  display: flex;
  flex-direction: column;
  border-radius: 22px;
  overflow: hidden;
  background: var(--fb-13-card);
  border: 1px solid oklch(0.22 0.025 270/.08);
  box-shadow: 0 34px 80px -30px oklch(0.22 0.025 270/.6),0 2px 8px oklch(0.22 0.025 270/.1);
  transform-origin: 100% 100%;
  opacity: 1;
  scale: 1;
  translate: 0 0;
  transition: opacity .26s ease,scale .32s cubic-bezier(.2,1.1,.3,1),translate .32s cubic-bezier(.2,1.1,.3,1),display .32s allow-discrete,overlay .32s allow-discrete;
}

.fb-13__panel[hidden] {
  display: none;
}

@starting-style {
  .fb-13__panel:not([hidden]) {
    opacity: 0;
    scale: .92;
    translate: 0 14px;
  }
}

.fb-13__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 16px 16px 14px;
  background: linear-gradient(130deg,var(--fb-13-brandDeep),oklch(0.46 0.2 300));
  color: oklch(0.99 0.01 275);
}

.fb-13__ptitle {
  font-size: 16.5px;
  font-weight: 680;
  letter-spacing: -.01em;
}

.fb-13__count {
  font-size: 11.5px;
  opacity: .84;
  margin-top: 1px;
}

.fb-13__clear {
  min-height: 34px;
  padding: 0 12px;
  border: 1px solid oklch(1 0 0/.28);
  border-radius: 99px;
  background: oklch(1 0 0/.1);
  color: inherit;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease;
}

.fb-13__clear:hover {
  background: oklch(1 0 0/.2);
}

.fb-13__clear:focus-visible {
  outline: 2.5px solid oklch(0.99 0.01 275);
  outline-offset: 2px;
}

.fb-13__list {
  list-style: none;
  flex: 1;
  overflow: auto;
  display: grid;
  align-content: start;
  scrollbar-width: thin;
}

.fb-13__row {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 11px;
  width: 100%;
  padding: 12px 15px;
  border: 0;
  border-bottom: 1px solid oklch(0.22 0.025 270/.07);
  background: transparent;
  text-align: left;
  cursor: pointer;
  transition: background .16s ease;
}

.fb-13__row:hover {
  background: oklch(0.52 0.18 275/.06);
}

.fb-13__row:focus-visible {
  outline: 2.5px solid var(--fb-13-brand);
  outline-offset: -3px;
}

.fb-13__row.is-unread {
  background: oklch(0.52 0.18 275/.045);
}

.fb-13__row.is-unread b::before {
  content: "";
  display: inline-block;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--fb-13-brand);
  margin-right: 7px;
  vertical-align: 1px;
}

.fb-13__av {
  position: relative;
  flex: none;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  overflow: visible;
  background: linear-gradient(140deg,oklch(0.8 0.09 275),oklch(0.62 0.12 320));
}

.fb-13__av img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  display: block;
}

.fb-13__av--txt {
  display: grid;
  place-items: center;
  font-size: 13px;
  font-weight: 700;
  color: oklch(0.24 0.06 275);
}

.fb-13__on {
  position: absolute;
  right: 0;
  bottom: 0;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: oklch(0.78 0.19 145);
  box-shadow: 0 0 0 2.5px var(--fb-13-card);
}

.fb-13__rTxt {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.fb-13__rTxt b {
  font-size: 13.8px;
  font-weight: 640;
  color: var(--fb-13-ink);
}

.fb-13__rTxt i {
  font-style: normal;
  font-size: 12.2px;
  color: var(--fb-13-mut);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.fb-13__rMeta {
  display: grid;
  justify-items: end;
  gap: 5px;
}

.fb-13__rMeta time {
  font-size: 10.8px;
  color: var(--fb-13-mut);
  font-variant-numeric: tabular-nums;
}

.fb-13__rMeta em {
  font-style: normal;
  min-width: 19px;
  height: 19px;
  padding: 0 5px;
  border-radius: 99px;
  background: var(--fb-13-brand);
  color: oklch(0.99 0.01 275);
  font-size: 11px;
  font-weight: 700;
  line-height: 19px;
  text-align: center;
}

.fb-13__typing {
  display: inline-flex;
  gap: 3px;
  margin-right: 5px;
  vertical-align: middle;
}

.fb-13__typing i {
  width: 4.5px;
  height: 4.5px;
  border-radius: 50%;
  background: var(--fb-13-brand);
  animation: fb-13-bounce 1.1s ease-in-out infinite;
}

.fb-13__typing i:nth-child(2) {
  animation-delay: .14s;
}

.fb-13__typing i:nth-child(3) {
  animation-delay: .28s;
}

@keyframes fb-13-bounce {
  0%,
    100% {
    transform: translateY(0);
    opacity: .4;
  }

  50% {
    transform: translateY(-3.5px);
    opacity: 1;
  }
}

.fb-13__compose {
  display: flex;
  gap: 8px;
  padding: 11px 12px;
  border-top: 1px solid oklch(0.22 0.025 270/.08);
  background: oklch(0.985 0.005 270);
}

.fb-13__field {
  flex: 1;
  min-height: 42px;
  padding: 0 14px;
  border: 1px solid oklch(0.22 0.025 270/.12);
  border-radius: 99px;
  background: var(--fb-13-card);
  font-size: 13.5px;
  font-family: inherit;
  color: var(--fb-13-ink);
}

.fb-13__field:focus-visible {
  outline: 2.5px solid var(--fb-13-brand);
  outline-offset: 1px;
}

.fb-13__send {
  flex: none;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border: 0;
  border-radius: 50%;
  background: var(--fb-13-brand);
  color: oklch(0.99 0.01 275);
  cursor: pointer;
  transition: transform .2s cubic-bezier(.2,1.3,.4,1),background .18s ease;
}

.fb-13__send svg {
  width: 20px;
  height: 20px;
}

.fb-13__send:hover {
  background: var(--fb-13-brandDeep);
}

.fb-13__send:active {
  transform: scale(.9);
}

.fb-13__send:focus-visible {
  outline: 3px solid var(--fb-13-brandDeep);
  outline-offset: 2px;
}

.fb-13__launch {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 62px;
  block-size: 62px;
  border: 0;
  border-radius: 22px;
  cursor: pointer;
  color: oklch(0.99 0.01 275);
  background: linear-gradient(145deg,oklch(0.6 0.19 285),var(--fb-13-brandDeep));
  box-shadow: 0 14px 34px -12px oklch(0.4 0.16 275/.85),0 2px 6px oklch(0.3 0.1 275/.3);
  transition: transform .28s cubic-bezier(.2,1.3,.4,1),border-radius .28s ease;
}

.fb-13__launch:hover {
  transform: translateY(-2px);
}

.fb-13__launch:active {
  transform: scale(.94);
}

.fb-13__launch:focus-visible {
  outline: 3px solid var(--fb-13-brandDeep);
  outline-offset: 4px;
}

.fb-13__launch[aria-expanded="true"] {
  border-radius: 50%;
}

.fb-13__lIco {
  grid-area: 1/1;
  display: grid;
  place-items: center;
  transition: opacity .22s ease,rotate .32s cubic-bezier(.3,1.4,.4,1),scale .3s ease;
}

.fb-13__lIco svg {
  width: 27px;
  height: 27px;
}

.fb-13__lIco--x {
  opacity: 0;
  rotate: -90deg;
  scale: .7;
}

.fb-13__launch[aria-expanded="true"] .fb-13__lIco--chat {
  opacity: 0;
  rotate: 90deg;
  scale: .7;
}

.fb-13__launch[aria-expanded="true"] .fb-13__lIco--x {
  opacity: 1;
  rotate: 0deg;
  scale: 1;
}

.fb-13__badge {
  position: absolute;
  top: -4px;
  right: -4px;
  min-width: 23px;
  height: 23px;
  padding: 0 6px;
  border-radius: 99px;
  background: oklch(0.62 0.22 22);
  color: oklch(0.99 0.01 22);
  font-size: 12px;
  font-weight: 700;
  line-height: 23px;
  box-shadow: 0 0 0 3px oklch(0.95 0.015 258);
  font-variant-numeric: tabular-nums;
  transition: scale .24s cubic-bezier(.2,1.5,.4,1),opacity .2s ease;
}

.fb-13__badge[data-zero="true"] {
  scale: 0;
  opacity: 0;
}

@media (max-width: 430px) {
  .fb-13__panel {
    width: calc(100vw - 28px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fb-13 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const launch = document.getElementById('fb-13-launch');
  const panel = document.getElementById('fb-13-panel');
  const badge = document.getElementById('fb-13-badge');
  const count = document.getElementById('fb-13-count');
  const clear = document.getElementById('fb-13-clear');
  if (!launch || !panel || launch.dataset.fbWired) return;
  launch.dataset.fbWired = '1';
  let unread = 3;
  const render = () => {
    badge.textContent = String(unread);
    badge.dataset.zero = String(unread === 0);
    count.textContent = unread === 0 ? 'All caught up' : unread + ' unread conversations';
    launch.setAttribute('aria-label', (panel.hidden ? 'Open' : 'Close') + ' messages, ' + unread + ' unread');
  };
  const setOpen = (open) => {
    panel.hidden = !open;
    launch.setAttribute('aria-expanded', String(open));
    render();
  };
  launch.addEventListener('click', () => setOpen(panel.hidden));
  clear.addEventListener('click', () => {
    unread = 0;
    panel.querySelectorAll('.fb-13__row').forEach((r) => r.classList.remove('is-unread'));
    panel.querySelectorAll('.fb-13__rMeta em').forEach((e) => e.remove());
    render();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !panel.hidden) { setOpen(false); launch.focus(); }
  });
  render();
})();
```
