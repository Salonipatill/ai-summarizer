# Step 1: Create Fresh new Folder:- The Infimit

# Step 2: Go inside this folder in the vs code

# Step 3: Click on the Terminal 

# Step 4 : git clone https://github.com/Srishti-Doshi/infimit.git

<<<<<<< HEAD
# step 4.1 : go inside infimit

PS C:\The Infimit> cd infimit

# step 5 : create a new branch   git checkout feat/subphase2-ai-service
=======
# Step 5 : Create a new branch: git checkout -b feat/subphase2-ai-service
>>>>>>> 47a972808d11de6f3b020ff2c9b4e9e93c38358d

# Step 6 : Switch on this branch

<<<<<<< HEAD


# step 7 : run this command 

git branch  

=======
# Step 7 : git branch  
recheck
>>>>>>> 47a972808d11de6f3b020ff2c9b4e9e93c38358d

# Step 8: now inside the infimit folder copy  ai-service folder [take this folder from old branch]

<<<<<<< HEAD
# step 8.1 : go inside ai-service

PS C:\The Infimit\infimit> cd ai-service
PS C:\The Infimit\infimit\ai-service> 

# step 8.2:
run
git branch

# step 9 : look  inside infimit -> .gitignore file 
=======
# Step 9 : go inside The Infimit->.gitignore file 
>>>>>>> 47a972808d11de6f3b020ff2c9b4e9e93c38358d

# Step 10 : 
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

# Step 11

run here
PS C:\The Infimit\infimit\ai-service> 
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

run here
PS C:\The Infimit\infimit\ai-service> 
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

run here
PS C:\The Infimit\infimit\ai-service> 
# cat .gitignore

✅ Expected to contain at least
venv/
.venv/
__pycache__/
*.pyc
.env

run here
PS C:\The Infimit\infimit\ai-service> 
# pytest -q

passed


run here
PS C:\The Infimit\infimit\ai-service> 

# git rev-list --count origin/feat/subphase2-ai-service..HEAD

Before commit

0

run here
PS C:\The Infimit\infimit\ai-service> 
# git commit -m "feat(ai-service): complete /v1/summarize implementation with schemas, stub, metrics, errors, and tests"

Expected
[ai-service/Subphase2 abc1234]
feat(ai-service): complete /v1/summarize implementation with schemas, stub, metrics, errors, and tests

10 files changed ...

## Check commits again

run here
PS C:\The Infimit\infimit\ai-service> 
# git rev-list --count origin/feat/subphase2-ai-service..HEAD

If you created exactly one new commit:

1


run here
PS C:\The Infimit\infimit\ai-service> 
# git push -u origin feat/subphase2-ai-service 

✅ Expected
Enumerating objects...
Counting objects...
Writing objects...
To github.com:...
 * [new branch]      ai-service/Subphase2 -> ai-service/Subphase2