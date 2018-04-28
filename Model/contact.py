from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middle=None, lastname=None, nick=None, title=None, company=None, address=None,
                 homephone=None, mobilephone=None, workphone=None, fax_telephone=None,
                 email_1=None, email_2=None, email_3=None, home_page=None, bday=None, bmonth=None,
                 byear=None, aday=None, amonth=None, ayear=None, address_2=None, secondaryphone=None,
                 notes=None, id=None):
        self.firstname = firstname
        self.middle = middle
        self.lastname = lastname
        self.nick = nick
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax_telephone = fax_telephone
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.home_page = home_page
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address_2 = address_2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
                and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize