## Important Note

Run the following command from the **repository root folder**, not from the child folder.

---

## Repository Structure

```text
project-root/
├── .gitignore
├── childfoldername/
│   ├── .env
│   └── ...
├── backend/
├── frontend/
└── docs/

### Command

```text
echo "childfoldername/.env" >> .gitignore
```

This command appends childfoldername/.env  to the root .gitignore file.

As a result, Git ignores the .env file located inside the specified child folder, preventing sensitive information such as API keys, database credentials, access tokens, and secret configuration values from being committed to the repositor



```text
Why Run It From the Root Folder?
```
The path childfoldername/.env is relative to the repository root.

If the command is executed inside the child folder, it will modify the child folder's .gitignore instead of the root .gitignore, which can lead to multiple ignore files and inconsistent repository configuration.



Verification

```text
git check-ignore -v childfoldername/.env
```

It displays the contents of the .gitignore file in the terminal.:-

```text
cat .gitignore
```

