from aiogram import types

from keyboards.default.menu import *
from loader import dp,bot

import requests
from bs4 import BeautifulSoup

@dp.message_handler(text="🕋Namoz vaqti")
async def bot_echo(message: types.Message):
    await message.answer(message.text,reply_markup=namoz)

@dp.message_handler(text="Alloh taoloning go'zal 99 ismi")
async def bot_echo(message: types.Message):
    await message.answer('''A‘rof surasining 180-oyatida: «Allohning go‘zal ismlari bordir. Bas, Unga o‘sha (ism)lar ila duo qiling», deyilgan.
* Abu Hurayra roziyallohu anhudan rivoyat qilinadi:
Rasululloh sollallohu alayhi vasallam: «Alloh taoloning to‘qson to‘qqizta – bir kam yuzta ismi bor. Kim uni sanasa, jannatga kiradi. Alloh toqdir, toqni yaxshi ko‘radi», dedilar.
Bu hadisni shu yergacha Imom Buxoriy va Imom Muslim rivoyat qilgan. Davomida Imom Termiziy va boshqalar Alloh taoloning ismlarini keltirishgan:

  <b>هُوَ اللهُ الَّذِي لاَ إلَهَ إلاَّ هُوَ، الرَّحْمَنُ، الرَّحِيمُ، الْمَلِكُ، القُدُّوسُ، السَّلاَمُ، الْمُؤْمِنُ، الْمُهَيْمِنُ، العَزِيزُ، الْجَبَّارُ، الْمُتَكَبِّرُ، الْخَالِقُ، البَارِئُ، الْمُصَوِّرُ، الغَفَّارُ، القَهَّارُ، الوَهَّابُ، الرَّزَّاقُ، الفَتَّاحُ، العَلِيمُ، القَابِضُ، البَاسِطُ، الْخَافِضُ، الرَّافِعُ، الْمُعِزُّ، الْمُذِلُّ، السَّمِيعُ، البَصِيرُ، الْحَكَمُ، العَدْلُ، اللَّطِيفُ، الْخَبِيرُ، الْحَلِيمُ، العَظِيمُ، الغَفُورُ، الشَّكُورُ، العَلِيُّ، الكَبِيرُ، الْحَفِيظُ، الْمُقِيتُ، الْحَسِيبُ، الْجَلِيلُ، الكَرِيْمُ، الرَّقِيبُ، الْمُجِيبُ، الوَاسِعُ، الْحَكِيمُ، الوَدُودُ، الْمَجِيدُ، البَاعِثُ، الشَّهِيدُ، الْحَقُّ، الوَكِيلُ، القَوِيُّ، الْمَتِينُ، الوَلِيُّ، الْحَمِيدُ، الْمُحْصِي، الْمُبْدِيءُ، الْمُعِيدُ، الْمُحْيِي، الْمُمِيتُ، الْحَيُّ، القَيُّومُ، الوَاجِدُ، الْمَاجِدُ، الوَاحِدُ، الصَّمَدُ، القَادِرُ، الْمُقْتَدِرُ، الْمُقَدِّمُ، الْمُؤَخِّرُ، الأَوَّلُ، الآخِرُ، الظَّاهِرُ، البَاطِنُ، الوَالِي، الْمُتَعَالِ، البَرُّ، التَّوَّابُ، الْمُنْتَقِمُ، العَفُوُّ، الرَّؤُوفُ، مَالِكُ الْمُلْكِ، ذُو الْجَلاَلِ وَالإِكْرَامِ، الْمُقْسِطُ، الْجَامِعُ، الغَنِيُّ، الْمُغْنِي، الْمَانِعُ، الضَّارُّ، النَّافِعُ، النُّورُ، الْهَادِي، البَدِيعُ، البَاقِي، الوَارِثُ، الرَّشِيدُ، الصَّبُورُ. </b>

<b>1)  Alloh. 2) ar-Rahmon. 3) ar-Rahiym. 4)  al-Malik. 5) al-Quddus. 6)  as-Salom. 7)  al-Mo‘min. 8)  al-Muhaymin. 9) al-Aziz. 10)  al-Jabbor. 11)  al-Mutakabbir. 12)  al-Xoliq. 13)  al-Bori‘. 14)  al-Musavvir. 15)  al-G‘affor. 16)  al-Qahhor. 17)  al-Vahhob. 18)   ar-Razzoq. 19)  al-Fattoh. 20) al-Aliym. 21) al-Qobiz. 22) al-Bosit. 23) al-Xofiz. 24)  ar-Rofe‘. 25)  al-Mu‘izz. 26)  al-Muzill. 27) as-Samiy‘. 28) al-Basiyr. 29) al-Hakam. 30) al-Adl. 31) al-Latiyf. 32) al-Xabiyr. 33) al-Haliym. 34) al-Aziym. 35)  al-G‘afur. 36)  ash-Shakur. 37) al-Aliy. 38) al-Kabiyr. 39) al-Hafiyz. 40) al-Muqiyt. 41) al-Hasiyb. 42)  al-Jaliyl. 43) al-Kariym. 44) ar-Raqiyb. 45) al-Mujiyb. 46) al-Vose‘. 47) al-Hakiym. 48) al-Vadud. 49)  al-Majiyd. 50)  al-Bo‘is. 51)  ash-Shahiyd. 52) al-Haq. 53)  al-Vakiyl. 54)  al-Qaviy. 55)  al-Matiyn. 56)  al-Valiy. 57) al-Hamiyd. 58)al-Muhsiy. 59) al-Mubdi‘. 60) al-Mu‘iyd. 61)  al-Muhyi. 62)  al-Mumiyt. 63) al-Hayy. 64) al-Qayyum. 65) al-Vojid. 66) al-Mojid. 67) al-Vohid. 68) as-Somad. 69) al-Qodir. 70)  al-Muqtadir. 71)  al-Muqaddim. 72)  al-Muaxxir. 73)  al-Avval. 74)  al-Oxir. 75) az-Zohir. 76) al-Botin. 77) al-Voliy. 78) al-Muta‘oliy. 79) al-Barr. 80) at-Tavvob. 81) al-Muntaqim. 82) al-Afuvv. 83) ar-Ra`uf. 84) al-Molikul mulk. 85) Zul jaloli val ikrom. 86) al-Muqsit. 87) al-Jome‘. 88) al-G‘aniy. 89) al-Mug‘niy. 90) al-Mone‘. 91) az-Zorr. 92) an-Nofe‘. 93)  an-Nur. 94) al-Hodiy. 95) al-Badiy‘. 96) al-Boqiy. 97) al-Voris. 98) ar-Rashiyd. 99) as-Sabur.</b>''',reply_markup=home)

