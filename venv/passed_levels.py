import level
import level_content
import questions
import answers
import photos


class Passed_levels:
    def __init__(self, is_passed, level):
        self.is_passed = is_passed
        self.level = level


level_one = Passed_levels(False, level.Level('one', level_content.Content(questions.one, answers.one, photos.one)))
level_two = Passed_levels(False, level.Level('two', level_content.Content(questions.two, answers.two, photos.two)))
level_three = Passed_levels(False, level.Level('three', level_content.Content(questions.three, answers.three, photos.three)))
level_four = Passed_levels(False, level.Level('four', level_content.Content(questions.four, answers.four, photos.four)))
level_five = Passed_levels(False, level.Level('five', level_content.Content(questions.five, answers.five, photos.five)))
level_six = Passed_levels(False, level.Level('six', level_content.Content(questions.six, answers.six, photos.six)))
level_seven = Passed_levels(False, level.Level('seven', level_content.Content(questions.seven, answers.seven, photos.seven)))
level_eight = Passed_levels(False, level.Level('eight', level_content.Content(questions.eight, answers.eight, photos.eight)))
level_nine = Passed_levels(False, level.Level('nine', level_content.Content(questions.nine, answers.nine, photos.nine)))
level_ten = Passed_levels(False, level.Level('ten', level_content.Content(questions.ten, answers.ten, photos.ten)))

levels_list = {
    0: level_one,
    1: level_two,
    2: level_three,
    3: level_four,
    4: level_five,
    5: level_six,
    6: level_seven,
    7: level_eight,
    8: level_nine,
    9: level_ten
}