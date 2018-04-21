import psycopg2
from config.herokudbconfig import pg_config


class ReactionDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'],
                                                                            pg_config['user'],
                                                                            pg_config['password'],
                                                                            pg_config['port'],
                                                                            pg_config['host'])

        self.conn = psycopg2.connect(connection_url)

    def getTotalReactions(self): #TODO Verify Query
        cursor = self.conn.cursor()
        query = "SELECT count(*) FROM likes NATURAL INNER JOIN messages " \
                "NATURAL INNER JOIN dislikes NATURAL INNER JOIN hashtag;"
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def getMessageLikes(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT count(*) FROM likes WHERE mid = %s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    def getWhoLikedMessage(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT username FROM likes NATURAL INNER JOIN person " \
                "WHERE mid = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getMessageDislikes(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT count(*) FROM dislikes WHERE mid = %s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    def getWhoDisLikedMessage(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT username " \
                "FROM dislikes NATURAL INNER JOIN person " \
                "WHERE mid = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
