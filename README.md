Static pip "simple" index generator

This repository contains a small manifest and a generator to produce a static PEP 503-compatible "simple" index for pip.

Files
- `packages.txt` - manifest lines using the minimal format: `name @ url [; marker] [# comment]`
- `generate_index.py` - script that reads `packages.txt` and writes the static `simple/` directory
- `simple/` - generated output (do not edit directly)

Usage

1. Regenerate the index:

```powershell
python .\generate_index.py
```

2. Serve the static `simple/` directory. For a quick local server:

```powershell
# From the repository root (Windows PowerShell)
cd .\
python -m http.server 8000 --directory .\simple\
# Then open http://localhost:8000 in your browser
```

Notes
- The generator is intentionally simple. It canonicalizes package names per PEP 503 and creates per-package pages with links to the provided URLs.
- You can expand `packages.txt` with more entries. Lines that don't match the pattern are skipped with a warning.

License
- The generated index contains links to external packages. This repository contains only a generator and manifest. Use according to the licenses of the linked packages.
