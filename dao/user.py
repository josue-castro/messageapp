from config.herokudbconfig import pg_config
import psycopg2
class UserDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'],
                                                                            pg_config['user'],
                                                                            pg_config['password'],
                                                                            pg_config['host'],
                                                                            pg_config['port'])
        self.conn = psycopg2.connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from person"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
