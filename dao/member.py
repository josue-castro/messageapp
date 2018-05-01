import psycopg2
from config.herokudbconfig import pg_config


class MembersDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'],
                                                                            pg_config['user'],
                                                                            pg_config['password'],
                                                                            pg_config['port'],
                                                                            pg_config['host'])

        self.conn = psycopg2.connect(connection_url)

    def getMembersINFO(self, gid):
        cursor = self.conn.cursor()
        query = "SELECT username, firstName, lastName, phone, email " \
                "FROM members NATURAL INNER JOIN person WHERE gid = %s"
        result = []
        cursor.execute(query, (gid,))
        for row in cursor:
            result.append(row)
        return result

    def getMemberById(self, gid, pid):
        cursor = self.conn.cursor()
        query = "SELECT username, firstName, lastName, phone, email " \
                "FROM members NATURAL INNER JOIN person " \
                "WHERE gid = %s AND pid = %s"
        cursor.execute(query, (gid, pid))
        result = cursor.fetchone()
        self.conn.commit()
        return result


    def insertMember(self, gid, pid):
        """Insert method for members table."""
        cursor = self.conn.cursor()
        query = "INSERT INTO members (gid, pid) VALUES (%s, %s) " \
                "RETURNING pid;"
        cursor.execute(query, (gid, pid))
        gid = cursor.fetchone()[0]
        self.conn.commit()
        return gid

    def delete(self, pid):
        cursor = self.conn.cursor()
        query = "DELETE FROM members WHERE pid = %s;"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return pid

