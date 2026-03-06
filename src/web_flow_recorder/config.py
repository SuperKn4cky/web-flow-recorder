from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppConfig:
    base_url: str
    signup_path: str
    browser: str
    headless: bool
    timeout_seconds: int
    output_dir: Path


TRUE_VALUES = {"1", "true", "yes", "y", "on"}


def _to_bool(value: str, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in TRUE_VALUES


def load_config() -> AppConfig:
    return AppConfig(
        base_url=os.getenv("WFR_BASE_URL", "http://localhost:3000"),
        signup_path=os.getenv("WFR_SIGNUP_PATH", "/signup"),
        browser=os.getenv("WFR_BROWSER", "chrome").strip().lower(),
        headless=_to_bool(os.getenv("WFR_HEADLESS"), default=True),
        timeout_seconds=int(os.getenv("WFR_TIMEOUT_SECONDS", "20")),
        output_dir=Path(os.getenv("WFR_OUTPUT_DIR", "artifacts")),
    )
