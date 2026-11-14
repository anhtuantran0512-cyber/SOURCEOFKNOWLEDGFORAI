---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-windows-95-desktop-interface/"
title: "Tailwind Windows 95 Desktop Interface"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "A full desktop: icon field, taskbar with a working Start menu, a window with title bar and system buttons, and a dialog."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Windows 95 Desktop Interface
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-windows-95-desktop-interface/

A full desktop: icon field, taskbar with a working Start menu, a window with title bar and system buttons, and a dialog. Every raised and sunken edge is the four-inset bevel as a named @utility, and the Start menu drops its :has() rule entirely &mdash; a peer-checked: variant does the same job from the markup, which is the port's cleanest simplification.
## HTML
```html
<section class="twr-09 relative block w-full min-h-svh box-border bg-twr09-desktop text-[#101010] font-twr09-sans" aria-labelledby="twr-09-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-09-title">Windows 95 style desktop interface</h2>

  <div class="absolute top-3 right-3 z-20">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-09-theme">
    <label class="grid place-items-center size-11 cursor-pointer bg-twr09-face text-[#101010] twr09-raised peer-focus-visible:outline-2 peer-focus-visible:outline-dotted peer-focus-visible:outline-twr09-dk peer-focus-visible:outline-offset-[-6px]" for="twr-09-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark surround</span>
    </label>
  </div>

  <div class="min-h-svh max-w-[76rem] mx-auto grid grid-cols-[minmax(0,1fr)] content-start gap-5 px-[clamp(0.6rem,0.4rem+1.5vw,2rem)] pt-4 pb-[calc(56px+1.5rem)] lg:grid-cols-[7rem_minmax(0,1fr)] lg:items-start">
    <ul class="list-none m-0 p-0 flex flex-wrap gap-2 lg:flex-col">
      <li><button class="w-[88px] min-h-[88px] px-1 py-2 border-0 cursor-pointer bg-transparent font-inherit text-[0.72rem] leading-tight text-white grid justify-items-center gap-1.5 [text-shadow:1px_1px_0_rgba(0,0,0,0.6)] focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-white focus-visible:outline-offset-[-3px]" type="button"><span class="block w-[30px] h-[26px] [background:linear-gradient(#e8e8e0_60%,#9a9a92_60%)] [clip-path:polygon(6%_0,94%_0,94%_62%,66%_62%,72%_80%,28%_80%,34%_62%,6%_62%)]" aria-hidden="true"></span>My Computer</button></li>
      <li><button class="w-[88px] min-h-[88px] px-1 py-2 border-0 cursor-pointer bg-transparent font-inherit text-[0.72rem] leading-tight text-white grid justify-items-center gap-1.5 [text-shadow:1px_1px_0_rgba(0,0,0,0.6)] focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-white focus-visible:outline-offset-[-3px]" type="button"><span class="block w-[30px] h-[26px] bg-[#cfd6de] [clip-path:polygon(0_20%,46%_20%,46%_0,100%_0,100%_62%,54%_62%,54%_82%,0_82%)]" aria-hidden="true"></span>Network</button></li>
      <li><button class="w-[88px] min-h-[88px] px-1 py-2 border-0 cursor-pointer bg-transparent font-inherit text-[0.72rem] leading-tight text-white grid justify-items-center gap-1.5 [text-shadow:1px_1px_0_rgba(0,0,0,0.6)] focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-white focus-visible:outline-offset-[-3px]" type="button"><span class="block w-[30px] h-[26px] [background:linear-gradient(#cfd2cf,#8f938f)] [clip-path:polygon(18%_12%,82%_12%,74%_100%,26%_100%)]" aria-hidden="true"></span>Recycle Bin</button></li>
    </ul>

    <div class="min-w-0 grid gap-5">
      <div class="min-w-0 p-[3px] bg-twr09-face twr09-raised">
        <div class="flex items-center gap-1.5 min-w-0 m-[3px] py-1 pe-1 ps-2 [background:linear-gradient(90deg,var(--color-twr09-capa),var(--color-twr09-capb))]">
          <span class="flex-none size-4 bg-[#f4f4ee] [clip-path:polygon(0_0,70%_0,100%_26%,100%_100%,0_100%)]" aria-hidden="true"></span>
          <span class="flex-1 min-w-0 overflow-hidden text-ellipsis whitespace-nowrap text-white text-[0.85rem] font-bold">Program Manager</span>
          <span class="flex flex-none gap-0.5">
            <button class="grid place-items-center size-11 p-0 border-0 cursor-pointer bg-twr09-face twr09-raised active:twr09-sunken focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-7px]" type="button" aria-label="Minimise"><i class="block w-2.5 h-[3px] mt-2 bg-[#101010]" aria-hidden="true"></i></button>
            <button class="grid place-items-center size-11 p-0 border-0 cursor-pointer bg-twr09-face twr09-raised active:twr09-sunken focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-7px]" type="button" aria-label="Maximise"><i class="block w-3 h-2.5 border-2 border-t-[3px] border-[#101010]" aria-hidden="true"></i></button>
            <button class="grid place-items-center size-11 p-0 border-0 cursor-pointer bg-twr09-face twr09-raised active:twr09-sunken focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-7px]" type="button" aria-label="Close"><i class="block size-3 [background-image:linear-gradient(45deg,transparent_44%,#101010_44%_56%,transparent_56%),linear-gradient(-45deg,transparent_44%,#101010_44%_56%,transparent_56%)]" aria-hidden="true"></i></button>
          </span>
        </div>
        <nav class="mx-[3px] min-w-0" aria-label="Program Manager menu">
          <ul class="list-none m-0 p-0 flex flex-wrap">
            <li><button class="min-h-11 min-w-11 px-2.5 border-0 bg-transparent font-inherit text-[0.82rem] text-[#101010] cursor-pointer hover:bg-twr09-capa hover:text-white focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-5px]" type="button"><u>F</u>ile</button></li>
            <li><button class="min-h-11 min-w-11 px-2.5 border-0 bg-transparent font-inherit text-[0.82rem] text-[#101010] cursor-pointer hover:bg-twr09-capa hover:text-white focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-5px]" type="button"><u>E</u>dit</button></li>
            <li><button class="min-h-11 min-w-11 px-2.5 border-0 bg-transparent font-inherit text-[0.82rem] text-[#101010] cursor-pointer hover:bg-twr09-capa hover:text-white focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-5px]" type="button"><u>V</u>iew</button></li>
            <li><button class="min-h-11 min-w-11 px-2.5 border-0 bg-transparent font-inherit text-[0.82rem] text-[#101010] cursor-pointer hover:bg-twr09-capa hover:text-white focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-5px]" type="button"><u>H</u>elp</button></li>
          </ul>
        </nav>
        <div class="m-[3px] p-3 min-w-0 bg-white twr09-well">
          <ul class="list-none m-0 p-0 grid gap-2 grid-cols-[repeat(auto-fill,minmax(min(100%,8rem),1fr))]">
            <li><span class="flex items-center gap-2 min-h-11 min-w-0 px-2 py-1.5 text-[0.82rem]"><i class="flex-none block size-[18px] bg-[#f4f4ee] [clip-path:polygon(0_0,70%_0,100%_26%,100%_100%,0_100%)]" aria-hidden="true"></i>Notepad</span></li>
            <li><span class="flex items-center gap-2 min-h-11 min-w-0 px-2 py-1.5 text-[0.82rem]"><i class="flex-none block size-[18px] bg-[#f4f4ee] [clip-path:polygon(0_0,70%_0,100%_26%,100%_100%,0_100%)]" aria-hidden="true"></i>Paint</span></li>
            <li><span class="flex items-center gap-2 min-h-11 min-w-0 px-2 py-1.5 text-[0.82rem]"><i class="flex-none block size-[18px] bg-[#f4f4ee] [clip-path:polygon(0_0,70%_0,100%_26%,100%_100%,0_100%)]" aria-hidden="true"></i>Minesweeper</span></li>
            <li><span class="flex items-center gap-2 min-h-11 min-w-0 px-2 py-1.5 text-[0.82rem]"><i class="flex-none block size-[18px] bg-[#f4f4ee] [clip-path:polygon(0_0,70%_0,100%_26%,100%_100%,0_100%)]" aria-hidden="true"></i>Defrag</span></li>
          </ul>
        </div>
        <div class="flex flex-wrap gap-[3px] m-[3px]">
          <span class="flex-1 basis-32 min-w-0 px-2.5 py-1.5 text-[0.78rem] [box-shadow:inset_1px_1px_0_0_var(--color-twr09-sh),inset_-1px_-1px_0_0_var(--color-twr09-hi)]">4 objects</span>
          <span class="flex-1 basis-32 min-w-0 px-2.5 py-1.5 text-[0.78rem] [box-shadow:inset_1px_1px_0_0_var(--color-twr09-sh),inset_-1px_-1px_0_0_var(--color-twr09-hi)]">Memory: 71% free</span>
        </div>
      </div>

      <dialog class="static m-0 min-w-0 max-w-[30rem] justify-self-start p-[3px] border-0 bg-twr09-face text-[#101010] twr09-raised" open aria-labelledby="twr-09-dlg-t">
        <div class="flex items-center gap-1.5 min-w-0 m-[3px] py-1 pe-1 ps-2 [background:linear-gradient(90deg,var(--color-twr09-capa),var(--color-twr09-capb))]">
          <span class="flex-1 min-w-0 overflow-hidden text-ellipsis whitespace-nowrap text-white text-[0.85rem] font-bold" id="twr-09-dlg-t">Confirm File Delete</span>
          <span class="flex flex-none gap-0.5">
            <button class="grid place-items-center size-11 p-0 border-0 cursor-pointer bg-twr09-face twr09-raised active:twr09-sunken focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-7px]" type="button" aria-label="Close dialog"><i class="block size-3 [background-image:linear-gradient(45deg,transparent_44%,#101010_44%_56%,transparent_56%),linear-gradient(-45deg,transparent_44%,#101010_44%_56%,transparent_56%)]" aria-hidden="true"></i></button>
          </span>
        </div>
        <div class="flex items-start gap-3.5 min-w-0 px-3 py-4">
          <span class="flex-none grid place-items-center size-[34px] rounded-full bg-twr09-capa text-white font-bold text-xl" aria-hidden="true">?</span>
          <p class="m-0 min-w-0 text-[0.88rem] leading-normal text-pretty">Are you sure you want to send AUTOEXEC.BAT to the Recycle Bin?</p>
        </div>
        <div class="flex flex-wrap gap-2 px-3 pb-3.5">
          <button class="min-h-11 min-w-[5.5rem] px-4 py-2 border-0 cursor-pointer font-inherit text-[0.85rem] bg-twr09-face text-[#101010] twr09-raised active:twr09-sunken focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-6px] [box-shadow:inset_0_0_0_1px_var(--color-twr09-dk)]" type="button">Yes</button>
          <button class="min-h-11 min-w-[5.5rem] px-4 py-2 border-0 cursor-pointer font-inherit text-[0.85rem] bg-twr09-face text-[#101010] twr09-raised active:twr09-sunken focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-6px]" type="button">No</button>
        </div>
      </dialog>
    </div>
  </div>

  <div class="absolute inset-x-0 bottom-0 z-15 flex items-center gap-1 min-w-0 min-h-14 p-[3px] bg-twr09-face [box-shadow:inset_0_var(--twr-09-b)_0_0_var(--color-twr09-hi),inset_0_calc(var(--twr-09-b)*2)_0_0_var(--color-twr09-lt)]">
    <input class="peer absolute size-px opacity-0 m-0" type="checkbox" id="twr-09-start">
    <label class="flex flex-none items-center gap-1.5 min-h-11 px-3 py-1.5 font-bold text-[0.88rem] cursor-pointer bg-twr09-face twr09-raised peer-checked:twr09-sunken peer-focus-visible:outline-2 peer-focus-visible:outline-dotted peer-focus-visible:outline-twr09-dk peer-focus-visible:outline-offset-[-6px]" for="twr-09-start">
      <span class="flex-none w-[18px] h-4 [background:linear-gradient(135deg,#ff3b30_0_50%,#ffd60a_50%_100%)] [clip-path:polygon(0_14%,46%_0,100%_10%,100%_88%,46%_100%,0_86%)]" aria-hidden="true"></span>Start
    </label>
    <nav class="absolute bottom-[calc(100%+3px)] left-[3px] w-[min(20rem,calc(100vw-1.5rem))] hidden peer-checked:flex p-[3px] bg-twr09-face twr09-raised" aria-label="Start menu">
      <span class="flex-none w-[30px] grid items-end justify-items-center py-2.5 text-white font-bold text-[0.9rem] tracking-[0.04em] [background:linear-gradient(180deg,#000080,#1084d0)] [writing-mode:vertical-rl] rotate-180" aria-hidden="true">Windows 95</span>
      <ul class="list-none m-0 p-1 flex-1 min-w-0">
        <li><button class="w-full min-h-11 flex items-center gap-2.5 px-2.5 py-2 border-0 bg-transparent font-inherit text-[0.88rem] text-[#101010] text-start cursor-pointer hover:bg-twr09-capa hover:text-white focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-5px]" type="button"><i class="flex-none block size-[18px] bg-[#f4f4ee] [clip-path:polygon(0_0,70%_0,100%_26%,100%_100%,0_100%)]" aria-hidden="true"></i>Programs</button></li>
        <li><button class="w-full min-h-11 flex items-center gap-2.5 px-2.5 py-2 border-0 bg-transparent font-inherit text-[0.88rem] text-[#101010] text-start cursor-pointer hover:bg-twr09-capa hover:text-white focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-5px]" type="button"><i class="flex-none block size-[18px] bg-[#f4f4ee] [clip-path:polygon(0_0,70%_0,100%_26%,100%_100%,0_100%)]" aria-hidden="true"></i>Documents</button></li>
        <li><button class="w-full min-h-11 flex items-center gap-2.5 px-2.5 py-2 border-0 bg-transparent font-inherit text-[0.88rem] text-[#101010] text-start cursor-pointer hover:bg-twr09-capa hover:text-white focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-5px]" type="button"><i class="flex-none block size-[18px] bg-[#f4f4ee] [clip-path:polygon(0_0,70%_0,100%_26%,100%_100%,0_100%)]" aria-hidden="true"></i>Settings</button></li>
        <li><button class="w-full min-h-11 flex items-center gap-2.5 px-2.5 py-2 border-0 bg-transparent font-inherit text-[0.88rem] text-[#101010] text-start cursor-pointer hover:bg-twr09-capa hover:text-white focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-5px]" type="button"><i class="flex-none block size-[18px] bg-[#f4f4ee] [clip-path:polygon(0_0,70%_0,100%_26%,100%_100%,0_100%)]" aria-hidden="true"></i>Find</button></li>
        <li class="h-0.5 mx-1.5 my-1.5 [box-shadow:inset_0_1px_0_0_var(--color-twr09-sh),inset_0_-1px_0_0_var(--color-twr09-hi)]"></li>
        <li><button class="w-full min-h-11 flex items-center gap-2.5 px-2.5 py-2 border-0 bg-transparent font-inherit text-[0.88rem] text-[#101010] text-start cursor-pointer hover:bg-twr09-capa hover:text-white focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-5px]" type="button"><i class="flex-none block size-[18px] bg-[#f4f4ee] [clip-path:polygon(0_0,70%_0,100%_26%,100%_100%,0_100%)]" aria-hidden="true"></i>Shut Down&hellip;</button></li>
      </ul>
    </nav>
    <ul class="list-none m-0 p-0 flex flex-1 gap-[3px] min-w-0 overflow-hidden">
      <li><button class="min-h-11 max-w-48 min-w-0 px-2.5 py-1.5 border-0 cursor-pointer font-inherit text-[0.8rem] font-bold bg-twr09-face text-[#101010] overflow-hidden text-ellipsis whitespace-nowrap twr09-sunken [background-image:repeating-conic-gradient(var(--color-twr09-hi)_0%_25%,var(--color-twr09-face)_0%_50%)] [background-size:2px_2px] focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-6px]" type="button">Program Manager</button></li>
      <li><button class="min-h-11 max-w-48 min-w-0 px-2.5 py-1.5 border-0 cursor-pointer font-inherit text-[0.8rem] bg-twr09-face text-[#101010] overflow-hidden text-ellipsis whitespace-nowrap twr09-raised active:twr09-sunken focus-visible:outline-2 focus-visible:outline-dotted focus-visible:outline-twr09-dk focus-visible:outline-offset-[-6px]" type="button">Read Me</button></li>
    </ul>
    <span class="flex flex-none items-center gap-1.5 min-h-11 px-2.5 text-[0.8rem] tabular-nums [box-shadow:inset_1px_1px_0_0_var(--color-twr09-sh),inset_-1px_-1px_0_0_var(--color-twr09-hi)]"><span class="size-3.5 bg-[#6a6a62] [clip-path:polygon(0_34%,30%_34%,62%_6%,62%_94%,30%_66%,0_66%)]" aria-hidden="true"></span>11:42</span>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr09-face: #c0c0c0;
  --color-twr09-hi: #ffffff;
  --color-twr09-lt: #dfdfdf;
  --color-twr09-sh: #808080;
  --color-twr09-dk: #000000;
  --color-twr09-capa: #000080;
  --color-twr09-capb: #1084d0;
  --color-twr09-desktop: #008080;
  --font-twr09-sans: system-ui, -apple-system, 'Segoe UI', Tahoma, Verdana, Arial, sans-serif;
  --font-twr09-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

.twr-09 {
  --twr-09-b: 2px;
}

@utility twr09-raised {
  box-shadow: inset var(--twr-09-b) var(--twr-09-b) 0 0 var(--color-twr09-hi), inset calc(var(--twr-09-b) * -1) calc(var(--twr-09-b) * -1) 0 0 var(--color-twr09-dk), inset calc(var(--twr-09-b) * 2) calc(var(--twr-09-b) * 2) 0 0 var(--color-twr09-lt), inset calc(var(--twr-09-b) * -2) calc(var(--twr-09-b) * -2) 0 0 var(--color-twr09-sh);
}

@utility twr09-sunken {
  box-shadow: inset var(--twr-09-b) var(--twr-09-b) 0 0 var(--color-twr09-dk), inset calc(var(--twr-09-b) * -1) calc(var(--twr-09-b) * -1) 0 0 var(--color-twr09-hi), inset calc(var(--twr-09-b) * 2) calc(var(--twr-09-b) * 2) 0 0 var(--color-twr09-sh), inset calc(var(--twr-09-b) * -2) calc(var(--twr-09-b) * -2) 0 0 var(--color-twr09-lt);
}

@utility twr09-well {
  box-shadow: inset var(--twr-09-b) var(--twr-09-b) 0 0 var(--color-twr09-sh), inset calc(var(--twr-09-b) * -1) calc(var(--twr-09-b) * -1) 0 0 var(--color-twr09-hi), inset calc(var(--twr-09-b) * 2) calc(var(--twr-09-b) * 2) 0 0 var(--color-twr09-dk), inset calc(var(--twr-09-b) * -2) calc(var(--twr-09-b) * -2) 0 0 var(--color-twr09-lt);
}

.twr-09:has(#twr-09-theme:checked) {
  --color-twr09-desktop: #06393c;
  --color-twr09-desktop: oklch(0.31 0.05 197);
}
```
