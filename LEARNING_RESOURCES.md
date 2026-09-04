# Python Environment and Packaging Notes

These notes explain the development setup used by the EEG AI Platform and provide resources to revisit later.

## 1. Python scripts and Python packages

A small script can be run directly:

```powershell
python xyz.py
```

This works because Python is given the exact file to execute.

The EEG AI Platform is being built as a package with several connected modules:

```text
src/eeg_ai_platform/
├── preprocessing.py
├── training.py
├── prediction.py
├── database.py
└── api.py
```

Other code can then import its components:

```python
from eeg_ai_platform.preprocessing import process_eeg
```

## 2. Virtual environment

A virtual environment gives one project its own Python packages and versions. It prevents dependencies from different projects from interfering with one another.

Create the environment:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal prompt begins with `(.venv)`.

Verify the Python executable:

```powershell
where.exe python
```

The first result should point to `.venv\Scripts\python.exe`.

## 3. Editable installation

A normal installation:

```powershell
python -m pip install .
```

installs a fixed copy of the package into the virtual environment.

An editable installation:

```powershell
python -m pip install -e .
```

tells Python to use the package directly from the project's source folder. Changes to files under `src/eeg_ai_platform` are therefore available immediately without reinstalling the package after each edit.

In this project, we used:

```powershell
python -m pip install -e ".[dev]"
```

- `-e` means editable mode.
- `.` means the project in the current directory.
- `[dev]` installs optional development dependencies defined in `pyproject.toml`, including pytest.

Editable mode is mainly for development. Production deployments normally use a regular fixed installation.

## 4. Source layout

The repository uses:

```text
eeg-ai-platform/
├── src/
│   └── eeg_ai_platform/
├── tests/
├── pyproject.toml
└── README.md
```

- `eeg-ai-platform` is the readable repository and distribution name.
- `eeg_ai_platform` is the importable Python package name. Python import names use underscores rather than hyphens.
- `src` separates application code from tests, documentation, and configuration.

## 5. Running tests

Run all tests with:

```powershell
python -m pytest
```

The initial project test result was:

```text
2 passed
```

## Videos to watch

1. [Corey Schafer — Python VENV on Windows](https://www.youtube.com/watch?v=APOPm01BVrk)
   - Focus on why virtual environments exist, how to create one, and how activation changes the active Python interpreter.

2. [Corey Schafer — Managing Python projects and virtual environments](https://www.youtube.com/watch?v=cY2NXB_Tqq0)
   - Focus on how separate projects maintain separate dependencies.

For editable installation and modern packaging, search YouTube for:

```text
Python src layout pyproject.toml pip install editable
```

Prefer newer videos using `pyproject.toml`. Older tutorials based mainly on `setup.py` may still explain useful concepts, but they use an older project configuration style.

## Written reference

- [Python Packaging User Guide — Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

## Short interview explanations

**Virtual environment**

> A virtual environment isolates a project's Python interpreter and dependencies, preventing package conflicts between projects.

**Editable installation**

> Editable installation allows the virtual environment to import directly from the project's source directory, so code changes are immediately available during development without reinstalling the package.

**Source layout**

> I used a src layout to separate importable application code from tests and project configuration and to make packaging behaviour more reliable.
