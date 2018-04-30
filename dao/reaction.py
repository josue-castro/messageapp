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

    def insertLike(self, mid, pid):
        """Insert when someone liked a message"""
        cursor = self.conn.cursor()
        query = "INSERT INTO likes (mid, pid) VALUES (%s, %s) " \
                "RETURNING pid;"
        cursor.execute(query, (mid, pid))
        mid = cursor.fetchone()[0]
        self.conn.commit()
        return mid

    def insertDislike(self, mid, pid):
        """Insert when someone dislikes a message"""
        cursor = self.conn.cursor()
        query = "INSERT INTO dislikes (mid, pid) VALUES (%s, %s)" \
                "RETURNING mid"
        cursor.execute(query, (mid, pid))
        mid = cursor.fetchone()[0]
        self.conn.commit()
        return mid

    def createHashtag(self, tag):
        """Insert a new hashtag into to hashtags table"""
        cursor = self.conn.cursor()
        query = "INSERT INTO hashtag(tag) VALUES (%s)" \
                "RETURNING hashtag"
        cursor.execute(query, (tag,))
        hashtag = cursor.fetchone()[0]
        self.conn.commit()
        return hashtag

    def tag(self, mid, hid):
        """Attaches a message with a contained tag and inserts it
        into tagged table."""
        cursor = self.conn.cursor()
        query = "INSERT INTO tagged (mid, hid) VALUES (%s, %s)" \
                "RETURNING mid"
        cursor.execute(query, (mid, hid,))
        mid = cursor.fetchone()[0]
        self.conn.commit()
        return mid

    def deleteLike(self, mid):
        cursor = self.conn.cursor()
        query = "DELETE FROM likes WHERE mid = %s;"
        cursor.execute(query, (mid,))
        self.conn.commit()
        return mid

    def deleteDislike(self, mid):
        cursor = self.conn.cursor()
        query = "DELETE FROM dislikes WHERE mid = %s;"
        cursor.execute(query, (mid,))
        self.conn.commit()
        return mid

    def deleteTag(self, mid):
        cursor = self.conn.cursor()
        query = "DELETE FROM tagged WHERE mid = %s;"
        cursor.execute(query, (mid,))
        self.conn.commit()
        return mid

    def deleteHashtag(self, hid):
        cursor = self.conn.cursor()
        query = "DELETE FROM hashtag WHERE hid = %s;"
        cursor.execute(query, (hid,))
        self.conn.commit()
        return hid
