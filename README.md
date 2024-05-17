# String Comparison

Text normalization for string comparison in Python.

This maps a Unicode code point key represented as an integer to a corresponding ASCII
character mapping. In some cases such as Hebrew niqqud & cantillation, we remove the
character altogether or replace certain punctuation with a space.

In addition, some characters are removed prior to normalization. For example, Unicode control chars.

## Requirements

This project requires Python 3.7+

## Installation

To install with pip

    pip install string_comparison

## Usage

    import string_comparison
    normalized = string_comparison.normalize("é")
    assert normalized == "e"
