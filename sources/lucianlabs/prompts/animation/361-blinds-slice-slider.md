---
source: "lucianlabs"
id: "361"
title: "Venetian-blind slide flip"
category: "Sections & Content"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#361"
tags: ["transition", "3d", "slider", "blinds", "carousel"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Venetian-blind slide flip (361, Sections & Content)
[What it does] Move to the next slide and the frame splits into eight vertical strips that flip over one after another to reveal the new scene on their backs. The strip edges darken as they turn so you can feel their thickness, and depending on direction the left or right strips go first.
[How to use it] Press the arrows or a dot below to change scenes

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
<!-- Lucian UX/UI Prompt #361 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#361 -->
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
@property --u361-e{syntax:"<number>";inherits:true;initial-value:0}
.u361{position:relative;width:340px;height:330px;display:flex;flex-direction:column;padding:14px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u361-fr{position:relative;flex:1;display:flex;border-radius:18px;overflow:hidden;perspective:800px}
.u361-s{position:relative;flex:1;margin-right:-.6px;transform-style:preserve-3d}
.u361-s i{position:absolute;inset:0;backface-visibility:hidden;background-size:800% 100%}
.u361-s i.b{transform:rotateY(180deg)}
.u361-s i::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,var(--u361-e)),transparent 30%,transparent 70%,rgba(0,0,0,var(--u361-e)))}
.u361-tx{position:absolute;left:16px;bottom:14px;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.35);pointer-events:none;transition:opacity .3s,transform .5s var(--ux-spring)}
.u361-tx.swap{opacity:0;transform:translateY(10px)}
.u361-tx b{display:block;font-size:28px;font-weight:900;letter-spacing:-.04em}
.u361-tx span{font-size:13px;font-weight:700}
.u361-ft{display:flex;align-items:center;gap:8px;margin-top:12px}
.u361-pv,.u361-nx{width:38px;height:38px;border:0;border-radius:50%;display:grid;place-items:center;background:var(--ux-surface-2);color:var(--ux-ink)}
.u361-ft svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.u361-dots{flex:1;display:flex;justify-content:center;gap:4px}
.u361-dot{width:26px;height:26px;border:0;background:none;display:grid;place-items:center}
.u361-dot::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--ux-line-2);transition:width .4s var(--ux-spring),background-color .3s,border-radius .3s}
.u361-dot[aria-pressed="true"]::before{width:20px;border-radius:4px;background:var(--ux-ink)}
</style>
<div class="ux u361">
  <div class="u361-fr" role="img"><div class="u361-tx"><b></b><span></span></div></div>
  <div class="u361-ft"><button class="u361-pv" type="button" aria-label="Previous scene"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg></button><div class="u361-dots" role="group" aria-label="Pick a scene"></div><button class="u361-nx" type="button" aria-label="Next scene"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg></button></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var fr = root.querySelector('.u361-fr'), tx = root.querySelector('.u361-tx'), dotsEl = root.querySelector('.u361-dots');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var SL = [['Spring', 'First picnic under the blossoms'], ['Summer', 'An afternoon by the waves'], ['Autumn', 'Slowly down the maple road'], ['Winter', 'A window on a snowy night']];
  var IMG = [
    'radial-gradient(18% 14% at 30% 30%,#FFDEEB,transparent 70%),radial-gradient(22% 16% at 70% 25%,#FCC2D7,transparent 70%),linear-gradient(#FFF0F6,#FFDEEB 50%,#8CE99A 51%,#40C057)',
    'radial-gradient(20% 16% at 75% 25%,#FFF3BF,transparent 70%),linear-gradient(#74C0FC,#D0EBFF 45%,#3BC9DB 46%,#0B7285 80%,#FFE8CC 81%)',
    'radial-gradient(30% 25% at 30% 60%,#FF922B,transparent 70%),radial-gradient(30% 25% at 70% 50%,#E03131,transparent 70%),linear-gradient(#FFE8CC,#FFC078 50%,#8C5A3C 51%,#5C3D2E)',
    'radial-gradient(1.5px 1.5px at 20% 20%,#fff,transparent),radial-gradient(1.5px 1.5px at 60% 40%,#fff,transparent),radial-gradient(1.5px 1.5px at 80% 15%,#fff,transparent),radial-gradient(30% 20% at 50% 80%,#FFD43B,transparent 70%),linear-gradient(#1C2A4A,#364FC7 60%,#E7F5FF 61%,#C5D7EE)'
  ];
  var N = 8, cur = 0, busy = false, strips = [];
  for (var i = 0; i < N; i++) {
    var s = document.createElement('div');
    s.className = 'u361-s';
    s.innerHTML = '<i class="f"></i><i class="b"></i>';
    s.querySelectorAll('i').forEach(function (f) { f.style.backgroundPosition = (i / (N - 1) * 100) + '% 0'; });
    fr.insertBefore(s, tx);
    strips.push(s);
  }
  var dots = SL.map(function (_, k) {
    var d = document.createElement('button');
    d.type = 'button'; d.className = 'u361-dot'; d.setAttribute('aria-label', SL[k][0]); d.setAttribute('aria-pressed', String(k === 0));
    d.addEventListener('click', function () { if (k !== cur) go(k, k > cur ? 1 : -1); });
    dotsEl.appendChild(d);
    return d;
  });
  function face(s, side, k) { s.querySelector('i.' + side).style.backgroundImage = IMG[k]; }
  function text(k) {
    tx.classList.add('swap');
    setTimeout(function () { tx.querySelector('b').textContent = SL[k][0]; tx.querySelector('span').textContent = SL[k][1]; tx.classList.remove('swap'); }, rm ? 0 : 320);
    fr.setAttribute('aria-label', SL[k][0] + ', ' + SL[k][1]);
    dots.forEach(function (d, j) { d.setAttribute('aria-pressed', String(j === k)); });
  }
  function go(k, dir) {
    if (busy) return;
    k = (k + SL.length) % SL.length;
    busy = true;
    text(k);
    strips.forEach(function (s, i) {
      face(s, 'b', k);
      var order = dir > 0 ? i : N - 1 - i;
      if (rm || !s.animate) return;
      var a = s.animate([{ transform: 'rotateY(0deg)' }, { transform: 'rotateY(' + (dir > 0 ? -90 : 90) + 'deg) scale(.96)', offset: 0.5 }, { transform: 'rotateY(' + (dir > 0 ? -180 : 180) + 'deg)' }], { duration: 650, delay: order * 70, easing: 'cubic-bezier(.5,0,.3,1)', fill: 'both' });
      s.querySelectorAll('i').forEach(function (f) { f.animate([{ '--u361-e': 0 }, { '--u361-e': 0.5 }, { '--u361-e': 0 }], { duration: 650, delay: order * 70 }); });
    });
    setTimeout(function () {
      if (!root.isConnected) return;
      strips.forEach(function (s) { face(s, 'f', k); if (s.getAnimations) s.getAnimations().forEach(function (a) { a.cancel(); }); });
      cur = k; busy = false;
    }, rm ? 10 : 650 + (N - 1) * 70 + 30);
  }
  root.querySelector('.u361-nx').addEventListener('click', function () { go(cur + 1, 1); });
  root.querySelector('.u361-pv').addEventListener('click', function () { go(cur - 1, -1); });
  strips.forEach(function (s) { face(s, 'f', 0); });
  tx.querySelector('b').textContent = SL[0][0]; tx.querySelector('span').textContent = SL[0][1];
  fr.setAttribute('aria-label', SL[0][0] + ', ' + SL[0][1]);
})();
</script>
--- Code end ---
