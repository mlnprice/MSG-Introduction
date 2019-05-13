"""Tests the mathematical functions defined in my_pkg/trail.py
"""

import pytest

def test_square():
    """Tests the squaring function"""

    from my_pkg.trial import square

    assert 4 == square(2)
