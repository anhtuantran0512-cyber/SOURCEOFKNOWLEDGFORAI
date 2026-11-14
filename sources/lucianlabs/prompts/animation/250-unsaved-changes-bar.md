---
source: "lucianlabs"
id: "250"
title: "Unsaved changes bar"
category: "App Screens"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#250"
tags: ["save-bar", "dirty-state", "settings", "form", "saas"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Unsaved changes bar (250, App Screens)
[What it does] Change anything in the store settings and a “2 unsaved changes” bar drops from the top, its count rolling as you go. Try to leave for another menu without saving and the bar shakes and flashes red, asking you to decide first. Press Save and the button spins before the bar turns green with Saved and slides up; press Discard and the changed fields flash as they return to their original values.
[How to use it] Change a setting, try another menu at the top, then save

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
<!-- Lucian UX/UI Prompt #250 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#250 -->
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
.u250{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u250-nv{position:absolute;left:0;right:0;top:0;display:flex;gap:4px;height:54px;align-items:center;padding:0 16px;border-bottom:1px solid var(--ux-line)}
.u250-nv a{padding:7px 11px;border-radius:9px;color:var(--ux-ink-3);font-size:12px;font-weight:800;text-decoration:none;cursor:pointer}
.u250-nv a[aria-current]{background:var(--ux-surface-2);color:var(--ux-ink)}
.u250-fm{position:absolute;left:18px;right:18px;top:70px}
.u250-fm label,.u250-lb{display:block;font-size:11px;font-weight:800;color:var(--ux-ink-2)}
.u250-in{display:block;width:100%;height:40px;margin-top:6px;padding:0 12px;border:0;border-radius:11px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1.5px var(--ux-line);color:var(--ux-ink);font:inherit;font-size:12.5px;font-weight:700;outline:none;box-sizing:border-box}
.u250-in:focus{box-shadow:inset 0 0 0 2px var(--ux-accent)}
.u250-rw{display:flex;align-items:center;gap:10px;margin-top:16px;padding:12px;border-radius:13px;background:var(--ux-surface-2)}
.u250-rw div{flex:1}
.u250-rw b{display:block;font-size:12px;font-weight:850}
.u250-rw small{display:block;margin-top:1px;font-size:10px;font-weight:650;color:var(--ux-ink-3)}
.u250-sw{position:relative;flex:none;width:40px;height:24px;border:0;border-radius:12px;background:var(--ux-surface-3);cursor:pointer;transition:background .2s}
.u250-sw::after{content:"";position:absolute;left:3px;top:3px;width:18px;height:18px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.25);transition:transform .25s cubic-bezier(.3,1.5,.5,1)}
.u250-sw[aria-checked="true"]{background:var(--ux-accent)}
.u250-sw[aria-checked="true"]::after{transform:translateX(16px)}
.u250-lb{margin-top:16px}
.u250-cs{display:flex;gap:8px;margin-top:7px}
.u250-cl{width:30px;height:30px;border:0;border-radius:50%;cursor:pointer;box-shadow:inset 0 0 0 2px rgba(255,255,255,.4);transition:transform .2s cubic-bezier(.3,1.6,.5,1),box-shadow .2s}
.u250-cl[aria-checked="true"]{transform:scale(1.1);box-shadow:0 0 0 2px var(--ux-surface),0 0 0 4px var(--ux-ink)}
.u250 .is-flash{animation:u250-fl .8s ease}
@keyframes u250-fl{25%{box-shadow:0 0 0 3px color-mix(in srgb,#F59E0B 60%,transparent)}}
.u250-br{position:absolute;left:8px;right:8px;top:8px;z-index:3;display:flex;align-items:center;gap:6px;height:44px;padding:0 6px 0 14px;border-radius:14px;background:var(--ux-ink);color:var(--ux-surface);font-size:11.5px;font-weight:800;transform:translateY(-140%);transition:transform .45s cubic-bezier(.3,1.3,.5,1),background .3s}
.u250.is-dirty .u250-br{transform:none}
.u250-br.is-warn{animation:u250-sh .45s;background:#BE123C}
@keyframes u250-sh{20%,60%{transform:translateX(-6px)}40%,80%{transform:translateX(6px)}}
.u250-br.is-ok{background:#059669}
.u250-br span{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.u250-br button{height:32px;padding:0 12px;border:0;border-radius:9px;font:inherit;font-size:11.5px;font-weight:850;cursor:pointer}
.u250-cx{background:color-mix(in srgb,var(--ux-surface) 14%,transparent);color:var(--ux-surface)}
.u250-sv{position:relative;min-width:52px;background:var(--ux-surface);color:var(--ux-ink)}
.u250-sv i{display:none;width:13px;height:13px;margin:0 auto;border-radius:50%;border:2px solid color-mix(in srgb,var(--ux-ink) 25%,transparent);border-top-color:var(--ux-ink);animation:u250-sp .7s linear infinite}
.u250-sv.is-busy i{display:block}
.u250-sv.is-busy b{display:none}
.u250-br.is-ok button{visibility:hidden}
@keyframes u250-sp{to{transform:rotate(360deg)}}
.u250 button:focus-visible,.u250 a:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
@media (prefers-reduced-motion: reduce){.u250-br,.u250-sw::after,.u250-cl{transition:none}.u250-br.is-warn,.u250 .is-flash{animation:none}}
</style>
<div class="ux u250">
  <nav class="u250-nv"><a href="#" aria-current="page">General</a><a href="#">Orders</a><a href="#">Products</a></nav>
  <div class="u250-fm">
    <label>Store name<input class="u250-in" value="Daily Florist" aria-label="Store name" autocomplete="off"></label>
    <div class="u250-rw"><div><b>Low stock alerts</b><small>Notify me when 5 or fewer are left</small></div><button type="button" class="u250-sw" role="switch" aria-checked="false" aria-label="Low stock alerts"></button></div>
    <span class="u250-lb">Brand color</span><div class="u250-cs" role="radiogroup"></div>
  </div>
  <div class="u250-br" role="status"><span class="u250-tx"></span><button type="button" class="u250-cx" tabindex="-1">Discard</button><button type="button" class="u250-sv" tabindex="-1"><i aria-hidden="true"></i><b>Save</b></button></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var inp = root.querySelector('.u250-in'), sw = root.querySelector('.u250-sw'), cs = root.querySelector('.u250-cs'), br = root.querySelector('.u250-br'), tx = root.querySelector('.u250-tx'), cx = root.querySelector('.u250-cx'), sv = root.querySelector('.u250-sv');
  var COL = ['#E11D48', '#F59E0B', '#10B981', '#6366F1'];
  var C = COL.map(function (c, i) { var b = document.createElement('button'); b.type = 'button'; b.className = 'u250-cl'; b.setAttribute('role', 'radio'); b.style.background = c; b.setAttribute('aria-label', c + ' color'); b.addEventListener('click', function () { now.color = i; paint(); diff(); }); cs.appendChild(b); return b; });
  var saved = { name: inp.value, alert: false, color: 0 }, now = { name: inp.value, alert: false, color: 0 };
  function paint() { inp.value = now.name; sw.setAttribute('aria-checked', now.alert); C.forEach(function (b, i) { b.setAttribute('aria-checked', i === now.color); }); }
  function changed() { return ['name', 'alert', 'color'].filter(function (k) { return now[k] !== saved[k]; }); }
  function diff() {
    var n = changed().length;
    br.classList.remove('is-ok', 'is-warn');
    tx.textContent = 'Unsaved changes: ' + n + '';
    root.classList.toggle('is-dirty', n > 0); cx.tabIndex = sv.tabIndex = n ? 0 : -1;
  }
  inp.addEventListener('input', function () { now.name = inp.value; diff(); });
  sw.addEventListener('click', function () { now.alert = !now.alert; paint(); diff(); });
  Array.prototype.forEach.call(root.querySelectorAll('.u250-nv a'), function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      if (!changed().length) return;
      tx.textContent = 'Save or discard first';
      br.classList.remove('is-warn'); void br.offsetWidth; br.classList.add('is-warn');
      setTimeout(function () { if (br.classList.contains('is-warn')) diff(); }, 1600);
      sv.focus({ preventScroll: true });
    });
  });
  cx.addEventListener('click', function () {
    var ch = changed(); now = { name: saved.name, alert: saved.alert, color: saved.color }; paint();
    ch.forEach(function (k) { var el = k === 'name' ? inp : k === 'alert' ? sw : C[now.color]; el.classList.remove('is-flash'); void el.offsetWidth; el.classList.add('is-flash'); });
    diff();
  });
  sv.addEventListener('click', function () {
    if (sv.classList.contains('is-busy')) return;
    sv.classList.add('is-busy');
    setTimeout(function () {
      sv.classList.remove('is-busy'); saved = { name: now.name, alert: now.alert, color: now.color };
      br.classList.remove('is-warn'); br.classList.add('is-ok'); tx.textContent = 'Saved';
      setTimeout(function () { root.classList.remove('is-dirty'); cx.tabIndex = sv.tabIndex = -1; }, 900);
    }, 750);
  });
  paint(); diff();
})();
</script>
--- Code end ---
