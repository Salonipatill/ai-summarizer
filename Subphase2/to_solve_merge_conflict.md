# Step 1: Create Fresh new Folder :-The Infimit

# Step 2: go  inside this folder in the vs code

# step 3: click on the terminal 

# step 4 : git clone https://github.com/Srishti-Doshi/infimit.git

# step 5 : create a new branch   git checkout feat/subphase2-ai-service

# step 6 : switch on this branch

# step 7 : git branch  
recheck

# step 8: now inside the infimit folder copy  ai-service folder [take this folder from old branch]

# step 9 : go inside infimit->.gitignore file 

# step 10 : 
paste this 
```text
# Local env files
/.env
/.env.*

_pycache_/
*.pyc
*.pyo
*.pyd
.Python
*.env
venv/
.venv/
```

# step 11

# git status

✅ Expected

Before committing:

On branch ai-service/Subphase2

Changes to be committed:
  modified: ai-service/...
  new file: ai-service/..

❌ Should NOT show
backend/
frontend/
venv/
.venv/
__pycache__/
.github/

# git diff --staged

✅ Expected

Only ai-service files:

+ summarize endpoint
+ schemas
+ metrics
+ tests

❌ Should NOT contain
backend/
frontend/
venv/
site-packages/


# cat .gitignore

✅ Expected to contain at least
venv/
.venv/
__pycache__/
*.pyc
.env


# pytest -q

passed


# git rev-list --count origin/feat/subphase2-ai-service..HEAD

Before commit

0

# git commit -m "feat(ai-service): complete /v1/summarize implementation with schemas, stub, metrics, errors, and tests"

Expected
[ai-service/Subphase2 abc1234]
feat(ai-service): complete /v1/summarize implementation with schemas, stub, metrics, errors, and tests

10 files changed ...

## Check commits again

# git rev-list --count origin/feat/subphase2-ai-service..HEAD

If you created exactly one new commit:

1

# git push -u origin feat/subphase2-ai-service 


✅ Expected
Enumerating objects...
Counting objects...
Writing objects...
To github.com:...
 * [new branch]      ai-service/Subphase2 -> ai-service/Subphase2

                                                                                                                        