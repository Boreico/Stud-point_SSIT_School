from telegram.ext import *
from telegram import *
import json
import re


def read_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def start_command(update, context):
    buttons = read_json("Buttons.json")
    update.message.reply_text('Привіт! Я бот-помічник від Stud-point. \n'
                              'Я створений для того, щоб відповідати на найпоширенші питання. \n'
                              'Будь-ласка оберіть свою роль ⬇',
                              reply_markup=ReplyKeyboardMarkup.from_column(buttons["first_choice"],
                                                                           one_time_keyboard=True,
                                                                           resize_keyboard=True))


def help_command(update, context):
    update.message.reply_text('Попросіть когось про допомогу!')


def contact_callback(update, context):
    constants = read_json("Constants.json")
    with open('temp.txt', 'r') as temp:
        text = temp.read()
    contact = update.effective_message.contact
    context.bot.send_message(chat_id=constants["manager_id"], text=text)
    context.bot.send_contact(chat_id=constants["manager_id"], phone_number=contact.phone_number,
                             first_name=contact.first_name)
    update.message.reply_text("Дякую! Очікуйте на відповідь від оператора.")


def resume_callback(update, context):
    constants = read_json("Constants.json")
    file = update.effective_message.document
    context.bot.send_document(chat_id=constants["manager_id"], document=file)
    update.message.reply_text("Дякую! Ваше резюме отримано.")


def handle_massage(update, context):
    buttons = read_json("Buttons.json")
    links = read_json("Links.json")
    user_massage = str(update.message.text).lower()
    if user_massage == 'студент':
        update.message.reply_text('Вітаю, я радий що ще одна людина ступила на шлях кар\'єрного зростання.',
                                  reply_markup=ReplyKeyboardMarkup.from_column(buttons["student_choice"],
                                                                               one_time_keyboard=True,
                                                                               resize_keyboard=True))

    elif user_massage == 'роботодавець':
        update.message.reply_text('Вітаю, що саме вас цікавить?',
                                  reply_markup=ReplyKeyboardMarkup.from_column(buttons["employers_choice"],
                                                                               one_time_keyboard=True,
                                                                               resize_keyboard=True))

    elif len(re.findall(r'.*партнер*', user_massage)) >= 1:
        update.message.reply_text('Вітаю, що саме вас цікавить?',
                                  reply_markup=ReplyKeyboardMarkup.from_column(buttons["partner_choice"],
                                                                               one_time_keyboard=True))

    elif user_massage in (
    "співпраця", "розмістити рекламу", "проект під ключ", "oплата курсу", "брендинг консультація", "зв'язатись з нами"):
        reply_markup = ReplyKeyboardMarkup([[KeyboardButton(buttons['get_contact'][0], request_contact=True),
                                             KeyboardButton(buttons['get_contact'][1])]],
                                           one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text("Залиште ваш номер, з вами зв'яжеться менеджер",
                                  reply_markup=reply_markup)
        with open("temp.txt", "w") as temp:
            temp.write(user_massage)

    elif user_massage == "реклама":
        update.message.reply_text("Оберіть вашу опцію ⬇",
                                  reply_markup=ReplyKeyboardMarkup.from_column(buttons['ad'], one_time_keyboard=True,
                                                                               resize_keyboard=True))

    elif user_massage == "брендинг":
        update.message.reply_text("Ви можете ознайомитись з нашим дослідженням, або зв'язатись з нами.",
                                  reply_markup=ReplyKeyboardMarkup.from_column(buttons["branding"],
                                                                               one_time_keyboard=True,
                                                                               resize_keyboard=True))

    elif user_massage == "дослідження":
        update.message.reply_text("Наше <b><a href={link}>дослідження</a></b>".format(link=links["research"]),
                                  parse_mode=ParseMode.HTML)

    elif user_massage == "інше":
        update.message.reply_text("Введіть ваш запит, або залиште контакт і звами зв'яжеться менеджер",
                                  reply_markup=ReplyKeyboardMarkup.from_column(buttons["other"],
                                                                               one_time_keyboard=True,
                                                                               resize_keyboard=True))


    elif len(re.findall(r'.*ваканс*', user_massage)) >= 1 or user_massage == "кар'єра":
        update.message.reply_text('На данний момент доступні наступні вакансії.... (їх треба десь взяти)',
                                  reply_markup=ReplyKeyboardMarkup.from_column(buttons["resume"],
                                                                               one_time_keyboard=True,
                                                                               resize_keyboard=True))
    elif user_massage == "актуальні курси":
        update.message.reply_text('Оберіть що вас цікавить ⬇',
                                  reply_markup=ReplyKeyboardMarkup.from_column(buttons["courses"],
                                                                               one_time_keyboard=True,
                                                                               resize_keyboard=True))
    elif user_massage == "marketing school":
        update.message.reply_text("Тут має бути опис школи...\n"
                                  "<b><a href={link}>дізнатись більше</a></b>".format(link=links["marketing_school"]),
                                  parse_mode=ParseMode.HTML)
    elif user_massage == "finance & audit school":
        update.message.reply_text("Тут має бути опис школи...\n"
                                  "<b><a href={link}>дізнатись більше</a></b>".format(link=links["finance_school"]),
                                  parse_mode=ParseMode.HTML)
    elif user_massage == "hr & recruitment school":
        update.message.reply_text("Тут має бути опис школи...\n"
                                  "<b><a href={link}>дізнатись більше</a></b>".format(link=links["HR_school"]),
                                  parse_mode=ParseMode.HTML)
    elif user_massage == "pm & leader school":
        update.message.reply_text("Тут має бути опис школи...\n"
                                  "<b><a href={link}>дізнатись більше</a></b>".format(link=links["PM_school"]),
                                  parse_mode=ParseMode.HTML)
    elif user_massage == "digital school":
        update.message.reply_text("Тут має бути опис школи...\n"
                                  "<b><a href={link}>дізнатись більше</a></b>".format(link=links["digital_school"]),
                                  parse_mode=ParseMode.HTML)

    elif user_massage == "startup school":
        update.message.reply_text("Тут має бути опис школи...\n"
                                  "<b><a href={link}>дізнатись більше</a></b>".format(link=links["startup_school"]),
                                  parse_mode=ParseMode.HTML)

    elif user_massage == "відправити резюме":
        update.message.reply_text('Завантажте ваше резюме в цей чат.')

    elif user_massage == "на початок":
        update.message.reply_text('Привіт! Я бот-помічник від Stud-point. \n'
                                  'Я створений для того, щоб відповідати на найпоширенші питання. \n'
                                  'Будь-ласка оберіть свою роль ⬇',
                                  reply_markup=ReplyKeyboardMarkup.from_column(buttons["first_choice"],
                                                                               one_time_keyboard=True,
                                                                               resize_keyboard=True))

    else:
        update.message.reply_text('Я вас не розумію... Спробуйте інший запит')


def error(update, context):
    print("Update {} caused error {}".format(update, context.error))


def main():
    constant = read_json("Constants.json")
    updater = Updater(constant["API_KEY"], use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler('help', help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_massage))

    dp.add_handler(MessageHandler(Filters.contact, contact_callback))

    dp.add_handler(MessageHandler(Filters.document, resume_callback))

    dp.add_error_handler(error)

    updater.start_polling()
    print('Бот Готовий!')
    updater.idle()


if __name__ == '__main__':
    print('Бот запускається...')
    main()
