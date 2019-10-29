import database_work
import level
import random


class User:
    def __init__(self, id, name, blood, level, passed_levels, level_object):
        self.id = id
        self.name = name
        self.blood = blood
        self.level = level
        self.passed_levels = passed_levels
        self.level_object = level_object

    def insert_user(self):
        database_work.insert_user(self.id, self.name, self.blood, self.level, self.passed_levels)

    def update_user(self):
        database_work.update_user(self.id, self.name, self.blood, self.level, self.passed_levels)

    @staticmethod
    def get_user(user_id):
        database_user = database_work.select_user(user_id)[0]
        user_id = database_user[0]
        user_name = database_user[1]
        user_blood = database_user[2]
        user_level = database_user[3]
        user_passed_levels = database_user[4]
        return User(user_id, user_name, user_blood, user_level, user_passed_levels, level.get_level_object(user_level))

    def set_random_level(self):
        if str(self.level) in self.passed_levels:
            self.level = random.randint(1, len(level.levels_dict) - 1)
            if self.level <= len(level.levels_dict) - 1:
                self.set_random_level()

    def is_finished(self):
        if len(self.passed_levels) < 11:
            return False
        return True

    def increase_user_level(self):
        if not self.is_finished():
            self.blood = self.blood + 1
            self.passed_levels = self.passed_levels + str(self.level)
            self.update_user()
            self.set_random_level()
            self.level_object = level.levels_dict.get(self.level)
        else:
            self.level_object = level.levels_dict.get(11)
