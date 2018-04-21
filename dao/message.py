class MessageDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'],
                                                                            pg_config['user'],
                                                                            pg_config['password'],
                                                                            pg_config['port'],
                                                                            pg_config['host'])

        self.conn = psycopg2.connect(connection_url)

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM messages;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupMessages(self, gid):
        cursor = self.conn.cursor()
        query = "SELECT * FROM messages WHERE gid = %s;"
        cursor.execute(query, gid)
        result = cursor.fetchone()
        return result

    def getMessagesBySender(self, gid, pid):
        cursor = self.conn.cursor()
        query = "SELECT * FROM messages WHERE gid = %s AND pid = %s;"
        cursor.execute(query, gid, pid)
        result = cursor.fetchone()
        return result
