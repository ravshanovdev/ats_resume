from aiogram import types, Router
from aiogram.filters import Command
from asgiref.sync import sync_to_async


router = Router()


@router.channel_post()
async def start_cmd(msg: types.Message):
    print(msg.chat.id)
    await msg.bot.send_message(
        chat_id=-1003418801315,
        text='"bot ishlayapti"'
    )







