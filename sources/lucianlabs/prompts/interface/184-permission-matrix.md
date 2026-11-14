---
source: "lucianlabs"
id: "184"
title: "Role permission matrix"
category: "Workflow & Systems"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#184"
tags: ["permission-matrix", "new-century"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Role permission matrix (184, Workflow & Systems)
[What it does] A permissions table for switching view, edit and share on or off for each role. Press a cell to flip that permission; the owner’s essential rights are locked on.
[How to use it] Press a cell in the Editor or Guest row to change a permission

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
<!-- Lucian UX/UI Prompt #184 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#184 -->
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
.u184 {width:100%;max-width:370px;font-size:14px;line-height:1.45;position:relative;--a:#cd5339;--soft:color-mix(in srgb,var(--a) 12%,var(--ux-surface));font-variant-numeric:tabular-nums}
.u184 button{border:1px solid var(--ux-line-2);background:var(--ux-surface);border-radius:9px;padding:9px 12px;min-height:38px;transition:background .2s,transform .3s,color .2s;color:var(--ux-ink)}
.u184 button:active{transform:translateY(1px)}.u184 button:disabled{opacity:.4;cursor:default}.u184 button.primary{background:var(--ux-ink);color:var(--ux-page);border-color:transparent}
.u184 .muted{color:var(--ux-ink-2);font-size:12px}.u184 .eyebrow{font:600 10px/1.2 ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--ux-ink-2)}
.u184 .row{display:flex;align-items:center;justify-content:space-between;gap:8px}.u184 .actions{display:flex;gap:8px;align-items:center;margin-top:16px;flex-wrap:wrap}
.u184 input,.u184 select{max-width:100%;min-width:0;background:var(--ux-surface);color:var(--ux-ink);border:1px solid var(--ux-line-2);border-radius:7px;padding:8px;font:inherit}
.u184 output{font-variant-numeric:tabular-nums}.u184 :focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
@media(prefers-reduced-motion:reduce){.u184 *,.u184 *::before,.u184 *::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
.u184 .matrix{width:100%;border-collapse:collapse;margin:22px 0 16px;table-layout:fixed}.u184 th{font-size:11px;color:var(--ux-ink-2);font-weight:500;text-align:center;padding-bottom:12px}.u184 th:first-child{text-align:left;width:28%}.u184 td{border-top:1px solid var(--ux-line);text-align:center;padding:11px 0;font-size:12px}.u184 td:first-child{text-align:left;font-weight:650}.u184 .cell{height:37px;width:37px;min-height:37px;padding:0;border-radius:50%;font-size:17px;background:var(--ux-surface-2)}.u184 .cell[aria-pressed=true]{background:light-dark(#dfe9d6,#2b4435);color:light-dark(#32552c,#d2e9ba);border-color:transparent;transform:scale(.96)}.u184 .cell[disabled]{opacity:1;border-style:dashed;border-color:var(--ux-line-2);background:none;font-size:12px}.u184 .footer{display:flex;justify-content:space-between;font-size:11px;color:var(--ux-ink-2);border-top:1px solid var(--ux-line-2);padding-top:14px}.u184 .reset{border:0;background:none;min-height:25px;font-size:11px;padding:0 5px}

/* Focused composition */
.u184{max-width:320px}.u184 .matrix{margin:0;border-collapse:separate;border-spacing:0 7px}.u184 td{padding:8px 0;border-top-color:var(--ux-line)}.u184 th{font-size:12px;padding-bottom:6px}.u184 td:first-child{font-size:13px;font-weight:500}.u184 .cell{border:0;background:none;width:39px;height:39px;min-height:39px}.u184 .cell[disabled]{color:var(--ux-ink-2);border:0;font-size:17px;opacity:.55}.u184 .cell[aria-pressed=true]:not([disabled]){box-shadow:none}</style>
<div class="ux u184" data-state="initial"><table class="matrix"><thead><tr><th>Role</th><th>View</th><th>Edit</th><th>Share</th></tr></thead><tbody><tr><td>Owner</td><td><button class="cell" data-r="0" data-c="0" aria-label="Owner View" aria-pressed="true" disabled>✓</button></td><td><button class="cell" data-r="0" data-c="1" aria-label="Owner Edit" aria-pressed="true" disabled>✓</button></td><td><button class="cell" data-r="0" data-c="2" aria-label="Owner Share" aria-pressed="true" disabled>✓</button></td></tr><tr><td>Editor</td><td><button class="cell" data-r="1" data-c="0" aria-label="Editor View" aria-pressed="true" >✓</button></td><td><button class="cell" data-r="1" data-c="1" aria-label="Editor Edit" aria-pressed="false" >−</button></td><td><button class="cell" data-r="1" data-c="2" aria-label="Editor Share" aria-pressed="false" >−</button></td></tr><tr><td>Guest</td><td><button class="cell" data-r="2" data-c="0" aria-label="Guest View" aria-pressed="true" >✓</button></td><td><button class="cell" data-r="2" data-c="1" aria-label="Guest Edit" aria-pressed="false" >−</button></td><td><button class="cell" data-r="2" data-c="2" aria-label="Guest Share" aria-pressed="false" >−</button></td></tr></tbody></table></div>

<script>
(()=>{const root=document.currentScript.previousElementSibling;const q=s=>root.querySelector(s),qa=s=>[...root.querySelectorAll(s)];const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;const state=s=>root.dataset.state=s;const pulse=(el,frames,duration=450)=>{if(!reduced)el.animate(frames,{duration,easing:'cubic-bezier(.2,.8,.2,1)'});};qa('.cell:not([disabled])').forEach(b=>b.onclick=()=>{const on=b.getAttribute('aria-pressed')!=='true';b.setAttribute('aria-pressed',on);b.textContent=on?'✓':'−';state('permission-'+b.dataset.r+'-'+b.dataset.c+'-'+on)});})();
</script>
--- Code end ---
