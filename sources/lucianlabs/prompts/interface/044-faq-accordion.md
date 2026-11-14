---
source: "lucianlabs"
id: "044"
title: "FAQ accordion"
category: "Menus & Tabs"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#044"
tags: ["accordion", "faq", "disclosure", "expand", "keyboard"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] FAQ accordion (044, Menus & Tabs)
[What it does] Press a question and its panel lifts as the answer unfolds smoothly, while one stroke of the plus lies down to become a minus. Only one opens at a time; the rest fold away calmly.
[How to use it] Press questions to open and close them. With a keyboard, move with the up and down arrows and open with Enter

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
<!-- Lucian UX/UI Prompt #044 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#044 -->
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
.u044{position:relative;width:350px;height:400px;display:flex;flex-direction:column;gap:8px}
.u044-it{position:relative;border-radius:20px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line);transition:background-color .4s var(--ux-ease),box-shadow .5s var(--ux-ease),transform .5s var(--ux-spring)}
.u044-it.open{box-shadow:0 0 0 1px var(--ux-line-2),0 22px 40px -22px var(--ux-shadow-strong);transform:translateY(-2px)}
.u044-q{position:relative;display:flex;align-items:center;gap:12px;width:100%;min-height:58px;padding:0 14px 0 16px;border:0;border-radius:20px;background:none;font-size:14.5px;font-weight:680;letter-spacing:-.02em;color:var(--ux-ink);text-align:left}
.u044-q:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u044-n{font-size:12px;font-weight:800;color:var(--ux-ink-3);font-variant-numeric:tabular-nums;transition:color .3s}
.u044-it.open .u044-n{color:var(--ux-accent)}
.u044-t{flex:1}
.u044-pm{position:relative;width:30px;height:30px;flex:none;border-radius:50%;background:var(--ux-surface-2);box-shadow:none;transition:background-color .35s var(--ux-ease),box-shadow .35s,transform .45s var(--ux-spring)}
.u044-q:hover .u044-pm{transform:scale(1.1)}
.u044-q:active .u044-pm{transform:scale(.9)}
.u044-pm::before,.u044-pm::after{content:"";position:absolute;left:50%;top:50%;width:11px;height:2px;margin:-1px 0 0 -5.5px;border-radius:2px;background:var(--ux-ink);transition:transform .5s var(--ux-spring),background-color .3s}
.u044-pm::after{transform:rotate(90deg)}
.u044-it.open .u044-pm{background:var(--ux-ink);box-shadow:none}
.u044-it.open .u044-pm::before,.u044-it.open .u044-pm::after{background:var(--ux-page)}
.u044-it.open .u044-pm::after{transform:rotate(180deg)}
.u044-body{display:grid;grid-template-rows:0fr;transition:grid-template-rows .5s var(--ux-ease)}
.u044-it.open .u044-body{grid-template-rows:1fr}
.u044-body>div{overflow:hidden;min-height:0}
.u044-a{padding:0 18px 16px 42px;opacity:0;transform:translateY(-8px);transition:opacity .25s var(--ux-ease),transform .45s var(--ux-spring)}
.u044-it.open .u044-a{opacity:1;transform:none;transition-delay:.12s}
.u044-a p{margin:0;font-size:13.5px;line-height:1.62;color:var(--ux-ink-2)}
.u044-a a{display:inline-flex;align-items:center;gap:4px;margin-top:10px;font-size:13px;font-weight:700;color:var(--ux-accent);text-decoration:none}
.u044-a a:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px;border-radius:4px}
.u044-a a i{font-style:normal;transition:transform .3s var(--ux-spring)}
.u044-a a:hover i{transform:translateX(3px)}
</style>
<div class="ux u044">
  <div class="u044-it open">
    <button class="u044-q" type="button" aria-expanded="true"><span class="u044-n">01</span><span class="u044-t">Can I cancel anytime?</span><span class="u044-pm" aria-hidden="true"></span></button>
    <div class="u044-body" role="region"><div><div class="u044-a"><p>Yes — cancel right from Billing in Settings. You keep access until your next billing date.</p><a href="#">How to cancel <i aria-hidden="true">→</i></a></div></div></div>
  </div>
  <div class="u044-it">
    <button class="u044-q" type="button" aria-expanded="false"><span class="u044-n">02</span><span class="u044-t">How many people can I invite?</span><span class="u044-pm" aria-hidden="true"></span></button>
    <div class="u044-body" role="region"><div><div class="u044-a"><p>The Team plan allows up to 40 people. Added seats apply from your next bill.</p><a href="#">Compare plans <i aria-hidden="true">→</i></a></div></div></div>
  </div>
  <div class="u044-it">
    <button class="u044-q" type="button" aria-expanded="false"><span class="u044-n">03</span><span class="u044-t">Where are my files saved?</span><span class="u044-pm" aria-hidden="true"></span></button>
    <div class="u044-body" role="region"><div><div class="u044-a"><p>Everything saves to its project automatically, and you can restore versions for 30 days.</p><a href="#">About version history <i aria-hidden="true">→</i></a></div></div></div>
  </div>
  <div class="u044-it">
    <button class="u044-q" type="button" aria-expanded="false"><span class="u044-n">04</span><span class="u044-t">Is there a student discount?</span><span class="u044-pm" aria-hidden="true"></span></button>
    <div class="u044-body" role="region"><div><div class="u044-a"><p>Verify with a school email and get Pro free for a year.</p><a href="#">Verify student status <i aria-hidden="true">→</i></a></div></div></div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var items = Array.prototype.slice.call(root.querySelectorAll('.u044-it'));
  var qs = items.map(function (it) { return it.querySelector('.u044-q'); });
  var uid = 'u044-' + Math.random().toString(36).slice(2, 7);
  items.forEach(function (it, i) {
    var q = qs[i], body = it.querySelector('.u044-body');
    q.id = uid + '-q' + i; body.id = uid + '-a' + i;
    q.setAttribute('aria-controls', body.id); body.setAttribute('aria-labelledby', q.id);
  });
  function set(it, open) {
    it.classList.toggle('open', open);
    it.querySelector('.u044-q').setAttribute('aria-expanded', String(open));
    it.querySelector('.u044-a a').tabIndex = open ? 0 : -1;
  }
  items.forEach(function (it, i) {
    set(it, it.classList.contains('open'));
    qs[i].addEventListener('click', function () {
      var willOpen = !it.classList.contains('open');
      items.forEach(function (o) { if (o !== it) set(o, false); });
      set(it, willOpen);
    });
    qs[i].addEventListener('keydown', function (e) {
      var n = e.key === 'ArrowDown' ? i + 1 : e.key === 'ArrowUp' ? i - 1 : e.key === 'Home' ? 0 : e.key === 'End' ? qs.length - 1 : -2;
      if (n === -2) return;
      e.preventDefault();
      qs[(n + qs.length) % qs.length].focus();
    });
    it.querySelector('.u044-a a').addEventListener('click', function (e) { e.preventDefault(); });
  });
})();
</script>
--- Code end ---
