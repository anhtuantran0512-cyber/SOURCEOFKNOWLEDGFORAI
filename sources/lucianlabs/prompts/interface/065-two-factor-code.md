---
source: "lucianlabs"
id: "065"
title: "Number-match device approval"
category: "Sign-in & Sign-up"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#065"
tags: ["2fa", "number-matching", "approval", "countdown", "security"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Number-match device approval (065, Sign-in & Sign-up)
[What it does] When a sign-in request comes from a new device, the time left shrinks around a ring and the location dot pulses like a heartbeat. Pick the number shown on the other screen to approve with a check; a wrong pick shakes, and denying turns it into a red shield.
[How to use it] The other screen shows 42. Pick 42 to approve, try a different number, or deny with “It’s not me”

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
<!-- Lucian UX/UI Prompt #065 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#065 -->
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
.u065{position:relative;width:340px;height:480px;border-radius:30px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u065-map{position:relative;height:150px;background:linear-gradient(180deg,color-mix(in srgb,var(--ux-accent) 12%,var(--ux-surface-2)),var(--ux-surface-2));overflow:hidden}
.u065-map::before{content:"";position:absolute;inset:-20px;background:repeating-linear-gradient(0deg,transparent 0 27px,var(--ux-line) 27px 28px),repeating-linear-gradient(90deg,transparent 0 27px,var(--ux-line) 27px 28px);transform:perspective(300px) rotateX(35deg) translateY(-20px)}
.u065-road{position:absolute;left:-10%;right:-10%;top:58%;height:14px;background:var(--ux-surface);transform:rotate(-8deg);opacity:.9}
.u065-pin{position:absolute;left:50%;top:52%;width:16px;height:16px;margin:-8px;border-radius:50%;background:var(--ux-accent);box-shadow:0 0 0 4px var(--ux-surface)}
.u065-pin::before,.u065-pin::after{content:"";position:absolute;inset:-4px;border-radius:50%;border:2px solid var(--ux-accent);animation:u065-pulse 2s ease-out infinite}
.u065-pin::after{animation-delay:1s}
@keyframes u065-pulse{from{transform:scale(1);opacity:.7}to{transform:scale(4);opacity:0}}
.u065-time{position:absolute;right:14px;top:14px;width:52px;height:52px;border-radius:50%;background:var(--ux-surface);display:grid;place-items:center;box-shadow:0 6px 14px -8px var(--ux-shadow-strong)}
.u065-time svg{position:absolute;inset:4px;width:44px;height:44px;transform:rotate(-90deg)}
.u065-time circle{fill:none;stroke-width:3.5}
.u065-time .t{stroke:var(--ux-surface-3)}
.u065-time .p{stroke:var(--ux-accent);stroke-linecap:round;stroke-dasharray:100;stroke-dashoffset:calc(100 - var(--p,1) * 100);transition:stroke .3s}
.u065-time.low .p{stroke:var(--ux-danger)}
.u065-time b{font-size:13px;font-weight:850;font-variant-numeric:tabular-nums}
.u065-body{position:absolute;left:0;right:0;top:150px;bottom:0;padding:18px 22px 22px;display:flex;flex-direction:column;transition:opacity .35s,transform .5s var(--ux-ease)}
.u065-dev{display:flex;align-items:center;gap:12px}
.u065-dev i{width:42px;height:42px;flex:none;border-radius:13px;display:grid;place-items:center;background:var(--ux-surface-2);color:var(--ux-ink)}
.u065-dev i svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.u065-dev b{display:block;font-size:16px;font-weight:800;letter-spacing:-.03em}
.u065-dev small{display:block;margin-top:2px;font-size:12.5px;font-weight:600;color:var(--ux-ink-3)}
.u065-ask{margin:18px 0 10px;font-size:14px;font-weight:700;color:var(--ux-ink-2)}
.u065-nums{display:flex;gap:10px}
.u065-n{flex:1;height:72px;border:0;border-radius:18px;background:var(--ux-surface-2);font-size:28px;font-weight:850;letter-spacing:-.03em;color:var(--ux-ink);font-variant-numeric:tabular-nums;transition:transform .3s var(--ux-spring),background-color .3s,box-shadow .3s}
.u065-n:hover{background:var(--ux-surface-3)}
.u065-n:active{transform:scale(.94)}
.u065-n:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u065-n.wrong{box-shadow:inset 0 0 0 2px var(--ux-danger);color:var(--ux-danger);animation:u065-no .4s}
@keyframes u065-no{20%{transform:translateX(-6px)}45%{transform:translateX(5px)}70%{transform:translateX(-2px)}}
.u065-msg{min-height:20px;margin-top:10px;font-size:12.5px;font-weight:650;color:var(--ux-danger)}
.u065-deny{margin-top:auto;height:48px;border:0;border-radius:15px;background:none;box-shadow:inset 0 0 0 1.5px var(--ux-line-2);color:var(--ux-danger);font-size:14.5px;font-weight:750;transition:background-color .3s,transform .3s var(--ux-spring)}
.u065-deny:hover{background:color-mix(in srgb,var(--ux-danger) 8%,transparent)}
.u065-deny:active{transform:scale(.97)}
.u065-deny:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u065-res{position:absolute;left:0;right:0;top:150px;bottom:0;padding:0 26px 24px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;opacity:0;transform:translateY(20px);pointer-events:none;transition:opacity .35s,transform .55s var(--ux-spring)}
.u065-res span{width:76px;height:76px;margin-top:-30px;border-radius:50%;display:grid;place-items:center;background:var(--c);color:var(--ux-accent-ink)}
.u065-res span svg{width:34px;height:34px;fill:none;stroke:currentColor;stroke-width:2.8;stroke-linecap:round;stroke-linejoin:round}
.u065-res b{margin-top:16px;font-size:20px;font-weight:850;letter-spacing:-.04em}
.u065-res p{margin:6px 0 18px;font-size:13.5px;line-height:1.5;color:var(--ux-ink-3)}
.u065-res button{height:44px;padding:0 18px;border:0;border-radius:999px;background:var(--ux-surface-2);color:var(--ux-ink);font-size:13.5px;font-weight:720}
.u065-res button:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u065[data-s] .u065-body{opacity:0;transform:translateY(-16px);pointer-events:none}
.u065[data-s="ok"] .u065-res.ok,.u065[data-s="no"] .u065-res.no,.u065[data-s="late"] .u065-res.late{opacity:1;transform:none;pointer-events:auto}
.u065[data-s="no"] .u065-pin,.u065[data-s="late"] .u065-pin{background:var(--ux-ink-3)}
.u065[data-s] .u065-pin::before,.u065[data-s] .u065-pin::after{animation:none;opacity:0}
.u065[data-s="ok"] .u065-pin{background:var(--ux-mint)}
</style>
<div class="ux u065">
  <div class="u065-map" aria-hidden="true"><span class="u065-road"></span><span class="u065-pin"></span></div>
  <div class="u065-time" role="timer" aria-label="Time left"><svg viewBox="0 0 44 44" aria-hidden="true"><circle class="t" cx="22" cy="22" r="19"/><circle class="p" cx="22" cy="22" r="19" pathLength="100"/></svg><b>60</b></div>
  <div class="u065-body">
    <div class="u065-dev"><i aria-hidden="true"><svg viewBox="0 0 24 24"><rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2.5 19h19"/></svg></i><span><b>Sign-in request from a new device</b><small>MacBook Pro · Seoul · just now</small></span></div>
    <p class="u065-ask" id="u065-ask">Pick the number shown on the sign-in screen</p>
    <div class="u065-nums" role="group" aria-label="Choose a number"><button class="u065-n" type="button">17</button><button class="u065-n" type="button">42</button><button class="u065-n" type="button">86</button></div>
    <p class="u065-msg" role="alert"></p>
    <button class="u065-deny" type="button">It’s not me · Deny</button>
  </div>
  <div class="u065-res ok" aria-hidden="true" style="--c:var(--ux-mint)"><span><svg viewBox="0 0 34 34"><path d="M9 17.5l5.5 5.5L25.5 12"/></svg></span><b>Sign-in approved</b><p>Continue on your MacBook Pro</p><button type="button" tabindex="-1">Start over</button></div>
  <div class="u065-res no" aria-hidden="true" style="--c:var(--ux-danger)"><span><svg viewBox="0 0 34 34"><path d="M17 5l10 4v7c0 6.5-4.4 11-10 13-5.6-2-10-6.5-10-13V9z"/><path d="M13 13l8 8M21 13l-8 8"/></svg></span><b>Request blocked</b><p>We recommend changing your password</p><button type="button" tabindex="-1">Start over</button></div>
  <div class="u065-res late" aria-hidden="true" style="--c:var(--ux-warn)"><span><svg viewBox="0 0 34 34"><circle cx="17" cy="17" r="11"/><path d="M17 11v6l4 3"/></svg></span><b>Request expired</b><p>Request again from the sign-in screen</p><button type="button" tabindex="-1">Request again</button></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var timer = root.querySelector('.u065-time'), sec = timer.querySelector('b'), msg = root.querySelector('.u065-msg');
  var nums = root.querySelectorAll('.u065-n'), res = root.querySelectorAll('.u065-res');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var LIMIT = 60, t0 = 0, raf = 0, tries = 0;
  var uid = 'u065' + Math.random().toString(36).slice(2, 7);
  root.querySelector('.u065-ask').id = uid; root.querySelector('.u065-nums').setAttribute('aria-describedby', uid);
  function finish(s) {
    cancelAnimationFrame(raf);
    root.setAttribute('data-s', s);
    root.querySelector('.u065-body').inert = true;
    res.forEach(function (r) {
      var on = r.classList.contains(s);
      r.setAttribute('aria-hidden', String(!on));
      r.querySelector('button').tabIndex = on ? 0 : -1;
      if (on) r.querySelector('button').focus({ preventScroll: true });
    });
    if (s !== 'ok' && !rm) root.animate([{ transform: 'translateX(-6px)' }, { transform: 'translateX(5px)' }, { transform: 'none' }], { duration: 320 });
  }
  function tick(now) {
    if (!root.isConnected) return;
    var left = Math.max(0, LIMIT - (now - t0) / 1000);
    timer.style.setProperty('--p', (left / LIMIT).toFixed(4));
    sec.textContent = Math.ceil(left);
    timer.classList.toggle('low', left <= 10);
    if (left <= 0) { finish('late'); return; }
    raf = requestAnimationFrame(tick);
  }
  function start() {
    root.removeAttribute('data-s');
    root.querySelector('.u065-body').inert = false;
    res.forEach(function (r) { r.setAttribute('aria-hidden', 'true'); r.querySelector('button').tabIndex = -1; });
    nums.forEach(function (n) { n.classList.remove('wrong'); n.disabled = false; });
    msg.textContent = ''; tries = 0;
    t0 = performance.now();
    cancelAnimationFrame(raf);
    raf = requestAnimationFrame(tick);
  }
  nums.forEach(function (n) {
    n.addEventListener('click', function () {
      if (n.textContent === '42') { finish('ok'); return; }
      tries++;
      n.classList.remove('wrong'); void n.offsetWidth; n.classList.add('wrong');
      n.disabled = true;
      msg.textContent = tries > 1 ? 'One more miss blocks the request' : 'Wrong number. Check the sign-in screen again';
      if (tries > 2) finish('no');
    });
  });
  root.querySelector('.u065-deny').addEventListener('click', function () { finish('no'); });
  res.forEach(function (r) { r.querySelector('button').addEventListener('click', function () { start(); nums[0].focus({ preventScroll: true }); }); });
  start();
})();
</script>
--- Code end ---
