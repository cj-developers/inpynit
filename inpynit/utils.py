"""
inpynit 유틸리티 함수들
"""

import re
import subprocess
import sys
from pathlib import Path


def validate_project_name(name: str) -> bool:
    """
    프로젝트 이름의 유효성을 검사합니다.

    Args:
        name: 검사할 프로젝트 이름

    Returns:
        bool: 유효한 이름인지 여부
    """
    # 파이썬 패키지 이름 규칙에 따라 검증
    pattern = re.compile(r"^[a-zA-Z][a-zA-Z0-9_-]*$")
    return bool(pattern.match(name)) and len(name) > 0


def create_virtual_env(project_path: Path) -> bool:
    """
    프로젝트 디렉토리에 가상환경을 생성합니다.

    Args:
        project_path: 프로젝트 경로

    Returns:
        bool: 성공 여부
    """
    try:
        venv_path = project_path / "venv"
        subprocess.run(
            [sys.executable, "-m", "venv", str(venv_path)],
            check=True,
            capture_output=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def get_python_version() -> str:
    """
    현재 실행 중인 파이썬 버전을 반환합니다.

    Returns:
        str: 파이썬 버전 (예: "3.9")
    """
    version_info = sys.version_info
    return f"{version_info.major}.{version_info.minor}"


def sanitize_filename(filename: str) -> str:
    """
    파일명에서 유효하지 않은 문자들을 제거합니다.

    Args:
        filename: 원본 파일명

    Returns:
        str: 정리된 파일명
    """
    # 파일명에 사용할 수 없는 문자들 제거
    invalid_chars = r'<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, "_")
    return filename


def format_project_description(description: str, max_length: int = 100) -> str:
    """
    프로젝트 설명을 적절한 길이로 포맷팅합니다.

    Args:
        description: 원본 설명
        max_length: 최대 길이

    Returns:
        str: 포맷팅된 설명
    """
    if len(description) <= max_length:
        return description

    # 단어 경계에서 자르기
    words = description.split()
    result = []
    current_length = 0

    for word in words:
        if current_length + len(word) + 1 <= max_length:
            result.append(word)
            current_length += len(word) + 1
        else:
            break

    if result:
        return " ".join(result) + "..."
    else:
        return description[: max_length - 3] + "..."


def check_command_available(command: str) -> bool:
    """
    시스템에서 특정 명령어가 사용 가능한지 확인합니다.

    Args:
        command: 확인할 명령어

    Returns:
        bool: 사용 가능 여부
    """
    try:
        subprocess.run([command, "--version"], check=True, capture_output=True, text=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def get_git_user_info() -> tuple[str, str]:
    """
    Git 사용자 정보를 가져옵니다.

    Returns:
        tuple: (사용자명, 이메일)
    """
    try:
        # Git 사용자명 가져오기
        name_result = subprocess.run(
            ["git", "config", "--global", "user.name"],
            capture_output=True,
            text=True,
            check=True,
        )
        name = name_result.stdout.strip()

        # Git 이메일 가져오기
        email_result = subprocess.run(
            ["git", "config", "--global", "user.email"],
            capture_output=True,
            text=True,
            check=True,
        )
        email = email_result.stdout.strip()

        return (name, email)
    except subprocess.CalledProcessError:
        return ("Developer", "dev@example.com")
