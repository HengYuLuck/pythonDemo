class Phone:
    __current_voltage = 0.5# 当前手机运行电压

    def __keep_single_core(self):
        print("让 cpu 以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print(f"5g 已经开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用 5g 通话，并已设置为单核运行进行省电。")

phone = Phone()
phone.call_by_5g()