---
source: "lucianlabs"
id: "042"
title: "Step-by-step wizard"
category: "Menus & Tabs"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#042"
tags: ["stepper", "wizard", "onboarding", "progress", "steps"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Step-by-step wizard (042, Menus & Tabs)
[What it does] Press Next and the progress line fills up to the next circle while finished steps turn into checks. The content slides in the direction you are moving, and on the last step the button becomes “Get started”.
[How to use it] Use Next and Back to move between steps. You can also press a finished step’s circle to go back

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
<!-- Lucian UX/UI Prompt #042 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#042 -->
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
.u042{position:relative;width:350px;height:400px;display:flex;flex-direction:column;padding:22px 20px 18px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong)}
.u042-steps{position:relative;display:flex;justify-content:space-between;margin:0 6px;padding:0;list-style:none}
.u042-line{position:absolute;left:17px;right:17px;top:16px;height:3px;border-radius:2px;background:var(--ux-surface-3)}
.u042-line i{position:absolute;inset:0;border-radius:inherit;background:var(--ux-grad);transform-origin:0 50%;transform:scaleX(var(--p,0));transition:transform .6s var(--ux-ease)}
.u042-st{position:relative;display:flex;flex-direction:column;align-items:center;gap:7px;width:34px}
.u042-dot{position:relative;width:34px;height:34px;border:0;padding:0;border-radius:50%;background:var(--ux-surface);box-shadow:inset 0 0 0 2px var(--ux-line-2);font-size:13.5px;font-weight:780;color:var(--ux-ink-3);display:grid;place-items:center;transition:box-shadow .35s,background-color .35s,color .35s,transform .45s var(--ux-spring)}
.u042-dot:focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
.u042-dot svg{position:absolute;width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;opacity:0}
.u042-dot path{stroke-dasharray:16;stroke-dashoffset:16;transition:stroke-dashoffset .35s var(--ux-ease) .1s}
.u042-st.cur .u042-dot{box-shadow:inset 0 0 0 2px var(--ux-accent),0 0 0 5px var(--ux-accent-soft);color:var(--ux-accent);transform:scale(1.08)}
.u042-st.done .u042-dot{background:var(--ux-accent);box-shadow:none;color:var(--ux-accent-ink);cursor:pointer}
.u042-st.done .u042-dot span{opacity:0}
.u042-st.done .u042-dot svg{opacity:1}
.u042-st.done .u042-dot path{stroke-dashoffset:0}
.u042-st small{font-size:11.5px;font-weight:700;color:var(--ux-ink-3);white-space:nowrap;transition:color .3s}
.u042-st.cur small,.u042-st.done small{color:var(--ux-ink)}
.u042-view{position:relative;flex:1;margin-top:22px;overflow:hidden}
.u042-pane{position:absolute;inset:0;transition:transform .55s var(--ux-ease),opacity .35s var(--ux-ease)}
.u042-pane h4{margin:0;font-size:19px;font-weight:780;letter-spacing:-.03em}
.u042-pane p{margin:5px 0 16px;font-size:13.5px;color:var(--ux-ink-3)}
.u042-fld{display:flex;align-items:center;gap:10px;height:50px;padding:0 14px;border-radius:14px;background:var(--ux-surface-2);font-size:15px;font-weight:620;margin-bottom:8px}
.u042-url{color:var(--ux-ink-3);font-weight:560}
.u042-url b{color:var(--ux-ink);font-weight:700}
.u042-fld small{margin-left:auto;font-size:12px;color:var(--ux-ink-3)}
.u042-chips{display:flex;gap:6px}
.u042-chips span{padding:8px 12px;border-radius:999px;font-size:13px;font-weight:650;box-shadow:inset 0 0 0 1px var(--ux-line-2);color:var(--ux-ink-2)}
.u042-chips span.on{background:var(--ux-ink);color:var(--ux-page);box-shadow:none}
.u042-av{width:30px;height:30px;flex:none;border-radius:50%;background:var(--c)}
.u042-done{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;text-align:center}
.u042-big{width:76px;height:76px;border-radius:50%;display:grid;place-items:center;background:var(--ux-mint);color:var(--ux-accent-ink);box-shadow:0 0 0 10px color-mix(in srgb,var(--ux-mint) 18%,transparent);transform:scale(.5);transition:transform .6s var(--ux-spring) .2s}
.u042-big svg{width:34px;height:34px;fill:none;stroke:currentColor;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}
.u042-pane.on .u042-big{transform:none}
.u042-done h4{margin-top:18px}
.u042-foot{display:flex;gap:8px;margin-top:12px}
.u042-b{height:50px;border:0;border-radius:15px;font-size:15px;font-weight:700;transition:transform .35s var(--ux-spring),opacity .3s,background-color .3s}
.u042-b:active{transform:scale(.96)}
.u042-b:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u042-prev{width:96px;background:var(--ux-surface-2);color:var(--ux-ink)}
.u042-prev[aria-disabled="true"]{opacity:.35}
.u042-next{flex:1;background:var(--ux-ink);color:var(--ux-page)}
.u042.is-last .u042-next{background:var(--ux-mint);color:var(--ux-accent-ink)}
</style>
<div class="ux u042">
  <ol class="u042-steps" aria-label="Sign-up steps">
    <li class="u042-line" aria-hidden="true"><i></i></li>
    <li class="u042-st"><button class="u042-dot" type="button" tabindex="-1"><span>1</span><svg viewBox="0 0 16 16"><path d="M3.5 8.4l3 3 6-6.4"/></svg></button><small>Account</small></li>
    <li class="u042-st"><button class="u042-dot" type="button" tabindex="-1"><span>2</span><svg viewBox="0 0 16 16"><path d="M3.5 8.4l3 3 6-6.4"/></svg></button><small>Workspace</small></li>
    <li class="u042-st"><button class="u042-dot" type="button" tabindex="-1"><span>3</span><svg viewBox="0 0 16 16"><path d="M3.5 8.4l3 3 6-6.4"/></svg></button><small>Invite</small></li>
    <li class="u042-st"><button class="u042-dot" type="button" tabindex="-1"><span>4</span><svg viewBox="0 0 16 16"><path d="M3.5 8.4l3 3 6-6.4"/></svg></button><small>Done</small></li>
  </ol>
  <div class="u042-view" aria-live="polite">
    <section class="u042-pane"><h4>What should we call you?</h4><p>This is the name your team will see</p><div class="u042-fld">Seoyeon Kim<small>Name</small></div><div class="u042-chips"><span class="on">Designer</span><span>Developer</span><span>PM</span></div></section>
    <section class="u042-pane"><h4>Create a workspace</h4><p>You can change this anytime</p><div class="u042-fld">Lumen Design<small>Name</small></div><div class="u042-fld"><span class="u042-url">lumen.app/<b>design</b></span><small>URL</small></div></section>
    <section class="u042-pane"><h4>Invite your teammates</h4><p>Invites go out right away</p><div class="u042-fld"><span class="u042-av" style="--c:linear-gradient(140deg,#FFB547,#FF7A45)"></span>jun@example.com<small>Editor</small></div><div class="u042-fld"><span class="u042-av" style="--c:linear-gradient(140deg,#22C3A6,#0EA5E9)"></span>mina@example.com<small>Viewer</small></div></section>
    <section class="u042-pane"><div class="u042-done"><span class="u042-big"><svg viewBox="0 0 34 34"><path d="M9 17.5l5.5 5.5L25.5 12"/></svg></span><h4>You’re all set</h4><p>Welcome to Lumen Design</p></div></section>
  </div>
  <div class="u042-foot"><button class="u042-b u042-prev" type="button">Back</button><button class="u042-b u042-next" type="button">Next</button></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sts = Array.prototype.slice.call(root.querySelectorAll('.u042-st'));
  var panes = Array.prototype.slice.call(root.querySelectorAll('.u042-pane'));
  var line = root.querySelector('.u042-line i');
  var prev = root.querySelector('.u042-prev'), next = root.querySelector('.u042-next');
  var cur = -1;
  function go(i) {
    if (i < 0 || i > 3 || i === cur) return;
    var dir = i > cur ? 1 : -1;
    panes.forEach(function (p, k) {
      p.classList.toggle('on', k === i);
      p.setAttribute('aria-hidden', String(k !== i));
      p.style.opacity = k === i ? '1' : '0';
      p.style.transform = k === i ? 'none' : 'translateX(' + (k < i ? -40 : 40) + '%)';
      if (k === i && cur >= 0) {
        p.style.transition = 'none';
        p.style.transform = 'translateX(' + (dir * 40) + '%)'; p.style.opacity = '0';
        void p.offsetWidth;
        p.style.transition = '';
        p.style.transform = 'none'; p.style.opacity = '1';
      }
    });
    cur = i;
    sts.forEach(function (s, k) {
      s.classList.toggle('done', k < i);
      s.classList.toggle('cur', k === i);
      var d = s.querySelector('.u042-dot');
      d.tabIndex = k < i ? 0 : -1;
      d.setAttribute('aria-label', 'Step ' + (k + 1) + ', ' + s.querySelector('small').textContent + (k < i ? ', done. Press to go back' : k === i ? ', current step' : ''));
      if (k === i) d.setAttribute('aria-current', 'step'); else d.removeAttribute('aria-current');
    });
    line.parentNode.style.setProperty('--p', (i / 3).toFixed(3));
    prev.setAttribute('aria-disabled', String(i === 0));
    root.classList.toggle('is-last', i === 3);
    next.textContent = i === 3 ? 'Get started' : 'Next';
  }
  next.addEventListener('click', function () {
    if (cur === 3) { next.textContent = 'Welcome!'; setTimeout(function () { if (root.isConnected) go(0); }, 900); return; }
    go(cur + 1);
  });
  prev.addEventListener('click', function () { go(cur - 1); });
  sts.forEach(function (s, k) { s.querySelector('.u042-dot').addEventListener('click', function () { if (k < cur) go(k); }); });
  go(0);
})();
</script>
--- Code end ---
