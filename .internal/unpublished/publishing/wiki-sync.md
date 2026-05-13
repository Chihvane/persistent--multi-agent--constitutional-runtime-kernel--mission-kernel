# GitHub Wiki Sync

GitHub Wiki content lives in a separate repository:

`https://github.com/Chihvane/persistent--multi-agent--constitutional-runtime-kernel--mission-kernel.wiki.git`

The canonical source files are stored in this repository under `.internal/unpublished/wiki/` so wiki
changes can be reviewed with the rest of the public launch material.

## First-Time Setup

1. Enable Wiki in the public repository settings.
2. Create the first wiki page in the GitHub UI if GitHub has not initialized the
   wiki repository yet.
3. Clone the wiki repository next to this repository.

```bash
git clone https://github.com/Chihvane/persistent--multi-agent--constitutional-runtime-kernel--mission-kernel.wiki.git ../constitutional-runtime-wiki
```

## Publish Wiki Source

From this repository root:

```bash
cp .internal/unpublished/wiki/*.md ../constitutional-runtime-wiki/
cd ../constitutional-runtime-wiki
git status --short
git add .
git commit -m "Update public wiki"
git push
```

## Review Rule

Run this repository's public gate before publishing wiki updates:

```bash
make -f .internal/engineering/Makefile check
```

Do not publish private implementation details, credentials, private prompts,
internal logs, or raw third-party source snapshots through the wiki.
