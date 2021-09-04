# by krutmaster (telegram: @krutmaster1)
import telebot
import os


# Classes
from settings import Settings
#fun
from check_ero import check_ero


settings = Settings.open()
bot = telebot.TeleBot(settings.token)
#boss = '538231919'
boss = '119893362'


@bot.message_handler(commands=["start"])
def start(message):
    id = str(message.chat.id)
    if id == boss:
        bot.send_message(id, 'Привет, Юра, всё пашет')
    else:
        bot.send_message(id, 'Напиши владельцу этого бота, если хочешь добавить его в свою группу, а то я тебе порнуху на аву чата поставлю')


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    id = str(message.chat.id)
    try:
        user = message.new_chat_member
        photo = bot.get_user_profile_photos(user.id, limit=1).photos[0]
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'temp/{user.id}.jpg', 'wb') as file:
            file.write(downloaded_file)
        check = check_ero(f'temp/{user.id}.jpg')
        os.remove(f'temp/{user.id}.jpg')
        if not check:
            bot.send_message(id, f'Шлюха детектед: {user.first_name}')
            bot.kick_chat_member(id, user.id)
    except Exception as e:
        bot.send_message(538231919, f'handler_new_member:\n{e}')


if __name__ == '__main__':
    bot.polling(none_stop=True)
