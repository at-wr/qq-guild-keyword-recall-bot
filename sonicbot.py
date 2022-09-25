import botpy
from botpy.types.message import Message
import base64

# 违禁词检测
disallowWord = []
with open('secrets.txt', 'r', encoding = "utf-8") as disallowWordFile:
    encodedDisallowWord = disallowWordFile.read().splitlines()
for encoded in encodedDisallowWord:
    #print (encoded)
    decodedText = base64.urlsafe_b64decode(encoded.encode('utf-8')).decode('utf8')
    disallowWord.append(decodedText)
    #print (decodedText)
#print (disallowWord)    
class MyClient(botpy.Client):
    async def on_message_create(self, message: Message):
        for detectDisallowWord in disallowWord:
            if detectDisallowWord in message.content:
                await self.api.recall_message(message.channel_id, message.id, hidetip=True) # 若 hidetip=False，则将不会隐藏撤回记录。目前建议设为 False。

# 监听频道消息事件
intents = botpy.Intents(guild_messages=True) #仅私域机器人能实现
client = MyClient(intents=intents)

# 配置机器人 AppID 与 Token
client.run(appid="", token="")
