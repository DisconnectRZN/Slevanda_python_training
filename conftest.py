import pytest
from Slevanda_python_training.Fixture.application import Application


@pytest.fixture(scope="session", autouse=True)
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture