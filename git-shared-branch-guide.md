# First
# Fetch Latest Updates from GitHub

```text
git fetch
```

# Switch to Shared Branch

```text 
git checkout ai-service/Subphase1
```

# Check current branch

```text
git branch
```

# Pull Latest Code
Always do this before starting work:

```text
git pull origin ai-service/Subphase1
```

# To Download GROQ
py -m pip install groq 

# To Download DOTENV
py -m pip install dotenv

# To Delete the Branch Name
git branch -D "Branch_Name"

# To Add requirements.txt File in the Project
pip install -r requirements.txt

# To Install Package Pydantic-Settings
pip install pydantic-settings

# To Verify It
py -m pip show pydantic-settings

# To check weather API Key is set in .env or not
type .env

## For Subphase 2

# Step 1: git checkout feat/subphase1-ai-service

# step 2: git pull

# step 3: create copy of the ai-service folder 

# step 4: git checkout ai-service/Subphase2

# step 5: review that is there ai-service folder or not if not so paste here ai-service folder(that we copyed)


# Create a new branch and switch to it

git checkout -b branch-name

# Verify Branch

git branch

# After creating it, push it to the remote repository

git push -u origin branch-name

# To clone the project from github Firstly create Virtual Environment

# Create a virtual environment named venv
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Deactivate the environment
deactivate