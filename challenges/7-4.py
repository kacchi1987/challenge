answer = [1, 11, 23, 58]
while True:
    a = input("input number. \"q\" is quit")
    if a == "q":
        print("終了します")
        break
    elif a.isdecimal():
        a = int(a)
        if a in answer:
            print("正解")
        else:
            print("不正解")
    else:
        print("数字を入力するか、qで終了します")
