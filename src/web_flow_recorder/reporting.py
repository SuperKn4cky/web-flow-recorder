from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass
class ScenarioResult:
    scenario_name: str
    success: bool
    error_message: str | None
    screenshot_path: str | None


@dataclass
class ExecutionReport:
    generated_at: str
    results: list[ScenarioResult]


def build_report(results: list[ScenarioResult]) -> ExecutionReport:
    now = datetime.now(timezone.utc).isoformat()
    return ExecutionReport(generated_at=now, results=results)


def write_report(report: ExecutionReport, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "report.json"

    payload = {
        "generated_at": report.generated_at,
        "results": [asdict(result) for result in report.results],
    }
    report_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return report_path
