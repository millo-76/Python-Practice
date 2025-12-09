import mysql.connector

def create_conn():
    return mysql.connector.connect(
        host='128.198.162.191',
        user='infscompany',
        password='yeadata',
        database='company'
    )