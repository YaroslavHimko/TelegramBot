import user
import json
import passed_levels
import level
import level_content


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
                         passed_levels=get_passed_levels_objects_dict(user_json.get('passed_levels')))


def get_passed_levels_objects_dict(passed_levels_json):
    passed_levels_dict = {}
    for key, value in passed_levels_json.items():
        passed_levels_dict[key] = passed_levels.Passed_levels(is_passed=value.get('is_passed'),
                                                              level=get_level(value.get('level')))
    return passed_levels_dict


def get_level(level_json):
    return level.Level(name=level_json.get('name'), content=get_content(level_json.get('content')))


def get_content(content_json):
    return level_content.Content(question=content_json.get('question'),
                                 answer=content_json.get('answer'),
                                 photo=content_json.get('photo'))
