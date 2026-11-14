---
source: "lucianlabs"
id: "013"
title: "Stretchy switch"
category: "Toggles & Pickers"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#013"
tags: ["switch", "toggle", "squash", "drag", "stretch"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Stretchy switch (013, Toggles & Pickers)
[What it does] While it travels, the knob stretches like rubber and then snaps back into place. The symbol inside the knob is redrawn from ✕ to ✓ and the caption below changes with the state. You can also drag the knob.
[How to use it] Press the switch or drag the knob left and right

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
<!-- Lucian UX/UI Prompt #013 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#013 -->
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
.u013{--on:linear-gradient(135deg,#2FD8A8,#14B8A6 55%,#0EA5E9);position:relative;width:300px;height:220px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px}
.u013-sw{position:relative;width:140px;height:76px;border:0;padding:0;border-radius:999px;background:var(--ux-surface-3);touch-action:none;
  box-shadow:inset 0 2px 6px rgba(0,0,0,.12),inset 0 0 0 1px var(--ux-line);transition:box-shadow .5s var(--ux-ease)}
.u013-sw::before{content:"";position:absolute;inset:0;border-radius:inherit;background:var(--on);opacity:0;transition:opacity .45s var(--ux-ease)}
.u013-sw:focus-visible{outline:2px solid var(--ux-accent);outline-offset:4px}
.u013.is-on .u013-sw::before{opacity:1}
.u013.is-on .u013-sw{box-shadow:inset 0 2px 6px rgba(0,0,0,.12),0 16px 30px -16px rgba(20,184,166,.8)}

.u013-knob{position:absolute;top:8px;left:8px;width:60px;height:60px;border-radius:999px;background:#fff;display:grid;place-items:center;
  box-shadow:0 1px 0 rgba(255,255,255,.9) inset,0 6px 14px -4px rgba(0,0,0,.28),0 0 0 .5px rgba(0,0,0,.06);
  transition:left .5s var(--ux-spring),width .32s var(--ux-ease)}
.u013.is-on .u013-knob{left:72px}
.u013.is-stretch .u013-knob{width:84px;transition:left .5s var(--ux-spring),width .18s var(--ux-ease)}
.u013.is-on.is-stretch .u013-knob{left:48px}
.u013.is-drag .u013-knob{transition:width .2s var(--ux-ease)}
.u013-knob svg{width:24px;height:24px;fill:none;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}
.u013-x{stroke:#A3A0AA;stroke-dasharray:14;stroke-dashoffset:0;transition:stroke-dashoffset .3s var(--ux-ease) .1s}
.u013-v{stroke:#14B8A6;stroke-dasharray:20;stroke-dashoffset:20;transition:stroke-dashoffset .35s var(--ux-ease)}
.u013.is-on .u013-x{stroke-dashoffset:14;transition-delay:0s}
.u013.is-on .u013-v{stroke-dashoffset:0;transition-delay:.18s}
.u013-txt{width:260px;text-align:center}
.u013-txt b{display:block;font-size:18px;font-weight:740;letter-spacing:-.03em}
.u013-sub{position:relative;display:block;height:20px;margin-top:5px;overflow:hidden;font-size:14px;color:var(--ux-ink-3)}
.u013-sub span{display:block;line-height:20px;transition:transform .5s var(--ux-spring),opacity .3s var(--ux-ease)}
.u013-sub span+span{position:absolute;left:0;right:0;top:0;transform:translateY(100%);opacity:0;color:var(--ux-mint);font-weight:620}
.u013.is-on .u013-sub span:first-child{transform:translateY(-100%);opacity:0}
.u013.is-on .u013-sub span+span{transform:none;opacity:1}
</style>
<div class="ux u013">
  <button class="u013-sw" type="button" role="switch" aria-checked="false">
    <span class="u013-knob" aria-hidden="true">
      <svg viewBox="0 0 24 24"><path class="u013-x" d="M7.5 7.5l9 9M16.5 7.5l-9 9"/><path class="u013-v" d="M5.5 12.5l4.5 4.5 8.5-9"/></svg>
    </span>
  </button>
  <div class="u013-txt">
    <b class="u013-lab">Do Not Disturb</b>
    <span class="u013-sub" aria-live="polite"><span>Notifications ring as usual</span><span>Silenced until 8 AM tomorrow</span></span>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sw = root.querySelector('.u013-sw');
  var knob = root.querySelector('.u013-knob');
  var lab = root.querySelector('.u013-lab');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var id = 'u013-l-' + Math.random().toString(36).slice(2, 7);
  lab.id = id;
  sw.setAttribute('aria-labelledby', id);
  var on = false, t = 0;

  function set(v) {
    on = v;
    root.classList.toggle('is-on', v);
    sw.setAttribute('aria-checked', String(v));
    if (!rm) {
      root.classList.add('is-stretch');
      clearTimeout(t);
      t = setTimeout(function () { root.classList.remove('is-stretch'); }, 170);
    }
  }
  var drag = null;
  sw.addEventListener('pointerdown', function (e) {
    if (e.button !== 0) return;
    drag = { x: e.clientX, moved: false, start: on ? 72 : 8 };
    sw.setPointerCapture(e.pointerId);
  });
  sw.addEventListener('pointermove', function (e) {
    if (!drag) return;
    var k = sw.getBoundingClientRect().width / sw.offsetWidth || 1;
    var dx = (e.clientX - drag.x) / k;
    if (Math.abs(dx) > 4) drag.moved = true;
    if (!drag.moved) return;
    root.classList.add('is-drag');
    var x = Math.max(8, Math.min(72, drag.start + dx));
    knob.style.left = x + 'px';
    knob.style.width = (60 + Math.min(18, Math.abs(dx) * 0.25)) + 'px';
  });
  function end(e) {
    if (!drag) return;
    var d = drag; drag = null;
    root.classList.remove('is-drag');
    var x = parseFloat(knob.style.left || (on ? 72 : 8));
    knob.style.left = ''; knob.style.width = '';
    if (d.moved) { set(x > 40); sw._skip = true; }
  }
  sw.addEventListener('pointerup', end);
  sw.addEventListener('pointercancel', end);
  sw.addEventListener('click', function () {
    if (sw._skip) { sw._skip = false; return; }
    set(!on);
  });
})();
</script>
--- Code end ---
