# allievo
A Python toolkit for music students, starting with smart scale selection and expanding into a full learning companion.

## Installation

```bash
pip install allievo
```

## Usage

```python
import allievo

# Get a C major scale for beginners
scale = allievo.suggest_scale_for_beginner()
print(scale.get_notes())  # ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Create custom scales
c_major = allievo.get_major_scale('C')
a_minor = allievo.get_minor_scale('A')
```

## Development and Releases

This project uses automated releases based on conventional commits. When a PR is merged to main, the GitHub Action will:

1. Analyze commit messages to determine version bump:
   - `feat: ...` → MINOR version bump
   - `fix: ...` → PATCH version bump  
   - `BREAKING CHANGE: ...` → MAJOR version bump

2. Create a new release with updated version
3. Publish the package to PyPI

### Commit Message Format

Use conventional commits for automatic versioning:

- `feat: add scale suggestion feature` → 0.1.0 → 0.2.0
- `fix: correct interval calculation` → 0.1.0 → 0.1.1  
- `feat!: refactor scale engine` or `BREAKING CHANGE: refactor scale engine` → 0.1.0 → 1.0.0

### Setup Requirements

For the automated release to work, ensure these secrets are configured in the repository:

- `GITHUB_TOKEN`: Automatically provided by GitHub Actions
- `PYPI_API_TOKEN`: Your PyPI API token for publishing packages
