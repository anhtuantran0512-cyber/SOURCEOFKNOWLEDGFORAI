---
source: "lucianlabs"
id: "205"
title: "Rippling letter logo"
category: "Text Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#205"
tags: ["text", "wave", "spring", "logo", "hover"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Rippling letter logo (205, Text Motion)
[What it does] Letters near the cursor rise and settle, and their neighbours follow less the farther away they are. Each letter wobbles on its own spring before coming to rest, and the higher it rises the more its color blooms and its floor shadow shrinks. Press the button to send one big wave from left to right.
[How to use it] Move the cursor across the letters. Change the wave height with the slider and press ‘Send a wave’

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
<!-- Lucian UX/UI Prompt #205 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#205 -->
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
.u205{position:relative;width:340px;height:300px;display:flex;flex-direction:column;padding:20px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u205-sea{position:absolute;left:0;right:0;bottom:0;height:120px;background:linear-gradient(transparent,color-mix(in srgb,var(--ux-accent-2) 10%,transparent));pointer-events:none}
.u205-wd{position:relative;flex:1;display:flex;align-items:center;justify-content:center;gap:1px;cursor:default;touch-action:none}
.u205-l{position:relative;display:inline-block;font-size:62px;line-height:1;font-weight:900;letter-spacing:-.03em;color:color-mix(in oklab,var(--ux-accent) calc(var(--t,0) * 100%),var(--ux-ink));transform:translateY(var(--y,0px)) scaleY(var(--sy,1));transform-origin:50% 100%;will-change:transform}
.u205-l::after{content:"";position:absolute;left:12%;right:12%;bottom:-14px;height:6px;border-radius:50%;background:var(--ux-shadow-strong);opacity:calc(.5 - var(--t,0) * .35);transform:translateY(calc(var(--y,0px) * -1)) scaleX(calc(1 - var(--t,0) * .5));filter:blur(2px)}
.u205-ft{position:relative;display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:18px;background:var(--ux-surface-2)}
.u205-ft label{display:flex;flex-direction:column;gap:6px;flex:1;font-size:11.5px;font-weight:700;color:var(--ux-ink-3)}
.u205-ft label span{display:flex;justify-content:space-between}
.u205-ft label b{color:var(--ux-ink);font-variant-numeric:tabular-nums}
.u205-r{width:100%;height:18px;margin:0;accent-color:var(--ux-accent)}
.u205-go{flex:none;height:40px;padding:0 15px;border:0;border-radius:13px;background:var(--ux-ink);color:var(--ux-page);font-size:13px;font-weight:750;transition:transform .35s var(--ux-spring)}
.u205-go:active{transform:scale(.93)}
</style>
<div class="ux u205">
  <div class="u205-sea" aria-hidden="true"></div>
  <div class="u205-wd" role="img" aria-label="MOTION"></div>
  <div class="u205-ft">
    <label><span>Wave height<b class="u205-v">34</b></span><input class="u205-r" type="range" min="10" max="64" value="34" aria-label="Wave height"></label>
    <button class="u205-go" type="button">Send a wave</button>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var wd = root.querySelector('.u205-wd'), range = root.querySelector('.u205-r'), val = root.querySelector('.u205-v');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var WORD = 'MOTION', SIG = 34;
  var amp = 34, px = null, pulse = null, raf = 0;
  var L = Array.from(WORD).map(function (ch) {
    var s = document.createElement('span');
    s.className = 'u205-l'; s.textContent = ch; s.setAttribute('aria-hidden', 'true');
    wd.appendChild(s);
    return { el: s, x: 0, y: 0, v: 0 };
  });
  function measure() { L.forEach(function (l) { l.x = l.el.offsetLeft + l.el.offsetWidth / 2; }); }
  function g(d, s) { return Math.exp(-(d * d) / (2 * s * s)); }
  function tick(now) {
    raf = 0;
    if (!root.isConnected) return;
    var moving = false, pc = null;
    if (pulse) {
      var k = (now - pulse) / 1100;
      if (k >= 1) pulse = null; else pc = -60 + (wd.offsetWidth + 120) * k;
    }
    L.forEach(function (l) {
      var tgt = 0;
      if (px != null) tgt -= amp * g(l.x - px, SIG);
      if (pc != null) tgt -= amp * 1.35 * g(l.x - pc, SIG * 1.2);
      l.v += (tgt - l.y) * 0.16;
      l.v *= 0.8;
      l.y += l.v;
      if (Math.abs(l.v) > 0.02 || Math.abs(tgt - l.y) > 0.05) moving = true;
      var t = Math.min(1, Math.max(0, -l.y / 50));
      l.el.style.setProperty('--y', l.y.toFixed(2) + 'px');
      l.el.style.setProperty('--sy', (1 + Math.max(-0.08, Math.min(0.14, -l.v * 0.02))).toFixed(3));
      l.el.style.setProperty('--t', t.toFixed(3));
    });
    if (moving || pulse || px != null) raf = requestAnimationFrame(tick);
  }
  function kick() { if (!raf && !rm) raf = requestAnimationFrame(tick); }
  function local(e) { var r = wd.getBoundingClientRect(); return (e.clientX - r.left) * (wd.offsetWidth / (r.width || 1)); }
  wd.addEventListener('pointermove', function (e) { if (!L[0].x) measure(); px = local(e); kick(); });
  wd.addEventListener('pointerleave', function () { px = null; kick(); });
  range.addEventListener('input', function () { amp = +range.value; val.textContent = range.value; kick(); });
  root.querySelector('.u205-go').addEventListener('click', function () { measure(); pulse = performance.now(); kick(); });
  measure();
})();
</script>
--- Code end ---
