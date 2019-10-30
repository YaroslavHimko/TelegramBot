import questions
import answers
import photos
import random
import greetings


class Level:
    def __init__(self, question, answer, photo):
        self.question = question
        self.answer = answer
        self.photo = photo


def get_random_wrong_answer():
    wrong_answer = random.choice(answers.wrong_answers)
    return wrong_answer


def get_levels_length():
    return len(levels_dict) - 1


def get_level_object(level):
    return levels_dict.get(level)


levels_dict = {
    1: Level(questions.one, answers.one, photos.one),
    2: Level(questions.two, answers.two, photos.two),
    3: Level(questions.three, answers.three, photos.three),
    4: Level(questions.four, answers.four, photos.four),
    5: Level(questions.five, answers.five, photos.five),
    6: Level(questions.six, answers.six, photos.six),
    7: Level(questions.seven, answers.seven, photos.seven),
    8: Level(questions.eight, answers.eight, photos.eight),
    9: Level(questions.nine, answers.nine, photos.nine),
    10: Level(questions.ten, answers.ten, photos.ten),
    11: Level(greetings.grats, greetings.grats, photos.grats)
}
