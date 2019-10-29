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


def get_random_wrong_answer():
    wrong_answer = random.choice(answers.wrong_answers)
    return wrong_answer


def get_levels_length():
    return len(levels_dict) - 1


def get_level_object(level):
    return levels_dict.get(level)


levels_dict = {
    1: Level(questions.one, answers.one, stickers.one),
    2: Level(questions.two, answers.two, stickers.two),
    3: Level(questions.three, answers.three, stickers.three),
    4: Level(questions.four, answers.four, stickers.four),
    5: Level(questions.five, answers.five, stickers.five),
    6: Level(questions.six, answers.six, stickers.six),
    7: Level(questions.seven, answers.seven, stickers.seven),
    8: Level(questions.eight, answers.eight, stickers.eight),
    9: Level(questions.nine, answers.nine, stickers.nine),
    10: Level(questions.ten, answers.ten, stickers.ten),
    11: Level(greetings.grats, greetings.grats, stickers.grats)
}
