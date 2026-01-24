import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################ransom note########################################

def ransomeNote(note, magazine):
    letter_freq0={} #magazine
    letter_freq1={} #notes
    
    for i in magazine:
        if not i in letter_freq0:
            letter_freq0[i]=1
        else:
            letter_freq0[i]+=1

    for i in note:
        if not i in letter_freq1:
            letter_freq1[i]=1
        else:
            letter_freq1[i]+=1

    for key in letter_freq1:

        if key in letter_freq0:
            if not letter_freq1[key]==letter_freq0[key]:
                return False
        else:
                return False
        
    return True



print(ransomeNote("a","b"))
print(ransomeNote("aa","ab"))
print(ransomeNote("aa","aab"))