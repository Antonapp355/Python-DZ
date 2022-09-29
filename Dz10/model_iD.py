import json

def iD_name():
    with open("book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    spisok_ID = []
    i = 0
    if data != [[{"RID":0}, {"RФ.И.О": ""}, {"Rтел.": ""}]]:
        for e in data:
            for q in e:
                if "RID" in q:
                    continue
                elif "ID" in q:
                    spisok_ID.append(q["ID"])
                    i+=1
        max_ID = max(spisok_ID)
    else:
        max_ID = 0
    return max_ID+1