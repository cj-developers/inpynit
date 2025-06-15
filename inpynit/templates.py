"""
inpynit 템플릿 관리 모듈
"""

from typing import Any, Dict, List

# 템플릿 설정 정보
TEMPLATE_CONFIGS = {
    "basic": {
        "name": "기본 패키지",
        "description": "기본적인 파이썬 패키지 구조",
        "directories": [
            "{project_slug}",
            "tests",
            "docs",
            ".vscode",
        ],
        "files": [
            {"template": "pyproject.toml.j2", "output": "pyproject.toml"},
            {"template": "README.md.j2", "output": "README.md"},
            {"template": "main.py.j2", "output": "{project_slug}/__init__.py"},
            {"template": "main.py.j2", "output": "{project_slug}/main.py"},
            {"template": "test_main.py.j2", "output": "tests/test_main.py"},
            {"template": "gitignore.j2", "output": ".gitignore"},
            {"template": ".vscode/settings.json.j2", "output": ".vscode/settings.json"},
        ],
    },
    "fastapi": {
        "name": "FastAPI 웹 앱",
        "description": "FastAPI 기반 웹 애플리케이션",
        "directories": [
            "{project_slug}",
            "{project_slug}/api",
            "{project_slug}/core",
            "{project_slug}/models",
            "tests",
            "docs",
        ],
        "files": [
            {"template": "pyproject.toml.j2", "output": "pyproject.toml"},
            {"template": "README.md.j2", "output": "README.md"},
            {"template": "fastapi_main.py.j2", "output": "{project_slug}/main.py"},
            {"template": "fastapi_init.py.j2", "output": "{project_slug}/__init__.py"},
            {
                "template": "fastapi_api_init.py.j2",
                "output": "{project_slug}/api/__init__.py",
            },
            {
                "template": "fastapi_router.py.j2",
                "output": "{project_slug}/api/router.py",
            },
            {
                "template": "fastapi_config.py.j2",
                "output": "{project_slug}/core/config.py",
            },
            {"template": "test_fastapi.py.j2", "output": "tests/test_main.py"},
            {"template": "gitignore.j2", "output": ".gitignore"},
            {"template": "requirements.txt.j2", "output": "requirements.txt"},
        ],
    },
    "flask": {
        "name": "Flask 웹 앱",
        "description": "Flask 기반 웹 애플리케이션",
        "directories": [
            "{project_slug}",
            "{project_slug}/templates",
            "{project_slug}/static",
            "tests",
            "docs",
        ],
        "files": [
            {"template": "pyproject.toml.j2", "output": "pyproject.toml"},
            {"template": "README.md.j2", "output": "README.md"},
            {"template": "flask_app.py.j2", "output": "{project_slug}/app.py"},
            {"template": "flask_init.py.j2", "output": "{project_slug}/__init__.py"},
            {"template": "flask_routes.py.j2", "output": "{project_slug}/routes.py"},
            {
                "template": "flask_index.html.j2",
                "output": "{project_slug}/templates/index.html",
            },
            {"template": "test_flask.py.j2", "output": "tests/test_app.py"},
            {"template": "gitignore.j2", "output": ".gitignore"},
            {"template": "requirements.txt.j2", "output": "requirements.txt"},
        ],
    },
    "cli": {
        "name": "CLI 도구",
        "description": "Click 기반 명령줄 인터페이스 도구",
        "directories": [
            "{project_slug}",
            "tests",
            "docs",
        ],
        "files": [
            {"template": "pyproject.toml.j2", "output": "pyproject.toml"},
            {"template": "README.md.j2", "output": "README.md"},
            {"template": "cli_main.py.j2", "output": "{project_slug}/main.py"},
            {"template": "cli_init.py.j2", "output": "{project_slug}/__init__.py"},
            {"template": "cli_commands.py.j2", "output": "{project_slug}/commands.py"},
            {"template": "test_cli.py.j2", "output": "tests/test_cli.py"},
            {"template": "gitignore.j2", "output": ".gitignore"},
            {"template": "requirements.txt.j2", "output": "requirements.txt"},
        ],
    },
    "datascience": {
        "name": "데이터 사이언스",
        "description": "데이터 분석 및 시각화 프로젝트",
        "directories": [
            "data",
            "data/raw",
            "data/processed",
            "notebooks",
            "src",
            "src/{project_slug}",
            "tests",
            "docs",
        ],
        "files": [
            {"template": "pyproject.toml.j2", "output": "pyproject.toml"},
            {"template": "README.md.j2", "output": "README.md"},
            {"template": "ds_init.py.j2", "output": "src/{project_slug}/__init__.py"},
            {
                "template": "ds_data_loader.py.j2",
                "output": "src/{project_slug}/data_loader.py",
            },
            {
                "template": "ds_analysis.py.j2",
                "output": "src/{project_slug}/analysis.py",
            },
            {
                "template": "ds_notebook.ipynb.j2",
                "output": "notebooks/01_exploratory_analysis.ipynb",
            },
            {"template": "test_ds.py.j2", "output": "tests/test_analysis.py"},
            {"template": "gitignore.j2", "output": ".gitignore"},
            {"template": "requirements.txt.j2", "output": "requirements.txt"},
        ],
    },
    "ml": {
        "name": "머신러닝",
        "description": "머신러닝 모델 개발 프로젝트",
        "directories": [
            "data",
            "data/raw",
            "data/processed",
            "models",
            "notebooks",
            "src",
            "src/{project_slug}",
            "tests",
            "docs",
        ],
        "files": [
            {"template": "pyproject.toml.j2", "output": "pyproject.toml"},
            {"template": "README.md.j2", "output": "README.md"},
            {"template": "ml_init.py.j2", "output": "src/{project_slug}/__init__.py"},
            {"template": "ml_model.py.j2", "output": "src/{project_slug}/model.py"},
            {"template": "ml_train.py.j2", "output": "src/{project_slug}/train.py"},
            {"template": "ml_predict.py.j2", "output": "src/{project_slug}/predict.py"},
            {
                "template": "ml_notebook.ipynb.j2",
                "output": "notebooks/01_model_training.ipynb",
            },
            {"template": "test_ml.py.j2", "output": "tests/test_model.py"},
            {"template": "gitignore.j2", "output": ".gitignore"},
            {"template": "requirements.txt.j2", "output": "requirements.txt"},
        ],
    },
}


