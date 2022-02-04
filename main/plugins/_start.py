#Github.com/Vasusen-code

st = """Buraya klonlamak için herhangi bir mesajın bağlantısını gönder, Özel kanal mesajı için önce davet bağlantısını gönder.

Yardım: @trbotlistesidestek
Geliştirici: @trbotlistesi"""

import os
from .. import bot as Drone
from telethon import events, Button

from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Bu Mesaja 'Yanıt' Olarak Küçük Resim İçin Bana Herhangi Bir Resim Gönder.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("Medya Bulunamadı.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("Resim Bulunamadı.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Deniyor.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Thumbnail Kaydedildi!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Drone = event.client            
    await event.edit('Deniyor.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Kaldırıldı!')
    except Exception:
        await event.edit("Küçük Resim Kaydedilmedi.")                        
  
@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    await event.reply(st, 
                      buttons=[
                              [Button.inline("Kapak Ayarla.", data="set"),
                               Button.inline("kapak Kaldır.", data="rem")],
                              [Button.url("Geliştirici", url="t.me/trbotlistesi")]])
                              
    
    
    
    
    
    
    
    
    
    
    
    
    
    
