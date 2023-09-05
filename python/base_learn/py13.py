my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

# for i in my_list:
#     if i % 2 == 0:
#         new_list.append(i)
# print(new_list)

index = 0
while index < len(my_list):
    if my_list[index] % 2 == 0:
        new_list.append(my_list[index])
    index += 1
print(new_list)
