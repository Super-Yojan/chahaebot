import sqlite3

class Database:

    def __init__(self):
        self.con = sqlite3.connect('simple.db')

        self.cur = self.con.cursor()


    def create_table(self):
        self.cur.execute('''CREATE TABLE homework
               (name text, date TIMESTAMP, notified int default 0)''')
        self.con.commit()

    def add_homework(self, homework):
        self.cur.execute("insert into homework values (?, ?,?)", (homework["name"],homework["date"], 0 ))
        self.con.commit()

    def get_homeworks(self, ):
        self.cur.execute("select * from homework")
        homeworks = self.cur.fetchall()
        return homeworks

    def delete_homework(self, homework):
        self.cur.execute("delete from homework where name = ?", (homework["name"], ))
        self.con.commit()
    
    def update_notify(self, name):
        self.cur.execute("update homework set notified=1 where name=?", (name,))
        self.con.commit()


    def __del__(self):
        self.con.close()
        self.con.close()


if __name__ == '__main__':
    data = Database()
    data.create_table()
    