@dp.message_handler(text="Bomdod")
async def bot_echo(message: types.Message):
    link = "https://namozvaqti.uz/shahar/namangan"
    responcec = requests.get(link).text
    soup = BeautifulSoup(responcec, 'lxml')
    vaqti = soup.select(".time")[0].text
    await message.answer(f'''<b>Bomdod vaqti: {vaqti}</b>\n\nSubhi sodiqdan (chin tong otgandan) kun chiqqunchadir.
Bomdod namozini tong yorishganda o‘qish mustahab, a'loroqdir. Soat bo‘yicha hisoblansa, bomdodni kun chiqishidan 40 daqiqacha ilgari o‘qish mustahab vaqtiga muvofiq bo‘ladi.''',reply_markup=namoz)
@dp.message_handler(text="Quyosh")
async def bot_echo(message: types.Message):
    link = "https://namozvaqti.uz/shahar/namangan"
    responcec = requests.get(link).text
    soup = BeautifulSoup(responcec, 'lxml')
    vaqti = soup.select(".time")[1].text
    await message.answer(f"<b>Quyosh chiqish vaqti: {vaqti}</b>",reply_markup=namoz)
@dp.message_handler(text="Peshin")
async def bot_echo(message: types.Message):
    link = "https://namozvaqti.uz/shahar/namangan"
    responcec = requests.get(link).text
    soup = BeautifulSoup(responcec, 'lxml')
    vaqti = soup.select(".time")[2].text
    await message.answer(f'''<b>Peshin vaqti: {vaqti}</b>\n\nQuyosh zavolga (og‘ishga) kеtganidan so‘ng to narsalarning soyasi quyosh tikkaga kеlgan paytdagi so-yasidan tashqari o‘z uzunligiga nisbatan ikki baravar ortguniga qadar.
Pеshin namozini yoz faslida biroz kеchiktirib, qish faslida esa vaqti kirishi bilan o‘qish mustahabdir.''',reply_markup=namoz)
@dp.message_handler(text="Asr")
async def bot_echo(message: types.Message):
    link = "https://namozvaqti.uz/shahar/namangan"
    responcec = requests.get(link).text
    soup = BeautifulSoup(responcec, 'lxml')
    vaqti = soup.select(".time")[3].text
    await message.answer(f'''<b>Ars vaqti: {vaqti}</b>\n\nHar bir narsaning soyasi quyosh tikkaga kеlgan paytdagi soyasidan tashqari o‘ziga nisbatan ikki baravar ortganidan boshlab quyosh botgunchadir.
Asr namozini quyosh tig‘ini o‘zgartirmay, nursiz holatga kiri-shidan oldinroq o‘qish mustahabdir.''',reply_markup=namoz)
@dp.message_handler(text="Shom")
async def bot_echo(message: types.Message):
    link = "https://namozvaqti.uz/shahar/namangan"
    responcec = requests.get(link).text
    soup = BeautifulSoup(responcec, 'lxml')
    vaqti = soup.select(".time")[4].text
    await message.answer(f'''<b>Shom vaqti: {vaqti}</b>\n\nKun botgan paytdan boshlab kunbotar tomonda shafaq (qizg‘ish nurlar) g‘oyib bo‘lgunchadir.
Shom namozini doimo quyosh botishi bilan o‘qish mustahabdir.''',reply_markup=namoz)
@dp.message_handler(text="Xuftan")
async def bot_echo(message: types.Message):
    link = "https://namozvaqti.uz/shahar/namangan"
    responcec = requests.get(link).text
    soup = BeautifulSoup(responcec, 'lxml')
    vaqti = soup.select(".time")[5].text
    await message.answer(f'''<b>Xuftan vaqti: {vaqti}</b>\n\nShafaq batamom yo‘qolgandan kеyin kiradi.
Xufton namozini kеchaning uchdan birining oxirida o‘qish afzal va nihoyatda a'lo bo‘ladi.''',reply_markup=namoz)

