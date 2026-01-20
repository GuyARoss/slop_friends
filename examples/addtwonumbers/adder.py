"""
Minimal adder: a testable function and a tiny CLI.

Usage:
  python adder.py 2 3          # prints 5
  python adder.py -1 4.5       # prints 3.5
  python adder.py 1e12 1e12    # prints 2E+12

Notes:
  - Uses Decimal for precise parsing of non-integer numbers.
  - Accepts integers and decimal/scientific notation strings.
  - Exits non-zero on invalid inputs.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
from typing import Union

Number = Union[int, Decimal]


def add(a: Number, b: Number) -> Number:
    """Return the sum of two numeric values.

    Accepts `int` or `Decimal`. Mixed types are supported and will yield a
    `Decimal` when any operand is a `Decimal`.
    """

    return a + b


def _parse_number(raw: str) -> Number:
    s = raw.strip()
    # Try integer first to preserve int type for whole numbers
    try:
        # Disallow integers with a leading '+' that int() accepts but keep consistent
        # behavior (int allows '+', that's fine). If it parses, return int.
        i = int(s, 10)
        return i
    except ValueError:
        pass

    # Fallback to Decimal for non-integer numeric formats
    try:
        # Use the original string for exact decimal parsing
        d = Decimal(s)
        return d
    except (InvalidOperation, ValueError):
        raise argparse.ArgumentTypeError(f"invalid number: '{raw}'")


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Add two numbers and print the sum.",
    )
    p.add_argument("a", type=_parse_number, help="First number (int or decimal)")
    p.add_argument("b", type=_parse_number, help="Second number (int or decimal)")
    return p


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    result = add(args.a, args.b)
    # Print as-is; Decimal and int have sensible str() representations
    print(result)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

