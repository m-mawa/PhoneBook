from dataclasses import dataclass
from typing import List, Union

import mariadb
import sys


class UserInfo:
    id: int = 0
    Login: str = ""
    Name: str = ""
    Org: str = ""
    Unit: str = ""
    Position: str = ""
    Last: str = ""
    SID: str = ""
    Email: str = ""
    Location: str = ""
    task_create: str = ""
    isui: str = ""
    Location_comment: str = ""
    Comment: str = ""
    Numbers: List = []
    pc_info: List = []
    is_fired: bool = False
    is_vip: bool = False


class DataBase():
    def __init__(self):
        self.connect_to_db()


    def connect_to_db(self):
        try:
            self.conn = mariadb.connect(
                user="user_td_new",
                password="user_td_passnew",
                host="pool-srv.efko.ru",
                port=3306,
                database="telephone_directory"
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

    def get_fios(self) -> List[str]:
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT full_name, account FROM people")
        fios = self.cur.fetchall()
        return fios

    def get_ids_by_fio(self, user_input) -> List[str]:
        self.cur.execute("SELECT id FROM people WHERE full_name LIKE '%'  ?  '%' OR account LIKE '%' ? '%'",
                         (user_input, user_input))
        result = self.cur.fetchall()
        return result

    def get_ids_by_number(self, user_input) -> List[str]:
        self.cur.execute("SELECT id_people FROM phone_list WHERE number LIKE '%'  ?  '%'", (user_input,))
        result = self.cur.fetchall()
        return result

    def get_user_info(self, id) -> Union[UserInfo, None]:
        user_info = UserInfo()

        self.cur.execute("SELECT * FROM people WHERE id=?", (id,))
        records = self.cur.fetchall()
        print(records)
        if len(records) == 0:
            return None
        records = records[0]
        self.cur.execute("SELECT number, type FROM phone_list WHERE id_people=? ", (id,))
        number = self.cur.fetchall()
        self.cur.execute("SELECT comment FROM comments WHERE id_people=?", (id,))
        comment = self.cur.fetchall()
        self.cur.execute("SELECT location FROM comments WHERE id_people=?", (id,))
        location = self.cur.fetchall()
        self.cur.execute("SELECT pc_name, when_changed FROM pc_list WHERE id_people=?", (id,))
        pc_info = self.cur.fetchall()

        user_info.id = id
        user_info.Login = records[3]
        user_info.Name = records[1]
        user_info.Org = records[8]
        user_info.Unit = records[9]
        user_info.Position = records[10]
        user_info.Last = str(records[13])
        user_info.SID = records[6]
        user_info.Email = records[7]
        user_info.Location = records[11]
        user_info.task_create = records[14]
        user_info.isui = records[12]
        user_info.Numbers = number
        user_info.pc_info = pc_info
        if len(location) > 0:
            user_info.Location_comment = location[0][0]
        if len(comment) > 0:
            user_info.Comment = comment[0][0]
        user_info.is_vip = records[5]
        user_info.is_fired = records[15]

        return user_info

    def saveData(self, comment, location, phonenum, id):
        self.cur.execute("UPDATE comments SET comment = ? WHERE id_people = ? ", (comment, id))
        self.cur.execute("UPDATE comments SET location = ? WHERE id_people = ? ", (location, id))
        self.cur.execute("UPDATE phone_list SET number = ? WHERE id_people = ? AND type = 3", (phonenum, id))
        self.conn.commit()

    def get_history(self, user) -> List:
        self.cur.execute("SELECT id FROM users WHERE user=? ", (user,))
        userid = self.cur.fetchall()
        self.cur.execute("SELECT query FROM history WHERE user_id=? ", (userid[0][0],))
        history = self.cur.fetchall()
        return history

    def save_history(self, user, user_input):
        self.cur.execute("SELECT id FROM users WHERE user=? ", (user,))
        userid = self.cur.fetchall()
        self.cur.execute("INSERT INTO history (query, user_id) VALUES (?,?)", (user_input, userid[0][0]))
        self.conn.commit()
