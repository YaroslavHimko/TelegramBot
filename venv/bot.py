import telebot
from src import level
from src import user
from resources import greetings
import os
from src import json_worker
from src import passed_levels
from resources import photos

token = os.environ.get('TelegramToken')
bot = telebot.TeleBot(token)

#bot = telebot.TeleBot('1007513687:AAEF8E6M45ku6RpCyw_iW0NPVErVefYY3BE')
winners_dict = []


def hello_message(message):
    bot.send_message(message.chat.id, greetings.one)
    bot.send_message(message.chat.id, greetings.two)


@bot.message_handler(commands=['start'])
def command_start(message):
    hello_message(message)
    current_user = user.create_user(message.from_user.id, message.chat.first_name)
    process_level(message, current_user)


def command_restart(message, curr_user):
    hello_message(message)
    curr_user.reset_user()
    process_level(message, curr_user)


def catching_excessive_text(message):
    curr_user = user.get_user(message.from_user.id, message.chat.first_name)
    process_level(message, curr_user)


def process_incorrect_content(message, curr_user):
    bot.send_message(message.from_user.id, greetings.incorrect_content)
    bot.register_next_step_handler_by_chat_id(message.chat.id, check_content, curr_user)


def process_level(message, curr_user):
    if curr_user.is_finished():
        winners_dict.append(message.chat.username)
        if (message.chat.username in winners_dict) and winners_dict.index(message.chat.username) < 26:
            bot.send_photo(message.chat.id, photo=open('resources/photos/{}'.format(photos.discount), 'rb'))
            bot.send_message(message.chat.id, greetings.grats_won)
            print('won')
            print(message.chat.username)
        else:
            bot.send_photo(message.chat.id, photo=open('resources/photos/{}'.format(photos.grats), 'rb'))
            bot.send_message(message.chat.id, greetings.grats)
            print('not won')
            print(message.chat.username)
        return
    curr_level = curr_user.level
    content = curr_user.passed_levels[curr_level].level
    if curr_user.level != 0:
        bot.send_photo(message.chat.id, photo=open('resources/photos/{}'.format(content.photo), 'rb'))
    sent = bot.send_message(message.chat.id, content.question)
    bot.register_next_step_handler(sent, check_content, curr_user)


def user_completed_level(message, curr_user):
    bot.send_message(message.chat.id, greetings.correct_answer + curr_user.show_bats())
    curr_user.get_new_level()
    process_level(message, curr_user)


def check_answer(message, curr_user):
    if curr_user is None:
        curr_user = user.get_user(message.from_user.id, message.chat.first_name)
    user_message = message.text.lower()
    curr_level = curr_user.level
    passed = curr_user.passed_levels[curr_level]
    content = passed.level
    if user_message == content.answer:
        user_completed_level(message, curr_user)
    else:
        bot.send_message(message.chat.id, level.get_random_wrong_answer())
        process_level(message, curr_user)


def check_content(message, curr_user):
    if message.content_type == 'text':
        if message.text == '/start' or message.text == '/reset' or message.text == 'Старт':
            command_restart(message, curr_user)
            return
        if curr_user.is_finished():
            bot.send_photo(message.chat.id, photo=open('resources/photos/{}'.format(photos.grats), 'rb'))
            bot.send_message(message.chat.id, greetings.grats)
        else:
            if not curr_user.is_finished():
                check_answer(message, curr_user)
            else:
                user_completed_level(message, curr_user)
    else:
        process_incorrect_content(message, curr_user)


bot.polling()
