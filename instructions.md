When I say **“Back to one!”**, run these commands in the current workshop repo to reset to clean state:
1. `git fetch origin main --prune`
2. `git checkout main`
3. `git reset --hard origin/main`
4. `git clean -fd`
5. Delete all local branches except main:
   `git for-each-ref --format='%(refname:short)' refs/heads | awk '$1 != "main"' | xargs -r git branch -D`
