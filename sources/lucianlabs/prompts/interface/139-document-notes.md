---
source: "lucianlabs"
id: "139"
title: "Margin notes"
category: "Document & Data Editing"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#139"
tags: ["document-notes", "editing", "interactive"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Margin notes (139, Document & Data Editing)
[What it does] An annotation editor that pins a margin note to each sentence. Press the mark after a sentence to open its note; whatever you type stays attached to that sentence.
[How to use it] Press the + mark after a sentence to open its note and write something

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
<!-- Lucian UX/UI Prompt #139 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#139 -->
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
.u139{width:min(100%,370px);font-size:14px;line-height:1.6;color:var(--ux-ink)}.u139 button,.u139 input,.u139 textarea,.u139 select{font:inherit;color:inherit;max-width:100%;min-width:0}.u139 button{cursor:pointer;min-height:44px;border:1px solid var(--ux-line-2);border-radius:8px;background:var(--ux-surface);padding:8px 12px}.u139 input,.u139 textarea,.u139 select{border:1px solid var(--ux-line-2);border-radius:6px;background:var(--ux-surface);padding:8px 10px}.u139 .quiet{color:var(--ux-ink-2)}.u139 .primary{background:var(--ux-accent);color:var(--ux-accent-ink);border-color:transparent}.u139 .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}.u139 [hidden]{display:none!important}.u139 :focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}@media(prefers-reduced-motion:reduce){.u139 *{animation:none!important;transition:none!important}}
.u139{position:relative;background:var(--ux-surface);padding:27px 24px;border-left:2px solid var(--ux-line-2);box-shadow:0 8px 18px var(--ux-shadow)}.u139 h3{font:700 25px/1.4 Georgia,'Apple SD Gothic Neo',serif;margin:0 0 16px}.u139 .anchor{display:block;width:100%;text-align:left;border:0;background:transparent;padding:6px 0;font:16px/1.9 Georgia,'Apple SD Gothic Neo',serif;border-radius:0}.u139 .anchor:after{content:'＋';color:var(--ux-warn);padding-left:7px;font:12px sans-serif}.u139 .anchor[aria-pressed="true"]{text-decoration:underline;text-decoration-color:var(--ux-warn);text-underline-offset:6px}.u139 .margin{margin-top:14px;background:color-mix(in srgb,var(--ux-warn) 14%,var(--ux-surface));border-left:2px solid var(--ux-warn);padding:14px}.u139 textarea{border:0;background:transparent;padding:0;width:100%;height:60px;resize:none;font-size:14px;line-height:1.7}
</style>
<div class="ux u139"><h3>A small forest in the city</h3><button class="anchor" data-anchor="0" aria-pressed="false">Rooftop gardens hold rainwater for a while.</button><button class="anchor" data-anchor="1" aria-pressed="false">Shade lowers the summer heat.</button><aside class="margin" hidden><textarea aria-label="Note for the selected sentence">Check the drainage too</textarea></aside></div>

<script>
(()=>{const root=document.currentScript.previousElementSibling,$=s=>root.querySelector(s),$$=s=>[...root.querySelectorAll(s)],esc=v=>String(v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));const motion=(node,frames,opts={})=>{if(node?.animate&&!matchMedia('(prefers-reduced-motion:reduce)').matches)node.animate(frames,{duration:220,easing:'cubic-bezier(.2,.8,.2,1)',...opts})};let notes=['Check the drainage too',''],active=null;function render(){$$('[data-anchor]').forEach(b=>b.setAttribute('aria-pressed',String(+b.dataset.anchor===active)));$('.margin').hidden=active===null;if(active!==null)$('textarea').value=notes[active];root.dataset.notes=JSON.stringify(notes)}$$('[data-anchor]').forEach(b=>b.onclick=()=>{active=active===+b.dataset.anchor?null:+b.dataset.anchor;render();if(active!==null){$('textarea').focus();motion($('.margin'),[{transform:'translateY(-5px)',opacity:.6},{transform:'none',opacity:1}])}});$('textarea').oninput=()=>{notes[active]=$('textarea').value;root.dataset.notes=JSON.stringify(notes)};$('textarea').onkeydown=e=>{if(e.key==='Escape'){const b=$('[data-anchor="'+active+'"]');active=null;render();b.focus()}};render();})();
</script>
--- Code end ---
