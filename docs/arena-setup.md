# Using this repository with Arena

Arena's own support answer is the source of truth here: you do **not** need a skill file or a special
`agent.md` for Arena to use a GitHub repo. Connect GitHub, grant access to the repo, and the agent can
clone, edit and open a pull request. A normal `README.md` plus a clearly named instruction file is enough.
This repo keeps those instructions in `AGENT.md`.

## 1. Connect the repository

1. In Arena, open **Settings → Integrations → GitHub** and connect your account.
2. Choose **Manage repositories** and enable
   `broamstuck-cybr/SOURCEOFKNOWLEDGFORAI`.
3. Toggle **GitHub** on for the workspace.
4. Start a new Agent Mode thread and reference the repo explicitly.

## 2. First message to send

```
Work in the repo broamstuck-cybr/SOURCEOFKNOWLEDGFORAI.
Read AGENT.md, then docs/usage-recipes.md.

Task: build <what you want> in <target folder>.
Use at most two references from sources/, prefer sources/lucianlabs first.
Keep license headers, use design tokens, and verify at 390/768/1440 px with
prefers-reduced-motion. Open a PR with a short summary of what you checked.
```

## 3. Why this works without skills

Arena reads the repository tree like a normal checkout. What it needs is:

- a top-level `README.md` that explains the repo in one screen;
- a named instruction file (`AGENT.md`) with rules and a workflow;
- small, self-contained files that can be opened without loading megabytes of context;
- an index (`manifest.json`) so the agent can filter before reading.

All four exist here.

## 4. Guardrails worth repeating in every thread

- "Only use files under `sources/` that are marked free; never reconstruct locked prompts."
- "Do not modify the archive while building the app. Put app code in the folder I name."
- "Open one PR per task. Do not mix archive refresh with feature work."
- "If a reference is missing, stop and tell me instead of inventing one."

## 5. Suggested repository settings

- Protect the default branch; require a PR for changes.
- Add a `CODEOWNERS` entry for `sources/` if several people will work in parallel.
- Keep the archive text-only; do not commit large media. Link to originals instead.

## 6. Troubleshooting

| Symptom | Fix |
|---|---|
| Agent cannot see the repo | Re-check **Manage repositories** access and the GitHub toggle. |
| Agent ignores `AGENT.md` | Reference it explicitly in the first message, and paste the three guardrails above. |
| Agent dumps entire folders into context | Tell it to query `manifest.json` with `jq` and open at most three files. |
| PR mixes archive and app changes | Ask for a clean branch from `main` and a PR limited to the target folder. |
