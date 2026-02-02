"""
FAM 450 Number of Allowed Deviations Calculator

A Python package to calculate the number of allowed devations for tests of internal control effectiveness or ineffectiveness.
"""

from .fam450 import fam450ss, fam450lt, fam450gt

__version__ = "0.1.0"
__author__ = "Wade K. Copeland"
__email__ = "wade@kingcopeland.com"
__all__ = ["fam450ss", "fam450lt", "fam450gt"]