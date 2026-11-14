---
source: "lucianlabs"
id: "198"
title: "Network path diagnosis"
category: "Workflow & Systems"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#198"
tags: ["network-hop-test", "new-century"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Network path diagnosis (198, Workflow & Systems)
[What it does] A diagnostic screen that checks the path from a device to the origin server hop by hop. The probe stops at the failing hop, and reroute restores the connection another way.
[How to use it] Press “Diagnose”, then “Reroute”

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
<!-- Lucian UX/UI Prompt #198 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#198 -->
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
.u198 {width:100%;max-width:370px;font-size:14px;line-height:1.45;position:relative;--a:#cd5339;--soft:color-mix(in srgb,var(--a) 12%,var(--ux-surface));font-variant-numeric:tabular-nums}
.u198 button{border:1px solid var(--ux-line-2);background:var(--ux-surface);border-radius:9px;padding:9px 12px;min-height:38px;transition:background .2s,transform .3s,color .2s;color:var(--ux-ink)}
.u198 button:active{transform:translateY(1px)}.u198 button:disabled{opacity:.4;cursor:default}.u198 button.primary{background:var(--ux-ink);color:var(--ux-page);border-color:transparent}
.u198 .muted{color:var(--ux-ink-2);font-size:12px}.u198 .eyebrow{font:600 10px/1.2 ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--ux-ink-2)}
.u198 .row{display:flex;align-items:center;justify-content:space-between;gap:8px}.u198 .actions{display:flex;gap:8px;align-items:center;margin-top:16px;flex-wrap:wrap}
.u198 input,.u198 select{max-width:100%;min-width:0;background:var(--ux-surface);color:var(--ux-ink);border:1px solid var(--ux-line-2);border-radius:7px;padding:8px;font:inherit}
.u198 output{font-variant-numeric:tabular-nums}.u198 :focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
@media(prefers-reduced-motion:reduce){.u198 *,.u198 *::before,.u198 *::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
.u198 .topology{height:199px;margin:18px 0 12px;position:relative;background:var(--ux-surface);border:1px solid var(--ux-line-2);border-radius:12px;overflow:hidden}.u198 svg{width:100%;height:100%;display:block}.u198 .wire{fill:none;stroke:var(--ux-line-2);stroke-width:2;transition:stroke .3s}.u198 .wire.ok{stroke:#648b63}.u198 .wire.bad{stroke:#c65d49;stroke-dasharray:4 4}.u198 .wire.bypass{stroke:#648b63;stroke-dasharray:4 4;opacity:0}.u198 .wire.bypass.on{opacity:1}.u198 .node{fill:var(--ux-surface-2);stroke:var(--ux-line-2);stroke-width:1.5;transition:fill .3s,stroke .3s}.u198 .node.ok{fill:light-dark(#e0ebd5,#304935);stroke:#6c9662}.u198 .node.bad{fill:light-dark(#f8dfd7,#653e37);stroke:#c65d49}.u198 svg text{font:10px system-ui;fill:var(--ux-ink)}.u198 .packet{fill:#709469;opacity:0;transition:cx .35s,cy .35s}.u198 .legend{display:flex;justify-content:space-between;font-size:11px;color:var(--ux-ink-2)}.u198 .status{font-size:12px;min-height:38px;margin-top:15px;padding-left:10px;border-left:2px solid #699060}.u198 .actions button{font-size:12px}.u198 .reset{border:0;background:none;font-size:11px;padding:2px 8px;min-height:28px}

/* Focused composition */
.u198{max-width:320px}.u198 .topology{height:172px;margin:0 0 10px;border:0;background:none;border-radius:0}.u198 svg text{font-size:11px}.u198 .diagnose{display:block;margin:auto;min-height:34px;font-size:12px;background:none;border:0}</style>
<div class="ux u198" data-state="initial"><div class="topology"><svg viewBox="0 0 340 172" role="img" aria-label="Path from device to gateway, edge and origin"><path class="wire w0" d="M46 60H128"/><path class="wire w1" d="M128 60H210"/><path class="wire w2" d="M210 60H292"/><path class="wire bypass" d="M128 60V137H292V60"/><circle class="node n0" cx="46" cy="60" r="17"/><circle class="node n1" cx="128" cy="60" r="17"/><circle class="node n2" cx="210" cy="60" r="17"/><circle class="node n3" cx="292" cy="60" r="17"/><g text-anchor="middle"><text x="46" y="100">My device</text><text x="128" y="100">GW</text><text x="210" y="100">Edge</text><text x="292" y="100">Origin</text></g><circle class="packet" cx="46" cy="60" r="5"/></svg></div><button class="diagnose">Diagnose →</button></div>

<script>
(()=>{const root=document.currentScript.previousElementSibling;const q=s=>root.querySelector(s),qa=s=>[...root.querySelectorAll(s)];const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;const state=s=>root.dataset.state=s;const pulse=(el,frames,duration=450)=>{if(!reduced)el.animate(frames,{duration,easing:'cubic-bezier(.2,.8,.2,1)'});};let phase=0,timers=[];function reset(){timers.forEach(clearTimeout);timers=[];phase=0;qa('.node,.wire').forEach(x=>x.classList.remove('ok','bad','on'));q('.packet').style.opacity=0;q('.packet').setAttribute('cx',46);q('.diagnose').disabled=false;q('.diagnose').textContent='Diagnose →';state('initial')}q('.diagnose').onclick=()=>{if(phase===2){reset();return}if(phase===1){q('.wire.bypass').classList.add('on');q('.n3').classList.add('ok');phase=2;q('.diagnose').textContent='✓ Connected · Reset';state('recovered');return}q('.diagnose').disabled=true;q('.diagnose').textContent='Checking path…';q('.n0').classList.add('ok');q('.packet').style.opacity=reduced?0:1;q('.packet').setAttribute('cx',128);state('testing');timers.push(setTimeout(()=>{q('.n1').classList.add('ok');q('.w0').classList.add('ok');q('.packet').setAttribute('cx',210)},300));timers.push(setTimeout(()=>{q('.n2').classList.add('bad');q('.w1').classList.add('bad');q('.packet').style.opacity=0;q('.diagnose').disabled=false;q('.diagnose').textContent='Edge failed · Reroute →';phase=1;state('failed-hop-2')},650))};})();
</script>
--- Code end ---
