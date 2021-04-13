"""Dlite main module."""

from . import mapping


def align(str_):
    """Align string through possible permutations for comparison."""
    if not str_:
        return ""

    try:
        str_.encode("ascii")
        # null byte is considered valid ascii so clean it out
        str_ = str_.replace("\x00", "")

    except UnicodeEncodeError:
        translate_table = str_.maketrans(mapping.UNICODE)
        str_ = str_.translate(translate_table)

    return str_.strip().casefold()
