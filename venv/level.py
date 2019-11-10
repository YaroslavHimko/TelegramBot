import questions
import answers
import photos
import random
import greetings


class Level:
    def __init__(self, name, content):
        self.name = name
        self.content = content


def get_random_wrong_answer():
    wrong_answer = random.choice(answers.wrong_answers)
    return wrong_answer


def get_levels_length():
    return len(levels_dict) - 1


def get_level_object(level):
    return levels_dict.get(level)