# Step-by step run the commands:-

```text
PS C:\The Infimit> cd infimit
```
```text
PS C:\The Infimit\infimit> echo ai-service/.env >> .gitignore
```
```text
PS C:\The Infimit\infimit> type .gitignore
```
echo .env >> .gitignore
# After running this command you will see

```text
/node_modules
/package-lock.json
/package.json
/yarn.lock
/pnpm-lock.yaml

# Build outputs accidentally produced at root
/dist
/build
/coverage

# OS / editor noise
.DS_Store
Thumbs.db
*.log
.idea
.vscode/*
!.vscode/settings.json
!.vscode/extensions.json

# Local env files
.env
.env.*
**/.env
**/.env.*ai-service/.env
```
Run:

```text
PS C:\The Infimit\infimit> git rm --cached ai-service/.env
git rm --cached.env
>> git add .gitignore
>> git commit -m "ignore .env file"
fatal: pathspec 'ai-service/.env' did not match any files
[feature/article-summarizer 802949d] ignore .env file
 1 file changed, 0 insertions(+), 0 deletions(-)
```
Run
```text
PS C:\The Infimit\infimit> git push
```
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>

Run

```text
PS C:\The Infimit\infimit> git remote -v     
```
```text                
PS C:\The Infimit\infimit> git remote add origin https://github.com/Srishti-Doshi/infimit.git
```
```text
PS C:\The Infimit\infimit> git remote -v
```
origin  https://github.com/Srishti-Doshi/infimit.git (fetch)
origin  https://github.com/Srishti-Doshi/infimit.git (push)

```text
PS C:\The Infimit\infimit> git push -u origin feature/article-summarizer
```
git push -u origin Subphase1

git push -u origin ai-service/Subphase1


Enumerating objects: 76, done.
Counting objects: 100% (76/76), done.
Delta compression using up to 4 threads
Compressing objects: 100% (39/39), done.
Writing objects: 100% (56/56), 14.82 KiB | 892.00 KiB/s, done.
Total 56 (delta 22), reused 46 (delta 14), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (22/22), completed with 13 local objects.
To https://github.com/Srishti-Doshi/infimit.git
   82cdc81..802949d  feature/article-summarizer -> feature/article-summarizer
branch 'feature/article-summarizer' set up to track 'origin/feature/article-summarizer'.
 