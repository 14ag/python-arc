import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################clean twitter hashtags########################################

tags = [" Python ", "coding", "#DataScience", " ", "sql "]


def cleaner(arg):
    clean_list=[]

    for i in range(0,len(arg)):
        tag=tags[i]
        
        count_spaces=tag.count(" ")
        tag_length=len(tag)

        if count_spaces == tag_length:
            continue

        tag=tag.strip().lower()
        
        if not tag.startswith("#"):
            tag="#"+tag

        clean_list.append(tag)
    return clean_list


tags=cleaner(tags)

print(tags)