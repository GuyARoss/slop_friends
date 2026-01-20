Adder — Minimal Two-Number Adder

Overview
- Simple Python utility to add two numbers.
- Provides a testable `add(a, b)` function and a tiny CLI.
- Accepts integers, decimals, and scientific notation; errors on invalid input.

Requirements
- Python 3.8+
- No external dependencies (tests use `pytest`).

Quick Start
- CLI: `python adder.py <a> <b>`
- Examples:
  - `python adder.py 2 3` → `5`
  - `python adder.py -1 4.5` → `3.5`
  - `python adder.py 1e12 1e12` → `2E+12`

Programmatic Use
- Import and call directly:
  - `from adder import add`
  - `add(2, 3)  # 5`
  - `from decimal import Decimal; add(Decimal("0.1"), Decimal("0.2"))  # Decimal('0.3')`

Input Rules
- Accepts: integers (e.g., `5`, `-2`, `+3`), decimals (e.g., `0.1`), and scientific notation (e.g., `1e6`).
- Whitespace around numbers is ignored.
- Invalid inputs exit non‑zero with a helpful error (e.g., `invalid number: 'foo'`).
- Current behavior forwards special Decimal values (e.g., `NaN`, `Infinity`) as entered; see “Open Questions”.

Errors and Exit Codes
- Invalid number or wrong number of arguments: non‑zero exit and usage/error shown via `argparse`.

Run Tests
- Ensure `pytest` is installed: `python -m pip install pytest` (once).
- Run: `python -m pytest -q`

Open Questions
- Whether to explicitly reject `NaN`/`Infinity` (currently accepted by `Decimal`).
- Whether to support locale-specific formats (e.g., commas in numbers); currently not supported.

