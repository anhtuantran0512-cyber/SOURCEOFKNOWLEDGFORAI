---
source: "lucianlabs"
id: "349"
title: "Pixel-dissolve photo transition"
category: "Sections & Content"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#349"
tags: ["transition", "pixel", "slider", "dissolve", "gallery"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Pixel-dissolve photo transition (349, Sections & Content)
[What it does] Move to the next photo and the frame breaks into a small grid, each cell popping in a piece of the new photo at its own moment until it is covered. Choose how the cells spread: a wave from the left, a ring from the center, or at random.
[How to use it] Change photos with the arrows below, and pick a spread pattern on the right

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
<!-- Lucian UX/UI Prompt #349 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#349 -->
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
.u349{position:relative;width:340px;height:330px;display:flex;flex-direction:column;padding:14px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u349-fr{position:relative;flex:1;border-radius:18px;overflow:hidden;background:var(--bg)}
.u349-cells{position:absolute;inset:0;display:grid;grid-template-columns:repeat(12,1fr);grid-template-rows:repeat(9,1fr)}
.u349-cells i{background-image:var(--nx);background-size:1200% 900%;transform:scale(0);border-radius:2px}
.u349-cells.go i{animation:u349-pop .38s cubic-bezier(.3,1.5,.5,1) both;animation-delay:var(--d)}
@keyframes u349-pop{0%{transform:scale(0);border-radius:50%}70%{transform:scale(1.12)}100%{transform:scale(1.02);border-radius:0}}
.u349-cap{position:absolute;left:14px;bottom:12px;padding:6px 10px;border-radius:999px;background:rgba(0,0,0,.35);color:#fff;font-size:12.5px;font-weight:750;-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
.u349-ft{display:flex;align-items:center;gap:8px;margin-top:12px}
.u349-pv,.u349-nx{width:38px;height:38px;border:0;border-radius:50%;display:grid;place-items:center;background:var(--ux-surface-2);color:var(--ux-ink)}
.u349-ft svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.u349-ms{display:flex;gap:3px;margin-left:auto;padding:3px;border-radius:11px;background:var(--ux-surface-2)}
.u349-m{height:30px;padding:0 10px;border:0;border-radius:8px;background:none;font-size:12px;font-weight:750;color:var(--ux-ink-3)}
.u349-m[aria-pressed="true"]{background:var(--ux-surface);color:var(--ux-ink);box-shadow:0 0 0 1px var(--ux-line)}
</style>
<div class="ux u349">
  <div class="u349-fr" role="img"><div class="u349-cells" aria-hidden="true"></div><span class="u349-cap" aria-hidden="true"></span></div>
  <div class="u349-ft">
    <button class="u349-pv" type="button" aria-label="Previous photo"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg></button>
    <button class="u349-nx" type="button" aria-label="Next photo"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg></button>
    <div class="u349-ms" role="group" aria-label="Spread pattern"><button class="u349-m" type="button" aria-pressed="true">Wave</button><button class="u349-m" type="button" aria-pressed="false">Ring</button><button class="u349-m" type="button" aria-pressed="false">Random</button></div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var fr = root.querySelector('.u349-fr'), cells = root.querySelector('.u349-cells'), cap = root.querySelector('.u349-cap');
  var ms = Array.prototype.slice.call(root.querySelectorAll('.u349-m'));
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var NAMES = ['Dawn lake', 'Desert afternoon', 'Violet night', 'Green forest'];
  var IMG = [
    'radial-gradient(30% 22% at 70% 35%,#FFF3BF,transparent 70%),linear-gradient(#A5D8FF 0,#FFD8A8 45%,#4DABF7 46%,#1864AB 100%)',
    'radial-gradient(22% 18% at 25% 30%,#FFF9DB,transparent 70%),linear-gradient(#FFA94D,#F76707 50%,#E8590C 51%,#C2410C 75%,#9A3412)',
    'radial-gradient(1.5px 1.5px at 30% 30%,#fff,transparent),radial-gradient(1.5px 1.5px at 70% 20%,#fff,transparent),radial-gradient(40% 30% at 50% 100%,#E64980,transparent 70%),linear-gradient(#1B1035,#5F3DC4 70%,#9C36B5)',
    'radial-gradient(50% 30% at 50% 10%,#D3F9D8,transparent 70%),linear-gradient(#69DB7C,#2F9E44 55%,#1B4332)'
  ];
  var cur = 0, mode = 0, busy = false, C = 12, R = 9, list = [];
  for (var y = 0; y < R; y++) for (var x = 0; x < C; x++) {
    var i = document.createElement('i');
    i.style.backgroundPosition = (x / (C - 1) * 100) + '% ' + (y / (R - 1) * 100) + '%';
    cells.appendChild(i); list.push({ el: i, x: x, y: y });
  }
  function show(n) { fr.style.setProperty('--bg', IMG[n]); cap.textContent = NAMES[n]; fr.setAttribute('aria-label', NAMES[n]); }
  function go(n) {
    if (busy) return;
    n = (n + IMG.length) % IMG.length;
    busy = true;
    cells.style.setProperty('--nx', IMG[n]);
    list.forEach(function (c) {
      var d = mode === 0 ? c.x * 45 + c.y * 12 + Math.random() * 60 : mode === 1 ? Math.hypot(c.x - 5.5, (c.y - 4) * 1.2) * 70 + Math.random() * 40 : Math.random() * 650;
      c.el.style.setProperty('--d', Math.round(d) + 'ms');
    });
    cells.classList.remove('go'); void cells.offsetWidth; cells.classList.add('go');
    setTimeout(function () {
      if (!root.isConnected) return;
      show(n); cur = n;
      cells.classList.remove('go');
      busy = false;
    }, rm ? 50 : 1080);
  }
  root.querySelector('.u349-nx').addEventListener('click', function () { go(cur + 1); });
  root.querySelector('.u349-pv').addEventListener('click', function () { go(cur - 1); });
  ms.forEach(function (b, i) { b.addEventListener('click', function () { mode = i; ms.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); }); }); });
  show(0);
})();
</script>
--- Code end ---
