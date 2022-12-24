import base64

secrets = open("secrets.txt","w",encoding = "utf-8").close()
secrets = open("secrets.txt","w",encoding = "utf-8")
with open('sonicbotDetectWord.txt', 'r', encoding = "utf-8") as disallowWordFile:
    disallowWord = disallowWordFile.read().splitlines()

for encodeLine in disallowWord:
    encodeText = base64.b64encode(encodeLine.encode('utf8'))
    encoded=str(encodeText,'utf-8')
    secrets.write(encoded)
    secrets.write('\n')
    print(encoded)
    print(base64.urlsafe_b64decode(encoded.encode('utf-8')).decode('utf8'))
    
print("Encode Done")
