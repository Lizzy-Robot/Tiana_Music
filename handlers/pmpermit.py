from callsmusic.callsmusic import client as USER

from pyrogram import filters

from pyrogram.types import Chat, Message, User

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)

async def pmPermit(client: USER, message: Message):

  await USER.send_message(message.chat.id,"Hi there, This is a music assistant service of @AnishaPro_RoBot .\n\n ❗️ Rules:\n   - No chatting allowed,if you want to chat with this user then message at [Raksha](https://t.me/Raksha_Backup)\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN'T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you are sending a message here it means admin will see your message and join chat\n    - Don't add this user to secret groups.\n   - Don't Share private info here\n\n")")

  return
