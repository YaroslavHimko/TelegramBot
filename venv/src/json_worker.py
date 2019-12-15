from src import user
import json
from src import passed_levels
from src import level

def jsonDefault(OrderedDict):
    return OrderedDict.__dict__


def user_json_writer(user):
    with open('users/{}.json'.format(user.user_id), 'w') as user_file:
        user_file.write(json.dumps(user, default=jsonDefault, indent=4))


def user_json_reader(user_id):
    with open('users/{}.json'.format(user_id), 'r') as user_file:
        user_json = json.load(user_file)
        return user.User(user_id=user_json.get('user_id'),
                         name=user_json.get('name'),
                         blood=user_json.get('blood'),
                         level=user_json.get('level'),
                         passed_levels=get_passed_levels_objects_list(user_json.get('passed_levels')))

def user_reader(user_id):
    with open('users/{}'.format(user_id), 'r') as user_file:
        user_json = json.load(user_file)
        return user.User(user_id=user_json.get('user_id'),
                         name=user_json.get('name'),
                         blood=user_json.get('blood'),
                         level=user_json.get('level'),
                         passed_levels=get_passed_levels_objects_list(user_json.get('passed_levels')))

def get_passed_levels_objects_list(passed_levels_json):
    passed_levels_list = []
    for item in passed_levels_json:
        passed_levels_list.append(passed_levels.Passed_levels(number=item.get('number'),
                                                              is_passed=item.get('is_passed'),
                                                              level=get_level(item.get('level'))))
    return passed_levels_list


def get_level(level_json):
    return level.Level(question=level_json.get('question'),
                                 answer=level_json.get('answer'),
                                 photo=level_json.get('photo'))