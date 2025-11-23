# optus-dsa-training-python

> Data Structures & Algorithms training repository using **Python** and **uv** 🐍⚙️  

This project is meant to be a clean, simple template for practicing DSA problems in Python while using **[uv](https://github.com/astral-sh/uv)** as the dependency manager and runner.

The idea is:

- Keep **all course/problem code** under `src/`
- Keep **project configuration** (like `pyproject.toml`) at the root
- Use `uv` for everything: creating environments, installing dependencies, and running scripts

---

## 1. Prerequisites

Before using this project, make sure you have:

1. **Python** (3.10+ recommended)
2. **uv** installed

Install `uv` (if not already installed):

```bash
# On most systems
curl -LsSf https://astral.sh/uv/install.sh | sh
