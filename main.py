meme_dict = {
    "РОФЛ ": "шутка",
    "ЩИЩ ": "одобрение или восторг"
}

word = input()
if word in meme_dict.keys():
    print(meme_dict[word])
else: 
    print("Такого слово нету!!!")
