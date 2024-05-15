#created by @tunchichi

from .. import loader, utils
from asyncio import sleep


@loader.tds
  class ratMod(loader.Module):
	  """rat"""
	  strings = {'name': 'rat'}
	@loader.owner
	async def ratcmd(self, message_id):
