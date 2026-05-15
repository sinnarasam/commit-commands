# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a minimal Python project currently containing utility functions. The project is configured to allow Python script execution via the `.claude/settings.local.json` file.

## Development Commands

### Running Python Scripts
```bash
python3 <script_name>.py
```

### Running a Specific Function
If you need to test individual functions, you can import and run them interactively:
```bash
python3 -c "from add_numbers import add; print(add(5, 3))"
```

## Current Project Structure

- `add_numbers.py` - Simple utility with an `add()` function that sums two numbers
- `.claude/settings.local.json` - Claude Code configuration with Python execution permissions

## Permissions

The project is configured to allow:
- `Bash(python *)` - Python command execution
- `Bash(python3 *)` - Python 3 command execution

These permissions are set in `.claude/settings.local.json` and enable running Python scripts without permission prompts.

## Future Development

As this project grows, consider:
- **Testing**: Add a `tests/` directory with unit tests (e.g., using `pytest`)
- **Build/Dependencies**: If external packages are needed, create a `requirements.txt` or `pyproject.toml`
- **Code Organization**: Move related functions into separate modules as complexity increases
- **Documentation**: Add module-level docstrings and a comprehensive README.md
