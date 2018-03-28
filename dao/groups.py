from config.dbconfig import pg_config
import psycopg2


class GroupsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllGroups(self):
        cursor = self.conn.cursor()
        query = "select * from GroupChat;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupById(self, gid):
        cursor = self.conn.cursor()
        query = "select * from GroupChat where gid = %s;"
        cursor.execute(query, (gid,))
        result = cursor.fetchone()
        return result

    def getPartsByGroupName(self, gName):
        cursor = self.conn.cursor()
        query = "select * from GroupChat where gName = %s;"
        cursor.execute(query, (gName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPartsByAdmin(self, admin):
        cursor = self.conn.cursor()
        query = "select * from GroupChat where admin = %d;"
        cursor.execute(query, (admin,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPartsByGroupNameAndAdmin(self, color, material):
        cursor = self.conn.cursor()
        query = "select * from GroupChat where gName = %s and admin = %d;"
        cursor.execute(query, (material,color))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, gid, gName, admin):
        cursor = self.conn.cursor()
        query = "insert into GroupChat(gid, gName, admin) values (%s, %s, %d) returning pid;"
        cursor.execute(query, (gid, gName, admin))
        gid = cursor.fetchone()[0]
        self.conn.commit()
        return gid

    def delete(self, gid):
        cursor = self.conn.cursor()
        query = "delete from GroupChat where gid = %s;"
        cursor.execute(query, (gid,))
        self.conn.commit()
        return gid

    def update(self, gid, gName, admin):
        cursor = self.conn.cursor()
        query = "update GroupChat set gName = %s, admin = %s, pmaterial = %s, pprice = %s where gid = %s;"
        cursor.execute(query, (gid, gName, admin))
        self.conn.commit()
        return gid

