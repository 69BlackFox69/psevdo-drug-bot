import logging
from aiogram import Bot, Dispatcher, executor, types
import config

#log lvl

logging.basicConfig(level=logging.INFO)

#bot int
#5598057305:AAHVA1bDxwCXFpurI9xHszq6fOBJAt1rsHc
bot = Bot(token = config.TOKEN)
dp = Dispatcher(bot)

# @dp.message_handler(is_admin=True, commands = ["ban"], commands_prefix = "!/")
# async def cmd_ban(message: types.Message):
#     if not message.reply_to_message:
#         await message.reply("Эта команда должна быть ответом на сообщение")
#         return
#
#     await message.bot.delete_message(chat_id=config.GROUP.ID, message.message_id)
#     await message.bot.kick_chat_member(chat_id=config.GROUP_ID, user_id=message.reply_to_message.from_user.id)
#     await message.reply_to_message.reply("Бан Нахуй")

@dp.message_handler()
async def filter_message(message: types.Message):
    if "хаха" in message.text:
        await message.reply("Согласен хорошая шутка, хахахахаха")
    elif "Хаха" in message.text:
        await message.reply("Согласен хорошая шутка, хахахахаха")
    elif "ты че" in message.text:
        await message.reply("А ни че на, нормально общайся на")
    elif "Ты че" in message.text:
        await message.reply("А ни че на, нормально общайся на")
    elif "надеюсь не прилетит" in message.text:
        await message.reply("Надежда умирает последней)")
    elif "Надеюсь не прилетит" in message.text:
        await message.reply("Надежда умирает последней)")
    elif "въебало" in message.text:
        await message.reply("Плотно въебало")
    elif "Въебало" in message.text:
        await message.reply("Плотно въебало")
    elif "вьебало" in message.text:
        await message.reply("Плотно въебало")
    elif "Вьебало" in message.text:
        await message.reply("Плотно въебало")
    elif "Щя вьебет" in message.text:
        await message.reply("Тикаем бигом зьебуем")
    elif "щя вьебет" in message.text:
        await message.reply("Тикаем бигом зьебуем")
    elif "Шя вьебет" in message.text:
        await message.reply("Тикаем бигом зьебуем")
    elif "шя вьебет" in message.text:
        await message.reply("Тикаем бигом зьебуем")
    elif "туса" in message.text:
        await  message.reply("Кто то сказал туса?")
    elif "Туса" in message.text:
        await  message.reply("Кто то сказал туса?")
    elif "спелая" in message.text:
        await message.reply("Я один уже на эту хуйню повелся")
    elif "Спелая" in message.text:
        await message.reply("Я один уже на эту хуйню повелся")

@dp.message_handler(content_types=['photo'])
async def get_eser_photo(message):
    await message.reply('Прикольно')




#echo
# @dp.message_handler()
# async def filter_message(message: types.Message):
#     if "плохое слово" in message.text:
#         await message.delete()



#run long-polling

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
