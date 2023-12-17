from tkinter import *
from random import shuffle
from copy import copy
import time


def clear():
    canvas = Canvas(root, bg='#FFFFFF', width=800, height=800, bd=0)
    canvas.place(x=0, y=0)


def train(words):
    clear()

    def p(_):
        pass

    def ent8(_):
        fi.set(1)

    def english_to_russian(eng, rus, words, r=False):
        def right(_='-'):
            clear()
            text = Label(root, text='Correct!', fg='green', bg='#FFFFFF', font=('Calibri', 20))
            text.place(x=150, y=50)
            e_l = Label(root, text=eng + ' - ' + rus, font=('Calibri', 15), bg=wte)
            e_l.place(x=150, y=100)
            so = Label(root, text=words_sounds.get(eng, ' '), bg=wte, font=('Calibri', 15))
            so.place(x=150, y=150)
            nonlocal fin
            root.update()
            root.bind('<Return>', p)
            time.sleep(1)
            fin.set(1)

        def wrong(_='-'):
            def en3(_):
                fin.set(1)
            clear()
            text = Label(root, text='Incorrect!', fg='red', bg='#FFFFFF', font=('Calibri', 20))
            text.place(x=150, y=50)
            e_l = Label(root, text=eng + ' - ' + rus, font=('Calibri', 15), bg=wte)
            e_l.place(x=150, y=100)
            so = Label(root, text=words_sounds.get(eng, ' '), bg=wte, font=('Calibri', 15))
            so.place(x=150, y=150)
            root.update()
            nonlocal fin, wrong_words
            if r:
                wrong_words.add(rus)
            else:
                wrong_words.add(eng)
            root.bind('<Return>', en3)

        variants = {rus}
        i = 0
        words = list(words)
        while (len(variants) != 4) and (len(variants) != len(words)):
            variants.add(words[i])
            i += 1
        mainWord = Label(root, text=eng + " " + words_sounds.get(eng, ""), bg=wte,  font=('Calibri', 17))
        mainWord.place(x=150, y=50)
        for i in range(len(variants)):
            n = variants.pop()
            sis1 = 15 if len(n) <= 15 else len(n)
            x = Button(root, text=str(i+1)+ ' '+ n, highlightcolor='green', bg='lightgreen', activebackground='green',
                       bd=1, height=2, width=sis1, font=('Calibri', 14))
            if n == rus:
                x['command'] = right
                root.bind(str(i+1), right)
            else:
                x['command'] = wrong
                root.bind(str(i+1), wrong)
            x.place(x=(i % 2)*180+50, y=(i >= 2)*70+100)
        root.update()

    def annogram(eng, rus):
        def ent4(_):
            fin.set(1)

        def right(_):
            nonlocal i, lr, ans
            la = Label(root, text=lr[i].upper(), bg=wte, fg='green', font=('Calibri', 23))
            la.place(x=300-(len(eng)*23/2 - len(rus)*15/2) + 25*i, y=110)
            ans.set(1)

        def not_right(_):
            nonlocal le, wrong_words
            le['fg'] = 'red'
            root.update()
            time.sleep(0.4)
            le['fg'] = 'black'
            root.update()
            wrong_words.add(eng)
        clear()
        l = list(eng)
        lr = list(eng)
        shuffle(l)
        word_rus = Label(root, text=rus, bg='#FFFFFF', font=('Calibri', 15))
        word_rus.place(x=300, y=30)
        le = Label(root, text=(' '.join(l)).upper(), bg='#FFFFFF', font=('Calibri', 20))
        le.place(x=300-(len(eng)*20/2 - len(rus)*15/2), y=70)
        for i in range(len(lr)):
            n = 'abcdefghijklmnopqrstuvwxyz'
            ans = IntVar()
            root.bind(lr[i], right)
            for j in n.replace(lr[i], '/'):
                root.bind(j, not_right)
            root.update()
            root.wait_variable(ans)
        root.update()
        fin = IntVar()
        root.bind('<Return>', ent4)
        so = Label(root, text=words_sounds[eng], font=('Calibri', 15), bg=wte)
        so.place(x=300, y=160)
        ent = Label(root, text='enter --->', bg=wte, fg='green', font=('Calibri', 12))
        ent.place(x=500, y=160)
        root.wait_variable(fin)

    def write_sound(eng, rus):
        def check(_):
            def ent5(_):
                ans.set(1)
            an = ent.get()
            clear()
            if an == eng:
                la = Label(root, text='Correct!', fg='green', bg=wte, font=('Calibri', 15))
                la.place(x=150, y=50)
                en = Label(root, text=eng+' - '+rus, bg=wte, font=('Calibri', 15))
                en.place(x=150, y=80)
                s = Label(root, text=words_sounds[eng], font=('Calibri', 15), bg=wte)
                s.place(x=150, y=110)
            else:
                rig = Label(root, text=eng, bg=wte, font=('Calibri', 15), fg='green')
                rig.place(x=150, y=50)
                your_ans = Label(root, text=an, bg=wte, fg='red', font=('Calibri', 15))
                your_ans.place(x=150, y=80)
                s = Label(root, text=words_sounds[eng], font=('Calibri', 15), bg=wte)
                s.place(x=150, y=110)
                wrong_words.add(eng)
            root.bind('<Return>', ent5)
            root.update()

        clear()
        l = Label(root, text=rus, bg=wte, font=('Calibri', 15))
        l.place(x=150, y=50)
        ent = Entry(root, bg=wte, font=('Calibri', 15))
        ent.place(x=150, y=80)
        ent.focus()
        root.bind('<Return>', check)
        ans = IntVar()
        root.update()
        root.wait_variable(ans)

    wrong_during_all = set()
    wrong_words = set()
    for i in words:
        root.bind('<Return>', p)
        fin = IntVar()
        clear()
        english_to_russian(i, words[i], words.values())
        root.wait_variable(fin)
    wrong_during_all = wrong_during_all.union(wrong_words)
    while len(wrong_words) != 0:
        copy_wrong = copy(wrong_words)
        wrong_words = set()
        root.bind('<Return>', p)
        for i in copy_wrong:
            fin = IntVar()
            clear()
            english_to_russian(i, words[i], words.values())
            root.wait_variable(fin)
    for j in words:
        root.bind('<Return>', p)
        fin = IntVar()
        clear()
        english_to_russian(words[j], j, words.keys(), r=True)
        root.wait_variable(fin)
    wrong_during_all = wrong_during_all.union(wrong_words)

    while len(wrong_words) != 0:
        root.bind('<Return>', p)
        copy_wrong = copy(wrong_words)
        wrong_words = set()
        for i in copy_wrong:
            fin = IntVar()
            clear()
            english_to_russian(words[i], i, words.keys(), r=True)
            root.wait_variable(fin)
    for a in words:
        clear()
        annogram(a, words[a])
    wrong_during_all = wrong_during_all.union(wrong_words)
    while len(wrong_words) != 0:
        copy_wrong = copy(wrong_words)
        wrong_words = set()
        for i in copy_wrong:
            clear()
            annogram(i, words[i])
    n = 'abcdefghijklmnopqrstuvwxyz'
    for letter in n:
        root.bind(letter, p)
    for s in words:
        clear()
        write_sound(s, words[s])
    wrong_during_all = wrong_during_all.union(wrong_words)
    a = 0
    while len(wrong_words) != 0:
        copy_wrong = copy(wrong_words)
        wrong_words = set()
        for i in copy_wrong:
            clear()
            write_sound(i, words[i])
        a += 1
        if a == 2:
            break
    for word in wrong_during_all:
        words_time[word] = time.time()
        words_how_much[word] = -1
    clear()
    y1 = 0
    for word in words:
        w = Label(root, text=word, bg=wte, font=('Calibri', 15), fg='green')
        if word in wrong_during_all:
            w['fg'] = 'red'
        w.place(x=50, y=50 + 30*y1)
        y1+=1
    fi = IntVar()
    root.bind('<Return>', ent8)
    root.wait_variable(fi)
    clear()
    main_screen()


