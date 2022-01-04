"""unduh anime dan film subtitle Indonesia"""

__version__ = "0.0.1"
__author__ = "Yoga"
__license__ = "MIT"
__all__ = [
    "extractors",
    "Bypass"
]

from .cli import main
from .extractors.bypasser import Bypass
