#!/usr/bin/env python
"""Utility to assist with string comparisons."""
import sys

from setuptools import setup

if sys.version_info < (3, 7):
    sys.exit("Sorry, Python < 3.7 is not supported")

__version__ = "1.0.0"

setup(
    name="string_comparison",
    version=__version__,
    description=__doc__,
    author="Brad Belyeu",
    author_email="bradley.belyeu@life.church",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    download_url=f"https://github.com/bbelyeu/string_comparison/archive/{__version__}.zip",
    keywords=["unicode"],
    license="MIT",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    platforms="any",
    py_modules=["string_comparison"],
    python_requires=">3.7.0",
    test_suite="tests",
    url="https://github.com/bbelyeu/string_comparison/",
)
