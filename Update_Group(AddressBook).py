# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_new_group_address_book(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Group Name", header="Group header", footer="Group footer"))
    app.logout()

def test_empty_group_address_book(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()