---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-chat-interface-layout/"
title: "CSS Flexbox Chat Interface Layout"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "A messaging UI with a flex-row shell (contacts sidebar + message pane), scrollable message thread with pinned input bar, and live send interaction — all…"
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Chat Interface Layout
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-chat-interface-layout/

A messaging UI with a flex-row shell (contacts sidebar + message pane), scrollable message thread with pinned input bar, and live send interaction — all flex-driven.
## HTML
```html
<div class="fl-12">
  <div class="fl-12__shell">

    <!-- Contacts -->
    <div class="fl-12__contacts">
      <div class="fl-12__contacts-top">
        <div class="fl-12__app-name">
          <div class="fl-12__app-icon">💬</div>
          FlexChat
        </div>
        <div class="fl-12__search">🔍 Search...</div>
      </div>
      <div class="fl-12__contacts-list">
        <div class="fl-12__contact is-active">
          <div class="fl-12__contact-avatar" style="background:linear-gradient(135deg,#6366f1,#4f46e5)">
            AI<div class="fl-12__contact-online"></div>
          </div>
          <div class="fl-12__contact-info">
            <div class="fl-12__contact-name">Alice Indigo</div>
            <div class="fl-12__contact-preview">flex: 1 is so clean</div>
          </div>
          <div class="fl-12__contact-meta">
            <div class="fl-12__contact-time">now</div>
            <div class="fl-12__unread">2</div>
          </div>
        </div>
        <div class="fl-12__contact">
          <div class="fl-12__contact-avatar" style="background:linear-gradient(135deg,#f43f5e,#be185d)">
            BK
          </div>
          <div class="fl-12__contact-info">
            <div class="fl-12__contact-name">Bob Kira</div>
            <div class="fl-12__contact-preview">checked the PR</div>
          </div>
          <div class="fl-12__contact-meta">
            <div class="fl-12__contact-time">2m</div>
          </div>
        </div>
        <div class="fl-12__contact">
          <div class="fl-12__contact-avatar" style="background:linear-gradient(135deg,#22c55e,#15803d)">
            CW
          </div>
          <div class="fl-12__contact-info">
            <div class="fl-12__contact-name">CSS Weekly</div>
            <div class="fl-12__contact-preview">New issue is out</div>
          </div>
          <div class="fl-12__contact-meta">
            <div class="fl-12__contact-time">1h</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Message pane -->
    <div class="fl-12__pane">
      <div class="fl-12__chat-header">
        <div class="fl-12__chat-avatar">AI</div>
        <div>
          <div class="fl-12__chat-name">Alice Indigo</div>
          <div class="fl-12__chat-status">● Online</div>
        </div>
        <div class="fl-12__spacer"></div>
        <div class="fl-12__header-actions">
          <div class="fl-12__hbtn">📞</div>
          <div class="fl-12__hbtn">🎥</div>
          <div class="fl-12__hbtn">⋯</div>
        </div>
      </div>

      <div class="fl-12__messages">
        <div class="fl-12__date-divider">Today</div>

        <div class="fl-12__msg fl-12__msg--in">
          <div class="fl-12__msg-avatar" style="background:linear-gradient(135deg,#6366f1,#4f46e5)">AI</div>
          <div class="fl-12__msg-body">
            <div class="fl-12__bubble">Hey! Have you tried the new flexbox chat layout demo? The message alignment is all done with flex-direction: row-reverse for outgoing bubbles 😍</div>
            <div class="fl-12__msg-time">10:41</div>
          </div>
        </div>

        <div class="fl-12__msg fl-12__msg--out">
          <div class="fl-12__msg-avatar" style="background:linear-gradient(135deg,#f43f5e,#be185d)">Me</div>
          <div class="fl-12__msg-body">
            <div class="fl-12__bubble">Yes! The trick of using flex: 1 on the messages area and flex-shrink: 0 on the input bar is so elegant</div>
            <div class="fl-12__msg-time">10:42 ✓✓</div>
          </div>
        </div>

        <div class="fl-12__msg fl-12__msg--in">
          <div class="fl-12__msg-avatar" style="background:linear-gradient(135deg,#6366f1,#4f46e5)">AI</div>
          <div class="fl-12__msg-body">
            <div class="fl-12__bubble">Exactly. And the whole outer shell is just display: flex on the row axis — sidebar + pane side by side 💪</div>
            <div class="fl-12__msg-time">10:43</div>
          </div>
        </div>

        <div class="fl-12__typing">
          <div class="fl-12__typing-dot"></div>
          <div class="fl-12__typing-dot"></div>
          <div class="fl-12__typing-dot"></div>
        </div>
      </div>

      <div class="fl-12__input-bar">
        <div class="fl-12__input">Type a message...</div>
        <div class="fl-12__send-btn">→</div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.fl-12,
.fl-12 *,
.fl-12 *::before,
.fl-12 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-12 ::selection {
  background: #6366f1;
  color: #fff;
}

.fl-12 {
  --bg: #18181b;
  --sidebar: #111113;
  --surface: #1c1c1f;
  --border: rgba(255,255,255,0.07);
  --accent: #6366f1;
  --accent2: #f43f5e;
  --text: #e4e4e7;
  --muted: #71717a;
  --bubble-in: #27272a;
  --bubble-out: #4f46e5;
  font-family: 'Inter', sans-serif;
  background: var(--bg);
  border-radius: 16px;
  overflow: hidden;
  min-height: 500px;
}
/* Outer flex row: chat list + message pane */

.fl-12__shell {
  display: flex;
  height: 500px;
}
/* ── Contacts sidebar ── */

.fl-12__contacts {
  width: 220px;
  flex-shrink: 0;
  background: var(--sidebar);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
}

.fl-12__contacts-top {
  padding: 14px 14px 8px;
  border-bottom: 1px solid var(--border);
}

.fl-12__app-name {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.fl-12__app-icon {
  width: 22px;
  height: 22px;
  border-radius: 6px;
  background: var(--accent);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
}

.fl-12__search {
  background: rgba(255,255,255,0.06);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 6px 10px;
  font-size: 0.75rem;
  color: var(--muted);
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
}

.fl-12__contacts-list {
  flex: 1;
  overflow-y: auto;
  padding: 8px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.fl-12__contact {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.15s;
}

.fl-12__contact:hover {
  background: rgba(255,255,255,0.05);
}

.fl-12__contact.is-active {
  background: rgba(99,102,241,0.15);
}

.fl-12__contact-avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
  font-weight: 700;
  color: #fff;
  flex-shrink: 0;
  position: relative;
}

.fl-12__contact-online {
  position: absolute;
  bottom: 1px;
  right: 1px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #22c55e;
  border: 2px solid var(--sidebar);
}

.fl-12__contact-info {
  flex: 1;
  min-width: 0;
}

.fl-12__contact-name {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.fl-12__contact-preview {
  font-size: 0.68rem;
  color: var(--muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.fl-12__contact-meta {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 3px;
}

.fl-12__contact-time {
  font-size: 0.62rem;
  color: var(--muted);
}

.fl-12__unread {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--accent);
  color: #fff;
  font-size: 0.58rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
}
/* ── Message pane ── */

.fl-12__pane {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
}
/* Chat header */

.fl-12__chat-header {
  height: 52px;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  padding: 0 16px;
  gap: 10px;
  flex-shrink: 0;
}

.fl-12__chat-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #6366f1, #4f46e5);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
  font-weight: 700;
  color: #fff;
  flex-shrink: 0;
}

.fl-12__chat-name {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--text);
}

.fl-12__chat-status {
  font-size: 0.65rem;
  color: #22c55e;
  font-weight: 500;
}

.fl-12__spacer {
  flex: 1;
}

.fl-12__header-actions {
  display: flex;
  gap: 4px;
}

.fl-12__hbtn {
  width: 30px;
  height: 30px;
  border-radius: 6px;
  background: rgba(255,255,255,0.05);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  cursor: pointer;
  color: var(--muted);
  transition: background 0.15s, color 0.15s;
}

.fl-12__hbtn:hover {
  background: rgba(255,255,255,0.1);
  color: var(--text);
}
/* Messages area: flex column, flex: 1 */

.fl-12__messages {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
/* Date divider */

.fl-12__date-divider {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.65rem;
  font-weight: 600;
  color: var(--muted);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.fl-12__date-divider::before,
.fl-12__date-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border);
}
/* Message row */

.fl-12__msg {
  display: flex;
  gap: 8px;
  max-width: 85%;
}

.fl-12__msg--out {
  flex-direction: row-reverse;
  /* bubble right, avatar right */
  align-self: flex-end;
}

.fl-12__msg--in {
  align-self: flex-start;
}

.fl-12__msg-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.65rem;
  font-weight: 700;
  color: #fff;
  align-self: flex-end;
}

.fl-12__msg-body {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.fl-12__msg--out .fl-12__msg-body {
  align-items: flex-end;
}

.fl-12__bubble {
  padding: 9px 13px;
  border-radius: 16px;
  font-size: 0.8rem;
  line-height: 1.5;
  color: var(--text);
  max-width: 260px;
}

.fl-12__msg--in .fl-12__bubble {
  background: var(--bubble-in);
  border-bottom-left-radius: 4px;
}

.fl-12__msg--out .fl-12__bubble {
  background: var(--bubble-out);
  border-bottom-right-radius: 4px;
}

.fl-12__msg-time {
  font-size: 0.62rem;
  color: var(--muted);
  padding: 0 4px;
}
/* Typing indicator */

.fl-12__typing {
  display: flex;
  gap: 4px;
  padding: 10px 14px;
  background: var(--bubble-in);
  border-radius: 16px;
  border-bottom-left-radius: 4px;
  align-items: center;
  align-self: flex-start;
}

.fl-12__typing-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--muted);
  animation: fl-12-bounce 1.2s ease-in-out infinite;
}

.fl-12__typing-dot:nth-child(2) {
  animation-delay: 0.2s;
}

.fl-12__typing-dot:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes fl-12-bounce {
  0%,
    80%,
    100% {
    transform: translateY(0);
    opacity: 0.5;
  }

  40% {
    transform: translateY(-4px);
    opacity: 1;
  }
}
/* Input bar */

.fl-12__input-bar {
  background: var(--surface);
  border-top: 1px solid var(--border);
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}

.fl-12__input {
  flex: 1;
  background: rgba(255,255,255,0.06);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 8px 14px;
  font-size: 0.78rem;
  color: var(--muted);
  display: flex;
  align-items: center;
}

.fl-12__send-btn {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: var(--accent);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  cursor: pointer;
  flex-shrink: 0;
  transition: background 0.15s, transform 0.15s;
}

.fl-12__send-btn:hover {
  background: #4f46e5;
  transform: scale(1.1);
}

@media (prefers-reduced-motion: reduce) {
  .fl-12__typing-dot {
    animation: none;
  }

  .fl-12__contact,
    .fl-12__hbtn,
    .fl-12__send-btn {
    transition: none;
  }
}
```
