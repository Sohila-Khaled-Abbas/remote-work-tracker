# Contributing to Remote Work Tracker

<div align="center">

![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**Thank you for your interest in contributing to the Remote Work Tracker project!** 🎉

</div>

---

## 📋 Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [Getting Started](#-getting-started)
- [How Can I Contribute?](#-how-can-i-contribute)
- [Development Workflow](#-development-workflow)
- [Coding Standards](#-coding-standards)
- [Commit Message Guidelines](#-commit-message-guidelines)
- [Pull Request Process](#-pull-request-process)
- [Testing Guidelines](#-testing-guidelines)
- [Documentation](#-documentation)
- [Community](#-community)

---

## 📜 Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [INSERT CONTACT EMAIL].

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11+** ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/downloads))
- **pip** (Python package manager)
- **virtualenv** or **venv** (for virtual environments)

### Setting Up Your Development Environment

1. **Fork the Repository**

   Click the "Fork" button at the top right of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/Sohila-Khaled-Abbas/remote-work-tracker.git
   cd remote-work-tracker
   ```

3. **Add Upstream Remote**

   ```bash
   git remote add upstream https://github.com/Sohila-Khaled-Abbas/remote-work-tracker.git
   ```

4. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

5. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

6. **Verify Installation**

   ```bash
   python remotive_api_scraper.py --help
   ```

---

## 🤝 How Can I Contribute?

### 🐛 Reporting Bugs

**When submitting a bug report, include:**

- **Clear and descriptive title**
- **Detailed description** of the issue
- **Steps to reproduce** the behavior
- **Expected behavior** vs. actual behavior
- **Screenshots** (if applicable)
- **Environment details:**
  - OS: [e.g., Windows 11, macOS 14, Ubuntu 22.04]
  - Python version: [e.g., 3.11.0]
  - Package versions: [from `pip freeze`]
- **Error messages** or logs (use code blocks)

**Template:**

```markdown
## Bug Description
[Clear description of the bug]

## Steps to Reproduce
1. Step one
2. Step two
3. ...

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- OS: 
- Python: 
- Package versions: 

## Additional Context
[Any other relevant information]
```

---

### 💡 Suggesting Enhancements

We welcome feature requests and enhancement suggestions!

**When suggesting an enhancement, include:**

- **Clear and descriptive title**
- **Detailed description** of the proposed feature
- **Use case** - why is this enhancement needed?
- **Proposed solution** or implementation approach
- **Alternatives considered**
- **Additional context** (mockups, examples, etc.)

---

### 📝 Contributing Code

#### Types of Contributions

- **Bug fixes** 🐛
- **New features** ✨
- **Performance improvements** ⚡
- **Documentation updates** 📚
- **Code refactoring** ♻️
- **Test coverage improvements** 🧪
- **CI/CD enhancements** 🔧

---

## 🔄 Development Workflow

### 1. Create a Branch

Always create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

**Branch Naming Conventions:**

- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Test additions or modifications
- `chore/` - Maintenance tasks

**Examples:**

```bash
git checkout -b feature/add-linkedin-scraper
git checkout -b fix/api-rate-limit-handling
git checkout -b docs/update-readme
```

---

### 2. Make Your Changes

- Write clean, readable, and well-documented code
- Follow the [Coding Standards](#-coding-standards)
- Add or update tests as needed
- Update documentation if necessary

---

### 3. Test Your Changes

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_scraper.py

# Run with coverage
pytest --cov=. --cov-report=html
```

---

### 4. Commit Your Changes

Follow our [Commit Message Guidelines](#-commit-message-guidelines):

```bash
git add .
git commit -m "feat: add LinkedIn job scraper integration"
```

---

### 5. Keep Your Branch Updated

```bash
git fetch upstream
git rebase upstream/main
```

---

### 6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

---

### 7. Submit a Pull Request

Go to the original repository and click "New Pull Request".

---

## 💻 Coding Standards

### Python Style Guide

We follow **PEP 8** with some modifications:

#### Code Formatting

- **Line length:** Maximum 100 characters (not 79)
- **Indentation:** 4 spaces (no tabs)
- **Quotes:** Use double quotes `"` for strings
- **Imports:** Group and sort imports (stdlib → third-party → local)

#### Example:

```python
"""
Module docstring describing the purpose of this module.
"""

import os
import sys
from typing import List, Dict, Optional

import pandas as pd
import requests
from bs4 import BeautifulSoup

from utils import setup_logger


class RemoteJobScraper:
    """
    A class to scrape remote job postings from various sources.
    
    Attributes:
        api_url (str): The base URL for the API endpoint.
        timeout (int): Request timeout in seconds.
    """
    
    def __init__(self, api_url: str, timeout: int = 30) -> None:
        """
        Initialize the RemoteJobScraper.
        
        Args:
            api_url: The base URL for the API endpoint.
            timeout: Request timeout in seconds. Defaults to 30.
        """
        self.api_url = api_url
        self.timeout = timeout
        self.logger = setup_logger(__name__)
    
    def fetch_jobs(self, category: str) -> List[Dict[str, str]]:
        """
        Fetch job postings for a specific category.
        
        Args:
            category: The job category to fetch.
        
        Returns:
            A list of dictionaries containing job information.
        
        Raises:
            requests.RequestException: If the API request fails.
        """
        try:
            response = requests.get(
                f"{self.api_url}/jobs",
                params={"category": category},
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch jobs: {e}")
            raise
```

#### Naming Conventions

- **Variables and functions:** `snake_case`
- **Classes:** `PascalCase`
- **Constants:** `UPPER_SNAKE_CASE`
- **Private methods:** `_leading_underscore`

```python
# Good
def fetch_remote_jobs(api_url: str) -> List[Dict]:
    pass

class JobDataProcessor:
    pass

MAX_RETRIES = 3
API_BASE_URL = "https://api.example.com"
```

#### Type Hints

Use type hints for function signatures:

```python
from typing import List, Dict, Optional

def process_job_data(
    jobs: List[Dict[str, str]], 
    filter_category: Optional[str] = None
) -> pd.DataFrame:
    """Process and filter job data."""
    pass
```

#### Docstrings

Use Google-style docstrings:

```python
def calculate_salary_stats(salaries: List[float]) -> Dict[str, float]:
    """
    Calculate statistical measures for salary data.
    
    Args:
        salaries: A list of salary values.
    
    Returns:
        A dictionary containing mean, median, and std deviation.
    
    Raises:
        ValueError: If the salaries list is empty.
    
    Example:
        >>> calculate_salary_stats([50000, 60000, 70000])
        {'mean': 60000.0, 'median': 60000.0, 'std': 10000.0}
    """
    if not salaries:
        raise ValueError("Salaries list cannot be empty")
    
    return {
        "mean": statistics.mean(salaries),
        "median": statistics.median(salaries),
        "std": statistics.stdev(salaries)
    }
```

---

### Code Quality Tools

We use the following tools to maintain code quality:

#### Black (Code Formatter)

```bash
pip install black
black . --line-length 100
```

#### Flake8 (Linter)

```bash
pip install flake8
flake8 . --max-line-length=100 --exclude=venv
```

#### isort (Import Sorter)

```bash
pip install isort
isort . --profile black
```

#### mypy (Type Checker)

```bash
pip install mypy
mypy . --ignore-missing-imports
```

#### Pre-commit Hook (Recommended)

```bash
pip install pre-commit
pre-commit install
```

---

## 📝 Commit Message Guidelines

We follow the **Conventional Commits** specification for clear and structured commit messages.

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat:** A new feature
- **fix:** A bug fix
- **docs:** Documentation changes
- **style:** Code style changes (formatting, no logic change)
- **refactor:** Code refactoring (no feature or bug fix)
- **perf:** Performance improvements
- **test:** Adding or updating tests
- **chore:** Maintenance tasks, dependencies, build config
- **ci:** CI/CD configuration changes

### Examples

```bash
# Feature
feat(scraper): add support for LinkedIn job scraping

# Bug fix
fix(etl): handle null values in salary field correctly

# Documentation
docs(readme): update installation instructions for Windows

# Refactoring
refactor(db): optimize database query performance

# Testing
test(scraper): add unit tests for API error handling

# Chore
chore(deps): update pandas to version 2.0.0
```

### Detailed Example

```
feat(scraper): add support for Indeed job scraping

- Implement IndeedScraper class with BeautifulSoup
- Add rate limiting to respect robots.txt
- Include error handling for network failures
- Update documentation with usage examples

Closes #42
```

---

## 🔀 Pull Request Process

### Before Submitting

- [ ] **Code follows** the project's coding standards
- [ ] **Tests pass** locally
- [ ] **Documentation updated** (if applicable)
- [ ] **Commit messages** follow the guidelines
- [ ] **Branch is up-to-date** with main
- [ ] **No merge conflicts**

### PR Title Format

Follow the same convention as commit messages:

```
feat(scraper): add LinkedIn job scraping support
fix(etl): resolve null value handling in salary field
```

### PR Description Template

```markdown
## Description
[Provide a clear description of the changes]

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Related Issues
Closes #[issue number]

## Changes Made
- [Change 1]
- [Change 2]
- [Change 3]

## Testing
[Describe the tests you ran and how to reproduce them]

## Screenshots (if applicable)
[Add screenshots to help explain your changes]

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published
```

### Review Process

1. **Automated checks** will run (linting, tests, coverage)
2. **Maintainers will review** your code
3. **Address feedback** by pushing new commits
4. Once approved, a **maintainer will merge** your PR

---

## 🧪 Testing Guidelines

### Writing Tests

- Use **pytest** for all tests
- Aim for **>80% code coverage**
- Write **unit tests** for individual functions
- Write **integration tests** for workflows
- Use **fixtures** for test data

### Test Structure

```python
import pytest
from remotive_api_scraper import RemoteJobScraper


class TestRemoteJobScraper:
    """Test suite for RemoteJobScraper class."""
    
    @pytest.fixture
    def scraper(self):
        """Fixture to create a scraper instance."""
        return RemoteJobScraper(api_url="https://api.example.com")
    
    def test_fetch_jobs_success(self, scraper, requests_mock):
        """Test successful job fetching."""
        requests_mock.get(
            "https://api.example.com/jobs",
            json={"jobs": [{"title": "Developer", "company": "TechCo"}]}
        )
        
        result = scraper.fetch_jobs("software-dev")
        
        assert len(result) == 1
        assert result[0]["title"] == "Developer"
    
    def test_fetch_jobs_api_error(self, scraper, requests_mock):
        """Test handling of API errors."""
        requests_mock.get(
            "https://api.example.com/jobs",
            status_code=500
        )
        
        with pytest.raises(requests.RequestException):
            scraper.fetch_jobs("software-dev")
```

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_scraper.py

# Run specific test
pytest tests/test_scraper.py::TestRemoteJobScraper::test_fetch_jobs_success

# Run with coverage
pytest --cov=. --cov-report=html

# Run with coverage and show missing lines
pytest --cov=. --cov-report=term-missing
```

---

## 📚 Documentation

### Code Documentation

- **Docstrings** for all public modules, classes, and functions
- **Inline comments** for complex logic
- **Type hints** for function signatures

### Project Documentation

When updating documentation:

- Keep **README.md** up-to-date
- Update **API documentation** if adding/changing endpoints
- Add **usage examples** for new features
- Update **troubleshooting** section if relevant

---

## 👥 Community

### Getting Help

- **GitHub Discussions:** Ask questions and share ideas
- **Issues:** Report bugs or request features
- **Pull Requests:** Contribute code

### Recognition

Contributors will be recognized in:

- **README.md** Contributors section
- **Project documentation**

---

## 🎯 Good First Issues

Looking for a place to start? Check out issues labeled:

- `good first issue` - Great for newcomers
- `help wanted` - We need your expertise
- `documentation` - Help improve our docs

---

## 📞 Contact

- **Project Maintainer:** Sohila Khaled Abbas
- **GitHub:** [@Sohila-Khaled-Abbas]

---

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

<div align="center">

**Thank you for contributing to Remote Work Tracker!** 🙏

Made with ❤️ by Sohila

</div>

