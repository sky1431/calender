import calendar as cl1
import datetime
import datetime as dt1
import random
import tkinter as tk1
from PIL import ImageTk, Image
import glob
import os

import jpholiday


def generate_calendar1(y1, m1):
    global wd1
    global cal1
    for i1 in range(len(cal1)):
        cal1[i1] = ""
    date1 = dt1.date(y1, m1, 1)
    wd1 = date1.weekday()
    if wd1 > 5:
        wd1 = wd1 - 7
    cal_max1 = cl1.monthrange(y1, m1)[1]
    for i1 in range(cal_max1):
        str1 = str(i1 + 1)
        i2 = i1 + wd1 + 1
        cal1[i2] = str1


# 祝日表示
def get_holiday(day_str):
    if day_str == '':
        return None
    m2 = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November",
          "December"]
    result = jpholiday.is_holiday_name(
        datetime.date(int(label_year["text"]), int(m2.index(label_month_name["text"])) + 1, int(day_str)))
    return result


def set_calendar1(cal1, btn_day):
    for i1 in range(len(cal1)):
        str1 = cal1[i1]
        btn_day[i1]["text"] = str1
        # 祝日表示↓↓↓
        if get_holiday(str1) is not None:
            fg0 = "#FF0000"
            btn_day[i1]["text"] = str1 + " " + get_holiday(str1)
        elif i1 % 7 == 0:
            fg0 = "#FF0000"
        elif i1 % 7 == 6:
            fg0 = "#0000A0"
        else:
            fg0 = "#000000"
        btn_day[i1]["fg"] = fg0


def prev_next1(n1):
    global y1
    global m1
    global btn_day
    m2 = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November",
          "December"]
    m1 = m1 + n1
    if m1 > 12:
        y1 = y1 + 1
        m1 = 1
    elif m1 < 1:
        y1 = y1 - 1
        m1 = 12
    label_month["text"] = str(m1)
    label_month_name["text"] = m2[m1 - 1]
    label_year["text"] = str(y1)
    generate_calendar1(y1, m1)
    set_calendar1(cal1, btn_day)

    img_cat["file"] = "img/cat" + str(random.randint(1, 20)) + ".png"
    lbl_cat["image"] = img_cat
    lbl_cat.place(x=0, y=0)

def btn_click_day():
    return

def memo_save():
    with open("memo.txt", mode='w') as file:
        file.write(memo.get(1.0, 100.0))

root = tk1.Tk()
# タイトル変更
root.title(u"my_calendar")
root.geometry("1255x730+100+100")
root["bg"] = "#EEEEE8"
# フォント変更
label_month = tk1.Label(font=("DIN 2014", 35), anchor=tk1.CENTER, width=2)
label_month["bg"] = "#EEEEE8"
label_month.place(x=50 +500, y=3)
# フォント変更
label_month_name = tk1.Label(font=("DIN 2014", 10), anchor=tk1.W, width=10)
label_month_name["bg"] = "#EEEEE5"
label_month_name.place(x=120 +500, y=8)
# フォント変更
label_year = tk1.Label(font=("DIN 2014", 12), anchor=tk1.W, width=10)
label_year["bg"] = "#EEEEE8"
label_year.place(x=120 +500, y=25)

label_week = [""] * 7
a1 = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for i1 in range(7):
    # フォント変更
    label_week[i1] = tk1.Label(text=a1[i1], font=("DIN 2014", 9), anchor=tk1.CENTER, width=10)
    label_week[i1]["bg"] = "#EEEEE8"
    label_week[i1].place(x=30 + 103 * i1 +500, y=55)

btn_day = [""] * 42
for i1 in range(6):
    for i2 in range(7):
        fg1 = "#000000"
        if i2 == 0:
            bg1 = "#FFF0F0"
            fg1 = "#FF0000"
        elif i2 == 6:
            bg1 = "#F6F0FF"
            fg1 = "#0000A0"
        else:
            bg1 = "#FFFFFF"
        btn_day[i2 + 7 * i1] = tk1.Button(root, font=("DIN 2014", 11), anchor=tk1.NW, bg=bg1, fg=fg1, relief='flat', command=btn_click_day)
        x2 = 20 + 103 * i2
        y2 = 75 + i1 * 73
        btn_day[i2 + 7 * i1].place(x=x2 +500, y=y2, width=100, height=70)
# フォント変更
btn_back = tk1.Button(root, text="<", font=("DIN 2014", 15), bg="#D0D0D0", relief='flat',
                  command=lambda: prev_next1(-1))
btn_back.place(x=600 +500, y=8, width=60, height=30)
# フォント変更
btn_next = tk1.Button(root, text=">", font=("DIN 2014", 15), bg="#D0D0D0", relief='flat',
                  command=lambda: prev_next1(1))
btn_next.place(x=680 +500, y=8, width=60, height=30)

now1 = dt1.datetime.now()
y1 = now1.year
m1 = now1.month
d1 = now1.day
wd1 = 0
cal1 = [""] * 40

#画像
#list=glob.glob('img/*.jpeg')
#data=random.choice(list)
#data1=os.path.split(data)[1]
#img_cat = ImageTk.PhotoImage(file="img/cat" + str(random.randint(1, 20)) + ".jpeg")
img_cat = tk1.PhotoImage(file="img/cat" + str(random.randint(1, 20)) + ".png")
lbl_cat = tk1.Label(root, image=img_cat, bd=0, width=500, height=500)
lbl_cat.place(x=0, y=0)

#TODOメモ
with open("memo.txt") as f:
    str_memo = f.read()
memo = tk1.Text(background='#FFFFFF', fg="#595959", font=("DIN 2014", 20))
memo.insert(1.0, str_memo)
memo.place(x=520, y=3 + 510, width=720, height=210)

#メモ保存ボタン
btn_memo_save = tk1.Button(root, text="save", font=("DIN 2014", 11), bg="#D0D0D0", relief='flat',
                  command=memo_save)
btn_memo_save.place(x=520 + 660, y=3 +510 + 180, width=60, height=30)


prev_next1(0)

root.mainloop()