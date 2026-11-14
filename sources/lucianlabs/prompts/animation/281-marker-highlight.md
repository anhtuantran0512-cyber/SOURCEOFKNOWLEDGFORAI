---
source: "lucianlabs"
id: "281"
title: "Sweeping highlighter"
category: "Text Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#281"
tags: ["text", "highlight", "marker", "emphasis", "reading"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Sweeping highlighter (281, Text Motion)
[What it does] A highlighter sweeps across the key phrases of a paragraph from left to right, one after another. A phrase that wraps is filled to the end of the first line before continuing on the next, and longer phrases take longer. Change the pen and the strokes bleed into the new color; ‘Redraw’ lifts them off and paints again from the start.
[How to use it] Pick a pen color below or press ‘Redraw’

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
<!-- Lucian UX/UI Prompt #281 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#281 -->
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
@property --u281-m{syntax:"<color>";inherits:true;initial-value:#FFD43B}
.u281{position:relative;width:340px;height:318px;display:flex;flex-direction:column;padding:22px 22px 18px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden;--u281-m:#FFD43B;transition:--u281-m .7s var(--ux-ease)}
.u281-k{margin:0;font-size:12px;font-weight:750;color:var(--ux-ink-3)}
.u281-p{margin:12px 0 0;font-size:19.5px;line-height:1.62;font-weight:650;letter-spacing:-.025em;color:var(--ux-ink-2)}
.u281-p mark{color:var(--ux-ink);border-radius:3px;
  background-image:linear-gradient(100deg,transparent .15em,color-mix(in srgb,var(--u281-m) 58%,transparent) .3em,color-mix(in srgb,var(--u281-m) 52%,transparent) calc(100% - .3em),transparent calc(100% - .1em));
  background-repeat:no-repeat;background-position:0 72%;background-size:0% 62%;transition:background-size var(--d,.6s) cubic-bezier(.55,.1,.3,1) var(--w,0s)}
.u281.is-on .u281-p mark{background-size:100% 62%}
.u281.is-off .u281-p mark{transition:background-size .35s ease;background-size:0% 62%}
.u281-ft{margin-top:auto;display:flex;align-items:center;gap:8px}
.u281-pens{display:flex;gap:6px;flex:1}
.u281-pen{position:relative;width:36px;height:36px;border:0;border-radius:12px;background:var(--ux-surface-2);display:grid;place-items:center;transition:transform .35s var(--ux-spring),box-shadow .25s}
.u281-pen i{width:12px;height:22px;border-radius:3px 3px 6px 6px;background:var(--c);transform:rotate(30deg);box-shadow:inset 0 -6px 0 rgba(0,0,0,.18)}
.u281-pen[aria-pressed="true"]{box-shadow:0 0 0 2px var(--ux-ink)}
.u281-pen:active{transform:scale(.9)}
.u281-again{height:38px;padding:0 15px;border:0;border-radius:999px;background:var(--ux-ink);color:var(--ux-page);font-size:13px;font-weight:750;transition:transform .35s var(--ux-spring)}
.u281-again:active{transform:scale(.93)}
</style>
<div class="ux u281">
  <p class="u281-k">Design notes · ch. 3</p>
  <p class="u281-p">A good interface <mark>can be used without explanation</mark>, leaves <mark>a quiet way back</mark> when you slip, and above all <mark>moves at a human pace.</mark></p>
  <div class="u281-ft">
    <div class="u281-pens" role="group" aria-label="Pen color">
      <button class="u281-pen" type="button" aria-pressed="true" aria-label="Yellow" style="--c:#FFD43B"><i></i></button>
      <button class="u281-pen" type="button" aria-pressed="false" aria-label="Mint" style="--c:#38D9A9"><i></i></button>
      <button class="u281-pen" type="button" aria-pressed="false" aria-label="Pink" style="--c:#FF6B9D"><i></i></button>
    </div>
    <button class="u281-again" type="button">Redraw</button>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var marks = Array.prototype.slice.call(root.querySelectorAll('mark'));
  var pens = Array.prototype.slice.call(root.querySelectorAll('.u281-pen'));
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var t = 0;
  function timing() {
    var at = 0.25;
    marks.forEach(function (m) {
      var d = Math.min(1.4, 0.25 + m.textContent.length * 0.045);
      m.style.setProperty('--d', d.toFixed(2) + 's');
      m.style.setProperty('--w', at.toFixed(2) + 's');
      at += d + 0.12;
    });
  }
  function draw() {
    clearTimeout(t);
    root.classList.remove('is-on');
    root.classList.add('is-off');
    t = setTimeout(function () {
      if (!root.isConnected) return;
      root.classList.remove('is-off');
      void root.offsetWidth;
      root.classList.add('is-on');
    }, rm ? 0 : 380);
  }
  pens.forEach(function (p) {
    p.addEventListener('click', function () {
      pens.forEach(function (x) { x.setAttribute('aria-pressed', String(x === p)); });
      root.style.setProperty('--u281-m', p.style.getPropertyValue('--c'));
    });
  });
  root.querySelector('.u281-again').addEventListener('click', draw);
  timing();
  requestAnimationFrame(function () { requestAnimationFrame(function () { root.classList.add('is-on'); }); });
})();
</script>
--- Code end ---
