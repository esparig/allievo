"""
allievo - A Python toolkit for music students.

Starting with smart scale selection and expanding into a full learning companion.
"""

from .scales import Scale, get_major_scale, get_minor_scale, suggest_scale_for_beginner

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "Scale",
    "get_major_scale", 
    "get_minor_scale",
    "suggest_scale_for_beginner"
]