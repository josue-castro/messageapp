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

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, pid):
        cursor = self.conn.cursor()
        query = "SELECT * FROM person WHERE pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def getUserByPhone(self, phone):
        cursor = self.conn.cursor()
        query = "SELECT * FROM person WHERE phone = %s;"
        cursor.execute(query, (phone,))
        result = cursor.fetchone()
        return result

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "SELECT * FROM person WHERE email = %s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result

    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = "SELECT * FROM person WHERE username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    def insert(self, firstName, lastName, username, phone, email):
        cursor = self.conn.cursor()
        query = "INSERT INTO person(firstName, lastName, username, phone, email) VALUES (%s, %s, %s, %s, %s) RETURNING pid;"
        cursor.execute(query, (firstName, lastName, username, phone, email,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def delete(self, pid):
        cursor = self.conn.cursor()
        query = "DELETE FROM person WHERE pid = %s;"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return pid

    def update(self, pid, firtName, lastName, username, phone, email):
        cursor = self.conn.cursor()
        query = "UPDATE person set firstName = %s, lastName = %s, username = %s, phone = %s, email = %s WHERE pid = %s;"
        cursor.execute(query, (firtName, lastName, username, phone, email, pid))
        self.conn.commit()
        return pid
