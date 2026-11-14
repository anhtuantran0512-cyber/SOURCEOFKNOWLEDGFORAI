---
source: "lucianlabs"
id: "276"
title: "Photo-following work list"
category: "Cursor & Hover"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#276"
tags: ["hover-preview", "list", "editorial", "cursor", "follow"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Photo-following work list (276, Cursor & Hover)
[What it does] In a list of project names set in large type, hover over a row and that project's photo floats up beside the cursor, following a beat behind and tilting toward your motion. Move to another row and the photo strip slides up or down to the next image, while the chosen row shifts right to reveal an arrow. Focusing a row with the keyboard also floats its photo at the row's end.
[How to use it] Move the cursor slowly up and down over the list

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
<!-- Lucian UX/UI Prompt #276 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#276 -->
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
.u276{position:relative;width:300px;height:480px;border-radius:32px;overflow:hidden;background:#111;box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:#F2EFEA;padding:22px 18px}
.u276-hd{display:flex;justify-content:space-between;font-size:10.5px;font-weight:750;letter-spacing:.12em;color:#8D8880;margin-bottom:10px;text-transform:uppercase}
.u276-ls{list-style:none;margin:0;padding:0;border-top:1px solid #2A2826}
.u276-it{border-bottom:1px solid #2A2826}
.u276-a{display:flex;align-items:baseline;gap:8px;width:100%;padding:16px 2px 15px;border:0;background:none;color:inherit;font:inherit;text-align:left;cursor:pointer;transition:transform .35s cubic-bezier(.3,1.3,.5,1),color .25s}
.u276-a b{font-size:22px;font-weight:800;letter-spacing:-.03em;flex:1;white-space:nowrap}
.u276-a span{font-size:10.5px;font-weight:650;color:#8D8880}
.u276-a i{font-style:normal;font-size:16px;opacity:0;transform:translateX(-8px);transition:opacity .25s,transform .3s}
.u276-ls.is-hov .u276-a{color:#5C5852}
.u276-ls.is-hov .u276-a.is-on{color:#F2EFEA;transform:translateX(10px)}
.u276-a.is-on i{opacity:1;transform:none}
.u276-a:focus-visible{outline:2px solid #F2EFEA;outline-offset:2px}
.u276-pv{position:absolute;left:0;top:0;width:120px;height:150px;border-radius:6px;overflow:hidden;pointer-events:none;opacity:0;transform:scale(.6);transition:opacity .25s,transform .35s cubic-bezier(.3,1.4,.5,1);z-index:3;box-shadow:0 20px 40px -16px rgba(0,0,0,.8)}
.u276-pv.is-on{opacity:1;transform:scale(1)}
.u276-st{position:absolute;left:0;top:0;width:100%;transition:transform .5s cubic-bezier(.6,0,.2,1)}
.u276-st i{display:block;width:120px;height:150px}
@media (prefers-reduced-motion: reduce){.u276-st{transition:none}}
</style>
<div class="ux u276">
  <div class="u276-hd" aria-hidden="true"><span>Selected work</span><span>2023—26</span></div>
  <ul class="u276-ls" aria-label="Work list"></ul>
  <div class="u276-pv" aria-hidden="true"><div class="u276-st"></div></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var ls = root.querySelector('.u276-ls'), pv = root.querySelector('.u276-pv'), st = root.querySelector('.u276-st');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var WK = [['House of Wind', 'Architecture', '2026'], ['Salt Studio', 'Branding', '2025'], ['Night Library', 'App', '2025'], ['Blue Garden', 'Exhibition', '2024'], ['Paper Workshop', 'Packaging', '2024'], ['Slow Post Office', 'Web', '2023']];
  var ART = ['linear-gradient(160deg,#DEE2E6,#868E96 60%,#343A40)', 'linear-gradient(#FFF 0 30%,#E9ECEF 30% 70%,#CED4DA 70%)', 'radial-gradient(circle at 50% 30%,#FFE066 0 14%,#1B1F3B 15%)', 'linear-gradient(#A5D8FF 0 40%,#2F9E44 40%)', 'linear-gradient(135deg,#F8F0E3 0 50%,#D9B482 50%)', 'linear-gradient(#FFA8A8 0 50%,#C92A2A 50%)'];
  ART.forEach(function (a) { var i = document.createElement('i'); i.style.background = a; st.appendChild(i); });
  var cur = -1, pos = { x: 0, y: 0 }, sp = { x: 0, y: 0 }, vx = 0, raf = 0, last = 0, anchored = false;
  var B = WK.map(function (w, i) {
    var li = document.createElement('li'); li.className = 'u276-it';
    var b = document.createElement('button'); b.type = 'button'; b.className = 'u276-a';
    b.innerHTML = '<b>' + w[0] + '</b><span>' + w[1] + ' · ' + w[2] + '</span><i aria-hidden="true">→</i>';
    li.appendChild(b); ls.appendChild(li);
    b.addEventListener('pointerenter', function () { pick(i); });
    b.addEventListener('focus', function () { anchored = true; pick(i); var r = b.getBoundingClientRect(), rr = root.getBoundingClientRect(), k = root.offsetWidth / (rr.width || 1); pos.x = 200; pos.y = (r.top - rr.top) * k + r.height * k / 2; if (!pv.classList.contains('is-on')) { sp.x = pos.x; sp.y = pos.y; } kick(); });
    b.addEventListener('blur', function () { if (anchored) { anchored = false; pick(-1); } });
    return b;
  });
  function pick(i) {
    if (i === cur) return;
    cur = i;
    B.forEach(function (b, j) { b.classList.toggle('is-on', j === i); });
    ls.classList.toggle('is-hov', i >= 0);
    pv.classList.toggle('is-on', i >= 0);
    if (i >= 0) st.style.transform = 'translateY(' + (-i * 150) + 'px)';
  }
  function frame(now) {
    raf = 0;
    if (!root.isConnected) return;
    var dt = Math.min(0.033, Math.max(0, (now - last) / 1000)); last = now;
    var tx = pos.x + 18, ty = pos.y - 75, k = rm ? 1 : Math.min(1, dt * 9);
    var nx = sp.x + (tx - sp.x) * k; vx = (nx - sp.x) / Math.max(dt, 0.001); sp.x = nx; sp.y += (ty - sp.y) * k;
    var tilt = Math.max(-12, Math.min(12, vx * 0.02));
    pv.style.left = sp.x.toFixed(1) + 'px'; pv.style.top = sp.y.toFixed(1) + 'px'; pv.style.rotate = (rm ? 0 : tilt).toFixed(2) + 'deg';
    if (Math.abs(tx - sp.x) + Math.abs(ty - sp.y) > 0.5 || Math.abs(tilt) > 0.2) raf = requestAnimationFrame(frame);
  }
  function kick() { if (!raf) { last = performance.now(); raf = requestAnimationFrame(frame); } }
  root.addEventListener('pointermove', function (e) {
    var r = root.getBoundingClientRect(), k = root.offsetWidth / (r.width || 1);
    pos.x = Math.min(170, (e.clientX - r.left) * k); pos.y = (e.clientY - r.top) * k; anchored = false;
    var hitEl = document.elementFromPoint(e.clientX, e.clientY), b = hitEl && hitEl.closest && hitEl.closest('.u276-a');
    pick(b ? B.indexOf(b) : -1);
    if (cur >= 0 && !pv.dataset.seen) { pv.dataset.seen = 1; sp.x = pos.x + 18; sp.y = pos.y - 75; }
    kick();
  });
  root.addEventListener('pointerleave', function () { pick(-1); delete pv.dataset.seen; });
})();
</script>
--- Code end ---
