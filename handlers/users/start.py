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



# async def start_bot(message: types.Message):
#     user_id = message.from_user.id
#     username = message.from_user.username
#
#     await message.answer(f'Salom <b>{username}</b>')

bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)

channel_id = '-1001958376816'

def inline_buttons():
    channel_url = InlineKeyboardButton('Kanalimiz', url='https://t.me/Boqi_Mirzo_Jome_Masjidi')
    check = InlineKeyboardButton("✅A'zo bo'ldim", callback_data='subdone')
    markup = InlineKeyboardMarkup(row_width=1).add(channel_url, check)
    return markup

@dp.message_handler(CommandStart())
async def start(message: types.Message):
    check_sub_channel = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
    user_id = message.from_user.username
    username = message.from_user.first_name

    if check_sub_channel['status'] != 'left':
        await message.answer(f"Assalomu alaykum <b>{username}</b> botimizga xush kelibsiz!",reply_markup=home)
    else:
        await message.answer(f"Assalomu alaykum <b>{username}</b> botimizdan foydalanish uchun iltimos kanalimizga a'zo bo'ling!", reply_markup=inline_buttons())


@dp.callback_query_handler()
async def check_sub(callback : types.CallbackQuery):
    if callback.data == "subdone":
       check_sub_channel = await bot.get_chat_member(chat_id=channel_id, user_id=callback.message.from_user.id)

       if check_sub_channel['status'] != 'left':
          await callback.message.answer("Kanalimizga a'zo bo'lganingiz uchun rahmat! :) 😊😊😊", reply_markup=home)
       else:
          await callback.message.answer("Botdan foydalanish uchun iltimos kanalimizga a'zo bo'ling!", reply_markup=inline_buttons())

def register_start_py(dp: Dispatcher):
    dp.register_message_handler(home, commands=['start'])

@dp.message_handler(text="Frontend darslari")
async def bot_echo(message: types.Message):
    await message.answer(message.text,reply_markup=fronted)

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
