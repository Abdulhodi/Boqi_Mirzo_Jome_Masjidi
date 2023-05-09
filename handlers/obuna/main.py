from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from data.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

channel_id = '-1001958376816'

def inline_buttons():
    channel_url = InlineKeyboardButton('Kanalimiz', url='https://t.me/Boqi_Mirzo_Jome_Masjidi')
    check = InlineKeyboardButton("✅A'zo bo'ldim", callback_data='subdone')
    markup = InlineKeyboardMarkup(row_width=1).add(channel_url, check)
    return markup

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    check_sub_channel = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)

    if check_sub_channel['status'] != 'left':
        await message.answer("Kanalga a'zo bo'lganingiz uchun rahmat! :) ")
    else:
        await message.answer("Botdan foydalanish uchun iltimos a'zo bo'ling!", reply_markup=inline_buttons())

@dp.callback_query_handler()
async def check_sub(callback : types.CallbackQuery):
    check_sub_channel = await bot.get_chat_member(chat_id=channel_id, user_id=callback.message.from_user.id)

    if check_sub_channel['status'] != 'left':
        await callback.message.answer("Kanalga a'zo bo'lganingiz uchun rahmat! :) ")
    else:
        await callback.message.answer("Botdan foydalanish uchun iltimos a'zo bo'ling!", reply_markup=inline_buttons())
