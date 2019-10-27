import database_work
import level

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
        
        
    def increase_user_level(self):
        levels_count = len(level.levels_list)
        if self.level < levels_count - 1:
            self.level = self.level + 1
            self.update_user()
            self.level_object = level.levels_list[self.level]
            print("set level " + self.level_object.question)
        else:
            self.level = level.levels_list[levels_count]