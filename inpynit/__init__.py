"""
inpynit: 무한한 가능성을 가진 파이썬 프로젝트를 시작하게 해주는 도구

Infinite + Python + Init = inpynit
"""

__version__ = "0.1.0"
__author__ = "inpynit"
__email__ = "contact@inpynit.dev"

from .core import ProjectCreator
from .templates import get_available_templates

__all__ = ["ProjectCreator", "get_available_templates"]
