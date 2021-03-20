import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("This line will execute after the steps in fixtureDemo method")

@pytest.fixture()
def dataLoad():
    print("Profile data required for test cases.")
    return ["Yashaswi", "Thannir", "yashaswithannir.com"]

@pytest.fixture(params=[("chrome", "yashaswi", "thannir"), ("firefox", "thannir"), ("IE", "website")])
def crossBrowser(request):
    return request.param