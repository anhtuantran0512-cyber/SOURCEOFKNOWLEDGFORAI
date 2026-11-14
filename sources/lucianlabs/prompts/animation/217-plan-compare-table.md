---
source: "lucianlabs"
id: "217"
title: "Plan comparison with differences only"
category: "Commerce & Pricing"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#217"
tags: ["pricing", "comparison-table", "sticky-header", "filter", "saas"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Plan comparison with differences only (217, Commerce & Pricing)
[What it does] A table comparing the features of three plans row by row. The plan name row stays pinned to the top as you scroll, and resting the pointer on a cell lights up that plan's whole column and darkens its select button at the top. Turn on Differences only and rows that are the same across all three plans fold away, and groups that empty out fold along with their titles.
[How to use it] Rest the pointer on a table cell, then turn on Differences only

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
<!-- Lucian UX/UI Prompt #217 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#217 -->
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
.u217{position:relative;width:300px;height:480px;border-radius:32px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u217-tp{position:absolute;left:18px;right:16px;top:20px;display:flex;align-items:center}
.u217-tp b{margin-right:auto;font-size:17px;font-weight:900;letter-spacing:-.03em}
.u217-df{display:inline-flex;align-items:center;gap:7px;height:28px;padding:0 4px 0 10px;border:0;border-radius:999px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line);color:var(--ux-ink-2);font:inherit;font-size:10.5px;font-weight:800;cursor:pointer}
.u217-df i{position:relative;width:28px;height:18px;border-radius:9px;background:var(--ux-surface-3);transition:background .2s}
.u217-df i::after{content:"";position:absolute;left:2px;top:2px;width:14px;height:14px;border-radius:50%;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.25);transition:transform .25s cubic-bezier(.3,1.5,.5,1)}
.u217-df[aria-checked="true"] i{background:var(--ux-accent)}
.u217-df[aria-checked="true"] i::after{transform:translateX(10px)}
.u217-df:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u217-sc{position:absolute;left:0;right:0;top:62px;bottom:0;overflow-y:auto;overscroll-behavior:contain;scrollbar-width:none;padding:0 10px 20px}
.u217-sc::-webkit-scrollbar{display:none}
.u217-sc:focus-visible{outline:2px solid var(--ux-accent);outline-offset:-3px}
.u217-r{display:grid;grid-template-columns:1fr 56px 56px 56px;align-items:center}
.u217-hd{position:sticky;top:0;z-index:2;background:var(--ux-surface);padding:6px 0 8px;box-shadow:0 1px 0 var(--ux-line)}
.u217-hd>div{display:flex;flex-direction:column;align-items:center;gap:2px;position:relative;padding-top:12px}
.u217-hd b{font-size:12px;font-weight:900}
.u217-hd small{font-size:9.5px;font-weight:800;color:var(--ux-ink-3);font-variant-numeric:tabular-nums}
.u217-hd em{position:absolute;top:-1px;padding:1px 6px;border-radius:999px;background:var(--ux-accent);color:#fff;font-style:normal;font-size:8.5px;font-weight:850}
.u217-hd .u217-c>span{margin-top:4px;height:22px;padding:0 9px;border-radius:999px;box-shadow:inset 0 0 0 1px var(--ux-line);font-size:9.5px;font-weight:850;line-height:22px;color:var(--ux-ink-2);transition:background .2s,color .2s,box-shadow .2s}
.u217-gp{display:grid;grid-template-rows:1fr;transition:grid-template-rows .45s cubic-bezier(.3,.8,.3,1),opacity .3s}
.u217-gp>div{min-height:0;overflow:hidden}
.u217-gp.is-off{grid-template-rows:0fr;opacity:0}
.u217-gh{padding:14px 6px 4px;font-size:10px;font-weight:850;letter-spacing:.06em;color:var(--ux-accent)}
.u217-rw{display:grid;grid-template-rows:1fr;transition:grid-template-rows .45s cubic-bezier(.3,.8,.3,1),opacity .3s}
.u217-rw>div{min-height:0;overflow:hidden}
.u217-rw.is-off{grid-template-rows:0fr;opacity:0}
.u217-rw .u217-r{min-height:34px;border-bottom:1px solid var(--ux-line)}
.u217-r>span:first-child{padding:0 6px;font-size:11px;font-weight:700;color:var(--ux-ink-2)}
.u217-c{display:grid;place-items:center;align-self:stretch;font-size:10.5px;font-weight:800;transition:background .2s}
.u217-c svg{width:13px;height:13px}
.u217-c .y{color:#10B981}.u217-c .n{color:var(--ux-ink-3);opacity:.6}
.u217[data-col="1"] .u217-c1,.u217[data-col="2"] .u217-c2,.u217[data-col="3"] .u217-c3{background:color-mix(in srgb,var(--ux-accent) 9%,transparent)}
.u217[data-col="1"] .u217-hd .u217-c1 span,.u217[data-col="2"] .u217-hd .u217-c2 span,.u217[data-col="3"] .u217-hd .u217-c3 span{background:var(--ux-ink);color:var(--ux-surface);box-shadow:none}
.u217-hd .u217-c{border-radius:12px 12px 0 0}
@media (prefers-reduced-motion: reduce){.u217-gp,.u217-rw{transition:none}}
</style>
<div class="ux u217">
  <div class="u217-tp"><b>Compare plans</b><button type="button" class="u217-df" role="switch" aria-checked="false">Differences only<i aria-hidden="true"></i></button></div>
  <div class="u217-sc" tabindex="0" aria-label="Plan feature comparison">
    <div class="u217-r u217-hd"><span></span><div class="u217-c u217-c1"><b>Free</b><small>$0</small><span>Choose</span></div><div class="u217-c u217-c2"><em>Popular</em><b>Pro</b><small>$9</small><span>Choose</span></div><div class="u217-c u217-c3"><b>Team</b><small>$19</small><span>Choose</span></div></div>
    <div class="u217-bd"></div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var bd = root.querySelector('.u217-bd'), df = root.querySelector('.u217-df'), sc = root.querySelector('.u217-sc');
  var G = [['Basics', [['Projects', '3', 'Unlimited', 'Unlimited'], ['Storage', '5GB', '100GB', '1TB'], ['File uploads', 1, 1, 1]]], ['Collaboration', [['Live editing', 1, 1, 1], ['Comments & mentions', 1, 1, 1], ['Guest invites', 0, 1, 1], ['Team spaces', 0, 0, 1]]], ['Security', [['Two-factor auth', 1, 1, 1], ['SSO sign-in', 0, 0, 1], ['Audit logs', 0, 0, 1]]], ['Support', [['Help center', 1, 1, 1], ['Email support', 1, 1, 1]]]];
  var Y = '<svg class="y" viewBox="0 0 14 14"><path d="M3 7.5l2.6 2.6L11 4.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>', N = '<svg class="n" viewBox="0 0 14 14"><path d="M4 7h6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>';
  var groups = G.map(function (g) {
    var gp = document.createElement('div'); gp.className = 'u217-gp'; gp.innerHTML = '<div><div class="u217-gh"></div></div>';
    gp.querySelector('.u217-gh').textContent = g[0];
    var rows = g[1].map(function (f) {
      var rw = document.createElement('div'); rw.className = 'u217-rw';
      rw.innerHTML = '<div><div class="u217-r"><span></span></div></div>';
      var r = rw.querySelector('.u217-r'); r.firstChild.textContent = f[0];
      [1, 2, 3].forEach(function (k) { var c = document.createElement('span'); c.className = 'u217-c u217-c' + k; if (typeof f[k] === 'number') { c.innerHTML = f[k] ? Y : N; c.firstChild.setAttribute('role', 'img'); c.firstChild.setAttribute('aria-label', f[k] ? 'Included' : 'Not included'); } else c.textContent = f[k]; r.appendChild(c); });
      gp.firstChild.appendChild(rw);
      return { el: rw, same: f[1] === f[2] && f[2] === f[3] };
    });
    bd.appendChild(gp); return { el: gp, rows: rows };
  });
  root.addEventListener('pointermove', function (e) { var c = e.target.closest && e.target.closest('.u217-c'); root.dataset.col = c ? c.className.match(/u217-c(\d)/)[1] : ''; });
  root.addEventListener('pointerover', function (e) { var c = e.target.closest && e.target.closest('.u217-c'); root.dataset.col = c ? c.className.match(/u217-c(\d)/)[1] : ''; });
  sc.addEventListener('pointerleave', function () { root.dataset.col = ''; });
  var only = false;
  df.addEventListener('click', function () {
    only = !only; df.setAttribute('aria-checked', only);
    groups.forEach(function (g) {
      var left = 0;
      g.rows.forEach(function (r) { var off = only && r.same; r.el.classList.toggle('is-off', off); r.el.setAttribute('aria-hidden', off); if (!off) left++; });
      g.el.classList.toggle('is-off', !left); g.el.setAttribute('aria-hidden', !left);
    });
  });
})();
</script>
--- Code end ---
