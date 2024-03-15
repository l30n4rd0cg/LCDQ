from os import system

VERSION: str = "1.3"
LANG: str = "fr.txt"

langFile = open("lang.txt", "r", encoding = "utf8")
print(langFile.read())
langFile.close()

lang = input()
if lang == "2":
    LANG = "es.txt"
elif lang == "3":
    LANG = "en.txt"
elif lang == "C":
    LANG = "cu.txt"
    try:
        _ = open(LANG)
        _.close()
    except:
        print("ERROR: No custom language.")
        LANG = "fr.txt"

textFile = open(LANG, "r", encoding = "utf8")
texts = list(map(lambda s: s[:-1], textFile.readlines()))
textFile.close()

questions: list = []

def sure(repeatIfAny: bool) -> bool:
    global texts
    
    while True:
        inp = input(texts[10]).capitalize()
        if inp == texts[21][0]:
            return True
        elif inp == texts[20][0]:
            return False
        if not repeatIfAny:
            return False

def list_questions(delete: bool = True):
    global questions
    
    if questions == []:
        if delete:    
            print(texts[17])
        else:
            print(texts[18])
        return True
    
    for q in range(len(questions)):
        print(f" {q + 1} {questions[q][0]}")
    
    return False

def action():
    global texts
    global questions
    
    print()

    list_questions(False)
    
    print()
    
    print(*texts[4:10], sep = "\n")
    
    option: str = input()

    if option == "1":
        return 1
    if option == "2":
        if list_questions():
            return 1
        q_str = input(texts[11])
        try:
            q_num = int(q_str)
            if q_num < 1 or q_num > len(questions):
                raise Exception
        except:
            print(texts[12])
            return 1
        if sure(False):
            print(texts[13].format(questions.pop(q_num - 1)[0]))
        else:
            print(texts[14])
        return 1
    if option == "3":
        if sure(False):
            questions = []
            print(texts[15])
        else:
            print(texts[14])
        return 1
    if option == "4":
        if sure(False):
            return 0
        else:
            print(texts[14])
            return 1
    if option == "5":
        if sure(False):
            exit(0)
        else:
            print(texts[14])
            return 1
    print(texts[12])
    return 1

def toHTML(q) -> str:
    global texts

    qu = q[0]
    r = q[1:4]
    rc = q[4]
    
    ret = f"<h2 style='font-family:\"Urbanist\";'>{qu}</h2><ul>"
    
    for rn in range(3):
        if rn + 1 == rc:
            txt = texts[21]
        else:
            txt = texts[20]
        ret += f"<li><button style='font-family:\"Urbanist\";' onclick='alert(\"{txt}\")'>{r[rn]}</button></li>"
    
    return ret + "</ul><br/>"

print(f"{texts[0]} [v. {VERSION}]", end = "\n\n")

while True:
    question = input(texts[1])
    if question == "":
        act = action()
        if act == 0:
            print()
            break
        elif act == 1:
            print()
            continue
    answers = []
    for i in range(1, 4):
        answers.append(input(texts[2].format(i)))
    try:
        correct_answer = int(input(texts[3]))
        if correct_answer not in range(1, 4):
            raise Exception
    except:
        print(texts[12])
        continue
    questions.append([
        question,
        *answers,
        correct_answer
    ])
    print(texts[16])

back_color = input(texts[22])
text_color = input(texts[23])

base_file = open("base.html", "r", encoding = "utf8")
base_text = base_file.read()
base_file.close()

output_file = open(texts[19], "w", encoding = "utf8")

html_body = ""

for q in questions:
    html_body += toHTML(q)

output_file.write(base_text.format(
    body = html_body,
    back_color = back_color,
    text_color = text_color
))

output_file.close()

system(texts[19])