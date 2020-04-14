import json
import random

with open('../data/idiom.json') as f:
  data = json.load(f)
chars = dict()
vowel_list = ["a", "o", "e", "i", "u", "v", " ", "g"]

chars["a"] = ["ā", "á", "ǎ", "à"] 
chars["o"] = ["ǒ", "ò", "ó", "ō"]
chars["e"] = ["é", "ě", "è", "ē"]
chars["i"] = ["ī", "í", "ì", "ǐ"]
chars["u"] = ["ū", "ú", "ǔ", "ù"]
chars["v"] = [str(chr(252)), str(chr(470)), str(chr(472)), str(chr(474)), str(chr(476))]
chars[" "] = ["，", ",", "1", str(chr(12288)), "?", "@", str(chr(12289))]
chars["g"] = [str(chr(609))]

found = False
new_data = list()
# while found is False:
for rand_int in range(len(data)):
    # rand_int = random.randint(0, len(data) - 1)
    rand_str = data[rand_int]["pinyin"]
    rand_word = data[rand_int]["word"]
    # print(rand_int)
    # print(rand_word)
    new_str = ""
    for i in range(len(rand_str)):
        c = str(rand_str[i])
        ok = False
        for vowel in vowel_list:
            if c in chars[vowel]:
                new_str += vowel
                ok = True
                break
        if ok is False:
            new_str += c

    new_dict = dict()
    new_dict["word"] = rand_word
    new_dict["english"] = new_str
    new_data.append(new_dict)

with open('../data/idiom-basic.json', 'w+') as outfile:
    json.dump(new_data, outfile)

    """
    for i in range(len(new_str)):
        str2i = 0
        try:
            str2i = ord(new_str[i])
            if (str2i != 0x20) and (str2i < ord('a') or str2i > ord('z')):
                print(new_str[i], str2i)
                print(rand_word)
                found = True
                break
        except:
            print(new_str)
    """

"""
for idiom in data:
    if idiom['english'][-1] == " ":
        print(idiom)
    if idiom['english'][0] == " ":
        print(idiom)

"""
