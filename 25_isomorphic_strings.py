import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################isomorphic strings########################################

def isIsomorphic(s_string,t_string):
    char_map={}
    x=len(s_string)

    for i in range(x):
        if not s_string[i] in char_map.keys():
            if not t_string[i] in char_map.values():
                char_map[s_string[i]]=t_string[i]
            else:
                return False
        else:
            if char_map[s_string[i]]!=t_string[i]:
                return False
        
    return True

print(isIsomorphic("egg","add"))
print(isIsomorphic("foo","bar"))
print(isIsomorphic("paper","title"))
print(isIsomorphic("badc","baba"))

