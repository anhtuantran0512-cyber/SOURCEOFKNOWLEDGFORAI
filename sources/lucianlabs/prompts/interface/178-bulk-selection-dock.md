---
source: "lucianlabs"
id: "178"
title: "Bulk selection dock"
category: "Workflow & Systems"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#178"
tags: ["bulk-selection-dock", "new-century"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Bulk selection dock (178, Workflow & Systems)
[What it does] A workbench for acting on several files at once. Select files and a bulk-action bar appears below; after archiving you can undo right away.
[How to use it] Select two or so file cards, then press “Archive”

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
<!-- Lucian UX/UI Prompt #178 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#178 -->
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
.u178 {width:100%;max-width:370px;font-size:14px;line-height:1.45;position:relative;--a:#cd5339;--soft:color-mix(in srgb,var(--a) 12%,var(--ux-surface));font-variant-numeric:tabular-nums}
.u178 button{border:1px solid var(--ux-line-2);background:var(--ux-surface);border-radius:9px;padding:9px 12px;min-height:38px;transition:background .2s,transform .3s,color .2s;color:var(--ux-ink)}
.u178 button:active{transform:translateY(1px)}.u178 button:disabled{opacity:.4;cursor:default}.u178 button.primary{background:var(--ux-ink);color:var(--ux-page);border-color:transparent}
.u178 .muted{color:var(--ux-ink-2);font-size:12px}.u178 .eyebrow{font:600 10px/1.2 ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--ux-ink-2)}
.u178 .row{display:flex;align-items:center;justify-content:space-between;gap:8px}.u178 .actions{display:flex;gap:8px;align-items:center;margin-top:16px;flex-wrap:wrap}
.u178 input,.u178 select{max-width:100%;min-width:0;background:var(--ux-surface);color:var(--ux-ink);border:1px solid var(--ux-line-2);border-radius:7px;padding:8px;font:inherit}
.u178 output{font-variant-numeric:tabular-nums}.u178 :focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
@media(prefers-reduced-motion:reduce){.u178 *,.u178 *::before,.u178 *::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
.u178 .files{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;margin:19px 0}.u178 .file{height:103px;position:relative;text-align:left;padding:12px 9px;background:var(--ux-surface-2);transition:transform .3s,background .3s}.u178 .file[aria-pressed=true]{background:color-mix(in srgb,#cf8a31 19%,var(--ux-surface));border-color:#b87623;transform:translateY(-4px)}.u178 .file i{display:block;font-style:normal;font:bold 11px ui-monospace,monospace;color:light-dark(#855210,#efbd78);margin-bottom:15px}.u178 .file span{font-size:11px;display:block}.u178 .file::after{content:'+';position:absolute;right:9px;top:6px;color:var(--ux-ink-2)}.u178 .file[aria-pressed=true]::after{content:'✓'}.u178 .dock{display:flex;align-items:center;justify-content:space-between;gap:6px;padding:10px 12px;border-radius:14px;background:var(--ux-ink);color:var(--ux-page);transform:translateY(7px);opacity:.55;transition:all .35s}.u178 .dock.active{transform:none;opacity:1}.u178 .dock button{background:var(--ux-page);color:var(--ux-ink);padding:6px 10px;font-size:12px}.u178 .restore{border:0;background:none;font-size:12px;padding:0;min-height:30px}

/* Focused composition */
.u178{max-width:320px}.u178 .files{margin:0;gap:12px;min-height:122px;align-items:start}.u178 .file{height:122px;border-radius:5px;padding:17px 10px;background:var(--ux-surface);box-shadow:0 9px 18px -17px var(--ux-ink)}.u178 .file i{font-size:15px;margin-bottom:24px}.u178 .file::after{font-size:12px}.u178 .dock{margin-top:18px;font-size:12px;opacity:1;transform:none;padding:7px 11px}.u178 .dock[hidden],.u178 .restore[hidden],.u178 .file[hidden]{display:none!important}.u178 .restore{display:block;margin:18px auto 0}</style>
<div class="ux u178" data-state="initial"><div class="files"><button class="file" data-i="0" aria-pressed="false"><i>FIG</i><span>brand.fig</span></button><button class="file" data-i="1" aria-pressed="false"><i>PDF</i><span>brief.pdf</span></button><button class="file" data-i="2" aria-pressed="false"><i>SVG</i><span>symbol.svg</span></button></div><div class="dock" hidden><span class="count" aria-live="polite"></span><button class="archive">Archive ↗</button></div><button class="restore" hidden>Undo archive ↶</button></div>

<script>
(()=>{const root=document.currentScript.previousElementSibling;const q=s=>root.querySelector(s),qa=s=>[...root.querySelectorAll(s)];const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;const state=s=>root.dataset.state=s;const pulse=(el,frames,duration=450)=>{if(!reduced)el.animate(frames,{duration,easing:'cubic-bezier(.2,.8,.2,1)'});};const selected=new Set();let archived=0;function render(){qa('.file').forEach(b=>b.setAttribute('aria-pressed',selected.has(b.dataset.i)));q('.count').textContent=selected.size+' selected';q('.dock').hidden=!selected.size;q('.restore').hidden=!archived;state('selected-'+[...selected].join('-')+'-archived-'+archived)}qa('.file').forEach(b=>b.onclick=()=>{selected.has(b.dataset.i)?selected.delete(b.dataset.i):selected.add(b.dataset.i);render()});q('.archive').onclick=()=>{archived+=selected.size;qa('.file').filter(b=>selected.has(b.dataset.i)).forEach(b=>b.hidden=true);selected.clear();render()};q('.restore').onclick=()=>{qa('.file').forEach(b=>b.hidden=false);selected.clear();archived=0;render()};})();
</script>
--- Code end ---
