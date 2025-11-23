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

2. Project Structure

The repository is organized in a very simple and predictable way:

optus-dsa-training-python/
│
├─ pyproject.toml          # Project & dependency configuration used by uv
├─ uv.lock                 # Auto-generated lockfile (do not edit manually)
│
└─ src/                    # All DSA / course practice lives here
   ├─ arrays/
   │   ├─ two_sum.py
   │   └─ ...
   ├─ linked_list/
   │   ├─ reverse_ll.py
   │   └─ ...
   ├─ trees/
   │   ├─ inorder_traversal.py
   │   └─ ...
   ├─ graphs/
   │   ├─ bfs.py
   │   └─ ...
   └─ main.py              # Optional entry point if you want to test things


❗ Everything under src/ is pure problem-solving code.
Nothing in src/ should configure dependencies or environments.

3. Setting up the Environment

Clone the project:

git clone https://github.com/<your-username>/optus-dsa-training-python.git
cd optus-dsa-training-python


Create and sync environment using uv:

uv sync


This installs dependencies listed in pyproject.toml and creates an isolated Python environment automatically.

If you need to add a new dependency later:

uv add <package_name>


Remove a dependency:

uv remove <package_name>

4. Activating the Environment

You don't need to manually activate anything when using uv run,
but if you want to drop into the environment’s Python shell:

uv run python


Or enter a virtual environment-style shell:

uv venv
source .venv/bin/activate

5. Running / Accessing Code (Setup Only — NOT the execution explanation yet)

There are two ways this project is meant to be used for problem-solving:

✔️ Method A — File-based execution

Each file under src/<topic>/<problem>.py can be executed individually.

✔️ Method B — Central main.py

You can import and run problems through src/main.py if you prefer a single entry point.
