---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/content-tag-card/"
title: "Content Tag Card"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "Colored pill labels (Machine Learning, DevOps, Security) that lift on hover and reveal a tag-detail card — colored icon block, article count, description,…"
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Content Tag Card
Source: https://codefronts.com/snippets/css-tooltips/content-tag-card/

Colored pill labels (Machine Learning, DevOps, Security) that lift on hover and reveal a tag-detail card — colored icon block, article count, description, popularity-this-month bar with trend, related-tag pills, and the top three articles in this tag. For blog tag clouds, knowledge bases, content discovery surfaces.
## HTML
```html
<div class="tp-12">
  <div class="tp-12__inner">
    <div class="tp-12__list">
      <div class="tp-12__t">
        <div class="tp-12__pill" style="background:#eff6ff;border-color:#bfdbfe;color:#1e40af"><span class="tp-12__dot" style="background:#3b82f6"></span>Machine Learning</div>
        <div class="tp-12__tip">
          <div class="tp-12__head">
            <div class="tp-12__head-row"><div class="tp-12__icon" style="background:#dbeafe;color:#1e40af">ML</div><div><div class="tp-12__name">Machine Learning</div><div class="tp-12__count">1,284 articles</div></div></div>
            <div class="tp-12__desc">Algorithms that enable systems to learn from data without explicit programming. Covers supervised, unsupervised, and reinforcement learning.</div>
          </div>
          <div class="tp-12__pop">
            <div class="tp-12__pop-label">Popularity this month</div>
            <div class="tp-12__track"><div class="tp-12__fill" style="width:88%;background:#3b82f6"></div></div>
            <div class="tp-12__trend"><span class="tp-12__trend-left"><strong>↑ trending</strong></span><span>+14% vs last month</span></div>
          </div>
          <div class="tp-12__rel">
            <div class="tp-12__rel-label">Related</div>
            <div class="tp-12__rel-pills"><span class="tp-12__rel-pill">Deep Learning</span><span class="tp-12__rel-pill">Neural Nets</span><span class="tp-12__rel-pill">PyTorch</span></div>
          </div>
          <div class="tp-12__ex">
            <div class="tp-12__ex-label">Top articles</div>
            <div class="tp-12__ex-item">Fine-tuning LLMs on custom datasets</div>
            <div class="tp-12__ex-item">Understanding transformer attention</div>
            <div class="tp-12__ex-item">Gradient descent, explained visually</div>
          </div>
        </div>
      </div>

      <div class="tp-12__t">
        <div class="tp-12__pill" style="background:#f0fdf4;border-color:#bbf7d0;color:#15803d"><span class="tp-12__dot" style="background:#22c55e"></span>Open Source</div>
        <div class="tp-12__tip">
          <div class="tp-12__head">
            <div class="tp-12__head-row"><div class="tp-12__icon" style="background:#dcfce7;color:#15803d">OS</div><div><div class="tp-12__name">Open Source</div><div class="tp-12__count">2,941 articles</div></div></div>
            <div class="tp-12__desc">Software with source code available for anyone to use, inspect, modify, and distribute. Covers licensing, contributing, and ecosystem news.</div>
          </div>
          <div class="tp-12__pop">
            <div class="tp-12__pop-label">Popularity this month</div>
            <div class="tp-12__track"><div class="tp-12__fill" style="width:94%;background:#22c55e"></div></div>
            <div class="tp-12__trend"><span class="tp-12__trend-left"><strong>↑ all-time high</strong></span><span>+22% vs last month</span></div>
          </div>
          <div class="tp-12__rel">
            <div class="tp-12__rel-label">Related</div>
            <div class="tp-12__rel-pills"><span class="tp-12__rel-pill">GitHub</span><span class="tp-12__rel-pill">Linux</span><span class="tp-12__rel-pill">Licensing</span></div>
          </div>
          <div class="tp-12__ex">
            <div class="tp-12__ex-label">Top articles</div>
            <div class="tp-12__ex-item">How to write a great README</div>
            <div class="tp-12__ex-item">OSS licensing: MIT vs Apache vs GPL</div>
            <div class="tp-12__ex-item">First PR tips for new contributors</div>
          </div>
        </div>
      </div>

      <div class="tp-12__t">
        <div class="tp-12__pill" style="background:#fdf4ff;border-color:#e9d5ff;color:#7e22ce"><span class="tp-12__dot" style="background:#a855f7"></span>System Design</div>
        <div class="tp-12__tip">
          <div class="tp-12__head">
            <div class="tp-12__head-row"><div class="tp-12__icon" style="background:#f3e8ff;color:#7e22ce">SD</div><div><div class="tp-12__name">System Design</div><div class="tp-12__count">876 articles</div></div></div>
            <div class="tp-12__desc">The process of defining the architecture, components, and interfaces of a system to satisfy specified requirements at scale.</div>
          </div>
          <div class="tp-12__pop">
            <div class="tp-12__pop-label">Popularity this month</div>
            <div class="tp-12__track"><div class="tp-12__fill" style="width:76%;background:#a855f7"></div></div>
            <div class="tp-12__trend"><span class="tp-12__trend-left"><strong>→ stable</strong></span><span>+3% vs last month</span></div>
          </div>
          <div class="tp-12__rel">
            <div class="tp-12__rel-label">Related</div>
            <div class="tp-12__rel-pills"><span class="tp-12__rel-pill">Distributed</span><span class="tp-12__rel-pill">CAP Theorem</span><span class="tp-12__rel-pill">Databases</span></div>
          </div>
          <div class="tp-12__ex">
            <div class="tp-12__ex-label">Top articles</div>
            <div class="tp-12__ex-item">Designing a rate limiter from scratch</div>
            <div class="tp-12__ex-item">When to use a message queue</div>
            <div class="tp-12__ex-item">Read replicas and write-ahead logs</div>
          </div>
        </div>
      </div>

      <div class="tp-12__t">
        <div class="tp-12__pill" style="background:#fff7ed;border-color:#fed7aa;color:#c2410c"><span class="tp-12__dot" style="background:#f97316"></span>Career</div>
        <div class="tp-12__tip">
          <div class="tp-12__head">
            <div class="tp-12__head-row"><div class="tp-12__icon" style="background:#ffedd5;color:#c2410c">CR</div><div><div class="tp-12__name">Career</div><div class="tp-12__count">3,102 articles</div></div></div>
            <div class="tp-12__desc">Advice on navigating tech careers — from first job to staff engineer, negotiation, interviews, and switching roles.</div>
          </div>
          <div class="tp-12__pop">
            <div class="tp-12__pop-label">Popularity this month</div>
            <div class="tp-12__track"><div class="tp-12__fill" style="width:82%;background:#f97316"></div></div>
            <div class="tp-12__trend"><span class="tp-12__trend-left"><strong>↑ trending</strong></span><span>+9% vs last month</span></div>
          </div>
          <div class="tp-12__rel">
            <div class="tp-12__rel-label">Related</div>
            <div class="tp-12__rel-pills"><span class="tp-12__rel-pill">Interviews</span><span class="tp-12__rel-pill">Salary</span><span class="tp-12__rel-pill">Remote work</span></div>
          </div>
          <div class="tp-12__ex">
            <div class="tp-12__ex-label">Top articles</div>
            <div class="tp-12__ex-item">The staff engineer path, explained</div>
            <div class="tp-12__ex-item">How to negotiate a competing offer</div>
            <div class="tp-12__ex-item">Writing your first performance review</div>
          </div>
        </div>
      </div>

      <div class="tp-12__t">
        <div class="tp-12__pill" style="background:#fff1f2;border-color:#fecdd3;color:#be123c"><span class="tp-12__dot" style="background:#f43f5e"></span>Security</div>
        <div class="tp-12__tip">
          <div class="tp-12__head">
            <div class="tp-12__head-row"><div class="tp-12__icon" style="background:#ffe4e6;color:#be123c">SE</div><div><div class="tp-12__name">Security</div><div class="tp-12__count">1,540 articles</div></div></div>
            <div class="tp-12__desc">Application security, cryptography, threat modelling, vulnerability research, and secure development practices for engineers.</div>
          </div>
          <div class="tp-12__pop">
            <div class="tp-12__pop-label">Popularity this month</div>
            <div class="tp-12__track"><div class="tp-12__fill" style="width:70%;background:#f43f5e"></div></div>
            <div class="tp-12__trend"><span class="tp-12__trend-left"><strong>↑ trending</strong></span><span>+18% vs last month</span></div>
          </div>
          <div class="tp-12__rel">
            <div class="tp-12__rel-label">Related</div>
            <div class="tp-12__rel-pills"><span class="tp-12__rel-pill">OWASP</span><span class="tp-12__rel-pill">Auth</span><span class="tp-12__rel-pill">CVE</span></div>
          </div>
          <div class="tp-12__ex">
            <div class="tp-12__ex-label">Top articles</div>
            <div class="tp-12__ex-item">SQL injection prevention in 2024</div>
            <div class="tp-12__ex-item">JWT vs sessions: which to use</div>
            <div class="tp-12__ex-item">Zero-trust architecture basics</div>
          </div>
        </div>
      </div>

      <div class="tp-12__t">
        <div class="tp-12__pill" style="background:#f0fdfa;border-color:#99f6e4;color:#0f766e"><span class="tp-12__dot" style="background:#14b8a6"></span>DevOps</div>
        <div class="tp-12__tip">
          <div class="tp-12__head">
            <div class="tp-12__head-row"><div class="tp-12__icon" style="background:#ccfbf1;color:#0f766e">DO</div><div><div class="tp-12__name">DevOps</div><div class="tp-12__count">1,188 articles</div></div></div>
            <div class="tp-12__desc">Practices and tools that unify software development and IT operations — CI/CD, containerisation, infrastructure as code, monitoring.</div>
          </div>
          <div class="tp-12__pop">
            <div class="tp-12__pop-label">Popularity this month</div>
            <div class="tp-12__track"><div class="tp-12__fill" style="width:66%;background:#14b8a6"></div></div>
            <div class="tp-12__trend"><span class="tp-12__trend-left"><strong>→ stable</strong></span><span>+2% vs last month</span></div>
          </div>
          <div class="tp-12__rel">
            <div class="tp-12__rel-label">Related</div>
            <div class="tp-12__rel-pills"><span class="tp-12__rel-pill">Docker</span><span class="tp-12__rel-pill">Kubernetes</span><span class="tp-12__rel-pill">Terraform</span></div>
          </div>
          <div class="tp-12__ex">
            <div class="tp-12__ex-label">Top articles</div>
            <div class="tp-12__ex-item">Building zero-downtime deploys</div>
            <div class="tp-12__ex-item">Helm charts for beginners</div>
            <div class="tp-12__ex-item">Observability vs. monitoring</div>
          </div>
        </div>
      </div>

      <div class="tp-12__t">
        <div class="tp-12__pill" style="background:#fefce8;border-color:#fef08a;color:#854d0e"><span class="tp-12__dot" style="background:#eab308"></span>Performance</div>
        <div class="tp-12__tip">
          <div class="tp-12__head">
            <div class="tp-12__head-row"><div class="tp-12__icon" style="background:#fef9c3;color:#854d0e">PF</div><div><div class="tp-12__name">Performance</div><div class="tp-12__count">922 articles</div></div></div>
            <div class="tp-12__desc">Techniques for optimising speed, throughput, and resource efficiency — from query tuning to Core Web Vitals.</div>
          </div>
          <div class="tp-12__pop">
            <div class="tp-12__pop-label">Popularity this month</div>
            <div class="tp-12__track"><div class="tp-12__fill" style="width:60%;background:#eab308"></div></div>
            <div class="tp-12__trend"><span class="tp-12__trend-left"><strong>→ stable</strong></span><span>+1% vs last month</span></div>
          </div>
          <div class="tp-12__rel">
            <div class="tp-12__rel-label">Related</div>
            <div class="tp-12__rel-pills"><span class="tp-12__rel-pill">Profiling</span><span class="tp-12__rel-pill">Caching</span><span class="tp-12__rel-pill">Web Vitals</span></div>
          </div>
          <div class="tp-12__ex">
            <div class="tp-12__ex-label">Top articles</div>
            <div class="tp-12__ex-item">N+1 queries and how to fix them</div>
            <div class="tp-12__ex-item">React re-renders: a visual guide</div>
            <div class="tp-12__ex-item">Redis caching patterns in production</div>
          </div>
        </div>
      </div>

      <div class="tp-12__t">
        <div class="tp-12__pill" style="background:#f8fafc;border-color:#e2e8f0;color:#475569"><span class="tp-12__dot" style="background:#94a3b8"></span>Architecture</div>
        <div class="tp-12__tip">
          <div class="tp-12__head">
            <div class="tp-12__head-row"><div class="tp-12__icon" style="background:#f1f5f9;color:#475569">AR</div><div><div class="tp-12__name">Architecture</div><div class="tp-12__count">748 articles</div></div></div>
            <div class="tp-12__desc">Software architecture patterns, trade-offs, and design decisions — microservices, monoliths, event-driven, hexagonal, and beyond.</div>
          </div>
          <div class="tp-12__pop">
            <div class="tp-12__pop-label">Popularity this month</div>
            <div class="tp-12__track"><div class="tp-12__fill" style="width:54%;background:#94a3b8"></div></div>
            <div class="tp-12__trend"><span class="tp-12__trend-left"><strong>↓ slight dip</strong></span><span>−3% vs last month</span></div>
          </div>
          <div class="tp-12__rel">
            <div class="tp-12__rel-label">Related</div>
            <div class="tp-12__rel-pills"><span class="tp-12__rel-pill">DDD</span><span class="tp-12__rel-pill">Microservices</span><span class="tp-12__rel-pill">Clean Code</span></div>
          </div>
          <div class="tp-12__ex">
            <div class="tp-12__ex-label">Top articles</div>
            <div class="tp-12__ex-item">Monolith first: the case for starting simple</div>
            <div class="tp-12__ex-item">CQRS and event sourcing, explained</div>
            <div class="tp-12__ex-item">When to break up a microservice</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-12 {
  width: 100%;
  min-height: 100vh;
  background: #fff;
  /* Top room — content-tag cards pop UP from each pill (~300px tall). */
  padding: 320px 28px 36px;
  font-family: 'Inter', system-ui, sans-serif;
}

.tp-12__inner {
  max-width: 560px;
  margin: 0 auto;
}

.tp-12__list {
  display: flex;
  flex-wrap: wrap;
  gap: 9px;
  justify-content: center;
}

.tp-12__t {
  position: relative;
}

.tp-12__pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12.5px;
  font-weight: 500;
  border: 1px solid transparent;
  cursor: help;
  transition: transform .15s, box-shadow .15s;
}

.tp-12__t:hover .tp-12__pill {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
}

.tp-12__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  flex-shrink: 0;
}

.tp-12__tip {
  position: absolute;
  bottom: calc(100% + 9px);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  width: 260px;
  background: #fff;
  border-radius: 11px;
  border: 1px solid rgba(0, 0, 0, 0.07);
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.11), 0 2px 8px rgba(0, 0, 0, 0.05);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .2s, transform .2s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .2s;
  z-index: 30;
  overflow: hidden;
  text-align: left;
}

.tp-12__t:hover .tp-12__tip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
  transition-delay: 0s;
}

.tp-12__head {
  padding: 13px 14px 11px;
  border-bottom: 1px solid #f4f4f4;
}

.tp-12__head-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}

.tp-12__icon {
  width: 30px;
  height: 30px;
  border-radius: 7px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.04em;
  flex-shrink: 0;
}

.tp-12__name {
  font-size: 14px;
  font-weight: 700;
  color: #111;
  line-height: 1.2;
}

.tp-12__count {
  font-size: 10px;
  color: #bbb;
  margin-top: 1px;
}

.tp-12__desc {
  font-size: 11.5px;
  color: #666;
  line-height: 1.55;
}

.tp-12__pop {
  padding: 10px 14px;
  border-bottom: 1px solid #f4f4f4;
}

.tp-12__pop-label {
  font-size: 7.5px;
  color: #ccc;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.tp-12__track {
  height: 5px;
  background: #f0f0f0;
  border-radius: 3px;
  overflow: hidden;
  margin-bottom: 5px;
}

.tp-12__fill {
  height: 100%;
  border-radius: 3px;
}

.tp-12__trend {
  font-size: 10px;
  color: #bbb;
  display: flex;
  justify-content: space-between;
}

.tp-12__trend-left strong {
  color: #555;
  font-weight: 600;
}

.tp-12__rel {
  padding: 10px 14px;
  border-bottom: 1px solid #f4f4f4;
}

.tp-12__rel-label {
  font-size: 7.5px;
  color: #ccc;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.tp-12__rel-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
}

.tp-12__rel-pill {
  font-size: 9.5px;
  padding: 2px 7px;
  border-radius: 10px;
  background: #f4f4f6;
  color: #888;
  border: 1px solid #eee;
}

.tp-12__ex {
  padding: 10px 14px 12px;
}

.tp-12__ex-label {
  font-size: 7.5px;
  color: #ccc;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.tp-12__ex-item {
  font-size: 10.5px;
  color: #777;
  margin-bottom: 4px;
  padding-left: 9px;
  position: relative;
  line-height: 1.4;
}

.tp-12__ex-item::before {
  content: '·';
  position: absolute;
  left: 2px;
  color: #ccc;
}
```
