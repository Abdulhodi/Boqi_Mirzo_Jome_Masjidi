from aiogram.dispatcher.filters.builtin import CommandStart
import handlers.users.namoz_vaqti
from loader import *
from states.state import Add_user,Aloqa
from aiogram.dispatcher import FSMContext
from keyboards.inline.menu import *
from data.config import ADMINS
from aiogram.types import ReplyKeyboardRemove, ForceReply

from utils.misc.check_links import check_link
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from data.config import BOT_TOKEN
from keyboards.default.menu import *
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from data.config import CHANNELS
# from handlers.users.check_sub import check

import logging
from aiogram import Bot, Dispatcher, executor,types
from aiogram.dispatcher.filters import Command, CommandStart
from asyncio import sleep

from data.config import BOT_TOKEN

############################## Majburiy obuna ishlayapti ###############################

logging.basicConfig(level=logging.INFO)

buttons = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton(text="➕Kanal", url="https://t.me/Boqi_Mirzo_Jome_Masjidi")
confirm_btn = types.InlineKeyboardButton(text="✅A'zo bo'ldim", callback_data="confirm")

buttons.add(btn)
buttons.add(confirm_btn)

bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)

channel_id = "@Boqi_Mirzo_Jome_Masjidi"

def check_sub_channel(chat_mumber):
    if chat_mumber['status'] != 'left':
        return True
    else:
        return False

@dp.message_handler()
async def send_welcome(message: types.Message):
    # user_id = message.from_user.username
    # username = message.from_user.first_name
    user=message.from_user.first_name
    chat_id = message.from_user.id

    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)):
        await message.reply(f"Assalomu alaykum {user}")
    else:
        await bot.send_message(chat_id, f"Assalomu alaykum {user}\nbotimizdan foydalanish uchun iltimos kanalimizga a'zo bo'ling!.",reply_markup=buttons)

@dp.callback_query_handler(text='confirm')
async def confirm(call: types.CallbackQuery):
    user = call.from_user.first_name
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=call.from_user.id)):
        await call.message.delete()
        await call.message.answer(f"Assalomu alaykum {user}\nKanalimizga obuna bo'lganingiz uchun rahmat!.😊😊😊",reply_markup=home)
    else:
        await call.message.answer(f"Kechirasiz lekin kanalimizga hali obuna bo'lmadingiz botdan foydalanish uchun iltimos kanalimizga a'zo bo'ling!.",reply_markup=buttons)

# async def start_bot(message: types.Message):
#     user_id = message.from_user.id
#     username = message.from_user.username
#
#     await message.answer(f'Salom <b>{username}</b>')

# matn = "Botimizdan foydalanish uchun rasmiy kanalimizga <b>obuna bo'ling</b> va <b>Tekshirish</b> tugmasini bosing."
# @dp.message_handler(commands=['start'])
# class Asosiy(BaseMiddleware):
#     async def on_pre_process_update(self,xabar:types.Update,data:dict):
#         if xabar.message:
#             user_id = xabar.message.from_user.id
#         elif xabar.callback_query:
#             user_id = xabar.callback_query.from_user.id
#         else:
#             return
#         buttons = InlineKeyboardMarkup(row_width=1)
#         dastlabki = True
#         for k in CHANNELS:
#             holat = await check(user_id=user_id,kanal_id=k)
#             if holat==1:
#                 channels = await bot.get_chat(k)
#                 buttons.insert(InlineKeyboardButton(text=f"✅ {channels.title}", url=f"{await channels.export_invite_link()}"))
#             elif holat==0:
#                 channels = await bot.get_chat(k)
#                 buttons.insert(InlineKeyboardButton(text=f"❌ {channels.title}", url=f"{await channels.export_invite_link()}"))
#             dastlabki *= holat
#         if not dastlabki:
#             buttons.insert(InlineKeyboardButton(text="🔄 Tekshirish",callback_data="check_subsciption"))
#             await bot.send_message(chat_id=user_id,text=matn,disable_web_page_preview=True,
#                                     reply_markup=buttons)
#             raise CancelHandler()

############################ Majburiy obuna #######################################

# # bot = Bot(token=BOT_TOKEN)
# # dp = Dispatcher(bot)
# #
# # channel_id = '-1001958376816'
# # channel_id1 = '-1001784047019'
# #
# # def inline_buttons():
# #   channel_url = InlineKeyboardButton("Kanalimiz", url='https://t.me/Boqi_Mirzo_Jome_Masjidi')
# #   channel_url1 = InlineKeyboardButton("Guruhimiz", url='https://t.me/Boqi_Mirzo_Jome_Masjidi_Muhokama')
#     check = InlineKeyboardButton("✅A'zo bo'ldim", callback_data='subdone')
#     markup = InlineKeyboardMarkup(row_width=1).add(channel_url, check)
#     return markup
#
# @dp.message_handler()
# async def start(message: types.Message):
#     check_sub_channel = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
#     # check_sub_channel1 = await bot.get_chat_member(chat_id=channel_id1, user_id=message.from_user.id)
#     user_id = message.from_user.username
#     username = message.from_user.first_name
#
#     if check_sub_channel['status'] != 'left':
#         await message.answer(f"Assalomu alaykum <b>{username}</b> botimizga xush kelibsiz!",reply_markup=home)
#     else:
#         await message.answer(f"Assalomu alaykum <b>{username}</b> botimizdan foydalanish uchun iltimos kanalimizga a'zo bo'ling!", reply_markup=inline_buttons())
#
#
# @dp.callback_query_handler()
# async def check_sub(callback : types.CallbackQuery):
#     check_sub_channel = await bot.get_chat_member(chat_id=channel_id, user_id=callback.message.from_user.id)
#
#     if check_sub_channel['status'] != 'left':
#         await callback.message.answer("Kanalimizga a'zo bo'lganingiz uchun rahmat! :) 😊😊😊", reply_markup=home)
#     else:
#         await callback.message.answer("Botdan foydalanish uchun iltimos kanalimizga a'zo bo'ling!", reply_markup=inline_buttons())

