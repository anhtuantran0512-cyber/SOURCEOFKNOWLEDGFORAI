---
source: "lucianlabs"
id: "049"
title: "Layered editorial card"
category: "Cards & Content"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#049"
tags: ["card", "editorial", "parallax", "hover", "reveal"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Layered editorial card (049, Cards & Content)
[What it does] Move the cursor and the sun and hills in the illustration shift at different depths. Hover or focus and the title rises to reveal a summary and a Read button; on touch, a single tap opens it.
[How to use it] Move over the card to feel the depth, and rest on it to reveal the summary. On touch, tap to open. Try the bookmark too

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
<!-- Lucian UX/UI Prompt #049 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#049 -->
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
.u049{--px:0;--py:0;position:relative;width:320px;height:460px;border-radius:30px;overflow:hidden;isolation:isolate;color:#fff;background:#1B1440;box-shadow:0 30px 60px -30px var(--ux-shadow-strong);transition:transform .6s var(--ux-ease),box-shadow .6s var(--ux-ease)}
.u049.is-open{transform:translateY(-4px);box-shadow:0 40px 70px -32px var(--ux-shadow-strong)}
.u049-art{position:absolute;inset:-20px;z-index:-1}
.u049-art svg{position:absolute;inset:0;width:100%;height:100%;transition:transform .9s var(--ux-ease)}
.u049-l1{transform:translate(calc(var(--px) * -6px),calc(var(--py) * -4px)) scale(1.02)}
.u049-l2{transform:translate(calc(var(--px) * -14px),calc(var(--py) * -8px)) scale(1.04)}
.u049-l3{transform:translate(calc(var(--px) * -24px),calc(var(--py) * -12px)) scale(1.06)}
.u049.is-open .u049-l1{transform:translate(calc(var(--px) * -6px),calc(var(--py) * -4px - 10px)) scale(1.06)}
.u049-shade{position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(14,10,36,0) 35%,rgba(14,10,36,.78) 100%);transition:opacity .6s}
.u049-top{position:absolute;left:20px;right:16px;top:18px;display:flex;align-items:center;justify-content:space-between}
.u049-tag{height:28px;padding:0 11px;border-radius:999px;display:inline-flex;align-items:center;background:rgba(255,255,255,.18);font-size:11.5px;font-weight:750;letter-spacing:.04em}
.u049-bm{width:40px;height:40px;border:0;padding:0;border-radius:50%;display:grid;place-items:center;background:rgba(255,255,255,.18);color:#fff;transition:transform .4s var(--ux-spring),background-color .3s}
.u049-bm:hover{background:rgba(255,255,255,.28)}
.u049-bm:active{transform:scale(.86)}
.u049-bm:focus-visible{outline:2px solid #fff;outline-offset:2px}
.u049-bm svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2;stroke-linejoin:round;transition:fill .3s}
.u049-bm[aria-pressed="true"] svg{fill:currentColor;animation:u049-pop .5s var(--ux-spring)}
@keyframes u049-pop{40%{transform:scale(1.3)}}
.u049-body{position:absolute;left:22px;right:22px;bottom:22px;transform:translateY(var(--lift,118px));transition:transform .7s var(--ux-spring)}
.u049.is-open .u049-body{--lift:0px}
.u049-k{font-size:12px;font-weight:700;letter-spacing:.12em;opacity:.75}
.u049-t{margin:8px 0 0;font-size:30px;line-height:1.12;font-weight:800;letter-spacing:-.05em}
.u049-sum{margin:12px 0 0;font-size:13.5px;line-height:1.6;color:rgba(255,255,255,.82);opacity:0;transform:translateY(10px);transition:opacity .3s,transform .5s var(--ux-ease)}
.u049-foot{display:flex;align-items:center;gap:10px;margin-top:16px;opacity:0;transform:translateY(14px);transition:opacity .3s,transform .5s var(--ux-ease)}
.u049.is-open .u049-sum{opacity:1;transform:none;transition:opacity .45s .12s,transform .6s var(--ux-spring) .12s}
.u049.is-open .u049-foot{opacity:1;transform:none;transition:opacity .45s .2s,transform .6s var(--ux-spring) .2s}
.u049-av{width:32px;height:32px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFD3A8,#FF7A93 60%,#8B6CFF);box-shadow:0 0 0 2px rgba(255,255,255,.5)}
.u049-by{font-size:12.5px;font-weight:650;line-height:1.3}
.u049-by small{display:block;font-size:11.5px;opacity:.65}
.u049-cta{margin-left:auto;height:40px;padding:0 16px;border:0;border-radius:999px;display:inline-flex;align-items:center;gap:6px;background:#fff;color:#1B1440;font-size:13.5px;font-weight:750;transition:transform .35s var(--ux-spring)}
.u049-cta:hover{transform:translateX(2px)}
.u049-cta:active{transform:scale(.94)}
.u049-cta:focus-visible{outline:2px solid #fff;outline-offset:3px}
.u049-cta svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.u049:focus-visible{outline:2px solid var(--ux-accent);outline-offset:4px}
</style>
<article class="ux u049" tabindex="0" aria-label="The trust in a short transition — an interaction essay">
  <div class="u049-art" aria-hidden="true">
    <svg class="u049-l1" viewBox="0 0 360 500" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="u049-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3B2A9E"/><stop offset=".55" stop-color="#C2549B"/><stop offset="1" stop-color="#FFB27A"/></linearGradient></defs><rect width="360" height="500" fill="url(#u049-sky)"/><circle cx="236" cy="210" r="62" fill="#FFE2B8"/><circle cx="236" cy="210" r="96" fill="#FFE2B8" opacity=".18"/></svg>
    <svg class="u049-l2" viewBox="0 0 360 500" preserveAspectRatio="xMidYMid slice"><path d="M-10 300 C 60 250 110 270 160 245 S 260 200 370 260 V500 H-10Z" fill="#7A3C8F"/><path d="M-10 330 C 80 300 120 320 190 300 S 300 290 370 310 V500 H-10Z" fill="#5A2E7E" opacity=".9"/></svg>
    <svg class="u049-l3" viewBox="0 0 360 500" preserveAspectRatio="xMidYMid slice"><path d="M-10 370 C 70 330 140 380 210 350 S 320 340 370 360 V500 H-10Z" fill="#2B1B57"/><path d="M40 368 l8 -26 l8 26 M70 360 l10 -34 l10 34" fill="#1E1446"/></svg>
  </div>
  <div class="u049-shade" aria-hidden="true"></div>
  <div class="u049-top"><span class="u049-tag">INTERACTION · ESSAY</span><button class="u049-bm" type="button" aria-pressed="false" aria-label="Bookmark"><svg viewBox="0 0 24 24"><path d="M6.5 4h11a.5.5 0 0 1 .5.5V20l-6-4-6 4V4.5a.5.5 0 0 1 .5-.5z"/></svg></button></div>
  <div class="u049-body">
    <div class="u049-k">ISSUE 12 · 6 MIN</div>
    <h3 class="u049-t">Trust in a<br>short transition</h3>
    <p class="u049-sum">A 150-millisecond response is enough to make a screen feel alive. Deciding where it settles and where it springs is the work of design.</p>
    <div class="u049-foot"><span class="u049-av" aria-hidden="true"></span><span class="u049-by">Jiwoo Han<small>Motion designer</small></span><button class="u049-cta" type="button">Read <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg></button></div>
  </div>
</article>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var bm = root.querySelector('.u049-bm'), cta = root.querySelector('.u049-cta');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var gid = 'u049-s' + Math.random().toString(36).slice(2, 7);
  root.querySelector('linearGradient').id = gid;
  root.querySelector('.u049-l1 rect').setAttribute('fill', 'url(#' + gid + ')');
  function open(v) { root.classList.toggle('is-open', v); }
  root.addEventListener('pointerenter', function (e) { if (e.pointerType === 'mouse') open(true); });
  root.addEventListener('pointermove', function (e) {
    if (e.pointerType !== 'mouse' || rm) return;
    var r = root.getBoundingClientRect();
    root.style.setProperty('--px', ((e.clientX - r.left) / r.width * 2 - 1).toFixed(3));
    root.style.setProperty('--py', ((e.clientY - r.top) / r.height * 2 - 1).toFixed(3));
  });
  root.addEventListener('pointerleave', function (e) {
    if (e.pointerType !== 'mouse') return;
    root.style.setProperty('--px', 0); root.style.setProperty('--py', 0);
    if (!root.contains(document.activeElement)) open(false);
  });
  root.addEventListener('click', function (e) {
    if (e.target.closest('button')) return;
    open(!root.classList.contains('is-open'));
  });
  var quiet = false;
  root.addEventListener('focusin', function () { if (!quiet) open(true); });
  root.addEventListener('focusout', function (e) { if (!root.contains(e.relatedTarget) && !root.matches(':hover')) open(false); });
  root.addEventListener('keydown', function (e) {
    if (e.target === root && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); cta.focus(); }
    if (e.key === 'Escape') { quiet = true; root.focus(); quiet = false; open(false); }
  });
  bm.addEventListener('click', function () {
    var on = bm.getAttribute('aria-pressed') !== 'true';
    bm.setAttribute('aria-pressed', String(on));
    bm.setAttribute('aria-label', on ? 'Remove bookmark' : 'Bookmark');
  });
  cta.addEventListener('click', function () {
    cta.firstChild.textContent = 'Opening ';
    setTimeout(function () { if (root.isConnected) cta.firstChild.textContent = 'Read '; }, 1200);
  });
})();
</script>
--- Code end ---