def get_available_templates() -> List[str]:
    """
    사용 가능한 템플릿 목록을 반환합니다.

    Returns:
        List[str]: 템플릿 이름 목록
    """
    return list(TEMPLATE_CONFIGS.keys())


def get_template_config(template_name: str) -> Dict[str, Any]:
    """
    특정 템플릿의 설정을 반환합니다.

    Args:
        template_name: 템플릿 이름

    Returns:
        Dict[str, Any]: 템플릿 설정

    Raises:
        KeyError: 존재하지 않는 템플릿
    """
    if template_name not in TEMPLATE_CONFIGS:
        raise KeyError(f"Template '{template_name}' not found")

    return TEMPLATE_CONFIGS[template_name]


def get_template_info(template_name: str) -> Dict[str, str]:
    """
    템플릿의 기본 정보를 반환합니다.

    Args:
        template_name: 템플릿 이름

    Returns:
        Dict[str, str]: 템플릿 정보 (name, description)
    """
    config = get_template_config(template_name)
    return {"name": config["name"], "description": config["description"]}


def list_templates_info() -> Dict[str, Dict[str, str]]:
    """
    모든 템플릿의 정보를 반환합니다.

    Returns:
        Dict[str, Dict[str, str]]: 템플릿별 정보
    """
    return {template_name: get_template_info(template_name) for template_name in get_available_templates()}
