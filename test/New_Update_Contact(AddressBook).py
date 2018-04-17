# -*- coding: utf-8 -*-
from Slevanda_python_training.Model.contact import Contact
import time

def test_create_new_contact(app):
    app.session.login(username="admin", password="secret")
    time.sleep(2)
    app.contact.create_new_contact(Contact(first="First name", middle="Middle name", last="Last name", nick="Nickname",
                                    title="Title", company="Company", address="Address", home_telephone="Home telephone",
                                    mobile_telephone="Mobile telephone", work_telephone="Work telephone",
                                    fax_telephone="Fax telephone", email_1="Email 1", email_2="Email 2",
                                    email_3="Email 3", home_page="Homepage", bday="1", bmonth="January", byear="1980",
                                    aday="18", amonth="July", ayear="1998", address_2="Address",
                                    home_address="Home address", notes="Notes"))
    app.session.logout()


