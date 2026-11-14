---
source: "lucianlabs"
id: "016"
title: "Star rating"
category: "Toggles & Pickers"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#016"
tags: ["rating", "stars", "hover", "feedback", "radio"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Star rating (016, Toggles & Pickers)
[What it does] Stars fill in ahead of time as far as the cursor goes, and when you press they pop up one after another from the left with a sparkle. A matching word and color change with the score.
[How to use it] Move over the stars and press to rate. Arrow keys work too

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
<!-- Lucian UX/UI Prompt #016 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#016 -->
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
.u016{--gold:linear-gradient(160deg,#FFD66B,#FFAA2C 60%,#FF7A45);position:relative;width:330px;height:220px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px}
.u016-q{margin:0;font-size:15px;font-weight:650;color:var(--ux-ink-2)}
.u016-stars{display:flex;gap:6px;border-radius:16px}
.u016-stars:focus-visible{outline:2px solid var(--ux-accent);outline-offset:6px}
.u016-s{position:relative;width:52px;height:52px;padding:0;border:0;background:none;transition:transform .35s var(--ux-spring)}
.u016-s svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.u016-s .bg{fill:var(--ux-surface-3);stroke:var(--ux-line-2);stroke-width:1}
.u016-s .fg{fill:url(#u016-g);transform-origin:50% 55%;transform:scale(0);transition:transform .4s var(--ux-spring)}
.u016-s.is-pre .fg{transform:scale(.72);opacity:.55}
.u016-s.is-on .fg{transform:scale(1);opacity:1}
.u016-s:hover{transform:scale(1.12) rotate(-6deg)}
.u016-s.is-pop{animation:u016-pop .55s var(--ux-spring)}
@keyframes u016-pop{0%{transform:scale(1)}35%{transform:scale(1.32) rotate(12deg)}100%{transform:scale(1)}}
.u016-s i{position:absolute;left:50%;top:50%;width:6px;height:6px;margin:-3px;border-radius:50%;background:#FFB547;opacity:0;pointer-events:none}
.u016-s.is-pop i{animation:u016-spark .6s var(--ux-ease) forwards}
@keyframes u016-spark{0%{opacity:1;transform:rotate(var(--a)) translateY(-14px) scale(1)}100%{opacity:0;transform:rotate(var(--a)) translateY(-40px) scale(.3)}}
.u016-out{display:flex;align-items:baseline;gap:10px;height:40px}
.u016-score{font-size:34px;font-weight:800;letter-spacing:-.04em;font-variant-numeric:tabular-nums;transition:color .4s var(--ux-ease)}
.u016-word{position:relative;height:24px;width:132px;overflow:hidden;font-size:16px;font-weight:700}
.u016-word span{position:absolute;left:0;top:0;line-height:24px;white-space:nowrap;transition:transform .5s var(--ux-spring),opacity .3s var(--ux-ease)}
</style>
<div class="ux u016">
  <p class="u016-q">How was your order?</p>
  <div class="u016-stars" role="slider" tabindex="0" aria-label="Rating" aria-valuemin="0" aria-valuemax="5" aria-valuenow="0" aria-valuetext="Not rated">
    <svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><linearGradient id="u016-g" x1="0" y1="0" x2=".6" y2="1"><stop offset="0" stop-color="#FFD66B"/><stop offset=".6" stop-color="#FFAA2C"/><stop offset="1" stop-color="#FF7A45"/></linearGradient></defs></svg>
  </div>
  <div class="u016-out" aria-hidden="true"><span class="u016-score">0.0</span><span class="u016-word"><span>Tap a star to rate</span></span></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var wrap = root.querySelector('.u016-stars');
  var score = root.querySelector('.u016-score');
  var word = root.querySelector('.u016-word');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var gid = 'u016-g-' + Math.random().toString(36).slice(2, 7);
  root.querySelector('linearGradient').id = gid;
  var WORDS = ['Tap a star to rate', 'Poor', 'Fair', 'Good', 'Great', 'Excellent'];
  var COLORS = ['var(--ux-ink-3)', '#E5484D', '#F07A3E', '#E8A317', '#2FB37A', '#7B61FF'];
  var STAR = 'M26 4.5l6.4 13.2 14.4 2-10.5 10.1 2.6 14.3L26 37.3l-12.9 6.8 2.6-14.3L5.2 19.7l14.4-2z';
  var stars = [];
  for (var i = 0; i < 5; i++) {
    var b = document.createElement('span');
    b.className = 'u016-s';
    var sparks = '';
    for (var k = 0; k < 5; k++) sparks += '<i style="--a:' + (k * 72) + 'deg"></i>';
    b.innerHTML = '<svg viewBox="0 0 52 52"><path class="bg" d="' + STAR + '" stroke-linejoin="round"/><path class="fg" d="' + STAR + '" style="fill:url(#' + gid + ')"/></svg>' + sparks;
    b.dataset.v = i + 1;
    wrap.appendChild(b);
    stars.push(b);
  }
  var val = 0;
  function preview(n) { stars.forEach(function (s, i) { s.classList.toggle('is-pre', i < n && i >= val); }); }
  function setWord(n) {
    var old = word.lastElementChild;
    var s = document.createElement('span');
    s.textContent = WORDS[n];
    s.style.color = COLORS[n];
    s.style.transform = 'translateY(100%)'; s.style.opacity = '0';
    word.appendChild(s);
    void s.offsetWidth;
    s.style.transform = 'none'; s.style.opacity = '1';
    old.style.transform = 'translateY(-100%)'; old.style.opacity = '0';
    setTimeout(function () { old.remove(); }, 500);
  }
  function set(n) {
    if (n === val) return;
    var prev = val;
    val = n;
    stars.forEach(function (s, i) {
      var on = i < n;
      s.classList.remove('is-pre');
      if (on && i >= prev) {
        setTimeout(function () {
          if (!root.isConnected) return;
          s.classList.add('is-on');
          if (!rm) { s.classList.remove('is-pop'); void s.offsetWidth; s.classList.add('is-pop'); }
        }, rm ? 0 : (i - prev) * 70);
      } else if (!on) s.classList.remove('is-on', 'is-pop');
    });
    score.textContent = n.toFixed(1);
    score.style.color = n ? COLORS[n] : '';
    setWord(n);
    wrap.setAttribute('aria-valuenow', String(n));
    wrap.setAttribute('aria-valuetext', n ? n + ' stars, ' + WORDS[n] : 'Not rated');
  }
  stars.forEach(function (s) {
    s.addEventListener('pointerenter', function () { preview(+s.dataset.v); });
    s.addEventListener('click', function () { set(+s.dataset.v); });
  });
  wrap.addEventListener('pointerleave', function () { preview(0); });
  wrap.addEventListener('keydown', function (e) {
    var d = { ArrowRight: 1, ArrowUp: 1, ArrowLeft: -1, ArrowDown: -1 }[e.key];
    if (e.key === 'Home') { e.preventDefault(); set(0); }
    if (e.key === 'End') { e.preventDefault(); set(5); }
    if (d) { e.preventDefault(); set(Math.max(0, Math.min(5, val + d))); }
    if (/^[0-5]$/.test(e.key)) set(+e.key);
  });
})();
</script>
--- Code end ---