@dp.message_handler(text="Vitr")
async def bot_echo(message: types.Message):
    await message.answer('''<b>Vitr namozi</b>\n\nXufton o‘qilgandan kеyingina kiradi. Xufton va vitr namozlarini subhi sodiqqacha o‘qisa bo‘ladi.
Vitr namozini tun oxirida uyg‘onishga qodir bo‘lgan kishilar subh oldidan o‘qisalar, mustahab amal qilgan bo‘lishadi.''',reply_markup=namoz)



@dp.message_handler(text="☪40 Farz")
async def bot_echo(message: types.Message):
    await message.answer('''Islomdagi 5 farz
1 Iymon;
2 Namoz;
3 Roʻza;
4 Zakot;
5 Haj.

📃Iymondagi 7 farz
1 Alloh taologa iymon keltirish;
2 Farishtalarga iymon keltirish;
3 Allohning kitoblariga iymon keltirish;
4 Paygʻambarlariga iymon keltirish;
5 Qiyomat kuniga iymon keltirish;
6 Yaxshilik va yomonlik ham Allohdan ekaniga iymon keltirish;
7 Oʻlgandan soʻng qayta tirilishga iymon keltirish.

📃Namozdagi 12 farz
Namozdan tashqaridagi 6 farz:
1 Namoz oʻquvchining badani katta va kichik betahoratlikdan pok boʻlishi;
2 Joyi pok boʻlishi;
3 Kiyimi pok boʻlishi va avratlarining berk boʻlishi;
4 Qiblani topishi;
5 Niyat;
6 Oʻz vaqtida oʻqish.

📃Namozning ichidagi 6 farz
1 Takbiri tahrima (Namoz avvalida aytiladigan, dunyo ishlarini harom qiluvchi “Allohu akbar” soʻzi);
2 Qiyomda turish;
3 Qiroat qilish;
4 Ruku;
5 Sajda;
6 Qaʼdai oxir (tashahhud miqdorida oʻtirish).

📃Tahoratdagi 4 farz
1 Yuzning soch chiqqan joyidan iyakning ostigacha va ikki quloq yumshoqlarining oralarini bir marta yuvish;
2 Ikki qoʻlning chigʻanoqlari bilan bir marta yuvish;
3 Boshning toʻrtdan biriga masʼh tortish;
4 Ikki oyoqning toʻfiqlari bilan bir boradan yuvish.

📃Tayammumdagi 4 farz
1 Namoz oʻqishni niyat qilib tayammum qilish;
2 Toza tuproqni qasd qilishi; (yer jinsidan boʻlgan, tuproq, tosh, qum kabilar)
3 Ikki qoʻlini tuproqqa urib yuziga masx tortish;
4 Ikki qoʻlini yana urib ikkala qoʻlining chigʻanoqlarini qoʻshib masx tortish.

📃Gʻusldagi 3 farz
1 Ogʻizga suv olib yuvish;
2 Burunga suv olib yuvish;
3 Butun badanga suv yetkazib yuvish.

📃Amru maʼrufdagi 1 farz
Yaxshi amallarni oʻzi bajarib, boshqalarga ham buyurish.

📃Nahiy munkardagi 1 farz
Yomon amallardan avval oʻzi saqlanib boshqalarni ham qaytarish.

📃Hayzdagi 1 farz
Hayz hukmlarini bilish. Hayz kunlarining ozi uch kun, koʻpi oʻn kun. Hayzdan pok yurishning eng ozi oʻn besh kun, koʻpining chegarasi yoʻq.
Hayz kunlarida namoz oʻqilmaydi, roʻza tutmaydi, jinsiy aloqa qilmaydi. Hayz toʻxtashi bilan gʻusl qilib poklanib namozini davom ettiradi, roʻzasini tutadi. Hayzli kunlarining namozlarini qayta oʻqimaydi. Roʻzaning qazolarini tutadi. Hayzli ayol Qurʼon tilovat qilmaydi, Musʼhafni ushlamaydi va Kaʼbani tavof qilmaydi.

📃Ilm izlashdagi 1 farz
Ilm izlash, oʻqish farz. Inson hayoti davomida kerak boʻladigan halol-haromga doir ilmlarni oʻzlashtirishi farzdir.

© G'ofurov Abdulhodi''', reply_markup=home)

