import pytest


@pytest.mark.usefixtures("setup")
class TestFixture:

    def test_fixtureDemo1(self):
        print("I will be executing the steps in fixtureDemo method1")

    def test_fixtureDemo2(self):
        print("I will be executing the steps in fixtureDemo method2")

    def test_fixtureDemo3(self):
        print("I will be executing the steps in fixtureDemo method3")