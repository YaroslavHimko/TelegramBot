import level
import random
import json_worker

class User:
    def __init__(self, user_id, name, blood, level, passed_levels):
        self.user_id = user_id
        self.name = name
        self.blood = blood
        self.level = level
        self.passed_levels = passed_levels


    def is_finished(self):
        for i in range(len(self.passed_levels)):
            if self.passed_levels.get(str(i)).is_passed is True:
                continue
            else:
                return False
        return True

    def get_new_level(self):
        self.passed_levels.get(str(self.level)).is_passed = True
        self.blood = self.blood + 1
        json_worker.user_json_writer(self)
        return self.generate_next_level()

    def generate_next_level(self):
        for i in range(len(self.passed_levels)):
            if self.passed_levels.get(str(i)).is_passed is True:
                continue
            else:
                self.level = i
                return self.passed_levels.get(str(i)).level.content

def get_user(user_id):
    return json_worker.user_json_reader(user_id)