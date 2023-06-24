# cookiecutter-python-ghpages

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a Python package with GitHub Pages.

Features:

- Python 3.x package with [setuptools](https://setuptools.readthedocs.io/en/latest/)
    - Formatting with [black]
    - Linting with [flake8](https://flake8.pycqa.org/en/latest/)
- Testing with [pytest](https://docs.pytest.org/en/latest/)
    - Code coverage with [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
- Documentation with [Sphinx](http://www.sphinx-doc.org/en/master/)
    - Automatic API Reference from code docstrings with [autodoc](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html)
    - Optimized for [GitHub Pages](https://pages.github.com/), with separate branches for `main` and `gh-pages`
    - Read the Docs theme with [sphinx_rtd_theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/)
    - Render jupyter notebooks with [nbsphinx](https://nbsphinx.readthedocs.io/en/latest/)
