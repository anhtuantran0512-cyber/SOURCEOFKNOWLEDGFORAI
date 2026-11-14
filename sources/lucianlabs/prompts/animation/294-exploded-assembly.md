---
source: "lucianlabs"
id: "294"
title: "Device that assembles on scroll"
category: "Scroll Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#294"
tags: ["scroll", "exploded", "product", "isometric", "3d"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Device that assembles on scroll (294, Scroll Motion)
[What it does] At first the phone’s glass, display, logic board, battery and back float apart in layers at an angle, each linked to a label by a line. Scroll down and the layers come down one at a time and lock together while the labels fold away, and once it is assembled the screen switches on.
[How to use it] Scroll down inside the card to assemble it, and back up to take it apart

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
<!-- Lucian UX/UI Prompt #294 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#294 -->
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
.u294{position:relative;width:300px;height:500px;border-radius:30px;background:radial-gradient(90% 60% at 50% 40%,var(--ux-surface),var(--ux-surface-2));box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u294-sc{position:absolute;inset:0;overflow-y:auto;scrollbar-width:none;outline:none}
.u294-sc::-webkit-scrollbar{display:none}
.u294-run{height:1200px}
.u294-st{position:sticky;top:0;height:500px}
.u294-k{position:absolute;left:20px;top:20px;margin:0;font-size:20px;font-weight:880;letter-spacing:-.03em}
.u294-ok{position:absolute;left:0;right:0;bottom:24px;text-align:center;font-size:13px;font-weight:800;color:var(--ux-mint);opacity:var(--done,0)}
.u294-iso{position:absolute;left:50%;top:56%;width:0;height:0;transform:rotateX(58deg) rotateZ(-38deg);transform-style:preserve-3d}
.u294-L{position:absolute;left:-60px;top:-110px;width:120px;height:220px;border-radius:22px;transform:translateZ(var(--z));transition:none}
.u294-L.g{background:linear-gradient(135deg,rgba(255,255,255,.75),rgba(200,220,255,.35));box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.9),0 0 0 1px var(--ux-line-2)}
.u294-L.d{background:linear-gradient(135deg,#1B1E3A,#0B0C12);box-shadow:0 0 0 1px rgba(0,0,0,.3)}
.u294-L.d::after{content:"";position:absolute;inset:8px;border-radius:16px;background:radial-gradient(70% 50% at 30% 30%,#7048E8,transparent 70%),radial-gradient(60% 50% at 80% 80%,#15AABF,transparent 70%),#151626;opacity:var(--on,0);transition:opacity .5s}
.u294-L.b{background:#1E7A4F;box-shadow:inset 0 0 0 1px rgba(255,255,255,.2)}
.u294-L.b::before{content:"";position:absolute;left:20px;top:24px;width:46px;height:46px;border-radius:6px;background:#2B2D33;box-shadow:54px 10px 0 -10px #C0A060,0 80px 0 -14px #2B2D33,40px 120px 0 -16px #C0A060}
.u294-L.y{background:linear-gradient(135deg,#ADB5BD,#868E96);border-radius:16px;left:-48px;top:-80px;width:96px;height:160px}
.u294-L.y::after{content:"";position:absolute;inset:16px;border:2px dashed rgba(255,255,255,.4);border-radius:10px}
.u294-L.k{background:linear-gradient(135deg,#E9ECEF,#CED4DA);box-shadow:inset 0 0 0 1.5px rgba(0,0,0,.08),0 20px 30px rgba(0,0,0,.15)}
.u294-lb{position:absolute;left:186px;display:flex;align-items:center;gap:6px;font-size:12px;font-weight:800;color:var(--ux-ink-2);white-space:nowrap;transform:translateY(-50%);transform-origin:0 50%}
.u294-lb::before{content:"";width:28px;height:1.5px;background:var(--ux-line-2)}
</style>
<div class="ux u294">
  <div class="u294-sc" tabindex="0" aria-label="Exploded view, scroll to assemble">
    <div class="u294-run"><div class="u294-st">
      <p class="u294-k">Look inside</p>
      <div class="u294-iso" aria-hidden="true"><span class="u294-L k"></span><span class="u294-L y"></span><span class="u294-L b"></span><span class="u294-L d"></span><span class="u294-L g"></span></div>
      <div class="u294-lbs" aria-hidden="true"></div>
      <p class="u294-ok">Assembled</p>
    </div></div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u294-sc'), st = root.querySelector('.u294-st'), lbs = root.querySelector('.u294-lbs');
  var layers = Array.prototype.slice.call(root.querySelectorAll('.u294-L')).reverse();
  var PARTS = ['Cover glass', 'Display', 'Logic board', 'Battery', 'Back panel'];
  var SPREAD = [200, 140, 80, 30, 0], TIGHT = [14, 11, 7, 4, 0];
  var labels = PARTS.map(function (p) { var l = document.createElement('span'); l.className = 'u294-lb'; l.textContent = p; lbs.appendChild(l); return l; });
  st.querySelector('.u294-iso').setAttribute('aria-label', PARTS.join(', '));
  var raf = 0;
  function draw() {
    raf = 0;
    var max = sc.scrollHeight - sc.clientHeight, p = max ? Math.min(1, sc.scrollTop / max) : 0;
    layers.forEach(function (L, i) {
      var start = (layers.length - 1 - i) * 0.14, k = Math.max(0, Math.min(1, (p - start) / 0.4)), e = k * k * (3 - 2 * k);
      var z = SPREAD[i] + (TIGHT[i] - SPREAD[i]) * e;
      L.style.setProperty('--z', z.toFixed(1) + 'px');
      var lb = labels[i];
      lb.style.top = (280 - z * 0.72 - (4 - i) * 6).toFixed(1) + 'px';
      lb.style.opacity = (1 - e * 1.3).toFixed(2);
      lb.style.transform = 'translateY(-50%) scaleX(' + (1 - e * 0.6).toFixed(2) + ')';
    });
    var done = p > 0.92 ? 1 : 0;
    st.style.setProperty('--done', done);
    layers[1].style.setProperty('--on', done);
  }
  sc.addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(draw); }, { passive: true });
  draw();
})();
</script>
--- Code end ---
