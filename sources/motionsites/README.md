# MotionSites AI — free prompt archive

Website-section prompts published as free on <https://motionsites.ai/sections>.

- Free prompts archived: **321**
- Catalogue entries seen: **772** (of which **451** are paid/locked and intentionally not archived)
- Format: one Markdown file per prompt, folder = category
- Upstream repository: none. MotionSites AI publishes no GitHub repo, so the free prompts are read from
  `motionsites.ai/sections`.
- Rights: prompts remain the property of MotionSites AI and their authors; not relicensed here.
  See [`NOTICE.md`](../../NOTICE.md).
- Manifest: [`manifest.json`](manifest.json) · full public catalogue: [`catalog.json`](catalog.json)

## Categories

- Hero — 28
- SaaS — 25
- Portfolio — 24
- Hero Section — 17
- 3D — 14
- Agency — 12
- Landing Page — 12
- Ecommerce — 11
- Travel — 10
- AI — 9
- Fashion — 9
- Footer — 8
- Interactive — 7
- Features — 6
- About — 5
- Creative — 4
- Fintech — 4
- Footer Section — 4
- Technology — 4
- 404 — 3
- CTA — 3
- AI Assistant — 2
- Architecture — 2
- Community — 2
- Cybersecurity — 2
- E-commerce — 2
- Editorial — 2
- Finance — 2
- Login Page — 2
- Logistics — 2
- Music — 2
- Wellness — 2
- 3D Character — 1
- 3D Website — 1
- AI Builder — 1
- AI Course — 1
- AI Data — 1
- AI Hero — 1
- AI Research — 1
- AI SaaS — 1
- Analytics — 1
- App — 1
- Art — 1
- Authentication — 1
- Automative — 1
- Benefits — 1
- Blog — 1
- Case Studies — 1
- Categories — 1
- Church — 1
- Component — 1
- Contact us — 1
- Creative Agency — 1
- Creator Platform — 1
- Crypto — 1
- Crypto Hero — 1
- Curated — 1
- Dashboard — 1
- Data Intelligence — 1
- Design — 1
- E-coommerce — 1
- Education Website — 1
- Email Marketing — 1
- Environmental — 1
- FAQ Page — 1
- Feature — 1
- Features Section — 1
- Fintech Landing — 1
- Halloween — 1
- Health — 1
- Healthcare — 1
- Healthcare AI — 1
- Hiking App — 1
- History — 1
- Interactive Map — 1
- Kids Show — 1
- Landing page — 1
- Legal Studio — 1
- Loyalty App — 1
- Manufacturing — 1
- Medicine — 1
- Mental Health — 1
- Motion — 1
- Navbar — 1
- Onboarding — 1
- Personal — 1
- Photography — 1
- Podcast — 1
- Portfolio Builder — 1
- Pricing — 1
- Product — 1
- Publishing — 1
- Robotics — 1
- Science — 1
- Sign Up — 1
- Sign in — 1
- Ski Gear — 1
- Space — 1
- Staffing — 1
- Statistics App — 1
- Stats — 1
- Supply — 1
- Tech — 1
- Testimonials — 1
- Trading App — 1
- Transportation — 1
- Travel Fintech — 1
- Use Case — 1
- Utility — 1
- Waitlist — 1
- Wearables — 1
- Website — 1

## Use

These prompts are best used as **section briefs**: they specify layout, fonts, spacing and interaction in
detail. Keep the structure and adapt the brand. The prompts often reference third-party asset URLs; replace
them with your own files.

```bash
jq -r '.[] | select(.category == "Hero") | [.title, .path] | @tsv' sources/motionsites/manifest.json
```

Paid prompts are deliberately absent. Do not try to reconstruct them from previews.
