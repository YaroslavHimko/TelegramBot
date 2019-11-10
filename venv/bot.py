import telebot
import level
import user
import greetings
import blood_work
import os
import json_worker
import passed_levels

##token = os.environ.get('TelegramToken')
bot = telebot.TeleBot('916863111:AAGWw4dubDgRIszatOgV3MlQFJf-I88FTs4')


def hello_message(message):
    print('calling hello message')
    bot.send_message(message.chat.id, greetings.one)
    bot.send_message(message.chat.id, greetings.two)


@bot.message_handler(commands=['start'])
def command_start(message):
    print('calling command start')
    hello_message(message)
    current_user = user.User(message.from_user.id, message.chat.first_name, 1, 0, passed_levels.levels_list)
    json_worker.user_json_writer(current_user)
    process_level(message, current_user, current_user.passed_levels.get(current_user.level).level.content)


@bot.message_handler(content_types=['text'])
def catching_excessive_text(message):
    print('calling catching excessive text')
    curr_user = user.get_user(message.from_user.id)
    process_level(message, curr_user, curr_user.passed_levels.get(str(curr_user.level)).level.content)


def process_incorrect_content(message, curr_user):
    print('calling process incorrect text')
    bot.send_message(message.from_user.id, greetings.incorrect_content)
    bot.register_next_step_handler_by_chat_id(message.chat.id, check_content, curr_user)


def process_level(message, curr_user, content):
    print('calling process level')
    bot.send_photo(message.chat.id, photo=open('resources/photos/{}'.format(content.photo), 'rb'))
    sent = bot.send_message(message.chat.id, content.question)
    bot.register_next_step_handler(sent, check_content, curr_user, content)


def user_completed_level(message, curr_user, content):
    print('calling user completed level')
    bot.send_message(message.chat.id, greetings.correct_answer + blood_work.show_bats(curr_user.blood))
    content = curr_user.get_new_level()
    process_level(message, curr_user, content)


def check_answer(message, curr_user, content):
    print('calling check asnwer')
    user_message = message.text.lower()
    if user_message == content.answer:
        user_completed_level(message, curr_user, content)
    else:
        bot.send_message(message.chat.id, level.get_random_wrong_answer())
        process_level(message, curr_user, content)


@bot.message_handler(content_types=['text'])
def check_content(message, curr_user, content):
    print('calling check content')
    if message.content_type == 'text':
        if message.text == '/start' or message.text == '/reset':
            command_start(message)
        else:
            if not curr_user.is_finished():
                check_answer(message, curr_user, content)
            else:
                user_completed_level(message, curr_user, content)
    else:
        process_incorrect_content(message, curr_user, content)


bot.polling()
