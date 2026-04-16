# Deploying the Privacy Wiki to GitHub Pages

Follow these steps once to get the wiki live. After that, every `git push` to `main` automatically rebuilds and republishes it.

---

## Step 1 — Create a GitHub repository

1. Go to https://github.com/new
2. Name it whatever you like (e.g. `privacy-wiki`)
3. Set it to **Public** (required for free GitHub Pages) or **Private** (requires GitHub Pro)
4. Do **not** initialise with a README — you'll push your existing files
5. Click **Create repository**

---

## Step 2 — Push your files

Open a terminal, `cd` into your `PrivacyKB` folder, then run:

```bash
git init
git add mkdocs.yml requirements.txt .gitignore hooks/ wiki/ .github/
git commit -m "Initial wiki commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO` with your GitHub username and repo name.

> **Note:** The `raw/` directory (source articles and PDFs) is not committed by default.
> Add `git add raw/` before committing if you want source files in the repo too.

---

## Step 3 — Enable GitHub Pages

1. Go to your repo on GitHub → **Settings** → **Pages** (left sidebar)
2. Under **Source**, select **GitHub Actions**
3. Click **Save**

That's it. GitHub will automatically run the workflow on your next push.

---

## Step 4 — Trigger the first deployment

The workflow runs on every push to `main`. Since you just pushed in Step 2, check its status:

1. Go to your repo → **Actions** tab
2. You should see a "Deploy Privacy Wiki to GitHub Pages" workflow running
3. Wait ~60 seconds for it to complete
4. Click the workflow run → **deploy** job → the URL shown at the bottom is your live wiki

Your wiki will be at:
```
https://YOUR_USERNAME.github.io/YOUR_REPO/
```

---

## Updating the wiki

Whenever you add or edit files in `wiki/`, just commit and push:

```bash
git add wiki/
git commit -m "Add new article on X"
git push
```

GitHub Actions rebuilds and redeploys automatically within about a minute.

---

## Password Protection (StatiCrypt)

The wiki is protected with [StatiCrypt](https://github.com/robinmoisson/staticrypt). Every HTML page is encrypted at build time — visitors see a password prompt before any content loads.

### One-time setup: add the password as a GitHub secret

1. Go to your repo on GitHub → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `STATICRYPT_PASSWORD`
4. Value: your chosen password (use something strong — share it only with intended readers)
5. Click **Add secret**

That's it. On the next `git push`, the Actions workflow will automatically encrypt all pages with this password before deploying.

### Changing the password

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click the pencil icon next to `STATICRYPT_PASSWORD`
3. Enter the new password and save
4. Trigger a new deployment (push any change, or use the **Actions** tab → **Run workflow**)
5. All pages are re-encrypted with the new password immediately

### What StatiCrypt does (and doesn't) protect

- **Protected**: All wiki content is AES-256 encrypted. Without the password, the HTML source reveals nothing.
- **Not protected**: The site URL itself is still public. Anyone who guesses the URL can see the password prompt — but not the content.
- **Not a substitute for**: Access control by individual user. Everyone with the password can access everything. For per-user access control, use Cloudflare Access instead.

---

## Local preview (optional)

To preview changes before pushing:

```bash
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000 in your browser. Changes to `wiki/` files reload live.
