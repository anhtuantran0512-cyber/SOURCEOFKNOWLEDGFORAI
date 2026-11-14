---
source: "lucianlabs"
id: "319"
title: "Cursor-following aurora background"
category: "Hero & Backgrounds"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#319"
tags: ["gradient", "aurora", "mesh", "canvas", "background"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Cursor-following aurora background (319, Hero & Backgrounds)
[What it does] A gradient background where five pools of light overlap and blend as they drift slowly across a dark sky. Hover and one light trails after your cursor while the others lean toward it, and switching palettes melts the colors over gradually instead of swapping at once. A fine film grain sits on top.
[How to use it] Move the cursor over the background and switch the palette at top right

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
<!-- Lucian UX/UI Prompt #319 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#319 -->
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
.u319{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:#050B1F;box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:#fff}
.u319 canvas{position:absolute;inset:-8%;width:116%;height:116%;filter:blur(18px) saturate(1.15)}
.u319-gr{position:absolute;inset:0;opacity:.16;mix-blend-mode:overlay;pointer-events:none}
.u319-pl{position:absolute;right:14px;top:14px;display:flex;gap:6px;padding:5px;border-radius:999px;background:rgba(255,255,255,.12);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px)}
.u319-p{width:24px;height:24px;border:0;padding:0;border-radius:50%;background:var(--g);box-shadow:0 0 0 2px transparent;transition:box-shadow .25s,transform .3s var(--ux-spring)}
.u319-p[aria-pressed="true"]{box-shadow:0 0 0 2px #fff;transform:scale(1.08)}
.u319-p:focus-visible{outline:2px solid #fff;outline-offset:3px}
.u319-tx{position:absolute;left:22px;bottom:22px;right:22px;pointer-events:none}
.u319-tx small{font-size:11.5px;font-weight:750;letter-spacing:.02em;opacity:.8}
.u319-tx b{display:block;margin-top:8px;font-size:30px;font-weight:880;letter-spacing:-.04em;line-height:1.05;text-shadow:0 2px 24px rgba(0,0,0,.25)}
.u319-tx span{display:block;margin-top:6px;font-size:13px;opacity:.85}
</style>
<div class="ux u319">
  <canvas width="72" height="72" aria-hidden="true"></canvas>
  <div class="u319-gr" aria-hidden="true"></div>
  <div class="u319-pl" role="group" aria-label="Palette"></div>
  <div class="u319-tx"><small>Living background</small><b>Light at dawn</b><span>The light drifts slowly after your cursor</span></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var cv = root.querySelector('canvas'), cx = cv.getContext('2d'), pl = root.querySelector('.u319-pl'), gr = root.querySelector('.u319-gr');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var PAL = [['Aurora', '#050B1F', ['#00F5A0', '#00D9F5', '#7B61FF', '#24FE41', '#2EC5FF']], ['Sunset', '#1A0B1F', ['#FF6B6B', '#FFD93D', '#FF8E3C', '#C44569', '#F8B500']], ['Ocean', '#031926', ['#00A8E8', '#007EA7', '#00F5D4', '#3A86FF', '#80FFDB']]];
  var S = 72;
  function rgb(h) { var n = parseInt(h.slice(1), 16); return [n >> 16 & 255, n >> 8 & 255, n & 255]; }
  var col = PAL[0][2].map(rgb), bg = rgb(PAL[0][1]), tCol = col.map(function (c) { return c.slice(); }), tBg = bg.slice();
  var B = [0, 1, 2, 3, 4].map(function (i) { return { bx: 0.2 + (i * 0.37) % 0.7, by: 0.25 + (i * 0.53) % 0.6, x: 0.5, y: 0.5, r: 0.38 + (i % 3) * 0.08, ph: i * 1.7, sp: 0.18 + i * 0.03 }; });
  var ptr = null, follow = { x: 0.5, y: 0.5 };
  PAL.forEach(function (p, i) {
    var b = document.createElement('button'); b.type = 'button'; b.className = 'u319-p';
    b.style.setProperty('--g', 'linear-gradient(135deg,' + p[2][0] + ',' + p[2][2] + ')');
    b.setAttribute('aria-label', p[0]); b.setAttribute('aria-pressed', String(i === 0));
    b.addEventListener('click', function () {
      Array.prototype.forEach.call(pl.children, function (x, k) { x.setAttribute('aria-pressed', String(k === i)); });
      tCol = p[2].map(rgb); tBg = rgb(p[1]);
      if (rm) { col = tCol.map(function (c) { return c.slice(); }); bg = tBg.slice(); draw(0); }
    });
    pl.appendChild(b);
  });
  (function () {
    var n = document.createElement('canvas'); n.width = n.height = 96; var c = n.getContext('2d'), d = c.createImageData(96, 96);
    for (var i = 0; i < d.data.length; i += 4) { var v = Math.random() * 255; d.data[i] = d.data[i + 1] = d.data[i + 2] = v; d.data[i + 3] = 255; }
    c.putImageData(d, 0, 0); gr.style.backgroundImage = 'url(' + n.toDataURL() + ')';
  })();
  function mix(a, b, k) { return [a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k, a[2] + (b[2] - a[2]) * k]; }
  function draw(t) {
    cx.globalCompositeOperation = 'source-over';
    cx.fillStyle = 'rgb(' + bg.map(Math.round).join(',') + ')'; cx.fillRect(0, 0, S, S);
    cx.globalCompositeOperation = 'lighter';
    B.forEach(function (b, i) {
      var x = b.bx + Math.sin(t * b.sp + b.ph) * 0.18, y = b.by + Math.cos(t * b.sp * 0.8 + b.ph * 1.3) * 0.16;
      if (ptr) { x += (ptr.x - x) * 0.18; y += (ptr.y - y) * 0.18; }
      if (i === 0) { x = follow.x; y = follow.y; }
      var c = col[i], g = cx.createRadialGradient(x * S, y * S, 0, x * S, y * S, b.r * S);
      g.addColorStop(0, 'rgba(' + c.map(Math.round).join(',') + ',.85)');
      g.addColorStop(1, 'rgba(' + c.map(Math.round).join(',') + ',0)');
      cx.fillStyle = g; cx.fillRect(0, 0, S, S);
    });
  }
  var vis = true, raf = 0, last = 0, t = 0;
  function frame(now) {
    raf = 0;
    if (!root.isConnected || !vis) return;
    var dt = Math.min(0.05, Math.max(0, (now - last) / 1000)); last = now; t += dt;
    var k = 1 - Math.pow(0.02, dt);
    col = col.map(function (c, i) { return mix(c, tCol[i], k); }); bg = mix(bg, tBg, k);
    var aim = ptr || { x: 0.3 + Math.sin(t * 0.21) * 0.15, y: 0.35 + Math.cos(t * 0.17) * 0.12 };
    follow.x += (aim.x - follow.x) * (1 - Math.pow(0.15, dt)); follow.y += (aim.y - follow.y) * (1 - Math.pow(0.15, dt));
    draw(t);
    raf = requestAnimationFrame(frame);
  }
  function run() { if (rm) { draw(2); return; } if (!raf && vis) { last = performance.now(); raf = requestAnimationFrame(frame); } }
  if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { vis = es[0].isIntersecting; run(); }).observe(root);
  root.addEventListener('pointermove', function (e) { var r = root.getBoundingClientRect(); ptr = { x: (e.clientX - r.left) / r.width, y: (e.clientY - r.top) / r.height }; if (rm) draw(2); });
  root.addEventListener('pointerleave', function () { ptr = null; });
  run();
})();
</script>
--- Code end ---
