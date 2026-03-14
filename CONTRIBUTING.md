# Contributing to tokenopt

Thanks for your interest in contributing!

## Quick Start

For first-time setup, run the environment bootstrap:

- **Windows**: `setup.bat`
- **macOS / Linux**: `chmod +x setup.sh && ./setup.sh`

The setup script handles dependency installation, environment configuration, and test verification automatically.

## Development Workflow

1. Fork and clone the repository
2. Run the setup script (see above)
3. Create a feature branch: `git checkout -b feature/my-feature`
4. Make your changes
5. Run tests: `pytest`
6. Submit a pull request

## Testing

```bash
pytest tests/ -v
```

## Code Style

We use `black` for formatting and `ruff` for linting:

```bash
black tokenopt/ tests/
ruff check tokenopt/ tests/
```

## Reporting Issues

Please include:
- Python version (`python --version`)
- OS and architecture
- Steps to reproduce
