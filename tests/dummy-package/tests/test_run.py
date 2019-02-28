import os
import dummy_package as pkg


def test_run_1():
    path = pkg.run()
    assert path is not None
    base = os.path.basename(path)
    assert base == "uproot-Event.root"
