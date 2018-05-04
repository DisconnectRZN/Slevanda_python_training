from Slevanda_python_training.Model.contact import Contact

def test_del_contact(app):
    if app.contact.count_contact(app) == 0:
        app.contact.create_new_contact(
            Contact(firstname="First name", middle="Middle name", lastname="Last name", nick="Nickname",
                    title="Title", company="Company", address="Address", homephone="Home telephone",
                    mobilephone="Mobile telephone", workphone="Work telephone",
                    fax_telephone="Fax telephone", email_1="Email 1", email_2="Email 2",
                    email_3="Email 3", home_page="Homepage", bday="1", bmonth="January", byear="1980",
                    aday="18", amonth="July", ayear="1998", address_2="Address",
                    secondaryphone="Home address", notes="Notes"))
    app.contact.delete_first_contact(app)
