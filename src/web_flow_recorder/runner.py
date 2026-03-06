from __future__ import annotations

from pathlib import Path

from web_flow_recorder.config import load_config
from web_flow_recorder.data_factory import build_signup_data
from web_flow_recorder.driver_factory import build_driver
from web_flow_recorder.pages.signup_page import SignupPage
from web_flow_recorder.reporting import ScenarioResult, build_report, write_report


def _screenshot(driver, output_dir: Path, scenario_name: str) -> str | None:
    if driver is None:
        return None

    screenshot_dir = output_dir / "screenshots"
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    shot = screenshot_dir / f"{scenario_name}.png"
    driver.save_screenshot(str(shot))
    return str(shot)


def run_signup_happy_path() -> ScenarioResult:
    config = load_config()
    scenario_name = "signup_happy_path"
    driver = None

    try:
        driver = build_driver(config.browser, config.headless)
        page = SignupPage(driver, config.timeout_seconds)
        url = f"{config.base_url}{config.signup_path}"
        page.visit(url)

        data = build_signup_data()
        page.fill_form(data)
        page.submit()
        page.wait_success()

        return ScenarioResult(scenario_name=scenario_name, success=True, error_message=None, screenshot_path=None)
    except Exception as exc:  # noqa: BLE001
        screenshot_path = _screenshot(driver, config.output_dir, scenario_name)
        return ScenarioResult(
            scenario_name=scenario_name,
            success=False,
            error_message=str(exc),
            screenshot_path=screenshot_path,
        )
    finally:
        if driver is not None:
            driver.quit()


def main() -> int:
    config = load_config()
    result = run_signup_happy_path()
    report = build_report([result])
    report_path = write_report(report, config.output_dir)

    print(f"Report generated: {report_path}")
    if not result.success:
        print(f"Scenario failed: {result.error_message}")
    return 0 if result.success else 1


if __name__ == "__main__":
    raise SystemExit(main())
