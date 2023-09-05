def list_while_fn():
    my_list = ["传智播客", "黑马程序媛", "Python"]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表的元素：{element}")
        index += 1


list_while_fn()

def list_for_fn():
    my_list = ["传智播客", "黑马程序媛", "Python"]
    for i in my_list:
        element = i
        print(element)
list_for_fn()