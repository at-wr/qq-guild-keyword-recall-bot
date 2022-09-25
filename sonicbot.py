import botpy
#from botpy import logging
from botpy.types.message import Message
import base64

# 违禁词检测
disallowWord = []
with open('secrets.txt', 'r', encoding = "utf-8") as disallowWordFile:
    encodedDisallowWord = disallowWordFile.read().splitlines()
for encoded in encodedDisallowWord:
    #print(encoded)
    decodedText = base64.urlsafe_b64decode(encoded.encode('utf-8')).decode('utf8')
    disallowWord.append(decodedText)
    #print(decodedText)
#print (disallowWord)    
class MyClient(botpy.Client):
    async def on_message_create(self, message: Message):
        """
        此处为处理该事件的代码
        """
        '''if "sleep" in message.content:
            await asyncio.sleep(10)
        await message.reply(content=f"消息信息: {message.content}  消息ID: {message.id}")
        await self.api.recall_message(channel_id=message.channel_id, message_id="{message.id}", hidetip=false)'''
        #_message = await message.reply(content=f"机器人{self.robot.name}收到你的@消息了: {message.content}")
        for detectDisallowWord in disallowWord:
            if detectDisallowWord in message.content:
                await self.api.recall_message(message.channel_id, message.id, hidetip=True)
    #async def on_message_delete(self, message: Message):
        """
        此处为处理该事件的代码
        """

# 监听频道消息事件
intents = botpy.Intents(guild_messages=True) #仅私域机器人能实现
client = MyClient(intents=intents)

# 配置机器人 AppID 与 Token
client.run(appid="", token="")
