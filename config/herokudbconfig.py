import urllib.parse as urlparse
import os

url = urlparse.urlparse(os.environ['postgres://ravuipjltyuoel:3b884db910a7ed97661a75d'
                                   '3203b101e7bf41248fb6c8b36d39ff02dc1556fd5@ec2-23-'
                                   '23-180-121.compute-1.amazonaws.com:5432/d4aeehb1r16558'])

pg_config = {
    'dbname': url.path[1:],
    'user': url.username,
    'password': url.password,
    'host': url.hostname,
    'port': url.port
}
