from Objects.account import *
from Security.account import *

class UserDao:
    def to_db(self, user, conn, cur):
        command = f"""INSERT INTO my_user VALUES ({user.to_str()})"""
        cur.execute(command)
        conn.commit()

    def check(self, username, password, cur):
        command = f"""SELECT * FROM my_user WHERE my_username='{username}'"""
        cur.execute(command)
        records = cur.fetchall()
        if len(records) != 1:
            return False
        else:
            record = records[0]
            username = record[1]
            hash = record[2]
            salt = record[3]
            check = verify_password(password, salt, hash)

            return check

    def check_exist(self, username, cur):
        command = f"""SELECT my_username FROM my_user WHERE my_username='{username}'"""
        cur.execute(command)
        records = cur.fetchall()

        return len(records) > 0;

    def get_user_id(self, username, cur):
        command = f"""SELECT id FROM my_user WHERE my_username = '{username}'"""
        cur.execute(command)
        records = cur.fetchall()

        return records[0][0]