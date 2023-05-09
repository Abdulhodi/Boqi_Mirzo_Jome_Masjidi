from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



class Keyboards:
    def main(self):
        menu = types.InlineKeyboardMarkup(row_width=2)
        Aloqa = types.InlineKeyboardButton("Adminga Xabar jo'natish",callback_data="habar")
        Channel = types.InlineKeyboardButton("Bizning Kanal",url="https://t.me/Boqi_Mirzo_Jome_Masjidi")
        return menu.add(Aloqa,Channel)

    def contact(self):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        contact = types.KeyboardButton("Raqamni yuborish 📞",request_contact=True)
        return menu.add(contact)

    def city(self):
        menu = types.InlineKeyboardMarkup(row_width=2)
        Toshkent = types.InlineKeyboardButton("Toshkent", callback_data="Toshkent")
        Namangan = types.InlineKeyboardButton("Namangan",callback_data="Namangan")
        Fargona = types.InlineKeyboardButton("Farg'ona",callback_data="Fargona")
        Andijon = types.InlineKeyboardButton("Andijon",callback_data="Andijon")
        Jizzah = types.InlineKeyboardButton("Jizzah",callback_data="Jizzah")
        Surxandaryo = types.InlineKeyboardButton("Surxandaryo", callback_data="Surxandaryo")
        Qashqadaryo = types.InlineKeyboardButton("Qashqadaryo", callback_data="Qashqadaryo")
        Buxoro = types.InlineKeyboardButton("Buxoro", callback_data="Buxoro")
        Navoiy = types.InlineKeyboardButton("Navoiy", callback_data="Navoiy")
        Samarqand = types.InlineKeyboardButton("Samarqand", callback_data="Samarqand")
        Sirdaryo = types.InlineKeyboardButton("Sirdaryo", callback_data="Sirdaryo")
        Xorazim = types.InlineKeyboardButton("Xorazim", callback_data="Xorazim")
        Qoraqalpogiston = types.InlineKeyboardButton("Qoraqalpog'iston", callback_data="Qoraqalpog'iston")
        return menu.add(Toshkent,Namangan,Samarqand,Buxoro,Andijon,Fargona,Sirdaryo,Qashqadaryo,Surxandaryo,Xorazim,Navoiy,Jizzah,Qoraqalpogiston)

kb = Keyboards()
