import re

def trans():
    with open("dict.txt", "r", encoding="utf-8") as fp:
        content = fp.read()
        for i, v in re.findall("(.*): (.*)", content):
            cont = '"{}":"{}",'.format(i, v)
            print(cont)

if __name__ == '__main__':
    trans()