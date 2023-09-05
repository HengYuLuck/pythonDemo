"""
  注释用法
"""
user_name = "\"音乐鱼\""
print(user_name)

user_age = 18
has_money = 10000
desc = "我的名字是：" + user_name + "我的年龄是：%s , 我的工资是%s" % (user_age,has_money)
print(desc)

point_number = 11.12345
print("结果：%0.3f" % point_number)

print(f"我是音乐🐟{user_name}") # 适合对精度没有要求的时候进行快速格式化