---
source: "lucianlabs"
id: "032"
title: "Drag-and-drop upload"
category: "Inputs & Search"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#032"
tags: ["upload", "dropzone", "drag-drop", "progress", "file"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Drag-and-drop upload (032, Inputs & Search)
[What it does] Drag files in and the dashed border starts marching as the area grows; each dropped file fills its own progress bar in the list below. Finished files draw a check, and failed ones can be retried.
[How to use it] Drop files in or press the area to choose them. Try Retry on the failed file too

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
<!-- Lucian UX/UI Prompt #032 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#032 -->
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
.u032{position:relative;width:340px;height:420px}
.u032-zone{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;width:100%;height:196px;border:0;padding:0;border-radius:26px;background:var(--ux-surface);color:var(--ux-ink);cursor:pointer;
  transition:transform .5s var(--ux-spring),background-color .3s var(--ux-ease)}
.u032-zone:focus-visible{outline:2px solid var(--ux-accent);outline-offset:4px}
.u032-zone svg.u032-dash{position:absolute;left:1px;top:1px;width:calc(100% - 2px);height:calc(100% - 2px);overflow:visible;pointer-events:none}
.u032-dash rect{fill:none;stroke:var(--ux-line-2);stroke-width:2;stroke-dasharray:8 7;transition:stroke .3s var(--ux-ease)}
.u032-zone:hover .u032-dash rect,.u032.is-over .u032-dash rect{stroke:var(--ux-accent);animation:u032-march .9s linear infinite}
@keyframes u032-march{to{stroke-dashoffset:-30}}
.u032.is-over .u032-zone{transform:scale(1.03);background:color-mix(in srgb,var(--ux-accent) 7%,var(--ux-surface))}
.u032-orb{width:60px;height:60px;border-radius:20px;display:grid;place-items:center;color:#fff;background:linear-gradient(140deg,#5B8CFF,#8B6CFF);box-shadow:0 16px 28px -14px rgba(91,108,255,.8);transition:transform .5s var(--ux-spring)}
.u032-orb svg{width:28px;height:28px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.u032-zone:hover .u032-orb{transform:translateY(-4px)}
.u032.is-over .u032-orb{transform:translateY(-8px) scale(1.1) rotate(-6deg)}
.u032-zone b{margin-top:14px;font-size:15.5px;font-weight:720;letter-spacing:-.02em}
.u032-zone b em{font-style:normal;color:var(--ux-accent)}
.u032-zone small{margin-top:4px;font-size:12.5px;color:var(--ux-ink-3)}
.u032-file{position:absolute;width:1px;height:1px;opacity:0;pointer-events:none}
.u032-list{margin:14px 0 0;padding:0;list-style:none;display:flex;flex-direction:column;gap:8px}
.u032-row{position:relative;display:flex;align-items:center;gap:12px;height:62px;padding:0 12px;border-radius:18px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line);overflow:hidden;animation:u032-in .5s var(--ux-spring)}
@keyframes u032-in{from{transform:translateY(-10px) scale(.96);opacity:0}}
.u032-row.out{transition:transform .35s var(--ux-ease),opacity .3s;transform:translateX(30px);opacity:0}
.u032-ic{width:36px;height:40px;flex:none;border-radius:9px;display:grid;place-items:end center;padding-bottom:5px;font-size:8.5px;font-weight:800;letter-spacing:.04em;color:#fff;background:var(--c)}
.u032-meta{flex:1;min-width:0}
.u032-meta b{display:block;font-size:14px;font-weight:660;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.u032-meta small{display:block;margin-top:3px;font-size:12px;color:var(--ux-ink-3);font-variant-numeric:tabular-nums}
.u032-bar{position:absolute;left:0;bottom:0;height:3px;width:100%;background:var(--ux-accent);transform-origin:0 50%;transform:scaleX(var(--p,0));transition:transform .2s linear,background-color .3s,opacity .5s .4s}
.u032-row.done .u032-bar{background:var(--ux-mint);opacity:0}
.u032-row.fail .u032-bar{background:var(--ux-danger)}
.u032-st{width:30px;height:30px;flex:none;border-radius:50%;display:grid;place-items:center}
.u032-st svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}
.u032-row.done .u032-st{background:var(--ux-mint);color:var(--ux-accent-ink);animation:u032-pop .45s var(--ux-spring)}
@keyframes u032-pop{from{transform:scale(.3)}}
.u032-row.done .u032-st path{stroke-dasharray:16;stroke-dashoffset:16;animation:u032-draw .4s var(--ux-ease) .15s forwards}
@keyframes u032-draw{to{stroke-dashoffset:0}}
.u032-row.fail .u032-meta small{color:var(--ux-danger)}
.u032-retry{height:32px;padding:0 12px;border:0;border-radius:10px;background:color-mix(in srgb,var(--ux-danger) 12%,transparent);color:var(--ux-danger);font-size:12.5px;font-weight:700;white-space:nowrap}
.u032-retry:focus-visible{outline:2px solid var(--ux-danger);outline-offset:2px}
.u032-spin{width:20px;height:20px;border-radius:50%;border:2.5px solid var(--ux-surface-3);border-top-color:var(--ux-accent);animation:u032-rot .8s linear infinite}
@keyframes u032-rot{to{transform:rotate(360deg)}}
</style>
<div class="ux u032">
  <button class="u032-zone" type="button">
    <svg class="u032-dash" aria-hidden="true"><rect width="100%" height="100%" rx="25"/></svg>
    <span class="u032-orb" aria-hidden="true"><svg viewBox="0 0 28 28"><path d="M8.5 20.5H7a5 5 0 0 1-.6-10 7 7 0 0 1 13.4-1.6A5.5 5.5 0 0 1 21 20.5h-1.5M14 13v10M10.5 16.5L14 13l3.5 3.5"/></svg></span>
    <b>Drag files here or <em>browse</em></b>
    <small>PNG, JPG, PDF, FIG · up to 50 MB each</small>
  </button>
  <input class="u032-file" type="file" multiple tabindex="-1" aria-hidden="true">
  <ul class="u032-list" aria-live="polite"></ul>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var zone = root.querySelector('.u032-zone');
  var pick = root.querySelector('.u032-file');
  var list = root.querySelector('.u032-list');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var TYPE = { pdf: '#E5484D', png: '#3D8BFF', jpg: '#22A06B', jpeg: '#22A06B', fig: '#8B6CFF' };
  function size(b) { return b > 1048576 ? (b / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(b / 1024)) + ' KB'; }
  function run(row, bytes, fail) {
    row.className = 'u032-row';
    var st = row.querySelector('.u032-st');
    var sm = row.querySelector('small');
    st.innerHTML = '<span class="u032-spin" aria-hidden="true"></span>';
    var p = 0, t0 = performance.now(), D = rm ? 300 : 1800 + Math.random() * 900;
    (function f(now) {
      if (!root.isConnected) return;
      p = Math.min(1, (now - t0) / D);
      var shown = fail ? Math.min(p, 0.62) : p;
      row.style.setProperty('--p', shown.toFixed(3));
      sm.textContent = size(bytes * shown) + ' / ' + size(bytes) + ' · ' + Math.round(shown * 100) + '%';
      if (fail && p >= 0.62) {
        row.classList.add('fail');
        sm.textContent = 'Connection lost · stopped at ' + Math.round(shown * 100) + '%';
        st.outerHTML = '<button class="u032-retry" type="button">Retry</button>';
        row.querySelector('.u032-retry').addEventListener('click', function () { var r = row.querySelector('.u032-retry'); r.outerHTML = '<span class="u032-st"></span>'; run(row, bytes, false); });
        return;
      }
      if (p < 1) requestAnimationFrame(f);
      else { row.classList.add('done'); sm.textContent = size(bytes) + ' · Uploaded'; st.innerHTML = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8.4l3 3 6-6.4"/></svg>'; }
    })(t0);
  }
  function add(name, bytes, fail) {
    var ext = (name.split('.').pop() || '').toLowerCase();
    var li = document.createElement('li');
    li.className = 'u032-row';
    li.innerHTML = '<span class="u032-ic" style="--c:' + (TYPE[ext] || '#8E8A97') + '" aria-hidden="true">' + (ext.slice(0, 3).toUpperCase() || 'FILE') + '</span><span class="u032-meta"><b></b><small></small></span><span class="u032-st"></span><span class="u032-bar" aria-hidden="true"></span>';
    li.querySelector('b').textContent = name;
    list.insertBefore(li, list.firstChild);
    while (list.children.length > 3) list.lastElementChild.remove();
    run(li, bytes, fail);
  }
  zone.addEventListener('click', function () { pick.click(); });
  pick.addEventListener('change', function () {
    Array.prototype.forEach.call(pick.files, function (f) { add(f.name, f.size, false); });
    pick.value = '';
  });
  var depth = 0;
  zone.addEventListener('dragenter', function (e) { e.preventDefault(); depth++; root.classList.add('is-over'); });
  zone.addEventListener('dragover', function (e) { e.preventDefault(); });
  zone.addEventListener('dragleave', function () { if (--depth <= 0) { depth = 0; root.classList.remove('is-over'); } });
  zone.addEventListener('drop', function (e) {
    e.preventDefault(); depth = 0; root.classList.remove('is-over');
    Array.prototype.forEach.call(e.dataTransfer.files, function (f) { add(f.name, f.size, false); });
  });
  add('brand-guide.pdf', 18.4 * 1048576, true);
  add('main-banner@2x.png', 4.2 * 1048576, false);
})();
</script>
--- Code end ---
