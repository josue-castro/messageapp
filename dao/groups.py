class GroupsDAO:
    def __init__(self):

        #connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
        #                                                    pg_config['user'],
        #                                                    pg_config['passwd'])
        #self.conn = psycopg2._connect(connection_url)

        #     gid,  gName,     admin
        G1 = [101, 'Grupo DB', 120]
        G2 = [122, 'Algarete Chat', 99]
        G3 = [3, 'Chat Group', 124]

        self.groups = []
        self.groups.append(G1)
        self.groups.append(G2)
        self.groups.append(G3)

    def getAllGroups(self):
        return self.groups

        # cursor = self.conn.cursor()
        # query = "select * from GroupChat;"
        # cursor.execute(query)
        # result = []
        # for row in cursor:
        #     result.append(row)
        # return result

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

