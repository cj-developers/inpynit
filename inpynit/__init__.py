"""
inpynit: 무한한 가능성을 가진 파이썬 프로젝트를 시작하게 해주는 도구

Infinite + Python + Init = inpynit
"""

try:
    from ._version import version as __version__
except ImportError:
    # 개발 모드이거나 setuptools_scm이 실행되지 않은 경우
    try:
        from importlib.metadata import version

        __version__ = version("inpynit")
    except Exception:
        __version__ = "0.0.0+dev"

__author__ = "inpynit"
__email__ = "contact@inpynit.dev"

from .core import ProjectCreator
from .templates import get_available_templates

__all__ = ["ProjectCreator", "get_available_templates"]
