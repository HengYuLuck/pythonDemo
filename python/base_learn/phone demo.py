class Phone:
    __is_5g_enable = False # 私有变量
    test = 'st'

    def _check_5g(self):
        if self.__is_5g_enable:
            print("5g已开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self._check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()