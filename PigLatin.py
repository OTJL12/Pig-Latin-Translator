vowels = ["a", "e", "i", "o", "u"]

def pigLatinSentence(toTranslate):
    toTranslate = str(toTranslate).lower().split()
    output = ""
    for word in toTranslate:
        if word[0] in vowels:
            output += word + "way "
        else:
            for letter in word:
                if letter in vowels:
                    halfed = word.split(letter, 1)
                    output += letter + halfed[1] + halfed[0] + "ay "
                    break
    return output

print(pigLatinSentence("this is pig latin"))
print(pigLatinSentence("wall street journal"))

translateText = input("What do you want to translate to Pig Latin? ")
print("Translated text: "+pigLatinSentence(translateText))