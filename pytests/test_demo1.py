# Any pytest file name should start with test_ or end with _test
# pytest method names should always start with test
# Any code should be wrapped in method only
# to run tests from cmd -> navigate to pytests path and run py.test -v -s
# in py test it cannot have multiple test method names as same. if it exists it will override the previous method
# py.test -k testnamecontains -v -s
# mark (tag) tests and then run with -m
# pytest.mark.xfail - test case will run but pass or fail report is not shown
# fixtures are used as setup and teardown methods for test cases- use conftest file to generalize fixtures
# use pytest.mark.usefixtures("setup") at class level to avoid passing setup as argument for every test case
# when fixture scope is defined to class only it will run once before class is initiated and after all class methods execution is complete
# datadriven and parameterization can be achieved with return statements in tuple format

import pytest


@pytest.mark.smoke
@pytest.mark.skip    # to skip this particular test
def test_program1():
    print("Hey! you")


#def test_program1():
#   print("Good Morning")


def test_program2():
    print("Good Morning")


def test_program3(crossBrowser):
    print(crossBrowser[1])


