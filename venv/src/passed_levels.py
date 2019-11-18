from src import level
from resources import questions
from resources import answers
from resources import photos


class Passed_levels:
    def __init__(self, number, is_passed, level):
        self.number = number
        self.is_passed = is_passed
        self.level = level

    @staticmethod
    def create_new_list():
        level_one = Passed_levels(1, False, level.Level(questions.one, answers.one, photos.one))
        level_two = Passed_levels(2, False, level.Level(questions.two, answers.two, photos.two))
        level_three = Passed_levels(3, False, level.Level(questions.three, answers.three, photos.three))
        level_four = Passed_levels(4, False, level.Level(questions.four, answers.four, photos.four))
        level_five = Passed_levels(5, False, level.Level(questions.five, answers.five, photos.five))
        level_six = Passed_levels(6, False, level.Level(questions.six, answers.six, photos.six))
        level_seven = Passed_levels(7, False, level.Level(questions.seven, answers.seven, photos.seven))
        level_eight = Passed_levels(8, False, level.Level(questions.eight, answers.eight, photos.eight))
        level_nine = Passed_levels(9, False, level.Level(questions.nine, answers.nine, photos.nine))
        level_ten = Passed_levels(10, False, level.Level(questions.ten, answers.ten, photos.ten))

        levels_list = [
            level_one,
            level_two,
            level_three,
            level_four,
            level_five,
            level_six,
            level_seven,
            level_eight,
            level_nine,
            level_ten
        ]
        return levels_list



