git status --short
git status --short ai-service
git status --untracked-files=all
git ls-files --others --exclude-standard
git diff --name-only
git add -p
git add ai-service/
git add ../.gitignore
git diff --cached --name-only
git diff --cached --name-only | findstr /R "^frontend/ ^backend/"
git commit -m "feat(ai-service): add ai-service source code and tests"
git commit -m "feat(ai-service): complete /v1/summarize implementation with schemas, stub, metrics, errors, and tests"
git show --name-only --oneline HEAD
git log --oneline origin/Ai-Service/subphase2..HEAD
git rev-list --count origin/Ai-Service/subphase2..HEAD
git push origin Ai-Service/subphase2
pytest
cat .gitignore