import pytest


@pytest.mark.smoke
def test_program1():
    msg = "Hello"
    assert msg == "Hi", "Test fails as strings do  not match"
