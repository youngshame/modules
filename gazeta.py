#created by @wich1

from .. import loader, utils
from asyncio import sleep


@loader.tds
class GazetaMod(loader.Module):
	"""Мем (Китайская газета)"""
	strings = {'name': 'Gazeta'}
	@loader.owner
	async def gazetacmd(self, message_id):
		await utils.answer(message, " Китайская газета -Хуй вам, хуй нам- ")
		await asyncio.sleep(4)
		await utils.answer(message, " сообщает - что Француский король ")
		await asyncio.sleep(4)
		await utils.answer(message, " Трипер второй выдаёт свою дочь, Ля Курву Дэ Бля Ве ")
		await asyncio.sleep(4)
		await utils.answer(message, " замуж за французского подданого Дон-Дон Штопаный Гандон. ")
		await asyncio.sleep(4)
		await utils.answer(message, " На пир были приглашены ")
		await asyncio.sleep(4)
		await utils.answer(message, " с Румынской стороны Залупыська, ")
		await asyncio.sleep(4)
		await utils.answer(message, " с русской Иван-Пиздарван, ")
		await asyncio.sleep(4)
		await utils.answer(message, " с грузинской Целкаламидзе, ")
		await asyncio.sleep(4)
		await utils.answer(message, " с китайской Сунь Хуй в Чай? ")
		await asyncio.sleep(4)
		await utils.answer(message, " Вынь Сухим и дай подержать другим. ")
		await asyncio.sleep(4)
		await utils.answer(message, " На обед были поданы - супы горячие, хуи стаоячие. ")
		await asyncio.sleep(4)
		await utils.answer(message, " После обеда был просмотр фильма ")
		await asyncio.sleep(4)
		await utils.answer(message, " -Не одна я в поле кувыркалась, не одной мне ветер в жопу дул-. ")
		await asyncio.sleep(4)
		await utils.answer(message, " После этого был показ спектакля ")
		await asyncio.sleep(4)
		await utils.answer(message, " -Как батька Махно выставил жопу в окно-. ")
		await asyncio.sleep(4)
		await utils.answer(message, " И после этого была пропета украиньска народна письня ")
		await asyncio.sleep(4)
		await utils.answer(message, " -Ох, да залупылась на хую шкурынка- ")
		await asyncio.sleep(4)
		await utils.answer(message, " Сегоднешняя газета зкончилась ")#пасхалочка