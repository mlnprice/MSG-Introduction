"""Tests the mathematical functions defined in my_pkg/trail.py
"""

import pytest

def test_square():
    """Tests the squaring function"""

    from my_pkg.trial import square

    assert 4 == square(2)
    assert 4 == square(-2)
    assert 12.25 == square(3.5)
    assert 2 == round(square(sqrt(2)), 5)

def test_factorial():
    """Tests the factorial function."""

    from my_pkg.trial import factorial

    assert 24 == factorial(4)
    assert 6 == factorial(3.0)
    assert 1 == factorial(0)
    assert 1 == factorial(-1)

    with pytest.raises(ValueError):
        factorial(3.5)
