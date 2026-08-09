<div align="center">
<img src="docs/img/horcrux-logo.png" width="150" alt="Horcrux Core logo">

<br/>
<br/>
<br/>

# Horcrux Hardware

[![Horcrux-core](https://img.shields.io/badge/Horcrux_core-v2.2.3-orange)](https://github.com/ficaud/horcrux-core)
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
