---
source: "lucianlabs"
id: "180"
title: "Approval sign-off line"
category: "Workflow & Systems"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#180"
tags: ["approval-signoff", "new-century"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Approval sign-off line (180, Workflow & Systems)
[What it does] An approval line that collects three signatures in order: drafted, reviewed, approved. Each press stamps the next box, and after final approval you can start over.
[How to use it] Press the approve button step by step

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
<!-- Lucian UX/UI Prompt #180 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#180 -->
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
.u180 {width:100%;max-width:370px;font-size:14px;line-height:1.45;position:relative;--a:#cd5339;--soft:color-mix(in srgb,var(--a) 12%,var(--ux-surface));font-variant-numeric:tabular-nums}
.u180 button{border:1px solid var(--ux-line-2);background:var(--ux-surface);border-radius:9px;padding:9px 12px;min-height:38px;transition:background .2s,transform .3s,color .2s;color:var(--ux-ink)}
.u180 button:active{transform:translateY(1px)}.u180 button:disabled{opacity:.4;cursor:default}.u180 button.primary{background:var(--ux-ink);color:var(--ux-page);border-color:transparent}
.u180 .muted{color:var(--ux-ink-2);font-size:12px}.u180 .eyebrow{font:600 10px/1.2 ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--ux-ink-2)}
.u180 .row{display:flex;align-items:center;justify-content:space-between;gap:8px}.u180 .actions{display:flex;gap:8px;align-items:center;margin-top:16px;flex-wrap:wrap}
.u180 input,.u180 select{max-width:100%;min-width:0;background:var(--ux-surface);color:var(--ux-ink);border:1px solid var(--ux-line-2);border-radius:7px;padding:8px;font:inherit}
.u180 output{font-variant-numeric:tabular-nums}.u180 :focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
@media(prefers-reduced-motion:reduce){.u180 *,.u180 *::before,.u180 *::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
.u180 .paper{background:var(--ux-surface);border:1px solid var(--ux-line-2);padding:23px 20px 18px;position:relative;border-radius:3px;box-shadow:5px 5px 0 var(--ux-surface-3)}.u180 .paper h3{font-size:24px;letter-spacing:-1px;margin:6px 0 2px}.u180 .signs{display:flex;margin:24px 0 18px;border:1px solid var(--ux-line-2)}.u180 .person{width:33.33%;text-align:center;padding:10px 2px;position:relative;border-right:1px solid var(--ux-line-2)}.u180 .person:last-child{border:0}.u180 .person small{display:block;font-size:11px;color:var(--ux-ink-2)}.u180 .seal{display:grid;place-items:center;width:55px;height:55px;margin:10px auto 0;border:2px dashed var(--ux-line-2);border-radius:50%;font:16px Georgia,serif;color:var(--ux-ink-2);transition:transform .45s,background .35s,color .35s}.u180 .person.done .seal{border:2px solid light-dark(#b44335,#ff9b85);color:light-dark(#b44335,#ff9b85);transform:rotate(-12deg);background:color-mix(in srgb,#b44335 8%,transparent)}.u180 .person.done .seal::after{content:'✓';margin-left:3px}.u180 .actions{justify-content:space-between;margin-top:12px}.u180 .reset{background:none;border:0;padding:5px;font-size:12px}

/* Focused composition */
.u180{max-width:320px}.u180 .paper{padding:24px 19px 20px;box-shadow:4px 4px 0 var(--ux-surface-3)}.u180 .paper h3{font-size:19px;margin:0;font-weight:550}.u180 .signs{margin:22px 0;border:0}.u180 .person{border-right:1px solid var(--ux-line);padding:0 3px}.u180 .seal{width:52px;height:52px;font-size:15px}.u180 .approve{display:block;margin:auto;min-width:135px;font-size:12px}</style>
<div class="ux u180" data-state="initial"><div class="paper"><h3>Brand draft</h3><div class="signs"><div class="person done"><small>Draft</small><div class="seal">Seoyeon</div></div><div class="person"><small>Review</small><div class="seal">Minho</div></div><div class="person"><small>Approve</small><div class="seal">Jisoo</div></div></div><button class="approve primary">Approve review</button></div></div>

<script>
(()=>{const root=document.currentScript.previousElementSibling;const q=s=>root.querySelector(s),qa=s=>[...root.querySelectorAll(s)];const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;const state=s=>root.dataset.state=s;const pulse=(el,frames,duration=450)=>{if(!reduced)el.animate(frames,{duration,easing:'cubic-bezier(.2,.8,.2,1)'});};let n=1;function render(){qa('.person').forEach((p,i)=>p.classList.toggle('done',i<n));q('.approve').textContent=n===1?'Approve review':n===2?'Final approval':'Approved · Reset';state('approved-'+n)}q('.approve').onclick=()=>{n=n===3?1:n+1;render();pulse(qa('.seal')[n-1],[{transform:'rotate(-25deg) scale(1.35)',opacity:.2},{transform:'rotate(-12deg) scale(1)',opacity:1}])};})();
</script>
--- Code end ---
