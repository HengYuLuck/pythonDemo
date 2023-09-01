str1 = 'sadfdasfasdf'
str2 = '12adfsads'
str3 = 'helloworld'

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")

my_len(str1)
my_len(str2)
my_len(str3)
