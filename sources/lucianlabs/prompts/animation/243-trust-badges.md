---
source: "lucianlabs"
id: "243"
title: "Tap-to-verify security badges"
category: "Social Proof"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#243"
tags: ["trust", "security", "badges", "compliance", "saas"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Tap-to-verify security badges (243, Social Proof)
[What it does] A row of security and compliance badges at the bottom of a product page gets a passing sheen now and then. Press a badge and the card flips to show the certifying body, scope and validity; press Verify and a ring spins before a green check stamps the time it was checked. Press again to flip back.
[How to use it] Press a badge to flip it, then press Verify

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
<!-- Lucian UX/UI Prompt #243 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#243 -->
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
.u243{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u243-hd{position:absolute;left:20px;right:20px;top:24px}
.u243-hd b{display:block;font-size:17px;font-weight:900;letter-spacing:-.03em}
.u243-hd small{display:block;margin-top:4px;font-size:11px;font-weight:650;color:var(--ux-ink-3)}
.u243-gd{position:absolute;left:14px;right:14px;top:84px;bottom:14px;display:grid;grid-template-columns:1fr 1fr;gap:8px;perspective:700px}
.u243-bg{position:relative;padding:0;border:0;background:none;font:inherit;color:inherit;cursor:pointer;transform-style:preserve-3d;transition:transform .6s cubic-bezier(.3,1.2,.4,1)}
.u243-bg.is-flip{transform:rotateY(180deg)}
.u243-bg:focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px;border-radius:16px}
.u243-f,.u243-b{position:absolute;inset:0;border-radius:16px;backface-visibility:hidden;-webkit-backface-visibility:hidden;overflow:hidden}
.u243-f{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line)}
.u243-f::after{content:"";position:absolute;top:0;bottom:0;left:-60%;width:40%;background:linear-gradient(105deg,transparent,rgba(255,255,255,.55),transparent);transform:skewX(-12deg);animation:u243-sh 5.5s ease-in-out infinite;animation-delay:var(--d)}
@keyframes u243-sh{0%,70%{left:-60%}90%,100%{left:130%}}
.u243-sd{width:42px;height:46px;display:grid;place-items:center;color:var(--c)}
.u243-sd svg{width:42px;height:46px}
.u243-f b{font-size:13px;font-weight:900;letter-spacing:-.01em}
.u243-f small{font-size:9.5px;font-weight:750;color:var(--ux-ink-3)}
.u243-b{transform:rotateY(180deg);display:flex;flex-direction:column;padding:11px 12px;text-align:left;background:var(--ux-surface);box-shadow:inset 0 0 0 1.5px var(--c)}
.u243-b b{font-size:12px;font-weight:900}
.u243-b span{margin-top:3px;font-size:10px;line-height:1.4;font-weight:700;color:var(--ux-ink-2)}
.u243-b small{margin-top:2px;font-size:9.5px;font-weight:650;color:var(--ux-ink-3)}
.u243-vf{display:inline-flex;align-items:center;gap:5px;align-self:flex-start;height:26px;margin-top:auto;padding:0 10px;border:0;border-radius:8px;background:var(--ux-ink);color:var(--ux-surface);font:inherit;font-size:10px;font-weight:850;cursor:pointer}
.u243-vf i{display:none;width:11px;height:11px;border-radius:50%;border:2px solid color-mix(in srgb,var(--ux-surface) 35%,transparent);border-top-color:var(--ux-surface);animation:u243-sp .7s linear infinite}
.u243-vf.is-busy i{display:block}
.u243-vf.is-ok{background:#059669}
@keyframes u243-sp{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion: reduce){.u243-bg{transition:none}.u243-f::after,.u243-vf i{animation:none}}
</style>
<div class="ux u243">
  <div class="u243-hd"><b>Why you can trust us</b><small>Customer data is protected to international standards</small></div>
  <div class="u243-gd"></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var gd = root.querySelector('.u243-gd');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var BG = [['ISO 27001', 'Info security', 'Certified by ISO', 'All services · until Mar 2027'], ['SOC 2', 'Security & uptime', 'Type II audit report', 'Audited externally every year'], ['GDPR', 'Privacy', 'EU privacy rules', 'DPA available'], ['ISMS-P', 'Korean infosec', 'Certified by KISA', 'Until Nov 2026']];
  var COL = ['#2563EB', '#7C3AED', '#0D9488', '#E11D48'];
  var SHIELD = '<svg viewBox="0 0 42 46" aria-hidden="true"><path d="M21 3l15 5.5v11.5c0 11-6.6 18.8-15 22.5C12.6 38.8 6 31 6 20V8.5z" fill="color-mix(in srgb,currentColor 14%,transparent)" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/><path d="M14.5 22.5l4.5 4.5 9-9.5" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  BG.forEach(function (g, i) {
    var b = document.createElement('div'); b.className = 'u243-bg'; b.style.setProperty('--c', COL[i]); b.style.setProperty('--d', (i * 1.1) + 's'); b.tabIndex = 0; b.setAttribute('role', 'button'); b.setAttribute('aria-pressed', 'false'); b.setAttribute('aria-label', g[0] + ' — details');
    b.innerHTML = '<div class="u243-f"><span class="u243-sd">' + SHIELD + '</span><b></b><small></small></div><div class="u243-b"><b></b><span></span><small></small><button type="button" class="u243-vf" tabindex="-1"><i aria-hidden="true"></i><em style="font-style:normal"></em></button></div>';
    b.querySelector('.u243-f b').textContent = g[0]; b.querySelector('.u243-f small').textContent = g[1];
    b.querySelector('.u243-b b').textContent = g[0]; b.querySelector('.u243-b span').textContent = g[2]; b.querySelector('.u243-b small').textContent = g[3];
    var vf = b.querySelector('.u243-vf'), vl = vf.querySelector('em'); vl.textContent = 'Verify';
    function flip() { var on = !b.classList.contains('is-flip'); b.classList.toggle('is-flip', on); b.setAttribute('aria-pressed', on); vf.tabIndex = on ? 0 : -1; }
    b.addEventListener('click', function (e) { if (e.target.closest('.u243-vf')) return; flip(); });
    b.addEventListener('keydown', function (e) { if ((e.key === 'Enter' || e.key === ' ') && e.target === b) { e.preventDefault(); flip(); } });
    vf.addEventListener('click', function (e) {
      e.stopPropagation(); if (vf.classList.contains('is-busy') || vf.classList.contains('is-ok')) return;
      vf.classList.add('is-busy'); vl.textContent = 'Checking…';
      setTimeout(function () { vf.classList.remove('is-busy'); vf.classList.add('is-ok'); vl.textContent = 'Valid · just checked'; }, rm ? 0 : 900);
    });
    gd.appendChild(b);
  });
})();
</script>
--- Code end ---
