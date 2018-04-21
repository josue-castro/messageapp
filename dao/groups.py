import psycopg2
from config.herokudbconfig import pg_config

from config.dbconfig import pg_config

class GroupsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'],
                                                                            pg_config['user'],
                                                                            pg_config['password'],
                                                                            pg_config['port'],
                                                                            pg_config['host'])

        self.conn = psycopg2.connect(connection_url)

        #     gid,  gName,     admin
        G1 = [101, 'Grupo DB', 120]
        G2 = [122, 'Algarete Chat', 99]
        G3 = [3, 'Chat Group', 124]

        self.groups = []
        self.groups.append(G1)
        self.groups.append(G2)
        self.groups.append(G3)

    def getAllGroups(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM groupchat;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupById(self, gid):
        cursor = self.conn.cursor()
        query = "SELECT * FROM GroupChat WHERE gid = %s;"
        cursor.execute(query, gid)
        result = cursor.fetchone()
        return result

    def getGroupByGroupName(self, gName):
        cursor = self.conn.cursor()
        query = "SELECT * FROM GroupChat WHERE gName = %s;"
        cursor.execute(query, gName)
        result = []
        for row in cursor:
            result.append(row)

        return result