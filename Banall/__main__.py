import os
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from . import bot 
from Banall import STARTED, FINISH, ERROR, OWN_UNAME
from datetime import datetime
from time import time


@bot.on_message(filters.group & filters.command("banall"))
def main(_, msg: Message):
    chat = msg.chat
    me = chat.get_member(bot.get_me().id)
    if chat.get_member(msg.from_user.id).can_manage_chat and me.can_restrict_members and me.can_delete_messages:
        try:
            msg.reply(STARTED.format(chat.members_count))
            count_kicks = 0
            for member in chat.iter_members():
                if not member.can_manage_chat:
                    bot.ban_chat_member(chat_id=msg.chat.id, user_id=member.user.id)
                    count_kicks += 1
            msg.reply(FINISH.format(count_kicks))
        except Exception as e:
            msg.reply(ERROR.format(str(e)))
    else:
        msg.reply("i need to be admin In This Group To Perform This Action!")


@bot.on_message(filters.group & filters.service, group=2)
def service(c, m):
    m.delete()


@bot.on_message(filters.private)
def start(_, msg: Message):
    msg.reply_photo(
                    photo="https://telegra.ph/file/b2704f702734610934b9c.jpg", 
                    caption="Hi, I'm a Banall Robot to help you remove all users from your group.\nNow add me to a group and don't forget to give me the permissions.\nThen send /banall in the group and I will start my work.", 
                    reply_markup=InlineKeyboardMarkup(
                                                      [
                                                       [
                                                        InlineKeyboardButton("Source", url="https://www.github.com/TheDeCode/BanAllBot"), 
                                                        InlineKeyboardButton("Support", url="https://t.me/TheeDeCode")                                      
                                                       ], 
                                                       [
                                                        InlineKeyboardButton("Update", url="https://t.me/OfficialDeCode"), 
                                                        InlineKeyboardButton("Creator", url="https://t.me/DeCodeDevs")                                      
                                                       ], 
                                                       [
                                                        InlineKeyboardButton("Owner", url=f"https://t.me/{OWN_UNAME}")                                                                                              
                                                       ]                                                     
                                                      ]
                                                     )
)

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@bot.on_message(filters.command(["ping"]
async def ping(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>I'm Online🍀</b> `{delta_ping * 1000:.3f} ms` \n<b>⏳Uptime </b> - `{uptime}`"
    )

    
bot.run()
idle()

print("Done BanAll Started...") 
print("Join @TheeDeCode || @OfficialDeCode For Help") 
