---
source: "lucianlabs"
id: "317"
title: "Sort list with flying rows"
category: "Sections & Content"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#317"
tags: ["flip", "sort", "list", "table", "reorder"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Sort list with flying rows (317, Sections & Content)
[What it does] Change the sort and the rows don’t jump all at once; each glides to its new place. Rows moving up lift slightly toward you while rows moving down recede, so overlapping paths never get confusing. The number in the sorted column is highlighted by how far each row moved.
[How to use it] Pick a sort key at the top, or press the same key again to flip ascending and descending

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
<!-- Lucian UX/UI Prompt #317 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#317 -->
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
.u317{position:relative;width:340px;height:350px;display:flex;flex-direction:column;padding:16px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u317-ss{display:flex;gap:4px;padding:4px;border-radius:13px;background:var(--ux-surface-2)}
.u317-s{flex:1;height:32px;border:0;border-radius:10px;display:flex;align-items:center;justify-content:center;gap:4px;background:none;font-size:12.5px;font-weight:750;color:var(--ux-ink-3)}
.u317-s[aria-pressed="true"]{background:var(--ux-surface);color:var(--ux-ink);box-shadow:0 0 0 1px var(--ux-line)}
.u317-s svg{width:10px;height:10px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;transition:transform .35s var(--ux-spring);opacity:0}
.u317-s[aria-pressed="true"] svg{opacity:1}
.u317-s.desc svg{transform:rotate(180deg)}
.u317-ls{position:relative;margin:10px 0 0;padding:0;list-style:none}
.u317-r{position:absolute;left:0;right:0;top:0;height:44px;display:flex;align-items:center;gap:8px;padding:0 8px;border-radius:12px;background:var(--ux-surface);transition:transform .6s cubic-bezier(.3,1.1,.4,1),box-shadow .3s}
.u317-r.up{z-index:2;box-shadow:0 10px 22px -12px var(--ux-shadow-strong)}
.u317-r.dn{z-index:0;opacity:.9}
.u317-r i{flex:none;width:28px;height:28px;border-radius:9px;background:linear-gradient(135deg,var(--a),var(--b))}
.u317-r b{flex:1;min-width:0;font-size:13px;font-weight:750;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.u317-r span{flex:none;text-align:right;font:650 12px/1 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--ux-ink-3);font-variant-numeric:tabular-nums}
.u317-r span.p{width:66px}
.u317-r span.s{width:40px}
.u317-r span.k{color:var(--ux-ink);font-weight:800}
.u317-r em{width:26px;font-style:normal;font:700 11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;text-align:right;opacity:0;transition:opacity .3s}
.u317-r em.show{opacity:1}
</style>
<div class="ux u317">
  <div class="u317-ss" role="group" aria-label="Sort by">
    <button class="u317-s" type="button" aria-pressed="true">Name<svg viewBox="0 0 10 10" aria-hidden="true"><path d="M5 8V2M2 5l3-3 3 3"/></svg></button>
    <button class="u317-s" type="button" aria-pressed="false">Price<svg viewBox="0 0 10 10" aria-hidden="true"><path d="M5 8V2M2 5l3-3 3 3"/></svg></button>
    <button class="u317-s" type="button" aria-pressed="false">Rating<svg viewBox="0 0 10 10" aria-hidden="true"><path d="M5 8V2M2 5l3-3 3 3"/></svg></button>
  </div>
  <ul class="u317-ls" aria-live="polite"></ul>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var ls = root.querySelector('.u317-ls'), ss = Array.prototype.slice.call(root.querySelectorAll('.u317-s'));
  var DATA = [['Wireless earbuds', 129000, 4.6], ['Mechanical keyboard', 89000, 4.8], ['Smartwatch', 299000, 4.3], ['Portable speaker', 59000, 4.1], ['Laptop stand', 39000, 4.7], ['Power bank', 45000, 4.4]];
  var C = [['#FFA8A8', '#FFD43B'], ['#A5D8FF', '#B197FC'], ['#96F2D7', '#4DABF7'], ['#FFC078', '#F783AC'], ['#C0EB75', '#38D9A9'], ['#D0BFFF', '#74C0FC']];
  var key = 0, desc = false, order = DATA.map(function (_, i) { return i; });
  var rows = DATA.map(function (d, i) {
    var li = document.createElement('li');
    li.className = 'u317-r';
    li.innerHTML = '<i style="--a:' + C[i][0] + ';--b:' + C[i][1] + '"></i><b></b><span class="p"></span><span class="s"></span><em aria-hidden="true"></em>';
    li.querySelector('b').textContent = d[0];
    li.querySelector('.p').textContent = d[1].toLocaleString() + ' KRW';
    li.querySelector('.s').textContent = '★ ' + d[2].toFixed(1);
    ls.appendChild(li);
    return li;
  });
  ls.style.height = (DATA.length * 48) + 'px';
  function place(prev) {
    order.forEach(function (idx, pos) {
      var r = rows[idx], was = prev ? prev.indexOf(idx) : pos, d = was - pos;
      r.style.transform = 'translateY(' + (pos * 48) + 'px)';
      r.classList.toggle('up', d > 0); r.classList.toggle('dn', d < 0);
      var em = r.querySelector('em');
      em.textContent = d > 0 ? '▲' + d : d < 0 ? '▼' + (-d) : '';
      em.style.color = d > 0 ? 'var(--ux-mint)' : 'var(--ux-danger)';
      em.classList.toggle('show', !!d);
      r.querySelector('.p').classList.toggle('k', key === 1);
      r.querySelector('.s').classList.toggle('k', key === 2);
    });
    setTimeout(function () { rows.forEach(function (r) { r.classList.remove('up', 'dn'); r.querySelector('em').classList.remove('show'); }); }, 1300);
  }
  function sort(k) {
    if (k === key) desc = !desc; else { key = k; desc = k > 0; }
    ss.forEach(function (b, i) { b.setAttribute('aria-pressed', String(i === key)); b.classList.toggle('desc', i === key && desc); });
    var prev = order.slice();
    order.sort(function (a, b) {
      var x = DATA[a][key], y = DATA[b][key];
      var c = key === 0 ? String(x).localeCompare(String(y), 'en') : x - y;
      return desc ? -c : c;
    });
    place(prev);
  }
  ss.forEach(function (b, i) { b.addEventListener('click', function () { sort(i); }); });
  order.sort(function (a, b) { return DATA[a][0].localeCompare(DATA[b][0], 'en'); });
  place(null);
})();
</script>
--- Code end ---
