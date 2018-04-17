import pytest
from Slevanda_python_training.Fixture.application import Application


@pytest.fixture(scope="session", autouse=True)
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture