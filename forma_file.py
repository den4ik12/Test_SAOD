import re


class Questions:
    def __init__(self, id, title, questions):
        self.title = title
        self.id = id
        self.q = questions


def read_file():
    file = open("vopr.txt", "r", encoding="utf-8")
    text = file.read()
    file.close()
    return text


def write_file(data):
    file = open("saod_test.txt", "w", encoding="utf-8")
    for item in data:
        file.write("ID = {}\nTitle = {}\nВопросы = {}\n\n".format(item.id, item.title, item.q))
    file.close()


def format_file(text, lst):
    text.strip()
    text_cst = text.split("}")
    for text in text_cst:
        if text_cst[len(text_cst) - 1] == text:
            continue
        id = re.search("question: \d{0,10}", text)
        id = re.search("\d+", id.group(0)).group(0)
        title = re.findall("name: (.+)", text)
        answer = re.findall("	(.+)\n", text)
        lst.append(Questions(int(id), title, answer))
    return lst


def get_base():
    lst = []
    text = read_file()
    lst = format_file(text, lst)
    sort_list = sorted(lst, key=lambda x: int(x.id), reverse=False)
    # write_file(sort_list)
    return sort_list
