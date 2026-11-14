---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-social-share-buttons-hover/"
title: "CSS Social Share Buttons Hover"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "A row of social share icon buttons with brand-colour reveals, floating tooltips, and a URL-copy button that flashes a \"Copied!\" confirmation on click."
has_js: "true"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Social Share Buttons Hover
Source: https://codefronts.com/motion/css-animated-buttons/css-social-share-buttons-hover/

A row of social share icon buttons with brand-colour reveals, floating tooltips, and a URL-copy button that flashes a "Copied!" confirmation on click.
## HTML
```html
<div class="ab-16">
  <p class="ab-16__label">Share this article</p>
  <div class="ab-16__row">
    <button class="ab-16__btn" style="--brand:#1d9bf0" data-tooltip="Twitter / X" aria-label="Share on Twitter">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.747l7.73-8.835L1.254 2.25H8.08l4.26 5.638zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
    </button>
    <button class="ab-16__btn" style="--brand:#0a66c2" data-tooltip="LinkedIn" aria-label="Share on LinkedIn">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
    </button>
    <button class="ab-16__btn" style="--brand:#24292f" data-tooltip="GitHub" aria-label="Share on GitHub">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
    </button>
    <button class="ab-16__btn ab-16__copy" id="ab-16-copy" style="--brand:#7c3aed" data-tooltip="Copy Link" aria-label="Copy link">
      <svg class="ab-16__copy-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
</div>
```
## CSS
```css
.ab-16,
.ab-16 *,
.ab-16 *::before,
.ab-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-16 ::selection {
  background: #7c3aed;
  color: #fff;
}

.ab-16 {
  font-family: system-ui,sans-serif;
  background: #f8fafc;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  padding: 2rem;
}

.ab-16__label {
  font-size: .8rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #64748b;
}

.ab-16__row {
  display: flex;
  gap: .75rem;
}

.ab-16__btn {
  --brand: #1e293b;
  position: relative;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #1e293b;
  color: #e2e8f0;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  outline: none;
  transition: background .25s,color .25s,transform .2s,box-shadow .25s;
}

.ab-16__btn svg {
  width: 18px;
  height: 18px;
  pointer-events: none;
}

.ab-16__btn:hover {
  background: var(--brand);
  color: #fff;
  transform: translateY(-3px);
  box-shadow: 0 6px 16px rgba(0,0,0,.2);
}

.ab-16__btn:active {
  transform: translateY(0);
}

.ab-16__btn::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  background: #1e293b;
  color: #f1f5f9;
  font-size: .72rem;
  font-weight: 600;
  white-space: nowrap;
  padding: .3rem .6rem;
  border-radius: 6px;
  pointer-events: none;
  opacity: 0;
  transition: opacity .2s,transform .2s;
}

.ab-16__btn:hover::after {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}

.ab-16__copy.is-copied {
  background: #059669 !important;
  color: #fff;
  transform: translateY(-3px);
}

@media (prefers-reduced-motion: reduce) {
  .ab-16__btn {
    transition: background .1s,color .1s;
  }

  .ab-16__btn::after {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var copyBtn=document.getElementById('ab-16-copy');
  if(!copyBtn)return;
  copyBtn.addEventListener('click',function(){
    var url=window.location.href;
    if(navigator.clipboard){
      navigator.clipboard.writeText(url).then(showCopied).catch(function(){fallbackCopy(url)});
    }else{fallbackCopy(url)}
  });
  function showCopied(){
    copyBtn.classList.add('is-copied');
    copyBtn.dataset.tooltip='Copied!';
    setTimeout(function(){
      copyBtn.classList.remove('is-copied');
      copyBtn.dataset.tooltip='Copy Link';
    },1500);
  }
  function fallbackCopy(url){
    var t=document.createElement('textarea');
    t.value=url;t.style.position='fixed';t.style.opacity='0';
    document.body.appendChild(t);t.select();
    try{document.execCommand('copy');showCopied();}catch(e){}
    document.body.removeChild(t);
  }
})();
```
