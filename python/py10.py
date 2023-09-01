def check():
    print("欢迎来到黑马程序员！")
    print("你好！")
    num = input("请输入体温:")
    if int(num) > 37.5:
        print("温度过高")
    else:
        print("没问题")
check()