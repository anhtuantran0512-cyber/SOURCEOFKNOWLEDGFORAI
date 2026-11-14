---
source: "lucianlabs"
id: "200"
title: "Folding receipt"
category: "Workflow & Systems"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#200"
tags: ["receipt-fold", "new-century"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Folding receipt (200, Workflow & Systems)
[What it does] A receipt folded down to just its total. Press details and the paper unfolds to show the items and VAT; press again to fold it back.
[How to use it] Press “Details” to unfold the receipt

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
<!-- Lucian UX/UI Prompt #200 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#200 -->
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
.u200 {width:100%;max-width:370px;font-size:14px;line-height:1.45;position:relative;--a:#cd5339;--soft:color-mix(in srgb,var(--a) 12%,var(--ux-surface));font-variant-numeric:tabular-nums}
.u200 button{border:1px solid var(--ux-line-2);background:var(--ux-surface);border-radius:9px;padding:9px 12px;min-height:38px;transition:background .2s,transform .3s,color .2s;color:var(--ux-ink)}
.u200 button:active{transform:translateY(1px)}.u200 button:disabled{opacity:.4;cursor:default}.u200 button.primary{background:var(--ux-ink);color:var(--ux-page);border-color:transparent}
.u200 .muted{color:var(--ux-ink-2);font-size:12px}.u200 .eyebrow{font:600 10px/1.2 ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--ux-ink-2)}
.u200 .row{display:flex;align-items:center;justify-content:space-between;gap:8px}.u200 .actions{display:flex;gap:8px;align-items:center;margin-top:16px;flex-wrap:wrap}
.u200 input,.u200 select{max-width:100%;min-width:0;background:var(--ux-surface);color:var(--ux-ink);border:1px solid var(--ux-line-2);border-radius:7px;padding:8px;font:inherit}
.u200 output{font-variant-numeric:tabular-nums}.u200 :focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
@media(prefers-reduced-motion:reduce){.u200 *,.u200 *::before,.u200 *::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
.u200 .receipt{max-width:302px;margin:auto;background:#f4edda;color:#3d3c31;padding:16px 23px 22px;position:relative;filter:drop-shadow(0 9px 9px #0002);clip-path:polygon(0 0,100% 0,100% 97%,95% 100%,90% 97%,85% 100%,80% 97%,75% 100%,70% 97%,65% 100%,60% 97%,55% 100%,50% 97%,45% 100%,40% 97%,35% 100%,30% 97%,25% 100%,20% 97%,15% 100%,10% 97%,5% 100%,0 97%)}.u200 .receipt h3{font:italic 27px/.95 Georgia;text-align:center;margin:1px 0 10px}.u200 .receipt .meta{text-align:center;font:9px ui-monospace;letter-spacing:1px;color:#5d5b4f;padding-bottom:9px;border-bottom:1px dashed #969383}.u200 .total{display:flex;align-items:center;justify-content:space-between;margin-top:10px;font:11px ui-monospace}.u200 .total strong{font:24px Georgia;letter-spacing:-1px}.u200 .fold{display:grid;grid-template-rows:0fr;transition:grid-template-rows .45s cubic-bezier(.22,1,.36,1);transform-origin:top}.u200 .fold-inner{overflow:hidden;min-height:0}.u200 .receipt.expanded .fold{grid-template-rows:1fr}.u200 .line{display:flex;justify-content:space-between;font:11px/1.4 ui-monospace;margin:4px 0;gap:10px}.u200 .line.sub{border-top:1px dashed #a09b88;padding-top:8px}.u200 .expand{width:100%;background:transparent;border:0;border-top:1px dashed #999580;border-bottom:1px dashed #999580;color:#514d3f;border-radius:0;font:10px ui-monospace;min-height:28px;margin-top:8px;padding:5px 0}.u200 .receipt button{color:#3d3c31;background:transparent}.u200 .split{display:flex;justify-content:space-between;align-items:center;margin-top:9px;font-size:11px}.u200 .split input{width:53px;min-height:30px;padding:4px 6px;border:1px solid #a09b88;background:#faf5e7;color:#3d3c31;font:12px ui-monospace}.u200 .per{font:12px ui-monospace;text-align:center;margin-top:9px}.u200 .footer{text-align:center;margin-top:10px;font:9px ui-monospace;letter-spacing:2px}

/* Focused composition */
.u200{max-width:320px}.u200 {max-width:250px}.u200 .receipt{padding:25px 25px 32px;max-width:250px}.u200 .receipt h3{font:italic 29px Georgia;margin:0 0 20px;text-align:center}.u200 .total{justify-content:center;margin:0 0 22px}.u200 .total strong{font:34px Georgia;letter-spacing:-1px}.u200 .expand{margin:0;padding:8px 0;font-size:11px;min-height:32px}.u200 .line{font-size:10px;margin:8px 0;line-height:1.6}</style>
<div class="ux u200" data-state="initial"><div class="receipt"><h3>Corner.</h3><div class="total"><strong>₩18,700</strong></div><button class="expand" aria-expanded="false" aria-controls="u200-lines">Details ↓</button><div class="fold" id="u200-lines" inert><div class="fold-inner"><div class="line" style="margin-top:16px"><span>FLAT WHITE × 2</span><span>10,000</span></div><div class="line"><span>CARDAMOM BUN</span><span>7,000</span></div><div class="line sub"><span>VAT 10%</span><span>1,700</span></div></div></div></div></div>

<script>
(()=>{const root=document.currentScript.previousElementSibling;const q=s=>root.querySelector(s),qa=s=>[...root.querySelectorAll(s)];const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;const state=s=>root.dataset.state=s;const pulse=(el,frames,duration=450)=>{if(!reduced)el.animate(frames,{duration,easing:'cubic-bezier(.2,.8,.2,1)'});};let open=false;q('.expand').onclick=()=>{open=!open;q('.receipt').classList.toggle('expanded',open);q('.expand').setAttribute('aria-expanded',open);q('.expand').textContent=open?'Hide details ↑':'Details ↓';q('.fold').inert=!open;state(open?'expanded':'initial')};})();
</script>
--- Code end ---
