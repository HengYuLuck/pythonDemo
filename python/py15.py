my_list = [1, 2, 3, 4, 5, 6, 7]
result1 = my_list[1:4]
print(result1)

my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]
print(f"结果是:{result2}")

my_str = '01234567'
result3 = my_str[::2]
print(result3)

result4 = my_str[::-1]
print(result4)

result5 = my_str[3:1:-1]
print(result5)