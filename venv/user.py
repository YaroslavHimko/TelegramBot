import level
import random
import json_worker
import passed_levels

class User:
    def __init__(self, user_id, name, blood, level, passed_levels):
        self.user_id = user_id
        self.name = name
        self.blood = blood
        self.level = level
        self.passed_levels = passed_levels


    def is_finished(self):
        for i in range(len(self.passed_levels)):
            if self.passed_levels[i].is_passed is True:
                continue
            else:
                return False
        return True

    def get_new_level(self):
        self.passed_levels[self.level].is_passed = True
        self.blood = self.blood + 1
        json_worker.user_json_writer(self)
        self.generate_next_level()

    def generate_next_level(self):
        for i in range(len(self.passed_levels)):
            if self.passed_levels[i].is_passed is True:
                continue
            else:
                self.level = i
                return self.passed_levels[i].level

def create_user(user_id, user_name):
    return User(user_id=user_id, name=user_name, blood=1, level=0, passed_levels=passed_levels.levels_list)

def get_user(user_id, user_name):
    try:
        user = json_worker.user_json_reader(user_id)
        print("Reading user {}".format(user_id))
    except:
        user = json_worker.user_json_writer(create_user(user_id, user_name))
        print("Writing user {}".format(user_id))
        user = json_worker.user_json_reader(user_id)
        print("Reading user {}".format(user_id))
    return user