def register_start_py(dp: Dispatcher):
    dp.register_message_handler(dp, commands=['start'])

# @dp.message_handler(text="Frontend darslari")
# async def bot_echo(message: types.Message):
#    await message.answer(message.text,reply_markup=fronted)

# @dp.message_handler(text="🕋Namoz vaqti")
# async def bot_echo(message: types.Message):
#     await message.answer(message.text,reply_markup=namoz)
#
#
# @dp.message_handler(text="☪40 Farz")
# async def bot_echo(message: types.Message):
#     await message.answer(message.text,reply_markup=home)
# @dp.message_handler(text="Og'iz berkitish duosi🤲")
# async def bot_echo(message: types.Message):
#     await message.answer(message.text,reply_markup=home)
# @dp.message_handler(text="Og'iz ochish duosi🤲")
# async def bot_echo(message: types.Message):
#     await message.answer(message.text,reply_markup=home)
#
# @dp.message_handler(text="🔙orqaga")
# async def bot_echo(message: types.Message):
#     await message.answer("Bosh sahifa",reply_markup=home)


# @dp.message_handler(text="Adminga yozish✍", state="*")
# async def bot_start(message: types.Message, state: FSMContext):
#     tekshirsh = db.count_user_id(user_id=message.from_user.id)
#     if tekshirsh[0] > 0:
#         await message.reply(f"Taklif va mulohazalaringiz bo'lsa yoki savolingiz bo'lsa yozing. Ismingiz va nomeringizni qoldirishni unutmang  👨‍✈️Admin  bilan bog'lanmoqchi bo'lsangiz Ismingiz va raqamingizni yozib qoldiring Admin siz bilan 5 daqiqada bog'lanadi📞", reply_markup=kb.main())
#         await state.finish()
#     else:
#         await message.reply("Ism familyangizni yozing!")
#         await Add_user.full_name.set()
#
# @dp.message_handler(state=Add_user.full_name)
# async def add_full_name(message :types.Message,state:FSMContext):
#     full_name = message.text
#     await state.update_data({'full_name':full_name})
#     await message.answer("Telefon raqamingiz pastdagi tugmani bosish orqali jo'nating!",reply_markup=kb.contact())
#     await Add_user.number.set()
#
# @dp.message_handler(content_types=['contact'], state=Add_user.number)
# async def add_number(message: types.Message,state:FSMContext):
#     id = message.contact.user_id
#     phone_number =message.contact.phone_number
#     await state.update_data({"phone_number":phone_number, "id": id})
#     message_id = (await message.answer("Saqlanmoqda...",reply_markup=ReplyKeyboardRemove())).message_id
#     await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
#     await message.answer("Endi Viloyatingizni Tanlang !",reply_markup=kb.city())
#     await Add_user.city.set()
#
# @dp.callback_query_handler(state=Add_user.city)
# async def add_city(call: types.CallbackQuery,state: FSMContext):
#     data = call.data
#     print(data)
#     await call.message.delete()
#     await state.update_data({"data": data})
#     malumot = await state.get_data()
#     user_id = malumot.get("id")
#     full_name = malumot.get("full_name")
#     number = malumot.get("phone_number")
#     city = malumot.get("data")
#     try:
#         db.add_user(user_id=user_id,full_name=full_name,number=number,city=city)
#     except Exception as xatolik:
#         print(xatolik)
#
#     await call.message.answer("Talif va mulohazalaringiz bo'lsa yoki savolingiz bo'lsa yozing  👨‍✈️Admin  bilan bog'lanmoqchi bo'lsangiz Ismingiz va raqamingizni yozib qoldiring Admin siz bilan 5 daqiqada bog'lanadi📞",reply_markup=ForceReply())
#     await state.finish()
#     await Aloqa.aloqa.set()
#
# @dp.message_handler(state=Aloqa.aloqa)
# async def add_full_name(message :types.Message, state:FSMContext):
#     user_id = message.from_user.id
#     Aloqa_TXT = message.text
#     await state.update_data({'Aloqa_TXT': Aloqa_TXT,"user_id":user_id})
#     tg_id = db.select_all_user(user_id=user_id)
#     for x in tg_id:
#         text = f"{message.from_user.get_mention()} Dan Xabar Keldi\n\n"
#         text += f"👤 Ism va familiyasi: {x[2]}\n"
#         text += f"📞 Telefon raqami : +{x[3]}\n"
#         text += f"🏘 Yashash Joyi : {x[4]}\n\n"
#         text += f"📝 Murojati :  {Aloqa_TXT}"
#         await bot.send_message(chat_id=ADMINS[0],text=text)
#         await message.answer("<b>Yuborildi ...</b>",reply_markup=home)
#         await state.finish()
#
# @dp.callback_query_handler(text="habar")
# async def add_full_name(call : types.CallbackQuery):
#     await call.message.answer("Xabar yozing ....",reply_markup=ForceReply())
#     await Aloqa.aloqa.set()
#
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Привет, {message.from_user.full_name}!")
