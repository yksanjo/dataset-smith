import importlib


def test_main_exists():
    mod = importlib.import_module("dataset_smith.cli")
    assert hasattr(mod, "main")
