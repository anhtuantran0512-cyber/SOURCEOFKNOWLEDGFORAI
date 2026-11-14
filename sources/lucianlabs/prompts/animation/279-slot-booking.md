---
source: "lucianlabs"
id: "279"
title: "Booking slot that splits to confirm"
category: "Forms & Input"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#279"
tags: ["booking", "calendar", "time-slot", "scheduling", "form"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Booking slot that splits to confirm (279, Forms & Input)
[What it does] In a call booking widget, pick a day from the date strip and that day's open times rise from below one after another. Press a time and its button shrinks to half as a Confirm button slides out beside it; press Confirm to move to a booked screen summarizing the date and time. Fully booked days are dimmed and blocked.
[How to use it] Pick a date, press a time, then press Confirm

Please add the UI element below to my project.

[Check first]
1. Find out the project’s framework (React, Next, Vue, Svelte, plain HTML, etc.), styling approach (CSS modules, Tailwind, global CSS) and existing theming approach (data-theme, a dark class, CSS variables).
2. Locate the file and any existing element at the insertion point first, and report where that element is used.

[How to apply]
3. Add it as a new component at the insertion point. If there is a replacement target, replace that element with the one below.
4. Keep existing data, props, event handlers, form values and accessibility attributes (labels, aria, keyboard support) as they are.
5. Port the structure, shapes and motion values (durations, curves, delays) of the code below as they are. Convert it into components and state for the framework, but do not guess a new design.
6. Map the --ux-* color tokens below to the project’s existing theme variables. Keep both the light and dark values and check both themes.
7. Keep styles inside this element’s class (.uNNN) and do not change global CSS or global scripts. Make sure the class names do not clash with existing ones.
8. Replace the sample copy and sample data with the project’s real data. Do not bring over gallery-only screens or demo code. Keep the one-line license comment at the top of the new component file.
9. Check that the feature and its final states still work with prefers-reduced-motion turned on.

[Report when done]
10. List the files you changed, behavior that differs from the old element, what you checked (both themes, mobile width, keyboard) and anything you could not check.

[Insertion point] Write the page or component name here
[Replacement target] Write the file path or component name of the existing element, or "none"

--- Code start (this whole code is the working original) ---
<!-- Lucian UX/UI Prompt #279 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#279 -->
<style>
/* lucianLabs UI 요소 — 공통 테마 토큰 (라이트 / 다크)
   라이트 기본값 → 시스템이 다크면 다크 → data-theme으로 명시하면 그 값을 우선합니다.
   요소 CSS는 --ux-* 토큰만 참조하므로, 프로젝트 테마 변수에 이 값을 매핑하면 됩니다. */
:root{
  color-scheme:light;
  --ux-page:#F4F2EE;
  --ux-surface:#FFFFFF;
  --ux-surface-2:#F5F3EF;
  --ux-surface-3:#EAE7E1;
  --ux-ink:#16151B;
  --ux-ink-2:#57535F;
  --ux-ink-3:#8E8A97;
  --ux-line:rgba(22,21,27,.09);
  --ux-line-2:rgba(22,21,27,.17);
  --ux-accent:#6A57F2;
  --ux-accent-2:#2F8FE0;
  --ux-accent-soft:rgba(106,87,242,.12);
  --ux-accent-ink:#FFFFFF;
  --ux-mint:#119C72;
  --ux-warn:#D6731E;
  --ux-danger:#D93A55;
  --ux-glass:rgba(255,255,255,.58);
  --ux-glass-line:rgba(255,255,255,.85);
  --ux-shadow:rgba(40,30,80,.14);
  --ux-shadow-strong:rgba(40,30,80,.3);
  --ux-grad:linear-gradient(120deg,#7B61FF,#3D8BFF 55%,#1FB89A);
  --ux-ease:cubic-bezier(.2,.8,.2,1);
  --ux-spring:cubic-bezier(.34,1.45,.64,1);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    color-scheme:dark;
    --ux-page:#07080D;
    --ux-surface:#13141C;
    --ux-surface-2:#1A1B25;
    --ux-surface-3:#252632;
    --ux-ink:#F4F0E8;
    --ux-ink-2:rgba(244,240,232,.68);
    --ux-ink-3:rgba(244,240,232,.42);
    --ux-line:rgba(255,255,255,.08);
    --ux-line-2:rgba(255,255,255,.16);
    --ux-accent:#B7A4FF;
    --ux-accent-2:#7DB4FF;
    --ux-accent-soft:rgba(183,164,255,.15);
    --ux-accent-ink:#0B0C12;
    --ux-mint:#7EE8C0;
    --ux-warn:#FFB26B;
    --ux-danger:#FF7D8C;
    --ux-glass:rgba(255,255,255,.07);
    --ux-glass-line:rgba(255,255,255,.18);
    --ux-shadow:rgba(0,0,0,.45);
    --ux-shadow-strong:rgba(0,0,0,.72);
    --ux-grad:linear-gradient(120deg,#B7A4FF,#7DB4FF 55%,#A5F2D3);
  }
}
:root[data-theme="dark"]{
  color-scheme:dark;
  --ux-page:#07080D;
  --ux-surface:#13141C;
  --ux-surface-2:#1A1B25;
  --ux-surface-3:#252632;
  --ux-ink:#F4F0E8;
  --ux-ink-2:rgba(244,240,232,.68);
  --ux-ink-3:rgba(244,240,232,.42);
  --ux-line:rgba(255,255,255,.08);
  --ux-line-2:rgba(255,255,255,.16);
  --ux-accent:#B7A4FF;
  --ux-accent-2:#7DB4FF;
  --ux-accent-soft:rgba(183,164,255,.15);
  --ux-accent-ink:#0B0C12;
  --ux-mint:#7EE8C0;
  --ux-warn:#FFB26B;
  --ux-danger:#FF7D8C;
  --ux-glass:rgba(255,255,255,.07);
  --ux-glass-line:rgba(255,255,255,.18);
  --ux-shadow:rgba(0,0,0,.45);
  --ux-shadow-strong:rgba(0,0,0,.72);
  --ux-grad:linear-gradient(120deg,#B7A4FF,#7DB4FF 55%,#A5F2D3);
}
/* 요소 공통 베이스 — 루트에 .ux 클래스를 붙입니다 */
.ux,.ux *,.ux *::before,.ux *::after{box-sizing:border-box}
.ux{
  font-family:"Pretendard Variable",Pretendard,-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Segoe UI",Roboto,"Noto Sans KR",sans-serif;
  color:var(--ux-ink);-webkit-font-smoothing:antialiased;letter-spacing:-.01em;
  -webkit-tap-highlight-color:transparent;
  word-break:keep-all;overflow-wrap:break-word;
}
/* :where()로 명시도를 0으로 둬서, 요소 클래스가 버튼·입력의 색과 글꼴을 덮어쓸 수 있게 합니다 */
:where(.ux) :is(button,input,textarea,select){font:inherit;color:inherit}
:where(.ux) button{cursor:pointer}
.ux :focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
.ux [hidden]{display:none!important}
/* 모션 줄이기: 전환은 즉시 끝나고, 무한 반복은 한 번으로 줄여 최종 상태가 보이게 합니다 */
@media (prefers-reduced-motion:reduce){
  .ux,.ux *,.ux *::before,.ux *::after{
    animation-duration:.001ms!important;animation-iteration-count:1!important;
    transition-duration:.001ms!important;scroll-behavior:auto!important;
  }
}
</style>

<style>
.u279{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u279-hd{position:absolute;left:20px;right:20px;top:18px;display:flex;align-items:center;gap:10px}
.u279-hd i{flex:none;width:34px;height:34px;border-radius:11px;background:var(--ux-grad)}
.u279-hd b{display:block;font-size:14px;font-weight:900}
.u279-hd small{display:block;margin-top:1px;font-size:10px;font-weight:700;color:var(--ux-ink-3)}
.u279-ds{position:absolute;left:14px;right:14px;top:66px;display:grid;grid-template-columns:repeat(5,1fr);gap:6px}
.u279-dy{display:flex;flex-direction:column;align-items:center;gap:2px;height:54px;padding-top:7px;border:0;border-radius:13px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line);color:var(--ux-ink);font:inherit;cursor:pointer;transition:background .2s,color .2s,box-shadow .2s,transform .15s}
.u279-dy small{font-size:9.5px;font-weight:800;color:var(--ux-ink-3)}
.u279-dy b{font-size:16px;font-weight:900;font-variant-numeric:tabular-nums}
.u279-dy i{width:4px;height:4px;border-radius:50%;background:#10B981}
.u279-dy[aria-pressed="true"]{background:var(--ux-ink);color:var(--ux-surface);box-shadow:none}
.u279-dy[aria-pressed="true"] small{color:inherit;opacity:.7}
.u279-dy:disabled{opacity:.38;cursor:not-allowed;background:repeating-linear-gradient(135deg,transparent 0 5px,color-mix(in srgb,var(--ux-ink) 6%,transparent) 5px 6px),var(--ux-surface-2)}
.u279-dy:disabled i{background:var(--ux-ink-3)}
.u279-ls{position:absolute;left:14px;right:14px;top:132px;bottom:12px;overflow-y:auto;scrollbar-width:none;padding:2px}
.u279-ls::-webkit-scrollbar{display:none}
.u279-rw{display:flex;gap:6px;height:40px;margin-bottom:6px;animation:u279-in .4s cubic-bezier(.3,1.3,.5,1) backwards}
@keyframes u279-in{from{opacity:0;transform:translateY(12px)}}
.u279-tm{flex:1 1 100%;min-width:0;border:0;border-radius:11px;background:var(--ux-surface);box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--ux-accent) 45%,transparent);color:var(--ux-accent);font:inherit;font-size:12.5px;font-weight:850;cursor:pointer;transition:flex-basis .4s cubic-bezier(.3,1.2,.5,1),background .25s,color .25s;font-variant-numeric:tabular-nums}
.u279-tm:hover,.u279-tm.g-hov{box-shadow:inset 0 0 0 2px var(--ux-accent)}
.u279-rw.is-on .u279-tm{flex-basis:48%;background:var(--ux-ink-2);color:var(--ux-surface);box-shadow:none}
.u279-ok{flex:0 0 0;min-width:0;padding:0;border:0;border-radius:11px;background:var(--ux-accent);color:#fff;font:inherit;font-size:12.5px;font-weight:850;cursor:pointer;overflow:hidden;opacity:0;white-space:nowrap;transition:flex-basis .4s cubic-bezier(.3,1.2,.5,1),opacity .25s}
.u279-rw.is-on .u279-ok{flex-basis:48%;opacity:1}
.u279-dn{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 24px;background:var(--ux-surface);text-align:center;opacity:0;pointer-events:none;transition:opacity .35s}
.u279.is-done .u279-dn{opacity:1;pointer-events:auto}
.u279-dn svg{width:62px;height:62px}
.u279-dn circle{fill:color-mix(in srgb,#10B981 14%,transparent);transform:scale(.4);transform-origin:center;transform-box:fill-box;transition:transform .5s cubic-bezier(.3,1.6,.5,1) .1s}
.u279-dn path{fill:none;stroke:#10B981;stroke-width:3.5;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:30;stroke-dashoffset:30;transition:stroke-dashoffset .4s ease .4s}
.u279.is-done .u279-dn circle{transform:none}
.u279.is-done .u279-dn path{stroke-dashoffset:0}
.u279-dn b{margin-top:12px;font-size:17px;font-weight:900}
.u279-dn p{margin:6px 0 0;padding:8px 14px;border-radius:11px;background:var(--ux-surface-2);font-size:12px;font-weight:850}
.u279-dn small{margin-top:10px;font-size:10.5px;font-weight:650;color:var(--ux-ink-3)}
.u279 button:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
@media (prefers-reduced-motion: reduce){.u279-rw{animation:none}.u279-tm,.u279-ok,.u279-dn,.u279-dn circle,.u279-dn path{transition:none}}
</style>
<div class="ux u279">
  <div class="u279-hd"><i aria-hidden="true"></i><div><b>30-min product demo</b><small>Video call · dedicated manager</small></div></div>
  <div class="u279-ds" role="group" aria-label="Date"></div>
  <div class="u279-ls" role="group" aria-label="Time"></div>
  <div class="u279-dn" aria-live="polite"><svg viewBox="0 0 62 62" aria-hidden="true"><circle cx="31" cy="31" r="29"/><path d="M20 32l7.5 7.5L43 24"/></svg><b>You’re booked</b><p class="u279-sm"></p><small>We sent an invite and a calendar event</small></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var ds = root.querySelector('.u279-ds'), ls = root.querySelector('.u279-ls'), sm = root.querySelector('.u279-sm');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var WD = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], AMPM = [' AM', ' PM'];
  var DAYS = [[14, [600, 690, 900]], [15, []], [16, [570, 630, 720, 840, 900, 960, 1020]], [17, [660, 780]], [18, [540, 600, 840, 930]]];
  function hm(m) { var h = Math.floor(m / 60), mm = m % 60, pm = h >= 12, hh = h % 12 || 12; return (pm ? '' : '') + hh + ':' + (mm < 10 ? '0' : '') + mm + AMPM[pm ? 1 : 0]; }
  var D = DAYS.map(function (d, i) {
    var b = document.createElement('button'); b.type = 'button'; b.className = 'u279-dy'; b.setAttribute('aria-pressed', 'false');
    b.innerHTML = '<small></small><b>' + d[0] + '</b><i aria-hidden="true"></i>'; b.firstChild.textContent = WD[i];
    if (!d[1].length) { b.disabled = true; b.setAttribute('aria-label', WD[i] + ' ' + d[0] + ' ' + 'Fully booked'); }
    b.addEventListener('click', function () { day(i); });
    ds.appendChild(b); return b;
  });
  var cd = -1;
  function day(i) {
    if (i === cd) return;
    cd = i; D.forEach(function (b, k) { b.setAttribute('aria-pressed', k === i); });
    ls.innerHTML = '';
    DAYS[i][1].forEach(function (m, k) {
      var r = document.createElement('div'); r.className = 'u279-rw'; r.style.animationDelay = k * 0.05 + 's';
      r.innerHTML = '<button type="button" class="u279-tm"></button><button type="button" class="u279-ok" tabindex="-1">Confirm</button>';
      var tm = r.firstChild, ok = r.lastChild; tm.textContent = hm(m);
      tm.addEventListener('click', function () { Array.prototype.forEach.call(ls.children, function (o) { o.classList.toggle('is-on', o === r); o.lastChild.tabIndex = o === r ? 0 : -1; }); setTimeout(function () { ok.focus({ preventScroll: true }); }, rm ? 0 : 300); });
      ok.addEventListener('click', function () { sm.textContent = 'Oct ' + DAYS[i][0] + ' (' + WD[i] + ') · ' + hm(m); root.classList.add('is-done'); });
      ls.appendChild(r);
    });
  }
  day(0);
})();
</script>
--- Code end ---
