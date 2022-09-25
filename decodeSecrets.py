import base64

writeOrNot = input ("Write in sonicbotDetectWord? (Y/N)\n")
if writeOrNot == "Y":
    write=True
    secrets = open("sonicbotDetectWord.txt","w",encoding = "utf-8").close()
    secrets = open("sonicbotDetectWord.txt","w",encoding = "utf-8")
else:
    write=False

with open('secrets.txt', 'r', encoding = "utf-8") as disallowWordFile:
    disallowWord = disallowWordFile.read().splitlines()

for encoded in disallowWord:
    #print(encoded)
    decodedText = base64.urlsafe_b64decode(encoded.encode('utf-8')).decode('utf8')
    print (decodedText)
    if write==True:
        secrets.write(decodedText)
        secrets.write('\n')