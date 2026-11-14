---
source: "lucianlabs"
id: "054"
title: "Follow profile card"
category: "Cards & Content"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#054"
tags: ["profile", "follow", "odometer", "suggestions", "social"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Follow profile card (054, Cards & Content)
[What it does] Press Follow and the button turns into “Following” with a check, while only the changed digits of the follower count roll. The lower panel slides from recent posts to “similar people” suggestions, and hovering the Following button turns it into an unfollow prompt.
[How to use it] Press Follow and watch the count and the lower panel change. While following, hover the button or press it again to unfollow

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
<!-- Lucian UX/UI Prompt #054 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#054 -->
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
.u054{position:relative;width:330px;height:470px;border-radius:30px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u054-cover{position:relative;height:118px;background:linear-gradient(120deg,#FFB547,#FF6B8B 50%,#7B61FF);overflow:hidden}
.u054-cover i{position:absolute;border-radius:50%}
.u054-cover i:nth-child(1){width:160px;height:160px;right:-30px;top:-70px;background:radial-gradient(circle,rgba(255,255,255,.55),transparent 65%)}
.u054-cover i:nth-child(2){width:240px;height:120px;left:-60px;bottom:-70px;background:rgba(40,20,90,.25);filter:blur(6px)}
.u054-av{position:absolute;left:20px;top:78px;width:84px;height:84px;border-radius:50%;padding:3px;background:conic-gradient(from 200deg,#FFB547,#FF6B8B,#7B61FF,#FFB547)}
.u054-av span{display:block;width:100%;height:100%;border-radius:50%;border:3px solid var(--ux-surface);background:radial-gradient(circle at 38% 32%,#FFE2C2,#F2A27A 45%,#B5577A 100%)}
.u054-av em{position:absolute;right:5px;bottom:5px;width:16px;height:16px;border-radius:50%;background:#22C38E;border:3px solid var(--ux-surface)}
.u054-act{position:absolute;right:18px;top:132px;display:flex;gap:8px}
.u054-msg{width:42px;height:42px;border:0;padding:0;border-radius:50%;display:grid;place-items:center;background:var(--ux-surface-2);color:var(--ux-ink);transition:transform .3s var(--ux-spring)}
.u054-msg:active{transform:scale(.9)}
.u054-msg svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2;stroke-linejoin:round}
.u054-msg:focus-visible,.u054-fb:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u054-fb{position:relative;width:112px;height:42px;border:0;border-radius:999px;background:var(--ux-ink);color:var(--ux-page);font-size:14px;font-weight:750;overflow:hidden;transition:background-color .4s,color .4s,box-shadow .4s,transform .35s var(--ux-spring)}
.u054-fb:active{transform:scale(.94)}
.u054-fb>span{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:5px;transition:transform .45s var(--ux-spring),opacity .25s}
.u054-fb svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}
.u054-fb svg path{stroke-dasharray:18;stroke-dashoffset:18;transition:stroke-dashoffset .4s var(--ux-ease) .15s}
.u054-fb .b,.u054-fb .c{transform:translateY(110%);opacity:0}
.u054.is-on .u054-fb{background:var(--ux-surface-2);color:var(--ux-ink);box-shadow:inset 0 0 0 1px var(--ux-line-2)}
.u054.is-on .u054-fb .a{transform:translateY(-110%);opacity:0}
.u054.is-on .u054-fb .b{transform:none;opacity:1}
.u054.is-on .u054-fb .b path{stroke-dashoffset:0}
@media (hover:hover){
  .u054.is-on:not(.just) .u054-fb:hover{background:color-mix(in srgb,var(--ux-danger) 12%,var(--ux-surface));color:var(--ux-danger);box-shadow:inset 0 0 0 1px color-mix(in srgb,var(--ux-danger) 40%,transparent)}
  .u054.is-on:not(.just) .u054-fb:hover .b{transform:translateY(-110%);opacity:0}
  .u054.is-on:not(.just) .u054-fb:hover .c{transform:none;opacity:1}
}
.u054-body{padding:52px 20px 0}
.u054-name{display:flex;align-items:center;gap:6px;margin:0;font-size:19px;font-weight:800;letter-spacing:-.035em}
.u054-name svg{width:18px;height:18px}
.u054-role{margin:3px 0 0;font-size:13px;font-weight:600;color:var(--ux-ink-3)}
.u054-bio{margin:10px 0 0;font-size:13.5px;line-height:1.55;color:var(--ux-ink-2)}
.u054-stats{display:flex;gap:22px;margin-top:14px}
.u054-stats div{font-size:12px;font-weight:600;color:var(--ux-ink-3)}
.u054-od{display:flex;height:22px;overflow:hidden;font-size:17px;font-weight:800;line-height:22px;color:var(--ux-ink);font-variant-numeric:tabular-nums;letter-spacing:-.01em}
.u054-col{display:flex;flex-direction:column;transform:translateY(calc(var(--d) * -22px));transition:transform .6s var(--ux-spring)}
.u054-low{position:absolute;left:0;right:0;bottom:0;height:126px;overflow:hidden}
.u054-pane{position:absolute;inset:0;padding:0 20px 18px;display:flex;flex-direction:column;transition:transform .55s var(--ux-ease),opacity .35s}
.u054-pane h4{margin:0 0 8px;font-size:12px;font-weight:800;letter-spacing:.04em;color:var(--ux-ink-3)}
.u054-posts{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;flex:1}
.u054-posts i{border-radius:12px;background:var(--g)}
.u054-sug{display:flex;flex-direction:column;gap:6px}
.u054-p{display:flex;align-items:center;gap:10px;height:40px}
.u054-p i{width:34px;height:34px;flex:none;border-radius:50%;background:var(--g)}
.u054-p b{flex:1;font-size:13.5px;font-weight:700;letter-spacing:-.02em}
.u054-p small{display:block;font-size:11.5px;font-weight:600;color:var(--ux-ink-3)}
.u054-p button{height:30px;padding:0 12px;border:0;border-radius:999px;background:var(--ux-accent-soft);color:var(--ux-accent);font-size:12.5px;font-weight:750;transition:background-color .3s,color .3s,transform .3s var(--ux-spring)}
.u054-p button:active{transform:scale(.92)}
.u054-p button[aria-pressed="true"]{background:var(--ux-surface-2);color:var(--ux-ink-3)}
.u054-p button:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u054-pane.s{transform:translateY(100%);opacity:0}
.u054.is-on .u054-pane.r{transform:translateY(-40%);opacity:0}
.u054.is-on .u054-pane.s{transform:none;opacity:1;transition-delay:.12s}
</style>
<div class="ux u054">
  <div class="u054-cover" aria-hidden="true"><i></i><i></i></div>
  <span class="u054-av" aria-hidden="true"><span></span><em></em></span>
  <div class="u054-act">
    <button class="u054-msg" type="button" aria-label="Send message"><svg viewBox="0 0 24 24"><path d="M4 12a8 8 0 1 1 3.4 6.5L4 19.5l1-3.3A8 8 0 0 1 4 12z"/></svg></button>
    <button class="u054-fb" type="button" aria-pressed="false" aria-label="Follow Jian Seo"><span class="a">Follow</span><span class="b"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8.4l3 3 6-6.4"/></svg>Following</span><span class="c">Unfollow</span></button>
  </div>
  <div class="u054-body">
    <h3 class="u054-name">Jian Seo <svg viewBox="0 0 24 24" role="img" aria-label="Verified"><path d="M12 2.5l2.4 1.8 3-.2.9 2.8 2.5 1.7-1 2.9 1 2.9-2.5 1.7-.9 2.8-3-.2L12 21.5l-2.4-1.8-3 .2-.9-2.8-2.5-1.7 1-2.9-1-2.9 2.5-1.7.9-2.8 3 .2z" fill="#3D8BFF"/><path d="M8.3 12.2l2.4 2.4 5-5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></h3>
    <p class="u054-role">Motion designer · Seoul</p>
    <p class="u054-bio">Obsessed with short transitions and response times. Weekends are for spring-curve experiments.</p>
    <div class="u054-stats">
      <div><span class="u054-od" data-v="4812" aria-live="polite"></span>Followers</div>
      <div><span class="u054-od" data-v="318"></span>Following</div>
      <div><span class="u054-od" data-v="162"></span>Posts</div>
    </div>
  </div>
  <div class="u054-low">
    <section class="u054-pane r"><h4>Recent posts</h4><div class="u054-posts" aria-hidden="true"><i style="--g:linear-gradient(140deg,#FFB547,#FF6B8B)"></i><i style="--g:linear-gradient(140deg,#7B61FF,#3D8BFF)"></i><i style="--g:linear-gradient(140deg,#22C3A6,#0EA5E9)"></i></div></section>
    <section class="u054-pane s" aria-hidden="true"><h4>Similar people</h4><div class="u054-sug">
      <div class="u054-p"><i style="--g:linear-gradient(140deg,#8B6CFF,#FF7A93)"></i><b>Doyun Han<small>Interaction designer</small></b><button type="button" aria-pressed="false" tabindex="-1">Follow</button></div>
      <div class="u054-p"><i style="--g:linear-gradient(140deg,#22C3A6,#3D8BFF)"></i><b>Harin Yoon<small>3D artist</small></b><button type="button" aria-pressed="false" tabindex="-1">Follow</button></div>
    </div></section>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var fb = root.querySelector('.u054-fb');
  var od = root.querySelector('.u054-od');
  var panes = root.querySelectorAll('.u054-pane');
  var subs = root.querySelectorAll('.u054-p button');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function build(el) {
    var s = Number(el.getAttribute('data-v')).toLocaleString('en-US');
    el.setAttribute('aria-label', s);
    el.innerHTML = s.split('').map(function (ch) {
      if (ch < '0' || ch > '9') return '<span aria-hidden="true">' + ch + '</span>';
      var col = '';
      for (var i = 0; i < 10; i++) col += '<span>' + i + '</span>';
      return '<span class="u054-col" aria-hidden="true" style="--d:' + ch + '">' + col + '</span>';
    }).join('');
  }
  function set(el, v) {
    var s = v.toLocaleString('en-US'), cols = el.querySelectorAll('.u054-col'), digits = s.replace(/\D/g, '');
    if (cols.length !== digits.length) { el.setAttribute('data-v', v); build(el); return; }
    cols.forEach(function (c, i) { c.style.setProperty('--d', digits[i]); });
    el.setAttribute('aria-label', s);
  }
  root.querySelectorAll('.u054-od').forEach(build);
  var base = 4812, on = false;
  fb.addEventListener('click', function () {
    on = !on;
    root.classList.toggle('is-on', on);
    root.classList.toggle('just', on);
    fb.setAttribute('aria-pressed', String(on));
    fb.setAttribute('aria-label', on ? 'Following Jian Seo, press to unfollow' : 'Follow Jian Seo');
    set(od, base + (on ? 1 : 0));
    panes[0].setAttribute('aria-hidden', String(on));
    panes[1].setAttribute('aria-hidden', String(!on));
    subs.forEach(function (b) { b.tabIndex = on ? 0 : -1; });
    if (!rm && on) root.querySelector('.u054-av').animate([{ transform: 'scale(1)' }, { transform: 'scale(1.08)' }, { transform: 'scale(1)' }], { duration: 450, easing: 'cubic-bezier(.34,1.5,.64,1)' });
  });
  fb.addEventListener('pointerleave', function () { root.classList.remove('just'); });
  subs.forEach(function (b) {
    b.addEventListener('click', function () {
      var p = b.getAttribute('aria-pressed') !== 'true';
      b.setAttribute('aria-pressed', String(p));
      b.textContent = p ? 'Following' : 'Follow';
    });
  });
})();
</script>
--- Code end ---
