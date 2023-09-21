from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 模拟表格数据（示例数据）
table_data = [
    {"id": 1, "name": "John", "age": 30},
    {"id": 2, "name": "Alice", "age": 25},
    {"id": 3, "name": "Bob", "age": 35},
    # 可以添加更多数据
]

@app.route('/table/data', methods=['GET'])
def get_table_data():
    # 在实际应用中，这里通常会查询数据库或其他数据源来获取表格数据
    # 这里我们直接返回示例数据
    response_data = {
        "code": 200,  # 成功的响应码
        "msg": "Success",  # 成功的消息
        "data": table_data  # 表格数据作为 data 字段
    }
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True, port=8083)  # 将端口更改为8083