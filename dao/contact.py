class ContactDAO:
    def __init__(self):
        #main user id, contact name, phone, email, cid
        C1 = [120, 'Joseph', '7873334455', '', 131]
        C2 = [120, 'Pamela', '', 'pamela.18@gmail.com', 171]
        C3 = [120, 'Fabian', '7871012233', '', 145]
        C4 = [120, 'Pedro', '','pedrito22@hotmail.com', 231]
        C5 = [171, 'Joe', '7873334455', '', 131]
        C6 = [171, 'Emmanuel', '7879890010', 'emma2018@gmail.com', 120]
        C7 = [171, 'Veronica', '9391248765', '', 169]
        C8 = [131, 'Emma', '', 'emma2018@gmail.com', 120]
        C9 = [131, 'Pam', '', 'pamela.18@gmail.com', 171]

        self.contacts = []
        self.contacts.append(C1)
        self.contacts.append(C2)
        self.contacts.append(C3)
        self.contacts.append(C4)
        self.contacts.append(C5)
        self.contacts.append(C6)
        self.contacts.append(C7)
        self.contacts.append(C8)
        self.contacts.append(C9)

    def getMyContacts(self, pid):
        result = []
        for c in self.contacts:
            if c[0] == pid:
                result.append(c)
        return result

    def getContactByName(self, pid, name):
        result = []

        for c in self.contacts:
            if c[0] == pid and str.lower(c[1]) == str.lower(name):
                result.append(c)
        return result
