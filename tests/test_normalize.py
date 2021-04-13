"""Unit align function."""

import string_comparison


def test_normalize():
    """Test the align method."""
    aligned = string_comparison.normalize("OH YEAH")
    assert aligned == "oh yeah"

    aligned = string_comparison.normalize("credinţă")
    assert aligned == "credinta"

    aligned = string_comparison.normalize("Paști")
    assert aligned == "pasti"

    aligned = string_comparison.normalize("פַּסחָא")
    assert aligned == "פסחא"

    aligned = string_comparison.normalize("\x00")  # null byte removal
    assert aligned == ""
