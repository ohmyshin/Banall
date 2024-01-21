import asyncio

from pyrogram import idle

from . import bot



async def main():
    await asyncio.gather(bot.start())



if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
