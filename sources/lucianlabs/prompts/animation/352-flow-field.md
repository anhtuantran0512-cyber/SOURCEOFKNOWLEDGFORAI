---
source: "lucianlabs"
id: "352"
title: "Swirling flow field"
category: "Hero & Backgrounds"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#352"
tags: ["flow-field", "generative", "particles", "canvas", "trails"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Swirling flow field (352, Hero & Backgrounds)
[What it does] A generative drawing where countless particles drift along an invisible current, leaving silky trails. The current slowly reshapes over time; hover and a vortex forms around the cursor, wrapping the particles around it. Press to switch the color scheme and start drawing anew.
[How to use it] Hover to create a vortex, and press to change colors

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
<!-- Lucian UX/UI Prompt #352 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#352 -->
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
.u352{position:relative;width:340px;height:330px;border-radius:30px;overflow:hidden;background:#120A1F;box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);transition:background-color .6s}
.u352-cv{position:absolute;inset:0;width:100%;height:100%;touch-action:none;cursor:pointer}
.u352-nm{position:absolute;right:14px;bottom:14px;padding:5px 10px;border-radius:999px;background:rgba(255,255,255,.12);color:rgba(255,255,255,.85);font-size:11.5px;font-weight:750;pointer-events:none;-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
</style>
<div class="ux u352"><canvas class="u352-cv" role="img" aria-label="Flow field, press to change colors"></canvas><span class="u352-nm" aria-live="polite"></span></div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var cv = root.querySelector('.u352-cv'), cx = cv.getContext('2d'), nm = root.querySelector('.u352-nm');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var PAL = [['Dusk', '#120A1F', [16, 36]], ['Deep sea', '#04121C', [175, 215]], ['Forest', '#08140C', [80, 140]]];
  var W = 340, H = 330, dpr = Math.min(2, window.devicePixelRatio || 1), pal = 0, ptr = null, t = 0;
  cv.width = W * dpr; cv.height = H * dpr; cx.scale(dpr, dpr);
  var P = [];
  function spawn(p) { p.x = Math.random() * W; p.y = Math.random() * H; p.life = 60 + Math.random() * 160; p.h = Math.random(); return p; }
  for (var i = 0; i < 900; i++) P.push(spawn({}));
  function angle(x, y) { return (Math.sin(x * 0.011 + t * 0.25) + Math.cos(y * 0.013 - t * 0.19) + Math.sin((x + y) * 0.006 + t * 0.12)) * Math.PI * 0.66; }
  function clear() { cx.fillStyle = PAL[pal][1]; cx.fillRect(0, 0, W, H); root.style.backgroundColor = PAL[pal][1]; nm.textContent = PAL[pal][0]; }
  function step(dt) {
    var bg = PAL[pal][1];
    cx.globalAlpha = 0.07; cx.fillStyle = bg; cx.fillRect(0, 0, W, H); cx.globalAlpha = 1;
    var groups = [[], [], [], [], [], []], hr = PAL[pal][2];
    P.forEach(function (p) {
      var a = angle(p.x, p.y), vx = Math.cos(a) * 46, vy = Math.sin(a) * 46;
      if (ptr) {
        var dx = p.x - ptr.x, dy = p.y - ptr.y, d = Math.hypot(dx, dy);
        if (d < 95 && d > 1) { var f = (1 - d / 95) * 160; vx += -dy / d * f - dx / d * f * 0.25; vy += dx / d * f - dy / d * f * 0.25; }
      }
      var nx = p.x + vx * dt, ny = p.y + vy * dt;
      groups[Math.min(5, (p.h * 6) | 0)].push(p.x, p.y, nx, ny);
      p.x = nx; p.y = ny; p.life -= 1;
      if (p.life < 0 || nx < -5 || nx > W + 5 || ny < -5 || ny > H + 5) spawn(p);
    });
    cx.lineWidth = 1.1; cx.lineCap = 'round';
    groups.forEach(function (g, k) {
      var hue = hr[0] + (hr[1] - hr[0]) * k / 5;
      cx.strokeStyle = 'hsla(' + hue.toFixed(0) + ',85%,' + (58 + k * 4) + '%,.55)';
      cx.beginPath();
      for (var j = 0; j < g.length; j += 4) { cx.moveTo(g[j], g[j + 1]); cx.lineTo(g[j + 2], g[j + 3]); }
      cx.stroke();
    });
  }
  var vis = true, raf = 0, last = 0;
  function frame(now) {
    raf = 0;
    if (!root.isConnected || !vis) return;
    var dt = Math.min(0.04, Math.max(0, (now - last) / 1000)); last = now; t += dt;
    step(dt);
    raf = requestAnimationFrame(frame);
  }
  function run() { if (rm) { clear(); for (var k = 0; k < 120; k++) { t += 0.016; step(0.016); } return; } if (!raf && vis) { last = performance.now(); raf = requestAnimationFrame(frame); } }
  if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { vis = es[0].isIntersecting; run(); }).observe(root);
  function loc(e) { var r = cv.getBoundingClientRect(), k = cv.offsetWidth / (r.width || 1); return { x: (e.clientX - r.left) * k, y: (e.clientY - r.top) * k }; }
  cv.addEventListener('pointermove', function (e) { ptr = loc(e); });
  cv.addEventListener('pointerleave', function () { ptr = null; });
  cv.addEventListener('click', function () { pal = (pal + 1) % PAL.length; P.forEach(spawn); clear(); if (rm) run(); });
  clear(); run();
})();
</script>
--- Code end ---
