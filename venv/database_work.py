import sqlite3


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('vampireDatabase', check_same_thread=False)
    except Error:
        pass

    return conn


def drop_table_users():
    conn = create_connection()
    cur = conn.cursor()
    command = 'drop table users;'
    cur.execute(command)


def create_table_users():
    conn = create_connection()
    cur = conn.cursor()
    command = 'create table if not exists users (id int, name varchar(255), blood int, level int, passed varchar(255));'
    try:
        cur.execute(command)
    except:
        print('table already created')


def insert_user(user_id, name, blood, level, passed):
    conn = create_connection()
    cur = conn.cursor()
    command = "insert into users values ('{}', '{}', '{}', '{}', '{}')".format(user_id, name, blood, level, passed)
    cur.execute(command)
    conn.commit()
    conn.close()


def select_user(user_id):
    conn = create_connection()
    cur = conn.cursor()
    command = "select * from users where id = {}".format(user_id)
    result = cur.execute(command).fetchall()
    conn.close()
    return result


def update_user_name(name, user_id):
    conn = create_connection()
    cur = conn.cursor()
    command = "update users set name = '{}' where id = {}".format(name, user_id)
    cur.execute(command)
    conn.commit()
    conn.close()


def update_user_blood(blood, user_id):
    conn = create_connection()
    cur = conn.cursor()
    command = "update users set blood = {} where id = {}".format(blood, user_id)
    cur.execute(command)
    conn.commit()
    conn.close()


def update_user_level(level, user_id):
    conn = create_connection()
    cur = conn.cursor()
    command = "update users set level = {} where id = {}".format(level, user_id)
    cur.execute(command)
    conn.commit()
    conn.close()


def update_user_blood_and_level(blood, level, user_id):
    conn = create_connection()
    cur = conn.cursor()
    command = "update users set blood = {}, level = {} where id = {}".format(blood, level, user_id)
    cur.execute(command)
    conn.commit()
    conn.close()


def update_user(user_id, name, blood, level, passed_levels):
    conn = create_connection()
    cur = conn.cursor()
    command = "update users set name = '{}', blood = {}, level = {}, passed = '{}' where id = {}".format(name,
                                                                                                         blood,
                                                                                                         level,
                                                                                                         passed_levels,
                                                                                                         user_id)
    cur.execute(command)
    conn.commit()
    conn.close()


def reset_user(user_id):
    conn = create_connection()
    cur = conn.cursor()
    level = 0
    blood = 1
    passed = '0'
    command = "update users set level = {}, blood = {}, passed = {} where id = {}".format(level, blood, passed, user_id)
    cur.execute(command)
    conn.commit()
    conn.close()


def update_passed(passed, user_id):
    conn = create_connection()
    cur = conn.cursor()
    command = "update users set passed = {} where id = {}".format(passed, user_id)
    cur.execute(command)
    conn.commit()
    conn.close()
