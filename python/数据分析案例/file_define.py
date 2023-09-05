from typing import List

from 数据分析案例.date_define import Record


class FileRenderer:
    def read_data(self) -> List[Record]:
        pass


class TextFileReader(FileRenderer):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> List[Record]:
        records = []
        with open(self.path, "r", encoding="UTF-8") as f:
            for line in f.readlines():
                line = line.strip()  # 去除换行符
                fields = line.split(",")  # 假设数据以逗号分隔

                # 检查字段数量是否正确
                if len(fields) != 4:
                    print(f"Ignoring line: {line}")
                    continue

                date, order_id, money, province = fields
                record = Record(date, order_id, int(money), province)  # 转换金额为整数类型
                records.append(record)
        return records


if __name__ == '__main__':
    text_file_reader = TextFileReader("/Users/hengyu/Desktop/workspace/test.txt")
    records = text_file_reader.read_data()
    for record in records:
        print(record)  # 假设 Record 类实现了 __str__ 方法来打印记录