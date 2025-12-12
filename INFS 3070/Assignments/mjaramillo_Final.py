"""Final assignment for INFS 3070 by mjaramillo
1. When launched your application should connect to the class database.
2. When launched your code should check to see if the appropriate database tables exist.
    If they do, the app should proceed. If they do not, your application should create the tables.
3. Your application must have a user interface with the appropriate elements.
4. When you enter information in the input fields and select "Save Sale" the field should
    clear the values and insert the records into the appropriate database tables and fields.
5. When you select "Show Sales Graph" a bar graph should appear in the application window that
    displays the total sales (revenue) for each product that has been entered.
6. Once you have completed your application, clear all records in your database tables
    and use your application to add the appropriate records.
"""

import mysql.connector as mariadb
from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plt


def get_conn_params():  # connection module 
    return {
        "host": "128.198.162.191",
        "user": "finalUser",
        "password": "itsover!",
        "database": "finaldb"
    }

params = get_conn_params()  # create varaible for get_conn_params module

engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}".format(**params))  # construct SQLAlchemy connection URL


if __name__=="__main__":
    get_conn_params()
