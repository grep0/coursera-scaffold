from hello import add


def test_add():
    assert add(1, 2) == 3

def test_add2():
    assert add(42, 42) == 84
