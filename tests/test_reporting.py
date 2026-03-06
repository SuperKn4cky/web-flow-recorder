import json

from web_flow_recorder.reporting import ScenarioResult, build_report, write_report


def test_write_report(tmp_path):
    report = build_report([
        ScenarioResult("scenario", True, None, None),
    ])
    path = write_report(report, tmp_path)

    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["results"][0]["scenario_name"] == "scenario"
    assert payload["results"][0]["success"] is True
