import questions
import answers
import stickers
import random
import greetings


class Level:
    def __init__(self, question, answer, sticker):
        self.question = question
        self.answer = answer
        self.sticker = sticker

    @staticmethod
    def get_random_wrong_answer():
        wrong_answer = random.choice(answers.wrong_answers)
        return wrong_answer


def get_levels_length():
    return len(levels_list) - 1


def get_level_object(level):
    return levels_list[level]


finished = Level(greetings.grats, greetings.grats, stickers.grats)
level_ten = Level(questions.ten, answers.ten, stickers.ten)
level_nine = Level(questions.nine, answers.nine, stickers.nine)
level_eight = Level(questions.eight, answers.eight, stickers.eight)
level_seven = Level(questions.seven, answers.seven, stickers.seven)
level_six = Level(questions.six, answers.six, stickers.six)
level_five = Level(questions.five, answers.five, stickers.five)
level_four = Level(questions.four, answers.four, stickers.four)
level_three = Level(questions.three, answers.three, stickers.three)
level_two = Level(questions.two, answers.two, stickers.two)
level_one = Level(questions.one, answers.one, stickers.one)

levels_list = [level_one, level_two, level_three, level_four, level_five, level_six, level_seven, level_eight,
               level_nine, level_ten, finished]
