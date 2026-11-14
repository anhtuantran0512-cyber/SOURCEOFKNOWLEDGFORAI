---
source: "lucianlabs"
id: "335"
title: "Enter-side overlay tiles"
category: "Cursor & Hover"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#335"
tags: ["direction-aware", "hover", "grid", "overlay", "portfolio"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Enter-side overlay tiles (335, Cursor & Hover)
[What it does] When the cursor enters any of nine project tiles, a caption panel slides in from the edge the cursor crossed and covers the tile. Enter from the top and it drops from the top, from the left and it sweeps from the left, and on leaving it pulls away toward the side the cursor exited. The panel seems to travel from tile to tile with the cursor.
[How to use it] Cross the cursor over the tiles from different directions

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
<!-- Lucian UX/UI Prompt #335 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#335 -->
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
.u335{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:#F1EEE8;box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);padding:18px}
.u335-gd{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);gap:8px;width:100%;height:100%}
.u335-t{position:relative;overflow:hidden;border-radius:12px;padding:0;border:0;cursor:pointer;font:inherit;color:#fff}
.u335-t>i{position:absolute;inset:0}
.u335-ov{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:flex-end;gap:2px;padding:10px;background:rgba(20,18,30,.82);text-align:left;transform:translate(0,-101%)}
.u335-ov.is-anim{transition:transform .32s cubic-bezier(.3,.8,.3,1)}
.u335-ov b{font-size:12px;font-weight:800;line-height:1.2;word-break:keep-all}
.u335-ov span{font-size:9.5px;font-weight:650;opacity:.7}
.u335-ov em{font-style:normal;font-size:10px;font-weight:800;margin-top:4px;color:#FFD8A8}
.u335-t:focus-visible{outline:2px solid #1E1B2E;outline-offset:2px}
@media (prefers-reduced-motion: reduce){.u335-ov.is-anim{transition:opacity .2s}}
</style>
<div class="ux u335"><div class="u335-gd" role="group" aria-label="Nine project tiles"></div></div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var gd = root.querySelector('.u335-gd');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var TT = [['House of Wind', 'Architecture'], ['Salt Studio', 'Branding'], ['Night Library', 'App'], ['Blue Garden', 'Exhibition'], ['Paper Workshop', 'Packaging'], ['Slow Post', 'Web'], ['Sea Cinema', 'Film'], ['Little Bakery', 'Branding'], ['Forest Sounds', 'Music']];
  var ART = ['linear-gradient(160deg,#ADB5BD,#343A40)', 'linear-gradient(#F8F9FA 0 40%,#CED4DA 40%)', 'radial-gradient(circle at 60% 30%,#FFE066 0 12%,#1B1F3B 13%)', 'linear-gradient(#A5D8FF 0 45%,#2F9E44 45%)', 'linear-gradient(135deg,#F8F0E3 0 50%,#D9B482 50%)', 'linear-gradient(#FFA8A8 0 55%,#C92A2A 55%)', 'linear-gradient(#1864AB 0 60%,#FCC419 60% 63%,#0B3D91 63%)', 'linear-gradient(150deg,#FFE8CC,#E8590C)', 'linear-gradient(160deg,#B2F2BB,#087F5B)'];
  var OUT = ['translate(0,-101%)', 'translate(101%,0)', 'translate(0,101%)', 'translate(-101%,0)'];
  var T = TT.map(function (w, i) {
    var b = document.createElement('button'); b.type = 'button'; b.className = 'u335-t'; b.setAttribute('aria-label', w[0] + ', ' + w[1]);
    b.innerHTML = '<i style="background:' + ART[i] + '"></i><span class="u335-ov" aria-hidden="true"><span>' + w[1] + '</span><b>' + w[0] + '</b><em>' + 'View →' + '</em></span>';
    gd.appendChild(b);
    var o = { el: b, ov: b.querySelector('.u335-ov') };
    b.addEventListener('focus', function () { show(o, 0); });
    b.addEventListener('blur', function () { hide(o, 2); });
    return o;
  });
  function side(o, x, y) {
    var r = o.el.getBoundingClientRect(), dx = (x - r.left - r.width / 2) / r.width, dy = (y - r.top - r.height / 2) / r.height;
    return Math.abs(dx) > Math.abs(dy) ? (dx > 0 ? 1 : 3) : (dy > 0 ? 2 : 0);
  }
  function show(o, s) {
    o.ov.classList.remove('is-anim'); o.ov.style.transform = rm ? 'none' : OUT[s]; o.ov.style.opacity = rm ? '0' : '';
    void o.ov.offsetWidth;
    o.ov.classList.add('is-anim'); o.ov.style.transform = 'none'; o.ov.style.opacity = '';
  }
  function hide(o, s) { o.ov.classList.add('is-anim'); if (rm) o.ov.style.opacity = '0'; else o.ov.style.transform = OUT[s]; }
  var cur = null;
  function at(e) { var el = document.elementFromPoint(e.clientX, e.clientY), t = el && el.closest && el.closest('.u335-t'); for (var i = 0; i < T.length; i++) if (T[i].el === t) return T[i]; return null; }
  function move(e) {
    var o = at(e);
    if (o === cur) return;
    if (cur) hide(cur, side(cur, e.clientX, e.clientY));
    if (o) show(o, side(o, e.clientX, e.clientY));
    cur = o;
  }
  root.addEventListener('pointermove', move);
  root.addEventListener('pointerleave', function (e) { if (cur) { hide(cur, side(cur, e.clientX, e.clientY)); cur = null; } });
})();
</script>
--- Code end ---
