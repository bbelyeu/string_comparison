"""Unit align function."""

import dlite


def test_align():
    """Test the align method."""
    aligned = dlite.align("OH YEAH")
    assert aligned == "oh yeah"

    aligned = dlite.align("credinţă")
    assert aligned == "credinta"

    aligned = dlite.align("Paști")
    assert aligned == "pasti"

    aligned = dlite.align("פַּסחָא")
    assert aligned == "פסחא"

    aligned = dlite.align("\x00")  # null byte removal
    assert aligned == ""
