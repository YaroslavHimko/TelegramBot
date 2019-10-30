import telebot
from telebot import types
import database_work
import level
import user
import greetings
import blood_work

bot = telebot.TeleBot('916863111:AAGWw4dubDgRIszatOgV3MlQFJf-I88FTs4')


def hello_message(message):
    bot.send_message(message.chat.id, greetings.one)
    bot.send_message(message.chat.id, greetings.two)


@bot.message_handler(commands=['start'])
def command_start(message):
    hello_message(message)
    current_user = user.User(message.from_user.id, 'default', 1, 1, '0', level.get_level_object(1))
    process_level(message, current_user)


@bot.message_handler(content_types=['text'])
def catching_excessive_text(message):
    curr_user = user.User.get_user(message.from_user.id)
    process_level(message, curr_user)


def process_incorrect_content(message, user):
    bot.send_message(message.from_user.id, greetings.incorrect_content)
    bot.register_next_step_handler_by_chat_id(message.chat.id, check_content, user)


def process_level(message, user):
    bot.send_sticker(message.chat.id, user.level_object.sticker)
    sent = bot.send_message(message.chat.id, user.level_object.question)
    bot.register_next_step_handler(sent, check_content, user)


def user_completed_level(message, user):
    bot.send_message(message.chat.id, greetings.correct_answer + blood_work.show_bats(user.blood))
    user.increase_user_level()
    process_level(message, user)


def check_answer(message, user):
    user_message = message.text.lower()
    if user_message == user.level_object.answer:
        user_completed_level(message, user)
        print("user {} passed to a level {}".format(user.id, user.level))
    else:
        bot.send_message(message.chat.id, level.get_random_wrong_answer())
        process_level(message, user)


@bot.message_handler(content_types=['text'])
def check_content(message, user):
    if message.content_type == 'text':
        if message.text == '/start' or message.text == '/reset':
            command_start(message)
        if not user.is_finished():
            print('calling check answer')
            check_answer(message, user)
        else:
            user_completed_level(message, user)
    else:
        process_incorrect_content(message, user)


bot.polling()
