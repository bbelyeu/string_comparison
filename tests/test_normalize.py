"""Unit align function."""

import string_comparison


def test_normalize():
    """Test the align method."""
    norm = string_comparison.normalize("OH YEAH")
    assert norm == "oh yeah"

    norm = string_comparison.normalize("credinţă")
    assert norm == "credinta"

    norm = string_comparison.normalize("Paști")
    assert norm == "pasti"

    norm = string_comparison.normalize("פַּסחָא")
    assert norm == "פסחא"

    norm = string_comparison.normalize("\x00")  # null byte removal
    assert norm == ""

    norm = string_comparison.normalize(
        "ww\xadw\xad.\xadg\xado\xado\xadd\xad\xad.\xad\xadc\xado\xadm\xad"
    )
    assert norm == "www.good.com"

    norm = string_comparison.normalize("3 j")
    assert norm == "3 j"
