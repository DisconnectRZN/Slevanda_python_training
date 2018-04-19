# -*- coding: utf-8 -*-
from Slevanda_python_training.Model.group import Group

def test_new_group_address_book(app):
    app.group.create(Group(name="Group Name", header="Group header", footer="Group footer"))
    app.session.logout()

def test_empty_group_address_book(app):
    app.group.create(Group(name="", header="", footer=""))