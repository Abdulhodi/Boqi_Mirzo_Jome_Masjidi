from aiogram import types

from loader import dp, bot


@dp.message_handler(text="1-dars")
async def bot_echo(message: types.Message):
    ms_id = message.from_user.id
    video_manzili = "https://t.me/Qoqon_quqon/70346"
    await bot.send_video(chat_id=ms_id,video=video_manzili,caption="Fronted 1-dars")