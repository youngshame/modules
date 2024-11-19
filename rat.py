from .. import loader, utils

big_rat_url = "https://cpad.ask.fm/7e5/139b5/4032/4587/ba8c/14bc66f44ef1/large/244392.jpg"


@loader.tds
class BigRatMod(loader.Module):
    """Big rat"""
    strings = {"name": "Big rat"}

    async def ratcmd(self, message):
        """Usage: .rat (user)"""
        target = await self.get_target(message)
        if not target:
            return await message.edit("<b>Please specify who to rat.</b>")

        msg = await utils.answer(message, "<b>Sending big rat...</b>")
        await message.client.send_file(chat, big_rat_url)
        await utils.answer(msg, "<b>Sent big rat successfully!</b>")

    @staticmethod
    async def get_target(message):
        if message.chat_id > 0:
            return await message.client.get_entity(message.chat_id)
        args = utils.get_args_raw(message)
        if args:
            args = args.split()[0]
        reply = await message.get_reply_message()

        if not args and not reply:
            return None
        if reply and reply.from_id:
            return reply.from_id

        user = args if not args.isnumeric() else int(args)
        return await message.client.get_entity(user)
