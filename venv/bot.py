import telebot
import database_work
import level
import user
import greetings
import blood_work

bot = telebot.TeleBot('916863111:AAGWw4dubDgRIszatOgV3MlQFJf-I88FTs4')
database_work.create_table_users()


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


def process_incorrect_content(message, curr_user):
    bot.send_message(message.from_user.id, greetings.incorrect_content)
    bot.register_next_step_handler_by_chat_id(message.chat.id, check_content, curr_user)


def process_level(message, curr_user):
    bot.send_photo(message.chat.id, photo=open('resources/photos/{}'.format(curr_user.level_object.photo), 'rb'))
    sent = bot.send_message(message.chat.id, curr_user.level_object.question)
    bot.register_next_step_handler(sent, check_content, curr_user)


def user_completed_level(message, curr_user):
    bot.send_message(message.chat.id, greetings.correct_answer + blood_work.show_bats(curr_user.blood))
    curr_user.increase_user_level()
    process_level(message, curr_user)


def check_answer(message, curr_user):
    user_message = message.text.lower()
    if user_message == curr_user.level_object.answer:
        user_completed_level(message, curr_user)
        print("user {} passed to a level {}".format(curr_user.user_id, curr_user.level))
    else:
        bot.send_message(message.chat.id, level.get_random_wrong_answer())
        process_level(message, curr_user)


@bot.message_handler(content_types=['text'])
def check_content(message, curr_user):
    if message.content_type == 'text':
        if message.text == '/start' or message.text == '/reset':
            command_start(message)
        else:
            if not curr_user.is_finished():
                print('calling check answer')
                check_answer(message, curr_user)
            else:
                user_completed_level(message, curr_user)
    else:
        process_incorrect_content(message, curr_user)


bot.polling()
