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
    current_user = user.User(message.from_user.id, 'default', 1, 0, '0', level.levels_list[0])
    process_level(message, current_user)


@bot.message_handler(content_types=['text'])
def catching_excessive_text(message):
    curr_user = user.User.get_user(message.from_user.id)
    process_level(message, curr_user)


@bot.message_handler(content_types=['text'])
def check_answer(message, user):
    if message.content_type == 'text':
        user_message = message.text.lower()
        if user_message == user.level_object.answer and user.level < level.get_levels_length():
            bot.send_message(message.chat.id, 'Молодец\n' + blood_work.show_bats(user.blood))
            if user.level < level.get_levels_length():
                user.increase_user_level()
                print("user {} passed to a level {}".format(user.id, user.level + 1))
                process_level(message, user)
            else:
                process_level(message, user)
        elif user_message == '/start':
            command_start(message)
        elif user.level >= level.get_levels_length():
            bot.send_sticker(message.chat.id, user.level_object.sticker)
            bot.send_message(message.chat.id, user.level_object.question)
        else:
            bot.send_message(message.chat.id, user.level_object.get_random_wrong_answer())
            bot.register_next_step_handler_by_chat_id(message.chat.id, check_answer, user)

    else:
        bot.send_message(message.from_user.id, greetings.incorrect_content)
        bot.register_next_step_handler_by_chat_id(message.chat.id, check_answer, user)


def process_level(message, user):
    bot.send_sticker(message.chat.id, user.level_object.sticker)
    sent = bot.send_message(message.chat.id, user.level_object.question)
    bot.register_next_step_handler(sent, check_answer, user)


def congrats(message):
    bot.send_message(message.chat.id, 'Grats')


bot.polling()
