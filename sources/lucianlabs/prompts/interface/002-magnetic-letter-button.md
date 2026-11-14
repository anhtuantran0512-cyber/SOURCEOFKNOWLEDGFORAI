---
source: "lucianlabs"
id: "002"
title: "Magnetic arrow button"
category: "Buttons"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#002"
tags: ["button", "magnetic", "cta", "hover", "arrow"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Magnetic arrow button (002, Buttons)
[What it does] The button and its label are pulled toward the cursor at different depths. Hover and the circle on the right floods the whole button; press it and the arrow shoots out and comes back from the other side.
[How to use it] Move the cursor slowly over the button, then press it

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
<!-- Lucian UX/UI Prompt #002 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#002 -->
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
.u002{--bg:#16151B;--fg:#F7F5F0;--blob:linear-gradient(135deg,#8B6CFF,#4F8DFF 60%,#2FC7B4);
  position:relative;width:340px;height:200px;display:grid;place-items:center}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .u002{--bg:#F4F0E8;--fg:#121117}}
:root[data-theme="dark"] .u002{--bg:#F4F0E8;--fg:#121117}
.u002-mag{transition:translate .9s var(--ux-spring)}
.u002-btn{position:relative;display:flex;align-items:center;gap:18px;height:76px;padding:0 10px 0 32px;border:0;border-radius:999px;background:var(--bg);color:var(--fg);overflow:hidden;isolation:isolate;
  box-shadow:0 24px 40px -24px rgba(40,24,110,.6),0 0 0 1px color-mix(in srgb,var(--fg) 8%,transparent);
  transition:transform .6s var(--ux-spring),box-shadow .6s var(--ux-ease)}
.u002-btn:hover{box-shadow:0 30px 52px -22px rgba(91,72,255,.7),0 0 0 1px transparent}
.u002-btn:active{transform:scale(.96)}
.u002-btn:focus-visible{outline:2px solid var(--ux-accent);outline-offset:5px}

.u002-fill{position:absolute;inset:0;z-index:-1;background:var(--blob);clip-path:circle(28px at calc(100% - 38px) 50%);transition:clip-path .8s var(--ux-ease)}
.u002-btn:hover .u002-fill,.u002-btn:focus-visible .u002-fill{clip-path:circle(160% at calc(100% - 38px) 50%)}
.u002-txt{position:relative;overflow:hidden;padding:5px 0;font-size:19px;font-weight:700;letter-spacing:-.03em;white-space:nowrap;transition:translate .7s var(--ux-spring),color .5s var(--ux-ease)}
.u002-btn:hover .u002-txt{color:#fff}
.u002-txt span{display:block;transition:transform .6s var(--ux-spring),opacity .35s var(--ux-ease)}
.u002-txt span+span{position:absolute;left:0;top:5px;transform:translateY(130%);opacity:0}
.u002[data-state="go"] .u002-txt span:first-child{transform:translateY(-130%);opacity:0}
.u002[data-state="go"] .u002-txt span+span{transform:none;opacity:1}
.u002-orb{position:relative;width:56px;height:56px;border-radius:50%;display:grid;place-items:center;color:#fff;overflow:hidden;flex:none;transition:translate .7s var(--ux-spring)}
.u002-orb svg{position:absolute;width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.u002-orb svg:last-child{transform:translateX(-46px)}
.u002[data-state="go"] .u002-orb svg:first-child{animation:u002-out .55s var(--ux-ease) forwards}
.u002[data-state="go"] .u002-orb svg:last-child{animation:u002-in .6s var(--ux-spring) .28s forwards}
@keyframes u002-out{to{transform:translateX(46px)}}
@keyframes u002-in{to{transform:none}}
.u002-glow{position:absolute;left:50%;top:50%;width:300px;height:110px;margin:-40px 0 0 -150px;border-radius:50%;background:var(--blob);filter:blur(36px);opacity:0;z-index:-1;transition:opacity .7s var(--ux-ease)}
.u002:hover .u002-glow{opacity:.45}
.u002-live{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
</style>
<div class="ux u002" data-state="idle">
  <span class="u002-glow" aria-hidden="true"></span>
  <div class="u002-mag">
    <button class="u002-btn" type="button">
      <span class="u002-fill" aria-hidden="true"></span>
      <span class="u002-txt"><span>Start a project</span><span aria-hidden="true">You’re all set</span></span>
      <span class="u002-orb" aria-hidden="true">
        <svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg>
        <svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg>
      </span>
    </button>
  </div>
  <span class="u002-live" aria-live="polite"></span>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var btn = root.querySelector('.u002-btn');
  var mag = root.querySelector('.u002-mag');
  var txt = root.querySelector('.u002-txt');
  var orb = root.querySelector('.u002-orb');
  var live = root.querySelector('.u002-live');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var t = 0;

  root.addEventListener('pointermove', function (e) {
    if (rm) return;
    var r = btn.getBoundingClientRect();
    var dx = e.clientX - (r.left + r.width / 2);
    var dy = e.clientY - (r.top + r.height / 2);
    var p = Math.max(0, 1 - Math.hypot(dx, dy) / 240);
    mag.style.translate = (dx * 0.12 * p).toFixed(1) + 'px ' + (dy * 0.22 * p).toFixed(1) + 'px';
    txt.style.translate = (dx * 0.05 * p).toFixed(1) + 'px ' + (dy * 0.08 * p).toFixed(1) + 'px';
    orb.style.translate = (dx * 0.1 * p).toFixed(1) + 'px ' + (dy * 0.14 * p).toFixed(1) + 'px';
  });
  root.addEventListener('pointerleave', function () {
    mag.style.translate = txt.style.translate = orb.style.translate = '0px 0px';
  });

  btn.addEventListener('click', function () {
    clearTimeout(t);
    root.dataset.state = 'idle';
    void btn.offsetWidth;
    root.dataset.state = 'go';
    live.textContent = 'You’re all set';
    t = setTimeout(function () { if (root.isConnected) { root.dataset.state = 'idle'; live.textContent = ''; } }, rm ? 900 : 1900);
  });
})();
</script>
--- Code end ---
