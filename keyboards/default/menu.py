from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

home=ReplyKeyboardMarkup(
    keyboard=[
        # [KeyboardButton(text="Frontend darslari")],
        [KeyboardButton(text="🕋Namoz vaqti")],
        [KeyboardButton(text="Alloh taoloning go'zal 99 ismi")],
        [KeyboardButton(text="☪40 Farz"),KeyboardButton(text="📿Zikr va duolar🤲")],
        [KeyboardButton(text="Og'iz berkitish duosi🤲"),KeyboardButton(text="Og'iz ochish duosi🤲")],
        # [KeyboardButton(text="Islomiy videolar")],
        [KeyboardButton(text="Adminga yozish✍")]
        # [KeyboardButton(text="Send Phone", request_contact=True)],
    ],
    resize_keyboard=True
)

fronted = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1-dars"),KeyboardButton(text="2-dars")],
        [KeyboardButton(text="3-dars"),KeyboardButton(text="4-dars")],
        [KeyboardButton(text="🔙orqaga")],
    ],
    resize_keyboard=True
)
namoz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Bomdod"),KeyboardButton(text="Quyosh")],
        [KeyboardButton(text="Peshin"),KeyboardButton(text="Asr")],
        [KeyboardButton(text="Shom"),KeyboardButton(text="Xuftan")],
        [KeyboardButton(text="Vitr")],
        [KeyboardButton(text="🔙orqaga")],
    ],
    resize_keyboard=True
)

duolar_zikrlar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Tong va kechqurunda"),KeyboardButton(text="Juma tongida")],
        [KeyboardButton(text="Uxlashdan oldin"),KeyboardButton(text="Bezovta bo'lib, uxlay olmaganda")],
        [KeyboardButton(text="Uyquda qo'rqqanda"), KeyboardButton(text="Tushida yoqtirmagan narsani ko'rganda")],
        [KeyboardButton(text="Uyqudan uyg'onganda"), KeyboardButton(text="Tahorat qilganda")],
        [KeyboardButton(text="Masjidga ketayotganda"), KeyboardButton(text="Masjidga kirayotganda va undan chiqayotganda")],
        [KeyboardButton(text="Azon va iqomatni eshitganda"), KeyboardButton(text="Namoz boshlaganda")],
        [KeyboardButton(text="Namozdagi rukuda"), KeyboardButton(text="Rukudan bosh ko'targanda va tik turganda")],
        [KeyboardButton(text="Sajda paytida"), KeyboardButton(text="Vitrdagi qunut duosi")],
        [KeyboardButton(text="Tashahhud"), KeyboardButton(text="Tashahhuddan keyingi salovotlar")],
        [KeyboardButton(text="Namoz tugaganda"), KeyboardButton(text="Kiyim kiyishda")],
        [KeyboardButton(text="Yangi kiyim kiyganda"), KeyboardButton(text="Kiyim yechilganda")],
        [KeyboardButton(text="Uydan chiqayotganda"), KeyboardButton(text="Uyga kirayotganda")],
        [KeyboardButton(text="Hojatxonaga kirayotganda"), KeyboardButton(text="Hojatxonadan chiqayotganda")],
        [KeyboardButton(text="Alloh taoloning go'zal 99 ismi"), KeyboardButton(text="Istixora qilganda")],
        [KeyboardButton(text="Qiyinchilik va g'amginlikda"), KeyboardButton(text="Biror narsadan qo'rqqanda")],
        [KeyboardButton(text="G'am yoki tashvish yetganida"), KeyboardButton(text="Qiyin ahvolga tushib qolganda")],
        [KeyboardButton(text="Bir qavmdan qo'rqqanda"), KeyboardButton(text="Sultondan qo'rqqanda")],
        [KeyboardButton(text="Dushmanga yo'liqqanda"), KeyboardButton(text="Bir ish og'irlik qilganida")],
        [KeyboardButton(text="Yashash qiyinlashganda"), KeyboardButton(text="Ofatni daf qilishda")],
        [KeyboardButton(text="Katta-kichik musibat yetganida"), KeyboardButton(text="Qarzini to'lashga qurbi yetmaganida")],
        [KeyboardButton(text="Biror narsadan qo'rqqanda"), KeyboardButton(text="Vasvasaga yo'liqqanda")],
        [KeyboardButton(text="Esi og'ganda va biror narsa chaqqanda"), KeyboardButton(text="Bolalarga panoh tilaganda")],
        [KeyboardButton(text="A'zolar yiringlaganda, yallig'langanda va narsa toshganda"), KeyboardButton(text="Kasal bo'lganda")],
        [KeyboardButton(text="Bosh og'rig'i, istma va boshqa og'riqlarda"), KeyboardButton(text="O'lim yaqinlashganda")],
        [KeyboardButton(text="Kishining yaqini vafot etganda"), KeyboardButton(text="Do'stning o'limi xabari yetganida")],
        [KeyboardButton(text="Janoza duosi"), KeyboardButton(text="Mayyit olib ketilayotganini ko'rganda")],
        [KeyboardButton(text="Mayyitni qabrga qo'yayotganda"), KeyboardButton(text="Ikkir hayit namozida aytiladigan takbir")],
        [KeyboardButton(text="Yomg'ir so'raladigan namozdagi zikrlar"), KeyboardButton(text="Qattiq shamol bo'lganda")],
        [KeyboardButton(text="Yulduz uchganda"), KeyboardButton(text="Yomg'irning zararidan qo'rqilganda")],
        [KeyboardButton(text="Hojat namozida"), KeyboardButton(text="Yangi chiqqan oyni ko'rganda")],
        [KeyboardButton(text="Iftor paytida"), KeyboardButton(text="Qadr kechasida")],
        [KeyboardButton(text="Haj uchun ehromga kirganda"), KeyboardButton(text="Talbiya aytganda")],

        [KeyboardButton(text="🔙orqaga")],
    ],
    resize_keyboard=True
)