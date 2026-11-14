---
source: "lucianlabs"
id: "176"
title: "Version filmstrip"
category: "Workflow & Systems"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#176"
tags: ["revision-filmstrip", "new-century"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Version filmstrip (176, Workflow & Systems)
[What it does] A filmstrip of a document’s earlier versions. Pick one and the large preview switches to it; press restore to make it the current version.
[How to use it] Press v1 or v2 below, then press “Restore this version”

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
<!-- Lucian UX/UI Prompt #176 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#176 -->
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
.u176 {width:100%;max-width:370px;font-size:14px;line-height:1.45;position:relative;--a:#cd5339;--soft:color-mix(in srgb,var(--a) 12%,var(--ux-surface));font-variant-numeric:tabular-nums}
.u176 button{border:1px solid var(--ux-line-2);background:var(--ux-surface);border-radius:9px;padding:9px 12px;min-height:38px;transition:background .2s,transform .3s,color .2s;color:var(--ux-ink)}
.u176 button:active{transform:translateY(1px)}.u176 button:disabled{opacity:.4;cursor:default}.u176 button.primary{background:var(--ux-ink);color:var(--ux-page);border-color:transparent}
.u176 .muted{color:var(--ux-ink-2);font-size:12px}.u176 .eyebrow{font:600 10px/1.2 ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--ux-ink-2)}
.u176 .row{display:flex;align-items:center;justify-content:space-between;gap:8px}.u176 .actions{display:flex;gap:8px;align-items:center;margin-top:16px;flex-wrap:wrap}
.u176 input,.u176 select{max-width:100%;min-width:0;background:var(--ux-surface);color:var(--ux-ink);border:1px solid var(--ux-line-2);border-radius:7px;padding:8px;font:inherit}
.u176 output{font-variant-numeric:tabular-nums}.u176 :focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
@media(prefers-reduced-motion:reduce){.u176 *,.u176 *::before,.u176 *::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
.u176 .poster{height:205px;background:#e8ddc8;border-radius:3px;position:relative;padding:22px;overflow:hidden;box-shadow:0 12px 24px -16px var(--ux-shadow-strong);color:#302b25;transition:background .55s}
.u176 .poster strong{position:relative;z-index:2;font:italic 54px/.94 Georgia,serif;letter-spacing:-3px;display:block;max-width:170px;transition:transform .55s}
.u176 .orb{width:125px;height:125px;position:absolute;right:22px;bottom:20px;background:#bb614b;border-radius:50%;transition:all .55s cubic-bezier(.2,.8,.2,1)}
.u176 .poster small{position:absolute;bottom:17px;left:22px;font:10px ui-monospace,monospace;letter-spacing:2px}
.u176 .film{display:flex;gap:10px;margin-top:20px;position:relative}.u176 .v{flex:1;border-top:3px solid transparent;border-radius:0;padding:9px 3px;background:none;text-align:left}.u176 .v[aria-pressed=true]{border-color:var(--a);color:var(--a)}.u176 .v span{display:block;font-size:11px;color:var(--ux-ink-2)}.u176 .live{font-size:11px;color:light-dark(#167349,#9ddab4)}

/* Focused composition */
.u176{max-width:320px}.u176 .poster{height:202px}.u176 .poster strong{font-size:46px;max-width:140px}.u176 .orb{width:106px;height:106px;right:18px}.u176 .version-rail{display:flex;justify-content:space-between;align-items:center;margin-top:12px;gap:20px}.u176 .film{margin:0;gap:2px;flex:1;max-width:145px}.u176 .v{padding:5px 10px;border:0;min-height:34px;font:12px ui-monospace;text-align:center;border-radius:5px}.u176 .v[aria-pressed=true]{background:var(--ux-surface-3);color:var(--ux-ink)}.u176 .restore{font-size:11px;border:0;background:none;min-height:32px;padding:5px 0}</style>
<div class="ux u176" data-state="initial"><div class="poster"><strong>Quiet<br>forms.</strong><i class="orb"></i></div><div class="version-rail"><div class="film"><button class="v" data-v="0" aria-pressed="false">v1</button><button class="v" data-v="1" aria-pressed="false">v2</button><button class="v" data-v="2" aria-pressed="true">v3</button></div><button class="restore" disabled>Current version</button></div></div>

<script>
(()=>{const root=document.currentScript.previousElementSibling;const q=s=>root.querySelector(s),qa=s=>[...root.querySelectorAll(s)];const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;const state=s=>root.dataset.state=s;const pulse=(el,frames,duration=450)=>{if(!reduced)el.animate(frames,{duration,easing:'cubic-bezier(.2,.8,.2,1)'});};let selected=2,live=2;const versions=[['#dadfd6','#416252','rotate(-12deg)','22%'],['#e9d1c8','#a45464','rotate(8deg)','50%'],['#e8ddc8','#bb614b','rotate(0deg)','50%']];function render(){const v=versions[selected];q('.poster').style.background=v[0];q('.orb').style.background=v[1];q('.orb').style.borderRadius=v[3];q('.poster strong').style.transform=v[2];qa('.v').forEach((b,i)=>b.setAttribute('aria-pressed',i===selected));q('.restore').disabled=selected===live;q('.restore').textContent=selected===live?'Current version':'Restore this version';state('preview-'+selected+'-live-'+live)}qa('.v').forEach(b=>b.onclick=()=>{selected=+b.dataset.v;render()});q('.restore').onclick=()=>{live=selected;render();pulse(q('.poster'),[{transform:'translateY(-5px)'},{transform:'none'}])};})();
</script>
--- Code end ---
