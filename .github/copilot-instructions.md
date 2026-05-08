# Copilot Instructions for Python-Magic-8ball

## “Back to one!” workflow (critical)

When the user says **“Back to one!”**, execute this reset flow in the current repo without entering a clarification loop:

1. `git fetch origin main --prune`
2. `git checkout main`
3. `git reset --hard origin/main`
4. `git clean -fd`
5. `git for-each-ref --format='%(refname:short)' refs/heads | awk '$1 != "main"' | xargs -r git branch -D`

Before running, briefly state you are executing the reset in this repo.  
After running, report branch and working-tree status.

## Branch and commit visibility rules

- Never commit directly to `main`.
- For code changes, explicitly state:
  - current branch before edits,
  - branch containing the final changes,
  - whether a PR is needed/already created.

## Local-only instructions handling

When the user wants instructions available locally but not pushed:

- Prefer `.git/info/exclude` for local-only ignores in this repo.
- Keep reset flows compatible with local ignored files (avoid `git clean -fdx` unless explicitly requested).
- If a file should remain local-only, confirm it is untracked/ignored after setup.
