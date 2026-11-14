---
source: "lucianlabs"
id: "143"
title: "Calculating cells"
category: "Document & Data Editing"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#143"
tags: ["spreadsheet-cells", "editing", "interactive"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Calculating cells (143, Document & Data Editing)
[What it does] A tiny sheet where editing a number recalculates the totals right away. Each column sum and the grand total update together.
[How to use it] Click a number cell and change its value

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
<!-- Lucian UX/UI Prompt #143 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#143 -->
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
.u143{width:min(100%,370px);font-size:14px;line-height:1.6;color:var(--ux-ink)}.u143 button,.u143 input,.u143 textarea,.u143 select{font:inherit;color:inherit;max-width:100%;min-width:0}.u143 button{cursor:pointer;min-height:44px;border:1px solid var(--ux-line-2);border-radius:8px;background:var(--ux-surface);padding:8px 12px}.u143 input,.u143 textarea,.u143 select{border:1px solid var(--ux-line-2);border-radius:6px;background:var(--ux-surface);padding:8px 10px}.u143 .quiet{color:var(--ux-ink-2)}.u143 .primary{background:var(--ux-accent);color:var(--ux-accent-ink);border-color:transparent}.u143 .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}.u143 [hidden]{display:none!important}.u143 :focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}@media(prefers-reduced-motion:reduce){.u143 *{animation:none!important;transition:none!important}}
.u143{background:var(--ux-surface);border-radius:4px;overflow:hidden;border:1px solid var(--ux-line-2)}.u143 table{border-collapse:collapse;width:100%;table-layout:fixed}.u143 th,.u143 td{border:1px solid var(--ux-line);height:47px;padding:0;text-align:center}.u143 th{background:var(--ux-surface-2);font-weight:500;color:var(--ux-ink-2);font-size:12px}.u143 th:first-child{width:32px}.u143 td input{width:100%;height:47px;border:0;border-radius:0;background:transparent;text-align:right;padding:8px 13px;font:15px ui-monospace,monospace;appearance:textfield}.u143 input::-webkit-inner-spin-button{appearance:none}.u143 input:focus-visible{outline-offset:-3px;background:var(--ux-accent-soft)}.u143 .sum{font:700 16px ui-monospace,monospace;color:var(--ux-accent);background:var(--ux-accent-soft)}.u143 tfoot td{padding-right:14px;text-align:right;font:14px ui-monospace,monospace}.u143 tfoot strong{padding-left:12px}
</style>
<div class="ux u143"><table aria-label="Small budget sheet"><thead><tr><th></th><th>A · Prep</th><th>B · Run</th></tr></thead><tbody><tr><th>1</th><td><input data-cell="0" type="number" value="120" aria-label="A1 value"></td><td><input data-cell="1" type="number" value="80" aria-label="B1 value"></td></tr><tr><th>2</th><td><input data-cell="2" type="number" value="60" aria-label="A2 value"></td><td><input data-cell="3" type="number" value="40" aria-label="B2 value"></td></tr><tr><th>Σ</th><td class="sum" data-colsum="0"></td><td class="sum" data-colsum="1"></td></tr></tbody><tfoot><tr><td colspan="3"><span class="quiet">SUM</span><strong data-total></strong></td></tr></tfoot></table></div>

<script>
(()=>{const root=document.currentScript.previousElementSibling,$=s=>root.querySelector(s),$$=s=>[...root.querySelectorAll(s)],esc=v=>String(v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));const motion=(node,frames,opts={})=>{if(node?.animate&&!matchMedia('(prefers-reduced-motion:reduce)').matches)node.animate(frames,{duration:220,easing:'cubic-bezier(.2,.8,.2,1)',...opts})};function render(){const v=$$('[data-cell]').map(x=>+x.value||0);$('[data-total]').textContent=v.reduce((a,b)=>a+b,0);$$('[data-colsum]').forEach(x=>x.textContent=v[+x.dataset.colsum]+v[+x.dataset.colsum+2])}$$('input').forEach(i=>{i.oninput=()=>{render();$$('.sum').forEach(o=>motion(o,[{transform:'scale(.96)'},{transform:'scale(1)'}]))};i.onkeydown=e=>{const ix=+i.dataset.cell,delta={ArrowRight:1,ArrowLeft:-1,ArrowDown:2,ArrowUp:-2}[e.key];if(delta!==undefined){e.preventDefault();$('[data-cell="'+Math.max(0,Math.min(3,ix+delta))+'"]').focus()}}});render();})();
</script>
--- Code end ---
