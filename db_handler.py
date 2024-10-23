from config_loader import get_db_config
from db_connection.mysql_connection import MySQLConnection


def get_database_connection():
    db_config = get_db_config()
    connection = MySQLConnection(host=db_config.get('host'),
                                 port=db_config.get('port'),
                                 user=db_config.get('user'),
                                 password=db_config.get('password'),
                                 database=db_config.get('database'))
    return connection
