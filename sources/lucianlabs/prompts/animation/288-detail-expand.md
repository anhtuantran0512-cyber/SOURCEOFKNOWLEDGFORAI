---
source: "lucianlabs"
id: "288"
title: "Expandable product details"
category: "Commerce & Pricing"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#288"
tags: ["read-more", "expand", "product-detail", "ecommerce", "collapse"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Expandable product details (288, Commerce & Pricing)
[What it does] On a store's product page, the long product details are only partly shown and fade out at the bottom. Press Show more and the details area smoothly grows to its real length as the fade lifts, while the button moves down and turns into Show less. When you collapse it, the height shrinks while the screen returns to the start of the details, so you never lose your place.
[How to use it] Scroll down and press Show more, then collapse it again at the end

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
<!-- Lucian UX/UI Prompt #288 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#288 -->
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
.u288{position:relative;width:300px;height:480px;border-radius:32px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u288-sc{position:absolute;inset:0;overflow-y:auto;overscroll-behavior:contain;scrollbar-width:none}
.u288-sc::-webkit-scrollbar{display:none}
.u288-sc:focus-visible{outline:2px solid var(--ux-accent);outline-offset:-4px;border-radius:32px}
.u288-ph{position:relative;height:200px;background:linear-gradient(160deg,#E7E5E4,#D6D3D1)}
.u288-ph svg{position:absolute;left:50%;top:50%;width:150px;height:150px;transform:translate(-50%,-46%)}
.u288-if{padding:16px 18px 6px}
.u288-if h3{margin:0;font-size:16px;font-weight:850;letter-spacing:-.02em}
.u288-pr{display:flex;align-items:baseline;gap:6px;margin-top:6px}
.u288-pr em{font-style:normal;font-size:17px;font-weight:900;color:#E11D48}
.u288-pr b{font-size:17px;font-weight:900}
.u288-pr s{font-size:11px;font-weight:650;color:var(--ux-ink-3)}
.u288-if small{display:block;margin-top:6px;font-size:10.5px;font-weight:750;color:#059669}
.u288-st{margin:14px 0 0;padding:14px 18px 0;border-top:8px solid var(--ux-surface-2);font-size:13px;font-weight:900}
.u288-dt{position:relative;height:170px;overflow:hidden;margin-top:10px;transition:height .65s cubic-bezier(.3,.8,.25,1)}
.u288-dt::after{content:"";position:absolute;left:0;right:0;bottom:0;height:110px;background:linear-gradient(transparent,var(--ux-surface) 88%);pointer-events:none;transition:opacity .4s}
.u288.is-open .u288-dt::after{opacity:0}
.u288-bn{margin:0 14px;height:150px;border-radius:16px;background:linear-gradient(140deg,#F5F5F4,#E7E5E4);display:flex;flex-direction:column;justify-content:flex-end;padding:16px;color:#292524}
.u288-bn b{font-size:19px;font-weight:900;letter-spacing:-.03em}
.u288-bn span{margin-top:4px;font-size:10.5px;font-weight:650;color:#57534E}
.u288-bk{margin:16px 18px 0}
.u288-bk h5{margin:0 0 8px;font-size:11px;font-weight:850;color:var(--ux-ink-2)}
.u288-sw{display:flex;gap:8px}
.u288-sw i{width:34px;height:34px;border-radius:10px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}
.u288-tb{width:100%;border-collapse:collapse;font-size:10.5px;font-weight:700;text-align:center}
.u288-tb th,.u288-tb td{padding:6px 0;border-bottom:1px solid var(--ux-line)}
.u288-tb th{color:var(--ux-ink-3);font-weight:800}
.u288-tb td:first-child{text-align:left;color:var(--ux-ink-3);font-weight:800}
.u288-bk p{margin:0;font-size:10.5px;line-height:1.5;font-weight:650;color:var(--ux-ink-2)}
.u288-md{margin:16px 14px 6px;height:120px;border-radius:16px;background:linear-gradient(180deg,#D6D3D1,#A8A29E);display:flex;align-items:flex-end;padding:12px;font-size:10px;font-weight:800;color:#fff}
.u288-mr{display:flex;align-items:center;justify-content:center;gap:6px;width:calc(100% - 28px);height:42px;margin:6px 14px 0;border:0;border-radius:12px;background:var(--ux-surface);box-shadow:inset 0 0 0 1.5px var(--ux-ink);color:var(--ux-ink);font:inherit;font-size:12px;font-weight:850;cursor:pointer;position:relative;z-index:1}
.u288-mr:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u288-mr svg{width:12px;height:12px;transition:transform .35s}
.u288.is-open .u288-mr svg{transform:rotate(180deg)}
.u288-rv{margin:18px 0 0;padding:14px 18px 34px;border-top:8px solid var(--ux-surface-2)}
.u288-rv b{font-size:13px;font-weight:900}
.u288-rv p{margin:8px 0 0;padding:10px 12px;border-radius:12px;background:var(--ux-surface-2);font-size:11px;font-weight:650;color:var(--ux-ink-2)}
@media (prefers-reduced-motion: reduce){.u288-dt,.u288-dt::after,.u288-mr svg{transition:none}}
</style>
<div class="ux u288">
  <div class="u288-sc" tabindex="0" aria-label="Product page">
    <div class="u288-ph" aria-hidden="true"><svg viewBox="0 0 150 150"><path d="M50 22 L75 30 L100 22 L132 40 L120 70 L106 64 L106 132 L44 132 L44 64 L30 70 L18 40Z" fill="#F5F5F4" stroke="#A8A29E" stroke-width="1.5" stroke-linejoin="round"/><path d="M75 30 L75 132" stroke="#D6D3D1" stroke-width="1.2"/><path d="M62 26 L75 44 L88 26" fill="none" stroke="#A8A29E" stroke-width="1.5" stroke-linejoin="round"/><circle cx="75" cy="60" r="1.8" fill="#A8A29E"/><circle cx="75" cy="80" r="1.8" fill="#A8A29E"/><circle cx="75" cy="100" r="1.8" fill="#A8A29E"/></svg></div>
    <div class="u288-if"><h3>Daily linen shirt</h3><div class="u288-pr"><em>20%</em><b>$39</b><s>$48</s></div><small>Free shipping · Arrives tomorrow</small></div>
    <h4 class="u288-st">Details</h4>
    <div class="u288-dt"><div class="u288-in">
      <div class="u288-bn"><b>Light, breezy linen</b><span>An everyday shirt you can wear all summer without worrying about wrinkles</span></div>
      <div class="u288-bk"><h5>Colors</h5><div class="u288-sw"><i style="background:#F5F5F4"></i><i style="background:#D6CFC4"></i><i style="background:#A3B8C8"></i><i style="background:#3F4A3C"></i></div></div>
      <div class="u288-bk"><h5>Size</h5><table class="u288-tb"><tr><th></th><th>S</th><th>M</th><th>L</th><th>XL</th></tr><tr><td>Shoulder</td><td>44</td><td>46</td><td>48</td><td>50</td></tr><tr><td>Chest</td><td>54</td><td>56</td><td>58</td><td>61</td></tr><tr><td>Length</td><td>72</td><td>74</td><td>76</td><td>78</td></tr></table></div>
      <div class="u288-bk"><h5>Care</h5><p>Cold hand wash · Dry in shade · Low iron</p></div>
      <div class="u288-md">Model 178 cm · wearing L</div>
    </div></div>
    <button type="button" class="u288-mr" aria-expanded="false"><span></span><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 4.5L6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
    <div class="u288-rv"><b>Reviews 128</b><p>“Not too thick, just right”</p></div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u288-sc'), dt = root.querySelector('.u288-dt'), inn = root.querySelector('.u288-in'), mr = root.querySelector('.u288-mr'), st = root.querySelector('.u288-st'), lb = mr.querySelector('span');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var SHUT = 170, open = false, uid = 'u288' + Math.random().toString(36).slice(2, 7);
  dt.id = uid; mr.setAttribute('aria-controls', uid);
  function sync() { lb.textContent = open ? 'Show less' : 'Show more details'; mr.setAttribute('aria-expanded', open); root.classList.toggle('is-open', open); }
  function scrollTo(y, ms) {
    if (rm) { sc.scrollTop = y; return; }
    var y0 = sc.scrollTop, t0 = performance.now();
    (function f(now) { var k = Math.min(1, (now - t0) / ms), e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; sc.scrollTop = y0 + (y - y0) * e; if (k < 1) requestAnimationFrame(f); })(t0);
  }
  mr.addEventListener('click', function () {
    open = !open; sync();
    if (open) { dt.style.height = inn.offsetHeight + 'px'; return; }
    dt.style.height = SHUT + 'px';
    scrollTo(Math.max(0, st.offsetTop - 12), 650);
  });
  sync();
})();
</script>
--- Code end ---
