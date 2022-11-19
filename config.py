import mysql.connector as mys
def dbconfig():
    db=mys.connect(host="localhost",user="root",
                    password="1234@")

    cur=db.cursor()
    cur.execute("Create database IF NOT EXISTS pwd_mngr")
    cur.execute("use pwd_mngr")
    cur.execute("""create table IF NOT EXISTS user(username varchar(50),
                 pwd varchar(100) not null,primary key(username))""")
    cur.execute("""create table IF NOT EXISTS pwd(uname varchar(40),
                   site_name varchar(30),password varchar(100) not null,
                   FOREIGN KEY (uname) REFERENCES user(username))""")
    return db

