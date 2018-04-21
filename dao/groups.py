import psycopg2
import subprocess

from config.dbconfig import pg_config

class GroupsDAO:
    def __init__(self):

        # connection_url = "dbname=%s user=%s password=%s" % (pg_config['postgres'],
        #                                                    pg_config['eggiemuniz'],
        #                                                     pg_config['andres'])

        self.conn = psycopg2.connect(host="localhost", database="postgres", user="eggiemuniz", password="andres")

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
        result = []
        for group in self.groups:
            if gid == group[0]:
                return result.append(group)

        # cursor = self.conn.cursor()
        # query = "select * from GroupChat where gid = %s;"
        # cursor.execute(query, gid)
        # result = cursor.fetchone()

        return result

    def getPartsByGroupName(self, gName):
        result = []
        for group in self.groups:
            if gName == group[1]:
                result.append(group)

        # cursor = self.conn.cursor()
        # query = "select * from GroupChat where gName = %s;"
        # cursor.execute(query, gName)
        # result = []
        # for row in cursor:
        #     result.append(row)

        return result

    def getPartsByAdmin(self, admin):
        result = []
        for group in self.groups:
            if admin == group[1]:
                result.append(group)

        # cursor = self.conn.cursor()
        # query = "select * from GroupChat where admin = %d;"
        # cursor.execute(query, admin)
        # result = []
        # for row in cursor:
        #     result.append(row)

        return result

    def getGroupChatsByGroupNameAndAdmin(self, gName, admin):
        result = []
        for group in self.groups:
            if (gName == group[1]) and (admin == group[2]):
                result.append(group)

        # cursor = self.conn.cursor()
        # query = "select * from GroupChat where gName = %s and admin = %d;"
        # cursor.execute(query, (gName, admin))
        # result = []
        # for row in cursor:
        #     result.append(row)

        return result