---
source: "lucianlabs"
id: "371"
title: "Rising contour map"
category: "Hero & Backgrounds"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#371"
tags: ["contour", "topography", "marching-squares", "canvas", "map"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Rising contour map (371, Hero & Backgrounds)
[What it does] A map that draws slowly breathing terrain as contour lines. Hover and a hill rises under the cursor as the lines wrap around it in rings; press to raise a peak there, labeled with its height. Every fifth line is drawn bolder, and higher lines turn warmer.
[How to use it] Move the cursor over the map, and press to raise a peak

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
<!-- Lucian UX/UI Prompt #371 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#371 -->
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
.u371{position:relative;width:340px;height:330px;border-radius:30px;overflow:hidden;background:#F4EFE3;box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong)}
.u371-cv{position:absolute;inset:0;width:100%;height:100%;touch-action:none;cursor:crosshair}
.u371-pk{position:absolute;left:0;top:0;transform:translate(-50%,-130%);padding:2px 6px;border-radius:6px;background:#3B2F2A;color:#FFF4E0;font:700 10px/1.3 ui-monospace,SFMono-Regular,Menlo,monospace;pointer-events:none;animation:u371-in .4s var(--ux-spring)}
.u371-pk::after{content:"▲";position:absolute;left:50%;top:100%;transform:translateX(-50%);font-size:8px;color:#3B2F2A}
@keyframes u371-in{from{opacity:0;transform:translate(-50%,-90%)}}
</style>
<div class="ux u371"><canvas class="u371-cv" role="img" aria-label="Contour map, press to raise a peak"></canvas></div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var cv = root.querySelector('.u371-cv'), cx = cv.getContext('2d');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var W = 340, H = 330, dpr = Math.min(2, window.devicePixelRatio || 1), GX = 58, GY = 56, sx = W / (GX - 1), sy = H / (GY - 1);
  cv.width = W * dpr; cv.height = H * dpr; cx.scale(dpr, dpr);
  var hgt = new Float32Array(GX * GY), peaks = [], hover = null, hoverK = 0, t = 0, LV = 14;
  function field() {
    for (var j = 0; j < GY; j++) for (var i = 0; i < GX; i++) {
      var x = i * sx, y = j * sy;
      var v = 0.42 + 0.16 * Math.sin(x * 0.018 + t * 0.25) * Math.cos(y * 0.021 - t * 0.2) + 0.1 * Math.sin((x + y) * 0.012 + t * 0.15) + 0.07 * Math.cos(x * 0.04 - y * 0.03 + t * 0.3);
      if (hover && hoverK > 0.01) { var dh = ((x - hover.x) * (x - hover.x) + (y - hover.y) * (y - hover.y)) / 2600; v += 0.32 * hoverK * Math.exp(-dh); }
      peaks.forEach(function (p) { var d = ((x - p.x) * (x - p.x) + (y - p.y) * (y - p.y)) / (2200 * p.s); v += 0.42 * p.k * Math.exp(-d); });
      hgt[j * GX + i] = v;
    }
  }
  function contours() {
    cx.clearRect(0, 0, W, H);
    for (var l = 1; l < LV; l++) {
      var lev = l / LV * 1.2, bold = l % 5 === 0, warm = l / LV;
      cx.strokeStyle = 'hsl(' + (200 - warm * 180).toFixed(0) + ' ' + (35 + warm * 30).toFixed(0) + '% ' + (bold ? 34 : 46) + '%)';
      cx.lineWidth = bold ? 1.8 : 0.9; cx.globalAlpha = bold ? 0.95 : 0.7;
      cx.beginPath();
      for (var j = 0; j < GY - 1; j++) for (var i = 0; i < GX - 1; i++) {
        var a = hgt[j * GX + i], b = hgt[j * GX + i + 1], c = hgt[(j + 1) * GX + i + 1], d = hgt[(j + 1) * GX + i];
        var code = (a > lev ? 8 : 0) | (b > lev ? 4 : 0) | (c > lev ? 2 : 0) | (d > lev ? 1 : 0);
        if (code === 0 || code === 15) continue;
        var x = i * sx, y = j * sy;
        var top = [x + sx * (lev - a) / (b - a), y], rt = [x + sx, y + sy * (lev - b) / (c - b)], bt = [x + sx * (lev - d) / (c - d), y + sy], lf = [x, y + sy * (lev - a) / (d - a)];
        var segs = { 1: [lf, bt], 2: [bt, rt], 3: [lf, rt], 4: [top, rt], 5: [lf, top, bt, rt], 6: [top, bt], 7: [lf, top], 8: [lf, top], 9: [top, bt], 10: [lf, bt, top, rt], 11: [top, rt], 12: [lf, rt], 13: [bt, rt], 14: [lf, bt] }[code];
        for (var s = 0; s < segs.length; s += 2) { cx.moveTo(segs[s][0], segs[s][1]); cx.lineTo(segs[s + 1][0], segs[s + 1][1]); }
      }
      cx.stroke();
    }
    cx.globalAlpha = 1;
  }
  var vis = true, raf = 0, last = 0, acc = 0;
  function frame(now) {
    raf = 0;
    if (!root.isConnected || !vis) return;
    var dt = Math.min(0.05, Math.max(0, (now - last) / 1000)); last = now; t += dt; acc += dt;
    hoverK += ((hover ? 1 : 0) - hoverK) * Math.min(1, dt * 3);
    peaks.forEach(function (p) { p.k += (1 - p.k) * Math.min(1, dt * 2.5); });
    if (acc > 0.033) { acc = 0; field(); contours(); }
    raf = requestAnimationFrame(frame);
  }
  function run() { if (rm) { hoverK = hover ? 1 : 0; peaks.forEach(function (p) { p.k = 1; }); field(); contours(); return; } if (!raf && vis) { last = performance.now(); raf = requestAnimationFrame(frame); } }
  if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { vis = es[0].isIntersecting; run(); }).observe(root);
  function loc(e) { var r = cv.getBoundingClientRect(), k = cv.offsetWidth / (r.width || 1); return { x: (e.clientX - r.left) * k, y: (e.clientY - r.top) * k }; }
  cv.addEventListener('pointermove', function (e) { hover = loc(e); if (rm) run(); });
  cv.addEventListener('pointerleave', function () { hover = null; if (rm) run(); });
  cv.addEventListener('pointerdown', function (e) {
    var q = loc(e);
    if (peaks.length >= 3) { var old = peaks.shift(); if (old.tag) old.tag.remove(); }
    var p = { x: q.x, y: q.y, k: 0, s: 0.8 + Math.random() * 0.6 };
    p.tag = document.createElement('span'); p.tag.className = 'u371-pk'; p.tag.style.left = q.x + 'px'; p.tag.style.top = q.y + 'px';
    p.tag.textContent = (680 + Math.round(Math.random() * 900)) + 'm';
    root.appendChild(p.tag); peaks.push(p);
    if (rm) run();
  });
  field(); contours(); run();
})();
</script>
--- Code end ---
