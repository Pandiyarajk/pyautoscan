# PyAutoScan Development Guide

This document provides comprehensive information for developers working on PyAutoScan.

## Table of Contents

- [Development Setup](#development-setup)
- [Code Quality Tools](#code-quality-tools)
- [Testing](#testing)
- [Building and Distribution](#building-and-distribution)
- [Contributing Guidelines](#contributing-guidelines)
- [Code Style](#code-style)
- [Security Considerations](#security-considerations)

## Development Setup

### Prerequisites

- Python 3.7+ (Tested on Python 3.13)
- Windows 10/11 (Required for WIA functionality)
- Git
- A compatible scanner with WIA drivers

### Initial Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Pandiyarajk/pyautoscan.git
   cd pyautoscan
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install development dependencies:**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Install pre-commit hooks:**
   ```bash
   pre-commit install
   ```

### Development Dependencies

The following tools are configured for development:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **bandit**: Security scanning
- **pytest**: Testing framework
- **pre-commit**: Git hooks for code quality

## Code Quality Tools

### Automated Code Formatting

```bash
# Format code with Black and isort
make format

# Check formatting without making changes
make lint
```

### Type Checking

```bash
# Run mypy type checking
make type-check
```

### Security Scanning

```bash
# Run bandit security checks
make security-check
```

### Running All Checks

```bash
# Run all quality checks
make check-all
```

## Testing

### Running Tests

```bash
# Run all tests
make test

# Run tests with coverage
python -m pytest tests/ --cov=pyautoscan --cov-report=html

# Run specific test file
python -m pytest tests/test_basic_scan.py -v
```

### Test Structure

- **Unit Tests**: Test individual functions and classes
- **Integration Tests**: Test module interactions
- **Mock Tests**: Test WIA interactions without hardware

### Writing Tests

1. **Follow naming conventions:**
   - Test files: `test_*.py`
   - Test classes: `Test*`
   - Test methods: `test_*`

2. **Use descriptive test names:**
   ```python
   def test_auto_scan_no_scanner_detected(self):
       """Test auto_scan when no scanner is detected"""
   ```

3. **Mock external dependencies:**
   ```python
   @patch('pyautoscan.basic_scan.win32com.client.Dispatch')
   def test_auto_scan_no_scanner(self, mock_dispatch):
   ```

## Building and Distribution

### Local Development

```bash
# Build package locally
make build

# Install package locally
make install-local

# Uninstall local package
make uninstall-local
```

### Distribution

```bash
# Create distribution packages
make dist

# Upload to TestPyPI
make upload-testpypi

# Upload to PyPI
make upload-pypi
```

### Package Structure

```
pyautoscan/
├── __init__.py          # Package initialization
├── basic_scan.py        # Basic scanning functionality
├── advanced_scan.py     # Advanced scanning features
└── scanner_info.py      # Scanner information utility
```

## Contributing Guidelines

### Code Style

- **Follow PEP 8**: Use Black for automatic formatting
- **Type Hints**: Use type annotations for all functions
- **Docstrings**: Use Google-style docstrings
- **Line Length**: Maximum 88 characters (Black default)

### Commit Messages

Use conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

Examples:
- `feat(scanner): add auto-crop functionality`
- `fix(basic_scan): resolve logger scope issue`
- `docs(readme): update installation instructions`

### Pull Request Process

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. **Make your changes and commit:**
   ```bash
   git add .
   git commit -m "feat(scanner): add amazing feature"
   ```

3. **Push and create PR:**
   ```bash
   git push origin feature/amazing-feature
   ```

4. **Ensure all checks pass:**
   - Code formatting (Black)
   - Import sorting (isort)
   - Linting (flake8)
   - Type checking (mypy)
   - Security scanning (bandit)
   - Tests (pytest)

## Code Style

### Python Code

```python
from typing import Optional, List, Dict, Any
import os
from datetime import datetime

import win32com.client
from PIL import Image

from powerlogger import get_logger


def auto_scan(
    output_dir: str = "Scans",
    file_format: str = "jpg",
    quality: str = "medium"
) -> Optional[str]:
    """
    Automatically scan documents using the first available scanner.
    
    Args:
        output_dir: Directory to save scanned files
        file_format: Output format (jpg, png, tiff, pdf)
        quality: Scan quality (low, medium, high)
    
    Returns:
        Path to saved file on success, None on failure
    """
    logger = get_logger("PyAutoScan.BasicScanner")
    
    try:
        # Implementation here
        pass
    except Exception as e:
        logger.error(f"Scan failed: {e}")
        return None
```

### Configuration Files

- **INI files**: Use clear section names and descriptive keys
- **YAML files**: Use consistent indentation and structure
- **TOML files**: Use for pyproject.toml and configuration

## Security Considerations

### Input Validation

- **File paths**: Validate and sanitize file paths
- **User input**: Validate all user-provided parameters
- **Configuration**: Validate configuration file contents

### External Dependencies

- **WIA API**: Use proper error handling for COM operations
- **File operations**: Use safe file handling practices
- **Image processing**: Validate image files before processing

### Security Tools

- **Bandit**: Automated security scanning
- **Pre-commit hooks**: Prevent insecure code from being committed
- **Regular audits**: Review dependencies for security updates

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure virtual environment is activated
2. **Type checking failures**: Add proper type annotations
3. **Formatting issues**: Run `make format` to fix
4. **Test failures**: Check mock configurations and dependencies

### Development Environment

- **Windows-specific**: Some functionality only works on Windows
- **Scanner hardware**: Tests may fail without compatible hardware
- **WIA drivers**: Ensure proper scanner drivers are installed

## Additional Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [Black Code Style](https://black.readthedocs.io/)
- [MyPy Type Checking](https://mypy.readthedocs.io/)
- [Pytest Testing Framework](https://docs.pytest.org/)
- [Pre-commit Hooks](https://pre-commit.com/)

## Support

For development questions or issues:

- **GitHub Issues**: [https://github.com/Pandiyarajk/pyautoscan/issues](https://github.com/Pandiyarajk/pyautoscan/issues)
- **Documentation**: [https://github.com/Pandiyarajk/pyautoscan#readme](https://github.com/Pandiyarajk/pyautoscan#readme)
- **Author**: Pandiyaraj Karuppasamy (pandiyarajk@live.com)
