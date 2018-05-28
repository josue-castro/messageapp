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

    def checkIsContact(self, pid, contact_id):
        cursor = self.conn.cursor()
        query = "SELECT contact_id FROM contacts NATURAL INNER JOIN person " \
                "WHERE pid = %s AND contact_id = %s;"
        cursor.execute(query, (pid, contact_id))
        result = cursor.fetchone()
        return result

    def addContact(self, pid, contact_id):
        """Insert method for contacts table"""
        cursor = self.conn.cursor()
        query = "INSERT INTO contacts (pid, contact_id) VALUES (%s, %s) " \
                "RETURNING pid;"
        cursor.execute(query, (pid, contact_id))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def delete(self, pid, contact_id):
        cursor = self.conn.cursor()
        query = "DELETE FROM contacts WHERE pid = %s AND contact_id = %s;"
        cursor.execute(query, (pid, contact_id,))
        self.conn.commit()
        return contact_id
