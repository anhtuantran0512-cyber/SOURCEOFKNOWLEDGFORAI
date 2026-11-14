---
source: "lucianlabs"
id: "006"
title: "Ink ripple subscribe button"
category: "Buttons"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#006"
tags: ["button", "ripple", "subscribe", "toggle", "counter"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Ink ripple subscribe button (006, Buttons)
[What it does] Ink spreads from the exact spot you press and the button switches to subscribed. The bell shakes and the subscriber count rolls up by one. Press again to reverse it.
[How to use it] Press anywhere on the button — the ripple starts where you press

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
<!-- Lucian UX/UI Prompt #006 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#006 -->
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
.u006{position:relative;width:320px;height:200px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px}
.u006-ch{display:flex;align-items:center;gap:14px;width:270px}
.u006-av{position:relative;width:58px;height:58px;border-radius:50%;flex:none;padding:3px;background:conic-gradient(from 200deg,#FF6B8B,#FFB26B,#8B6CFF,#FF6B8B)}
.u006-av span{display:block;width:100%;height:100%;border-radius:50%;border:3px solid var(--ux-page);background:radial-gradient(circle at 35% 30%,#FFD3A8,#FF7A93 55%,#7B61FF)}
.u006-ch b{display:block;font-size:17px;font-weight:720;letter-spacing:-.025em}
.u006-cnt{display:flex;align-items:center;white-space:pre;margin-top:3px;font-size:13.5px;color:var(--ux-ink-3);font-variant-numeric:tabular-nums}
.u006-roll{position:relative;display:inline-block;height:1.3em;overflow:hidden;vertical-align:bottom}
.u006-roll span{display:block;line-height:1.3em;transition:transform .55s var(--ux-spring),opacity .3s var(--ux-ease)}
.u006-roll span+span{position:absolute;left:0;top:0}
.u006-btn{position:relative;width:270px;height:60px;border:0;padding:0;border-radius:18px;overflow:hidden;isolation:isolate;background:var(--ux-danger);color:var(--ux-accent-ink);
  box-shadow:0 18px 32px -18px color-mix(in srgb,var(--ux-danger) 80%,transparent);transition:background-color .55s var(--ux-ease),color .45s var(--ux-ease),box-shadow .5s var(--ux-ease),transform .45s var(--ux-spring)}
.u006-btn:hover{transform:translateY(-2px)}
.u006-btn:active{transform:scale(.97)}
.u006-btn:focus-visible{outline:2px solid var(--ux-danger);outline-offset:4px}
.u006-lab{position:relative;z-index:1;display:flex;align-items:center;justify-content:center;gap:10px;font-size:16.5px;font-weight:720;letter-spacing:-.02em}
.u006-bell{width:20px;height:20px;transform-origin:50% 8%}
.u006-bell svg{width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.u006-bell .u006-solid{fill:currentColor;opacity:0;transition:opacity .3s var(--ux-ease)}
.u006-ink{position:absolute;z-index:0;width:20px;height:20px;margin:-10px 0 0 -10px;border-radius:50%;background:var(--c);pointer-events:none;animation:u006-ink .75s var(--ux-ease) forwards}
@keyframes u006-ink{from{transform:scale(0);opacity:.9}to{transform:scale(var(--s));opacity:1}}
.u006.is-on .u006-btn{background:var(--ux-surface);color:var(--ux-ink);box-shadow:inset 0 0 0 1px var(--ux-line-2),0 14px 26px -20px var(--ux-shadow-strong)}
.u006.is-on .u006-bell{animation:u006-ring .9s var(--ux-ease)}
.u006.is-on .u006-bell .u006-solid{opacity:1}
@keyframes u006-ring{0%{transform:rotate(0)}15%{transform:rotate(18deg)}30%{transform:rotate(-15deg)}45%{transform:rotate(11deg)}60%{transform:rotate(-7deg)}75%{transform:rotate(3deg)}100%{transform:rotate(0)}}
.u006-txt{position:relative;display:inline-grid;justify-items:center;height:22px;overflow:hidden}
.u006-txt span{grid-area:1/1;display:block;line-height:22px;white-space:nowrap;transition:transform .5s var(--ux-spring)}
.u006-txt span+span{transform:translateY(100%)}
.u006.is-on .u006-txt span:first-child{transform:translateY(-100%)}
.u006.is-on .u006-txt span+span{transform:none}
.u006-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
</style>
<div class="ux u006">
  <div class="u006-ch">
    <span class="u006-av" aria-hidden="true"><span></span></span>
    <div>
      <b>Motion Studio</b>
      <span class="u006-cnt"><span class="u006-roll" aria-hidden="true"><span>1,284</span><span></span></span> subscribers<span class="u006-sr" aria-live="polite"></span></span>
    </div>
  </div>
  <button class="u006-btn" type="button" aria-pressed="false">
    <span class="u006-lab">
      <span class="u006-bell" aria-hidden="true"><svg viewBox="0 0 24 24"><path class="u006-solid" d="M6 16.5V11a6 6 0 0 1 12 0v5.5l1.5 1.5h-15z"/><path d="M6 16.5V11a6 6 0 0 1 12 0v5.5l1.5 1.5h-15zM10 20.5a2.2 2.2 0 0 0 4 0"/></svg></span>
      <span class="u006-txt"><span>Subscribe</span><span aria-hidden="true">Subscribed</span></span>
    </span>
  </button>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var btn = root.querySelector('.u006-btn');
  var roll = root.querySelector('.u006-roll');
  var sr = root.querySelector('.u006-sr');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var count = 1284;
  var on = false;
  var fmt = function (n) { return n.toLocaleString('en-US'); };

  var curIdx = 0;
  function rollTo(n, up) {
    var cur = roll.children[curIdx], nxt = roll.children[1 - curIdx];
    nxt.style.transition = 'none';
    nxt.textContent = fmt(n);
    nxt.style.transform = 'translateY(' + (up ? 100 : -100) + '%)';
    nxt.style.opacity = '0';
    void nxt.offsetWidth;
    nxt.style.transition = '';
    nxt.style.transform = 'none';
    nxt.style.opacity = '1';
    cur.style.transform = 'translateY(' + (up ? -100 : 100) + '%)';
    cur.style.opacity = '0';
    curIdx = 1 - curIdx;
  }
  function ripple(x, y) {
    if (rm) return;
    var r = btn.getBoundingClientRect();
    var k = r.width / btn.offsetWidth || 1;
    var px = (x - r.left) / k, py = (y - r.top) / k;
    var w = btn.offsetWidth, h = btn.offsetHeight;
    var far = Math.hypot(Math.max(px, w - px), Math.max(py, h - py));
    var ink = document.createElement('span');
    ink.className = 'u006-ink';
    ink.style.left = px + 'px';
    ink.style.top = py + 'px';
    ink.style.setProperty('--s', (far / 10 + 0.4).toFixed(2));
    ink.style.setProperty('--c', on ? 'var(--ux-danger)' : 'var(--ux-surface)');
    btn.appendChild(ink);
    setTimeout(function () { ink.remove(); }, 900);
  }
  btn.addEventListener('click', function (e) {
    var x = e.clientX, y = e.clientY;
    if (!e.detail) { var r = btn.getBoundingClientRect(); x = r.left + r.width / 2; y = r.top + r.height / 2; }
    ripple(x, y);
    on = !on;
    count += on ? 1 : -1;
    root.classList.toggle('is-on', on);
    btn.setAttribute('aria-pressed', String(on));
    rollTo(count, on);
    sr.textContent = on ? 'Subscribed. ' + fmt(count) + ' subscribers' : 'Unsubscribed';
  });
})();
</script>
--- Code end ---
