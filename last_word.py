import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################length of last word########################################

def lengthOfLastWord(sentence):
    LOLW=len(sentence.strip().split()[-1])
    return LOLW


print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord(" fly me to the moon "))
print(lengthOfLastWord("luffy is still joyboy"))