@dp.message_handler(text="Og'iz berkitish duosi🤲")
async def bot_echo(message: types.Message):
    ms_id = message.from_user.id
    rasm_manzili = "https://t.me/Boqi_Mirzo_Jome_Masjidi/4"
    await bot.send_photo(chat_id=ms_id,photo=rasm_manzili,caption="<b>Og'iz berkitish duosi</b>\n\nنَوَيْتُ أَنْ أَصُومَ صَوْمَ شَهْرَ رَمَضَانَ مِنَ الْفَجْرِ إِلَى الْمَغْرِبِ، خَالِصًا لِلهِ تَعَالَى أَللهُ أَكْبَرُ\n\n<b>Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi taʼaalaa Allohu akbar</b>.\n\nManosi: Ramazon oyining roʻzasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.", reply_markup=home)

@dp.message_handler(text="Og'iz ochish duosi🤲")
async def bot_echo(message: types.Message):
    ms_id = message.from_user.id
    rasm_manzili = "https://t.me/Boqi_Mirzo_Jome_Masjidi/5"
    await bot.send_photo(chat_id=ms_id,photo=rasm_manzili,caption="<b>Og'iz ochish duosi</b>\n\nاَللَّهُمَّ لَكَ صُمْتُ وَ بِكَ آمَنْتُ وَ عَلَيْكَ تَوَكَّلْتُ وَ عَلَى رِزْقِكَ أَفْتَرْتُ، فَغْفِرْلِى مَا قَدَّمْتُ وَ مَا أَخَّرْتُ بِرَحْمَتِكَ يَا أَرْحَمَ الرَّاحِمِين\n\n<b>Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.</b>\n\nManosi: Ey Alloh, ushbu Roʻzamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning yeng mehriboni, mening avvalgi va keyingi gunohlarimni magʻfirat qilgil.", reply_markup=home)
