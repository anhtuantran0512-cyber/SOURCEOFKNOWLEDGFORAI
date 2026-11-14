---
source: "lucianlabs"
id: "394"
title: "Scroll-driven marquee rows"
category: "Scroll Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#394"
tags: ["scroll", "marquee", "velocity", "typography", "banner"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Scroll-driven marquee rows (394, Scroll Motion)
[What it does] Three rows of big text drift slowly in opposite directions, then speed up with your scroll and lean slightly toward the motion. Scroll up and the direction flips; stop and they ease back to a lazy drift.
[How to use it] Scroll quickly up and down inside the card

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
<!-- Lucian UX/UI Prompt #394 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#394 -->
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
.u394{position:relative;width:340px;height:330px;border-radius:28px;background:var(--ux-ink);box-shadow:0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden;color:var(--ux-page)}
.u394-sc{position:absolute;inset:0;overflow-y:auto;scrollbar-width:none;outline:none}
.u394-sc::-webkit-scrollbar{display:none}
.u394-run{height:2400px}
.u394-st{position:sticky;top:0;height:330px;display:flex;flex-direction:column;justify-content:center;gap:8px;overflow:hidden}
.u394-row{display:flex;white-space:nowrap;will-change:transform}
.u394-row span{flex:none;padding-right:.3em;font-size:52px;line-height:1.05;font-weight:900;letter-spacing:-.04em}
.u394-row:nth-child(2) span{font-size:30px;font-weight:800;color:var(--ux-accent);letter-spacing:-.03em}
.u394-row:nth-child(3) span{color:transparent;-webkit-text-stroke:1.5px color-mix(in srgb,var(--ux-page) 70%,transparent)}
.u394-hint{position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:11.5px;font-weight:750;color:color-mix(in srgb,var(--ux-page) 50%,transparent)}
</style>
<div class="ux u394">
  <div class="u394-sc" tabindex="0" aria-label="Moving text rows, scroll to change their speed"><div class="u394-run"><div class="u394-st" aria-hidden="true"></div></div></div>
  <span class="u394-hint" aria-hidden="true">Scroll to change the speed</span>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u394-sc'), st = root.querySelector('.u394-st');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ROWS = ['DESIGN · MOTION · CODE · ', 'Interfaces that speak in motion · ', 'LUCIAN LABS · 2026 · '];
  var rows = ROWS.map(function (t, i) {
    var r = document.createElement('div');
    r.className = 'u394-row';
    for (var k = 0; k < 4; k++) { var s = document.createElement('span'); s.textContent = t; r.appendChild(s); }
    st.appendChild(r);
    return { el: r, x: -Math.random() * 200, dir: i % 2 ? 1 : -1, w: 0 };
  });
  st.setAttribute('aria-label', ROWS.join(' '));
  var lastY = 0, boost = 0, sign = 1, last = 0, vis = true, skew = 0;
  sc.addEventListener('scroll', function () {
    var dy = sc.scrollTop - lastY;
    lastY = sc.scrollTop;
    boost = Math.min(40, boost + Math.abs(dy) * 0.25);
    if (dy) sign = dy > 0 ? 1 : -1;
  }, { passive: true });
  function frame(now) {
    if (!root.isConnected) return;
    var dt = Math.max(0, Math.min(50, now - (last || now))) / 16.7;
    last = now;
    boost *= Math.pow(0.92, dt);
    skew += ((boost > 1 ? sign * Math.min(8, boost * 0.35) : 0) - skew) * 0.15 * dt;
    rows.forEach(function (r) {
      if (!r.w) r.w = r.el.firstChild.offsetWidth;
      r.x += r.dir * sign * (0.5 + boost) * dt;
      if (r.x < -r.w) r.x += r.w;
      if (r.x > 0) r.x -= r.w;
      r.el.style.transform = 'translateX(' + r.x.toFixed(1) + 'px) skewX(' + (-skew * r.dir).toFixed(2) + 'deg)';
    });
    if (vis && !rm) requestAnimationFrame(frame);
  }
  new IntersectionObserver(function (en) { var was = vis; vis = en[0].isIntersecting; if (vis && !was) requestAnimationFrame(frame); }).observe(root);
  requestAnimationFrame(frame);
})();
</script>
--- Code end ---
