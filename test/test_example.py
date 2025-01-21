"""Example test file."""

from __future__ import annotations

import pytest

import your_module


def test_example() -> None:
    """Example test method."""
    assert your_module.__name__ is not None


if __name__ == "__main__":
    pytest.main()
