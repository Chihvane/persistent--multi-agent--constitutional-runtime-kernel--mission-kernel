# GitHub Repository Setup

Target repository name:

`persistent--multi-agent--constitutional-runtime-kernel--mission-kernel`

Recommended visibility:

`public`

This repository is intended to be the public mission, article, and whitepaper repository. Keep the source implementation repository private.

## Local Setup

```bash
git init -b main
git add .
git commit -m "Initial public mission kernel docs"
```

## Remote Setup

Only run these commands after creating the GitHub repository under the intended account or organization.

```bash
git remote add origin git@github.com:Chihvane/persistent--multi-agent--constitutional-runtime-kernel--mission-kernel.git
git push -u origin main
```

## GitHub Pages

After the repository is pushed:

1. Open the repository settings.
2. Go to Pages.
3. Select GitHub Actions as the build and deployment source.
4. Run the `Deploy GitHub Pages` workflow if it does not run automatically.

