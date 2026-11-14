---
source: "lucianlabs"
id: "034"
title: "Airport autocomplete"
category: "Inputs & Search"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#034"
tags: ["autocomplete", "combobox", "typeahead", "search", "listbox"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Airport autocomplete (034, Inputs & Search)
[What it does] As you type, the rest of the name appears faintly and Tab accepts it. The list below filters with the matching letters highlighted, and the highlight bar glides along with the arrow keys. Choosing one locks it in with a plane icon.
[How to use it] Type “To”, “O” or “Ba”. Tab completes; arrow keys and Enter choose

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
<!-- Lucian UX/UI Prompt #034 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#034 -->
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
.u034{position:relative;width:340px;height:380px}
.u034-lab{display:block;margin:0 4px 8px;font-size:13px;font-weight:700;color:var(--ux-ink-3)}
.u034-box{position:relative;display:flex;align-items:center;gap:10px;height:60px;padding:0 16px;border-radius:18px;background:var(--ux-surface);box-shadow:0 0 0 1.5px var(--ux-line-2);transition:box-shadow .25s var(--ux-ease)}
.u034-box:focus-within{box-shadow:0 0 0 2px var(--ux-accent),0 0 0 6px var(--ux-accent-soft)}
.u034-pl{width:22px;height:22px;flex:none;fill:none;stroke:var(--ux-ink-3);stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round;transition:stroke .3s,transform .6s var(--ux-spring)}
.u034.is-set .u034-pl{stroke:var(--ux-accent);transform:translateX(3px) rotate(-12deg)}
.u034-wrap{position:relative;flex:1;height:100%}
.u034-ghost,.u034-in{position:absolute;inset:0;width:100%;padding:0;border:0;font:inherit;font-size:17px;font-weight:650;letter-spacing:-.02em;line-height:60px;background:none;white-space:pre}
.u034-ghost{color:var(--ux-ink-3);pointer-events:none;opacity:.7}
.u034-ghost b{font-weight:inherit;color:transparent}
.u034-in{outline:0;color:var(--ux-ink)}
.u034-in:focus-visible{outline:none}
.u034-code{flex:none;padding:5px 9px;border-radius:9px;background:var(--ux-accent-soft);color:var(--ux-accent);font-size:12.5px;font-weight:800;letter-spacing:.06em;opacity:0;transform:scale(.6);transition:opacity .2s,transform .45s var(--ux-spring)}
.u034.is-set .u034-code{opacity:1;transform:none}
.u034-list{position:relative;margin:10px 0 0;padding:6px;list-style:none;border-radius:20px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 26px 50px -30px var(--ux-shadow-strong);height:268px;overflow:hidden;transition:opacity .25s var(--ux-ease)}
.u034-hl{position:absolute;left:6px;right:6px;top:6px;height:64px;border-radius:14px;background:var(--ux-surface-2);transform:translateY(calc(var(--i,0) * 64px));transition:transform .35s var(--ux-spring),opacity .2s;pointer-events:none}
.u034-o{position:relative;display:flex;align-items:center;gap:12px;height:64px;padding:0 12px;border-radius:14px;cursor:pointer;animation:u034-in .35s var(--ux-spring) backwards}
@keyframes u034-in{from{opacity:0;transform:translateY(6px)}}
.u034-o i{width:38px;height:38px;flex:none;border-radius:12px;display:grid;place-items:center;font-style:normal;font-size:11px;font-weight:800;letter-spacing:.04em;color:#fff;background:var(--c)}
.u034-o b{display:block;font-size:15px;font-weight:680}
.u034-o b mark{background:none;color:var(--ux-accent)}
.u034-o small{display:block;margin-top:2px;font-size:12.5px;color:var(--ux-ink-3)}
.u034-o em{margin-left:auto;font-style:normal;font-size:12px;font-weight:650;color:var(--ux-ink-3);font-variant-numeric:tabular-nums}
.u034-none{padding:90px 0;text-align:center;font-size:14px;color:var(--ux-ink-3)}
</style>
<div class="ux u034">
  <label class="u034-lab">Arriving at</label>
  <div class="u034-box">
    <svg class="u034-pl" viewBox="0 0 24 24" aria-hidden="true"><path d="M10.5 13.5L4 11l1.5-1.5 7 1 4-4c1-1 2.6-1.4 3.2-.7.7.6.3 2.2-.7 3.2l-4 4 1 7L14.5 21 12 14.5l-3 3V20l-1.5 1L6 18l-3-1.5 1-1.5h2.5z"/></svg>
    <div class="u034-wrap">
      <span class="u034-ghost" aria-hidden="true"></span>
      <input class="u034-in" type="text" role="combobox" aria-autocomplete="both" aria-expanded="true" autocomplete="off" value="To" placeholder="City or airport code">
    </div>
    <span class="u034-code" aria-hidden="true"></span>
  </div>
  <ul class="u034-list" role="listbox" aria-label="Airports"><li class="u034-hl" role="presentation"></li></ul>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var input = root.querySelector('.u034-in');
  var ghost = root.querySelector('.u034-ghost');
  var list = root.querySelector('.u034-list');
  var hl = root.querySelector('.u034-hl');
  var code = root.querySelector('.u034-code');
  var lab = root.querySelector('.u034-lab');
  var uid = 'u034-' + Math.random().toString(36).slice(2, 7);
  input.id = uid + '-in'; lab.htmlFor = input.id;
  list.id = uid; input.setAttribute('aria-controls', uid);
  var DATA = [
    ['Tokyo', 'Narita International', 'NRT', '2h 25m', 'linear-gradient(140deg,#FF7A93,#F0264D)'],
    ['Tokyo', 'Haneda Airport', 'HND', '2h 20m', 'linear-gradient(140deg,#FF8A65,#E5484D)'],
    ['Doha', 'Hamad International', 'DOH', '10h 40m', 'linear-gradient(140deg,#B07CFF,#7B61FF)'],
    ['Osaka', 'Kansai International', 'KIX', '1h 50m', 'linear-gradient(140deg,#FFB547,#FF7A45)'],
    ['Auckland', 'Auckland Airport', 'AKL', '11h 30m', 'linear-gradient(140deg,#22C3A6,#0EA5E9)'],
    ['Bangkok', 'Suvarnabhumi Airport', 'BKK', '5h 50m', 'linear-gradient(140deg,#5B8CFF,#22C3A6)'],
    ['Da Nang', 'Da Nang International', 'DAD', '4h 30m', 'linear-gradient(140deg,#3D8BFF,#8B6CFF)']
  ];
  var shown = [], act = 0;
  function esc(s) { return s.replace(/[&<>]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]; }); }
  function hit(d, q) { return d[0].indexOf(q) === 0 || d[2].toLowerCase().indexOf(q.toLowerCase()) === 0; }
  function render() {
    var q = input.value.trim();
    shown = q ? DATA.filter(function (d) { return hit(d, q) || d[1].indexOf(q) >= 0; }).slice(0, 4) : DATA.slice(0, 4);
    act = 0;
    Array.prototype.slice.call(list.querySelectorAll('.u034-o,.u034-none')).forEach(function (n) { n.remove(); });
    hl.style.opacity = shown.length ? 1 : 0;
    if (!shown.length) { list.insertAdjacentHTML('beforeend', '<li class="u034-none">No airports match ‘' + esc(q) + '’</li>'); }
    shown.forEach(function (d, i) {
      var li = document.createElement('li');
      li.className = 'u034-o';
      li.id = uid + '-' + i;
      li.setAttribute('role', 'option');
      li.style.animationDelay = (i * 35) + 'ms';
      var name = esc(d[0]);
      if (q && d[0].indexOf(q) === 0) name = '<mark>' + esc(q) + '</mark>' + esc(d[0].slice(q.length));
      li.innerHTML = '<i style="--c:' + d[4] + '" aria-hidden="true">' + d[2] + '</i><span><b>' + name + '</b><small>' + esc(d[1]) + '</small></span><em>' + d[3] + '</em>';
      li.addEventListener('pointermove', function () { if (act !== i) { act = i; mark(); } });
      li.addEventListener('mousedown', function (e) { e.preventDefault(); choose(i); });
      list.appendChild(li);
    });
    mark();
  }
  function mark() {
    hl.style.setProperty('--i', act);
    Array.prototype.forEach.call(list.querySelectorAll('.u034-o'), function (li, i) { li.setAttribute('aria-selected', String(i === act)); });
    if (shown[act]) input.setAttribute('aria-activedescendant', uid + '-' + act); else input.removeAttribute('aria-activedescendant');
    var q = input.value, d = shown[act];
    ghost.innerHTML = d && q && d[0].indexOf(q) === 0 && d[0] !== q ? '<b>' + esc(q) + '</b>' + esc(d[0].slice(q.length)) + ' (' + d[2] + ')' : '';
  }
  function choose(i) {
    var d = shown[i];
    if (!d) return;
    input.value = d[0] + ' · ' + d[1];
    code.textContent = d[2];
    root.classList.add('is-set');
    ghost.innerHTML = '';
  }
  input.addEventListener('input', function () { root.classList.remove('is-set'); render(); });
  input.addEventListener('keydown', function (e) {
    if (e.isComposing || e.keyCode === 229) return;
    if (e.key === 'ArrowDown' && shown.length) { e.preventDefault(); act = (act + 1) % shown.length; mark(); }
    else if (e.key === 'ArrowUp' && shown.length) { e.preventDefault(); act = (act - 1 + shown.length) % shown.length; mark(); }
    else if (e.key === 'Enter') { e.preventDefault(); choose(act); }
    else if (e.key === 'Tab' && ghost.textContent && !e.shiftKey) { e.preventDefault(); choose(act); }
    else if (e.key === 'Escape') { e.preventDefault(); input.value = ''; root.classList.remove('is-set'); render(); }
  });
  render();
})();
</script>
--- Code end ---
