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
        # member gid, pid
        # M1 = [101, 120]
        # M2 = [101, 117]
        # M3 = [101, 131]
        #
        # M4 = [122, 99]
        # M5 = [122, 76]
        # M6 = [122, 81]
        #
        # self.members = []
        # self.members.append(M1)
        # self.members.append(M2)
        # self.members.append(M3)
        # self.members.append(M4)
        # self.members.append(M5)
        # self.members.append(M6)

    def getMembersINFO(self, gid):
        cursor = self.conn.cursor()
        query = "SELECT username FROM members NATURAL INNER JOIN person WHERE gid = %s"
        result = []
        cursor.execute(query, (gid,))
        for row in cursor:
            result.append(row)
        return result

    def getMember(self, gid, pid):
        result = []
        for member in self.members:
            if gid == member[0] & pid == member[1]:
                result.append(member)
        return result

    def addMember(self, gid, pid):
        member = [gid, pid]
        self.members.append(member)
