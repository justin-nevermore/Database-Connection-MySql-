from django.conf import settings
from django.db import connection


cn_open=None
cursor=None

class databaselayer:

    @staticmethod
    def open():
        try:
            global cn_open
            cn_open=connection

        except Exception as e:
            print(e)

    @staticmethod
    def close():
        try:
            cn_open.close()

        except Exception as e:
            print(e)

    @staticmethod
    def registration(fname, lname, loc, age, username, password):
        try:
            databaselayer.open()
            cursor=cn_open.cursor()
            cursor.callproc('a',[fname, lname, loc, age, username, password])
            databaselayer.close()
        except Exception as e:
            print(e)