def choose_words():
    def enter2(_):
        yes.set(1)
    clear()
    words_to_train = dict()
    new = False
    if words_for_now:
        a = 0
        for i in copy(words_for_now):
            words_to_train[i] = words_for_now[i]
            del words_for_now[i]
            a += 1
            if a == 5:
                break

    else:
        with open('dict.txt', encoding='utf-8') as d:
            elses = dict()
            for i in range(5):
                line = d.readline()
                if line == '':
                    error = Label(root, text='Нет слов для изучения, пожалуйста, добавьте слова', bg=wte, font=('Calibri', 15))
                    error.place(x=100, y=50)
                    break
                eng, rus, sound = line.split()
                words_to_train[eng] = rus
                words_for_r[eng] = rus
                words_time[eng] = time.time()
                words_sounds[eng] = sound
                words_how_much[eng] = 0
            for word in d:
                eng, rus, sound = word.split()
                elses[eng] = [rus, sound]
        new = True

    show = Label(root, text='Now you will train this words:', bg=wte, font=('Calibri Light', 17))
    show.place(x=50, y=10)
    r = 1
    for i in words_to_train:
        a = Label(root, text=i, bg=wte, font=('Calibri', 13), fg='green')
        b = Label(root, text=' - ' + words_to_train[i], bg=wte, font=('Calibri', 13))
        a.place(x=100, y=30*r+20)
        b.place(x=100+len(i)*10, y=30*r+20)
        r += 1
    root.update()
    ent = Label(root, text='enter --->', bg=wte, fg='green', font=('Calibri', 12))
    ent.place(x=500, y=160)
    yes = IntVar()
    root.bind('<Return>', enter2)
    root.wait_variable(yes)
    train(words_to_train)
    for word in words_to_train:
        words_how_much[word] += 1
    if new:
        with open('dict.txt', 'w', encoding='utf-8') as d:
            for word in elses:
                d.write(' '.join([word, elses[word][0], elses[word][1]]) + '\n')


