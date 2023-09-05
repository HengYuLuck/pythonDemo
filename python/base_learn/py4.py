age = int(input("请输入您的年龄"))
vip_level = int(input("请输入您的级别"))
if age < 18:
    print("您可以免费游玩")
elif vip_level >= 3:
    print("您的 vip 等级大于 3 可以免费游玩")
elif int(input("请告诉我今天星期几")) == 1:
    print("恭喜您答对了，可以免费游玩")
else:
    print("抱歉，您需要补缴 10 元")