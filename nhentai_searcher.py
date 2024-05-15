#Create users seesonrise for @wich1
#My github github.com/seesonrise
#Github @wich1 github.com/wich1
#This module has a Copyright please do not copy this code


from .. import loader, utils
from asyncio import sleep
import random

@loader.tds
class HentaiMod(loader.Module):
	"""Дает рандомную ссылку на nhetai"""
	strings = {'name': 'Hentai Module'}
	@loader.owner
	async def nhcmd(self,message):
		"""Начать поиск"""
		await utils.answer(message,"Поиск хентыча")
		await sleep(1)
		for _ in range(3):
			for search in ['Поиск.','Поиск..','Поиск...']:
				await utils.answer(message,search)
				await sleep(1) 
		await sleep(1) 
		await utils.answer(message,"Ваш хентай")
		await sleep(1)
		x = random.randint(1,383041) 
		url ="nhentai.net/g/"+ str(x)
		await utils.answer(message,url)
