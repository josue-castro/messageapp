from config.herokudbconfig import pg_config
import psycopg2


class DashboardDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'],
                                                                            pg_config['user'],
                                                                            pg_config['password'],
                                                                            pg_config['port'],
                                                                            pg_config['host'])

        self.conn = psycopg2._connect(connection_url)

    def messagesPerDay(self):
        cursor = self.conn.cursor()
        query = "SELECT date(date), count(*) FROM messages GROUP BY date(date) ORDER BY date(date) LIMIT 7;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def topTenHashtags(self):
        cursor = self.conn.cursor()
        query = "SELECT tag, count(*) AS count FROM tagged NATURAL INNER JOIN hashtag " \
                "GROUP BY tag ORDER BY count LIMIT 10"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def repliesPerDay(self):
        cursor = self.conn.cursor()
        query = "SELECT date(messages.date), count(*) " \
                "FROM replies INNER JOIN messages ON replies.reply_id = messages.mid " \
                "GROUP BY date(messages.date) LIMIT 7;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def likesPerDay(self):
        cursor = self.conn.cursor()
        query = "SELECT date(date), count(*) FROM likes GROUP BY date(date) ORDER BY date;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def dislikesPerDay(self):
        cursor = self.conn.cursor()
        query = "SELECT date(date), count(*) FROM dislikes GROUP BY date(date) ORDER BY date;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def topActiveUsers(self):
        cursor = self.conn.cursor()
        query = "SELECT username, count(*) as count " \
                "FROM messages NATURAL INNER JOIN person " \
                "WHERE date(date) = date(now()) " \
                "GROUP BY username ORDER BY count DESC LIMIT 10;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result