@dp.message_handler(text="📿Zikr va duolar🤲")
async def bot_echo(message: types.Message):
    await message.answer("🛠Bu bo'lim hozircha ta'mirda🛠",reply_markup=duolar_zikrlar)

@dp.message_handler(text="Adminga yozish✍")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f'''Assalomu alaykum hurmatli foydalanuvchi botning kamchiligi yoki sizning bot bo'yicha takliflaringiz bo'lsa iltimos adminga yozib qoldiring sizning fikringiz biz uchun muhim!!!\n\nMurojat uchun!!!\n\n<b>ADMIN: @Abdulhodi_2007</b>''',reply_markup=home)
    text = f"{message.from_user.get_mention()} Dan Xabar Keldi\n\n"

@dp.message_handler(text="Tong va kechqurunda")
async def bot_echo(message: types.Message):

    await message.answer(f'''Abu Hurayra roziyallohu anhudan rivoyat qilinadi:
Rasululloh sollallohu alayhi vasallam: «Kim ertalab yoki kechqurun:
 
<b>سُبْحَانَ اللهِ وَبِحَمْدِهِ</b>
 
«Subhanallohi va bihamdihi», (Allohga hamd aytish bilan Uni aybu nuqsonlardan poklab yod etaman) deb yuz marta aytsa, qiyomat kuni biror kishi undan afzal bo‘lmaydi. Faqat ana shu kishi aytganidek yoki undan oshirib aytsagina, bo‘lishi mumkin», dedilar. 
Imom Muslim rivoyati.
Abu Dovudning rivoyatida:

<b>سُبْحَانَ اللهِ العَظِيمِ وَبِحَمْدِهِ </b>
«Subhanallohil ‘aziym va bihamdihi», deb kelgan.

Rasululloh sollallohu alayhi vasallam qizlarining biridan rivoyat qilinadi. U zot qizlariga tong otganida:

<b>سُبْحَانَ اللهِ وَبِحَمْدِهِ لاَ قُوَّةَ إِلاَّ بِاللهِ مَا شَاءَ اللهُ كَانَ وَمَا لَمْ يَشَأْ لَمْ يَكُنْ، أَعْلَمُ أَنَّ اللهَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ، وَأَنَّ اللهَ قَدْ أَحَاطَ بِكُلِّ شَيْءٍ عِلْمًا</b>

«Subhanallohi va bihamdihi, la quvvata illa billahi maasha`allohu kana va maa lam yasha` lam yakun. A‘lamu annalloha ‘ala kulli shay‘in qodiyr. Va annalloha qod ahato bikulli shay`in ‘ilma», deb aytishni o‘rgatar edilar. Chunki bu kalimalarni tong otganida aytgan kishi kech kirgunicha muhofaza qilinadi. Kech kirganida aytsa, tong otgunicha muhofaza etiladi.
Ma‘nosi: Allohga hamd aytish bilan Uni poklab yod etaman. Allohdan boshqada  quvvat yo‘q. Alloh xohlagan narsa bo‘ladi. Xohlamagan narsa bo‘lmaydi. Bilamanki, Alloh har bir narsaga qodirdir. Va, albatta, Alloh har bir narsani ilmi bilan ihota qilgandir.
Abu Dovud rivoyati.''',reply_markup=duolar_zikrlar)

@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''Anas roziyallohu anhudan rivoyat qilinadi:
Rasululloh sollallohu alayhi vasallam: «Kim juma kuni bomdod namozidan oldin:

  <b>أسْتَغْفِرُ اللهَ الَّذِي لاَ إِلَهَ إِلاَّ هُوَ الْحَيُّ القَيُّومُ وَأَتُوبُ إِلَيْهِ</b>

<b>«Astag‘firullohallaziy laa ilaha illaa huval hayyul qoyyum va atubu ilayh», deb uch marta aytsa, Alloh taolo uning gunohlarini dengiz ko‘pigicha bo‘lsa ham, kechirib yuboradi», dedilar.</b>

