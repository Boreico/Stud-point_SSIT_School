import re
from telegram.ext import *
from telegram import *


def sample_responses(update, context, input_text):
    user_massage = str(input_text).lower()

    if user_massage in ('привіт', 'привіт!'):
        return ['Привіт! Радий тебе чути!']

    if user_massage in ('хто ти такий', 'хто ти такий?', 'хто ти', 'хто ти?'):
        return ['Я Stud-point бот!']

    if user_massage in ('Студент, студент'):
        return ['Вітаю, я радий що ще одна людина ступила на шлях кар\'єрного зростання.',
                update.message.reply_text(reply_markup=ReplyKeyboardMarkup('test', one_time_keyboard=True))]

    if user_massage in ('Роботодавець, роботодавець', 'Партнер', 'партнер'):
        return ['Вітаю, що саме вас цікавить?']

    return ['Я тебе не розумію... Спробуй інший запит']
