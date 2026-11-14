---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/typing-indicator/"
title: "Typing Indicator"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "The three bouncing dots are the convention."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Typing Indicator
Source: https://codefronts.com/snippets/css-badges/typing-indicator/

The three bouncing dots are the convention. Without the animation the badge could mean "typed recently" or "about to type." The motion defines the tense: present continuous, active right now.
## HTML
```html
<div class="bdg-02-stage">
  <div class="bdg-02-wrap">
    <div class="bdg-02-join">
      <div class="bdg-02-join-dot"></div>
      Ana Sousa joined the conversation
    </div>

    <div class="bdg-02-msg">Let me check the latest build and get back to you.</div>

    <div class="bdg-02-msg bdg-02-sent">Sure — does the badge spec look right to you?</div>

    <div class="bdg-02-bubble">
      <div class="bdg-02-inner">
        <svg class="bdg-02-avatar" viewBox="0 0 20 20" aria-hidden="true">
          <circle cx="10" cy="10" r="10" fill="#3d7ebf"/>
          <text x="10" y="14.5" text-anchor="middle" font-size="10" fill="white" font-family="sans-serif" font-weight="bold">A</text>
        </svg>
        <span class="bdg-02-name">Ana</span>
        <div class="bdg-02-dots">
          <div class="bdg-02-dot"></div>
          <div class="bdg-02-dot"></div>
          <div class="bdg-02-dot"></div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-02-stage {
  background: #ebe4d8;
  padding: 40px 36px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-02-wrap {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 100%;
  max-width: 360px;
}

.bdg-02-msg {
  align-self: flex-end;
  background: #fff;
  border-radius: 18px 18px 4px 18px;
  padding: 10px 16px;
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 14px;
  color: #2a2018;
  box-shadow: 0 1px 4px rgba(0,0,0,0.08);
  max-width: 80%;
}

.bdg-02-sent {
  background: #1a1612;
  color: #f0ece0;
  border-radius: 18px 18px 18px 4px;
  align-self: flex-start;
}

.bdg-02-bubble {
  align-self: flex-start;
}

.bdg-02-inner {
  background: #fff;
  border-radius: 18px 18px 18px 4px;
  padding: 12px 16px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.08);
}

.bdg-02-avatar {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  flex-shrink: 0;
}

.bdg-02-name {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 11px;
  letter-spacing: 0.08em;
  color: #888;
  text-transform: uppercase;
}

.bdg-02-dots {
  display: flex;
  gap: 3px;
  align-items: center;
}

.bdg-02-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #aaa;
}

.bdg-02-dot:nth-child(1) {
  animation: bdg-02-bounce 1.4s ease-in-out infinite 0ms;
}

.bdg-02-dot:nth-child(2) {
  animation: bdg-02-bounce 1.4s ease-in-out infinite 160ms;
}

.bdg-02-dot:nth-child(3) {
  animation: bdg-02-bounce 1.4s ease-in-out infinite 320ms;
}

@keyframes bdg-02-bounce {
  0%,
    60%,
    100% {
    transform: translateY(0);
  }

  30% {
    transform: translateY(-5px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-02-dot {
    animation: none;
  }
}

.bdg-02-join {
  align-self: center;
  background: rgba(255,255,255,0.7);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border-radius: 20px;
  padding: 6px 14px;
  display: flex;
  align-items: center;
  gap: 7px;
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 11px;
  letter-spacing: 0.06em;
  color: #666;
  box-shadow: 0 1px 4px rgba(0,0,0,0.1);
}

.bdg-02-join-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #0cce6b;
}
```
