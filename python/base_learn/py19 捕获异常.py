try:
    f = open("d:/abc.text", "r", encoding="UTF-8")
except:
    print("出现异常了，因为文件不存在，我将 open 的模式")
    f = open("py15", "r", encoding="UTF-8")
