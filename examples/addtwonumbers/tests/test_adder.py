import sys
import subprocess
from pathlib import Path
from decimal import Decimal

import pytest

# Ensure project root is importable for direct script import
ROOT = str(Path(__file__).resolve().parents[1])
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import adder


def run_cli(*args: str):
    proc = subprocess.run(
        [sys.executable, "adder.py", *args],
        capture_output=True,
        text=True,
    )
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


class TestAddFunction:
    def test_integers(self):
        assert adder.add(2, 3) == 5
        assert adder.add(-1, 4) == 3
        assert adder.add(-2, -3) == -5

    def test_decimals_and_precision(self):
        a = Decimal("0.1")
        b = Decimal("0.2")
        assert adder.add(a, b) == Decimal("0.3")

    def test_mixed_int_decimal(self):
        assert adder.add(2, Decimal("3.5")) == Decimal("5.5")

    def test_large_values(self):
        big = 10**30
        assert adder.add(big, big) == big * 2


class TestCLI:
    def test_cli_simple_integers(self):
        code, out, err = run_cli("2", "3")
        assert code == 0
        assert out == "5"
        assert err == ""

    def test_cli_negatives_and_whitespace(self):
        code, out, err = run_cli(" -1 ", " 4 ")
        assert code == 0
        assert out == "3"
        assert err == ""

    def test_cli_decimals(self):
        code, out, err = run_cli("0.1", "0.2")
        assert code == 0
        assert out == "0.3"

    def test_cli_scientific_notation(self):
        code, out, err = run_cli("1e12", "1e12")
        assert code == 0
        # Decimal prints with uppercase E by default
        assert out.upper() == "2E+12"

    def test_cli_leading_plus(self):
        code, out, err = run_cli("+2", "+3")
        assert code == 0
        assert out == "5"

    @pytest.mark.parametrize("a,b", [
        ("foo", "1"),
        ("1", "bar"),
        ("1.2.3", "4"),
    ])
    def test_cli_invalid_inputs(self, a, b):
        code, out, err = run_cli(a, b)
        assert code != 0
        # argparse by default writes to stderr; check either channel for message
        combined = "\n".join(x for x in (out, err) if x)
        assert "invalid number" in combined.lower()

    def test_cli_too_few_args(self):
        code, out, err = run_cli("1")
        assert code != 0
        combined = "\n".join(x for x in (out, err) if x)
        assert "usage" in combined.lower()

    def test_cli_too_many_args(self):
        # Pass three args; argparse should error
        proc = subprocess.run(
            [sys.executable, "adder.py", "1", "2", "3"],
            capture_output=True,
            text=True,
        )
        assert proc.returncode != 0
        combined = "\n".join(x for x in (proc.stdout.strip(), proc.stderr.strip()) if x)
        assert "usage" in combined.lower()
