import psycopg2
from config.herokudbconfig import pg_config


class ContactDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'],
                                                                            pg_config['user'],
                                                                            pg_config['password'],
                                                                            pg_config['port'],
                                                                            pg_config['host'])

        self.conn = psycopg2.connect(connection_url)
        # #main user id, contact name, phone, email, cid
        # C1 = [120, 'Joseph', '7873334455', '', 131]
        # C2 = [120, 'Pamela', '', 'pamela.18@gmail.com', 171]
        # C3 = [120, 'Fabian', '7871012233', '', 145]
        # C4 = [120, 'Pedro', '','pedrito22@hotmail.com', 231]
        # C5 = [171, 'Joe', '7873334455', '', 131]
        # C6 = [171, 'Emmanuel', '7879890010', 'emma2018@gmail.com', 120]
        # C7 = [171, 'Veronica', '9391248765', '', 169]
        # C8 = [131, 'Emma', '', 'emma2018@gmail.com', 120]
        # C9 = [131, 'Pam', '', 'pamela.18@gmail.com', 171]
        #
        # self.contacts = []
        # self.contacts.append(C1)
        # self.contacts.append(C2)
        # self.contacts.append(C3)
        # self.contacts.append(C4)
        # self.contacts.append(C5)
        # self.contacts.append(C6)
        # self.contacts.append(C7)
        # self.contacts.append(C8)
        # self.contacts.append(C9)

    def getMyContactsINFO(self, pid): #hay que usar equi join
        cursor = self.conn.cursor()
        # query = "SELECT firstName, lastName, username, phone, email FROM contacts NATURAL INNER JOIN person " \
        #         "WHERE pid = %s"
        query = "SELECT firstname, lastname, username, phone, email " \
                "FROM contacts c INNER JOIN person p ON c.contact_id = p.pid WHERE c.pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getContactByName(self, pid, name): #TODO IMPLEMENT
        result = ["not implemented"]

        return result
