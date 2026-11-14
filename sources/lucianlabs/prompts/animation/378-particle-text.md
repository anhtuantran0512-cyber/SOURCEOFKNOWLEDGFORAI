---
source: "lucianlabs"
id: "378"
title: "Particles that form words"
category: "Hero & Backgrounds"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#378"
tags: ["particles", "text", "spring", "canvas", "morph"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Particles that form words (378, Hero & Backgrounds)
[What it does] Hundreds of specks of light lie scattered, then spring in to assemble into the shape of a word. Bring the cursor close and the specks are pushed aside, opening a hole that closes again as you move away; press and they all fly to the positions of the next word to spell it out.
[How to use it] Move the cursor over the letters to scatter them, and press to change the word

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
<!-- Lucian UX/UI Prompt #378 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#378 -->
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
.u378{position:relative;width:340px;height:320px;border-radius:30px;overflow:hidden;background:radial-gradient(90% 70% at 50% 45%,#22144A,#0A0716 70%);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong)}
.u378-cv{position:absolute;inset:0;width:100%;height:100%;touch-action:none;cursor:pointer}
</style>
<div class="ux u378"><canvas class="u378-cv" role="img" aria-label="Particle letters, press to change the word"></canvas></div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var cv = root.querySelector('.u378-cv'), cx = cv.getContext('2d');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var W = 340, H = 320, dpr = Math.min(2, window.devicePixelRatio || 1), N = 720;
  cv.width = W * dpr; cv.height = H * dpr; cx.scale(dpr, dpr);
  var WORDS = ['HELLO', 'NICE', 'LUCIAN'], wi = 0, ptr = null;
  function targets(word) {
    var o = document.createElement('canvas'); o.width = W; o.height = H;
    var c = o.getContext('2d'), size = Math.min(150, Math.floor(560 / Math.max(2, word.length)));
    c.fillStyle = '#fff'; c.font = '900 ' + size + 'px system-ui,-apple-system,"Apple SD Gothic Neo","Malgun Gothic",sans-serif'; c.textAlign = 'center'; c.textBaseline = 'middle';
    c.fillText(word, W / 2, H / 2 + 4);
    var d = c.getImageData(0, 0, W, H).data, pts = [];
    for (var y = 0; y < H; y += 4) for (var x = 0; x < W; x += 4) if (d[(y * W + x) * 4 + 3] > 128) pts.push([x, y]);
    for (var k = pts.length - 1; k > 0; k--) { var j = (Math.random() * (k + 1)) | 0, t = pts[k]; pts[k] = pts[j]; pts[j] = t; }
    return pts;
  }
  var P = [];
  for (var i = 0; i < N; i++) P.push({ x: Math.random() * W, y: Math.random() * H, vx: 0, vy: 0, tx: W / 2, ty: H / 2, h: 250 + Math.random() * 80, on: true });
  function assign() {
    var pts = targets(WORDS[wi]);
    P.forEach(function (p, i) {
      if (i < pts.length) { p.tx = pts[i][0] + (Math.random() - 0.5) * 1.5; p.ty = pts[i][1] + (Math.random() - 0.5) * 1.5; p.on = true; }
      else { var a = Math.random() * 6.28, r = 150 + Math.random() * 60; p.tx = W / 2 + Math.cos(a) * r; p.ty = H / 2 + Math.sin(a) * r; p.on = false; }
    });
  }
  function draw() {
    cx.clearRect(0, 0, W, H);
    cx.globalCompositeOperation = 'lighter';
    P.forEach(function (p) {
      var sp = Math.min(1, Math.hypot(p.vx, p.vy) / 300);
      cx.fillStyle = 'hsla(' + (p.h - sp * 60).toFixed(0) + ',90%,' + (68 + sp * 20).toFixed(0) + '%,' + (p.on ? 0.9 : 0.18) + ')';
      cx.fillRect(p.x - 1.3, p.y - 1.3, 2.6, 2.6);
    });
    cx.globalCompositeOperation = 'source-over';
  }
  var vis = true, raf = 0, last = 0;
  function frame(now) {
    raf = 0;
    if (!root.isConnected || !vis) return;
    var dt = Math.min(0.033, Math.max(0, (now - last) / 1000)); last = now;
    P.forEach(function (p) {
      var ax = (p.tx - p.x) * 38 - p.vx * 7.5, ay = (p.ty - p.y) * 38 - p.vy * 7.5;
      if (ptr) { var dx = p.x - ptr.x, dy = p.y - ptr.y, d2 = dx * dx + dy * dy; if (d2 < 3600) { var f = (1 - d2 / 3600) * 9000 / (Math.sqrt(d2) + 6); ax += dx * f / 40; ay += dy * f / 40; } }
      p.vx += ax * dt; p.vy += ay * dt; p.x += p.vx * dt; p.y += p.vy * dt;
    });
    draw();
    raf = requestAnimationFrame(frame);
  }
  function run() { if (rm) { P.forEach(function (p) { p.x = p.tx; p.y = p.ty; }); draw(); return; } if (!raf && vis) { last = performance.now(); raf = requestAnimationFrame(frame); } }
  if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { vis = es[0].isIntersecting; run(); }).observe(root);
  function loc(e) { var r = cv.getBoundingClientRect(), k = cv.offsetWidth / (r.width || 1); return { x: (e.clientX - r.left) * k, y: (e.clientY - r.top) * k }; }
  cv.addEventListener('pointermove', function (e) { ptr = loc(e); });
  cv.addEventListener('pointerleave', function () { ptr = null; });
  cv.addEventListener('click', function () {
    wi = (wi + 1) % WORDS.length; assign();
    P.forEach(function (p) { p.vx += (Math.random() - 0.5) * 260; p.vy += (Math.random() - 0.5) * 260; });
    run();
  });
  assign(); run();
})();
</script>
--- Code end ---