def add():
    clear()
    def right_func(_):
        nonlocal i
        if i % 3 == 0:
            entryRus.focus()
        elif i % 3 == 1:
            entryTrans.focus()
        else:
            entryEng.focus()
        i += 1

    def enter(_):
        eng = entryEng.get()
        rus = entryRus.get()
        trans = entryTrans.get()

        with open('dict.txt', 'a', encoding='utf-8') as f:
            f.write(eng + " " + rus + " " + trans + '\n')
        root.update()

        fine = Label(root, text='Successfully added!', bg=wte, fg='green')
        fine.place(x=450, y=70)
        root.update()

        time.sleep(0.5)
        fine['fg'] = wte

        entryEng.delete(0, 'end')
        entryRus.delete(0, 'end')
        entryTrans.delete(0, 'end')
        entryEng.focus()
        root.update()
    entryEng = Entry(root, bd=3)
    entryRus = Entry(root, bd=3)
    entryTrans = Entry(root, bd=3)
    entryEng.focus()

    entryEng.place(x=30, y=70)
    entryRus.place(x=170, y=70)
    entryTrans.place(x=310, y=70)

    labelEng = Label(root, text='English', bg=wte)
    labelRus = Label(root, text='Russian', bg=wte)
    LabelTrans = Label(root, text='Transcription', bg=wte)

    labelEng.place(x=30, y=40)
    labelRus.place(x=170, y=40)
    LabelTrans.place(x=310, y=40)

    i = 1
    root.bind('<Right>', right_func)
    root.bind('<Return>', enter)
    print('æ ɔ ʌ ə ɵ ð ʒ ʃ ʤ ŋ')


def main_screen():
    global first
    if first:
        with open('wait_for_train.txt', encoding='utf-8') as f:
            t_sr = time.time()
            for word in f:
                eng, rus, sound, t, h = word.split()
                t = float(t)
                h = int(h)
                words_time[eng] = t
                words_for_r[eng] = rus
                words_sounds[eng] = sound
                words_how_much[eng] = h
                if (((12*60*60 < t_sr-t) and (h < 2))
                        or ((7*24*60*60 < t_sr-t) and (h < 3))
                        or ((30*24*60*60 < t_sr-t) and (h<4))
                        or ((60*24*60*60 < t_sr-t) and (h < 5))):
                    words_for_now[eng] = rus
    if words_for_now:
        f1 = Label(root, text='Привет! Сегодня тебе нужно повторить эти слова:', bg=wte, font=('Calibri', 15))
    else:
        f1 = Label(root, text='Привет! Сегодня тебе не нужно повторять слова :)', bg=wte, font=('Calibri Light', 15))
    f1.place(x=10, y=10)
    r = 1
    for word in words_for_now:
        m = Label(root, text=word, bg=wte, font=('Calibri', 13), fg='green')
        m2 = Label(root, text=' - ' + words_for_now[word], bg=wte, font=('Calibri', 13))
        m.place(x=30, y=30*r+20)
        m2.place(x=30+len(word)*10, y=30*r+20)
        r += 1
    first = False
    root.update()


def exit():
    with open('wait_for_train.txt', 'w', encoding='utf-8') as f:
        j = 0
        for i in words_for_r:
            if j == 0:
                f.write(' '.join([i, words_for_r[i], words_sounds[i], str(words_time[i]), str(words_how_much[i])]))
            else:
                f.write('\n' + ' '.join([i, words_for_r[i], words_sounds[i], str(words_time[i]), str(words_how_much[i])]))
            j += 1
    root.destroy()



root = Tk()
root.geometry('700x600')
root.configure(bg='#FFFFFF')
root.title("Simple English")
wte = '#FFFFFF'
mennu = Menu(root)
root.config(menu=mennu)
mennu.add_command(label='add', command=add)
mennu.add_command(label='train', command=choose_words)

words_for_r = {}
words_time = {}
words_for_now = {}
words_sounds = {}
words_how_much = {}
first = True
root.protocol("WM_DELETE_WINDOW", exit)
main_screen()
root.mainloop()
