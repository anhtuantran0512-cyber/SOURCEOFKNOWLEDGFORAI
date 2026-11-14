---
source: "lucianlabs"
id: "223"
title: "Shrinking sticky card stack"
category: "Scroll Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#223"
tags: ["scroll", "sticky", "stack", "cards", "features"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Shrinking sticky card stack (223, Scroll Motion)
[What it does] As you scroll, each card comes to rest at the top, and while the next card slides over it, the one underneath shrinks, darkens and recedes. By the last card the stacked cards form steps.
[How to use it] Scroll down inside the card

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
<!-- Lucian UX/UI Prompt #223 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#223 -->
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
.u223{position:relative;width:300px;height:500px;border-radius:30px;background:var(--ux-surface-2);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u223-sc{position:absolute;inset:0;overflow-y:auto;padding:22px 16px 30px;scrollbar-width:none;outline:none}
.u223-sc::-webkit-scrollbar{display:none}
.u223-k{margin:0 4px 14px;font-size:22px;font-weight:880;letter-spacing:-.04em}
.u223-c{position:sticky;height:330px;margin-bottom:24px;padding:20px;border-radius:24px;color:#fff;transform-origin:50% 0;will-change:transform;box-shadow:0 -10px 30px -18px rgba(0,0,0,.35);display:flex;flex-direction:column}
.u223-c i{font:800 12px/1 ui-monospace,SFMono-Regular,Menlo,monospace;opacity:.7;font-style:normal}
.u223-c b{display:block;margin-top:auto;font-size:26px;line-height:1.15;font-weight:880;letter-spacing:-.04em}
.u223-c p{margin:8px 0 0;font-size:14px;line-height:1.5;opacity:.85}
.u223-art{position:absolute;right:18px;top:18px;width:90px;height:90px;border-radius:26px;background:rgba(255,255,255,.18);transform:rotate(12deg)}
.u223-art::after{content:"";position:absolute;inset:22px;border-radius:50%;background:rgba(255,255,255,.35)}
.u223-sh{position:absolute;inset:0;border-radius:inherit;background:#000;opacity:0;pointer-events:none}
.u223-end{height:120px;display:grid;place-items:center}
.u223-end button{height:44px;padding:0 22px;border:0;border-radius:999px;background:var(--ux-ink);color:var(--ux-page);font-size:14px;font-weight:800}
</style>
<div class="ux u223">
  <div class="u223-sc" tabindex="0" aria-label="Features, scroll to browse">
    <p class="u223-k">How it works</p>
    <div class="u223-list"></div>
    <div class="u223-end"><button type="button">Get started</button></div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u223-sc'), list = root.querySelector('.u223-list');
  var CARDS = [['01', 'Plan in one place', 'Gather scattered notes and docs onto one board.'], ['02', 'Refine together', 'Comments and versions stay in the same spot.'], ['03', 'Share instantly', 'Show it beyond your team with a single link.'], ['04', 'Check the numbers', 'Get a summary of the response every morning.']];
  var BG = ['linear-gradient(150deg,#7048E8,#4C6EF5)', 'linear-gradient(150deg,#F76707,#F59F00)', 'linear-gradient(150deg,#0CA678,#15AABF)', 'linear-gradient(150deg,#E64980,#BE4BDB)'];
  var cards = CARDS.map(function (c, i) {
    var el = document.createElement('article');
    el.className = 'u223-c';
    el.style.top = (14 + i * 12) + 'px';
    el.style.background = BG[i];
    el.innerHTML = '<span class="u223-art" aria-hidden="true"></span><i></i><b></b><p></p><span class="u223-sh" aria-hidden="true"></span>';
    el.querySelector('i').textContent = c[0];
    el.querySelector('b').textContent = c[1];
    el.querySelector('p').textContent = c[2];
    list.appendChild(el);
    return el;
  });
  var raf = 0;
  function draw() {
    raf = 0;
    var top = sc.getBoundingClientRect().top, k = sc.offsetHeight / (sc.getBoundingClientRect().height || 1);
    var pos = cards.map(function (c) { return (c.getBoundingClientRect().top - top) * k; });
    cards.forEach(function (c, i) {
      var depth = 0;
      for (var j = i + 1; j < cards.length; j++) {
        var stick = 14 + j * 12, d = (pos[j] - stick) / 330;
        depth += Math.max(0, Math.min(1, 1 - d));
      }
      c.style.transform = 'scale(' + (1 - depth * 0.06).toFixed(3) + ')';
      c.querySelector('.u223-sh').style.opacity = (depth * 0.18).toFixed(3);
    });
  }
  sc.addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(draw); }, { passive: true });
  requestAnimationFrame(draw);
})();
</script>
--- Code end ---
