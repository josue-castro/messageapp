import psycopg2
from config.herokudbconfig import pg_config


class GroupsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'],
                                                                            pg_config['user'],
                                                                            pg_config['password'],
                                                                            pg_config['port'],
                                                                            pg_config['host'])

        self.conn = psycopg2.connect(connection_url)

    def getAllGroupsINFO(self):
        cursor = self.conn.cursor()
        query = "SELECT gid, gname, pid, username, firstName, lastName " \
                "FROM groupchat NATURAL INNER JOIN person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupByIdINFO(self, gid):
        cursor = self.conn.cursor()
        query = "SELECT gid, gname, pid, username, firstName, lastName " \
                "FROM groupchat NATURAL INNER JOIN person " \
                "WHERE gid = %s;"
        cursor.execute(query, (gid,))
        result = cursor.fetchone()
        return result

    def getGroupByGroupNameINFO(self, gName):
        cursor = self.conn.cursor()
        query = "SELECT gid, gname, pid, username, firstName, lastName " \
                "FROM groupchat NATURAL INNER JOIN person " \
                "WHERE gName = %s;"
        cursor.execute(query, gName)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def getGroupNameById(self, gid):
    #     cursor = self.conn.cursor()
    #     query = "SELECT gname FROM GroupChat WHERE gid = %s;"
    #     cursor.execute(query, gid)
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

    # def getGroupAdminINFO(self, gid):
    #     cursor = self.conn.cursor()
    #     query = "SELECT pid, firstname, lastname, username, phone, email " \
    #             " FROM GroupChat NATURAL INNER JOIN person " \
    #             "WHERE gid = %s;"
    #     cursor.execute(query, (gid,))
    #     result = cursor.fetchone()
    #     return result

    def getAllGroupsAdminByUserINFO(self, pid):
        """get all groups that are administrated by User with pid = pid"""
        cursor = self.conn.cursor()
        query = "SELECT gid, gname " \
                "FROM groupchat NATURAL INNER JOIN person " \
                "WHERE pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupMembersINFO(self, gid):
        cursor = self.conn.cursor()
        query = "SELECT pid, firstname, lastname, username, phone, email " \
                "FROM members NATURAL INNER JOIN person " \
                "WHERE gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertGroup(self, gname, pid):
        cursor = self.conn.cursor()
        query1 = "INSERT INTO groupchat (gname, pid) VALUES (%s, %s) " \
                "RETURNING gid;"
        cursor.execute(query1, (gname, pid,))
        gid = cursor.fetchone()[0]
        self.conn.commit()
        query2 = "INSERT INTO members (gid, pid) VALUES (%s, %s)"
        cursor.execute(query2, (gid, pid,))
        self.conn.commit()
        return gid

    def delete(self, gid):
        """Delete a group from groupchat table."""
        cursor = self.conn.cursor()
        query = "DELETE FROM groupchat WHERE gid = %s;"
        cursor.execute(query, (gid,))
        self.conn.commit()
        return gid

    def update(self, gid, gname, pid):
        """update all values of a specific group in in Groupchat table."""
        cursor = self.conn.cursor()
        query = "UPDATE groupchat SET gname = %s, pid = %s " \
                "WHERE gid = %s;"
        cursor.execute(query, (gid, gname, pid))
        self.conn.commit()
        return gid

    def changeGroupName(self, gid, gname):
        """Update the group's name"""
        cursor = self.conn.cursor()
        query = "UPDATE groupchat SET gname = %s " \
                "WHERE gid = %s;"
        cursor.execute(query, (gid, gname))
        self.conn.commit()
        return gid

    def changeAdmin(self, gid, pid):
        """Change the admin of a group"""
        cursor = self.conn.cursor()
        query = "UPDATE groupchat SET pid = %s " \
                "WHERE gid = %s;"
        cursor.execute(query, (pid, gid))
        self.conn.commit()
        return gid
