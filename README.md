# dlite

Text normalization for string comparison in Python.

## Requirements

This project requires Python 3.7+

## Installation

To install with pip

    pip install dlite

## Usage

    import dlite
    normalized = dlite.align("é")
    assert normalized == "e"
