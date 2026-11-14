---
source: "lucianlabs"
id: "212"
title: "Hide-on-scroll header"
category: "Navigation"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#212"
tags: ["header", "navbar", "scroll", "sticky", "navigation"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Hide-on-scroll header (212, Navigation)
[What it does] At the top, a roomy transparent header sits over the page; scroll down and it slides up out of the way to give you room to read. Scroll up even a little and it comes back down as a slim header with a blurred background and shadow, while a thin bar beneath it fills as you read. Back at the very top it turns transparent again.
[How to use it] Scroll down inside the card, then scroll up a little

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
<!-- Lucian UX/UI Prompt #212 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#212 -->
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
.u212{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u212-hd{position:absolute;left:0;right:0;top:0;z-index:2;display:flex;align-items:center;gap:12px;height:58px;padding:0 18px;font-size:11px;font-weight:750;color:var(--ux-ink-2);transition:transform .38s cubic-bezier(.2,.8,.2,1),height .3s,background-color .3s,box-shadow .3s,backdrop-filter .3s}
.u212-hd b{margin-right:auto;display:flex;align-items:center;gap:6px;font-size:13px;font-weight:900;color:var(--ux-ink)}
.u212-hd b i{width:14px;height:14px;border-radius:50%;background:var(--ux-grad)}
.u212-hd strong{padding:6px 11px;border-radius:999px;background:var(--ux-ink);color:var(--ux-surface);font-size:10.5px;font-weight:800}
.u212.is-solid .u212-hd{height:46px;background:color-mix(in srgb,var(--ux-surface) 78%,transparent);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);box-shadow:0 1px 0 var(--ux-line),0 8px 20px -14px var(--ux-shadow-strong)}
.u212.is-hide .u212-hd{transform:translateY(-110%)}
.u212-pg{position:absolute;left:0;bottom:-1px;height:2px;width:0;background:var(--ux-accent);opacity:0;transition:opacity .3s}
.u212.is-solid .u212-pg{opacity:1}
.u212-sc{position:absolute;inset:0;overflow-y:auto;overscroll-behavior:contain;scrollbar-width:none}
.u212-sc::-webkit-scrollbar{display:none}
.u212-sc:focus-visible{outline:2px solid var(--ux-accent);outline-offset:-4px;border-radius:30px}
.u212-cv{height:150px;margin:0;padding:72px 22px 0;background:linear-gradient(160deg,var(--ux-accent-soft),transparent 80%)}
.u212-cv small{font-size:10px;font-weight:800;color:var(--ux-accent)}
.u212-cv h3{margin:6px 0 0;font-size:24px;line-height:1.15;font-weight:900;letter-spacing:-.04em}
.u212-bd{padding:22px 22px 40px}
.u212-bd p{margin:0 0 14px;font-size:12.5px;line-height:1.75;font-weight:600;color:var(--ux-ink-2)}
.u212-bd i{display:block;height:84px;margin:0 0 14px;border-radius:14px;background:linear-gradient(135deg,var(--ux-surface-2),color-mix(in srgb,var(--ux-accent) 18%,var(--ux-surface)))}
@media (prefers-reduced-motion: reduce){.u212-hd{transition:none}}
</style>
<div class="ux u212">
  <header class="u212-hd"><b><i aria-hidden="true"></i>Relay</b><span>Product</span><span>Pricing</span><span>Blog</span><strong>Get started</strong><span class="u212-pg" aria-hidden="true"></span></header>
  <div class="u212-sc" tabindex="0" aria-label="Blog post"><div class="u212-cv"><small>Blog · 5 min read</small><h3>How small teams<br>ship fast</h3></div><div class="u212-bd"></div></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u212-sc'), bd = root.querySelector('.u212-bd'), pg = root.querySelector('.u212-pg');
  var P = ['If you try to make it perfect from the start, launch keeps slipping. Ship the smallest useful thing and refine it as people respond.', 'Keep meetings short and notes long. When the reason behind a decision is written down, the next person won’t repeat the same debate.', 'Automate the third time you repeat something. Automate too early and you cement what is still changing.', 'Finally, set the launch date first. A date is what lets you choose what to cut.'];
  P.forEach(function (t, i) { var p = document.createElement('p'); p.textContent = t; bd.appendChild(p); if (i === 1) bd.appendChild(document.createElement('i')); });
  var last = 0, acc = 0;
  sc.addEventListener('scroll', function () {
    var y = sc.scrollTop, d = y - last; last = y;
    acc = (d > 0) === (acc > 0) ? acc + d : d;
    root.classList.toggle('is-solid', y > 20);
    if (y < 60) root.classList.remove('is-hide');
    else if (acc > 8) root.classList.add('is-hide');
    else if (acc < -6) root.classList.remove('is-hide');
    pg.style.width = (y / Math.max(1, sc.scrollHeight - sc.clientHeight) * 100).toFixed(1) + '%';
  }, { passive: true });
})();
</script>
--- Code end ---
