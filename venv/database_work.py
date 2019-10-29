import sqlite3


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('testdatabase', check_same_thread=False)
    except Error as e:
        print(e)

    return conn


def drop_table_users():
    conn = create_connection()
    cur = conn.cursor()
    command = 'drop table users;'
    cur.execute(command)


def create_table_users():
    conn = create_connection()
    cur = conn.cursor()
    command = 'create table users (id int, name varchar(255), blood int, level int, passed varchar(255));'
    try:
        cur.execute(command)
    except:
        print('table already created')


def insert_user(id, name, blood, level, passed):
    conn = create_connection()
    cur = conn.cursor()
    command = "insert into users values ('{}', '{}', '{}', '{}', '{}')".format(id, name, blood, level, passed)
    cur.execute(command)
    conn.commit()
    conn.close()


def select_user(id):
    conn = create_connection()
    cur = conn.cursor()
    command = "select * from users where id = {}".format(id)
    result = cur.execute(command).fetchall()
    conn.close()
    return result


def update_user_name(name, id):
    conn = create_connection()
    cur = conn.cursor()
    command = "update users set name = '{}' where id = {}".format(name, id)
    cur.execute(command)
    conn.commit()
    conn.close()


def update_user_blood(blood, id):
    conn = create_connection()
    cur = conn.cursor()
    command = "update users set blood = {} where id = {}".format(blood, id)
    cur.execute(command)
    conn.commit()
    conn.close()


def update_user_level(level, id):
    conn = create_connection()
    cur = conn.cursor()
    command = "update users set level = {} where id = {}".format(level, id)
    cur.execute(command)
    conn.commit()
    conn.close()


def update_user_blood_and_level(blood, level, id):
    conn = create_connection()
    cur = conn.cursor()
    command = "update users set blood = {}, level = {} where id = {}".format(blood, level, id)
    cur.execute(command)
    conn.commit()
    conn.close()


def update_user(id, name, blood, level, passed_levels):
    conn = create_connection()
    cur = conn.cursor()
    command = "update users set name = '{}', blood = {}, level = {}, passed = '{}' where id = {}".format(name,
                                                                                                         blood,
                                                                                                         level,
                                                                                                         passed_levels,
                                                                                                         id)
    cur.execute(command)
    conn.commit()
    conn.close()


def reset_user(id):
    conn = create_connection()
    cur = conn.cursor()
    level = 0
    blood = 1
    passed = '0'
    command = "update users set level = {}, blood = {}, passed = {} where id = {}".format(level, blood, passed, id)
    cur.execute(command)
    conn.commit()
    conn.close()


def update_passed(passed, id):
    conn = create_connection()
    cur = conn.cursor()
    command = "update users set passed = {} where id = {}".format(passed, id)
    cur.execute(command)
    conn.commit()
    conn.close()


def update_user_blood(blood, id):
    conn = create_connection()
    cur = conn.cursor()
    command = "update users set blood = {} where id = {}".format(blood, id)
    cur.execute(command)
    conn.commit()
    conn.close()
