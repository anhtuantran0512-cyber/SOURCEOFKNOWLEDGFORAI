---
source: "lucianlabs"
id: "001"
title: "Liquid glass button"
category: "Buttons"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#001"
tags: ["button", "glass", "loading", "success", "magnetic"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Liquid glass button (001, Buttons)
[What it does] A glass capsule with light caught inside. Press it and it shrinks like a water drop to show loading, then expands again with a check mark.
[How to use it] Move the cursor near the button, then press it

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
<!-- Lucian UX/UI Prompt #001 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#001 -->
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
.u001{--g1:rgba(255,255,255,.66);--g2:rgba(255,255,255,.16);--g3:rgba(255,255,255,.4);--hi:rgba(255,255,255,.95);--rim:rgba(255,255,255,.65);--drop:rgba(70,48,160,.42);--blob:.55;
  position:relative;width:340px;height:240px;display:grid;place-items:center;isolation:isolate}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .u001{--g1:rgba(255,255,255,.2);--g2:rgba(255,255,255,.03);--g3:rgba(255,255,255,.1);--hi:rgba(255,255,255,.5);--rim:rgba(255,255,255,.16);--drop:rgba(0,0,0,.75);--blob:.5}}
:root[data-theme="dark"] .u001{--g1:rgba(255,255,255,.2);--g2:rgba(255,255,255,.03);--g3:rgba(255,255,255,.1);--hi:rgba(255,255,255,.5);--rim:rgba(255,255,255,.16);--drop:rgba(0,0,0,.75);--blob:.5}
.u001-blobs{position:absolute;inset:0;z-index:-1;pointer-events:none}
.u001-blobs i{position:absolute;border-radius:50%;filter:blur(30px);opacity:var(--blob);animation:u001-drift 12s ease-in-out infinite alternate}
.u001-blobs i:nth-child(1){left:30px;top:44px;width:150px;height:130px;background:#8B6CFF}
.u001-blobs i:nth-child(2){right:24px;bottom:34px;width:160px;height:118px;background:#33B6FF;animation-delay:-4s}
.u001-blobs i:nth-child(3){left:150px;top:36px;width:92px;height:92px;background:#3BE0B0;opacity:calc(var(--blob) * .7);animation-delay:-8s}
@keyframes u001-drift{from{transform:translate3d(-10px,-6px,0) scale(1)}to{transform:translate3d(12px,8px,0) scale(1.12)}}
.u001-mag{transition:translate .8s var(--ux-spring)}
.u001-float{animation:u001-float 6s ease-in-out infinite}
@keyframes u001-float{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}
.u001-btn{position:relative;display:block;width:252px;height:78px;padding:0;border:0;border-radius:999px;overflow:hidden;isolation:isolate;color:var(--ux-ink);
  background:linear-gradient(150deg,var(--g1),var(--g2) 55%,var(--g3));
  -webkit-backdrop-filter:blur(18px) saturate(180%);backdrop-filter:blur(18px) saturate(180%);
  box-shadow:inset 0 1.5px 0 var(--hi),inset 0 -12px 20px -14px var(--hi),inset 0 0 0 1px var(--rim),0 26px 44px -22px var(--drop),0 3px 8px -4px var(--drop);
  transition:width .7s var(--ux-ease),transform .55s var(--ux-spring),box-shadow .6s var(--ux-ease)}
.u001-btn::before{content:"";position:absolute;left:9%;right:9%;top:7%;height:42%;border-radius:999px;pointer-events:none;background:linear-gradient(180deg,rgba(255,255,255,.42),rgba(255,255,255,0))}
.u001-btn::after{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;opacity:0;transition:opacity .4s var(--ux-ease);background:radial-gradient(130px 70px at var(--mx,50%) var(--my,0%),rgba(255,255,255,.4),transparent 70%)}
.u001-btn:hover::after{opacity:1}
.u001-btn:active{transform:scale(1.03,.92)}
.u001-btn:focus-visible{outline:2px solid var(--ux-accent);outline-offset:6px}
.u001-sheen{position:absolute;top:-40%;bottom:-40%;left:0;width:38%;pointer-events:none;background:linear-gradient(100deg,transparent,rgba(255,255,255,.45) 50%,transparent);transform:translateX(-150%) skewX(-12deg);transition:transform 1.1s var(--ux-ease)}
.u001-btn:hover .u001-sheen{transform:translateX(300%) skewX(-12deg)}
.u001-txt,.u001-done{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:10px;font-size:18px;font-weight:680;letter-spacing:-.025em;white-space:nowrap;transition:opacity .35s var(--ux-ease),transform .55s var(--ux-ease),filter .4s var(--ux-ease)}
.u001-done{opacity:0;transform:translateY(14px);filter:blur(4px)}
.u001-done b{width:30px;height:30px;border-radius:50%;display:grid;place-items:center;background:var(--ux-mint);color:#fff;box-shadow:0 0 0 6px color-mix(in srgb,var(--ux-mint) 22%,transparent)}
.u001-done svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2.8;stroke-linecap:round;stroke-linejoin:round}
.u001-done path{stroke-dasharray:18;stroke-dashoffset:18;transition:stroke-dashoffset .5s var(--ux-ease) .3s}
.u001-spin{position:absolute;left:50%;top:50%;width:30px;height:30px;margin:-15px 0 0 -15px;opacity:0;transform:scale(.5);transition:opacity .35s var(--ux-ease),transform .6s var(--ux-spring)}
.u001-spin svg{width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;animation:u001-rot 1s linear infinite}
.u001-spin circle{stroke-dasharray:1 56;animation:u001-arc 1.4s ease-in-out infinite}
@keyframes u001-rot{to{transform:rotate(360deg)}}
@keyframes u001-arc{0%,100%{stroke-dasharray:1 56}50%{stroke-dasharray:38 19}}
.u001[data-state="load"] .u001-btn{width:78px;cursor:progress}
.u001[data-state="load"] .u001-txt{opacity:0;transform:translateY(-14px);filter:blur(5px)}
.u001[data-state="load"] .u001-spin{opacity:1;transform:none}
.u001[data-state="ok"] .u001-btn{transition-timing-function:var(--ux-spring);box-shadow:inset 0 1.5px 0 var(--hi),inset 0 0 0 1px var(--rim),0 26px 44px -22px var(--drop),0 0 52px -8px color-mix(in srgb,var(--ux-mint) 70%,transparent)}
.u001[data-state="ok"] .u001-txt{opacity:0;transform:translateY(-14px);filter:blur(5px)}
.u001[data-state="ok"] .u001-done{opacity:1;transform:none;filter:none}
.u001[data-state="ok"] .u001-done path{stroke-dashoffset:0}
.u001-live{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
</style>
<div class="ux u001" data-state="idle">
  <div class="u001-blobs" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="u001-mag">
    <div class="u001-float">
      <button class="u001-btn" type="button">
        <span class="u001-sheen" aria-hidden="true"></span>
        <span class="u001-txt">Continue</span>
        <span class="u001-spin" aria-hidden="true"><svg viewBox="0 0 30 30"><circle cx="15" cy="15" r="10"/></svg></span>
        <span class="u001-done" aria-hidden="true"><b><svg viewBox="0 0 16 16"><path d="M3.5 8.4l3 3 6-6.4"/></svg></b>Saved</span>
      </button>
    </div>
  </div>
  <span class="u001-live" aria-live="polite"></span>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var btn = root.querySelector('.u001-btn');
  var mag = root.querySelector('.u001-mag');
  var live = root.querySelector('.u001-live');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var timers = [];
  function later(fn, ms) { timers.push(setTimeout(function () { if (root.isConnected) fn(); }, ms)); }
  function clear() { timers.forEach(clearTimeout); timers = []; }

  root.addEventListener('pointermove', function (e) {
    var r = btn.getBoundingClientRect();
    var dx = e.clientX - (r.left + r.width / 2);
    var dy = e.clientY - (r.top + r.height / 2);
    var pull = rm ? 0 : Math.max(0, 1 - Math.hypot(dx, dy) / 190);
    mag.style.translate = (dx * 0.18 * pull).toFixed(1) + 'px ' + (dy * 0.18 * pull).toFixed(1) + 'px';
    btn.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100).toFixed(1) + '%');
    btn.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100).toFixed(1) + '%');
  });
  root.addEventListener('pointerleave', function () { mag.style.translate = '0px 0px'; });

  btn.addEventListener('click', function () {
    if (root.dataset.state === 'load') return;
    clear();
    root.dataset.state = 'load';
    btn.setAttribute('aria-busy', 'true');
    live.textContent = 'Saving';
    later(function () {
      root.dataset.state = 'ok';
      btn.removeAttribute('aria-busy');
      live.textContent = 'Saved';
    }, rm ? 200 : 1600);
    later(function () { root.dataset.state = 'idle'; live.textContent = ''; }, rm ? 1200 : 3600);
  });
})();
</script>
--- Code end ---
