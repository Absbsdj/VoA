import base64
import contextlib
from asyncio import sleep

from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name

from . import mody

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format, get_user_from_event
from ..sql_helper import broadcast_sql as sql
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البوت"
LOGS = logging.getLogger(__name__)

ZE_BLACKLIST = [
    -1001236815136,
    -1001614012587,
    ]

DEVZ = [
    6673736816,
]
#

ModyPRO_cmd = (
    "𓆩 [🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 - اوامـر الاذا؏ـــة](t.me/UI_XB) 𓆪\n\n"
    "**⎞𝟏⎝** `.للكروبات`  / `.للمجموعات`\n"
    "**بالــࢪد ؏ــلى ࢪســالة نصيــة او وسـائــط تحتهــا نــص**\n"
    "**- لـ اذاعـة رسـالة او ميديـا لكـل المجموعـات اللي انت موجود فيهـا . .**\n\n\n"
    "**⎞𝟐⎝** `.للخاص`\n"
    "**بالــࢪد ؏ــلى ࢪســالة نصيــة او وسـائــط تحتهــا نــص**\n"
    "**- لـ اذاعـة رسـالة او ميديـا لكـل الاشخـاص اللي موجـودين عنـدك خـاص . .**\n\n\n"
    "**⎞𝟑⎝** `.خاص`\n"
    "**الامـر + معرف الشخص + الرسـاله . .**\n"
    " **- إرســال رسـاله إلـــى الشخص المحدد بدون الدخول للخاص وقراءة الرسـائل . .**\n\n\n"
    "**⎞4⎝** `.للكل`\n"
    "**بالــࢪد ؏ــلى ࢪســالة نصيــة او وسـائــط تحتهــا نــص**\n"
    " **- إرســال رسـاله اذاعـة إلـــى جميـع اعضـاء مجموعـة محددة .. قم باستخـدام الامـر داخـل المجموعـة . .**\n\n"
    "**⎞5⎝** `.زاجل`\n"
    "**بالــࢪد ؏ــلى ࢪســالة نصيــة او وسـائــط تحتهــا نــص**\n"
    " **- إرســال رسـاله اذاعـة إلـــى أشـخـاص محددة 🕊. .**\n\n"
    "\n 𓆩 [🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱](t.me/UI_XB) 𓆪"
)


# Copyright (C) 2023 ZE . All Rights Reserved
@mody.ar_cmd(pattern="م45")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ModyPRO_cmd)


@mody.ar_cmd(pattern=f"للكروبات(?: |$)(.*)")
async def gcast(event):
    SourceZe = event.pattern_match.group(1)
    if SourceZe: #Write Code By T.me/UP_UO
        await edit_or_reply(event, "**𓆰 بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    elif event.is_reply:
        mody = await event.get_reply_message()
    else:
        await edit_or_reply(event, "**𓆰 بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    zzz = await edit_or_reply(event, "**𓆰 جـاري الإذاعـة في المجموعـات ...الرجـاء الانتظـار**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if mody.text: #Write Code By T.me/UP_UO
                    try:
                        await borg.send_message(chat, mody, link_preview=False)
                        done += 1
                    except BaseException:
                        er += 1
                else:
                    try: #Write Code By T.me/UP_UO
                        await borg.send_file(
                            chat,
                            mody,
                            caption=mody.caption,
                            link_preview=False,
                        )
                        done += 1
                    except BaseException:
                        er += 1
            except BaseException:
                er += 1
    await zzz.edit(
        f"**𓆰 تمت الإذاعـة بنجـاح إلـى ** `{done}` **من المجموعـات** \n**𓆰 خطـأ في الإرســال إلـى ** `{er}` **من المجموعـات**"
    )

@mody.ar_cmd(pattern=f"للمجموعات(?: |$)(.*)")
async def gcast(event):
    SourceZe = event.pattern_match.group(1)
    if SourceZe: #Write Code By T.me/UP_UO
        await edit_or_reply(event, "**𓆰 بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    elif event.is_reply:
        mody = await event.get_reply_message()
    else:
        await edit_or_reply(event, "**𓆰 بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    zzz = await edit_or_reply(event, "**𓆰 جـاري الإذاعـة في المجموعـات ...الرجـاء الانتظـار**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if mody.text: #Write Code By T.me/UP_UO
                    try:
                        await borg.send_message(chat, mody, link_preview=False)
                        done += 1
                    except BaseException:
                        er += 1
                else:
                    try: #Write Code By T.me/UP_UO
                        await borg.send_file(
                            chat,
                            mody,
                            caption=mody.caption,
                            link_preview=False,
                        )
                        done += 1
                    except BaseException:
                        er += 1
            except BaseException:
                return
    await zzz.edit(
        f"**𓆰 تمت الإذاعـة بنجـاح إلـى ** `{done}` **من المجموعـات ، خطـأ في الإرســال إلـى ** `{er}` **من المجموعـات**"
    )
    
@mody.ar_cmd(pattern=f"للخاص(?: |$)(.*)")
async def gucast(event):
    SourceZe = event.pattern_match.group(1)
    if SourceZe: #Write Code By T.me/UP_UO
        await edit_or_reply(event, "**𓆰 بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    elif event.is_reply:
        mody = await event.get_reply_message()
    else:
        await edit_or_reply(event, "**𓆰 بالـࢪد ؏ــلى ࢪسـالة او وسائـط**")
        return
    zzz = await edit_or_reply(event, "**𓆰 جـاري الإذاعـة في الخـاص ...الرجـاء الانتظـار**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if mody.text: #Write Code By T.me/UP_UO
                    try:
                        await borg.send_message(chat, mody, link_preview=False)
                        done += 1
                    except BaseException:
                        return
                else:
                    try: #Write Code By T.me/UP_UO
                        await borg.send_file(
                            chat,
                            mody,
                            caption=mody.caption,
                            link_preview=False,
                        )
                        done += 1
                    except BaseException:
                        er += 1
            except BaseException:
                return
    await zzz.edit(
        f"**𓆰 تمت الإذاعـة بنجـاح إلـى ** `{done}` **من الخـاص**\n**𓆰 خطـأ في الإرســال إلـى ** `{er}` **من الخـاص**"
    )
    

@mody.ar_cmd(pattern="خاص ?(.*)")
async def pmto(event):
    r = event.pattern_match.group(1)
    p = r.split(" ")
    chat_id = p[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    mody = ""
    for i in p[1:]:
        mody += i + " "
    if mody == "":
        return
    try:
        await mody.send_message(chat_id, mody)
        await event.edit("**𓆰 تـم إرســال الرسـالة بنجـاح ✓**\n**𓆰 بـدون الدخـول للخـاص**")
    except BaseException:
        await event.edit("**𓆰 اووبس .. لقـد حدث خطـأ مـا .. اعـد المحـاولة**")
 
