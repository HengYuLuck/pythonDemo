my_str = "ittheima itcast boxuegu"
num = my_str.count("it")
print(f"字符串{my_str}中有{num}个 it 字符")
new_my_str = my_str.replace(" ","｜")
print(new_my_str)
my_str_list = new_my_str.split("｜")
print(f"分割后的结果，我的第一个 list是：{my_str_list}")