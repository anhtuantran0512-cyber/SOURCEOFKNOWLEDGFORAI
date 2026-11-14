---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-data-table-cell-tooltip-segment-breakdown-bars/"
title: "Tailwind Data Table Cell Tooltip with Segment Breakdown Bars"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "A quarterly metrics table where every number is a hover target: the popover names the metric, restates the value large, shows the change versus prior quarter…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Data Table Cell Tooltip with Segment Breakdown Bars
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-data-table-cell-tooltip-segment-breakdown-bars/

A quarterly metrics table where every number is a hover target: the popover names the metric, restates the value large, shows the change versus prior quarter and breaks the total into three segments. Twelve cells of identical structure make this the clearest @apply case in the collection &mdash; the shell is one class, the numbers are markup.
## HTML
```html
<section class="ttp-11 w-full min-h-svh bg-ttp11-stage px-7 pt-[240px] pb-9 font-ttp11-sans">
  <div class="mx-auto max-w-[520px]">
    <table class="w-full border-collapse">
      <caption class="sr-only">Quarterly metrics. Each value opens a breakdown on hover or focus.</caption>
      <thead>
        <tr><th class="ttp11-th text-left"><span class="sr-only">Metric</span></th><th class="ttp11-th">Q1</th><th class="ttp11-th">Q2</th><th class="ttp11-th">Q3</th><th class="ttp11-th">Q4</th></tr>
      </thead>
      <tbody>
        <tr class="border-t border-ttp11-rule hover:bg-black/2">
          <th scope="row" class="ttp11-rowlabel">Revenue</th>
          <td class="ttp11-td"><span class="ttp11-t"><button type="button" aria-describedby="ttp11-a1" class="ttp11-val">$2.1M</button><span id="ttp11-a1" role="tooltip" class="ttp11-tip"><span class="ttp11-head"><span class="ttp11-metric">Revenue · Q1</span><span class="ttp11-bigrow"><span class="ttp11-big">$2.1M</span><span class="ttp11-up">↑ +18% vs Q4</span></span></span><span class="ttp11-bars"><span class="ttp11-barslabel">By segment</span><span class="ttp11-row"><span class="ttp11-name">SMB</span><span class="ttp11-track"><span class="ttp11-fill w-[62%] bg-[#6366f1]"></span></span><span class="ttp11-pct">62%</span></span><span class="ttp11-row"><span class="ttp11-name">Mid</span><span class="ttp11-track"><span class="ttp11-fill w-[28%] bg-[#8b5cf6]"></span></span><span class="ttp11-pct">28%</span></span><span class="ttp11-row"><span class="ttp11-name">Ent.</span><span class="ttp11-track"><span class="ttp11-fill w-[10%] bg-[#a78bfa]"></span></span><span class="ttp11-pct">10%</span></span></span><span class="ttp11-foot"><span>vs prior: <strong>+$320K</strong></span><span>ARR: <strong>$8.4M</strong></span></span></span></span></td>
          <td class="ttp11-td"><span class="ttp11-t"><button type="button" aria-describedby="ttp11-a2" class="ttp11-val">$2.8M</button><span id="ttp11-a2" role="tooltip" class="ttp11-tip"><span class="ttp11-head"><span class="ttp11-metric">Revenue · Q2</span><span class="ttp11-bigrow"><span class="ttp11-big">$2.8M</span><span class="ttp11-up">↑ +33% vs Q1</span></span></span><span class="ttp11-bars"><span class="ttp11-barslabel">By segment</span><span class="ttp11-row"><span class="ttp11-name">SMB</span><span class="ttp11-track"><span class="ttp11-fill w-[55%] bg-[#6366f1]"></span></span><span class="ttp11-pct">55%</span></span><span class="ttp11-row"><span class="ttp11-name">Mid</span><span class="ttp11-track"><span class="ttp11-fill w-[33%] bg-[#8b5cf6]"></span></span><span class="ttp11-pct">33%</span></span><span class="ttp11-row"><span class="ttp11-name">Ent.</span><span class="ttp11-track"><span class="ttp11-fill w-[12%] bg-[#a78bfa]"></span></span><span class="ttp11-pct">12%</span></span></span><span class="ttp11-foot"><span>vs Q1: <strong>+$700K</strong></span><span>ARR: <strong>$11.2M</strong></span></span></span></span></td>
          <td class="ttp11-td"><span class="ttp11-t"><button type="button" aria-describedby="ttp11-a3" class="ttp11-val">$3.4M</button><span id="ttp11-a3" role="tooltip" class="ttp11-tip"><span class="ttp11-head"><span class="ttp11-metric">Revenue · Q3</span><span class="ttp11-bigrow"><span class="ttp11-big">$3.4M</span><span class="ttp11-up">↑ +21% vs Q2</span></span></span><span class="ttp11-bars"><span class="ttp11-barslabel">By segment</span><span class="ttp11-row"><span class="ttp11-name">SMB</span><span class="ttp11-track"><span class="ttp11-fill w-[48%] bg-[#6366f1]"></span></span><span class="ttp11-pct">48%</span></span><span class="ttp11-row"><span class="ttp11-name">Mid</span><span class="ttp11-track"><span class="ttp11-fill w-[38%] bg-[#8b5cf6]"></span></span><span class="ttp11-pct">38%</span></span><span class="ttp11-row"><span class="ttp11-name">Ent.</span><span class="ttp11-track"><span class="ttp11-fill w-[14%] bg-[#a78bfa]"></span></span><span class="ttp11-pct">14%</span></span></span><span class="ttp11-foot"><span>vs Q2: <strong>+$600K</strong></span><span>ARR: <strong>$13.6M</strong></span></span></span></span></td>
          <td class="ttp11-td"><span class="ttp11-t"><button type="button" aria-describedby="ttp11-a4" class="ttp11-val">$4.2M</button><span id="ttp11-a4" role="tooltip" class="ttp11-tip"><span class="ttp11-head"><span class="ttp11-metric">Revenue · Q4</span><span class="ttp11-bigrow"><span class="ttp11-big">$4.2M</span><span class="ttp11-up">↑ +24% vs Q3</span></span></span><span class="ttp11-bars"><span class="ttp11-barslabel">By segment</span><span class="ttp11-row"><span class="ttp11-name">SMB</span><span class="ttp11-track"><span class="ttp11-fill w-[42%] bg-[#6366f1]"></span></span><span class="ttp11-pct">42%</span></span><span class="ttp11-row"><span class="ttp11-name">Mid</span><span class="ttp11-track"><span class="ttp11-fill w-[38%] bg-[#8b5cf6]"></span></span><span class="ttp11-pct">38%</span></span><span class="ttp11-row"><span class="ttp11-name">Ent.</span><span class="ttp11-track"><span class="ttp11-fill w-[20%] bg-[#a78bfa]"></span></span><span class="ttp11-pct">20%</span></span></span><span class="ttp11-foot"><span>vs Q3: <strong>+$800K</strong></span><span>Year: <strong>$12.5M</strong></span></span></span></span></td>
        </tr>
        <tr class="border-t border-ttp11-rule hover:bg-black/2">
          <th scope="row" class="ttp11-rowlabel">Active Users</th>
          <td class="ttp11-td"><span class="ttp11-t"><button type="button" aria-describedby="ttp11-b1" class="ttp11-val">12.4K</button><span id="ttp11-b1" role="tooltip" class="ttp11-tip"><span class="ttp11-head"><span class="ttp11-metric">Active Users · Q1</span><span class="ttp11-bigrow"><span class="ttp11-big">12.4K</span><span class="ttp11-up">↑ +22%</span></span></span><span class="ttp11-bars"><span class="ttp11-barslabel">By plan</span><span class="ttp11-row"><span class="ttp11-name">Free</span><span class="ttp11-track"><span class="ttp11-fill w-[58%] bg-[#22c55e]"></span></span><span class="ttp11-pct">58%</span></span><span class="ttp11-row"><span class="ttp11-name">Pro</span><span class="ttp11-track"><span class="ttp11-fill w-[32%] bg-[#16a34a]"></span></span><span class="ttp11-pct">32%</span></span><span class="ttp11-row"><span class="ttp11-name">Ent.</span><span class="ttp11-track"><span class="ttp11-fill w-[10%] bg-[#166534]"></span></span><span class="ttp11-pct">10%</span></span></span><span class="ttp11-foot"><span>New: <strong>+2,240</strong></span><span>DAU/MAU: <strong>41%</strong></span></span></span></span></td>
          <td class="ttp11-td"><span class="ttp11-t"><button type="button" aria-describedby="ttp11-b2" class="ttp11-val">18.9K</button><span id="ttp11-b2" role="tooltip" class="ttp11-tip"><span class="ttp11-head"><span class="ttp11-metric">Active Users · Q2</span><span class="ttp11-bigrow"><span class="ttp11-big">18.9K</span><span class="ttp11-up">↑ +52%</span></span></span><span class="ttp11-bars"><span class="ttp11-barslabel">By plan</span><span class="ttp11-row"><span class="ttp11-name">Free</span><span class="ttp11-track"><span class="ttp11-fill w-[54%] bg-[#22c55e]"></span></span><span class="ttp11-pct">54%</span></span><span class="ttp11-row"><span class="ttp11-name">Pro</span><span class="ttp11-track"><span class="ttp11-fill w-[36%] bg-[#16a34a]"></span></span><span class="ttp11-pct">36%</span></span><span class="ttp11-row"><span class="ttp11-name">Ent.</span><span class="ttp11-track"><span class="ttp11-fill w-[10%] bg-[#166534]"></span></span><span class="ttp11-pct">10%</span></span></span><span class="ttp11-foot"><span>New: <strong>+6,500</strong></span><span>DAU/MAU: <strong>44%</strong></span></span></span></span></td>
          <td class="ttp11-td"><span class="ttp11-t"><button type="button" aria-describedby="ttp11-b3" class="ttp11-val">24.1K</button><span id="ttp11-b3" role="tooltip" class="ttp11-tip"><span class="ttp11-head"><span class="ttp11-metric">Active Users · Q3</span><span class="ttp11-bigrow"><span class="ttp11-big">24.1K</span><span class="ttp11-up">↑ +28%</span></span></span><span class="ttp11-bars"><span class="ttp11-barslabel">By plan</span><span class="ttp11-row"><span class="ttp11-name">Free</span><span class="ttp11-track"><span class="ttp11-fill w-[50%] bg-[#22c55e]"></span></span><span class="ttp11-pct">50%</span></span><span class="ttp11-row"><span class="ttp11-name">Pro</span><span class="ttp11-track"><span class="ttp11-fill w-[38%] bg-[#16a34a]"></span></span><span class="ttp11-pct">38%</span></span><span class="ttp11-row"><span class="ttp11-name">Ent.</span><span class="ttp11-track"><span class="ttp11-fill w-[12%] bg-[#166534]"></span></span><span class="ttp11-pct">12%</span></span></span><span class="ttp11-foot"><span>New: <strong>+5,200</strong></span><span>DAU/MAU: <strong>47%</strong></span></span></span></span></td>
          <td class="ttp11-td"><span class="ttp11-t"><button type="button" aria-describedby="ttp11-b4" class="ttp11-val">31.8K</button><span id="ttp11-b4" role="tooltip" class="ttp11-tip"><span class="ttp11-head"><span class="ttp11-metric">Active Users · Q4</span><span class="ttp11-bigrow"><span class="ttp11-big">31.8K</span><span class="ttp11-up">↑ +32%</span></span></span><span class="ttp11-bars"><span class="ttp11-barslabel">By plan</span><span class="ttp11-row"><span class="ttp11-name">Free</span><span class="ttp11-track"><span class="ttp11-fill w-[44%] bg-[#22c55e]"></span></span><span class="ttp11-pct">44%</span></span><span class="ttp11-row"><span class="ttp11-name">Pro</span><span class="ttp11-track"><span class="ttp11-fill w-[40%] bg-[#16a34a]"></span></span><span class="ttp11-pct">40%</span></span><span class="ttp11-row"><span class="ttp11-name">Ent.</span><span class="ttp11-track"><span class="ttp11-fill w-[16%] bg-[#166534]"></span></span><span class="ttp11-pct">16%</span></span></span><span class="ttp11-foot"><span>New: <strong>+7,700</strong></span><span>YoY: <strong>+156%</strong></span></span></span></span></td>
        </tr>
        <tr class="border-t border-ttp11-rule hover:bg-black/2">
          <th scope="row" class="ttp11-rowlabel">Churn</th>
          <td class="ttp11-td"><span class="ttp11-t"><button type="button" aria-describedby="ttp11-c1" class="ttp11-val">2.8%</button><span id="ttp11-c1" role="tooltip" class="ttp11-tip"><span class="ttp11-head"><span class="ttp11-metric">Monthly Churn · Q1</span><span class="ttp11-bigrow"><span class="ttp11-big">2.8%</span><span class="ttp11-dn">↑ +0.4pp worse</span></span></span><span class="ttp11-bars"><span class="ttp11-barslabel">Reason</span><span class="ttp11-row"><span class="ttp11-name">Price</span><span class="ttp11-track"><span class="ttp11-fill w-[42%] bg-[#dc2626]"></span></span><span class="ttp11-pct">42%</span></span><span class="ttp11-row"><span class="ttp11-name">Feat.</span><span class="ttp11-track"><span class="ttp11-fill w-[31%] bg-[#ef4444]"></span></span><span class="ttp11-pct">31%</span></span><span class="ttp11-row"><span class="ttp11-name">Other</span><span class="ttp11-track"><span class="ttp11-fill w-[27%] bg-[#f87171]"></span></span><span class="ttp11-pct">27%</span></span></span><span class="ttp11-foot"><span>Net rev churn: <strong>1.1%</strong></span><span>Win-back: <strong>14%</strong></span></span></span></span></td>
          <td class="ttp11-td"><span class="ttp11-t"><button type="button" aria-describedby="ttp11-c2" class="ttp11-val">2.4%</button><span id="ttp11-c2" role="tooltip" class="ttp11-tip"><span class="ttp11-head"><span class="ttp11-metric">Monthly Churn · Q2</span><span class="ttp11-bigrow"><span class="ttp11-big">2.4%</span><span class="ttp11-up">↓ −0.4pp better</span></span></span><span class="ttp11-bars"><span class="ttp11-barslabel">Reason</span><span class="ttp11-row"><span class="ttp11-name">Price</span><span class="ttp11-track"><span class="ttp11-fill w-[38%] bg-[#dc2626]"></span></span><span class="ttp11-pct">38%</span></span><span class="ttp11-row"><span class="ttp11-name">Feat.</span><span class="ttp11-track"><span class="ttp11-fill w-[34%] bg-[#ef4444]"></span></span><span class="ttp11-pct">34%</span></span><span class="ttp11-row"><span class="ttp11-name">Other</span><span class="ttp11-track"><span class="ttp11-fill w-[28%] bg-[#f87171]"></span></span><span class="ttp11-pct">28%</span></span></span><span class="ttp11-foot"><span>Net rev churn: <strong>0.8%</strong></span><span>Win-back: <strong>18%</strong></span></span></span></span></td>
          <td class="ttp11-td"><span class="ttp11-t"><button type="button" aria-describedby="ttp11-c3" class="ttp11-val">2.1%</button><span id="ttp11-c3" role="tooltip" class="ttp11-tip"><span class="ttp11-head"><span class="ttp11-metric">Monthly Churn · Q3</span><span class="ttp11-bigrow"><span class="ttp11-big">2.1%</span><span class="ttp11-up">↓ −0.3pp better</span></span></span><span class="ttp11-bars"><span class="ttp11-barslabel">Reason</span><span class="ttp11-row"><span class="ttp11-name">Price</span><span class="ttp11-track"><span class="ttp11-fill w-[32%] bg-[#dc2626]"></span></span><span class="ttp11-pct">32%</span></span><span class="ttp11-row"><span class="ttp11-name">Feat.</span><span class="ttp11-track"><span class="ttp11-fill w-[38%] bg-[#ef4444]"></span></span><span class="ttp11-pct">38%</span></span><span class="ttp11-row"><span class="ttp11-name">Other</span><span class="ttp11-track"><span class="ttp11-fill w-[30%] bg-[#f87171]"></span></span><span class="ttp11-pct">30%</span></span></span><span class="ttp11-foot"><span>Net rev churn: <strong>0.6%</strong></span><span>Win-back: <strong>21%</strong></span></span></span></span></td>
          <td class="ttp11-td"><span class="ttp11-t"><button type="button" aria-describedby="ttp11-c4" class="ttp11-val">1.8%</button><span id="ttp11-c4" role="tooltip" class="ttp11-tip"><span class="ttp11-head"><span class="ttp11-metric">Monthly Churn · Q4</span><span class="ttp11-bigrow"><span class="ttp11-big">1.8%</span><span class="ttp11-up">↓ −0.3pp better</span></span></span><span class="ttp11-bars"><span class="ttp11-barslabel">Reason</span><span class="ttp11-row"><span class="ttp11-name">Price</span><span class="ttp11-track"><span class="ttp11-fill w-[28%] bg-[#dc2626]"></span></span><span class="ttp11-pct">28%</span></span><span class="ttp11-row"><span class="ttp11-name">Feat.</span><span class="ttp11-track"><span class="ttp11-fill w-[40%] bg-[#ef4444]"></span></span><span class="ttp11-pct">40%</span></span><span class="ttp11-row"><span class="ttp11-name">Other</span><span class="ttp11-track"><span class="ttp11-fill w-[32%] bg-[#f87171]"></span></span><span class="ttp11-pct">32%</span></span></span><span class="ttp11-foot"><span>Net rev churn: <strong>0.4%</strong></span><span>Year: <strong>−1.0pp</strong></span></span></span></span></td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp11-stage: #f8f9fa;
  --color-ttp11-stage: oklch(0.98 0.002 260);
  --color-ttp11-ink: #1a1a1a;
  --color-ttp11-ink: oklch(0.21 0 0);
  --color-ttp11-body: #333333;
  --color-ttp11-body: oklch(0.32 0 0);
  --color-ttp11-muted: #6b6b6b;
  --color-ttp11-muted: oklch(0.52 0 0);
  --color-ttp11-rule: #eeeeee;
  --color-ttp11-rule: oklch(0.94 0 0);
  --color-ttp11-dash: #8a8a8a;
  --color-ttp11-dash: oklch(0.62 0 0);
  --color-ttp11-up: #15803d;
  --color-ttp11-up: oklch(0.52 0.15 150);
  --color-ttp11-dn: #b91c1c;
  --color-ttp11-dn: oklch(0.5 0.19 27);
  --font-ttp11-sans: 'Inter', system-ui, sans-serif;
}

.ttp-11 {
  width: 100%;
  min-height: 100svh;
}
/* Twelve cells, one card. This is the clearest @apply case in the
   collection: every utility below is identical twelve times over,
   while the numbers and bar widths stay inline in the markup. */

.ttp-11 .ttp11-th {
  @apply px-3.5 pb-2.75 text-right text-[10px] font-medium uppercase tracking-[0.1em] text-ttp11-muted;
}

.ttp-11 .ttp11-td {
  @apply px-3.5 py-3 text-right text-[12.5px] whitespace-nowrap text-ttp11-body;
}

.ttp-11 .ttp11-rowlabel {
  @apply px-3.5 py-3 text-left text-[11px] font-normal uppercase tracking-[0.08em] text-ttp11-muted;
}

.ttp-11 .ttp11-t {
  @apply relative inline-block cursor-help;
}

.ttp-11 .ttp11-val {
  @apply cursor-help border-0 border-b border-dashed border-ttp11-rule bg-transparent p-0 font-ttp11-sans text-[12.5px] text-ttp11-body transition-colors duration-150 group-hover:text-ttp11-ink hover:border-b-ttp11-dash hover:text-ttp11-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp11-ink;
}

.ttp-11 .ttp11-tip {
  @apply pointer-events-none invisible absolute bottom-[calc(100%+9px)] left-1/2 z-30 block w-60 max-w-[calc(100vw-48px)] -translate-x-1/2 translate-y-1 overflow-hidden whitespace-normal rounded-[9px] border border-black/8 bg-white text-left opacity-0 shadow-[0_12px_36px_rgba(0,0,0,0.11),0_2px_8px_rgba(0,0,0,0.05)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)];
}

.ttp-11 .ttp11-val:hover + .ttp11-tip,
.ttp-11 .ttp11-val:focus-visible + .ttp11-tip {
  @apply visible translate-y-0 opacity-100;
}

.ttp-11 .ttp11-head {
  @apply block border-b border-ttp11-rule px-3.25 pt-3 pb-2.25;
}

.ttp-11 .ttp11-metric {
  @apply mb-1.25 block text-[10px] uppercase tracking-[0.09em] text-ttp11-muted;
}

.ttp-11 .ttp11-bigrow {
  @apply flex items-baseline gap-2;
}

.ttp-11 .ttp11-big {
  @apply text-[22px] font-bold text-ttp11-ink;
}

.ttp-11 .ttp11-up {
  @apply text-[11px] font-semibold text-ttp11-up;
}

.ttp-11 .ttp11-dn {
  @apply text-[11px] font-semibold text-ttp11-dn;
}

.ttp-11 .ttp11-bars {
  @apply block border-b border-ttp11-rule px-3.25 pt-2.75 pb-1.75;
}

.ttp-11 .ttp11-barslabel {
  @apply mb-1.75 block text-[8.5px] uppercase tracking-[0.1em] text-ttp11-muted;
}

.ttp-11 .ttp11-row {
  @apply mb-1.25 flex items-center gap-2;
}

.ttp-11 .ttp11-name {
  @apply w-8 shrink-0 text-right text-[10px] text-ttp11-muted;
}

.ttp-11 .ttp11-track {
  @apply block h-1.25 flex-1 overflow-hidden rounded-[3px] bg-ttp11-rule;
}

.ttp-11 .ttp11-fill {
  @apply block h-full rounded-[3px];
}

.ttp-11 .ttp11-pct {
  @apply w-7 shrink-0 text-right text-[10px] text-ttp11-muted;
}

.ttp-11 .ttp11-foot {
  @apply flex justify-between px-3.25 py-2.5 text-[10.5px] text-ttp11-muted;
}

.ttp-11 .ttp11-foot strong {
  @apply font-semibold text-ttp11-body;
}
```
