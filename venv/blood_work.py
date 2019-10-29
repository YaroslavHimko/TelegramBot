import database_work


def user_lose_blood(blood, user_id):
    blood = blood - 1
    database_work.update_user_blood(blood, user_id)
    return blood


def user_increase_blood(blood, user_id):
    blood = blood + 1
    database_work.update_user_blood(blood, user_id)
    return blood


def get_user_blood(user_id):
    blood = database_work.select_user(user_id)[0][2]
    return blood


def show_bats(blood):
    bat = '🦇'
    result = ''
    i = 0
    while i < blood:
        i = i + 1
        result += bat
    return result
