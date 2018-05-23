from config.herokudbconfig import pg_config
import psycopg2


class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'],
                                                                            pg_config['user'],
                                                                            pg_config['password'],
                                                                            pg_config['port'],
                                                                            pg_config['host'])

        self.conn = psycopg2._connect(connection_url)

    def getUserIdLogin(self, username, password):
        cursor = self.conn.cursor()
        query = "SELECT pid, firstname, lastname, username, phone, email FROM person " \
                "WHERE username = %s AND password = crypt(%s, password);"
        cursor.execute(query, (username, password,))
        result = cursor.fetchone()
        return result

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "SELECT username FROM person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, pid):
        cursor = self.conn.cursor()
        query = "SELECT pid, firstname, lastname, username, phone, email FROM person WHERE pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def getUserByPhone(self, phone):
        cursor = self.conn.cursor()
        query = "SELECT pid, firstname, lastname, username, phone, email FROM person WHERE phone = %s;"
        cursor.execute(query, (phone,))
        result = cursor.fetchone()
        return result

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "SELECT pid, firstname, lastname, username, phone, email FROM person WHERE email = %s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = "SELECT pid, firstname, lastname, username, phone, email FROM person WHERE username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def getUserSearchByName(self, firstName, lastName):
        cursor = self.conn.cursor()
        query = "SELECT pid, firstname, lastname, username, phone, email " \
                "FROM person WHERE lower(firstname) = lower(%s) AND lower(lastname) = lower(%s);"
        cursor.execute(query, (firstName, lastName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserGroups(self, pid):
        """Gets groups where User with pid = pid is a member,
        not necessarily admin"""
        cursor = self.conn.cursor()
        query = "SELECT gid, gname, members.pid FROM members INNER JOIN groupchat USING (gid) WHERE members.pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserContacts(self, pid):
        cursor = self.conn.cursor()
        query = "SELECT firstname, lastname, username, phone, email " \
                "FROM contacts c INNER JOIN person p ON c.contact_id = p.pid WHERE c.pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserContactsByName(self, pid, firstName, lastName):
        cursor = self.conn.cursor()
        query = "SELECT firstname, lastname, username, phone, email " \
                "FROM contacts c INNER JOIN person p ON c.contact_id = p.pid " \
                "WHERE c.pid = %s AND lower(p.firstname) = lower(%s) AND lower(p.lastname) = lower(%s);"
        cursor.execute(query, (pid, firstName, lastName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, firstName, lastName, username, phone, email, password):
        cursor = self.conn.cursor()
        query = "INSERT INTO person(firstName, lastName, username, phone, email, password) " \
                "VALUES (%s, %s, %s, %s, %s, crypt(%s, gen_salt('md5'))) RETURNING pid;"
        cursor.execute(query, (firstName, lastName, username, phone, email, password,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def delete(self, pid):
        cursor = self.conn.cursor()
        query = "DELETE FROM person WHERE pid = %s;"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return pid

    def update(self, pid, firtName, lastName, username, phone, email, password):
        cursor = self.conn.cursor()
        query = "UPDATE person SET firstName = %s, lastName = %s, " \
                "username = %s, phone = %s, email = %s, password = crypt(%s, gen_salt('md5')) " \
                "WHERE pid = %s;"
        cursor.execute(query, (firtName, lastName, username, phone, email, password, pid))
        self.conn.commit()
        return pid
