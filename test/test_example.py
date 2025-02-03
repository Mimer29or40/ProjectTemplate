"""Example test file."""

from __future__ import annotations

import pytest

import your_module


def test_example() -> None:
    """Example test method."""
    assert your_module.__name__ is not None


def test_main() -> None:
    """Test __main__.py."""
    from your_module.__main__ import main

    main()


if __name__ == "__main__":
    pytest.main()
