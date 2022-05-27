import Constants as keys
from telegram.ext import *
from telegram import *
import json

print('Бот запускається...')


def read_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def start_command(update, context):
    buttons = read_json("Buttons.json")
    update.message.reply_text('Привіт! Я бот-помічник від Stud-point. \n'
                              'Я створений для того, щоб відповідати на найпоширенші питання. \n'
                              'Будь-ласка оберіть свою роль ⬇',
                              reply_markup=ReplyKeyboardMarkup(buttons["first_choice"], one_time_keyboard=True))


def help_command(update, context):
    update.message.reply_text('Попросіть когось про допомогу!')


def handle_massage(update, context):
    buttons = read_json("Buttons.json")
    user_massage = str(update.message.text).lower()

    if user_massage in ('Студент, студент'):
        update.message.reply_text('Вітаю, я радий що ще одна людина ступила на шлях кар\'єрного зростання.',
                                  reply_markup=ReplyKeyboardMarkup(buttons["student_choice"], one_time_keyboard=True))

    elif user_massage in ('Роботодавець, роботодавець', 'Партнер', 'партнер'):
        update.message.reply_text('Вітаю, що саме вас цікавить?')

    else:
        update.message.reply_text('Я вас не розумію... Спробуйте інший запит')


def error(update, context):
    print("Update {} caused error {}".format(update, context.error))


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler('help', help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_massage))

    dp.add_error_handler(error)

    updater.start_polling()
    print('Бот Готовий!')
    updater.idle()


if __name__ == '__main__':
    main()
