# How to put this on GitHub

The whole project is already organized in this folder. You just need to create a repo and push it. Two ways — pick one.

---

## Option A — the easy way (GitHub website, no command line)

1. Go to **https://github.com/new** and create a new repository.
   - Name it something like `la-clef` or `madrigal-french`.
   - Add a description: *"A guided French study app built from a classic 1959 primer."*
   - **Leave it empty** — do NOT add a README, .gitignore, or license (this folder already has them).
   - Click **Create repository**.
2. On the next page, click **uploading an existing file**.
3. Drag this entire folder's contents into the upload area (or zip it, but GitHub wants the files, not the zip — unzip first if needed).
4. Write a commit message like `Initial commit — La Clef`.
5. Click **Commit changes**. Done.

---

## Option B — the command line (cleaner, keeps full history)

You'll need [git](https://git-scm.com) installed. From inside this folder:

```bash
# 1. start a repo here
git init
git add .
git commit -m "Initial commit — La Clef"

# 2. create an EMPTY repo on github.com first (no README/license),
#    then connect it. Replace YOUR-USERNAME and REPO-NAME:
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git

# 3. push
git push -u origin main
```

If it asks you to log in, GitHub now uses a **personal access token** instead of a password:
- Go to **github.com → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token**, give it `repo` scope, and use that token as the password when prompted.

---

## Pushing updates later

Every time you change something:

```bash
git add .
git commit -m "Describe what you changed"
git push
```

That's the whole loop: edit → `add` → `commit` → `push`.

---

## Showing off the live app

GitHub can host the app for free with **GitHub Pages**:

1. In your repo, go to **Settings → Pages**.
2. Under "Build and deployment," set Source to **Deploy from a branch**, branch **main**, folder **/ (root)**, and Save.
3. After a minute, your app will be live at:
   `https://YOUR-USERNAME.github.io/REPO-NAME/app/la-clef.html`

Share that link and anyone can try it in their browser.
