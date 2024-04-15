import requests
import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from SourceZe import mody
from . import mody
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "البوت"


# code by t.me/UP_UO
@mody.ar_cmd(pattern="زد إي(?: |$)(.*)")
async def zelzal_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    chat = "@V4JRBOT" #code by t.me/UP_UO
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**𓆰بالـرد ع سـؤال او باضـافة السـؤال للامـر**\n**𓆰مثـــال :**\n`.ريفز من هو مكتشف الجاذبية الارضية`")
    if not zilzal and event.reply_to_msg_id and zzz.text: #code by t.me/UP_UO
        zelzal = zzz.text
    if not event.reply_to_msg_id: #code by t.me/UP_UO
        zelzal = event.pattern_match.group(1)
    zed = await edit_or_reply(event, "**𓆰جـارِ الاتصـال بـ الذكـاء الاصطنـاعـي\n𓆰الرجـاء الانتظـار .. لحظـات**")
    async with borg.conversation(chat) as conv: #code by t.me/UP_UO
        try:
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/UP_UO
                aa = ahmed.replace("⏳ Please wait another 30 seconds before sending the next question . . .", "**𓆰يُرجى الانتظار 8 ثوانٍ ⏳\n𓆰بين إرسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "understanding" in zedthon.text: #code by t.me/UP_UO
                aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await zed.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {zelzal}\n\n{malath}**\n\n───────────────────\n𝐙𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓**** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\t@UI_XB • ᴼᵖᵉⁿᴬᴵ")
        except YouBlockedUserError: #code by t.me/UP_UO
            await mody(unblock("V4JRBOT"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/UP_UO
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**𓆰يُرجى الانتظار 8 ثوانٍ ⏳\n𓆰بين إرسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "understanding" in zedthon.text: #code by t.me/UP_UO
                aa = malath.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            if "Please wait a moment" in zedthon.text: #code by t.me/UP_UO
                await asyncio.sleep(5)
                zedthon = await conv.get_response()
                malath = zedthon.text
            await zed.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {zelzal}\n\n{malath}**\n\n───────────────────\n𝐙𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓**** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\t@UI_XB • ᴼᵖᵉⁿᴬᴵ")


# تخمــط اهينـــك Fuk-You

# code by t.me/UP_UO
@mody.ar_cmd(pattern="ذك(?: |$)(.*)")
async def zelzal_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    chat = "@V4JRBOT" #code by t.me/UP_UO
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**𓆰بالـرد ع سـؤال او باضـافة السـؤال للامـر**\n**𓆰مثـــال :**\n`.ريفز من هو مكتشف الجاذبية الارضية`")
    if not zilzal and event.reply_to_msg_id and zzz.text: #code by t.me/UP_UO
        zelzal = zzz.text
    if not event.reply_to_msg_id: #code by t.me/UP_UO
        zelzal = event.pattern_match.group(1)
    zed = await edit_or_reply(event, "**𓆰جـارِ الاتصـال بـ الذكـاء الاصطنـاعـي\n𓆰الرجـاء الانتظـار .. لحظـات**")
    async with borg.conversation(chat) as conv: #code by t.me/UP_UO
        try:
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/UP_UO
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**𓆰يُرجى الانتظار 8 ثوانٍ ⏳\n𓆰بين إرسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "understanding" in zedthon.text: #code by t.me/UP_UO
                aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            if "Please wait a moment" in zedthon.text: #code by t.me/UP_UO
                await asyncio.sleep(5)
                zedthon = await conv.get_response()
                malath = zedthon.text
            await zed.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {zelzal}\n\n{malath}**\n\n───────────────────\n𝐙𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓**** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\t@UI_XB • ᴼᵖᵉⁿᴬᴵ")
        except YouBlockedUserError: #code by t.me/UP_UO
            await mody(unblock("GPT4Telegrambot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/UP_UO
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**𓆰يُرجى الانتظار 8 ثوانٍ ⏳\n𓆰بين إرسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "understanding" in zedthon.text: #code by t.me/UP_UO
                aa = malath.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await zed.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {zelzal}\n\n{malath}**\n\n───────────────────\n𝐙𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓**** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\t@UI_XB • ᴼᵖᵉⁿᴬᴵ")