Ma‘nosi: Hay va qayyum sifatli Zotdan boshqa iloh yo‘q va Unga istig‘for aytaman, Unga tavba qilaman.
Ibn Sunniy rivoyati.''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Uxlashdan oldin")
async def bot_echo(message: types.Message):
    await message.answer('''Abu Hurayra roziyallohu anhudan rivoyat qilinadi:
Rasululloh sollallohu alayhi vasallam:
«Kishi to‘shakka yotayotganida ko‘rpa va izorini qoqib tashlasin. Chunki uning orasida nima borligini bilmaydi. So‘ng: 

<b>بِاسْمِكَ رَبِّي وَضَعْتُ جَنْبِي وَبِكَ أَرْفَعُهُ إِنْ أَمْسَكْتَ نَفْسِي فَارْحَمْهَا وَإِنْ أرْسَلْتَهَا فَاحْفَظْهَا بِمَا تَحْفَظُ بِهِ عِبَادَكَ الصَّالِحِينَ</b>

<b>«Bismika robbiy vazo‘tu jambiy va bika arfa‘uhu, in amsakta nafsiy farhamha va in arsaltaha fahfazha bimaa tahfazu bihi ‘ibadakas solihiyn», deb aytsin», dedilar.</b>

Ma‘nosi: Ey Robbim, Sening isming bilan yotdim va Sening isming bilan turaman. Agar mening ruhimni olsang, unga rahm qil. Agar uni qo‘yib yuborsang, xuddi solih bandalaringni saqlaganingdek, uni ham hifzu himoyangga ol.
Imom Buxoriy va Muslim rivoyati.

* Oisha roziyallohu anho aytadilar:
«Rasululloh sollallohu alayhi vasallam to‘shaklariga yotsalar, qo‘llariga suflab, ikkita «Qul a‘uzu»ni o‘qir, so‘ng tanalariga surtar edilar».
Imom Buxoriy va Muslim rivoyati.''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)
@dp.message_handler(text="Juma tongida")
async def bot_echo(message: types.Message):
    await message.answer('''''',reply_markup=duolar_zikrlar)




@dp.message_handler(text="🔙orqaga")
async def bot_echo(message: types.Message):
    await message.answer("Bosh sahifa",reply_markup=home)
# import requests
# from bs4 import BeautifulSoup as BS

# def bugun(viloyat):
#     link = f"https://namozvaqti.uz/shahar/{viloyat}"
#     r = requests.get(link).text
#     soup = BS(r,"html.parser")
#     bugun = soup.select(".vil")[0].text
#     return bugun
#
# def hozirgi(viloyat):
#     link = f"https://namozvaqti.uz/shahar/{viloyat}"
#     r = requests.get(link).text
#     soup = BS(r,"html.parser")
#     bugun = soup.select(".current_time")[0].text
#     return bugun
#
# def bomdod(viloyat):
#     link = f"https://namozvaqti.uz/shahar/{viloyat}"
#     r = requests.get(link).text
#     soup = BS(r,"html.parser")
#     bugun = soup.select(".time")[0].text
#     return bugun
# def quyosh(viloyat):
#     link = f"https://namozvaqti.uz/shahar/{viloyat}"
#     r = requests.get(link).text
#     soup = BS(r,"html.parser")
#     bugun = soup.select(".time")[1].text
#     return bugun
#
# def peshin(viloyat):
#     link = f"https://namozvaqti.uz/shahar/{viloyat}"
#     r = requests.get(link).text
#     soup = BS(r,"html.parser")
#     bugun = soup.select(".time")[2].text
#     return bugun
#
# def asr(viloyat):
#     link = f"https://namozvaqti.uz/shahar/{viloyat}"
#     r = requests.get(link).text
#     soup = BS(r,"html.parser")
#     bugun = soup.select(".time")[3].text
#     return bugun
#
# def shom(viloyat):
#     link = f"https://namozvaqti.uz/shahar/{viloyat}"
#     r = requests.get(link).text
#     soup = BS(r,"html.parser")
#     bugun = soup.select(".time")[4].text
#     return bugun
#
# def xufton(viloyat):
#     link = f"https://namozvaqti.uz/shahar/{viloyat}"
#     r = requests.get(link).text
#     soup = BS(r,"html.parser")
#     bugun = soup.select(".time")[5].text
#     return bugun