<div align="center">
<img src="docs/img/horcrux-logo.png" width="150" alt="Horcrux Core logo">

<br/>
<br/>
<br/>

# Horcrux Hardware

[![Horcrux-core](https://img.shields.io/badge/Horcrux_core-v1.2.3-orange)](https://github.com/ficaud/horcrux-core)
[![Docs](https://img.shields.io/badge/Docs-GitHub_Pages-blue)](https://ficaud.github.io/horcrux-hw/)

</div>

**Horcrux Hardware** is a step-by-step guide that teaches **complete beginners** how to build a Horcrux device entirely from scratch — a physical device that safely stores your most sensitive secrets using [horcrux-core](https://github.com/ficaud/horcrux-core).

## Documentation

The full documentation is hosted on **GitHub Pages** and rendered with **MkDocs**:

- **[Read the docs](https://ficaud.github.io/horcrux-hw/)**

## Local development

To build and preview the documentation locally:

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open <http://localhost:8000>.

The site is automatically rebuilt and deployed to GitHub Pages on every push to `main` (see `.github/workflows/deploy.yml`).

## Versioning

The documentation is versioned with [`mike`](https://github.com/jimporter/mike), which publishes multiple versions of the docs and adds a version selector in the navigation bar.

### Publish a new version

```bash
pip install -r requirements.txt
mike deploy v1.0.0 latest   # build & publish version v1.0.0
mike set-default latest     # make "latest" the default version
mike deploy --push          # push the gh-pages branch
```

### List published versions

```bash
mike list
```

### Delete a version

```bash
mike delete v1.0.0 --push
```

The `latest` alias always points to the most recent version, and the CI workflow (`.github/workflows/deploy.yml`) publishes a `latest` alias on every push to `main`.

### Release via git tag (automatique)

The CI workflow is configured to deploy a versioned release automatically when you push a `v*` tag. No manual `mike` command needed:

```bash
git tag v1.0.0
git push origin v1.0.0
```

This triggers the workflow, which:
- Extracts the version from the tag (`v1.0.0` → `1.0.0`)
- Deploys that version with `mike`
- Moves the `latest` alias to the new version and sets it as default
