---
source: "lucianlabs"
id: "248"
title: "Feature request board that reorders on votes"
category: "Sections & Content"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#248"
tags: ["voting", "roadmap", "feedback", "reorder", "saas"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Feature request board that reorders on votes (248, Sections & Content)
[What it does] A product site's feature request board. Press the arrow on the left of an item and the number rolls up by one with a floating +1, and once its votes beat the row above, the item glides up a place. Press again to take the vote back and it slides back down, and each item carries a colored status badge such as In progress or Under review.
[How to use it] Press the arrow on the left of an item to vote, and again to take it back

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
<!-- Lucian UX/UI Prompt #248 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#248 -->
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
.u248{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u248-hd{position:absolute;left:20px;right:18px;top:20px;display:flex;align-items:flex-start}
.u248-hd div{margin-right:auto}
.u248-hd b{display:block;font-size:16px;font-weight:900;letter-spacing:-.03em}
.u248-hd small{display:block;margin-top:3px;font-size:10.5px;font-weight:650;color:var(--ux-ink-3)}
.u248-hd span{height:28px;padding:0 11px;border-radius:999px;background:var(--ux-ink);color:var(--ux-surface);font-size:10.5px;font-weight:850;display:inline-flex;align-items:center;white-space:nowrap}
.u248-ls{position:absolute;left:14px;right:14px;top:74px;margin:0;padding:0;list-style:none}
.u248-it{position:relative;display:flex;align-items:center;gap:11px;height:46px;margin-bottom:6px;padding:0 10px 0 6px;border-radius:14px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line);will-change:transform}
.u248-it.is-mv{z-index:2;box-shadow:inset 0 0 0 1px var(--ux-line),0 12px 24px -12px var(--ux-shadow-strong)}
.u248-up{position:relative;flex:none;width:40px;height:36px;border:0;border-radius:10px;background:var(--ux-surface);box-shadow:inset 0 0 0 1px var(--ux-line);color:var(--ux-ink-2);font:inherit;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0;cursor:pointer;transition:background .2s,color .2s,box-shadow .2s}
.u248-up:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u248-up svg{width:11px;height:11px;transition:transform .35s cubic-bezier(.3,1.8,.5,1)}
.u248-up.is-on{background:var(--ux-accent);color:#fff;box-shadow:none}
.u248-up.is-on svg{transform:translateY(-1px)}
.u248-up.is-pop svg{animation:u248-hop .45s cubic-bezier(.3,1.6,.5,1)}
@keyframes u248-hop{40%{transform:translateY(-5px)}}
.u248-nm{position:relative;display:block;height:13px;overflow:hidden;font-size:11px;font-weight:900;line-height:13px;font-variant-numeric:tabular-nums}
.u248-nm span{display:block;transition:transform .35s cubic-bezier(.3,1.4,.5,1)}
.u248-pl{position:absolute;left:50%;top:-4px;font-size:10px;font-weight:900;color:var(--ux-accent);pointer-events:none;animation:u248-pl .8s ease-out forwards}
@keyframes u248-pl{from{transform:translate(-50%,0);opacity:1}to{transform:translate(-50%,-18px);opacity:0}}
.u248-tx{flex:1;min-width:0}
.u248-tx b{display:block;font-size:12.5px;font-weight:850;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.u248-bd{display:inline-flex;align-items:center;gap:4px;margin-top:3px;font-size:9.5px;font-weight:800;color:var(--c)}
.u248-bd::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--c)}
.u248-rk{flex:none;font-size:10px;font-weight:850;color:var(--ux-ink-3);font-variant-numeric:tabular-nums}
@media (prefers-reduced-motion: reduce){.u248-it,.u248-nm span,.u248-up svg{transition:none!important;animation:none!important}.u248-pl{display:none}}
</style>
<div class="ux u248">
  <div class="u248-hd"><div><b>What we build next</b><small>We build in order of votes</small></div><span>+ Suggest</span></div>
  <ol class="u248-ls"></ol>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var ls = root.querySelector('.u248-ls');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var D = [['Google Calendar sync', 42, 0], ['Dark mode calendar', 39, 1], ['Home screen widget', 37, 2], ['Export to CSV', 37, 2], ['Per-team permissions', 22, 3]];
  var ST = [['In progress', '#2563EB'], ['Planned', '#7C3AED'], ['Under review', '#D97706'], ['Received', '#64748B']];
  var items = D.map(function (d, i) {
    var li = document.createElement('li'); li.className = 'u248-it';
    li.innerHTML = '<button type="button" class="u248-up" aria-pressed="false"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2 8l4-4.5L10 8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="u248-nm"><span></span></span></button><div class="u248-tx"><b></b><span class="u248-bd"></span></div><span class="u248-rk"></span>';
    li.querySelector('b').textContent = d[0];
    var bd = li.querySelector('.u248-bd'); bd.textContent = ST[d[2]][0]; bd.style.setProperty('--c', ST[d[2]][1]);
    var it = { el: li, name: d[0], n: d[1], base: d[1], i: i, on: false, btn: li.querySelector('.u248-up'), nm: li.querySelector('.u248-nm') };
    it.nm.firstChild.textContent = d[1];
    it.btn.addEventListener('click', function () { vote(it); });
    ls.appendChild(li); return it;
  });
  function label(it) { it.btn.setAttribute('aria-label', it.name + ', ' + it.n + ' votes' + (it.on ? ', remove vote' : ', vote')); }
  function roll(it, up) {
    var box = it.nm, old = box.firstChild, nw = document.createElement('span');
    nw.textContent = it.n;
    if (rm) { box.replaceChild(nw, old); return; }
    nw.style.transform = 'translateY(' + (up ? 100 : -100) + '%)'; nw.style.position = 'absolute'; nw.style.left = '0'; nw.style.right = '0'; nw.style.top = '0';
    box.appendChild(nw); void nw.offsetWidth;
    old.style.transform = 'translateY(' + (up ? -100 : 100) + '%)'; nw.style.transform = 'none';
    setTimeout(function () { if (old.parentNode) old.remove(); nw.style.position = ''; }, 360);
  }
  function order() {
    var s = items.slice().sort(function (a, b) { return b.n - a.n || a.i - b.i; });
    var top0 = items.map(function (it) { return it.el.offsetTop; });
    s.forEach(function (it, k) { ls.appendChild(it.el); it.el.querySelector('.u248-rk').textContent = '#' + (k + 1); });
    if (rm) return;
    items.forEach(function (it, k) {
      var dy = top0[k] - it.el.offsetTop;
      if (!dy) return;
      it.el.style.transition = 'none'; it.el.style.transform = 'translateY(' + dy + 'px)';
      if (dy > 0) it.el.classList.add('is-mv');
      void it.el.offsetWidth;
      it.el.style.transition = 'transform .55s cubic-bezier(.3,1.25,.5,1)'; it.el.style.transform = '';
      setTimeout(function () { it.el.classList.remove('is-mv'); }, 560);
    });
  }
  function vote(it) {
    it.on = !it.on; it.n = it.base + (it.on ? 1 : 0);
    it.btn.classList.toggle('is-on', it.on); it.btn.setAttribute('aria-pressed', it.on);
    roll(it, it.on); label(it);
    if (it.on && !rm) {
      it.btn.classList.remove('is-pop'); void it.btn.offsetWidth; it.btn.classList.add('is-pop');
      var p = document.createElement('span'); p.className = 'u248-pl'; p.textContent = '+1'; p.setAttribute('aria-hidden', 'true'); it.btn.appendChild(p); setTimeout(function () { p.remove(); }, 820);
    }
    setTimeout(order, rm ? 0 : 260);
  }
  items.forEach(label); order();
})();
</script>
--- Code end ---
