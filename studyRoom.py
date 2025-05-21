class MyClass:
    def __init__(self):
        self._single_underscore = "单下划线变量,hhh"  # 约定为内部使用
        self.__double_underscore = "双下划线变量,hhh2"  # 名称改写

obj = MyClass()
print(obj._single_underscore)  # 可以访问，但这是内部使用的,尽管python不限制访问
# print(obj.__double_underscore)  # 会报错，因为名称被改写了
print(obj._MyClass__double_underscore)  # 可以通过改写后的名称访问