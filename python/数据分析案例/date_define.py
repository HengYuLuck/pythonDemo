class Record:
    date = None
    order_id = None
    money = None
    province = None

    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province
