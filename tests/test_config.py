from web_flow_recorder.config import _to_bool


def test_to_bool_true_values():
    assert _to_bool("true", default=False) is True
    assert _to_bool("YES", default=False) is True


def test_to_bool_false_and_default():
    assert _to_bool("no", default=True) is False
    assert _to_bool(None, default=True) is True
