from config.dbconfig import pg_config
import psycopg2


class GroupsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllGroups(self):
        result = []

        G1 = {}
        G1['gid'] = 1
        G1['gName'] = 'MessageGroup'
        G1['admin'] = 85

        G2 = {}
        G2['gid'] = 2
        G2['gName'] = 'Grupo DB'
        G2['admin'] = 123

        G3 = {}
        G3['gid'] = 3
        G3['gName'] = 'Algarete Chat'
        G3['admin'] = 1

        result.append(G1, G2, G3)

        return result

        # cursor = self.conn.cursor()
        # query = "select * from GroupChat;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result

    def getGroupById(self, gid):
        cursor = self.conn.cursor()
        query = "select * from GroupChat where gid = %s;"
        cursor.execute(query, gid)
        result = cursor.fetchone()
        return result

    def getPartsByGroupName(self, gName):
        cursor = self.conn.cursor()
        query = "select * from GroupChat where gName = %s;"
        cursor.execute(query, gName)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPartsByAdmin(self, admin):
        cursor = self.conn.cursor()
        query = "select * from GroupChat where admin = %d;"
        cursor.execute(query, admin)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatsByGroupNameAndAdmin(self, color, material):
        cursor = self.conn.cursor()
        query = "select * from GroupChat where gName = %s and admin = %d;"
        cursor.execute(query, (gName, admin))
        result = []
        for row in cursor:
            result.append(row)
        return result


    # def insert(self, gid, gName, admin):
    #     cursor = self.conn.cursor()
    #     query = "insert into GroupChat(gid, gName, admin) values (%s, %s, %d) returning gid;"
    #     cursor.execute(query, (gid, gName, admin))
    #     gid = cursor.fetchone()[0]
    #     self.conn.commit()
    #     return gid
    #
    # def delete(self, gid):
    #     cursor = self.conn.cursor()
    #     query = "delete from GroupChat where gid = %s;"
    #     cursor.execute(query, (gid,))
    #     self.conn.commit()
    #     return gid
    #
    # def update(self, gid, gName, admin):
    #     cursor = self.conn.cursor()
    #     query = "update GroupChat set gName = %s, admin = %s, pmaterial = %s, pprice = %s where gid = %s;"
    #     cursor.execute(query, (gid, gName, admin))
    #     self.conn.commit()
    #     return gid

