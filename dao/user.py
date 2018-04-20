from config.herokudbconfig import pg_config
import psycopg2
import urllib.parse as urlparse
import os



class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'],
                                                                            pg_config['user'],
                                                                            pg_config['password'],
                                                                            pg_config['port'],
                                                                            pg_config['host'])

        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
