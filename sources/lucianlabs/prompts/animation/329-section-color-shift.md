---
source: "lucianlabs"
id: "329"
title: "Background that shifts per section"
category: "Scroll Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#329"
tags: ["scroll", "color", "product", "sticky", "brand"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Background that shifts per section (329, Scroll Motion)
[What it does] Scroll through the product and at every section the whole background blends into the next flavor’s color, while the drink can pinned in the middle turns to match and its label and name change. The color never jumps between sections; it keeps blending as far as you scroll.
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
<!-- Lucian UX/UI Prompt #329 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#329 -->
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
.u329{position:relative;width:300px;height:500px;border-radius:30px;background:var(--bg,#FF8A65);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden;color:#1B1B22}
.u329-sc{position:absolute;inset:0;overflow-y:auto;scrollbar-width:none;outline:none}
.u329-sc::-webkit-scrollbar{display:none}
.u329-stage{position:sticky;top:0;height:500px;display:flex;align-items:flex-start;justify-content:center;padding-top:74px;pointer-events:none}
.u329-can{position:relative;width:104px;height:196px;border-radius:26px 26px 22px 22px;background:linear-gradient(90deg,rgba(0,0,0,.25),rgba(255,255,255,.35) 30%,rgba(255,255,255,.05) 55%,rgba(0,0,0,.28)),var(--can,#E64A19);box-shadow:0 30px 40px -24px rgba(0,0,0,.45);transform:rotate(var(--r,0deg));overflow:hidden}
.u329-can::before{content:"";position:absolute;left:8px;right:8px;top:0;height:14px;border-radius:0 0 8px 8px;background:linear-gradient(#E9ECEF,#ADB5BD)}
.u329-lab{position:absolute;left:0;right:0;top:64px;height:80px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(255,255,255,.9);transform:translateX(var(--lx,0px))}
.u329-lab b{font-size:16px;font-weight:900;letter-spacing:-.02em;color:var(--can,#E64A19)}
.u329-lab i{font-size:9px;font-style:normal;font-weight:800;letter-spacing:.2em;color:#555}
.u329-k{position:absolute;left:20px;top:20px;margin:0;font-size:13px;font-weight:800;opacity:.75}
.u329-dots{position:absolute;right:18px;top:50%;display:flex;flex-direction:column;gap:7px;transform:translateY(-50%)}
.u329-dots i{width:6px;height:6px;border-radius:50%;background:rgba(0,0,0,.25);transition:transform .3s,background-color .3s}
.u329-dots i.on{background:#1B1B22;transform:scale(1.5)}
.u329-secs{position:relative;margin-top:-500px}
.u329-sec{height:420px;display:flex;flex-direction:column;justify-content:flex-end;padding:0 22px 30px}
.u329-sec:first-child{height:500px}
.u329-sec b{font-size:30px;font-weight:900;letter-spacing:-.04em}
.u329-sec span{font-size:14px;font-weight:700;opacity:.75}
</style>
<div class="ux u329">
  <div class="u329-sc" tabindex="0" aria-label="Flavors, scroll to browse">
    <div class="u329-stage" aria-hidden="true"><p class="u329-k">Four sparkling flavors</p><div class="u329-can"><div class="u329-lab"><i>SPARKLING</i><b></b></div></div><div class="u329-dots"></div></div>
    <div class="u329-secs"></div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u329-sc'), secs = root.querySelector('.u329-secs'), lab = root.querySelector('.u329-lab b'), dots = root.querySelector('.u329-dots');
  var FLAV = [['Grapefruit', 'A bright, bittersweet morning'], ['Green grape', 'A light, fizzy afternoon'], ['Blueberry', 'A deep, sweet evening'], ['Peach', 'A soft end to the night']];
  var BG = [[255, 171, 145], [192, 235, 117], [165, 180, 252], [255, 200, 221]];
  var CAN = ['#E64A19', '#5C940D', '#4C3BCF', '#D6336C'];
  var els = FLAV.map(function (f) {
    var s = document.createElement('section');
    s.className = 'u329-sec';
    s.innerHTML = '<b></b><span></span>';
    s.querySelector('b').textContent = f[0];
    s.querySelector('span').textContent = f[1];
    secs.appendChild(s);
    dots.appendChild(document.createElement('i'));
    return s;
  });
  var raf = 0, shown = -1;
  function draw() {
    raf = 0;
    var max = sc.scrollHeight - sc.clientHeight, f = max ? sc.scrollTop / max * (FLAV.length - 1) : 0;
    var i = Math.min(FLAV.length - 2, Math.floor(f)), t = f - i;
    var c = BG[i].map(function (v, k) { return Math.round(v + (BG[i + 1][k] - v) * t); });
    root.style.setProperty('--bg', 'rgb(' + c.join(',') + ')');
    var cur = Math.round(f);
    root.style.setProperty('--r', ((f - cur) * 24).toFixed(1) + 'deg');
    root.style.setProperty('--lx', ((f - cur) * -60).toFixed(1) + 'px');
    if (cur !== shown) {
      shown = cur;
      root.style.setProperty('--can', CAN[cur]);
      lab.textContent = FLAV[cur][0];
      Array.prototype.forEach.call(dots.children, function (d, k) { d.classList.toggle('on', k === cur); });
    }
  }
  sc.addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(draw); }, { passive: true });
  draw();
})();
</script>
--- Code end ---
