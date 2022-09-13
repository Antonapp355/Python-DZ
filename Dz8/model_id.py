import json

# ID для name_book
def iD_name():
    with open("name_book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    spisok_ID = []
    i = 0
    if data != []:
        for e in data:
            spisok_ID.append(data[i]["ID"])
            i+=1
        max_ID = max(spisok_ID)
    else:
        max_ID = 0
    return max_ID+1

# ID для post_book
def iD_Post():
    with open("post_book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    spisok_ID = []
    i = 0
    if data != []:
        for e in data:
            spisok_ID.append(data[i]["ID"])
            i+=1
        max_ID = max(spisok_ID)
    else:
        max_ID = 0
    return max_ID+1

# ID для office_book
def iD_Office():
    with open("office_book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    spisok_ID = []
    i = 0
    if data != []:
        for e in data:
            spisok_ID.append(data[i]["ID"])
            i+=1
        max_ID = max(spisok_ID)
    else:
        max_ID = 0
    return max_ID+1