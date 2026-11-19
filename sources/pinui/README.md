# Pin UI — components and blocs with source

Free, open-source React components rebuilt from Pinterest designs. Light + dark, animated with Motion,
installable with the shadcn CLI. This folder is the archive copy.

- Site: <https://www.pinui.xyz/>
- Upstream app: <https://github.com/shadcn-labs/Pin-UI>
- License: **MIT (c) Rachit Thakur / Shadcn Labs** — keep the header comment in every adapted file.

## What is here

| Path | Count | Contents |
|---|---:|---|
| `registry/<name>/` | 30 | `*.tsx` + `*.css` (+ engine `.ts`), `ITEM.md`, `meta.json` |
| `blocx/<name>/` | 11 | Whole page sections: hero, pricing, footer, sign-in, contact form |
| `pages/` | 50 | One brief per public page |
| `registry/registry.json` | — | The site's own shadcn registry, source included |
| `catalog.json` | — | Totals + every public page with URL and preview image |

Everything is public: the site publishes the registry for
`npx shadcn@latest add "https://pinui.xyz/r/<name>.json"`. No `/api/` call was made (robots.txt
disallows it) and nothing was paywalled.

## Use

```bash
# install exactly as the site intends
npx shadcn@latest add "https://pinui.xyz/r/theme-switch.json"
npx shadcn@latest add "https://pinui.xyz/r/blocx/smart-pricing.json"

# or read the local source first
cat sources/pinui/registry/theme-switch/ITEM.md
```

## Find something

```bash
jq -r --arg q "<keyword>" '.[] | select(.kind=="component") |
  select((.title+" "+(.description//"")) | test($q;"i")) | [.title, .path, .install] | @tsv' \
  sources/pinui/manifest.json
```

## Adapt rules

1. Keep the MIT header comment in the new file.
2. CSS is prefixed per component — keep the prefix, do not edit global styles.
3. Preserve motion timing and easing; do not "improve" by feel.
4. Add a `prefers-reduced-motion: reduce` path if the reference has none.
5. Replace demo copy, names and brand colours with the project's real data and tokens.
